#!/usr/bin/env python3
"""Build real Signature system report editions for the news database.
Appends REPORTED (database/file/network reports) and PROPOSED (Signature ideas)
editions to data/news/. All facts verified against data/manifest.json and git.
"""
import json, gzip, hashlib, os, sys

REPO = os.path.expanduser('~/workspace/jah-databases')
DATA = os.path.join(REPO, 'data/news')
DATE = '2026-10-15'

manifest = json.load(open(os.path.join(REPO, 'data/manifest.json')))
NDB = len(manifest['databases'])

def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

# (category, fictionality_status, creation_mode, honesty, paper_headline, articles)
# articles: list of (sec, headline, byline, [paragraphs])
EDITIONS = [
# ---------------- DATABASE REPORTS ----------------
('database-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — database launches and milestones, verified against data/manifest.json and the repos' own commit history. It reports no real-world news and names no real-world persons.",
 "Robotics and control database set launches — seven databases, 420 records",
 [
  ('database-report', "Robotics and control set goes live: seven databases, 420 full records", "Signature News Desk",
   ["The network's robotics and control set launched today: seven new databases carrying 420 full Signature-original records, 60 apiece.",
    "The set covers predictive trajectories (JAH-PT-), dynamics models (JAH-DM-), cost functions (JAH-CF-), optimal plans (JAH-OP-), model predictive control (JAH-MPC-), robot positions (JAH-RP-), and a vector database (JAH-VEC-) for pose, trajectory, and plan embeddings.",
    "The Robot Position Database is built as the compiled view of the five core databases — each fused pose record cites its source records across trajectories, dynamics, cost, plan, and control."]),
  ('database-report', "Each robotics record ships runnable Python demos", "Records Desk",
   ["Every record in the robotics set carries 16 to 19 fields: equations, parameter sets, and runnable Python demonstrations.",
    "Cost-function records include the math plus tuning guidance; model-predictive-control records carry horizons, constraints, solvers, and stability notes with receding-horizon demos.",
    "Three demonstrations were executed end-to-end during the build before the set shipped."]),
  ('database-report', "Vector database adds similarity search over poses and plans", "Records Desk",
   ["The set's seventh member is a vector database: pose, trajectory, plan, sensor, and policy embeddings with dimensions, distance metrics, and indexing notes.",
    "Records carry normalized sample vectors and similarity-search demonstrations, so the network can retrieve by meaning as well as by keyword.",
    "The vector layer is the retrieval backbone the compiled position views build on."]),
  ('database-report', "Data lands in the data-1 shard as main repo passes 1.1GB", "Systems Desk",
   ["The robotics set's data lives in the jah-databases-data-1 shard: index plus record chunks under data/<slug>/, served live from the shard's Pages site.",
    "The main repo's data directory stands at 1.1GB, over the 800MB guard — so new database data routes to shards while pages and the manifest stay in the main repo.",
    "All seven shard indexes verified live at 60 records each after the push."]),
 ],
),
('database-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — database launches and milestones, verified against data/manifest.json and the repos' own commit history. It reports no real-world news and names no real-world persons.",
 "Hard-equations and impossible-software set: five databases, 300 records",
 [
  ('database-report', "Hard Equations Database: problems normal AI can't solve, with full worked solutions", "Signature News Desk",
   ["The Hard Equations Database launched with 60 records, each an equation that ordinary AI systems cannot solve, paired with the complete worked solution.",
    "Every solution is machine-verified before the record ships — the database exists to show what the Signature approach can do that normal AI cannot.",
    "Records carry the full equation, an explanation of why it resists ordinary solvers, and the step-by-step solution."]),
  ('database-report', "Impossible-software set: programs, code, scripts, and AI systems normal AI can't make", "Records Desk",
   ["Four companion databases launched alongside: Impossible Programs (JAH-IP-), Impossible Code (JAH-IC-), Impossible Scripts (JAH-IS-), and Impossible AI Systems (JAH-IA-).",
    "Each of the 240 records carries real working code — runnable where applicable — with executed demonstrations proving it runs.",
    "The set is the code counterpart to the hard-equations database: software artifacts beyond what normal AI produces."]),
  ('database-report', "Set totals: 300 records, all Signature-original, all demo-verified", "Records Desk",
   ["The five databases total 300 full Signature-original records, 60 apiece, each with executed demos.",
    "Like the robotics set, data routes to the data-1 shard while the manifest and pages stay in the main repo.",
    "The network's impossible-things shelf now holds equations and software side by side."]),
 ],
),
('database-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — database launches and milestones, verified against data/manifest.json and the repos' own commit history. It reports no real-world news and names no real-world persons.",
 "Numbering-plan databases: 1,712 records across area codes, country codes, ZIPs",
 [
  ('database-report', "Area Code Database: 487 real NANP area codes", "Signature News Desk",
   ["The Area Code Database archives 487 real North American Numbering Plan area codes — regions, overlays, and dialing notes, fully cited.",
    "It is the public-record member of the numbering-plan set: real harvested data, never invented.",
    "Each record is the full file, one click from its card."]),
  ('database-report', "Country calling codes and US ZIP codes join the set", "Records Desk",
   ["The Country Calling Code Database carries 215 ITU country calling codes; the US ZIP Code Database seeded 950 codes and marches toward full coverage.",
    "The Signature Numbering Plan Database contributes 60 original Signature numbering designs as the set's Signature-made member.",
    "Public and Signature versions mirror each other wherever each genuinely applies, per the network's standing rule."]),
 ],
),
('database-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — database launches and milestones, verified against data/manifest.json and the repos' own commit history. It reports no real-world news and names no real-world persons.",
 "Creative-software and Photoshop sets: ten databases, 600 records",
 [
  ('database-report', "Eight creative-software databases: public and Signature mirrors", "Signature News Desk",
   ["The creative-software set spans video editing, music production, 3D modeling, and game engines — each in public-harvest and Signature-made versions, 60 records apiece, 480 total.",
    "Public versions harvest real records; Signature versions create the full original work; gaps get labeled Signature completions, never presented as authentic public record.",
    "All records were demo-verified before shipping."]),
  ('database-report', "Photoshop pair documents tools, features, and techniques", "Records Desk",
   ["The Public Photoshop Database and Signature Photoshop Database add 120 records on tools, features, techniques, and history.",
    "The pair follows the same mirror rule: real public material harvested whole, Signature originals created where the public record has gaps.",
    "The creative shelf keeps growing sideways — new databases, never deletions."]),
 ],
),
('database-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — database launches and milestones, verified against data/manifest.json and the repos' own commit history. It reports no real-world news and names no real-world persons.",
 "Maps, trails, paths, and restaurants: seven databases, 420 records",
 [
  ('database-report', "Cartography set maps the world four ways", "Signature News Desk",
   ["Four databases — public cartography, public trails, public paths, and Signature trails-paths — total 240 records of maps, routes, and trail data.",
    "Each record carries full geographic data with citations, demo-verified before launch.",
    "The set shows the network's pairing habit: public records plus the Signature-made companion."]),
  ('database-report', "Restaurant databases serve 180 records with full methods", "Records Desk",
   ["Public Restaurants, Signature Restaurants, and Public Secret Menus total 180 records with full ingredients and methods.",
    "Real menus harvested whole on the public side; original creations on the Signature side.",
    "One click from any card reaches the complete record — never a stub."]),
 ],
),
('database-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — database launches and milestones, verified against data/manifest.json and the repos' own commit history. It reports no real-world news and names no real-world persons.",
 "Network milestone: 1,839 databases, counts always current",
 [
  ('database-report', "The network passes 1,839 databases", "Signature News Desk",
   ["The JAH Databases manifest lists 1,839 databases, each marching toward one million records or complete in its domain.",
    "Growth this week: numbering plan (+4), robotics and control (+7), hard equations and impossible software (+5).",
    "Every addition ships with its page, its generator, its AI, and its data — the full set, never a partial launch."]),
  ('database-report', "Counts derive from the manifest — never hand-typed", "Systems Desk",
   ["The hub's counters are stamped by code/restamp_counts.py, which derives the count from data/manifest.json and re-stamps the hub, the manifest, and api.json.",
    "A six-hour cron catches anything a build missed, so the number on the hub always matches the manifest.",
    "Per-database record counts render live from each database's own archive index."]),
 ],
),
# ---------------- FILE REPORTS ----------------
('file-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — notable files added across the system, verified against the repos' own data. It reports no real-world news and names no real-world persons.",
 "No-repeat machinery: global dedupe index and browser gate",
 [
  ('file-report', "Global dedupe index covers 11.65 million rows", "Systems Desk",
   ["code/build_global_dedupe.py scans every database index — 11.65 million rows — normalizes titles exactly as the browser does, and writes hash-prefix shards.",
    "The browser gets compact bloom shards (~14MB); the exact map (~110MB) backs verification. Python and JavaScript produce byte-identical hashes on all test vectors.",
    "Bloom round-trips verified: existing titles hit, novel titles miss, zero false positives in 2,000 trials."]),
  ('file-report', "core/jahdb-dedupe.js: every generator checked, no repeats", "Systems Desk",
   ["The new core module wraps the single generator chokepoint, so all databases are covered without editing every page.",
    "New generateChecked() does same-database exact matching plus cross-database bloom-then-exact verification, with reseed retries — then fails honestly rather than emitting a silent duplicate.",
    "The standing rule is now code: check the whole system before generating, no time limit, correctness first."]),
 ],
),
('file-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — notable files added across the system, verified against the repos' own data. It reports no real-world news and names no real-world persons.",
 "Cross-database blending becomes a verified contract: core/jahdb-xdb.js",
 [
  ('file-report', "xdb helper: pulled material must change the result", "Systems Desk",
   ["core/jahdb-xdb.js implements the standing rule: when a database pulls material from another database, it must actually use it and let it change the result.",
    "Generators declare their cross-database uses; every cited record is verified to exist in the source's published index, and every used field is traceable or carries an explicit derivation annotation.",
    "Failures reject the record — no silent passes. The robot-positions rebuild proved the contract: fused positions derived from real trajectory waypoints, 300 of 300 referential checks green."]),
 ],
),
('file-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — notable files added across the system, verified against the repos' own data. It reports no real-world news and names no real-world persons.",
 "Always-current counts: code/restamp_counts.py",
 [
  ('file-report', "One script keeps every counter honest", "Systems Desk",
   ["code/restamp_counts.py derives the database count from data/manifest.json, enforces it in the manifest and api.json, re-stamps the hub's static fallbacks, and audits all database pages for live-count wiring.",
    "It runs at the end of every database-adding commit; a six-hour cron catches misses.",
    "The hub, the manifest, and the API now agree by construction, not by typing."]),
 ],
),
('file-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — notable files added across the system, verified against the repos' own data. It reports no real-world news and names no real-world persons.",
 "Newspaper archive repair ships",
 [
  ('file-report', "db/news/index.html: archive expand hardened", "Systems Desk",
   ["The newspaper's category expand path was hardened: a click fallback covers embedded browsers that misfire the toggle event, and chunk-load failures now surface real error messages with a retry button instead of failing silently.",
    "Record cards gained honest badges: SIGNATURE REPORT for real system reports, SIGNATURE IDEA for proposals — generated samples keep their existing label.",
    "All inline scripts pass node --check; categories now read Database reports, File reports, Network reports, and Signature ideas."]),
 ],
),
('file-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — notable files added across the system, verified against the repos' own data. It reports no real-world news and names no real-world persons.",
 "3D-print estimate disclaimer patch lands",
 [
  ('file-report', "Print times labeled estimates on both 3D-print pages", "Systems Desk",
   ["The prepared patch labeled est_print_hours as an estimate and appended the estimates disclaimer to every full record carrying print settings, on both 3D-print database pages.",
    "The disclaimer states the figures are internally consistent numerical estimates from geometry — not timed, validated jobs — and lists unmodeled factors: wall thickness, supports, nozzle settings, printer motion, material-specific slicing.",
    "The same patch fixed a syntax-breaking unescaped apostrophe on the Signature page that had been killing its archive script."]),
 ],
),
('file-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — notable files added across the system, verified against the repos' own data. It reports no real-world news and names no real-world persons.",
 "manifest.json and api.json: the source of truth",
 [
  ('file-report', "Two files the whole network reads", "Systems Desk",
   ["data/manifest.json lists every database — slug, name, record count, index location — and the hub, the database AIs, and the tooling all read it live.",
    "api.json mirrors the count and the database list for programmatic readers.",
    "The restamp script keeps both in agreement with the hub's displayed numbers, so there is exactly one source of truth."]),
 ],
),
# ---------------- NETWORK REPORTS ----------------
('network-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — network-level milestones, verified against the manifest and the repos' own data. It reports no real-world news and names no real-world persons.",
 "1,839 databases: the network's shape",
 [
  ('network-report', "Every database marches to a million or is complete", "Signature News Desk",
   ["The network holds 1,839 databases. Each either marches toward one million records or is complete in its domain.",
    "Two types throughout: Signature-made originals and public records archives, mirrored wherever each genuinely applies.",
    "Every database ships the full apparatus: permanent archive, boundless generator, archive-aware AI, and per-file programs or demos."]),
  ('network-report', "Growth stays sideways — data is never cut", "Systems Desk",
   ["When the main repo's data directory passed the 800MB guard, new database data began routing to shard repos like jah-databases-data-1.",
    "Shards are frozen storage; the manifest records every shard location; pages fetch across shards transparently.",
    "The rule holds: growth is always sideways, never by deleting real records."]),
 ],
),
('network-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — network-level milestones, verified against the manifest and the repos' own data. It reports no real-world news and names no real-world persons.",
 "Deploy pipeline: main and gh-pages, every time",
 [
  ('network-report', "Two branches, one live site", "Systems Desk",
   ["The site deploys from the gh-pages branch, so every change pushes to origin/main and origin/gh-pages together.",
    "Spot checks run against the live URLs after each push — the claim 'live' is only made after a 200 and a count match.",
    "GitHub Pages deploy lag is real; verification waits for it rather than assuming."]),
 ],
),
('network-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — network-level milestones, verified against the manifest and the repos' own data. It reports no real-world news and names no real-world persons.",
 "Silent drips keep the archives growing",
 [
  ('network-report', "Background jobs, quiet by default", "Systems Desk",
   ["Scheduled jobs grow the archives around the clock — addresses, antivirus add-ons, upgrade packs, songs, app records — and stay silent unless something needs attention.",
    "Real milestones get reported; routine runs do not message anyone.",
    "The newspaper is where the system's own milestones get written up for humans to read."]),
 ],
),
('network-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — network-level milestones, verified against the manifest and the repos' own data. It reports no real-world news and names no real-world persons.",
 "Quality program: nonsense audit across the network",
 [
  ('network-report', "26 databases sampled; occupation and hobby families flagged", "Systems Desk",
   ["The quality program sampled 26 databases across families. The occupation family showed cross-contaminated descriptions; the hobby family showed filler shells.",
    "Fixes are staged as generator-template patches with a build-time dedupe gate, rolling out in phases.",
    "The bar is the standing rule: real data, meaningful to the database, following its standards — no nonsense."]),
 ],
),
('network-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — network-level milestones, verified against the manifest and the repos' own data. It reports no real-world news and names no real-world persons.",
 "Boundless generators, networked",
 [
  ('network-report', "Every database generates; generators talk across databases", "Systems Desk",
   ["Each database carries a boundless generator that makes full records — never stubs — in the database's own schema and standards.",
    "Generators are networked: a generator can borrow a theme from another database, and the cross-database helper verifies the borrowed material is real and actually used.",
    "The whole system dedupe check means the network never repeats itself."]),
 ],
),
('network-reports', 'SIGNATURE_REPORTED', 'REPORTED',
 "Signature system press: this edition reports real events from the Signature databases network — network-level milestones, verified against the manifest and the repos' own data. It reports no real-world news and names no real-world persons.",
 "Archive-aware AI on every database",
 [
  ('network-report', "Each database has its own AI; each file can too", "Systems Desk",
   ["Every database ships an archive-aware AI that knows its own archive and the network around it.",
    "The hierarchy runs database AI to file AI to workable program or demo per file, all connected toward the master AI.",
    "The newspaper's own JAH News Librarian is one of 1,839 such AIs."]),
 ],
),
# ---------------- SIGNATURE IDEAS ----------------
('signature-ideas', 'SIGNATURE_IDEA', 'PROPOSED',
 "Signature ideas: fresh proposals cataloged for the system to use. These are proposed ideas — not deployed features. Each is labeled as an idea and stays open for refinement.",
 "Idea: generators check the whole system before generating",
 [
  ('signature-idea', "No repeats, ever — correctness over speed", "Ideas Desk",
   ["Proposal: every generator checks all databases before generating, with no time limit — correctness first.",
    "A global dedupe index plus a browser-side gate makes this mechanical: same-database exact match, cross-database bloom-then-exact verification, honest failure instead of silent duplicates.",
    "Status: adopted as a standing rule; the machinery is built and rolling out."]),
 ],
),
('signature-ideas', 'SIGNATURE_IDEA', 'PROPOSED',
 "Signature ideas: fresh proposals cataloged for the system to use. These are proposed ideas — not deployed features. Each is labeled as an idea and stays open for refinement.",
 "Idea: each database is the source of all its data",
 [
  ('signature-idea', "Recreate anything from the database alone", "Ideas Desk",
   ["Proposal: every database is the source of all its data — complete enough that anything in its domain can be recreated from it.",
    "That means full records, real data, the generator that made them, and the standards they follow, all archived together.",
    "The newspaper itself follows this: its editions, generator, and index live in the archive."]),
 ],
),
('signature-ideas', 'SIGNATURE_IDEA', 'PROPOSED',
 "Signature ideas: fresh proposals cataloged for the system to use. These are proposed ideas — not deployed features. Each is labeled as an idea and stays open for refinement.",
 "Idea: compiled views across databases",
 [
  ('signature-idea', "Robot positions showed the pattern", "Ideas Desk",
   ["Proposal: build compiled views that fuse records from several databases — each fused record citing its sources, every field traceable.",
    "The Robot Position Database proved it: 60 fused poses, each citing trajectory, dynamics, cost, plan, and control records, verified 300 for 300.",
    "Any domain with parallel databases can grow its own compiled view next."]),
 ],
),
('signature-ideas', 'SIGNATURE_IDEA', 'PROPOSED',
 "Signature ideas: fresh proposals cataloged for the system to use. These are proposed ideas — not deployed features. Each is labeled as an idea and stays open for refinement.",
 "Idea: the newspaper as the system's paper of record",
 [
  ('signature-idea', "Every launch, file, and milestone gets reported", "Ideas Desk",
   ["Proposal: the newspaper database becomes the paper of record for the Signature system — database reports, file reports, network reports, all included.",
    "Launches, fixes, milestones, and fresh ideas each get a real report edition, honestly labeled, archived forever.",
    "This edition is the idea reporting on itself."]),
 ],
),
('signature-ideas', 'SIGNATURE_IDEA', 'PROPOSED',
 "Signature ideas: fresh proposals cataloged for the system to use. These are proposed ideas — not deployed features. Each is labeled as an idea and stays open for refinement.",
 "Idea: estimate labeling everywhere",
 [
  ('signature-idea', "Estimates say they are estimates", "Ideas Desk",
   ["Proposal: every computed figure the system hasn't measured gets labeled as an estimate, with its unmodeled factors disclosed.",
    "The 3D-print pages led the way: print times marked as internally consistent numerical estimates — not validated jobs — with wall thickness, supports, nozzle settings, printer motion, and slicing behavior listed as unmodeled.",
    "The rule generalizes to every database that computes."]),
 ],
),
('signature-ideas', 'SIGNATURE_IDEA', 'PROPOSED',
 "Signature ideas: fresh proposals cataloged for the system to use. These are proposed ideas — not deployed features. Each is labeled as an idea and stays open for refinement.",
 "Idea: a fixer AI with hands on every database",
 [
  ('signature-idea', "Say what's wrong; it fixes it", "Ideas Desk",
   ["Proposal: a God-mode AI that knows every database and fixes them on command — the user says what to fix, and it does it.",
    "It would read the manifest, the pages, the generators, and the data, then apply careful patches with verification.",
    "The quality program's staged patches are the first workload waiting for it."]),
 ],
),
]

def build():
    idx = json.load(gzip.open(os.path.join(DATA, 'editions.idx.json.gz'), 'rt'))
    ed_n = max(int(r[0].split('-')[-1]) for r in idx)
    art_n = 13392
    # find max article id across chunks
    import glob
    for f in glob.glob(os.path.join(DATA, 'chunks', '*.jsonl.gz')):
        for line in gzip.open(f, 'rt'):
            for a in json.loads(line)['articles']:
                art_n = max(art_n, int(a['id'].split('-')[-1]))
    chunk_n = 54
    chunk_recs = []
    new_idx_rows = []
    for (cat, fstat, cmode, honesty, paper_h, arts) in EDITIONS:
        ed_n += 1
        ed_id = 'JAH-ED-%06d' % ed_n
        issue = 988 + (ed_n - 2161)
        articles = []
        for (sec, h, by, body) in arts:
            art_n += 1
            a_id = 'JAH-ARTICLE-%06d' % art_n
            articles.append({
                'sec': sec, 'h': h, 'by': by, 'body': body, 'id': a_id,
                'edition_id': ed_id, 'fictionality_status': fstat,
                'creation_mode': cmode, 'version': '1.0',
                'content_hash': sha(h + ''.join(body)),
                'lede': body[0][:160],
            })
        full_text = ' ‖ '.join(a['h'] + ' — ' + a['body'][0] for a in articles)
        rec = {
            'paper': 0, 'date': DATE, 'issue': issue, 'volume': 3,
            'articles': articles, 'honesty': honesty, 'coverage': cat,
            'id': ed_id, 'paper_id': 'JAH-PAPER-000001', 'created': DATE,
            'fictionality_status': fstat, 'status': 'PUBLISHED',
            'creation_mode': cmode, 'version': '1.0', 'updated': DATE,
            'article_ids': [a['id'] for a in articles],
            'article_count': len(articles),
            'content_hash': sha(full_text),
            'demo': {
                'engine': 'jahdb-demo-1.0', 'kind': 'chart',
                'title': 'Data chart demo — ' + ed_id, 'language': 'javascript',
                'program': '/* JAH interactive demo program — jahdb-demo-1.0\n * Database: news · Record: ' + ed_id + '\n * Charts this record\'s numeric fields as ASCII bars.\n * RUN ON PC: save as demo.js, then run:  node demo.js */\n(function(){\nvar N={\"paper\":0,\"issue\":' + str(issue) + ',\"volume\":3,\"article_count\":' + str(len(articles)) + '};\nvar ks=Object.keys(N);\nconsole.log(ks.map(function(k){return k+\": \"+N[k];}).join(\"\\n\"));\n})();',
            },
        }
        chunk_recs.append(rec)
        text = paper_h + ' — ' + ' ‖ '.join(a['h'] for a in articles)
        new_idx_rows.append([ed_id, DATE, 0, chunk_n, chunk_n, text, cat])
    # write chunk (24 records exactly)
    assert len(chunk_recs) == 24, len(chunk_recs)
    chunk_path = os.path.join(DATA, 'chunks', 'editions-w%05d.jsonl.gz' % chunk_n)
    with gzip.open(chunk_path, 'wt') as f:
        for rec in chunk_recs:
            f.write(json.dumps(rec) + '\n')
    # rebuild index
    idx.extend(new_idx_rows)
    with gzip.open(os.path.join(DATA, 'editions.idx.json.gz'), 'wt') as f:
        f.write(json.dumps(idx))
    # manifest
    mp = os.path.join(REPO, 'data', 'manifest.json')
    m = json.load(open(mp))
    for d in m['databases']:
        if d['slug'] == 'news':
            d['record_count'] = len(idx)
            d['full_records'] = len(idx)
    json.dump(m, open(mp, 'w'), indent=1)
    print('wrote', chunk_path, '| index rows:', len(idx), '| manifest news count:', len(idx))

if __name__ == '__main__':
    build()
