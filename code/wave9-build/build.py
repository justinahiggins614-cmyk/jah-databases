#!/usr/bin/env python3
"""Wave 9 build orchestrator: 150 databases (75 items x public+Signature),
34 full records each = 5,100 records. Stages pages + shard data. NEVER commits,
NEVER touches manifest.json or api.json (coordinator merges)."""
import contextlib
import gzip
import io
import json
import os
import re
import subprocess
import sys

W9 = '/home/hatch/workspace/jah-databases/code/wave9-build'
REPO = '/home/hatch/workspace/jah-databases'
SHARD = '/home/hatch/workspace/jah-databases-data-1'
NB = '/home/hatch/workspace/jah-databases/code/numbering-build'
sys.path.insert(0, W9)
sys.path.insert(0, REPO + '/code')
sys.path.insert(0, NB)

import items
import records as R
import genjs
import importlib.util as _ilu
def _load_nb():
    spec = _ilu.spec_from_file_location(
        'nbbuild', NB + '/build.py')
    mod = _ilu.module_from_spec(spec)
    sys.modules['nbbuild'] = mod
    spec.loader.exec_module(mod)
    return mod
nb = _load_nb()  # numbering-build/build.py (explicit path; avoids name shadow)
from dedupe_gate import DedupeGate

ALL = json.load(open(os.path.join(W9, 'all_topics.json')))
PREFIXES = json.load(open(os.path.join(W9, 'prefixes.json')))
SHARD_BASE = 'https://justinahiggins614-cmyk.github.io/jah-databases-data-1'

# ---------------- content gates ----------------
DENY = ['facebook', 'fuck', 'shit', 'bitch', 'cunt', 'nigger', 'faggot',
        'porn', 'xxx', 'jesus christ', 'praise the lord', 'hallelujah',
        'in jesus name', 'biblical prophecy']
def content_gate(text, rid):
    low = text.lower()
    for w in DENY:
        if w in low:
            raise ValueError('content gate hit %r in %s' % (w, rid))

def exec_demo(program, rid):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(program, rid, 'exec'), {'__name__': '__main__'})
    out = buf.getvalue()
    if 'OK:' not in out:
        raise ValueError('demo did not print OK: in %s' % rid)
    return out

# ---------------- page config ----------------
SCHEMA = ('id · name · title · description · how_it_works · key_points · requirements · '
          'standards · citations · src · ladder_rank · ladder_tier · demo')

def page_cfg(slug, item, is_sig):
    name = item['name'] + (' (Signature Edition)' if is_sig else '')
    ai_short = item['ai_short']
    ai = 'JAH %s %sArchivist' % (ai_short, 'Signature ' if is_sig else '')
    sig_type = 'Signature originals in Signature system' if is_sig else (
        'Boundless generator in Signature system' if item['klass'] == 'gen'
        else 'Public records in Signature system')
    tag_base = item['tagline']
    if is_sig:
        tagline = ('Signature edition: ' + tag_base +
                   ' Original Signature creations organized in the Signature system.')
        gen_desc = ('Generate Signature-edition %s. Seeded archive records are the authoritative entries.'
                    % item['record_kind'])
    elif item['klass'] == 'gen':
        tagline = (tag_base +
                   ' A boundless generator producing genuine complete plans, organized in the Signature system.')
        gen_desc = ('Generate complete %s. Seeded archive records are the authoritative entries.'
                    % item['record_kind'])
    else:
        tagline = tag_base + ' Public records organized in the Signature system.'
        gen_desc = ('Generate %s studies. Seeded archive records are the authoritative entries.'
                    % item['record_kind'])
    b = lambda s: '<b>%s</b>' % s
    hero_p = ('%s — organized in the Signature system. Every record carries the full entry: '
              'description, how it works, key points, requirements, standards, citations, and a working demo.' % tag_base)
    return {
        'name': name,
        'tagline': tagline,
        'record_kind': item['record_kind'],
        'prefix': PREFIXES[slug],
        'ai': ai,
        'role': item['role'] + (' — signature edition' if is_sig else ''),
        'hero_p': hero_p,
        'search_ph': 'Search %s…' % item['record_kind'],
        'fields': 'Foundations · Compounded · Advanced',
        'schema': SCHEMA,
        'archive_blurb': ('The %s archive (%s records): %s Every record carries the full entry — '
                          'never a stub.' % (name, PREFIXES[slug], tag_base)),
        'gen_desc': gen_desc,
        'greet': 'I am the %s. Ask me about %s.' % (ai, item['record_kind']),
        'chat_ph': 'Ask about %s…' % item['record_kind'],
        'sig_type': sig_type,
        'source': 'signature' if is_sig else 'public',
    }

# ---------------- shard writing ----------------
def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, 'wt', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')

def write_shard_db(slug, recs):
    base = os.path.join(SHARD, 'data', slug)
    light = [{'id': r['id'], 't': r['t'], 'g': r['g']} for r in recs]
    write_gz_jsonl(os.path.join(base, 'index.jsonl.gz'), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, 'chunks', 'chunk-%04d.jsonl.gz' % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)

# ---------------- node sample generation (gen-* items) ----------------
def node_generate_samples(js_path, slug):
    """Run the real generator JS in node to produce 34 ladder-ordered sample records."""
    runner = '''
var g = require(%s);
var out = [];
for (var i = 0; i < 34; i++) {
  var r = g.generate(i + 1, {topicIndex: i});
  r.ladder_rank = i + 1;
  var v = g.validate(r);
  if (!v.ok) { console.error("VALIDATE FAIL " + JSON.stringify(v.errors)); process.exit(1); }
  out.push(r);
}
console.log(JSON.stringify(out));
''' % json.dumps(js_path)
    p = subprocess.run(['node', '-e', runner], capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        raise RuntimeError('node sample generation failed for %s: %s' % (slug, p.stderr[:500]))
    recs = json.loads(p.stdout)
    assert len(recs) == 34, 'node produced %d records' % len(recs)
    return recs

# ---------------- build ----------------
def ordered_topics(slug):
    ts = [tuple(x) for x in ALL[slug]]
    ts.sort(key=lambda t: R.TIER_ORDER[t[1]])
    assert len(ts) == 34, (slug, len(ts))
    return ts

def main():
    gate = DedupeGate(os.path.join(SHARD, 'data', 'dedupe', 'exact'))
    # Pre-seed the gate with titles from already-staged wave-9 shards so a
    # resume run still enforces whole-system + within-wave uniqueness.
    only = [s for s in os.environ.get('W9_ONLY', '').split(',') if s]
    if only:
        import glob
        for idx_path in glob.glob(os.path.join(SHARD, 'data', '*', 'index.jsonl.gz')):
            slug = idx_path.split('/')[-2]
            if slug in only:
                continue
            try:
                with gzip.open(idx_path, 'rt', encoding='utf-8') as f:
                    for line in f:
                        r = json.loads(line)
                        gate.admit(slug, r['t'], r['id'])
            except Exception:
                pass
        print('pre-seeded gate from staged shards; building only: %d slugs' % len(only))
    with open(os.path.join(REPO, 'db', 'public-synthetic-intelligence', 'index.html'),
              encoding='utf-8') as f:
        template = f.read()

    # build queue: first_release_pick items first
    queue = []
    for slug, item in items.ITEMS.items():
        queue.append((slug, item))
    queue.sort(key=lambda q: (not q[1]['first_pick'], q[0]))
    print('first picks first:', [s for s, it in queue[:9] if it['first_pick']])

    # inject page configs
    slugs_all = []
    for slug, item in queue:
        slugs_all.append((slug, item, False))
        slugs_all.append((slug + '-signature', item, True))
    for slug, item, is_sig in slugs_all:
        nb.DBCFG[slug] = page_cfg(slug, item, is_sig)

    staged_pages = 0
    staged_shards = 0
    staged_gens = 0
    total_recs = 0
    skips = []

    for slug, item, is_sig in slugs_all:
        if only and slug not in only:
            continue
        base = slug.replace('-signature', '')
        topics = ordered_topics(base)
        klass = item['klass']
        src = 'signature' if is_sig else ('sample' if klass == 'gen' else 'public')
        recs = []
        try:
            if klass == 'gen' and not is_sig:
                # sample records produced by the REAL generator JS via node
                js = genjs.build_gen_js(item, topics, PREFIXES[slug])
                ddir = os.path.join(REPO, 'db', slug)
                os.makedirs(ddir, exist_ok=True)
                js_path = os.path.join(ddir, 'gen-%s.js' % slug)
                with open(js_path, 'w', encoding='utf-8') as f:
                    f.write(js)
                cp = subprocess.run(['node', '--check', js_path], capture_output=True, text=True)
                if cp.returncode != 0:
                    raise RuntimeError('node --check failed: ' + cp.stderr[:300])
                staged_gens += 1
                recs = node_generate_samples(js_path, slug)
                for r in recs:
                    gate.check_and_raise(slug, r['title'])
                    gate.admit(slug, r['title'], r['id'])
                    content_gate(json.dumps(r, ensure_ascii=False), r['id'])
                    exec_demo(r['demo']['program'], r['id'])
            else:
                recs = []
                for i, t in enumerate(topics):
                    rec, _dk = R.build_record(item, t, i, PREFIXES[slug], src, slug)
                    gate.check_and_raise(slug, rec['title'])
                    gate.admit(slug, rec['title'], rec['id'])
                    content_gate(json.dumps(rec, ensure_ascii=False), rec['id'])
                    exec_demo(rec['demo']['program'], rec['id'])
                    recs.append(rec)
                # real generator JS for the page (db-* pages and signature pages)
                edition = ' (Signature Edition)' if is_sig else ''
                js = genjs.build_gen_js(item, topics, PREFIXES[slug], edition)
                ddir = os.path.join(REPO, 'db', slug)
                os.makedirs(ddir, exist_ok=True)
                js_path = os.path.join(ddir, 'gen-%s.js' % slug)
                with open(js_path, 'w', encoding='utf-8') as f:
                    f.write(js)
                cp = subprocess.run(['node', '--check', js_path], capture_output=True, text=True)
                if cp.returncode != 0:
                    raise RuntimeError('node --check failed: ' + cp.stderr[:300])
                staged_gens += 1

            # write shard data
            n = write_shard_db(slug, recs)
            staged_shards += 1
            total_recs += n

            # write page
            page = nb.build_page(slug, template)
            for needle in ['id="stCount"', 'Exhaustive', 'All Database Merger',
                           'mergePanel', 'minmax(120px,1fr)', 'pre.codeblock',
                           'dataset.p', "var SLUG='%s';" % slug]:
                assert needle in page, (slug, needle)
            assert 'facebook' not in page.lower(), slug
            ddir = os.path.join(REPO, 'db', slug)
            os.makedirs(ddir, exist_ok=True)
            with open(os.path.join(ddir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(page)
            staged_pages += 1
            if staged_pages % 25 == 0:
                print('... %d pages staged' % staged_pages, flush=True)
        except Exception as e:
            skips.append((slug, repr(e)[:200]))
            print('SKIP %s: %s' % (slug, repr(e)[:200]), flush=True)

    print('=' * 60)
    print('pages staged:  %d' % staged_pages)
    print('shards staged: %d' % staged_shards)
    print('gen JS staged: %d' % staged_gens)
    print('records:       %d' % total_recs)
    print('skips:         %d' % len(skips))
    for s in skips:
        print('  SKIP', s)
    json.dump({'pages': staged_pages, 'shards': staged_shards,
               'gens': staged_gens, 'records': total_recs,
               'skips': skips},
              open(os.path.join(W9, 'build_report.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
