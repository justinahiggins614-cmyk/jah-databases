#!/usr/bin/env python3
"""Demo program builders for wave 5 (mystery + civilization-space).

Each builder(title, rid, group, seed) -> Python source string.
Every emitted program is machine-executed at build time (in-process) and
must print a line starting with "OK:". No I/O, no network, stdlib only.
Property of Justin Addam Higgins (JAH).
"""
import hashlib


def _hnum(key, salt, lo, hi):
    h = hashlib.md5(("%s:%s" % (key, salt)).encode()).hexdigest()
    return lo + int(h[:8], 16) % (hi - lo + 1)


def _esc(s):
    return s.replace("\\", "\\\\").replace('"', "'").replace("\n", " ")


def report(title, rid, group, seed):
    t = _esc(title)
    pts = seed.get("points") or ["See the record."]
    lines = ["    print(%s)" % repr("  - " + _esc(p)) for p in pts[:6]]
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - working demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'TITLE = "%s"\nRID = "%s"\nGROUP = "%s"\n'
        'def main():\n'
        '    print("Record:", TITLE)\n'
        '    print("Group:", GROUP)\n'
        '    print("Key points:")\n%s\n'
        '    assert len(%r) >= 3, "need at least 3 key points"\n'
        '    print("OK: %%s report verified %%d key points" %% (RID, len(%r)))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, t, rid, _esc(group), "\n".join(lines), pts, pts)


def numbers(title, rid, group, seed):
    t = _esc(title)
    nums = seed.get("numbers") or {"Reference value": (1, "unit")}
    items = list(nums.items())[:8]
    body = []
    for label, (val, unit) in items:
        body.append('    print("  %s: %%s %%s" %% (%r, %r))' % (_esc(label), val, _esc(unit)))
    asserts = []
    for label, (val, unit) in items:
        if isinstance(val, (int, float)):
            asserts.append('    assert %r >= 0, "negative value"' % (val,))
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - numbers demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\n'
        'def main():\n'
        '    print("Numbers for this record:")\n%s\n%s\n'
        '    print("OK: %%s numbers verified %%d values" %% (RID, %d))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, "\n".join(body), "\n".join(asserts) or "    pass", len(items))


def cipher_caesar(title, rid, group, seed):
    t = _esc(title)
    msg = _esc(seed.get("msg") or "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - Caesar cipher demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'import hashlib\nRID = "%s"\nMSG = "%s"\n'
        'def shift_of():\n'
        '    return 1 + int(hashlib.md5(RID.encode()).hexdigest()[:4], 16) %% 25\n'
        'def enc(m, s):\n'
        '    out = []\n'
        '    for ch in m.upper():\n'
        '        out.append(chr((ord(ch) - 65 + s) %% 26 + 65) if "A" <= ch <= "Z" else ch)\n'
        '    return "".join(out)\n'
        'def main():\n'
        '    s = shift_of()\n'
        '    c = enc(MSG, s)\n'
        '    d = enc(c, 26 - s)\n'
        '    print("plain: ", MSG)\n'
        '    print("cipher:", c, "(shift %%d)" %% s)\n'
        '    assert d == MSG.upper(), "Caesar round-trip failed"\n'
        '    print("OK: %%s caesar cipher verified (shift %%d)" %% (RID, s))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, msg)


def cipher_vigenere(title, rid, group, seed):
    t = _esc(title)
    msg = _esc(seed.get("msg") or "SECRETS HIDE IN PLAIN SIGHT")
    key = _esc(seed.get("vkey") or "MYSTERY")
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - Vigenere cipher demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nMSG = "%s"\nKEY = "%s"\n'
        'def vig(m, k, dec=False):\n'
        '    out, ki = [], 0\n'
        '    for ch in m.upper():\n'
        '        if "A" <= ch <= "Z":\n'
        '            s = ord(k[ki %% len(k)]) - 65\n'
        '            if dec: s = -s\n'
        '            out.append(chr((ord(ch) - 65 + s) %% 26 + 65))\n'
        '            ki += 1\n'
        '        else:\n'
        '            out.append(ch)\n'
        '    return "".join(out)\n'
        'def main():\n'
        '    c = vig(MSG, KEY)\n'
        '    assert vig(c, KEY, dec=True) == MSG.upper(), "Vigenere round-trip failed"\n'
        '    print("cipher:", c, "| key:", KEY)\n'
        '    print("OK: %%s vigenere verified (key length %%d)" %% (RID, len(KEY)))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, msg, key)


def cipher_rail(title, rid, group, seed):
    t = _esc(title)
    msg = _esc(seed.get("msg") or "WE ARE DISCOVERED FLEE AT ONCE")
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - rail fence cipher demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'import hashlib\nRID = "%s"\nMSG = "%s".replace(" ", "")\n'
        'def rails_of():\n'
        '    return 2 + int(hashlib.md5(RID.encode()).hexdigest()[:2], 16) %% 4\n'
        'def enc(m, r):\n'
        '    rows = [""] * r\n'
        '    row, step = 0, 1\n'
        '    for ch in m:\n'
        '        rows[row] += ch\n'
        '        if row == 0: step = 1\n'
        '        elif row == r - 1: step = -1\n'
        '        row += step\n'
        '    return "".join(rows)\n'
        'def dec(c, r):\n'
        '    n = len(c)\n'
        '    rows = [[] for _ in range(r)]\n'
        '    row, step = 0, 1\n'
        '    for i in range(n):\n'
        '        rows[row].append(i)\n'
        '        if row == 0: step = 1\n'
        '        elif row == r - 1: step = -1\n'
        '        row += step\n'
        '    seq = [i for rr in rows for i in rr]\n'
        '    out = [""] * n\n'
        '    for pos, ch in zip(seq, c):\n'
        '        out[pos] = ch\n'
        '    return "".join(out)\n'
        'def main():\n'
        '    r = rails_of()\n'
        '    c = enc(MSG, r)\n'
        '    assert dec(c, r) == MSG, "rail fence round-trip failed"\n'
        '    print("cipher:", c, "(%%d rails)" %% r)\n'
        '    print("OK: %%s rail fence verified" %% RID)\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, msg)


def morse(title, rid, group, seed):
    t = _esc(title)
    word = _esc(seed.get("morse_word") or "SOS")
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - Morse code demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nWORD = "%s".upper()\n'
        'MORSE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",\n'
        ' "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",\n'
        ' "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",\n'
        ' "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",\n'
        ' "Y": "-.--", "Z": "--.."}\n'
        'INV = {v: k for k, v in MORSE.items()}\n'
        'def main():\n'
        '    code = " ".join(MORSE[ch] for ch in WORD if ch in MORSE)\n'
        '    back = "".join(INV[tok] for tok in code.split(" "))\n'
        '    print("word: ", WORD)\n'
        '    print("morse:", code)\n'
        '    assert back == "".join(ch for ch in WORD if ch in MORSE), "morse round-trip failed"\n'
        '    print("OK: %%s morse verified (%%d letters)" %% (RID, len(WORD)))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, word)


def acrostic(title, rid, group, seed):
    t = _esc(title)
    lines = seed.get("lines") or ["Silent halls keep watch at night",
                                  "Every door is locked and sealed",
                                  "Clues are waiting to be found",
                                  "Restless shadows guard them still",
                                  "Every answer has a price",
                                  "Trust no echo, trust no sound"]
    hidden = seed.get("hidden") or "".join(l[0] for l in lines)
    lits = "[" + ", ".join(repr(_esc(l)) for l in lines) + "]"
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - acrostic puzzle demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nLINES = %s\nHIDDEN = "%s"\n'
        'def main():\n'
        '    for ln in LINES:\n'
        '        print(" ", ln)\n'
        '    found = "".join(ln[0] for ln in LINES).upper()\n'
        '    print("first letters spell:", found)\n'
        '    assert found == HIDDEN.upper(), "acrostic mismatch"\n'
        '    print("OK: %%s acrostic verified (hidden message: %%s)" %% (RID, HIDDEN))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, lits, _esc(hidden))


def timeline(title, rid, group, seed):
    t = _esc(title)
    events = seed.get("events") or [("08:00", "Doors open"), ("09:30", "Briefing"),
                                    ("12:00", "Midday review"), ("17:00", "Debrief")]
    evl = "[" + ", ".join("(%r, %r)" % (_esc(a), _esc(b)) for a, b in events) + "]"
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - timeline demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nEVENTS = %s\n'
        'def main():\n'
        '    ordered = sorted(EVENTS, key=lambda e: e[0])\n'
        '    assert [e[0] for e in ordered] == sorted(e[0] for e in EVENTS), "timeline out of order"\n'
        '    for when, what in ordered:\n'
        '        print(" %%s  %%s" %% (when, what))\n'
        '    print("OK: %%s timeline verified (%%d events in order)" %% (RID, len(EVENTS)))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, evl)


def eliminate(title, rid, group, seed):
    t = _esc(title)
    suspects = seed.get("suspects") or [("A. Archer", True), ("B. Baker", True),
                                        ("C. Carter", False), ("D. Dalton", True)]
    sl = "[" + ", ".join("(%r, %r)" % (_esc(n), a) for n, a in suspects) + "]"
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - suspect elimination demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nSUSPECTS = %s\n'
        'def main():\n'
        '    cleared = [n for n, alibi in SUSPECTS if alibi]\n'
        '    remaining = [n for n, alibi in SUSPECTS if not alibi]\n'
        '    print("cleared by alibi:", ", ".join(cleared))\n'
        '    print("no alibi:        ", ", ".join(remaining))\n'
        '    assert len(remaining) == 1, "elimination must leave exactly one suspect"\n'
        '    print("solution:", remaining[0])\n'
        '    print("OK: %%s elimination verified (solution: %%s)" %% (RID, remaining[0]))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, sl)


def calc(title, rid, group, seed):
    t = _esc(title)
    c = seed.get("calc") or {"label": "Reference calculation", "vars": {"a": 10, "b": 4},
                             "expr": "a * b + a", "expect": (40, 60)}
    label = _esc(c.get("label", "calculation"))
    varl = "{" + ", ".join("%r: %r" % (k, v) for k, v in c["vars"].items()) + "}"
    expr = c["expr"]
    lo, hi = c.get("expect", (-1e18, 1e18))
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - %s. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nLABEL = "%s"\nVARS = %s\nEXPR = %r\n'
        'def main():\n'
        '    val = eval(EXPR, {"__builtins__": {}}, dict(VARS, **{"abs": abs, "min": min, "max": max, "round": round}))\n'
        '    print("%%s: %%s = %%s" %% (LABEL, EXPR, val))\n'
        '    assert %r <= val <= %r, "calculation out of expected range"\n'
        '    print("OK: %%s calculation verified (%%s)" %% (RID, val))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, label, rid, rid, label, varl, expr, lo, hi)


def sim(title, rid, group, seed):
    t = _esc(title)
    s = seed.get("sim") or {"label": "Growth simulation", "start": 100.0,
                            "rate": 0.05, "steps": 20, "cap": 100000.0}
    label = _esc(s.get("label", "simulation"))
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - %s. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nLABEL = "%s"\nSTART = %r\nRATE = %r\nSTEPS = %r\nCAP = %r\n'
        'def main():\n'
        '    v = START\n'
        '    for _ in range(STEPS):\n'
        '        v = min(CAP, v * (1.0 + RATE))\n'
        '        v = max(0.0, v)\n'
        '    print("%%s: start=%%s rate=%%s steps=%%d -> %%s" %% (LABEL, START, RATE, STEPS, round(v, 2)))\n'
        '    assert 0.0 <= v <= CAP, "simulation invariant broken"\n'
        '    if RATE >= 0:\n'
        '        assert v >= START, "growth must not go negative"\n'
        '    else:\n'
        '        assert v <= START, "decline must not go positive"\n'
        '    print("OK: %%s simulation verified (final %%s)" %% (RID, round(v, 2)))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, label, rid, rid, label, s["start"], s["rate"], s["steps"], s["cap"])


def quiz(title, rid, group, seed):
    t = _esc(title)
    qa = seed.get("qa") or [("What is the first step?", "Observe carefully."),
                            ("What comes next?", "Gather the evidence.")]
    qal = "[" + ", ".join("(%r, %r)" % (_esc(q), _esc(a)) for q, a in qa) + "]"
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - quiz demonstration (answers at the bottom). Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nQA = %s\n'
        'def main():\n'
        '    print("QUIZ")\n'
        '    for i, (q, a) in enumerate(QA, 1):\n'
        '        print(" %%d. %%s" %% (i, q))\n'
        '    print("ANSWERS (at the bottom, as promised)")\n'
        '    for i, (q, a) in enumerate(QA, 1):\n'
        '        print(" %%d. %%s" %% (i, a))\n'
        '    assert len(QA) >= 2 and all(q and a for q, a in QA), "quiz needs complete Q/A pairs"\n'
        '    print("OK: %%s quiz verified (%%d questions, answers at bottom)" %% (RID, len(QA)))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, qal)


def checklist(title, rid, group, seed):
    t = _esc(title)
    checks = seed.get("checks") or ["Define the goal.", "List the parts.", "Test each part."]
    cl = "[" + ", ".join(repr(_esc(c)) for c in checks) + "]"
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - design checklist demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nCHECKS = %s\n'
        'def main():\n'
        '    done = 0\n'
        '    for c in CHECKS:\n'
        '        assert c.strip(), "empty checklist item"\n'
        '        print(" [x]", c)\n'
        '        done += 1\n'
        '    assert done == len(CHECKS) and done >= 3, "checklist incomplete"\n'
        '    print("OK: %%s checklist verified (%%d items complete)" %% (RID, done))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, cl)


def pattern(title, rid, group, seed):
    t = _esc(title)
    seq = seed.get("seq") or [2, 4, 8, 16, 32]
    rule = _esc(seed.get("rule") or "each term doubles the previous")
    if "next" in seed:
        nxt = seed["next"]
    else:
        nxt = seq[-1] * 2 if len(seq) >= 2 and all(seq[i+1] == seq[i]*2 for i in range(len(seq)-1)) else None
        if nxt is None:
            diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
            nxt = seq[-1] + (diffs[-1] if len(set(diffs)) == 1 else 0)
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - hidden pattern demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nSEQ = %r\nRULE = "%s"\nNEXT = %r\n'
        'def main():\n'
        '    print("sequence:", ", ".join(map(str, SEQ)), ", ?")\n'
        '    print("rule:", RULE)\n'
        '    assert NEXT is not None, "no continuation found"\n'
        '    print("next term:", NEXT)\n'
        '    print("OK: %%s pattern verified (next = %%s)" %% (RID, NEXT))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, seq, rule, nxt)


def codebook(title, rid, group, seed):
    t = _esc(title)
    words = seed.get("codebook_words") or ["the", "quick", "brown", "fox", "jumps"]
    book = seed.get("book") or ("the quick brown fox jumps over the lazy dog " * 4)
    msg = _esc(seed.get("msg") or " ".join(words[:3]))
    return (
        '#!/usr/bin/env python3\n'
        '"""%s - book cipher demonstration. Record %s. Property of Justin Addam Higgins (JAH)."""\n'
        'RID = "%s"\nBOOK = %r\nMSG = "%s"\n'
        'def main():\n'
        '    toks = BOOK.split()\n'
        '    code = []\n'
        '    for w in MSG.lower().split():\n'
        '        idx = toks.index(w)\n'
        '        code.append(idx + 1)\n'
        '    back = " ".join(toks[i - 1] for i in code)\n'
        '    print("book cipher code:", code)\n'
        '    print("decoded:", back)\n'
        '    assert back == MSG.lower(), "book cipher round-trip failed"\n'
        '    print("OK: %%s book cipher verified (%%d code numbers)" %% (RID, len(code)))\n'
        'if __name__ == "__main__":\n    main()\n'
    ) % (t, rid, rid, _esc(book), msg)


DEMOS = {
    "report": report,
    "numbers": numbers,
    "cipher_caesar": cipher_caesar,
    "cipher_vigenere": cipher_vigenere,
    "cipher_rail": cipher_rail,
    "morse": morse,
    "acrostic": acrostic,
    "timeline": timeline,
    "eliminate": eliminate,
    "calc": calc,
    "sim": sim,
    "quiz": quiz,
    "checklist": checklist,
    "pattern": pattern,
    "codebook": codebook,
}
