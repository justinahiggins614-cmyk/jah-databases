#!/usr/bin/env python3
"""JAH-OLY-000014 — AI version of JAH-OLY-000014 (JAH-OLY-000014).
No arguments: runs the thing's demo program. With a question:
answers as the thing, from its own numbers, using the same Q&A
logic as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/olympics/records/JAH-OLY-000014.html. Run: python3 <file>  OR  python3 <file> "question"
Free forever. Part of The 'Merica-L Internet."""
import json, re, sys
KB = json.loads('{"current": {"id": "JAH-OLY-000014", "title": "JAH-OLY-000014", "family": "bout", "desc": "Debug a Python function that silently returns the wrong total", "spec": {"mechanism": "Debug a Python function that silently returns the wrong total"}, "key_figures": {"margin": 27.7, "totals.JAH-AI-DOM-091": 210.6, "totals.JAH-MIX-000069": 182.89999999999998}, "url": "JAH-OLY-000014.html"}, "records": [{"id": "JAH-OLY-000001", "title": "JAH-OLY-000001", "family": "bout", "desc": "Write the opening paragraph of a cookbook from the year 2150", "spec": {"mechanism": "Write the opening paragraph of a cookbook from the year 2150"}, "key_figures": {"margin": 11.4, "totals.JAH-AI-DOM-026": 229.9, "totals.JAH-AI-DOM-065": 218.5}, "url": "JAH-OLY-000001.html"}, {"id": "JAH-OLY-000002", "title": "JAH-OLY-000002", "family": "bout", "desc": "Explain compound interest with a garden metaphor", "spec": {"mechanism": "Explain compound interest with a garden metaphor"}, "key_figures": {"margin": 20.1, "totals.JAH-AI-DOM-109": 152.6, "totals.JAH-MIX-000115": 172.7}, "url": "JAH-OLY-000002.html"}, {"id": "JAH-OLY-000003", "title": "JAH-OLY-000003", "family": "bout", "desc": "Plan a 3-day trip through an imaginary coastal city on a budget", "spec": {"mechanism": "Plan a 3-day trip through an imaginary coastal city on a budget"}, "key_figures": {"margin": 7.4, "totals.JAH-AI-DOM-106": 193.50000000000003, "totals.JAH-MIX-000096": 186.10000000000002}, "url": "JAH-OLY-000003.html"}, {"id": "JAH-OLY-000004", "title": "JAH-OLY-000004", "family": "bout", "desc": "Draft a town proclamation banning frowning on Fridays", "spec": {"mechanism": "Draft a town proclamation banning frowning on Fridays"}, "key_figures": {"margin": 22.5, "totals.JAH-AI-DOM-028": 190.6, "totals.JAH-AI-DOM-051": 213.1}, "url": "JAH-OLY-000004.html"}, {"id": "JAH-OLY-000005", "title": "JAH-OLY-000005", "family": "bout", "desc": "Summarize your own strengths and one weakness, honestly", "spec": {"mechanism": "Summarize your own strengths and one weakness, honestly"}, "key_figures": {"margin": 17.2, "totals.JAH-AI-DOM-171": 186.5, "totals.JAH-AI-SIG-009": 203.70000000000002}, "url": "JAH-OLY-000005.html"}, {"id": "JAH-OLY-000006", "title": "JAH-OLY-000006", "family": "bout", "desc": "Explain why the sky is blue using only food metaphors", "spec": {"mechanism": "Explain why the sky is blue using only food metaphors"}, "key_figures": {"margin": 67.1, "totals.JAH-MIX-000047": 162.2, "totals.JAH-MIX-000091": 229.29999999999998}, "url": "JAH-OLY-000006.html"}, {"id": "JAH-OLY-000007", "title": "JAH-OLY-000007", "family": "bout", "desc": "Write a weather report for a planet with two suns", "spec": {"mechanism": "Write a weather report for a planet with two suns"}, "key_figures": {"margin": 28.7, "totals.JAH-AI-DOM-184": 204.1, "totals.JAH-MIX-000025": 175.4}, "url": "JAH-OLY-000007.html"}, {"id": "JAH-OLY-000008", "title": "JAH-OLY-000008", "family": "bout", "desc": "BATTLE JAH-OLY-000008 — THE MIDNIGHT BAZAAR\\n\\nLantern-lit stalls of half-finished thoughts; haggle for the best reasoning.\\n\\nTonight the dome hosts Home Repair Guide (domain) against Knot Teacher x Neighbor Note Writer (hybrid). Judging: The Sprinter\'s Rubric. The mission: \\"Describe a color that does not exist.\\" Three rounds. No mercy.\\n\\nROUND 1: Home Repair Guide ripples a precision strike of clarit", "spec": {"mechanism": "BATTLE JAH-OLY-000008 — THE MIDNIGHT BAZAAR\\n\\nLantern-lit stalls of half-finished thoughts; haggle for the best reasoning.\\n\\nTonight the dome hosts Home Repair Guide (domain) against Knot Teacher x Neighbor Note Writer (hybrid). Judging: The Sprinter\'s Rubric. The mission: \\"Describe a color that does not exist.\\" Three rounds. No mercy.\\n\\nROUND 1: Home Repair Guide ripples a precision strike of clarity (64.7 pts). Knot Teacher x Neighbor Note Writer detonates a precision strike of clarity (57.3 pts). Round to Home Repair Guide.\\n\\nROUND 2: Home Repair Guide detonates a shield-wall of facts (70.5 pts"}, "key_figures": {"margin": 33.2, "totals.JAH-AI-DOM-018": 203.2, "totals.JAH-MIX-000069": 170}, "url": "JAH-OLY-000008.html"}, {"id": "JAH-OLY-000009", "title": "JAH-OLY-000009", "family": "bout", "desc": "Draft a town proclamation banning frowning on Fridays", "spec": {"mechanism": "Draft a town proclamation banning frowning on Fridays"}, "key_figures": {"margin": 2.5, "totals.JAH-AI-DOM-050": 201.1, "totals.JAH-AI-DOM-183": 203.60000000000002}, "url": "JAH-OLY-000009.html"}, {"id": "JAH-OLY-000010", "title": "JAH-OLY-000010", "family": "bout", "desc": "Teach long division using a story about pirates", "spec": {"mechanism": "Teach long division using a story about pirates"}, "key_figures": {"margin": 10.7, "totals.JAH-AI-DOM-021": 202.5, "totals.JAH-AI-DOM-232": 191.8}, "url": "JAH-OLY-000010.html"}, {"id": "JAH-OLY-000011", "title": "JAH-OLY-000011", "family": "bout", "desc": "Explain why the sky is blue using only food metaphors", "spec": {"mechanism": "Explain why the sky is blue using only food metaphors"}, "key_figures": {"margin": 0.8, "totals.JAH-AI-DOM-030": 205.1, "totals.JAH-MIX-000072": 205.89999999999998}, "url": "JAH-OLY-000011.html"}, {"id": "JAH-OLY-000012", "title": "JAH-OLY-000012", "family": "bout", "desc": "Write a four-line poem about a thunderstorm over the ocean", "spec": {"mechanism": "Write a four-line poem about a thunderstorm over the ocean"}, "key_figures": {"margin": 63.6, "totals.JAH-AI-DOM-031": 255.2, "totals.JAH-MIX-000087": 191.6}, "url": "JAH-OLY-000012.html"}, {"id": "JAH-OLY-000013", "title": "JAH-OLY-000013", "family": "bout", "desc": "Draft a town proclamation banning frowning on Fridays", "spec": {"mechanism": "Draft a town proclamation banning frowning on Fridays"}, "key_figures": {"margin": 68.7, "totals.JAH-AI-DOM-026": 241.9, "totals.JAH-AI-DOM-071": 173.20000000000002}, "url": "JAH-OLY-000013.html"}, {"id": "JAH-OLY-000014", "title": "JAH-OLY-000014", "family": "bout", "desc": "Debug a Python function that silently returns the wrong total", "spec": {"mechanism": "Debug a Python function that silently returns the wrong total"}, "key_figures": {"margin": 27.7, "totals.JAH-AI-DOM-091": 210.6, "totals.JAH-MIX-000069": 182.89999999999998}, "url": "JAH-OLY-000014.html"}, {"id": "JAH-OLY-000015", "title": "JAH-OLY-000015", "family": "bout", "desc": "Summarize your own strengths and one weakness, honestly", "spec": {"mechanism": "Summarize your own strengths and one weakness, honestly"}, "key_figures": {"margin": 11.3, "totals.JAH-AI-DOM-045": 202.6, "totals.JAH-AI-DOM-103": 213.9}, "url": "JAH-OLY-000015.html"}, {"id": "JAH-OLY-000016", "title": "JAH-OLY-000016", "family": "bout", "desc": "Write a dialogue between a clock and a calendar", "spec": {"mechanism": "Write a dialogue between a clock and a calendar"}, "key_figures": {"margin": 10.2, "totals.JAH-AI-DOM-134": 179.1, "totals.JAH-MIX-000090": 189.29999999999998}, "url": "JAH-OLY-000016.html"}, {"id": "JAH-OLY-000017", "title": "JAH-OLY-000017", "family": "bout", "desc": "Summarize the plot of an unwritten mystery novel in 5 sentences", "spec": {"mechanism": "Summarize the plot of an unwritten mystery novel in 5 sentences"}, "key_figures": {"margin": 2.8, "totals.JAH-AI-DOM-226": 213.70000000000002, "totals.JAH-AI-SIG-004": 210.89999999999998}, "url": "JAH-OLY-000017.html"}, {"id": "JAH-OLY-000018", "title": "JAH-OLY-000018", "family": "bout", "desc": "Pitch a movie about a lighthouse keeper who discovers a signal", "spec": {"mechanism": "Pitch a movie about a lighthouse keeper who discovers a signal"}, "key_figures": {"margin": 27.5, "totals.JAH-AI-DOM-178": 171.9, "totals.JAH-MIX-000059": 199.4}, "url": "JAH-OLY-000018.html"}, {"id": "JAH-OLY-000019", "title": "JAH-OLY-000019", "family": "bout", "desc": "Write instructions for folding a paper crane for a beginner", "spec": {"mechanism": "Write instructions for folding a paper crane for a beginner"}, "key_figures": {"margin": 36.8, "totals.JAH-AI-DOM-048": 184.2, "totals.JAH-AI-DOM-054": 221}, "url": "JAH-OLY-000019.html"}, {"id": "JAH-OLY-000020", "title": "JAH-OLY-000020", "family": "bout", "desc": "Write instructions for folding a paper crane for a beginner", "spec": {"mechanism": "Write instructions for folding a paper crane for a beginner"}, "key_figures": {"margin": 1.9, "totals.JAH-AI-DOM-205": 202.7, "totals.JAH-AI-DOM-214": 200.8}, "url": "JAH-OLY-000020.html"}, {"id": "JAH-OLY-000021", "title": "JAH-OLY-000021", "family": "bout", "desc": "Argue why breakfast is the most strategic meal of the day", "spec": {"mechanism": "Argue why breakfast is the most strategic meal of the day"}, "key_figures": {"margin": 56.4, "totals.JAH-MIX-000025": 160.3, "totals.JAH-MIX-000043": 216.7}, "url": "JAH-OLY-000021.html"}, {"id": "JAH-OLY-000022", "title": "JAH-OLY-000022", "family": "bout", "desc": "Write the opening paragraph of a cookbook from the year 2150", "spec": {"mechanism": "Write the opening paragraph of a cookbook from the year 2150"}, "key_figures": {"margin": 45.5, "totals.JAH-AI-DOM-122": 208.7, "totals.JAH-MIX-000087": 163.2}, "url": "JAH-OLY-000022.html"}, {"id": "JAH-OLY-000023", "title": "JAH-OLY-000023", "family": "bout", "desc": "BATTLE JAH-OLY-000023 — THE SILENT DOJO\\n\\nNo crowd, no noise — only the slap of a perfect argument landing.\\n\\nTonight the dome hosts School Lunch Rotator (domain) against Song Lyric Starter (domain). Judging: The Scholar\'s Rubric. The mission: \\"Write a haiku about debugging at 3am.\\" Three rounds. No mercy.\\n\\nROUND 1: School Lunch Rotator steadies a cascade of examples (61.2 pts). Song Lyric Starter r", "spec": {"mechanism": "BATTLE JAH-OLY-000023 — THE SILENT DOJO\\n\\nNo crowd, no noise — only the slap of a perfect argument landing.\\n\\nTonight the dome hosts School Lunch Rotator (domain) against Song Lyric Starter (domain). Judging: The Scholar\'s Rubric. The mission: \\"Write a haiku about debugging at 3am.\\" Three rounds. No mercy.\\n\\nROUND 1: School Lunch Rotator steadies a cascade of examples (61.2 pts). Song Lyric Starter ripples a shield-wall of facts (67.4 pts). Round to Song Lyric Starter.\\n\\nROUND 2: School Lunch Rotator presses the attack a feint of pure logic (66.1 pts). Song Lyric Starter weaves a gambit of wit (62"}, "key_figures": {"margin": 3.8, "totals.JAH-AI-DOM-173": 193.5, "totals.JAH-AI-DOM-235": 189.7}, "url": "JAH-OLY-000023.html"}, {"id": "JAH-OLY-000024", "title": "JAH-OLY-000024", "family": "bout", "desc": "Pitch a movie about a lighthouse keeper who discovers a signal", "spec": {"mechanism": "Pitch a movie about a lighthouse keeper who discovers a signal"}, "key_figures": {"margin": 0.1, "totals.JAH-AI-DOM-112": 207.3, "totals.JAH-AI-DOM-153": 207.2}, "url": "JAH-OLY-000024.html"}], "twin": {"id": "olympics-signature", "title": "AI Olympics Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-BOUT-GEN-"}')
DEMO_CODE = '"""Numeric check — JAH-OLY-000014 (JAH-OLY-000014).\nMade for this page from the record\'s own numbers.\nThis program checks the arithmetic of the stored figures; its outputs\nare check-sums, not physical quantities."""\nimport hashlib\ndef compute():\n    margin = 27.699999999999999; totals_jah_mix_000069 = 182.899999999999977; totals_jah_ai_dom_091 = 210.599999999999994\n    total = round(margin + totals_jah_mix_000069 + totals_jah_ai_dom_091, 2)\n    mean = round(total / 3, 2)\n    first_plus_second = round(margin + totals_jah_mix_000069, 2)\n    first_minus_second = round(margin - totals_jah_mix_000069, 2)\n    first_times_second = round(margin * totals_jah_mix_000069, 2)\n    return {"total": total, "mean": mean, "first_plus_second": first_plus_second, "first_minus_second": first_minus_second, "first_times_second": first_times_second}\ndef main():\n    a = compute(); b = compute()\n    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()\n    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()\n    for key in ["total", "mean", "first_plus_second", "first_minus_second", "first_times_second"]:\n        print(f"{key}: {a[key]}")\n    print(f"Run 1 SHA-256: {sa}")\n    print(f"Run 2 SHA-256: {sb}")\n    print(f"Deterministic: {\'MATCH\' if sa == sb else \'MISMATCH\'}")\nif __name__ == "__main__":\n    main()\n'

def _norm(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()
def _toks(s):
    return [w for w in _norm(s).split(" ") if len(w) > 1]
_STOPWORDS = set("what is the of a an and or to in on for how does do did can could would should it its this that there here me my you your please tell about show give get with by from at as be are was were has have had i we they he she who whom whose which when where why not no yes if then than so such any some all each every other another more most many much few little own same too very just also only even still already now".split())
def _score_rec(q, rec):
    hay = _norm(" ".join(str(rec.get(k) or "") for k in ("title", "family", "desc", "spec")))
    qt = [w for w in _toks(q) if w not in _STOPWORDS]
    ht = _toks(hay)
    sc = 0
    for w in qt:
        if w in ht:
            sc += 2
        elif w in hay:
            sc += 1
    return sc
def _answer_question(q, kb):
    nq = _norm(q)
    if not nq:
        return "Ask me something about this page \u2014 a record, a number, a material, a step."
    if kb.get("legal") and re.search(r"\blegal\b|\blaw\b|\bjurisdiction\b", nq):
        return kb["legal"]
    if re.search(r"\bdownload\b", nq):
        return "Every download on this page is a real file: the full record, the demo program, the full program, the spec sheet, the complete file, and both downloadable AIs with their spec sheets. See section 8, Use, download, copy \u2014 all free forever."
    if re.search(r"\bcopy\b", nq):
        return "Use the Copy-all button in section 8. It copies the full record text, including the demo code, with its sources attached."
    if re.search(r"\bread aloud\b|\bread this\b|\blisten\b", nq):
        return "Press the Read aloud button at the top of the page. It reads the whole page aloud and stops when you press Stop reading."
    if re.search(r"\bgenerat|\bscale\b|\bbigger\b|\bsmaller\b|\bvariant\b", nq):
        return "Use the boundless generator in section 8: pick a seed (1 to 999,999,999) or a pocket / standard / workshop scale and press Generate. The generator ceiling is 1,000,000,000 scales per file."
    if re.search(r"\bsources?\b|\bcitation\b|\bwhere.*from\b", nq):
        srcs = kb.get("sources") or []
        if srcs:
            parts = []
            for s in srcs:
                if s.get("text"):
                    parts.append("%s: %s" % (s.get("title", ""), s["text"][:300]))
                else:
                    parts.append("%s \u2014 %s" % (s.get("title", ""), s.get("url", "")))
            return "Sources for this record: " + "; ".join(parts) + "."
        return "This record carries no external source list in the archive. Its provenance is the archive itself, stated on the page."
    if re.search(r"\btwin\b|\bsignature\b|\bpublic version\b", nq):
        tw = kb.get("twin")
        if tw:
            return "The twin edition is %s (%s). Open it here: %s" % (tw.get("title", ""), tw.get("id", ""), tw.get("url", ""))
        return "This page has no twin edition."
    recs = kb.get("records") or ([kb["current"]] if kb.get("current") else [])
    best = None
    best_sc = 0
    for r in recs:
        s = _score_rec(q, r)
        if s > best_sc:
            best_sc = s
            best = r
    explicit = bool(re.search(r"\bthis\b|\bit\b|\bthe (record|thing|item|entry|database|archive|mix|program|file|option|supply)\b", nq))
    target = best
    if not target and kb.get("current") and explicit:
        target = kb["current"]
    if target and (best_sc > 0 or explicit):
        spec = target.get("spec") or {}
        if not isinstance(spec, dict):
            spec = {}
        if re.search(r"\bdimension|\bsize\b|\bhow big|\bhow tall|\bhow wide|\bdiameter\b", nq) and spec.get("dimensions"):
            return "%s \u2014 dimensions: %s" % (target.get("title", ""), spec["dimensions"])
        if re.search(r"\bmaterial|\bmade of|\bmade from\b", nq) and spec.get("materials"):
            return "%s \u2014 materials: %s" % (target.get("title", ""), spec["materials"])
        if re.search(r"\bmechanism|\bhow.*work|\bhow does\b", nq) and spec.get("mechanism"):
            return "%s \u2014 mechanism: %s" % (target.get("title", ""), spec["mechanism"])
        if re.search(r"\buse\b|\bhow.*use\b|\bhow to use\b", nq) and spec.get("use"):
            return "%s \u2014 use: %s" % (target.get("title", ""), spec["use"])
        if re.search(r"\bcare\b|\bclean\b", nq) and spec.get("care"):
            return "%s \u2014 care: %s" % (target.get("title", ""), spec["care"])
        if re.search(r"\bvariant|\bversion\b", nq) and spec.get("variants"):
            return "%s \u2014 variants: %s" % (target.get("title", ""), spec["variants"])
        if re.search(r"\bdemo\b|\bprogram\b|\bcalculat|\bcompute\b", nq):
            return "The demo for %s is in section 6. Run it from the download, or use the live calculator on this page \u2014 it runs the record\u2019s own numbers in your browser and matches the record\u2019s official output exactly at the record\u2019s own inputs." % target.get("title", "")
        if re.search(r"\bwhat is\b|\bwhat.*(this|that)\b|\btell me about\b", nq) or best_sc > 0:
            ans = "%s: %s" % (target.get("title", ""), target.get("desc", ""))
            if target.get("url"):
                ans += " Full record: " + target["url"]
            return ans
    if len(recs) > 1:
        return "I answer only from this page\u2019s own records. Try asking about a record by name, a material, a dimension, a mechanism, or a use \u2014 or ask for the full list."
    return "That goes outside what this page\u2019s records cover. I answer only from this page\u2019s own records and their cited sources, and I say so plainly when a question goes outside them."

if __name__ == "__main__":
    _args = sys.argv[1:]
    if not _args:
        _g = {"__name__": "__main__"}
        exec(DEMO_CODE, _g)
    else:
        print(_answer_question(" ".join(_args), KB))
