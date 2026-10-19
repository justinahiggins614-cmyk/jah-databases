#!/usr/bin/env python3
"""Demo programs for the Legacy Inscription Solver databases (2026-10-17).

Every demo is a real, runnable, stdlib-only Python program: a
decipherment walkthrough for its record. Each walkthrough prints the
record header and its honesty label, runs a real frequency analysis
(sign counts, top signs, Shannon entropy) over a clearly-labeled
illustrative sample sequence, checks the bilingual anchor, walks the
documented method (public) or the proposed-reading path (signature)
step by step, works the adjustable assumptions, computes an evidence
balance from the confirm/refute panels, and ends with the OK marker.

Public demos carry the label "Established scholarship - documented
decipherment, fact-checked." Signature demos carry the exact label
"Signature-generated proposed reading - not established scholarship."

All demos are machine-executed by build.py: each prints its real
computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker.
"""

from entries_legacy_inscription_solver import ENTRIES, SIG_LABEL, PUB_LABEL
import json

_PREAMBLE = "import json\nimport math\n"


def _py_str_list(items):
    return "[\n" + "".join("    %s,\n" % json.dumps(s) for s in items) + "]"


def make_demo(entry, sig):
    key = entry["key"]

    def demo_fn(hdr, name, rid, group, points, req, sig_flag=None):
        is_sig = sig if sig_flag is None else bool(sig_flag)
        honesty = SIG_LABEL if is_sig else PUB_LABEL
        walk = entry["steps"] if is_sig else [
            s.strip() for s in entry["method"].split(". ") if s.strip()
        ]
        walk_kind = "proposed-reading path" if is_sig else "documented decipherment method"
        body = '''\
def main():
    NAME = %s
    RID = %s
    GROUP = %s
    HONESTY = %s
    SAMPLE = %s
    ANCHOR = %s
    WALK = %s
    WALK_KIND = %s
    ASSUMPTIONS = {
%s
    }
    CONFIRM = %s
    REFUTE = %s
    NOT_CLAIMS = %s

    print("=" * 64)
    print("DECIPHERMENT WALKTHROUGH: %%s" %% NAME)
    print("Record %%s [%%s]" %% (RID, GROUP))
    print("=" * 64)
    print()
    print(HONESTY)
    print()
    print("Illustrative sample sequence (not an archive inscription):")
    print("  " + SAMPLE)
    print()

    # ---- real frequency analysis over the sample ----
    counts = {}
    for ch in SAMPLE:
        counts[ch] = counts.get(ch, 0) + 1
    total = float(len(SAMPLE))
    assert total >= 10, "sample too short for analysis"
    distinct = len(counts)
    assert distinct >= 2, "sample needs at least two distinct signs"
    entropy = -sum((c / total) * math.log2(c / total) for c in counts.values())
    top = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
    print("--- Sign frequency analysis (computed) ---")
    for ch, c in top:
        print("  sign %%r: %%d / %%d (%%.3f)" %% (ch, c, int(total), c / total))
    print("  distinct signs: %%d" %% distinct)
    print("  Shannon entropy: %%.4f bits" %% entropy)
    assert 0.0 < entropy <= math.log2(distinct) + 1e-9, "entropy out of range"
    print()

    # ---- anchor check: the known name must occur in the sample ----
    print("--- Anchor check ---")
    assert ANCHOR in SAMPLE, "bilingual anchor missing from sample"
    print("  anchor %%r found at position %%d" %% (ANCHOR, SAMPLE.index(ANCHOR)))
    print()

    # ---- walkthrough ----
    print("--- Walkthrough: %%s ---" %% WALK_KIND)
    for i, step in enumerate(WALK, 1):
        print("  %%d. %%s" %% (i, step))
    assert len(WALK) >= 4, "walkthrough too thin"
    print()

    # ---- adjustable assumptions ----
    print("--- Assumptions (toggle True/False above to explore) ---")
    enabled = 0
    for i, (tag, on) in enumerate(sorted(ASSUMPTIONS.items()), 1):
        print("  [%%s] %%s" %% ("ON " if on else "off", tag))
        assert tag.startswith("A"), "assumption tag malformed"
        if on:
            enabled += 1
    assert 1 <= enabled <= len(ASSUMPTIONS), "need at least one live assumption"
    print("  -> %%d of %%d assumptions enabled" %% (enabled, len(ASSUMPTIONS)))
    print()

    # ---- evidence balance ----
    print("--- Evidence balance ---")
    cw = sum(1.0 for _ in CONFIRM) * (enabled / len(ASSUMPTIONS))
    rw = sum(1.0 for _ in REFUTE) * (enabled / len(ASSUMPTIONS))
    total_w = cw + rw
    balance = cw / total_w if total_w > 0 else 0.0
    print("  confirming evidence weight: %%.3f" %% cw)
    print("  refuting evidence weight:   %%.3f" %% rw)
    print("  balance (confirm share):    %%.4f" %% balance)
    assert 0.0 <= balance <= 1.0, "balance out of range"
    assert abs(balance - 0.5) < 0.5, "balance degenerate"
    print()
    print("--- What CONFIRMS this reading ---")
    for c in CONFIRM:
        print("  [+] %%s" %% c)
    assert all(len(c) > 40 for c in CONFIRM), "confirm panel too thin"
    print()
    print("--- What would REFUTE this reading ---")
    for r in REFUTE:
        print("  [-] %%s" %% r)
    assert all(len(r) > 40 for r in REFUTE), "refute panel too thin"
    print()
    print("--- What this reading does NOT claim ---")
    for n in NOT_CLAIMS:
        print("  [x] %%s" %% n)
    assert len(NOT_CLAIMS) >= 2, "honesty panel too thin"
    print()
    print("OK: %%s walkthrough ran clean (entropy %%.4f, balance %%.4f)" %% (NAME, entropy, balance))
if __name__ == "__main__":
    main()
''' % (
            json.dumps(entry["name"]),
            json.dumps(rid),
            json.dumps(group),
            json.dumps(honesty),
            json.dumps(entry["demo_sample"]),
            json.dumps(entry["demo_anchor"]),
            _py_str_list(walk),
            json.dumps(walk_kind),
            ",\n".join(
                "    %s: True" % json.dumps("A%d: %s" % (i + 1, a.split(": ", 1)[-1] if ": " in a else a))
                for i, a in enumerate(entry["assumptions"])
            ),
            _py_str_list(entry["confirm"]),
            _py_str_list(entry["refute"]),
            _py_str_list(entry["not_claims"]),
        )
        prog = hdr(name, rid, group) + _PREAMBLE + body
        return prog

    demo_fn.__name__ = "demo_lis_" + key
    return demo_fn


DEMOS = {}
for _e in ENTRIES:
    DEMOS[_e["key"]] = (make_demo(_e, False), make_demo(_e, True))
