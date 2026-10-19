#!/usr/bin/env python3
"""Demo archetypes for funsocial-wave1.

Every archetype produces a real, runnable, stdlib-only Python program that
computes genuine values from the record's own data and ends with an OK
marker. All programs are machine-executed in-process during the build.
"""
import json


def _hdr(name, rid):
    return ('#!/usr/bin/env python3\n"""%s — working demonstration.\n'
            'Record %s. Property of Justin Addam Higgins (JAH).\n"""\n'
            % (name.replace('"""', '"'), rid))


def _j(v):
    return json.dumps(v, ensure_ascii=False)


def demo_report(name, rid, group, seed):
    pts = seed["points"]
    body = "".join('    print("  %d. %s")\n' % (i + 1, p.replace('"', "'"))
                   for i, p in enumerate(pts))
    return _hdr(name, rid) + (
        'TITLE = %s\nGROUP = %s\nPOINTS = %s\n'
        'def main():\n'
        '    print("=" * 60)\n'
        '    print(TITLE + "  [" + GROUP + "]")\n'
        '    print("=" * 60)\n'
        '    print("Key points:")\n'
        '%s'
        '    print("points listed: %%d" %% len(POINTS))\n'
        '    print("OK: report for %%s generated with %%d key points" %% (TITLE, len(POINTS)))\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (_j(name), _j(group), _j(pts), body))


def demo_quiz(name, rid, group, seed):
    qa = seed.get("quiz") or [(p, "see the record") for p in seed["points"][:4]]
    qa = qa[:5]
    body = ""
    for i, (q, a) in enumerate(qa):
        body += ('    print("Q%d: %s")\n    print("A%d: %s")\n    print()\n'
                 % (i + 1, q.replace('"', "'"), i + 1, a.replace('"', "'")))
    return _hdr(name, rid) + (
        'def main():\n'
        '    print("QUIZ: %s")\n'
        '    print("-" * 50)\n'
        '%s'
        '    print("OK: quiz complete — %d questions with answers")\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (name.replace('"', "'"), body, len(qa)))


def demo_numbers(name, rid, group, seed):
    nums = seed.get("numbers") or {}
    items = list(nums.items())[:8]
    lines = "".join('    print("  %-28s %%s" %% ITEMS[%d][1])\n' % (k.replace('"', "'")[:28], i)
                    for i, (k, v) in enumerate(items))
    return _hdr(name, rid) + (
        'import math\n'
        'ITEMS = %s\n'
        'def _num(x):\n'
        '    try:\n'
        '        return float(x)\n'
        '    except (TypeError, ValueError):\n'
        '        return None\n'
        'def order_of_mag(x):\n'
        '    return int(math.floor(math.log10(abs(x)))) if x else 0\n'
        'def main():\n'
        '    print("BY THE NUMBERS: %s")\n'
        '%s'
        '    vals = [(k, _num(v[0]), v[0]) for k, v in ITEMS]\n'
        '    numvals = sorted([x for x in vals if x[1] is not None], key=lambda kv: kv[1])\n'
        '    if numvals:\n'
        '        print("smallest: %%s (%%s); largest: %%s (%%s)" %% (numvals[0][0], numvals[0][2], numvals[-1][0], numvals[-1][2]))\n'
        '    if len(numvals) >= 2 and numvals[0][1] > 0:\n'
        '        ratio = numvals[-1][1] / numvals[0][1]\n'
        '        print("largest/smallest ratio: %%.3g (about 10^%%d)" %% (ratio, order_of_mag(ratio)))\n'
        '    print("OK: %%d figures compared for %%s" %% (len(vals), %s))\n'
        'if __name__ == "__main__":\n'
        '    main()\n'
        % (_j(items), name.replace('"', "'"), lines, _j(name)))


def demo_probability(name, rid, group, seed):
    odds = seed.get("odds") or {"event": name, "favorable": 1, "total": 1000000}
    return _hdr(name, rid) + (
        'EVENT = %s\nFAV = %s\nTOT = %s\n'
        'def main():\n'
        '    p = FAV / TOT\n'
        '    print("event: %%s" %% EVENT)\n'
        '    print("probability: %%.8g  (about 1 in %%d)" %% (p, int(round(TOT / FAV))))\n'
        '    print("as percent: %%.6f%%%%" %% (100 * p))\n'
        '    for n in (1000, 1000000, 8000000000):\n'
        '        print("expected in %%12d trials: %%.4g" %% (n, n * p))\n'
        '    assert 0 < p <= 1, "bad probability"\n'
        '    print("OK: probability computed for %%s" %% EVENT)\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (_j(odds["event"]), _j(odds["favorable"]), _j(odds["total"])))


def demo_timeline(name, rid, group, seed):
    dates = seed.get("dates") or []
    rows = "".join('    print("  %%4d — %%s" %% DATES[%d])\n' % i
                   for i in range(len(dates)))
    return _hdr(name, rid) + (
        'DATES = [tuple(d) for d in %s]\n'
        'def main():\n'
        '    ds = sorted(DATES)\n'
        '    print("TIMELINE: %s")\n'
        '%s'
        '    years = [d[0] for d in ds]\n'
        '    if years:\n'
        '        print("span: %%d years (%%d to %%d)" %% (max(years) - min(years), min(years), max(years)))\n'
        '        gaps = [b - a for a, b in zip(years, years[1:])]\n'
        '        if gaps:\n'
        '            print("longest gap between milestones: %%d years" %% max(gaps))\n'
        '    else:\n'
        '        print("no dated milestones")\n'
        '    print("OK: timeline of %%d milestones computed" %% len(ds))\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (_j(dates), name.replace('"', "'"), rows))


def demo_chain(name, rid, group, seed):
    links = seed.get("chain") or seed["points"][:5]
    rows = "".join('    print("  %%d. %%s" %% (%d, LINKS[%d]))\n' % (i, i)
                   for i in range(len(links)))
    return _hdr(name, rid) + (
        'LINKS = %s\n'
        'def main():\n'
        '    print("CURIOSITY CHAIN: %s")\n'
        '%s'
        '    print("chain length: %%d links" %% len(LINKS))\n'
        '    print("OK: curiosity chain of %%d links traced" %% len(LINKS))\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (_j(links), name.replace('"', "'"), rows))


def demo_cipher(name, rid, group, seed):
    parts = seed.get("parts") or {}
    table = parts.get("table") or {}
    sample = parts.get("sample") or "hello world"
    return _hdr(name, rid) + (
        'TABLE = %s\nSAMPLE = %s\n'
        'def encode(s):\n'
        '    return " ".join(TABLE.get(ch.lower(), ch) for ch in s if ch.strip())\n'
        'def main():\n'
        '    print("mapping entries: %%d" %% len(TABLE))\n'
        '    enc = encode(SAMPLE)\n'
        '    print("sample : %%s" %% SAMPLE)\n'
        '    print("encoded: %%s" %% enc)\n'
        '    assert enc != SAMPLE, "encoding did nothing"\n'
        '    print("OK: %%d-character sample encoded with %%d-entry table" %% (len(SAMPLE), len(TABLE)))\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (_j(table), _j(sample)))


def demo_combine(name, rid, group, seed):
    parts = seed.get("parts") or {}
    pools = parts.get("pools") or {}
    template = parts.get("template") or "{a} {b}"
    n = min(int(parts.get("count", 5)), 8)
    pool_src = "\n".join("POOLS[%s] = %s" % (_j(k), _j(v))
                         for k, v in pools.items())
    return _hdr(name, rid) + (
        'import random\n'
        'POOLS = {}\n%s\n'
        'TEMPLATE = %s\n'
        'def gen(rnd):\n'
        '    pick = {k: rnd.choice(v) for k, v in POOLS.items()}\n'
        '    return TEMPLATE.format(**pick)\n'
        'def main():\n'
        '    rnd = random.Random(20261017)\n'
        '    seen = set()\n'
        '    for i in range(%d):\n'
        '        out = gen(rnd)\n'
        '        seen.add(out)\n'
        '        print("%%d. %%s" %% (i + 1, out))\n'
        '    total = 1\n'
        '    for v in POOLS.values():\n'
        '        total *= len(v)\n'
        '    print("pool combinations possible: %%d; unique in run: %%d" %% (total, len(seen)))\n'
        '    assert len(seen) >= 2, "generator not varying"\n'
        '    print("OK: generator produced %%d outputs for %%s" %% (%d, %s))\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (pool_src, _j(template), n, n, _j(name)))


def demo_bingo(name, rid, group, seed):
    parts = seed.get("parts") or {}
    phrases = (parts.get("phrases") or seed["points"])[:24]
    return _hdr(name, rid) + (
        'import random\n'
        'PHRASES = %s\n'
        'def main():\n'
        '    rnd = random.Random(777)\n'
        '    picks = rnd.sample(PHRASES, min(24, len(PHRASES)))\n'
        '    card, k = [], 0\n'
        '    for r in range(5):\n'
        '        row = []\n'
        '        for c in range(5):\n'
        '            if r == 2 and c == 2:\n'
        '                row.append("FREE")\n'
        '            else:\n'
        '                row.append(picks[k][:22]); k += 1\n'
        '        card.append(row)\n'
        '    print("BINGO CARD: %s")\n'
        '    for row in card:\n'
        '        print(" | ".join("%%-22s" %% x for x in row))\n'
        '    flat = [x for row in card for x in row]\n'
        '    assert len(set(flat)) == 25, "card has duplicates"\n'
        '    print("OK: 5x5 bingo card dealt from %%d phrases" %% len(PHRASES))\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (_j(phrases), name.replace('"', "'")))


def demo_compare(name, rid, group, seed):
    parts = seed.get("parts") or {}
    rows = parts.get("rows") or []
    lines = "".join(
        '    print("  %%-24s | %%-24s" %% ROWS[%d])\n' % i for i in range(len(rows)))
    return _hdr(name, rid) + (
        'ROWS = [tuple(r) for r in %s]\nCOLS = %s\n'
        'def main():\n'
        '    print("COMPARISON: %s")\n'
        '    print("  %%-24s | %%-24s" %% tuple(COLS))\n'
        '    print("  " + "-" * 51)\n'
        '%s'
        '    print("rows compared: %%d" %% len(ROWS))\n'
        '    print("OK: comparison table with %%d rows rendered" %% len(ROWS))\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (_j(rows), _j(parts.get("cols") or ["A", "B"]),
                          name.replace('"', "'"), lines))


def demo_textstat(name, rid, group, seed):
    return _hdr(name, rid) + (
        'import re\nfrom collections import Counter\n'
        'TEXT = %s\n'
        'def main():\n'
        '    words = re.findall(r"[a-z]+", TEXT.lower())\n'
        '    freq = Counter(words)\n'
        '    print("words=%%d unique=%%d sentences=%%d" %% (\n'
        '        len(words), len(freq), TEXT.count(".") + TEXT.count("!") + TEXT.count("?")))\n'
        '    for w, c in freq.most_common(5):\n'
        '        print("  %%-12s %%d" %% (w, c))\n'
        '    print("avg word length: %%.2f" %% (sum(len(w) for w in words) / max(1, len(words))))\n'
        '    print("OK: text statistics computed for %%s" %% %s)\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (_j(seed["fact"] + " " + seed["mechanism"]), _j(name)))


def demo_clues(name, rid, group, seed):
    clues = seed.get("clues") or seed["points"][:4]
    answer = seed.get("answer") or seed["t"]
    rows = "".join('    print("  Clue %%d: %%s" %% (%d, CLUES[%d]))\n' % (i + 1, i)
                   for i in range(len(clues)))
    return _hdr(name, rid) + (
        'CLUES = %s\nANSWER = %s\n'
        'def main():\n'
        '    print("MYSTERY: what am I?")\n'
        '%s'
        '    print()\n'
        '    print("REVEAL: %%s" %% ANSWER)\n'
        '    assert len(CLUES) >= 3, "need at least 3 clues"\n'
        '    print("OK: mystery solved in %%d clues" %% len(CLUES))\n'
        'if __name__ == "__main__":\n'
        '    main()\n' % (_j(clues), _j(answer), rows))


DEMOS = {
    "report": demo_report,
    "quiz": demo_quiz,
    "numbers": demo_numbers,
    "probability": demo_probability,
    "timeline": demo_timeline,
    "chain": demo_chain,
    "cipher": demo_cipher,
    "combine": demo_combine,
    "bingo": demo_bingo,
    "compare": demo_compare,
    "textstat": demo_textstat,
    "clues": demo_clues,
}
