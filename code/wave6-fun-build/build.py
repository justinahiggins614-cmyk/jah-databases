"""Wave 6 of 11 build — 74 items -> 148 databases (public + Signature), 34 FULL records each.
Art-visual (15) + music-audio (22) + fashion-style (38), minus sustainable-fashion
(already live in manifest as JAH-SUST-FASH from another wave — skipped).

Stages:
  pages: ~/workspace/jah-databases/db/<slug>/{index.html,gen-<slug>.js}
  data:  ~/workspace/jah-databases-data-1/data/<slug>/{index.jsonl.gz,chunks/chunk-0000.jsonl.gz}
  fragment: ./manifest-fragment.json (150 entries, status staged — coordinator merges)

NEVER commits. NEVER touches data/manifest.json or api.json.
Property of Justin Addam Higgins (JAH).
"""
import sys, os, json, subprocess, gzip, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib
from lib import (PREFIXES, sig_prefix, sig_name, make_record, sig_wrap, run_demo,
                 gate_scan, render_page, genjs_db, write_data, write_page,
                 manifest_entry, node_check)

import art_db, art_gen, music_db, music_gen, fashion_db15, fashion_gen

# sustainable-fashion is already live in the manifest (JAH-SUST-FASH, built by
# another wave) — skipping the pair to avoid a slug collision / duplicate DB.
SKIP_SLUGS = {'sustainable-fashion'}

ITEMS = [i for i in (art_db.ITEMS + art_gen.ITEMS + music_db.ITEMS + music_gen.ITEMS
         + fashion_db15.ITEMS + fashion_gen.ITEMS)
         if i['slug'] not in SKIP_SLUGS]

MANIFEST = '/home/hatch/workspace/jah-databases/data/manifest.json'
FRAG_OUT = os.path.join(HERE, 'manifest-fragment.json')
GEN_TMP = os.path.join(HERE, 'tmp-genjs')
os.makedirs(GEN_TMP, exist_ok=True)

LOG = []


def log(msg):
    LOG.append(msg)
    print(msg, flush=True)


def fail(msg):
    log('FATAL: ' + msg)
    raise SystemExit(1)


# ---------------- preflight ----------------
def preflight():
    assert len(ITEMS) == 74, 'expected 74 items (75 minus 1 skipped), got %d' % len(ITEMS)
    slugs = [i['slug'] for i in ITEMS]
    assert len(set(slugs)) == 74, 'duplicate slugs in wave'
    # prefixes assigned
    for it in ITEMS:
        p = PREFIXES.get(it['slug'])
        assert p, 'no prefix for %s' % it['slug']
        it['prefix'] = p
    # prefix collisions vs manifest (exact + substring), like the 2026-10-17 check
    man = json.load(open(MANIFEST))
    existing = [d.get('id_prefix', '') for d in man.get('databases', [])]
    mslugs = set(d.get('slug', '') for d in man.get('databases', []))
    for it in ITEMS:
        for sig in (False, True):
            px = sig_prefix(it['prefix']) if sig else it['prefix']
            for e in existing:
                if e and (px == e or px in e or e in px):
                    fail('prefix collision: %s (%s) vs manifest %s' % (it['slug'], px, e))
            slug = it['slug'] + ('-signature' if sig else '')
            if slug in mslugs:
                fail('slug already in manifest: %s' % slug)
            # no other builder writing my slugs
            if os.path.exists(os.path.join('/home/hatch/workspace/jah-databases/db', slug)):
                fail('db dir already exists (another builder?): %s' % slug)
    log('preflight OK: 74 items (1 skipped: sustainable-fashion, already live), 148 slugs+prefixes clear of manifest (%d dbs)' % len(existing))


# ---------------- record builders ----------------
def gate_text(text, label):
    b, r, _ = gate_scan(text, label)
    if b or r:
        fail('content gate hit in %s: %s / %s' % (label, b, r))


def scan_record(rec, label):
    for key in ('title', 'description', 'how_it_works', 'citations'):
        v = rec.get(key)
        if isinstance(v, str):
            gate_text(v, label + ':' + key)
    for key in ('key_points', 'requirements', 'standards'):
        for s in rec.get(key) or []:
            gate_text(s, label + ':' + key)


def build_db_records(item, sig, prefix):
    recs = []
    for rank, pack in enumerate(item['topics'], 1):
        rec = make_record(item, pack, rank, sig, prefix)
        prog = rec['demo']['program']
        ok, out = run_demo(prog)
        if not ok:
            fail('demo failed: %s rank %d: %s' % (item['slug'], rank, out[-300:]))
        scan_record(rec, '%s#%d' % (item['slug'], rank))
        recs.append(rec)
    assert len(recs) == 34
    return recs


GEN_NODE_TMPL = """var g=require(%s);var seeds=%s;var out=seeds.map(function(s){var r=g.generate(s,{});var v=g.validate(r);if(!v.ok)throw new Error('validate failed seed '+s+': '+v.errors.join(','));if(!r.demo||!r.demo.program)throw new Error('no demo seed '+s);return r;});console.log(JSON.stringify(out));"""


def build_gen_records(item, sig, prefix, full_slug):
    # 1. materialize the gen JS with real slug/prefix
    js = item['genjs'].replace('__SLUG__', full_slug).replace('__PREFIX__', prefix)
    assert '__SLUG__' not in js and '__PREFIX__' not in js
    tmp = os.path.join(GEN_TMP, 'gen-%s.js' % full_slug)
    open(tmp, 'w').write(js)
    ok, err = node_check(tmp)
    if not ok:
        fail('node --check failed for %s: %s' % (full_slug, err))
    # 2. functional harness (lib's)
    ok, out = lib.node_functional_test(tmp)
    if not ok:
        fail('node functional test failed for %s: %s' % (full_slug, out))
    # 3. generate 34 records in one node call
    seeds = list(range(101, 135)) if sig else list(range(1, 35))
    prog = GEN_NODE_TMPL % (json.dumps(tmp), json.dumps(seeds))
    p = subprocess.run(['node', '-e', prog], capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        fail('node generate failed for %s: %s' % (full_slug, (p.stdout + p.stderr)[-500:]))
    recs = json.loads(p.stdout)
    assert len(recs) == 34, 'expected 34 gen records, got %d' % len(recs)
    final = []
    for i, r in enumerate(recs, 1):
        r.pop('_seed', None)
        r['ladder_rank'] = i
        r['ladder_tier'] = r.get('field', '')
        r['t'] = r['title']
        r['g'] = r.get('field', '')
        if sig:
            r = sig_wrap(r, item, [
                'Signature expansion: this record carries the Signature system treatment on top of the public knowledge.',
                'Cross-database aware: connects to sibling Signature databases in the network.',
            ])
        okd, outd = run_demo(r['demo']['program'])
        if not okd:
            fail('gen demo failed: %s seed %d: %s' % (full_slug, seeds[i - 1], outd[-300:]))
        scan_record(r, '%s#%d' % (full_slug, i))
        final.append(r)
    return final, js


# ---------------- main ----------------
def main():
    preflight()
    fragments = []
    seen_ids, seen_titles = set(), set()
    dupes = []
    counts = {'items': 0, 'dbs': 0, 'records': 0, 'demos': 0, 'pages': 0}
    for item in ITEMS:
        for sig in (False, True):
            slug = item['slug'] + ('-signature' if sig else '')
            prefix = sig_prefix(item['prefix']) if sig else item['prefix']
            if item['cls'] == 'gen':
                recs, genjs_text = build_gen_records(item, sig, prefix, slug)
            else:
                recs = build_db_records(item, sig, prefix)
                genjs_text = genjs_db(item, sig)
            # batch dedupe gate: ids unique globally; titles unique across
            # different base items (a public/Signature pair shares titles by design)
            base = slug[:-len('-signature')] if sig else slug
            for r in recs:
                if r['id'] in seen_ids:
                    dupes.append(('id', r['id']))
                seen_ids.add(r['id'])
                key = (r['title'], r.get('field', ''))
                if key in seen_titles and seen_titles[key] != base:
                    dupes.append(('title', r['title'], base, seen_titles[key]))
                seen_titles.setdefault(key, base)
            write_data(slug, recs)
            html_text = render_page(item, sig)
            write_page(slug, html_text, genjs_text)
            ok, err = node_check(os.path.join('/home/hatch/workspace/jah-databases/db', slug, 'gen-%s.js' % slug))
            if not ok:
                fail('node --check failed on written page genjs %s: %s' % (slug, err))
            fragments.append(manifest_entry(item, sig))
            counts['dbs'] += 1
            counts['records'] += len(recs)
            counts['demos'] += len(recs)
            counts['pages'] += 1
            log('staged %s (%d records)' % (slug, len(recs)))
        counts['items'] += 1
    if dupes:
        fail('batch dedupe gate: %d duplicates: %s' % (len(dupes), dupes[:10]))
    json.dump(fragments, open(FRAG_OUT, 'w'), indent=1, ensure_ascii=False)
    log('wrote %s (%d entries)' % (FRAG_OUT, len(fragments)))
    log('DONE: items=%d dbs=%d records=%d demos_run=%d pages=%d dupes=0' % (
        counts['items'], counts['dbs'], counts['records'], counts['demos'], counts['pages']))
    assert counts['dbs'] == 148 and counts['records'] == 148 * 34


if __name__ == '__main__':
    main()
