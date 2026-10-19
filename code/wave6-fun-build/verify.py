"""Verify wave 6 staged output on disk (no rebuild)."""
import sys, os, json, gzip, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from lib import gate_scan, node_check

ITEMS_MOD = __import__('build')
ITEMS = ITEMS_MOD.ITEMS
DB_ROOT = '/home/hatch/workspace/jah-databases/db'
DATA_ROOT = '/home/hatch/workspace/jah-databases-data-1/data'

REQUIRED = ['id', 't', 'g', 'name', 'title', 'description', 'how_it_works',
            'key_points', 'requirements', 'standards', 'citations', 'src',
            'ladder_rank', 'ladder_tier', 'demo']

fails = []
def fail(m):
    fails.append(m); print('FAIL:', m)

slugs = []
for it in ITEMS:
    for sig in (False, True):
        slugs.append((it, sig, it['slug'] + ('-signature' if sig else '')))

seen_ids, seen_titles = {}, {}
nrec = 0
for it, sig, slug in slugs:
    # pages
    pdir = os.path.join(DB_ROOT, slug)
    if not os.path.isfile(os.path.join(pdir, 'index.html')):
        fail('%s missing index.html' % slug); continue
    gpath = os.path.join(pdir, 'gen-%s.js' % slug)
    if not os.path.isfile(gpath):
        fail('%s missing gen js' % slug); continue
    ok, err = node_check(gpath)
    if not ok:
        fail('%s node --check: %s' % (slug, err))
    html = open(os.path.join(pdir, 'index.html')).read()
    for needle in ['id="stCount"', 'Exhaustive', 'All Database Merger', 'mergePanel',
                   'mergerLoadAll', 'minmax(120px,1fr)', 'codeblock', 'data-p=']:
        if needle not in html:
            fail('%s page missing %s' % (slug, needle))
    # data
    idx = os.path.join(DATA_ROOT, slug, 'index.jsonl.gz')
    if not os.path.isfile(idx):
        fail('%s missing index.jsonl.gz' % slug); continue
    lines = [json.loads(l) for l in gzip.open(idx, 'rt', encoding='utf-8')]
    if len(lines) != 34:
        fail('%s index has %d lines' % (slug, len(lines)))
    chk = os.path.join(DATA_ROOT, slug, 'chunks', 'chunk-0000.jsonl.gz')
    recs = [json.loads(l) for l in gzip.open(chk, 'rt', encoding='utf-8')]
    if len(recs) != 34:
        fail('%s chunk has %d records' % (slug, len(recs)))
    base = slug[:-len('-signature')] if sig else slug
    for r in recs:
        nrec += 1
        for k in REQUIRED:
            if k not in r:
                fail('%s record %s missing %s' % (slug, r.get('id'), k))
        if r['id'] in seen_ids:
            fail('dup id %s in %s and %s' % (r['id'], slug, seen_ids[r['id']]))
        seen_ids[r['id']] = slug
        key = (r['title'], r.get('g', ''))
        if key in seen_titles and seen_titles[key] != base:
            fail('dup title %r in %s and %s' % (r['title'], base, seen_titles[key]))
        seen_titles.setdefault(key, base)
        for f in ('title', 'description', 'how_it_works'):
            b, rr, _ = gate_scan(r.get(f, ''), slug)
            if b or rr:
                fail('gate %s %s: %s %s' % (slug, r['id'], b, rr))

frag = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'manifest-fragment.json')))
if len(frag) != 148:
    fail('fragment has %d entries' % len(frag))
for e in frag:
    for k in ('slug', 'name', 'tagline', 'record_kind', 'id_prefix', 'ai_name',
              'local_index', 'page_url', 'index', 'chunk_pattern', 'source',
              'record_count', 'full_records', 'status'):
        if k not in e:
            fail('fragment entry %s missing %s' % (e.get('slug'), k))

print('slugs: %d  records: %d  unique ids: %d' % (len(slugs), nrec, len(seen_ids)))
print('VERIFY ' + ('FAILED (%d)' % len(fails) if fails else 'PASSED'))
sys.exit(1 if fails else 0)
