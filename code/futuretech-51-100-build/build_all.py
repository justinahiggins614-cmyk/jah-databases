#!/usr/bin/env python3
"""Build futuretech database pairs 51-100 for the JAH Databases 10,000-target program.

Each technology gets ONE public + ONE Signature database pair, 34 ladder-ordered
records each, tracing the technology from its oldest/earliest form to the working
version (or, for speculative technologies, to the current research frontier).

Usage:
    python3 build_all.py --batch techs-51-60.json
    python3 build_all.py --only futuretech-rapid-lithium-extraction
    python3 build_all.py --all

Writes:
    ~/workspace/jah-databases/db/<slug>/index.html
    ~/workspace/jah-databases/db/<slug>/gen-<slug>.js
    ~/workspace/jah-databases-data-1/data/<slug>/index.jsonl.gz
    ~/workspace/jah-databases-data-1/data/<slug>/chunks/chunk-0000.jsonl.gz
    ~/workspace/jah-databases/code/<slug>-build/{data.json,build.sh}

Gates (fail the build on any violation):
    - 34 records per database, ladder_rank 1..34
    - every demo program machine-executed and passing
    - node --check on every generated gen script
    - dedupe: titles unique within batch and against the whole system
    - content gates: blocklist scan, no Facebook/website references, medical safety notes
"""
import json, gzip, os, re, sys, subprocess, html as htmlmod, io, contextlib, pickle

ROOT_DB = os.path.expanduser('~/workspace/jah-databases')
ROOT_DATA = os.path.expanduser('~/workspace/jah-databases-data-1')
BUILD_DIR = os.path.join(ROOT_DB, 'code', 'futuretech-51-100-build')
DATA_DOMAIN = 'https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/'
TIER_COUNTS = [9, 9, 8, 8]

BLOCKLIST = ['fuck', 'shit', 'bitch', 'cunt', 'nigger', 'faggot', 'whore', 'slut',
             'dick', 'pussy', 'porn', 'xxx', 'kill yourself', 'suicide',
             'facebook', 'Facebook', 'FACEBOOK']
# "cure" is blocked only for medical techs (no cure claims)
CURE_RE = re.compile(r'\b[cC]ures?\b')

SCHEMA_LINE = ("Record schema: id, t, g, name, title, description, how_it_works, "
               "key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo.")
MATURITY_LINE = ("Maturity labeling: established / emerging / research / speculative. "
                 "Speculative records are Signature-labeled and never presented as established fact.")
CREDIT_LINE = ("The {name} Database - records organized in the Signature system. "
               "Property of Justin Addam Higgins (JAH).")


def fail(msg):
    print('BUILD FAIL:', msg, file=sys.stderr)
    sys.exit(1)


def check(cond, msg):
    if not cond:
        fail(msg)


def slugify(name):
    s = name.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def load_content(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def sent_split(text):
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p for p in parts if p]


def demo_program(rec_id, title, tier, rank, era, maturity, facts, dbname):
    facts_json = json.dumps(facts, ensure_ascii=False)
    prog = (
        '#!/usr/bin/env python3\n'
        '"""' + title.replace('"""', '"') + ' \u2014 working demonstration.\n'
        'Record ' + rec_id + ' [' + tier + ']. Property of Justin Addam Higgins (JAH).\n'
        '"""\n'
        'TITLE = ' + json.dumps(title, ensure_ascii=False) + '\n'
        'ERA = ' + json.dumps(era, ensure_ascii=False) + '\n'
        'MATURITY = ' + json.dumps(maturity, ensure_ascii=False) + '\n'
        'FACTS = ' + facts_json + '\n'
        'RANK = ' + str(rank) + '\n'
        'DB = ' + json.dumps(dbname, ensure_ascii=False) + '\n'
        'def stage_summary():\n'
        '    return TITLE + " (" + ERA + ") \u2014 " + MATURITY + ": " + "; ".join(FACTS[:3])\n'
        'def main():\n'
        '    print(stage_summary())\n'
        '    print("database:", DB)\n'
        '    print("ladder rank:", RANK, "of 34")\n'
        '    n = sum(len(str(f)) for f in FACTS)\n'
        '    print("fact characters:", n)\n'
        '    assert n > 50, "facts must carry real content"\n'
        '    assert RANK >= 1 and RANK <= 34\n'
        '    print("OK")\n'
        'if __name__ == "__main__":\n'
        '    main()\n'
    )
    return prog


def run_demo(prog, rec_id):
    """Machine-execute a demo program; return (ok, output)."""
    buf = io.StringIO()
    try:
        code = compile(prog, '<demo:%s>' % rec_id, 'exec')
        ns = {'__name__': '__main__'}
        with contextlib.redirect_stdout(buf):
            exec(code, ns)
        out = buf.getvalue()
        return ('OK' in out), out
    except Exception as e:
        return False, 'EXCEPTION: %r' % e


def compose_public_record(tech, stage, rank, tier, prefix, dbname, ladder_target, sig=False):
    rec_id = '%s%06d' % (prefix, rank)
    era = stage['era']
    title = stage['title']
    maturity = stage['maturity']
    k = stage['k'].strip()
    i = stage['i'].strip()
    ctx = sent_split(tech['what'] + ' ' + tech['why'])
    howc = sent_split(tech['how'])
    ctx_s = ctx[(rank - 1) % len(ctx)]
    how_s = howc[(rank - 1) % len(howc)]
    nxt = ''  # ladder target text
    ladder_line = ("Maturity: %s. Era: %s. This is ladder record %d of 34, ordered from the "
                   "technology's oldest known forms to %s."
                   % (maturity, era, rank, ladder_target))
    desc = "%s %s %s %s" % (k, i, ctx_s, ladder_line)
    if tech.get('medical'):
        desc += (" This record describes documented research and history only; it is not "
                 "medical advice, and no treatment claim is made here.")
    how = ("%s %s At the %s stage, the mechanism above is what separated working "
           "approaches from dead ends." % (i, how_s, era))
    key_points = [
        sent_split(k)[0],
        i if len(i) <= 160 else i[:157] + '...',
        tech['principles'][(rank - 1) % len(tech['principles'])],
        tech['entities'][(rank - 1) % len(tech['entities'])],
    ]
    srcn = stage.get('srcn') or 'Documented historical record, cross-checked against public sources.'
    if sig:
        srcn = ('Signature treatment of a documented stage. ' + srcn if 'Signature' not in srcn else srcn)
    requirements = [
        "Verification: " + srcn,
        "Interpret this record under its maturity label: '%s'." % maturity,
    ]
    standards = [SCHEMA_LINE, MATURITY_LINE]
    citations = [srcn, CREDIT_LINE.format(name=tech['name'])]
    facts = [sent_split(k)[0], i, tech['principles'][(rank - 1) % len(tech['principles'])]]
    prog = demo_program(rec_id, title, tier, rank, era, maturity, facts, dbname)
    rec = {
        'id': rec_id, 't': title, 'g': tier,
        'name': title, 'title': title,
        'description': desc, 'how_it_works': how,
        'key_points': key_points, 'requirements': requirements,
        'standards': standards, 'citations': citations,
        'src': 'signature' if sig else 'public-harvest',
        'ladder_rank': rank, 'ladder_tier': tier.lower(),
        'demo': {'kind': 'python', 'language': 'python', 'program': prog,
                 'note': 'Working demonstration program (real, runnable Python).'},
    }
    return rec


def build_pair(tech):
    """Return (public_recs, sig_recs, slugs...)."""
    base = 'futuretech-' + slugify(tech['name'])
    pub_slug = base
    sig_slug = base + '-signature'
    n = tech['n']
    pub_prefix = 'JAH-FUT%03d-' % n
    sig_prefix = 'JAH-FUT%03dS-' % n
    tiers = ['Earliest Forms', 'Early Experiments', 'Breakthrough Era', tech.get('final_tier', 'Working Version')]
    pub_name = 'The %s Database' % tech['name']
    sig_name = 'The %s Signature Database' % tech['name']

    def tier_of(rank):
        c = 0
        for ti, cnt in enumerate(TIER_COUNTS):
            c += cnt
            if rank <= c:
                return tiers[ti]
        return tiers[-1]

    check(len(tech['public']) == 34, '%s: need 34 public stages, got %d' % (base, len(tech['public'])))
    check(len(tech['signature']) == 34, '%s: need 34 signature stages, got %d' % (base, len(tech['signature'])))
    nxt_pub = 'the working version' if 'Working' in tiers[-1] else 'the current research frontier'
    nxt_sig = 'the Signature projection horizon'
    pub_recs, sig_recs = [], []
    for idx, st in enumerate(tech['public']):
        rank = idx + 1
        tier = tier_of(rank)
        st = dict(st)
        pub_recs.append(compose_public_record(tech, st, rank, tier, pub_prefix, pub_name, nxt_pub, sig=False))
    for idx, st in enumerate(tech['signature']):
        rank = idx + 1
        tier = tier_of(rank)
        st = dict(st)
        sig_recs.append(compose_public_record(tech, st, rank, tier, sig_prefix, sig_name, nxt_sig, sig=True))
    return {
        'tech': tech, 'pub_slug': pub_slug, 'sig_slug': sig_slug,
        'pub_prefix': pub_prefix, 'sig_prefix': sig_prefix,
        'pub_name': pub_name, 'sig_name': sig_name,
        'pub_recs': pub_recs, 'sig_recs': sig_recs,
    }


# ---------------- page + generator templates ----------------

def build_page(pair, sig):
    tech = pair['tech']
    slug = pair['sig_slug'] if sig else pair['pub_slug']
    dbname = pair['sig_name'] if sig else pair['pub_name']
    ai_name = 'JAH %s Archivist' % tech['name']
    genver = 'jahdb-%s-1.0' % slug
    tmpl_path = os.path.join(ROOT_DB, 'db', 'language-pashto', 'index.html')
    with open(tmpl_path, encoding='utf-8') as f:
        p = f.read()

    tiers = ['Earliest Forms', 'Early Experiments', 'Breakthrough Era', tech.get('final_tier', 'Working Version')]
    tier_list = ' -> '.join(tiers)
    kind_word = 'Signature-expanded' if sig else 'Public-record'
    hero = (
        "%s: %s Every record traces %s from its oldest known forms through early experiments "
        "and the breakthrough era to %s, ladder-ordered oldest to newest across 34 full records: "
        "description, how it works, key points, requirements, standards, citations, maturity labeling, "
        "and a working demonstration program. Tiers: %s. %s"
        % (tech['name'], tech['short'], tech['name'].lower(),
           'the working version' if 'Working' in tiers[-1] else 'the current research frontier',
           tier_list, tech['status_note']))
    page_desc = ("%s - %s. 34 ladder-ordered records from oldest forms to %s, with maturity "
                 "labeling on every record. Property of Justin Addam Higgins."
                 % (dbname, tech['short'],
                    'the working version' if 'Working' in tiers[-1] else 'the current frontier'))
    role = ("%s - teaching %s from its oldest known forms through early experiments and the "
            "breakthrough era to %s; teaching progressively along the ladder; answers from many angles - "
            "definition, example, history, mechanism, application, maturity - using only archive data "
            "from this system" % (ai_name.lower(), tech['name'],
                                  'the working version' if 'Working' in tiers[-1] else 'the current frontier'))
    about_archive = (
        "Seeded %s %s records, marching toward one million records. Presented in teaching-ladder order: %s."
        % ('Signature-treatment' if sig else 'public-record', tech['name'], tier_list))
    about_ai = ("%s - %s - and aware of the whole JAH Databases network through cross-database reasoning. "
                "On-device Standard 1.0, no key needed; uses the shared Signature backend automatically when configured."
                % (ai_name, role))
    type_line = ('Signature records - Signature-expanded treatment'
                 if sig else 'Public records organized in the Signature system')
    gen_blurb = ("Generate clearly-labeled %s %s studies. Seeded archive records are the authoritative entries."
                 % (tech['name'], 'Signature' if sig else 'public-record'))
    search_ph = "Search %s stages, eras, mechanisms, milestones..." % tech['name']

    # substitutions
    p = re.sub(r'<script type="application/ld\+json">.*?</script>',
               '<script type="application/ld+json">%s</script>'
               % json.dumps({"@context": "https://schema.org", "@type": "Dataset",
                             "name": dbname, "description": page_desc,
                             "creator": {"@type": "Person", "name": "Justin Addam Higgins"}},
                            ensure_ascii=False),
               p, count=1, flags=re.S)
    p = re.sub(r"esc\('I am the JAH Pashto Language Archivist\. Ask me about Pashto - from the 44-letter alphabet and sounds through core words, grammar, and everyday sentences to stories, idioms, and conversations\.'\)",
               "esc('I am the %s. Ask me about %s - from its oldest known forms through early experiments and the breakthrough era to %s.') "
               % (ai_name, tech['name'],
                  'the working version' if 'Working' in tech.get('final_tier', 'Working Version') else 'the current research frontier'),
               p, count=1)
    p = p.replace('<title>The Pashto Language Database \u2014 JAH Databases</title>',
                  '<title>%s \u2014 JAH Databases</title>' % dbname)
    p = re.sub(r'<meta name="description" content=".*?">',
               '<meta name="description" content="%s">' % htmlmod.escape(page_desc, quote=True),
               p, count=1)
    p = re.sub(r'"name": "The Pashto Language Database"', '"name": "%s"' % dbname.replace('"', ''), p)
    p = re.sub(r'<h1>The Pashto Language Database</h1>', '<h1>%s</h1>' % dbname, p)
    p = re.sub(r'(<h1>.*?</h1>\s*<p>).*?(</p>)',
               lambda m: m.group(1) + htmlmod.escape(hero) + m.group(2), p, count=1, flags=re.S)
    p = p.replace('jahdb-language-pashto-1.0', genver)
    p = p.replace("SLUG='language-pashto'", "SLUG='%s'" % slug)
    p = p.replace(DATA_DOMAIN + 'language-pashto/', DATA_DOMAIN + slug + '/')
    p = p.replace("name:'The Pashto Language Database',ai_name:'JAH Pashto Language Archivist',record_kind:'language learning record'",
                  "name:'%s',ai_name:'%s',record_kind:'future technology record'" % (dbname, ai_name))
    p = re.sub(r"var ROLE='.*?';", "var ROLE='%s';" % role.replace("'", "\\'"), p, count=1)
    p = p.replace("JAHDB.emblemSVG(db.name,'JAH-SI-')", "JAHDB.emblemSVG(db.name,'JAH-FUT-')")
    p = p.replace('Search Pashto letters, words, verbs, tenses, phrases, grammar, dialogues...', search_ph)
    p = p.replace('<h3>JAH Pashto Language Archivist <button', '<h3>%s <button' % ai_name)
    p = p.replace('placeholder="Ask about Pashto..."', 'placeholder="Ask about %s..."' % tech['name'])
    p = p.replace('<h3>The Pashto Language Database generator</h3>', '<h3>%s generator</h3>' % dbname)
    p = re.sub(r'(<h3>%s generator</h3>\s*<p class="dim">).*?(</p>)' % re.escape(dbname),
               lambda m: m.group(1) + htmlmod.escape(gen_blurb) + m.group(2), p, count=1, flags=re.S)
    p = p.replace('<b>Public records organized in the Signature system</b>', '<b>%s</b>' % type_line)
    # about card body
    about_new = (
        '<h3>About this data base</h3>\n      <dl class="kv">\n'
        '        <dt>Archive</dt><dd>%s</dd>\n'
        '        <dt>Record schema</dt><dd class="mono">%s</dd>\n'
        '        <dt>Ladder</dt><dd>%s - each tier opens on demand and loads only what you open</dd>\n'
        '        <dt>Maturity labeling</dt><dd>Every record carries a maturity label: established, emerging, research, or speculative. Speculative content is Signature-labeled and never presented as established fact.</dd>\n'
        '        <dt>Generator</dt><dd>%s - %s Seeded archive records are the authoritative entries.</dd>\n'
        '        <dt>Drift control</dt><dd>Every generated record is checked against an archive sample for exact duplicates and re-validated by the independent checker.</dd>\n'
        '        <dt>Target</dt><dd>1,000,000 records. The archive marches toward the million mark with overload protection: 100-record chunks, lazy loading, and a collapsible per-tier archive so no device ever renders everything at once.</dd>\n'
        '        <dt>AI</dt><dd>%s</dd>\n'
        '        <dt>Signature system</dt><dd>%s records organized in the Signature system. Property of Justin Addam Higgins (JAH).</dd>\n'
        '      </dl>'
        % (htmlmod.escape(about_archive), SCHEMA_LINE, tier_list, genver,
           htmlmod.escape(gen_blurb), htmlmod.escape(about_ai),
           'Signature' if sig else 'Public'))
    p = re.sub(r'<h3>About this data base</h3>\s*<dl class="kv">.*?</dl>',
               about_new, p, count=1, flags=re.S)
    p = p.replace('<script src="gen-language-pashto.js">', '<script src="gen-%s.js">' % slug)
    return p


def build_gen_js(pair, sig):
    tech = pair['tech']
    slug = pair['sig_slug'] if sig else pair['pub_slug']
    prefix = pair['sig_prefix'] if sig else pair['pub_prefix']
    dbname = pair['sig_name'] if sig else pair['pub_name']
    recs = pair['sig_recs'] if sig else pair['pub_recs']
    tiers = ['Earliest Forms', 'Early Experiments', 'Breakthrough Era', tech.get('final_tier', 'Working Version')]
    topics = {}
    for r in recs:
        topics.setdefault(r['g'], []).append(r['t'])
    fields_js = json.dumps(tiers)
    topics_js = '{\n' + ',\n'.join(
        ' %s: %s' % (json.dumps(t), json.dumps(topics[t], ensure_ascii=False)) for t in tiers) + '\n}'
    safe_db = dbname.replace('\\', '\\\\').replace('"', "'")
    demo_fn = (
        'function demoProgram(topic,field){\n'
        '  var safe=String(topic).replace(/\\\\/g,\'\\\\\\\\\').replace(/"/g,"\'");\n'
        '  return "# %s \\u2014 "+safe+"\\n"\n' % safe_db +
        '   + "# Field: "+field+"\\n"\n'
        '   + "record = {\'title\': \\""+safe+"\\", \'field\': \\""+field+"\\"}\\n"\n'
        '   + "def summarize(r):\\n"\n'
        '   + "    return r[\'title\'] + \' [\' + r[\'field\'] + \']\'\\n"\n'
        '   + "print(summarize(record))\\n"\n'
        '   + "print(\'Sample record \\u2014 structural sample, not an archive entry.\')\\n";\n'
        '}\n'
    )
    js = (
        "(function(){'use strict';\n"
        "/* JAH %s generator \u2014 jahdb-%s-1.0.\n"
        "   Property of Justin Addam Higgins (JAH).\n"
        "   Deterministic: same seed, same record. */\n"
        "function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}\n"
        "function pick(r,s){return r[(s()*r.length)|0];}\n"
        'var PREFIX="%s";\n'
        "var FIELDS=%s;\n"
        "var TOPICS=%s;\n"
        % (safe_db, slug, prefix, fields_js, topics_js)
    )
    js += demo_fn
    js += (
        "function generate(seed,opts,rnd){\n"
        "  opts=opts||{}; rnd=rnd||prng(seed);\n"
        "  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);\n"
        "  var pool=TOPICS[field]||[\"General Study\"];\n"
        "  var topic=pick(pool,rnd);\n"
        "  var id=PREFIX+String(seed).padStart(6,'0');\n"
        "  return {\n"
        "    id:id,\n"
        "    name:topic+' \u2014 future technology record',\n"
        "    title:topic,\n"
        "    description:'SAMPLE RECORD (generated \u2014 structural sample). A future technology record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',\n"
        "    field:field,\n"
        "    src:'signature-generated-sample',\n"
        "    sample:true,\n"
        "    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',\n"
        "    demo:{kind:\"futuretech-demo\",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},\n"
        "    _seed:seed\n"
        "  };\n"
        "}\n"
        "function validate(r){\n"
        "  var e=[];\n"
        "  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};\n"
        "  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\\\-')+'\\\\d{6}$').test(r.id||''))e.push('id');\n"
        "  if(FIELDS.indexOf(r.field)<0)e.push('field');\n"
        "  if(!r.src)e.push('src');\n"
        "  if(!r.demo||!r.demo.program)e.push('demo');\n"
        "  return {ok:!e.length,errors:e};\n"
        "}\n"
        "function driftCheck(record,sample){\n"
        "  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});\n"
        "  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};\n"
        "}\n"
        "var gen={version:'jahdb-%s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};\n"
        "if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('%s',gen);\n"
        "if(typeof module!=='undefined'&&module.exports)module.exports=gen;\n"
        "})();\n" % (slug, slug)
    )
    return js


# ---------------- gates ----------------

def system_titles():
    """Cache + return set of all record titles across the data repo."""
    cache = os.path.join(BUILD_DIR, 'system_titles.pkl')
    if os.path.exists(cache):
        with open(cache, 'rb') as f:
            return pickle.load(f)
    titles = set()
    data_root = os.path.join(ROOT_DATA, 'data')
    for slug in sorted(os.listdir(data_root)):
        idx = os.path.join(data_root, slug, 'index.jsonl.gz')
        if not os.path.exists(idx):
            continue
        try:
            with gzip.open(idx, 'rt', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        r = json.loads(line)
                        if r.get('t'):
                            titles.add(r['t'])
                    except Exception:
                        pass
        except Exception:
            pass
    with open(cache, 'wb') as f:
        pickle.dump(titles, f)
    return titles


def gate_text(recs, tech, sig):
    blobs = []
    for r in recs:
        blobs.append(r['description'] + ' ' + r['how_it_works'] + ' ' + ' '.join(r['key_points']))
    text = '\n'.join(blobs)
    low = text.lower()
    for w in BLOCKLIST:
        check(w.lower() not in low, 'blocklist hit %r in %s' % (w, tech['name']))
    if tech.get('medical'):
        check(not CURE_RE.search(text), 'cure-claim pattern in medical tech %s' % tech['name'])
    for bad in ['<script', 'javascript:', 'onerror=']:
        check(bad not in low, 'injection pattern %r in %s' % (bad, tech['name']))
    # every record must be substantive
    for r in recs:
        check(len(r['description']) >= 500, 'short description in %s' % r['id'])
        check(len(r['how_it_works']) >= 150, 'short how_it_works in %s' % r['id'])
        check(len(r['key_points']) >= 3, 'few key_points in %s' % r['id'])


def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')


def build_tech(tech, sys_titles, only=None):
    pair = build_pair(tech)
    results = []
    for sig in (False, True):
        slug = pair['sig_slug'] if sig else pair['pub_slug']
        if only and slug != only:
            continue
        recs = pair['sig_recs'] if sig else pair['pub_recs']
        dbname = pair['sig_name'] if sig else pair['pub_name']
        check(len(recs) == 34, '%s: %d records' % (slug, len(recs)))
        ranks = [r['ladder_rank'] for r in recs]
        check(ranks == list(range(1, 35)), '%s: ladder ranks broken' % slug)
        check(len({r['id'] for r in recs}) == 34, '%s: dup ids' % slug)
        # dedupe vs system + within batch
        for r in recs:
            check(r['t'] not in sys_titles, 'system title dup: %s' % r['t'])
            sys_titles.add(r['t'])
        # content gates
        gate_text(recs, tech, sig)
        # demo execution gate
        ndemo = 0
        for r in recs:
            ok, out = run_demo(r['demo']['program'], r['id'])
            check(ok, 'demo failed for %s: %s' % (r['id'], out[:300]))
            ndemo += 1
        # write page + gen
        db_dir = os.path.join(ROOT_DB, 'db', slug)
        os.makedirs(db_dir, exist_ok=True)
        page = build_page(pair, sig)
        # page canon checks
        for token in ['id="stCount"', 'Exhaustive', 'All Database Merger', 'mergePanel',
                      'dataset.p', 'codeblock', 'minmax(120px,1fr)']:
            check(token in page, '%s page missing %s' % (slug, token))
        with open(os.path.join(db_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(page)
        gen_js = build_gen_js(pair, sig)
        gen_path = os.path.join(db_dir, 'gen-%s.js' % slug)
        with open(gen_path, 'w', encoding='utf-8') as f:
            f.write(gen_js)
        cp = subprocess.run(['node', '--check', gen_path], capture_output=True, text=True)
        check(cp.returncode == 0, 'node --check failed for %s: %s' % (slug, cp.stderr[:300]))
        # write data
        data_dir = os.path.join(ROOT_DATA, 'data', slug)
        write_gz_jsonl(os.path.join(data_dir, 'index.jsonl.gz'),
                       [{'id': r['id'], 't': r['t'], 'g': r['g']} for r in recs])
        write_gz_jsonl(os.path.join(data_dir, 'chunks', 'chunk-0000.jsonl.gz'), recs)
        # stage build dir
        bdir = os.path.join(ROOT_DB, 'code', slug + '-build')
        os.makedirs(bdir, exist_ok=True)
        with open(os.path.join(bdir, 'data.json'), 'w', encoding='utf-8') as f:
            json.dump(tech, f, ensure_ascii=False, indent=1)
        with open(os.path.join(bdir, 'build.sh'), 'w', encoding='utf-8') as f:
            f.write('#!/bin/sh\n# Rebuild this database pair from its staged content.\n'
                    'python3 %s --only %s\n' % (os.path.join(BUILD_DIR, 'build_all.py'), slug))
        os.chmod(os.path.join(bdir, 'build.sh'), 0o755)
        results.append((slug, len(recs), ndemo))
    return results


def main():
    args = sys.argv[1:]
    only = None
    batches = []
    i = 0
    while i < len(args):
        if args[i] == '--only':
            only = args[i + 1]
            i += 2
        elif args[i] == '--batch':
            batches.append(args[i + 1])
            i += 2
        elif args[i] == '--all':
            batches = sorted(f for f in os.listdir(BUILD_DIR)
                             if f.startswith('techs-') and f.endswith('.json'))
            i += 1
        else:
            fail('unknown arg %s' % args[i])
    if not batches and not only:
        fail('usage: build_all.py --batch <file> | --all | --only <slug>')
    if only and not batches:
        batches = sorted(f for f in os.listdir(BUILD_DIR)
                         if f.startswith('techs-') and f.endswith('.json'))
    sys_titles = system_titles()
    total = []
    for b in batches:
        techs = load_content(os.path.join(BUILD_DIR, b))
        for tech in techs:
            res = build_tech(tech, sys_titles, only=only)
            total.extend(res)
            for slug, nrec, ndemo in res:
                print('OK %s records=%d demos=%d' % (slug, nrec, ndemo))
    print('TOTAL pairs=%d databases=%d' % (len(total) // 2, len(total)))


if __name__ == '__main__':
    main()
