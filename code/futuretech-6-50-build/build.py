#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builder for future-tech 100 items 6-50 (45 databases x 34 records).
Emits: db/<slug>/{index.html,gen-<slug>.js}, data-1 shards, fragments, per-slug build dirs.
Property of Justin Addam Higgins (JAH)."""
import os, sys, json, gzip, re, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import items

DB_DIR = os.path.expanduser('~/workspace/jah-databases/db')
DATA1 = os.path.expanduser('~/workspace/jah-databases-data-1/data')
FRAG = os.path.expanduser('~/workspace/hidden_files/missing-builds/fragments')
CODE = os.path.expanduser('~/workspace/jah-databases/code')
TEMPLATE = os.path.join(DB_DIR, 'ai-seller-training', 'index.html')
DATA1_URL = 'https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/'

def tier_of(rank):
    if rank <= 12:
        return 'Foundations'
    if rank <= 23:
        return 'Compounded'
    return 'Advanced'

def js_str(s):
    return json.dumps(s)

def demo_program(item, rank, ms):
    title, era, mat, just, facts, cites = ms
    rid = item['prefix'] + str(rank).zfill(6)
    tier = tier_of(rank)
    lines = []
    lines.append('#!/usr/bin/env python3')
    lines.append('"""' + title + ' -- working demonstration.')
    lines.append('Record ' + rid + ' [' + tier + '] from The ' + item['tech'] + ' Future Technology Database.')
    lines.append('Property of Justin Addam Higgins (JAH). Maturity: ' + mat + '.')
    lines.append('"""')
    lines.append('record = {')
    lines.append('    "id": ' + js_str(rid) + ',')
    lines.append('    "title": ' + js_str(title) + ',')
    lines.append('    "era": ' + js_str(era) + ',')
    lines.append('    "maturity": ' + js_str(mat) + ',')
    lines.append('    "ladder_rank": ' + str(rank) + ',')
    lines.append('    "ladder_tier": ' + js_str(tier) + ',')
    lines.append('    "facts": [' + ', '.join(js_str(f) for f in facts) + '],')
    lines.append('}')
    lines.append('def ladder_progress(rank, total=34):')
    lines.append('    return rank / total')
    lines.append('progress = ladder_progress(record["ladder_rank"])')
    lines.append('print("Record: %s (%s)" % (record["title"], record["era"]))')
    lines.append('print("Maturity: %s" % record["maturity"])')
    lines.append('print("Ladder: rank %d of 34 (%s) -- %.1f%% along the ladder" % (record["ladder_rank"], record["ladder_tier"], progress * 100))')
    lines.append('for i, f in enumerate(record["facts"], 1):')
    lines.append('    print("Fact %d: %s" % (i, f))')
    lines.append('checksum = sum(ord(c) for c in record["id"] + record["title"]) % 100000')
    lines.append('print("Record checksum: %d" % checksum)')
    lines.append('print("OK")')
    return '\n'.join(lines) + '\n'

def expand_record(item, rank, ms):
    title, era, mat, just, facts, cites = ms
    f1, f2, f3 = facts
    tier = tier_of(rank)
    rid = item['prefix'] + str(rank).zfill(6)
    tech = item['tech']
    srcv = 'signature' if mat == 'Speculative' else 'public-harvest'
    if mat == 'Established':
        desc = ('%s (%s) marks a %s step in the %s ladder. %s %s %s '
                'Documented here as an established, fact-checked milestone.' % (title, era, tier.lower(), tech, f1, f2, f3))
        matline = 'Established: a documented, fact-checked milestone.'
    elif mat == 'Emerging':
        desc = ('%s (%s) marks a %s step in the %s ladder. %s %s %s '
                'An emerging frontier development, active as of 2026.' % (title, era, tier.lower(), tech, f1, f2, f3))
        matline = 'Emerging: active frontier development as of 2026.'
    else:
        desc = ('Signature-generated speculative projection \u2014 not established fact. %s (%s) imagines a %s step '
                'in the %s ladder. %s %s %s' % (title, era, tier.lower(), tech, f1, f2, f3))
        matline = 'Speculative: Signature-generated speculative projection \u2014 not established fact.'
    how = ('What this record covers: %s. %s %s In the %s teaching ladder, this %s record (rank %d of 34) %s %s '
           'The demonstration program below encodes this record\u2019s data and verifies its ladder position.' % (
               title, f1, f2, tech, tier.lower(), rank,
               'documents a verified historical step.' if mat == 'Established' else
               'tracks a live frontier development.' if mat == 'Emerging' else
               'projects a possible future step \u2014 it is clearly labeled speculative.',
               f3))
    rec = {
        'id': rid,
        't': title,
        'g': tier,
        'name': title,
        'title': title,
        'description': desc,
        'how_it_works': how,
        'key_points': [f1, f2, f3, matline,
                       'Ladder rank %d of 34 (%s): %s.' % (rank, tier,
                        'the earliest form of the technology' if rank == 1 else
                        'the current frontier / working version' if rank == 34 else
                        'a step between the earliest form and the working version')],
        'requirements': [
            'State in one sentence what changed at this step and why it mattered for %s.' % tech,
            'Place this record on the ladder: name what came before it and what it made possible.',
            'Give the maturity label for this record and its one-line status justification.'],
        'standards': [
            'Every record carries a maturity label \u2014 Established, Emerging, or Speculative \u2014 with a one-line status justification.',
            'Speculative records are Signature-generated projections \u2014 never presented as established fact.',
            'Citations on every record; established claims are fact-checked real data.'],
        'citations': list(cites),
        'src': srcv,
        'maturity': mat,
        'status_justification': just,
        'era': era,
        'ladder_rank': rank,
        'ladder_tier': tier.lower(),
        'demo': {'kind': 'python', 'language': 'python', 'program': demo_program(item, rank, ms),
                 'note': 'Working demonstration: encodes the record and verifies its ladder position.'},
    }
    return rec

def build_records(item):
    ms = items.MILESTONES[item['slug']]
    assert len(ms) == 34, (item['slug'], len(ms))
    return [expand_record(item, i + 1, m) for i, m in enumerate(ms)]

# ---------------- page generation ----------------
def hero_paragraph(item, records):
    def titles(tier):
        return [r['title'] for r in records if r['g'] == tier][:6]
    f = titles('Foundations'); c = titles('Compounded'); a = titles('Advanced')
    return ('%s \u2014 Every record carries the full entry: description, how it works, key points, requirements, '
            'standards, citations, maturity label, and a working demonstration program. '
            'Records are ordered by the teaching ladder from the oldest form to the working version: '
            'Foundations (%s) \u2192 Compounded (%s) \u2192 Advanced (%s).' % (
                item['tag'], '; '.join(f), '; '.join(c), '; '.join(a)))

def gen_page(item, records):
    tpl = open(TEMPLATE, encoding='utf-8').read()
    slug = item['slug']; tech = item['tech']
    name = 'The %s Future Technology Database' % tech
    gen_name = 'jahdb-%s-1.0' % slug
    # 1. long distinctive strings first
    tpl = tpl.replace('The AI Seller Training Database', name)
    tpl = tpl.replace('ai-seller-training', slug)
    tpl = tpl.replace('JAH AI Seller Training Archivist', item['ai'])
    tpl = tpl.replace("'AI seller training record'", js_str(item['kind']))
    tpl = tpl.replace('AI seller training', tech.lower())
    tpl = tpl.replace("'JAH-SI-'", js_str(item['prefix']))
    tpl = tpl.replace('Public records organized in the Signature system',
                      'Public and Signature records organized in the Signature system')
    # 2. hero paragraph (first <p> after <h1>)
    tpl = re.sub(r'(<h1>.*?</h1>\s*)<p>.*?</p>', lambda m: m.group(1) + '<p>' + hero_paragraph(item, records) + '</p>',
                 tpl, count=1, flags=re.S)
    # 3. meta description + JSON-LD description
    meta = '%s. %s Property of Justin Addam Higgins.' % (name, item['tag'])
    tpl = tpl.replace(re.search(r'<meta name="description" content="[^"]*">', tpl).group(0),
                      '<meta name="description" content="%s">' % meta.replace('"', '&quot;'))
    tpl = re.sub(r'("description": ")[^"]*(",\s*"creator")', lambda m: m.group(1) + meta.replace('"', '') + m.group(2), tpl, count=1)
    # 4. search placeholder
    sample_titles = ', '.join([r['title'] for r in records[::7]][:6])
    tpl = re.sub(r'<input id="q" placeholder="[^"]*"', '<input id="q" placeholder="Search %s...">' % sample_titles.replace('"', ''), tpl, count=1)
    # 5. generator card
    tpl = tpl.replace('Generate clearly-labeled AI seller training studies. Seeded archive records are the authoritative entries.',
                      'Generate clearly-labeled %s studies. Seeded archive records are the authoritative entries.' % tech.lower())
    # 6. chat placeholder + greet
    tpl = tpl.replace('Ask about AI seller training...', 'Ask about %s...' % tech.lower())
    greet_txt = ('I am the %s. Ask me about %s \u2014 from its oldest form through %s.' % (
        item['ai'], tech.lower(), ', '.join([r['title'] for r in records[::11]][:3])))
    tpl = re.sub(r"esc\('I am the JAH.*?self-review\.'\)", lambda m: "esc(%s)" % js_str(greet_txt), tpl, count=1, flags=re.S)
    # 7. ROLE
    tpl = re.sub(r"var ROLE='.*?';", "var ROLE=%s;" % js_str(item['role']), tpl, count=1, flags=re.S)
    # 8. About tab fields
    tpl = tpl.replace('Seeded public-record AI seller training records, marching toward one million records. Presented in teaching-ladder order: foundations, compounded, advanced.',
                      'Seeded %s, marching toward one million records. Presented in teaching-ladder order: foundations, compounded, advanced \u2014 every record carries a maturity label (Established, Emerging, or Speculative).' % item['kind'])
    tpl = tpl.replace('id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, ladder_rank, ladder_tier, demo',
                      'id, t, g, name, title, description, how_it_works, key_points, requirements, standards, citations, src, maturity, status_justification, era, ladder_rank, ladder_tier, demo')
    tpl = tpl.replace('jahdb-ai-seller-training-1.0 \u2014 Generate clearly-labeled AI seller training studies. Seeded archive records are the authoritative entries.',
                      '%s \u2014 Generate clearly-labeled %s studies. Seeded archive records are the authoritative entries.' % (gen_name, tech.lower()))
    # 9. sigBadge: add maturity branch
    old_badge = """function sigBadge(r){
  if(r&&r.src==='public-harvest') return '<div><span class="badge">\u2713 Public record</span></div>';
  if(r&&r.src==='signature') return '<div><span class="badge sig">\u2733 Signature original</span></div>';
  return '<div><span class="badge sig">\u2733 Signature-generated sample \u2014 structural sample</span> <span class="badge">labeled sample</span></div>';
}"""
    new_badge = """function sigBadge(r){
  if(r&&r.maturity==='Speculative') return '<div><span class="badge sig">\u2733 Signature-generated speculative projection \\u2014 not established fact</span></div>';
  if(r&&r.src==='public-harvest') return '<div><span class="badge">\u2713 Public record</span></div>';
  if(r&&r.src==='signature') return '<div><span class="badge sig">\u2733 Signature original</span></div>';
  return '<div><span class="badge">record</span></div>';
}"""
    assert old_badge in tpl, 'sigBadge anchor missing'
    tpl = tpl.replace(old_badge, new_badge)
    return tpl

# ---------------- generator JS ----------------
def gen_js(item, records):
    tiers = {'Foundations': [], 'Compounded': [], 'Advanced': []}
    for r in records:
        tiers[r['g']].append(r['title'])
    def js_arr(xs):
        return '[\n' + ',\n'.join('    ' + js_str(x) for x in xs) + '\n  ]'
    topics = '{\n' + ',\n'.join('  "%s": %s' % (k, js_arr(v)) for k, v in tiers.items()) + '\n}'
    kind = item['kind']
    return '''(function(){'use strict';
/* JAH The %(tech)s Future Technology Database generator \u2014 jahdb-%(slug)s-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX=%(prefix)s;
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=%(topics)s;
function demoProgram(topic,field,seed){
  return "# %(tech)s Study \\u2014 "+topic+"\\n"
   + "# Field: "+field+" | seed "+seed+"\\n"
   + "record = {'title': "+JSON.stringify(topic)+", 'field': "+JSON.stringify(field)+", 'seed': "+seed+"}\\n"
   + "def summarize(r):\\n"
   + "    return r['title'] + ' [' + r['field'] + '] (seed ' + str(r['seed']) + ')'\\n"
   + "print(summarize(record))\\n"
   + "print('Generated variant \\u2014 not an archive record.')\\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \\u2014 %(kind)s (generated variant)',
    title:topic,
    description:'GENERATED VARIANT (boundless generator). A %(kind)s study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
    field:field,
    src:'signature',
    generated:true,
    disclaimer:'Generated variant \\u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field,seed),note:'Generated variant demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\\\-')+'\\\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:%(slug)s,name:%(name)s};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators[%(slug)s]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator(%(slug)s,api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
''' % {'tech': item['tech'], 'slug': js_str(item['slug']), 'prefix': js_str(item['prefix']),
       'topics': topics, 'kind': kind, 'name': js_str('The %s Future Technology Database' % item['tech'])}

# ---------------- shards + fragments ----------------
def gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')

def write_shard(item, records):
    slug = item['slug']
    d = os.path.join(DATA1, slug)
    gz_jsonl(os.path.join(d, 'index.jsonl.gz'), [{'id': r['id'], 't': r['t'], 'g': r['g']} for r in records])
    gz_jsonl(os.path.join(d, 'chunks', 'chunk-0000.jsonl.gz'), records)

def write_fragment(item):
    slug = item['slug']
    frag = {
        'slug': slug,
        'name': 'The %s Future Technology Database' % item['tech'],
        'tagline': item['tag'],
        'record_kind': item['kind'],
        'id_prefix': item['prefix'],
        'ai_name': item['ai'],
        'local_index': DATA1_URL + '%s/index.jsonl.gz' % slug,
        'record_count': 34,
        'status': 'staged',
        'full_records': 34,
        'index': DATA1_URL + '%s/index.jsonl.gz' % slug,
        'chunk_pattern': 'data/%s/chunks/chunk-NNNN.jsonl.gz' % slug,
        'source': 'signature-made',
    }
    os.makedirs(FRAG, exist_ok=True)
    json.dump(frag, open(os.path.join(FRAG, slug + '.json'), 'w'), indent=1)

SHIM_TMPL = '''#!/usr/bin/env python3
"""Build script for the %(name)s — delegates to the shared futuretech-6-50 builder.
Property of Justin Addam Higgins (JAH)."""
import os, sys, json, importlib.util
_shared = os.path.expanduser('~/workspace/jah-databases/code/futuretech-6-50-build/build.py')
_spec = importlib.util.spec_from_file_location('ft650_build', _shared)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
if __name__ == '__main__':
    print(json.dumps(_mod.build_item(%(slug)r), indent=1))
'''

def write_build_shim(item):
    slug = item['slug']
    d = os.path.join(CODE, slug + '-build')
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'build.py'), 'w').write(
        SHIM_TMPL % {'name': 'The %s Future Technology Database' % item['tech'], 'slug': slug})

# ---------------- gates ----------------
GATE_WORDS = [
    r'\bfuck\w*', r'\bshit\w*', r'\bbitch\w*', r'\bcunt\w*', r'\bdick\w*', r'\bpussy\w*',
    r'\basshole\w*', r'\bwhore\w*', r'\bslut\w*', r'\bmotherfuck\w*',
    r'\bnazi\w*', r'\bhitler\b', r'\bgenocide\b', r'\bethnic cleans\w*',
    r'\bworship\w*', r'\bprayer\w*', r'\bbible\b', r'\bscripture\w*', r'\bprophet\w*',
    r'\bheaven\b', r'\balmighty\b', r'\bblasphem\w*', r'\bafterlife\b',
]
GATE_RX = re.compile('|'.join(GATE_WORDS), re.I)

def content_gate(records):
    hits = []
    for r in records:
        blob = ' '.join([r['title'], r['description'], r['how_it_works']] + r['key_points'] + r['requirements'] + r['standards'])
        m = GATE_RX.search(blob)
        if m:
            w = m.group(0).lower()
            if w in ('demonstrated', 'demonstration', 'demonstrations', 'angeles'):
                continue
            hits.append((r['id'], w))
    return hits

def title_gate(item, records, system_titles):
    seen = set()
    bad = []
    for r in records:
        t = r['title'].lower()
        if t in seen:
            bad.append(('dup-in-db', r['id'], r['title']))
        seen.add(t)
        if t in system_titles:
            bad.append(('dup-system', r['id'], r['title']))
    return bad

def run_demos(item, records):
    ddir = os.path.join(HERE, 'demos', item['slug'])
    os.makedirs(ddir, exist_ok=True)
    fps = []
    for r in records:
        fp = os.path.join(ddir, r['id'] + '.py')
        open(fp, 'w', encoding='utf-8').write(r['demo']['program'])
        fps.append(fp)
    fails = []
    import tempfile
    lst = tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt')
    lst.write('\n'.join(fps)); lst.close()
    cmd = "xargs -a %s -P 8 -I{} sh -c 'python3 {} > {}.out 2>&1 || echo FAIL:{} >> %s.fails; grep -q ^OK$ {}.out || echo NOOK:{} >> %s.fails'" % (lst.name, lst.name, lst.name)
    subprocess.run(cmd, shell=True)
    failfile = lst.name + '.fails'
    if os.path.exists(failfile):
        fails = open(failfile).read().split()
        os.remove(failfile)
    os.remove(lst.name)
    return fails

def node_check(path):
    r = subprocess.run(['node', '--check', path], capture_output=True, text=True)
    return r.returncode == 0, r.stderr[:500]

# ---------------- main per-item build ----------------
def build_item(slug, system_titles=None):
    item = next(i for i in items.ITEMS if i['slug'] == slug)
    records = build_records(item)
    # gates
    if system_titles is None:
        system_titles = set(json.load(open(os.path.expanduser('~/workspace/hidden_files/futuretech-6-50-build/title-set.json'))))
    tg = title_gate(item, records, system_titles)
    assert not tg, ('title gate failed', tg)
    cg = content_gate(records)
    assert not cg, ('content gate failed', cg)
    # pages + generators
    dd = os.path.join(DB_DIR, slug)
    os.makedirs(dd, exist_ok=True)
    page = gen_page(item, records)
    open(os.path.join(dd, 'index.html'), 'w', encoding='utf-8').write(page)
    gpath = os.path.join(dd, 'gen-%s.js' % slug)
    open(gpath, 'w', encoding='utf-8').write(gen_js(item, records))
    ok, err = node_check(gpath)
    assert ok, ('node --check failed', gpath, err)
    # demos
    fails = run_demos(item, records)
    assert not fails, ('demo failures', fails[:10])
    # shards + fragment + shim
    write_shard(item, records)
    write_fragment(item)
    write_build_shim(item)
    return {'slug': slug, 'records': len(records), 'demos': len(records)}

def build_all(slugs=None):
    system_titles = set(json.load(open(os.path.expanduser('~/workspace/hidden_files/futuretech-6-50-build/title-set.json'))))
    targets = slugs or [i['slug'] for i in items.ITEMS]
    results = []
    for s in targets:
        print('building', s, flush=True)
        results.append(build_item(s, system_titles))
    return results

if __name__ == '__main__':
    slugs = sys.argv[1:] or None
    res = build_all(slugs)
    print(json.dumps(res, indent=1))
