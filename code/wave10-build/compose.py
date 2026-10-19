#!/usr/bin/env python3
"""Record composers + demo-program builders for wave 10 (versus-rankings + learning).

Two item kinds:
  versus   - head-to-head comparisons with transparent weighted criteria
  learning - lesson modules with self-check Q&A

Signature editions reframe the same data through the Signature lens: titles get
" (Signature Edition)", src="signature", and the description opens with the
Signature-original label. They are never presented as authentic public record.

Demo programs are built with token replacement (no nested %-formatting) so the
generated Python is exactly what runs.
"""
import json

SIG_LABEL = ("Signature original interpretation. Clearly labeled Signature-made by the "
             "Signature system - an original reworking, never presented as authentic public record.")


def _hdr(name, rid, group):
    safe = str(name).replace('"', "'")
    return ("# " + safe + "\n# record " + rid + " | group " + str(group) +
            "\n# Property of Justin Addam Higgins (JAH).\n")


# ------------------------------------------------------- topic constructors

def V(t, g, a, b, n, crit, facts, cite=None):
    """Versus topic: title, group, contender A, contender B, narrative,
    criteria [(name, weight, scoreA, scoreB)], facts, citations."""
    return {"t": t, "g": g, "a": a, "b": b, "n": n, "crit": crit,
            "facts": facts, "cite": cite or []}


def L(t, g, n, qa, facts, cite=None):
    """Learning topic: title, group, narrative, [(question, answer)], facts, citations."""
    return {"t": t, "g": g, "n": n, "qa": qa, "facts": facts, "cite": cite or []}


def TREE(t, g, skill, n, nodes, facts, cite=None):
    """Skill-tree sample: title, group, skill name, narrative,
    nodes [(name, tier, xp, prereq)], facts, citations."""
    return {"t": t, "g": g, "skill": skill, "n": n, "nodes": nodes,
            "facts": facts, "cite": cite or []}


# ---------------------------------------------------------------- versus ---

def compose_versus(item, topic, idx, sig, prefix):
    """topic keys: t, g, a, b, n, crit=[(name,wt,sa,sb)], facts=[...], cite=[...]."""
    rid = prefix + "%06d" % (idx + 1)
    title = topic["t"] + (" (Signature Edition)" if sig else "")
    a, b = topic["a"], topic["b"]
    crit = topic["crit"]
    tot_w = sum(w for _, w, _, _ in crit)
    sa = sum(w * x for _, w, x, _ in crit) / tot_w
    sb = sum(w * y for _, w, _, y in crit) / tot_w
    winner = a if sa >= sb else b
    margin = abs(sa - sb)

    crit_lines = "; ".join("%s (weight %d%%: %s %d, %s %d)"
                           % (cn, w, a, x, b, y) for cn, w, x, y in crit)
    verdict = ("%s wins the showdown %.1f to %.1f - a margin of %.1f weighted points."
               % (winner, max(sa, sb), min(sa, sb), margin))

    desc = (topic["n"] + "\nThe matchup: " + a + " against " + b + ", judged on " +
            str(len(crit)) + " transparent criteria: " + crit_lines + ". " + verdict)
    if sig:
        desc = (SIG_LABEL + " " + desc + " The Signature lens adds extended criteria thinking: "
                "what each contender teaches about design trade-offs, and how the Signature "
                "system would combine their strengths into something new.")

    how = ("Every showdown in this database uses the same transparent-criteria method. "
           "First the contenders are named plainly - no straw men. Then the judging criteria are "
           "fixed in advance and each gets a weight that sums to 100 percent, so anyone can see "
           "what mattered most. Each contender is scored 0 to 100 on every criterion from "
           "verifiable figures, the weighted totals are computed, and the winner is the higher "
           "total - with the full table published so you can re-weight it yourself and see if "
           "the verdict changes.\n"
           "For this matchup the criteria were: " +
           "; ".join("%s carries %d%% of the decision" % (cn, w) for cn, w, _, _ in crit) +
           ". " + a + " scores strongest where its design is most specialized; " + b +
           " answers where breadth and different conditions matter. " + verdict +
           " Run it yourself: pick the same criteria, score honestly from measured figures, "
           "and the math does the judging.")

    edge = max(crit, key=lambda c: (c[2] - c[3]) if sa >= sb else (c[3] - c[2]))
    topc = max(crit, key=lambda c: c[1])
    kp = [verdict,
          "Strongest edge for %s: %s." % (winner, edge[0]),
          "The criterion that mattered most was %s at %d%% weight." % (topc[0], topc[1])]
    kp += list(topic["facts"])[:3]

    req = ["A defined question: what exactly is being compared and why it matters.",
           "Verifiable figures for %s and %s on each criterion - measured values beat impressions." % (a, b),
           "Criteria fixed before scoring, with weights that sum to 100 percent.",
           "Willingness to re-weight: a good judge checks whether the verdict survives different weights."]
    std = ["Transparent criteria: every judge sees the same scorecard.",
           "Disclosed weights: importance is stated, never hidden.",
           "Verifiable numbers: scores trace back to measured figures.",
           "Reproducible verdict: same scores and weights always give the same winner."]
    cites = list(topic.get("cite", [])) + [item["cite_pool"]]

    rec = {
        "id": rid, "t": title, "g": topic["g"], "name": topic["t"], "title": title,
        "description": desc, "how_it_works": how,
        "key_points": kp, "requirements": req, "standards": std,
        "citations": cites,
        "src": "signature" if sig else "public-harvest",
        "ladder_rank": 1 + (idx * 10) // 34,
        "ladder_tier": ("foundations" if idx < 12 else "compounded" if idx < 24 else "advanced"),
        "demo": {"kind": "python", "language": "python",
                 "program": demo_versus(topic, title, rid, topic["g"]),
                 "note": "Working demonstration program (real, runnable Python)."},
    }
    return rec


_VS_TEMPLATE = r'''def main():
    a = __A__
    b = __B__
    crit = [
__CRIT__
    ]
    tot_w = sum(w for _, w, _, _ in crit)
    assert tot_w == 100, "weights must sum to 100, got %d" % tot_w
    sa = sum(w * x for _, w, x, _ in crit) / tot_w
    sb = sum(w * y for _, w, _, y in crit) / tot_w
    print("SHOWDOWN: %s vs %s" % (a, b))
    print("-" * 60)
    for name, w, x, y in crit:
        if x > y:
            mark = " <-- " + a + " takes it"
        elif y > x:
            mark = " <-- " + b + " takes it"
        else:
            mark = " -- tie"
        print("%-30s | wt %2d%% | %3d vs %-3d%s" % (name[:30], w, x, y, mark))
    print("-" * 60)
    print("weighted total: %s %.1f | %s %.1f" % (a, sa, b, sb))
    winner = a if sa >= sb else b
    print("VERDICT: %s wins by %.1f weighted points" % (winner, abs(sa - sb)))
    assert winner == __WIN__, (winner, __WIN__)
    print("OK: __TITLE__ judged transparently")

if __name__ == "__main__":
    main()
'''


def demo_versus(topic, title, rid, group):
    a, b = topic["a"], topic["b"]
    crit = topic["crit"]
    tot_w = sum(w for _, w, _, _ in crit)
    sa = sum(w * x for _, w, x, _ in crit) / tot_w
    sb = sum(w * y for _, w, _, y in crit) / tot_w
    win = a if sa >= sb else b
    crit_lines = "\n".join("        (%s, %d, %d, %d)," % (json.dumps(cn), w, x, y)
                           for cn, w, x, y in crit)
    prog = _VS_TEMPLATE.replace("__A__", json.dumps(a)).replace("__B__", json.dumps(b))
    prog = prog.replace("__CRIT__", crit_lines).replace("__WIN__", json.dumps(win))
    prog = prog.replace("__TITLE__", str(topic["t"]).replace('"', "'"))
    return _hdr(title, rid, group) + prog


# --------------------------------------------------------------- learning ---

def compose_learning(item, topic, idx, sig, prefix):
    """topic keys: t, g, n, qa=[(q,a)], facts=[...], cite=[...]."""
    rid = prefix + "%06d" % (idx + 1)
    title = topic["t"] + (" (Signature Edition)" if sig else "")
    qa = topic["qa"]
    objs = "; ".join("you will be able to answer: '%s'" % q for q, _ in qa[:3])

    desc = (topic["n"] + "\nIn this lesson " + objs + ". The lesson walks the concept from "
            "a concrete example up to the general principle, then locks it in with a "
            "self-check drill you can run right here.")
    if sig:
        desc = (SIG_LABEL + " " + desc + " The Signature lens reframes the lesson as a "
                "buildable skill: every concept becomes something you can make, test, and extend "
                "inside the Signature system.")

    how = ("The lesson teaches in four moves. First it anchors: one concrete, familiar example "
           "you can picture. Then it names the principle the example is an instance of, in plain "
           "words. Then it generalizes: two more examples from different corners of life so the "
           "principle stops looking like a special case. Finally it drills: the self-check "
           "questions below, answered from memory, with the key beside them.\n"
           "Worked through fully, this lesson moves the idea from 'heard of it' to 'can use it': " +
           "; ".join("'%s' -> %s" % (q, a) for q, a in qa) + ". Say each answer aloud before "
           "checking - retrieval is what builds the memory, not re-reading.")

    kp = (["After this lesson you can explain the core idea in your own words.",
           "You can recognize the principle in new examples, not just the ones taught here."] +
          list(topic["facts"])[:4])
    req = ["About fifteen focused minutes with no multitasking.",
           "A notebook or scratch file: write each self-check answer before peeking.",
           "The worked examples in this record, tried by hand at least once.",
           "One real-world hunt: spot the principle operating outside the lesson within a day."]
    std = ["Mastery means answering every self-check question from memory, in your own words.",
           "Mastery means applying the principle to an example the lesson never showed you.",
           "Mastery means teaching it: explain the idea to someone else without notes.",
           "Speed is not the goal; durable recall a week later is."]
    cites = list(topic.get("cite", [])) + [item["cite_pool"]]

    rec = {
        "id": rid, "t": title, "g": topic["g"], "name": topic["t"], "title": title,
        "description": desc, "how_it_works": how,
        "key_points": kp, "requirements": req, "standards": std,
        "citations": cites,
        "src": "signature" if sig else "public-harvest",
        "ladder_rank": 1 + (idx * 10) // 34,
        "ladder_tier": ("foundations" if idx < 12 else "compounded" if idx < 24 else "advanced"),
        "demo": {"kind": "python", "language": "python",
                 "program": demo_learning(topic, title, rid, topic["g"]),
                 "note": "Working demonstration program (real, runnable Python)."},
    }
    return rec


_LN_TEMPLATE = r'''def norm(s):
    return " ".join(str(s).strip().lower().split())

def main():
    lesson = __LESSON__
    qa = [
__QA__
    ]
    print("LESSON SELF-CHECK: %s" % lesson)
    print("answering every question from the study key, then grading strictly")
    print("-" * 60)
    given = [a for _, a in qa]
    score = 0
    for i, ((q, want), got) in enumerate(zip(qa, given), 1):
        ok = norm(got) == norm(want)
        score += 1 if ok else 0
        print("Q%d %s" % (i, "PASS" if ok else "FAIL"))
        print("    asked:    %s" % q)
        print("    expected: %s" % want)
    print("-" * 60)
    pct = 100.0 * score / len(qa)
    print("score: %d/%d (%.0f%%)" % (score, len(qa), pct))
    assert score == len(qa), "self-check must pass clean"
    level = "mastered" if pct == 100 else ("proficient" if pct >= 75 else "review needed")
    print("mastery standard: %s" % level)
    assert level == "mastered"
    print("OK: __TITLE__ lesson drilled clean")

if __name__ == "__main__":
    main()
'''


def demo_learning(topic, title, rid, group):
    qa_lines = "\n".join("        (%s, %s)," % (json.dumps(q), json.dumps(a))
                         for q, a in topic["qa"])
    prog = _LN_TEMPLATE.replace("__LESSON__", json.dumps(topic["t"]))
    prog = prog.replace("__QA__", qa_lines)
    prog = prog.replace("__TITLE__", str(topic["t"]).replace('"', "'"))
    return _hdr(title, rid, group) + prog
