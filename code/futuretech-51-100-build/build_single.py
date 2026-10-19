#!/usr/bin/env python3
"""Build ONE database per future-tech technology, items 51-100.

Each technology gets a SINGLE database (not a pair): 34 FULL ladder-ordered
records tracing the technology from its oldest/earliest form to the working
version. Every record carries a maturity label (Established / Emerging /
Speculative) with a one-line status justification. Speculative records are
Signature-labeled and never presented as established fact.

Usage:
    python3 build_single.py --all
    python3 build_single.py --only <slug>

Reads:
    data/ft51.json ... data/ft100.json   (exactly 50 files)

Writes (STAGE ONLY - never touches manifest/api.json, never commits):
    ~/workspace/jah-databases/db/<slug>/index.html
    ~/workspace/jah-databases/db/<slug>/gen-<slug>.js
    ~/workspace/jah-databases-data-1/data/<slug>/index.jsonl.gz        (34 rows)
    ~/workspace/jah-databases-data-1/data/<slug>/chunks/chunk-0000.jsonl.gz  (34 full)
    ~/workspace/hidden_files/missing-builds/fragments/<slug>.json
    ~/workspace/jah-databases/code/<slug>-build/{data.json,build.sh}
    build-report.json (this dir)

Gates (fail the build on any violation):
    - exactly 50 data files, 34 records each, ladder ranks 1..34, unique IDs
    - roster prefix exact + substring unique vs data/manifest.json
    - whole-system exact-title dedupe vs hidden_files/all_db_titles.json
    - every demo program machine-executed: exit 0 + OK marker
    - node --check on every gen-<slug>.js
    - content gates: blocklist, no religious framing, no military-neutralization
      content, no website/Facebook references
    - page canon tokens: id="stCount", Exhaustive, All Database Merger,
      mergePanel, dataset.p, codeblock, minmax(120px,1fr)

Property of Justin Addam Higgins (JAH).
"""
import json
import gzip
import os
import re
import sys
import glob
import subprocess

ROOT_DB = os.path.expanduser('~/workspace/jah-databases')
ROOT_DATA = os.path.expanduser('~/workspace/jah-databases-data-1')
BUILD_DIR = os.path.join(ROOT_DB, 'code', 'futuretech-51-100-build')
DATA_DIR = os.path.join(BUILD_DIR, 'data')
FRAG_DIR = os.path.expanduser('~/workspace/hidden_files/missing-builds/fragments')
TITLES_JSON = os.path.expanduser('~/workspace/hidden_files/all_db_titles.json')
MANIFEST = os.path.join(ROOT_DB, 'data', 'manifest.json')
DATA_DOMAIN = 'https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/'
EXEMPLAR_PAGE = os.path.join(ROOT_DB, 'db', 'cloud-internet-things', 'index.html')
EXEMPLAR_GEN = os.path.join(ROOT_DB, 'db', 'cloud-internet-things',
                            'gen-cloud-internet-things.js')

TIERS = [(1, 11, 'Foundations'), (12, 23, 'Compounded'), (24, 34, 'Advanced')]
MAT = {'E': 'Established', 'G': 'Emerging', 'S': 'Speculative'}

BLOCK_SUB = ['fuck', 'bitch', 'cunt', 'nigger', 'faggot', 'whore', 'slut',
             'pussy', 'porn', 'xxx', 'kill yourself', 'suicide', 'facebook']
BLOCK_WORD = ['shit', 'dick']
RELIG_SUB = ['jesus', 'bible', 'quran', 'koran', 'allah']
RELIG_WORD = ['god', 'christ', 'prayer', 'prophet', 'church', 'mosque',
              'temple', 'divine', 'sacred', 'worship']
MIL_PATTERNS = ['neutraliz', 'defeat the military', 'defeat military',
                'missile defense', 'air defense system', 'kill chain',
                'how to destroy', 'disable the radar']


def fail(msg):
    print('BUILD FAIL:', msg, file=sys.stderr)
    sys.exit(1)


def check(cond, msg):
    if not cond:
        fail(msg)


def tier_of(rank):
    for lo, hi, name in TIERS:
        if lo <= rank <= hi:
            return name
    return TIERS[-1][2]


def db_name(title):
    base = title if title.lower().startswith('the ') else 'The ' + title
    return base + ' Future Technology Database'


def parse_spec(z):
    parts = [p for p in z.split('|') if p]
    check(len(parts) >= 2, 'bad demo spec: %r' % z)
    arch = parts[0]
    kv = {}
    for p in parts[1:]:
        check('=' in p, 'bad demo spec part %r in %r' % (p, z))
        k, v = p.split('=', 1)
        kv[k.strip()] = v
    return arch, kv


def num(v):
    try:
        f = float(v)
    except (ValueError, TypeError):
        fail('bad number in demo spec: %r' % (v,))
    return int(f) if f.is_integer() else f


def demo_program(rec_id, title, tier, rank, maturity, z):
    arch, kv = parse_spec(z)
    L = []
    L.append('# %s - %s' % (rec_id, title))
    L.append('# Tier: %s | Rank %d/34 | Maturity: %s' % (tier, rank, maturity))
    L.append('# Working demonstration program (real, runnable Python).')
    q = json.dumps
    if arch == 'timeline':
        year = int(num(kv['year']))
        span = int(num(kv['span']))
        events = kv['events'].split('~')
        L.append('year = %d' % year)
        L.append('span = %d' % span)
        L.append('events = %s' % q(events))
        L.append('for i, ev in enumerate(events):')
        L.append('    print(str(year + i * span) + ": " + ev)')
    elif arch == 'formula':
        a, b, op = num(kv['a']), num(kv['b']), kv['op']
        check(op in ('mul', 'div', 'add', 'sub', 'pow'), 'bad op %r' % op)
        check(not (op == 'div' and b == 0), 'div by zero in %r' % z)
        L.append('a = %r' % (a,))
        L.append('b = %r' % (b,))
        L.append("result = {'mul': a * b, 'div': a / b, 'add': a + b, "
                 "'sub': a - b, 'pow': a ** b}['%s']" % op)
        L.append('print(' + q(kv['label'] + ': ') + ' + str(result) + ' +
                 q(' ' + kv['unit']) + ')')
    elif arch == 'growth':
        start = num(kv['start'])
        pct = num(kv['rate_pct'])
        years = int(num(kv['years']))
        L.append('start = %r' % (start,))
        L.append('rate = %r' % (pct / 100.0,))
        L.append('years = %d' % years)
        L.append('v = start')
        L.append('for y in range(1, years + 1):')
        L.append('    v = v * (1 + rate)')
        L.append('    print("year " + str(y) + ": " + str(round(v, 2)) + ' +
                 q(' ' + kv['unit']) + ')')
    elif arch == 'compare':
        old, new = num(kv['old']), num(kv['new'])
        L.append('old = %r' % (old,))
        L.append('new = %r' % (new,))
        L.append('print(' + q(kv['label'] + ': ') + ' + str(old) + " -> " + '
                 'str(new) + ' + q(' ' + kv['unit']) + ')')
        L.append('if old != 0:')
        L.append('    print("change: " + str(round((new - old) / old * 100, 1)) + "%")')
        L.append('else:')
        L.append('    print("change: from zero baseline")')
    elif arch == 'convert':
        value, factor = num(kv['value']), num(kv['factor'])
        L.append('value = %r' % (value,))
        L.append('factor = %r' % (factor,))
        L.append('print(str(value) + ' + q(' ' + kv['from'] + ' = ') +
                 ' + str(value * factor) + ' + q(' ' + kv['to']) + ')')
    elif arch == 'throughput':
        units = num(kv['units'])
        per = num(kv['per_unit'])
        hours = num(kv['hours'])
        L.append('total = %r * %r * %r' % (units, per, hours))
        L.append('print("throughput: " + str(total) + ' + q(' ' + kv['unit']) + ')')
    elif arch == 'march':
        if 'steps' in kv:
            steps = int(num(kv['steps']))
            start = num(kv['start'])
            delta = num(kv['delta'])
            L.append('start = %r' % (start,))
            L.append('delta = %r' % (delta,))
            L.append('steps = %d' % steps)
            L.append('for i in range(steps):')
            L.append('    print(' + q(kv['label'] + ' step ') +
                     ' + str(i + 1) + ": " + str(start + i * delta))')
        else:
            n = int(num(kv['n']))
            L.append('n = %d' % n)
            L.append('for i in range(1, 11):')
            L.append('    print("march " + str(i * n // 10) + " / " + str(n) + ' +
                     q(' ' + kv['unit']) + ')')
    elif arch == 'score':
        items = []
        for it in kv['items'].split('~'):
            parts = it.split(':')
            check(len(parts) == 3, 'bad score item %r' % it)
            items.append((parts[0], num(parts[1]), num(parts[2])))
        L.append('items = %s' % q([[n_, w, s] for n_, w, s in items]))
        L.append('tw = sum(w for _, w, _ in items)')
        L.append('sc = sum(w * s for _, w, s in items) / tw')
        L.append('for name, w, s in items:')
        L.append('    print(name + ": weight " + str(w) + ", score " + str(s) + "/10")')
        L.append('print(' + q('weighted ' + kv['label'] + ': ') +
                 ' + str(round(sc, 2)) + "/10")')
    elif arch == 'check':
        limit, value = num(kv['limit']), num(kv['value'])
        L.append('limit = %r' % (limit,))
        L.append('value = %r' % (value,))
        L.append('print(' + q('gate "' + kv['label'] + '": ') + ' + str(value) + ' +
                 q(' ' + kv['unit'] + ' measured vs threshold ') + ' + str(limit))')
    elif arch == 'ladder':
        n = int(num(kv['n']))
        L.append('n = %d' % n)
        L.append('for r in range(1, n + 1):')
        L.append('    mark = " << frontier" if r == n else (" << origin" if r == 1 else "")')
        L.append('    print("rung " + str(r) + "/" + str(n) + ": " + ' +
                 q(kv['name']) + ' + mark)')
    else:
        fail('unknown demo archetype %r' % arch)
    L.append('print("OK")')
    return '\n'.join(L) + '\n'


def run_demo(prog, rec_id):
    try:
        cp = subprocess.run([sys.executable, '-c', prog], capture_output=True,
                            text=True, timeout=30)
    except subprocess.TimeoutExpired:
        return False, 'timeout'
    out = (cp.stdout or '') + (cp.stderr or '')
    if cp.returncode != 0:
        return False, 'exit %d: %s' % (cp.returncode, out[:300])
    if 'OK' not in (cp.stdout or ''):
        return False, 'no OK marker: %s' % out[:300]
    return True, 'ok'


REQ_KEYS = ['t', 'd', 'h', 'k', 'm', 'mj', 'r', 's', 'c', 'z']


def compose_record(d, r, rank):
    prefix = d['prefix']
    for k in REQ_KEYS:
        check(k in r and r[k], '%s rank %d missing key %s' % (d['slug'], rank, k))
    check(r['m'] in MAT, '%s rank %d bad maturity %r' % (d['slug'], rank, r['m']))
    check(isinstance(r['k'], list) and len(r['k']) >= 3,
          '%s rank %d key_points < 3' % (d['slug'], rank))
    check(isinstance(r['c'], list) and len(r['c']) >= 2,
          '%s rank %d citations < 2' % (d['slug'], rank))
    rec_id = '%s%04d' % (prefix, rank)
    tier = tier_of(rank)
    maturity = MAT[r['m']]
    prog = demo_program(rec_id, r['t'], tier, rank, maturity, r['z'])
    return {
        'id': rec_id,
        't': r['t'],
        'g': tier,
        'name': r['t'],
        'title': r['t'],
        'description': r['d'],
        'how_it_works': r['h'],
        'key_points': r['k'],
        'requirements': r['r'],
        'standards': r['s'],
        'citations': r['c'],
        'src': 'signature' if r['m'] == 'S' else 'public-harvest',
        'ladder_rank': rank,
        'ladder_tier': tier,
        'maturity': maturity,
        'maturity_justification': r['mj'],
        'demo': {'kind': 'python', 'language': 'python', 'program': prog,
                 'note': 'Working demonstration program (real, runnable Python).'},
    }


def gate_text(recs, slug):
    for r in recs:
        blob = ' '.join([
            r['t'], r['description'], r['how_it_works'],
            ' '.join(r['key_points']), ' '.join(r['requirements']),
            ' '.join(r['standards']), ' '.join(r['citations']),
            r['maturity_justification'],
        ])
        low = blob.lower()
        for w in BLOCK_SUB:
            check(w not in low, '%s %s: blocklist %r' % (slug, r['id'], w))
        for w in BLOCK_WORD:
            check(not re.search(r'\b%s\b' % w, low),
                  '%s %s: blocklist word %r' % (slug, r['id'], w))
        for w in RELIG_SUB:
            check(w not in low, '%s %s: religious term %r' % (slug, r['id'], w))
        for w in RELIG_WORD:
            if w == 'god':
                # "god game"/"god-game" is an established video game genre, not framing
                pat = r'\bgod\b(?!\s*-?\s*game)'
            else:
                pat = r'\b%s\b' % w
            check(not re.search(pat, low),
                  '%s %s: religious framing %r' % (slug, r['id'], w))
        for w in MIL_PATTERNS:
            check(w not in low,
                  '%s %s: military-neutralization pattern %r' % (slug, r['id'], w))
        check('http://' not in blob and 'https://' not in blob,
              '%s %s: URL reference' % (slug, r['id']))
        check('<script' not in low and 'javascript:' not in low,
              '%s %s: injection pattern' % (slug, r['id']))


def check_prefixes(datas):
    man = json.load(open(MANIFEST, encoding='utf-8'))
    existing = []
    for db in man.get('databases', []):
        p = db.get('id_prefix')
        if p:
            existing.append(p)
    for d in datas:
        p = d['prefix']
        check(p not in existing, 'prefix exact collision: %s' % p)
        for e in existing:
            check(p not in e and e not in p,
                  'prefix substring collision: %s vs %s' % (p, e))
    seen = set()
    for d in datas:
        check(d['prefix'] not in seen, 'batch prefix dup: %s' % d['prefix'])
        seen.add(d['prefix'])


def esc(s):
    import html as htmlmod
    return htmlmod.escape(str(s), quote=True)


def tier_titles(recs, lo, hi):
    return [r['t'] for r in recs if lo <= r['ladder_rank'] <= hi]


MAT_BADGE_JS = """
function matBadge(r){
  var m=r&&r.maturity;
  if(m==='Established')return '<span class="badge" style="background:#0d3b24;border-color:#00e5a0;color:#a7f3d0">Established</span>';
  if(m==='Emerging')return '<span class="badge" style="background:#3d2c0d;border-color:#ffb020;color:#ffe1a8">Emerging</span>';
  if(m==='Speculative')return '<span class="badge sig">Speculative</span>';
  return '';
}
"""


def build_page(d, recs):
    slug = d['slug']
    dbname = db_name(d['title'])
    tagline = d['tagline']
    kind = d['kind']
    ai_name = d['ai']
    prefix = d['prefix']
    page = open(EXEMPLAR_PAGE, encoding='utf-8').read()

    def rep(old, new, count=1):
        nonlocal page
        check(old in page, '%s: template token missing: %r' % (slug, old[:60]))
        page = page.replace(old, new, count)

    # head
    rep('<title>The Cloud and Internet Things Database \u2014 JAH Databases</title>',
        '<title>%s \u2014 JAH Databases</title>' % esc(dbname))
    m = re.search(r'<meta name="description" content="[^"]*">', page)
    check(m, '%s: meta description not found' % slug)
    page = page.replace(m.group(0),
                        '<meta name="description" content="%s Property of Justin Addam Higgins (JAH).">' % esc(tagline),
                        1)
    m = re.search(r'<script type="application/ld\+json">.*?</script>', page, re.DOTALL)
    check(m, '%s: JSON-LD not found' % slug)
    ld = {"@context": "https://schema.org", "@type": "Dataset", "name": dbname,
          "description": tagline,
          "creator": {"@type": "Person", "name": "Justin Addam Higgins"}}
    page = page.replace(m.group(0),
                        '<script type="application/ld+json">%s</script>' % json.dumps(ld),
                        1)
    # hero
    rep('<h1>The Cloud and Internet Things Database</h1>',
        '<h1>%s</h1>' % esc(dbname))
    m = re.search(r'</h1>\s*<p>.*?</p>', page, re.DOTALL)
    check(m, '%s: hero paragraph not found' % slug)
    f_t = tier_titles(recs, 1, 11)
    c_t = tier_titles(recs, 12, 23)
    a_t = tier_titles(recs, 24, 34)
    hero = ('%s %s. Every record carries the full entry: description, how it works, '
            'key points, requirements, standards, citations, maturity labeling '
            '(Established / Emerging / Speculative), and a working demonstration program. '
            'Records are ordered by the teaching ladder: Foundations (%s) -&gt; Compounded (%s) '
            '-&gt; Advanced (%s).') % (
                esc(tagline), esc(d['scope']),
                esc('; '.join(f_t)), esc('; '.join(c_t)), esc('; '.join(a_t)))
    page = page.replace(m.group(0), '</h1>\n      <p>%s</p>' % hero, 1)
    # stats + type
    rep('jahdb-cloud-internet-things-1.0', 'jahdb-%s-1.0' % slug)
    rep('<span class="stat">Type: <b>Public records organized in the Signature system</b></span>',
        '<span class="stat">Type: <b>Future technology records in the Signature system</b></span>')
    # global name / slug swaps
    rep('The Cloud and Internet Things Database', esc(dbname), page.count('The Cloud and Internet Things Database'))
    rep('cloud-internet-things', slug, page.count('cloud-internet-things'))
    rep('JAH Cloud and Internet Things Archivist', esc(ai_name),
        page.count('JAH Cloud and Internet Things Archivist'))
    rep("'cloud and internet record'", "'%s'" % kind.replace("'", "\\'"))
    # search placeholder
    m = re.search(r'placeholder="Search [^"]*"', page)
    check(m, '%s: search placeholder not found' % slug)
    kw = ', '.join(t.split(':')[0].split('-')[0].strip() for t in
                   [r['t'] for r in recs[:14]])
    page = page.replace(m.group(0), 'placeholder="Search %s..."' % esc(kw[:220]), 1)
    # generator card
    rep('Generate clearly-labeled cloud and internet studies.',
        'Generate clearly-labeled future technology studies.')
    # chat
    rep('placeholder="Ask about cloud and internet things..."',
        'placeholder="Ask about %s..."' % esc(d['title'].lower()))
    role = ('%s - %s; teaching progressively along the ladder from foundations '
            'through compounded to advanced; answers from many angles - definition, '
            'example, analogy, application, history, math, how-to - using only archive '
            'data from this system') % (kind, tagline)
    m = re.search(r"var ROLE='.*?';", page)
    check(m, '%s: ROLE var not found' % slug)
    page = page.replace(m.group(0), "var ROLE=%s;" % json.dumps(role), 1)
    greet = ('I am the %s. Ask me about %s - from %s through %s to %s.') % (
        ai_name, d['title'].lower(), f_t[0], c_t[0], a_t[-1])
    m = re.search(r"'I am the " + re.escape(ai_name) + r"\..*?future internet\.'",
                  page, re.DOTALL)
    check(m, '%s: greet text not found' % slug)
    page = page.replace(m.group(0), "'" + greet.replace("'", "\\'") + "'", 1)
    rep("'JAH-SI-'", "'%s'" % prefix)
    # about section
    rep('<dt>Archive</dt><dd>Seeded public-record cloud and internet things records, '
        'marching toward one million records. Presented in teaching-ladder order: '
        'foundations, compounded, advanced.</dd>',
        '<dt>Archive</dt><dd>Seeded %s tracing the technology from its oldest form '
        'to the working version, marching toward one million records. Presented in '
        'teaching-ladder order: foundations, compounded, advanced.</dd>' % esc(kind + 's'))
    rep('<dt>Record schema</dt><dd class="mono">id, t, g, name, title, description, '
        'how_it_works, key_points, requirements, standards, citations, src, ladder_rank, '
        'ladder_tier, demo</dd>',
        '<dt>Record schema</dt><dd class="mono">id, t, g, name, title, description, '
        'how_it_works, key_points, requirements, standards, citations, src, ladder_rank, '
        'ladder_tier, maturity, maturity_justification, demo</dd>'
        '<dt>Maturity labeling</dt><dd>Every record carries a maturity label: Established '
        '(fact-checked real data), Emerging (real technology still developing), or '
        'Speculative (Signature-generated speculative projection \u2014 not established fact).</dd>')
    rep('jahdb-%s-1.0 \u2014 Generate clearly-labeled cloud and internet studies. '
        'Seeded archive records are the authoritative entries.' % slug,
        'jahdb-%s-1.0 \u2014 Generate clearly-labeled future technology studies. '
        'Seeded archive records are the authoritative entries.' % slug)
    m = re.search(r'<dt>AI</dt><dd>' + re.escape(ai_name) + r' \u2014 .*?</dd>',
                  page, re.DOTALL)
    check(m, '%s: AI dd not found' % slug)
    page = page.replace(m.group(0),
                        '<dt>AI</dt><dd>%s \u2014 %s \u2014 and aware of the whole JAH '
                        'Databases network through cross-database reasoning. On-device '
                        'Standard 1.0, no key needed; uses the shared Signature backend '
                        'automatically when configured.</dd>' % (esc(ai_name), esc(role)), 1)
    rep('<dt>Signature system</dt><dd>Public records organized in the Signature system. '
        'Property of Justin Addam Higgins (JAH).</dd>',
        '<dt>Signature system</dt><dd>Future technology records organized in the Signature '
        'system. Property of Justin Addam Higgins (JAH).</dd>')
    rep('<div class="foot">JAH Databases. Public records organized in the Signature '
        'system. Property of Justin Addam Higgins (JAH).</div>',
        '<div class="foot">JAH Databases. Future technology records organized in the '
        'Signature system. Property of Justin Addam Higgins (JAH).</div>')
    # maturity badges on browse cards
    rep('function sigBadge(r){', MAT_BADGE_JS + '\nfunction sigBadge(r){')
    rep("'<div><span class=\"badge mono\">'+esc(r.id||'')+'</span><span class=\"badge\">'+esc(catOf(r))+'</span></div>'",
        "'<div><span class=\"badge mono\">'+esc(r.id||'')+'</span>'+matBadge(r)+'<span class=\"badge\">'+esc(catOf(r))+'</span></div>'")
    # canon tokens
    for token in ['id="stCount"', 'Exhaustive', 'All Database Merger', 'mergePanel',
                  'dataset.p', 'codeblock', 'minmax(120px,1fr)']:
        check(token in page, '%s page missing %s' % (slug, token))
    check('facebook' not in page.lower(), '%s page mentions facebook' % slug)
    return page, dbname


def js_str(s):
    return json.dumps(s)


def build_gen_js(d, recs):
    slug = d['slug']
    dbname = db_name(d['title'])
    prefix = d['prefix']
    kind = d['kind']
    js = open(EXEMPLAR_GEN, encoding='utf-8').read()

    def rep(old, new, count=1):
        nonlocal js
        check(old in js, '%s: gen template token missing: %r' % (slug, old[:60]))
        js = js.replace(old, new, count)

    rep('/* JAH The Cloud and Internet Things Database generator \u2014 jahdb-cloud-internet-things-1.0.',
        '/* JAH %s generator \u2014 jahdb-%s-1.0.' % (dbname, slug))
    rep('var PREFIX="JAH-CIT-";', 'var PREFIX=%s;' % js_str(prefix))
    m = re.search(r'var TOPICS=\{.*?\n\};', js, re.DOTALL)
    check(m, '%s: TOPICS block not found' % slug)
    topics = {}
    for lo, hi, tname in TIERS:
        topics[tname] = ['%s - %s' % (r['t'], tname)
                         for r in recs if lo <= r['ladder_rank'] <= hi]
    tjs = 'var TOPICS={\n' + ',\n'.join(
        ' %s: [\n%s\n ]' % (js_str(tname), ',\n'.join(
            '  %s' % js_str(t) for t in topics[tname]))
        for tname in [t[2] for t in TIERS]) + '\n};'
    js = js.replace(m.group(0), tjs, 1)
    rep('"# Cloud Internet Study \u2014 "', '"# Future Technology Study \u2014 "')
    rep("name:topic+' \u2014 cloud and internet record'",
        "name:topic+' \u2014 %s'" % kind)
    rep("A cloud and internet record of", "A %s of" % kind)
    rep('demo:{kind:"cloud-internet-demo"', 'demo:{kind:"%s-demo"' % slug)
    rep('jahdb-cloud-internet-things-1.0', 'jahdb-%s-1.0' % slug,
        js.count('jahdb-cloud-internet-things-1.0'))
    rep("String(seed).padStart(6,'0')", "String(seed).padStart(4,'0')")
    rep('d{6}$', 'd{4}$')
    rep("JAHDB.registerGenerator('cloud-internet-things',gen)",
        "JAHDB.registerGenerator('%s',gen)" % slug)
    check('facebook' not in js.lower(), '%s gen mentions facebook' % slug)
    return js


def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')


def build_tech(d, sys_titles, only=None):
    slug = d['slug']
    if only and slug != only:
        return None
    check(len(d['records']) == 34, '%s: %d records' % (slug, len(d['records'])))
    recs = [compose_record(d, r, i + 1) for i, r in enumerate(d['records'])]
    check([r['ladder_rank'] for r in recs] == list(range(1, 35)),
          '%s: ladder ranks broken' % slug)
    check(len({r['id'] for r in recs}) == 34, '%s: dup ids' % slug)
    for r in recs:
        check(r['t'] not in sys_titles, 'system title dup: %s' % r['t'])
        sys_titles.add(r['t'])
    gate_text(recs, slug)
    ndemo = 0
    for r in recs:
        ok, out = run_demo(r['demo']['program'], r['id'])
        check(ok, 'demo failed for %s: %s' % (r['id'], out[:300]))
        ndemo += 1
    # page + generator
    db_dir = os.path.join(ROOT_DB, 'db', slug)
    os.makedirs(db_dir, exist_ok=True)
    page, dbname = build_page(d, recs)
    with open(os.path.join(db_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    gen_js = build_gen_js(d, recs)
    gen_path = os.path.join(db_dir, 'gen-%s.js' % slug)
    with open(gen_path, 'w', encoding='utf-8') as f:
        f.write(gen_js)
    cp = subprocess.run(['node', '--check', gen_path],
                        capture_output=True, text=True)
    check(cp.returncode == 0,
          'node --check failed for %s: %s' % (slug, cp.stderr[:300]))
    # data shards
    data_dir = os.path.join(ROOT_DATA, 'data', slug)
    write_gz_jsonl(os.path.join(data_dir, 'index.jsonl.gz'),
                   [{'id': r['id'], 't': r['t'], 'g': r['g']} for r in recs])
    write_gz_jsonl(os.path.join(data_dir, 'chunks', 'chunk-0000.jsonl.gz'), recs)
    # fragment
    os.makedirs(FRAG_DIR, exist_ok=True)
    local_index = DATA_DOMAIN + slug + '/index.jsonl.gz'
    frag = {
        'slug': slug,
        'name': dbname,
        'tagline': d['tagline'],
        'record_kind': d['kind'],
        'id_prefix': d['prefix'],
        'ai_name': d['ai'],
        'local_index': local_index,
        'record_count': 34,
        'status': 'live',
        'full_records': 34,
        'index': local_index,
        'chunk_pattern': 'data/%s/chunks/chunk-NNNN.jsonl.gz' % slug,
        'source': 'mixed',
    }
    with open(os.path.join(FRAG_DIR, slug + '.json'), 'w', encoding='utf-8') as f:
        json.dump(frag, f, ensure_ascii=False, indent=1)
    # per-DB build dir
    bdir = os.path.join(ROOT_DB, 'code', slug + '-build')
    os.makedirs(bdir, exist_ok=True)
    with open(os.path.join(bdir, 'data.json'), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    with open(os.path.join(bdir, 'build.sh'), 'w', encoding='utf-8') as f:
        f.write('#!/bin/sh\n# Rebuild this database from its staged content.\n'
                '# Property of Justin Addam Higgins (JAH).\n'
                'python3 %s --only %s\n' % (os.path.join(BUILD_DIR, 'build_single.py'), slug))
    os.chmod(os.path.join(bdir, 'build.sh'), 0o755)
    return {'slug': slug, 'name': dbname, 'records': 34, 'demos': ndemo,
            'maturity': {m: sum(1 for r in recs if r['maturity'] == m)
                         for m in ('Established', 'Emerging', 'Speculative')}}


def main():
    args = sys.argv[1:]
    only = None
    if args == ['--all']:
        pass
    elif len(args) == 2 and args[0] == '--only':
        only = args[1]
    else:
        fail('usage: build_single.py --all | --only <slug>')
    files = sorted(glob.glob(os.path.join(DATA_DIR, 'ft*.json')),
                   key=lambda f: int(re.search(r'ft(\d+)\.json', f).group(1)))
    check(len(files) == 50, 'need exactly 50 data files, got %d' % len(files))
    datas = []
    for f in files:
        d = json.load(open(f, encoding='utf-8'))
        for k in ('num', 'title', 'slug', 'prefix', 'ai', 'kind', 'scope',
                  'tagline', 'records'):
            check(k in d, '%s missing key %s' % (f, k))
        check(51 <= d['num'] <= 100, '%s num out of range' % f)
        check(d['slug'] == 'futuretech-%d-%s' % (d['num'], d['slug'].split('futuretech-%d-' % d['num'], 1)[1]),
              '%s slug/num mismatch' % f)
        datas.append(d)
    check_prefixes(datas)
    sys_titles = set(json.load(open(TITLES_JSON, encoding='utf-8')))
    print('system titles loaded: %d' % len(sys_titles), flush=True)
    results = []
    for d in datas:
        r = build_tech(d, sys_titles, only=only)
        if r:
            results.append(r)
            print('OK %s records=%d demos=%d maturity=%s' %
                  (r['slug'], r['records'], r['demos'], r['maturity']), flush=True)
    report = {
        'built': len(results),
        'databases': results,
        'total_records': sum(r['records'] for r in results),
        'total_demos': sum(r['demos'] for r in results),
    }
    with open(os.path.join(BUILD_DIR, 'build-report.json'), 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print('TOTAL databases=%d records=%d demos=%d' %
          (len(results), report['total_records'], report['total_demos']))


if __name__ == '__main__':
    main()
