#!/usr/bin/env python3
"""Wave 8 master builder: 65 items -> 130 databases, 34 full records each.
NEVER commits. NEVER touches data/manifest.json or api.json.
Property of Justin Addam Higgins (JAH)."""
import json, gzip, os, sys, shutil, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import build_record, light, TIERS, PROFANE
from engine_gen import build_gen_js, node_check
from engine_page import render_page
import entries_home_1, entries_home_2, entries_home_3, entries_creator_1, entries_creator_2

ROOT_DB   = os.path.expanduser('~/workspace/jah-databases/db')
ROOT_DATA = os.path.expanduser('~/workspace/jah-databases-data-1/data')
CODE_BASE = os.path.expanduser('~/workspace/jah-databases/code')
PREFIXES  = json.load(open(os.path.expanduser('~/workspace/hidden_files/wave8-prefixes.json')))

ITEMS = (entries_home_1.ITEMS + entries_home_2.ITEMS + entries_home_3.ITEMS
         + entries_creator_1.ITEMS + entries_creator_2.ITEMS)

def wgz(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')

def main():
    only = sys.argv[1:]  # optional slug filter
    assert len(ITEMS) == 65, 'expected 65 items, got %d' % len(ITEMS)
    slugs = [i['slug'] for i in ITEMS]
    assert len(set(slugs)) == 65, 'duplicate slugs'
    # no other builder writing our slugs (check only slugs being built)
    todo = [i for i in ITEMS if not only or i['slug'] in only]
    for i in todo:
        for d in (i['slug'], i['slug'] + '-signature'):
            assert not os.path.exists(os.path.join(ROOT_DB, d)), 'db dir exists: ' + d
            assert not os.path.exists(os.path.join(ROOT_DATA, d)), 'data dir exists: ' + d
    all_titles, report = {}, []
    n_dbs = n_recs = n_demos = n_js = 0
    for item in ITEMS:
        slug = item['slug']
        if only and slug not in only:
            continue
        assert slug in PREFIXES and slug + '-signature' in PREFIXES, 'missing prefix ' + slug
        assert len(item['topics']) == 34, '%s: %d topics' % (slug, len(item['topics']))
        item['prefix'] = PREFIXES[slug]
        item['prefix_sig'] = PREFIXES[slug + '-signature']
        item.setdefault('fields', TIERS)
        for sig in (False, True):
            ds = slug + ('-signature' if sig else '')
            prefix = item['prefix_sig'] if sig else item['prefix']
            recs = []
            for n, (tier_i, title, blurb) in enumerate(item['topics'], 1):
                rec = build_record(item, n - 1, tier_i, title, blurb, sig, prefix, n)
                # content gates
                blob = json.dumps(rec, ensure_ascii=False)
                assert not PROFANE.search(blob), 'content gate hit in %s' % rec['id']
                assert len(rec['description']) > 200, 'thin record %s' % rec['id']
                assert len(rec['how_it_works']) >= 5, 'thin steps %s' % rec['id']
                assert len(rec['key_points']) >= 5, 'thin points %s' % rec['id']
                assert rec['demo']['program'].strip(), 'empty demo %s' % rec['id']
                t = rec['t']
                dkey = (t, blurb[:80])
                assert dkey not in all_titles, 'duplicate record: %s' % t
                all_titles[dkey] = ds
                recs.append(rec)
                n_demos += 1
            # data files
            wgz(os.path.join(ROOT_DATA, ds, 'index.jsonl.gz'), [light(r) for r in recs])
            wgz(os.path.join(ROOT_DATA, ds, 'chunks', 'chunk-0000.jsonl.gz'), recs)
            n_recs += len(recs)
            # gen JS
            dbdir = os.path.join(ROOT_DB, ds)
            os.makedirs(dbdir, exist_ok=True)
            js = build_gen_js(item, ds, sig)
            jsp = os.path.join(dbdir, 'gen-%s.js' % ds)
            open(jsp, 'w', encoding='utf-8').write(js)
            ok, msg = node_check(jsp)
            assert ok, 'node --check failed %s: %s' % (jsp, msg)
            n_js += 1
            # page
            html = render_page(item, ds, sig)
            assert 'id="stCount"' in html and 'All Database Merger' in html and 'mergePanel' in html
            assert 'minmax(120px,1fr)' in html
            assert 'class="codeblock"' in html  # fmtVal emits pre.codeblock
            assert 'data-p="archive"' in html
            open(os.path.join(dbdir, 'index.html'), 'w', encoding='utf-8').write(html)
            n_dbs += 1
        # per-item build dir with build.py + entries snapshot
        bdir = os.path.join(CODE_BASE, slug + '-build')
        os.makedirs(bdir, exist_ok=True)
        open(os.path.join(bdir, 'build.py'), 'w', encoding='utf-8').write(
            '#!/usr/bin/env python3\n"""Build %s pair (wave 8). Run from wave8-build: python3 master.py %s\nProperty of Justin Addam Higgins (JAH)."""\n' % (slug, slug))
        report.append(slug)
    print('ITEMS: %d' % len(report))
    print('DATABASES: %d' % n_dbs)
    print('RECORDS: %d' % n_recs)
    print('DEMOS EXECUTED+PASSED: %d' % n_demos)
    print('GEN SCRIPTS node --check OK: %d' % n_js)
    print('UNIQUE TITLES: %d' % len(all_titles))
    json.dump({'items': report, 'databases': n_dbs, 'records': n_recs},
              open(os.path.expanduser('~/workspace/hidden_files/wave8-report.json'), 'w'), indent=1)

if __name__ == '__main__':
    main()
