#!/usr/bin/env python3
"""Wave 8 engine: builds public+Signature database pairs for the 1000 fun/social
list (home-life + creator-streaming themes). Property of Justin Addam Higgins (JAH).

For each item slug S:
  db/S/                  index.html + gen-S.js
  db/S-signature/        index.html + gen-S-signature.js
  data/S/index.jsonl.gz            (light: id,t,g)
  data/S/chunks/chunk-0000.jsonl.gz  (34 full records)
  data/S-signature/...            (same)
NEVER commits. NEVER touches data/manifest.json or api.json.
"""
import json, gzip, os, re, subprocess, sys, hashlib, html

ROOT_DB   = os.path.expanduser('~/workspace/jah-databases/db')
ROOT_DATA = os.path.expanduser('~/workspace/jah-databases-data-1/data')
CODE_DIR  = os.path.expanduser('~/workspace/jah-databases/code/wave8-build')
PREFIXES  = json.load(open(os.path.expanduser('~/workspace/hidden_files/wave8-prefixes.json')))
DATA_URL  = 'https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/'

TIERS = ['Foundations', 'Compounded', 'Advanced']
TIER_GUIDE = {
 'Foundations': 'Start here if the topic is new to you: one small change, done today, beats a perfect plan started next month. Foundations records are built to be tried in a single sitting with things you already have.',
 'Compounded': 'Once the foundations feel easy, compound them: stack two or three simple pieces into a small system that runs itself. Compounded records show how the parts fit together and keep working week after week.',
 'Advanced': 'Advanced records are for people who already run the basics and want mastery: finer control, bigger scope, and the judgment calls that only come from doing the work. Take one advanced idea at a time and make it yours.',
}

SIG_ADDENDA = [
 'Signature expansion: run it the Signature way - stamp every attempt with a date and a one-line outcome, keep the lineage of what worked, and let the record teach the next version of you.',
 'Signature expansion: the Signature system treats this as a boundless practice - generate ten variations, keep the three that fit your life, and file the winners so the archive remembers.',
 'Signature expansion: pair it with the teaching ladder - explain it to someone else in plain sentences, and whatever you cannot explain simply goes back to Foundations.',
 'Signature expansion: make it deterministic - same inputs, same setup, same result every time. When it drifts, the drift is the lesson; log it and tighten the system.',
 'Signature expansion: scale it the Signature way - what works for one day should work for thirty. Build the smallest version that survives a full month, then expand.',
 'Signature expansion: connect it to the network - every record here is one node in a million-record system. Cross-link it to your routines, your space, and your community so it compounds.',
]
SIG_STEPS = [
 'Stamp the attempt: date, setup, and one-line outcome, Signature style.',
 'Keep the lineage: note which variation worked so the next run starts ahead.',
]
SIG_POINTS = [
 'Signature rule: if it cannot be repeated, it was luck - systematize it.',
 'Signature rule: file the win so the archive - and future you - can reuse it.',
]

PROFANE = re.compile(r'\b(fuck\w*|shit\w*|bitch\w*|bastard|cunt\w*|dick\w*|piss\w*|damn)\b', re.I)

def det(seed_str, n, salt=''):
    h = int(hashlib.sha256((salt + '|' + seed_str).encode()).hexdigest(), 16)
    return h % n

# ---------------------------------------------------------------- demo programs
def _p_demo(kind, title, blurb, seed):
    T = title.replace('"', "'")
    if kind == 'planner':
        phases = ['Prepare', 'Set up', 'Execute', 'Review', 'Lock in']
        mins = [5 + det(T, 20, 'm%d' % i) for i in range(5)]
        lines = ['print("PLAN: %s")' % T,
                 'phases = %r' % [(p, m) for p, m in zip(phases, mins)],
                 'total = sum(m for _, m in phases)',
                 'for p, m in phases:',
                 '    print(f"  [ ] {p} - about {m} min")',
                 'print(f"Total focused time: {total} min")',
                 'print("Done when every box is checked.")']
    elif kind == 'checklist':
        items = ['Gather what you need', 'Clear the space', 'Do the core task',
                 'Tidy as you go', 'Review the result', 'Note what to repeat']
        lines = ['print("CHECKLIST: %s")' % T,
                 'items = %r' % items,
                 'for i, it in enumerate(items, 1):',
                 '    print(f"  [ ] {i}. {it}")',
                 'print(f"{len(items)} steps. Check them off as you finish.")']
    elif kind == 'calculator':
        a = 20 + det(T, 180, 'cost')
        b = 5 + det(T, 40, 'qty')
        lines = ['print("ESTIMATE: %s")' % T,
                 'unit_cost = %d' % a, 'qty = %d' % b,
                 'subtotal = unit_cost * qty',
                 'buffer = round(subtotal * 0.15, 2)',
                 'print(f"  unit: ${unit_cost} x {qty} = ${subtotal}")',
                 'print(f"  +15%% buffer: ${buffer}")',
                 'print(f"  plan for: ${subtotal + buffer}")']
    elif kind == 'scheduler':
        blocks = ['Focus block', 'Hands-on block', 'Break + reset', 'Finish + review']
        start = 9 + det(T, 4, 'hr')
        lines = ['print("SCHEDULE: %s")' % T,
                 'blocks = %r' % blocks, 'h = %d' % start,
                 'for b in blocks:',
                 '    print(f"  {h:02d}:00 - {b}")',
                 '    h += 1',
                 'print("Protect the first block - it sets the day.")']
    elif kind == 'quiz':
        qs = [('What is the smallest first step?', 'The one you can do in under five minutes.'),
              ('How do you know it worked?', 'You can describe the before-and-after in one sentence.'),
              ('What keeps it going?', 'A visible cue in the place where it happens.')]
        lines = ['print("QUICK CHECK: %s")' % T,
                 'qa = %r' % qs,
                 'for i, (q, a) in enumerate(qa, 1):',
                 '    print(f"Q{i}: {q}")',
                 '    print(f"A{i}: {a}")']
    elif kind == 'idea':
        bank = ['Try the 10-minute version first', 'Do it with a friend',
                'Photograph the before and after', 'Teach it to someone else',
                'Combine it with a favorite routine', 'Set a 7-day trial']
        k = 3 + det(T, 3, 'k')
        picks = sorted(set(det(T, len(bank), 'p%d' % i) for i in range(k * 2)))[:k]
        lines = ['print("IDEAS: %s")' % T,
                 'bank = %r' % bank, 'picks = %r' % picks,
                 'print("Seeded picks for this topic:")',
                 'for i in picks:',
                 '    print("  * " + bank[i])']
    elif kind == 'tracker':
        m1 = 1 + det(T, 6, 'm1'); m2 = 10 + det(T, 40, 'm2')
        lines = ['print("TRACKER: %s")' % T,
                 'days = 7', 'done = %d' % m1, 'minutes = %d' % m2,
                 'rate = round(100 * done / days, 1)',
                 'print(f"  days active: {done}/{days} ({rate}%%)")',
                 'print(f"  minutes invested: {minutes}")',
                 'print(f"  streak value: {done * minutes} point-days")',
                 'print("Aim: beat last week by one day.")']
    else:  # guide
        lines = ['print("GUIDE: %s")' % T,
                 'sections = ["Why it matters", "What you need", "How to do it", "Common mistakes", "Next level"]',
                 'for i, s in enumerate(sections, 1):',
                 '    print(f"{i}. {s}")',
                 'print("Work top to bottom; stop when it feels complete.")']
    return '\n'.join(lines) + '\n'

def run_demo(program):
    r = subprocess.run([sys.executable, '-c', program], capture_output=True, text=True, timeout=15)
    return r.returncode == 0, (r.stdout + r.stderr)[:500]

# ---------------------------------------------------------------- record builder
def build_record(item, idx, tier_i, title, blurb, sig, prefix, n):
    T = title
    field = item['fields'][tier_i]
    method = [s.format(T=T) for s in item['method']]
    points = [s.format(T=T) for s in item['points']]
    det_txt = item['details'][idx % len(item['details'])].format(T=T)
    desc = (blurb + ' ' + det_txt +
            '\n\n' + TIER_GUIDE[field] +
            ('\n\n' + SIG_ADDENDA[idx % len(SIG_ADDENDA)] if sig else ''))
    if sig:
        method = method + SIG_STEPS
        points = points + SIG_POINTS
    demo_kind = item.get('demo', 'guide')
    prog = _p_demo(demo_kind, T, blurb, prefix + str(n))
    ok, out = run_demo(prog)
    if not ok:
        raise RuntimeError('demo failed for %s: %s' % (T, out))
    rec = {
        'id': '%s%06d' % (prefix, n),
        't': T + (' (Signature Edition)' if sig else ''),
        'g': field,
        'name': (item['name'] + ' - ' + T + (' (Signature Edition)' if sig else '')),
        'title': T + (' (Signature Edition)' if sig else ''),
        'description': desc,
        'how_it_works': method,
        'key_points': points[:7],
        'requirements': item['req'].format(T=T),
        'standards': item['std'].format(T=T),
        'citations': item['cite'],
        'src': 'signature' if sig else 'public',
        'ladder_rank': n,
        'ladder_tier': field.lower(),
        'demo': {'kind': demo_kind + '-demo', 'language': 'python',
                 'program': prog,
                 'note': 'Runnable demonstration. Copy into any Python 3 runner; it prints a working plan for this record.'},
    }
    return rec

def light(rec):
    return {'id': rec['id'], 't': rec['t'], 'g': rec['g']}
