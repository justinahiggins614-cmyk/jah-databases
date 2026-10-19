#!/usr/bin/env python3
"""Build the Retail Commerce Operations database pair for JAH Databases (5,000-target program).

Dedupe gate: every record title is checked against the WHOLE system with
code/dedupe_gate.py BEFORE writing (his standing rule: no time limit,
correctness first). ID prefixes verified free: zero hits in manifest
id_prefix values (exact + substring) and zero hits in shard record IDs.

So this build creates two NEW databases, 34 ladder-ordered records each:
  retail-commerce-operations              - The Retail Commerce Operations Database
  retail-commerce-operations-signature          - The Retail Commerce Operations Signature Database

34 records each, ladder-ordered 1-34 (Foundations 1-12 / Compounded 13-23 /
Advanced 24-34); the shard index is written in ladder order so pages present
simple -> compounded -> complex.

Numerical cores: all hand-computed, machine-verified by the demos
(see demos_*.py). Every demo prints its real computed values, asserts tight
bounds (never float exact-equality), and ends with the OK marker; the build
machine-executes every demo.

Writes (this builder's scope ONLY - a coordinator merges the rest):
  main repo : db/<slug>/index.html + gen-<slug>.js
              db/<slug>-signature/index.html + gen-<slug>-signature.js
  shard repo: data/<slug>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/<slug>-signature/... (same)
  build dir : code/<slug>-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/<slug>.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes. Fragment status is
"staged" - never "live" (the coordinator marks live).

No website references. No Facebook. Nothing hate-adjacent, profane,
inappropriate, or religiously framed.
"""
import gzip
import importlib
import json
import os
import re
import subprocess
import sys

# ---------------- pair parameters ----------------
P = {
 'slug': 'retail-commerce-operations',
 'sig_slug': 'retail-commerce-operations-signature',
 'name': 'The Retail Commerce Operations Database',
 'signame': 'The Retail Commerce Operations Signature Database',
 'prefix': 'JAH-RTCO-',
 'sigprefix': 'JAH-RTCOS-',
 'ai': 'JAH Retail Commerce Archivist',
 'sigai': 'JAH Retail Commerce Archivist (Signature)',
 'kind': 'retail operations record',
 'genver': 'jahdb-retail-commerce-operations-1.0',
 'demokind': 'retail-demo',
 'tagline': 'The full retail industry: product catalogs and SKU systems, pricing strategy, inventory management, point-of-sale systems, merchandising, e-commerce and omnichannel fulfillment, returns, loyalty programs, and retail analytics - every record a complete operational file taught progressively along the ladder.',
 'sigtagline': 'His original Signature Retail Method: every SKU a sworn sign, every shelf a sealed aisle, every price a covenant with the customer, every return a kept promise - the full ladder from the storefront through catalogs, pricing, inventory, and fulfillment to analytics and the mastery review, reframed as Signature science. Clearly labeled Signature-made, never presented as authentic public record.',
 'hero': 'The full retail industry: product catalogs and SKU systems, pricing strategy, inventory management, point-of-sale systems, merchandising, e-commerce and omnichannel fulfillment, returns, loyalty programs, and retail analytics - every record a complete operational file taught progressively along the ladder. - Public records - real, fact-checked retail operations: what retail commerce is, the product catalog and SKU system, barcodes and GTINs, pricing strategy, the point of sale, payment processing, store layout, inventory basics, receiving goods, customer service, merchandising, retail math, demand forecasting, purchase orders and replenishment, EOQ, markdowns and promotions, planograms, e-commerce operations, omnichannel fulfillment, warehousing, returns and reverse logistics, loyalty programs, loss prevention, retail analytics, market basket analysis, category management, private label, supply chain management, labor scheduling, site selection, RFID and automation, open-to-buy planning, franchise operations, and a mastery review - every record carrying the full entry: description, how it works, key points, requirements, standards, citations, and a working demonstration program. Records are ordered by the teaching ladder: Foundations (what retail commerce is, product catalogs, barcodes, pricing strategy, the POS system, payment processing, store layout, inventory basics, receiving, customer service, merchandising, retail math) -&gt; Compounded (demand forecasting, purchase orders, EOQ, markdowns, planograms, e-commerce, omnichannel fulfillment, warehousing, returns, loyalty programs, loss prevention) -&gt; Advanced (retail analytics, basket analysis, category management, private label, supply chain, labor scheduling, site selection, RFID, seasonal planning, franchise operations, mastery review).',
 'sighero': 'His original Signature Retail Method: every SKU a sworn sign, every shelf a sealed aisle, every price a covenant with the customer, every return a kept promise - the full ladder from the storefront through catalogs, pricing, inventory, and fulfillment to analytics and the mastery review, reframed as Signature science. Clearly labeled Signature-made, never presented as authentic public record. - Signature records - his original Signature treatment of the retail industry, marching the same ladder as the public edition: foundations, compounded, advanced - every record carrying the full entry: description, how it works, key points, requirements, standards, citations, and a working demonstration program.',
 'role': 'Retail commerce archivist - teaching the full retail industry from product catalogs, SKUs, barcodes, pricing, the point of sale, and store operations through inventory, forecasting, e-commerce, fulfillment, and returns to analytics, category management, supply chain, and the mastery review; teaching progressively along the ladder from foundations through compounded to advanced; answers from many angles - definition, example, calculation, operation, standards, application - using only archive data from this system',
 'sigrole': 'Signature retail archivist - teaching his original Signature Retail Method from the sworn SKU and sealed aisle through pricing covenants, inventory oaths, fulfillment promises, and analytics seals to the mastery review; teaching progressively along the ladder from foundations through compounded to advanced; answers from many angles - definition, example, calculation, operation, standards, application - using only archive data from this system; clearly labeled Signature-made, never presented as authentic public record',
 'searchph': 'Search SKUs, pricing, inventory, POS, merchandising, e-commerce, returns, loyalty, analytics...',
 'chatph': 'Ask about retail operations...',
 'greet': 'I am the JAH Retail Commerce Archivist. Ask me about retail - from product catalogs, SKUs, pricing, and the point of sale through inventory, forecasting, e-commerce, and fulfillment to analytics and the full operation.',
 'siggreet': 'I am the JAH Retail Commerce Archivist (Signature). Ask me about the Signature Retail Method - every SKU a sworn sign, every shelf a sealed aisle, every price a covenant.',
 'gendesc': 'Generate clearly-labeled retail operations studies. Seeded archive records are the authoritative entries.',
 'siggendesc': 'Generate clearly-labeled Signature retail studies. Seeded archive records are the authoritative entries.',
 'archdesc': 'Seeded public-record retail operations records, marching toward one million records. Presented in teaching-ladder order: foundations, compounded, advanced.',
 'sigarchdesc': 'Seeded Signature-made retail operations records, marching toward one million records. Presented in teaching-ladder order: foundations, compounded, advanced.',
}

REPO = os.path.expanduser('~/workspace/jah-databases')
DATAREPO = os.path.expanduser('~/workspace/jah-databases-data-1')
FRAGDIR = os.path.expanduser('~/workspace/hidden_files/missing-builds/fragments')
REF_HTML = os.path.join(REPO, 'db', 'language-pashto', 'index.html')
REF_JS = os.path.join(REPO, 'db', 'language-pashto', 'gen-language-pashto.js')
BASEURL = 'https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/'

BLOCKLIST = ['fuck', 'shit', 'bitch', 'whore', 'slut', 'nigger', 'faggot',
             'cunt', 'dick ', 'porn', 'facebook', 'bat belt']


def rep_once(h, old, new):
    assert old in h, 'anchor missing: %r' % old[:80]
    assert h.count(old) == 1, 'anchor not unique: %r' % old[:80]
    return h.replace(old, new, 1)


def build_html(ref, ed):
    """ed: dict with slug,name,prefix,ai,kind,genver,demokind,tagline,hero,role,
    searchph,chatph,greet,gendesc,archdesc,aid, local (LOCAL url), sigmode(bool)."""
    h = ref
    # meta description
    h2, n = re.subn(r'<meta name="description" content="[^"]*">',
                    '<meta name="description" content="%s Property of Justin Addam Higgins.">' % ed['tagline'],
                    h, count=1)
    assert n == 1, 'meta description anchor'
    h = h2
    # JSON-LD
    ld = {'@context': 'https://schema.org', '@type': 'Dataset', 'name': ed['name'],
          'description': ed['tagline'],
          'creator': {'@type': 'Person', 'name': 'Justin Addam Higgins'}}
    h2, n = re.subn(r'<script type="application/ld\+json">.*?</script>',
                    '<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False),
                    h, count=1, flags=re.S)
    assert n == 1, 'json-ld anchor'
    h = h2
    # hero paragraph
    h2, n = re.subn(r'<p>Learn Pashto from the ground up:.*?</p>',
                    '<p>%s</p>' % ed['hero'], h, count=1, flags=re.S)
    assert n == 1, 'hero anchor'
    h = h2
    h = rep_once(h, '<title>The Pashto Language Database — JAH Databases</title>',
                 '<title>%s — JAH Databases</title>' % ed['name'])
    h = rep_once(h, '<h1>The Pashto Language Database</h1>', '<h1>%s</h1>' % ed['name'])
    assert h.count('jahdb-language-pashto-1.0') == 2, 'genver count'
    h = h.replace('jahdb-language-pashto-1.0', ed['genver'])
    h = rep_once(h, '<script src="gen-language-pashto.js"></script>',
                 '<script src="gen-%s.js"></script>' % ed['slug'])
    h = rep_once(h, "var SLUG='language-pashto';", "var SLUG='%s';" % ed['slug'])
    h = rep_once(h, "var LOCAL='https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/language-pashto/';",
                 "var LOCAL='%s';" % ed['local'])
    h = rep_once(h, "name:'The Pashto Language Database',", "name:'%s'," % ed['name'])
    h = rep_once(h, "ai_name:'JAH Pashto Language Archivist',", "ai_name:'%s'," % ed['ai'])
    h = rep_once(h, "record_kind:'language learning record'}", "record_kind:'%s'}" % ed['kind'])
    h2, n = re.subn(r"var ROLE='.*?';", "var ROLE='%s';" % ed['role'], h, count=1)
    assert n == 1, 'ROLE anchor'
    h = h2
    h = rep_once(h, 'placeholder="Search Pashto letters, words, verbs, tenses, phrases, grammar, dialogues..."',
                 'placeholder="%s"' % ed['searchph'])
    h = rep_once(h, '<h3>The Pashto Language Database generator</h3>',
                 '<h3>%s generator</h3>' % ed['name'])
    h = rep_once(h, '<p class="dim">Generate clearly-labeled Pashto language studies. Seeded archive records are the authoritative entries.</p>',
                 '<p class="dim">%s</p>' % ed['gendesc'])
    h = rep_once(h, 'placeholder="Ask about Pashto..."', 'placeholder="%s"' % ed['chatph'])
    h = rep_once(h, '<h3>JAH Pashto Language Archivist ', '<h3>%s ' % ed['ai'])
    h = rep_once(h, 'I am the JAH Pashto Language Archivist. Ask me about Pashto - from the 44-letter alphabet and sounds through core words, grammar, and everyday sentences to stories, idioms, and conversations.',
                 ed['greet'])
    h = rep_once(h, 'Seeded public-record Pashto language records, marching toward one million records. Presented in teaching-ladder order: foundations, compounded, advanced.',
                 ed['archdesc'])
    assert h.count(' — Generate clearly-labeled Pashto language studies. Seeded archive records are the authoritative entries.') == 1
    h = h.replace(' — Generate clearly-labeled Pashto language studies. Seeded archive records are the authoritative entries.',
                  ' — %s' % ed['gendesc'])
    h2, n = re.subn(r'<dt>AI</dt><dd>.*?</dd>',
                    '<dt>AI</dt><dd>%s — %s</dd>' % (ed['ai'], ed['role']), h, count=1, flags=re.S)
    assert n == 1, 'AI dd anchor'
    h = h2
    h = rep_once(h, "JAHDB.emblemSVG(db.name,'JAH-SI-')",
                 "JAHDB.emblemSVG(db.name,'%s')" % ed['prefix'])
    if ed['sigmode']:
        assert h.count('Public records organized in the Signature system') == 3, 'sigmode public-phrase count'
        h = h.replace('Public records organized in the Signature system',
                      'Signature-made records in the Signature system')
        h = rep_once(h, 'Seeded Signature-made', 'Seeded Signature-made')  # no-op guard
    # leak checks: no leftover reference-domain text
    for leak in ['Pashto', 'pashto', 'JAH-LPUS-', 'language-pashto']:
        assert leak not in h, 'LEAK in html: %r' % leak
    return h


def build_js(ref_js, ed, topics):
    j = ref_js

    def rep1(old, new):
        nonlocal j
        assert old in j, 'js anchor missing: %r' % old[:80]
        j = j.replace(old, new, 1)

    rep1('/* JAH The Pashto Language Database generator — jahdb-language-pashto-1.0.',
         '/* JAH %s generator — %s.' % (ed['name'], ed['genver']))
    rep1('var PREFIX="JAH-LPUS-";', 'var PREFIX="%s";' % ed['prefix'])
    assert j.count('jahdb-language-pashto-1.0') == 1, 'js genver count'
    j = j.replace('jahdb-language-pashto-1.0', ed['genver'])
    rep1("JAHDB.registerGenerator('language-pashto',gen);",
         "JAHDB.registerGenerator('%s',gen);" % ed['slug'])
    rep1("name:topic+' — language learning record',", "name:topic+' — %s'," % ed['kind'])
    rep1('A language learning record of', 'A %s of' % ed['kind'])
    rep1('demo:{kind:"pashto-demo",', 'demo:{kind:"%s",' % ed['demokind'])
    # TOPICS block
    lines = ['var TOPICS={']
    for tier in ['Foundations', 'Compounded', 'Advanced']:
        lines.append(' "%s": [' % tier)
        for t in topics[tier]:
            safe = t.replace('\\', '\\\\').replace('"', "'")
            lines.append('  "%s - %s",' % (safe, tier))
        lines.append(' ],')
    lines.append('};')
    topics_block = '\n'.join(lines)
    j2, n = re.subn(r'var TOPICS=\{.*?\n\};', lambda _m: topics_block, j, count=1, flags=re.S)
    assert n == 1, 'TOPICS anchor'
    j = j2
    # demoProgram -> domain calculator (replacement fn: backslashes must survive)
    demofn = ed['demofn']
    j2, n = re.subn(r'function demoProgram\(topic,field\)\{.*?\n\}\n(?=function generate)',
                    lambda _m: demofn, j, count=1, flags=re.S)
    assert n == 1, 'demoProgram anchor'
    j = j2
    for leak in ['Pashto', 'pashto', 'JAH-LPUS-', 'language-pashto', 'language learning record']:
        assert leak not in j, 'LEAK in js: %r' % leak
    return j


def write_gz(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')


def run_demo(prog, rid):
    p = subprocess.run([sys.executable, '-c', prog], capture_output=True, text=True, timeout=120)
    ok = (p.returncode == 0) and ('OK:' in p.stdout)
    return ok, p.stdout, p.stderr


def content_gate(text, where):
    low = text.lower()
    for b in BLOCKLIST:
        assert b not in low, 'CONTENT GATE: %r found in %s' % (b, where)


def main():
    slugmod = 'entries_' + P['slug'].replace('-', '_')
    demomod = 'demos_' + P['slug'].replace('-', '_')
    entries = importlib.import_module(slugmod)
    demos = importlib.import_module(demomod)
    PUB, SIG = entries.PUB, entries.SIG
    assert len(PUB) == 34 and len(SIG) == 34, 'need 34+34 entries, got %d+%d' % (len(PUB), len(SIG))

    # ---- dedupe gate: whole system, before writing anything ----
    sys.path.insert(0, os.path.join(REPO, 'code'))
    from dedupe_gate import DedupeGate
    gate = DedupeGate(os.path.join(REPO, 'data', 'dedupe', 'exact'))

    def make(prefix, idx, e, src, sigtitle=False):
        rid = '%s%06d' % (prefix, idx)
        title = e['t'] + (' (Signature Edition)' if sigtitle else '')
        prog = demos.build(e['dk'], title, rid, e['tier'], e['data'])
        return {
            'id': rid, 't': title, 'g': e['tier'], 'name': title, 'title': title,
            'description': e['desc'], 'how_it_works': e['how'],
            'key_points': e['kp'], 'requirements': e['req'],
            'standards': e['std'], 'citations': e['cit'], 'src': src,
            'ladder_rank': e['rank'], 'ladder_tier': e['tier'].lower(),
            'demo': {'kind': 'python', 'language': 'python', 'program': prog,
                     'note': 'Working demonstration program (real, runnable Python).'},
        }

    pubrecs = [make(P['prefix'], i + 1, e, 'public-harvest') for i, e in enumerate(PUB)]
    sigrecs = [make(P['sigprefix'], i + 1, e, 'signature', sigtitle=True) for i, e in enumerate(SIG)]

    dupe_hits = []
    for slug, recs in ((P['slug'], pubrecs), (P['sig_slug'], sigrecs)):
        for r in recs:
            hits = gate.check(slug, r['title'])
            if hits:
                dupe_hits.append((r['title'], hits))
            gate.admit(slug, r['title'], r['id'])
    assert not dupe_hits, 'WHOLE-SYSTEM DUPES: %r' % dupe_hits[:5]

    # ---- machine-execute every demo ----
    for r in pubrecs + sigrecs:
        ok, out, err = run_demo(r['demo']['program'], r['id'])
        assert ok, 'DEMO FAIL %s\nSTDOUT:\n%s\nSTDERR:\n%s' % (r['id'], out[-2000:], err[-2000:])
    print('demos: %d/%d passed' % (len(pubrecs) + len(sigrecs), len(pubrecs) + len(sigrecs)))

    # ---- content gate ----
    for r in pubrecs + sigrecs:
        content_gate(json.dumps(r, ensure_ascii=False), r['id'])

    # ---- write shard data ----
    for slug, recs in ((P['slug'], pubrecs), (P['sig_slug'], sigrecs)):
        ddir = os.path.join(DATAREPO, 'data', slug)
        write_gz(os.path.join(ddir, 'index.jsonl.gz'),
                 [{'id': r['id'], 't': r['t'], 'g': r['g']} for r in recs])
        write_gz(os.path.join(ddir, 'chunks', 'chunk-0000.jsonl.gz'), recs)
    print('shard data written: %s, %s' % (P['slug'], P['sig_slug']))

    # ---- build pages + generators from the merged reference pair ----
    with open(REF_HTML, encoding='utf-8') as f:
        ref_html = f.read()
    with open(REF_JS, encoding='utf-8') as f:
        ref_js = f.read()

    def ed_pub():
        return {'slug': P['slug'], 'name': P['name'], 'prefix': P['prefix'],
                'ai': P['ai'], 'kind': P['kind'], 'genver': P['genver'],
                'demokind': P['demokind'], 'tagline': P['tagline'], 'hero': P['hero'],
                'role': P['role'], 'searchph': P['searchph'], 'chatph': P['chatph'],
                'greet': P['greet'], 'gendesc': P['gendesc'], 'archdesc': P['archdesc'],
                'local': BASEURL + P['slug'] + '/', 'sigmode': False,
                'demofn': entries.GEN_DEMOFN}

    def ed_sig():
        return {'slug': P['sig_slug'], 'name': P['signame'], 'prefix': P['sigprefix'],
                'ai': P['sigai'], 'kind': P['kind'], 'genver': P['genver'],
                'demokind': P['demokind'], 'tagline': P['sigtagline'], 'hero': P['sighero'],
                'role': P['sigrole'], 'searchph': P['searchph'], 'chatph': P['chatph'],
                'greet': P['siggreet'], 'gendesc': P['siggendesc'], 'archdesc': P['sigarchdesc'],
                'local': BASEURL + P['sig_slug'] + '/', 'sigmode': True,
                'demofn': entries.GEN_DEMOFN}

    topics_pub = {'Foundations': [e['t'] for e in PUB if e['tier'] == 'Foundations'],
                  'Compounded': [e['t'] for e in PUB if e['tier'] == 'Compounded'],
                  'Advanced': [e['t'] for e in PUB if e['tier'] == 'Advanced']}
    topics_sig = {'Foundations': [e['t'] + ' (Signature Edition)' for e in SIG if e['tier'] == 'Foundations'],
                  'Compounded': [e['t'] + ' (Signature Edition)' for e in SIG if e['tier'] == 'Compounded'],
                  'Advanced': [e['t'] + ' (Signature Edition)' for e in SIG if e['tier'] == 'Advanced']}

    for ed, topics in ((ed_pub(), topics_pub), (ed_sig(), topics_sig)):
        html = build_html(ref_html, ed)
        content_gate(html, ed['slug'] + '/index.html')
        js = build_js(ref_js, ed, topics)
        ddir = os.path.join(REPO, 'db', ed['slug'])
        os.makedirs(ddir, exist_ok=True)
        with open(os.path.join(ddir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        jsp = os.path.join(ddir, 'gen-%s.js' % ed['slug'])
        with open(jsp, 'w', encoding='utf-8') as f:
            f.write(js)
        # node --check on the generator
        p = subprocess.run(['node', '--check', jsp], capture_output=True, text=True, timeout=60)
        assert p.returncode == 0, 'node --check failed for %s: %s' % (jsp, p.stderr)
        print('page+generator ok: %s' % ed['slug'])

    # ---- compile-check one gen.js sample demo program ----
    sample = subprocess.run(['node', '-e',
                             'var JAHDB={registerGenerator:function(){}};'
                             'var g=require(%s);'
                             'var r=g.generate(7,{});'
                             'console.log(r.demo.program);' % json.dumps(
                                 os.path.join(REPO, 'db', P['slug'], 'gen-%s.js' % P['slug']))],
                            capture_output=True, text=True, timeout=60)
    assert sample.returncode == 0, 'gen sample failed: %s' % sample.stderr[-1000:]
    compile(sample.stdout, '<gen-demo>', 'exec')
    print('gen.js sample demo program compiles as Python')

    # ---- fragment (STAGED, never live - coordinator merges) ----
    frag = {
        'public': {
            'slug': P['slug'], 'name': P['name'], 'tagline': P['tagline'],
            'record_kind': P['kind'], 'id_prefix': P['prefix'], 'ai_name': P['ai'],
            'local_index': BASEURL + P['slug'] + '/index.jsonl.gz',
            'record_count': 34, 'status': 'staged', 'full_records': 34,
            'index': BASEURL + P['slug'] + '/index.jsonl.gz',
            'chunk_pattern': 'data/%s/chunks/chunk-NNNN.jsonl.gz' % P['slug'],
            'source': 'public-harvest',
        },
        'signature': {
            'slug': P['sig_slug'], 'name': P['signame'], 'tagline': P['sigtagline'],
            'record_kind': P['kind'], 'id_prefix': P['sigprefix'], 'ai_name': P['sigai'],
            'local_index': BASEURL + P['sig_slug'] + '/index.jsonl.gz',
            'record_count': 34, 'status': 'staged', 'full_records': 34,
            'index': BASEURL + P['sig_slug'] + '/index.jsonl.gz',
            'chunk_pattern': 'data/%s/chunks/chunk-NNNN.jsonl.gz' % P['sig_slug'],
            'source': 'signature',
        },
    }
    os.makedirs(FRAGDIR, exist_ok=True)
    with open(os.path.join(FRAGDIR, P['slug'] + '.json'), 'w', encoding='utf-8') as f:
        json.dump(frag, f, ensure_ascii=False, indent=1)
    print('fragment staged: %s.json' % P['slug'])
    print('BUILD COMPLETE: %s (34) + %s (34)' % (P['slug'], P['sig_slug']))


if __name__ == '__main__':
    main()
