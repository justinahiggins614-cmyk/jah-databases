#!/usr/bin/env python3
"""Warm Bakery Garden — AI version of Warm Bakery Garden (JAH-TPL-0000021).
No arguments: runs the thing's demo program. With a question:
answers as the thing, from its own numbers, using the same Q&A
logic as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/websites/records/JAH-TPL-0000021.html. Run: python3 <file>  OR  python3 <file> "question"
Free forever. Part of The 'Merica-L Internet."""
import json, re, sys
KB = json.loads('{"current": {"id": "JAH-TPL-0000021", "title": "Warm Bakery Garden", "family": "Bakery & Food", "desc": "A soft pastel bakery & food website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#33122b; #ff8fb2", "mechanism": "A soft pastel bakery & food website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000021.html"}, "records": [{"id": "JAH-TPL-0000001", "title": "Cozy Bakery Studio", "family": "Bakery & Food", "desc": "A soft pastel bakery & food website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#16264a; #59d6ff", "mechanism": "A soft pastel bakery & food website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000001.html"}, {"id": "JAH-TPL-0000002", "title": "Cozy Portfolio Garden", "family": "Portfolio", "desc": "A sunny bright portfolio website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#4a2a10; #ffc46b", "mechanism": "A sunny bright portfolio website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000002.html"}, {"id": "JAH-TPL-0000003", "title": "Shiny Blog Garden", "family": "Blog & Writing", "desc": "A ocean fresh blog & writing website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#33122b; #ff8fb2", "mechanism": "A ocean fresh blog & writing website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000003.html"}, {"id": "JAH-TPL-0000004", "title": "Lucky Local Nest", "family": "Local Business", "desc": "A soft pastel local business website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#4a2a10; #ffc46b", "mechanism": "A soft pastel local business website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000004.html"}, {"id": "JAH-TPL-0000005", "title": "Zesty Online Works", "family": "Online Store", "desc": "A ocean fresh online store website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#2a1a08; #ffd166", "mechanism": "A ocean fresh online store website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000005.html"}, {"id": "JAH-TPL-0000006", "title": "Clever Restaurant Corner", "family": "Restaurant", "desc": "A bold modern restaurant website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#0e2a3a; #7ef0d4", "mechanism": "A bold modern restaurant website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000006.html"}, {"id": "JAH-TPL-0000007", "title": "Prime Photography House", "family": "Photography", "desc": "A bold modern photography website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#4a2a10; #ffc46b", "mechanism": "A bold modern photography website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000007.html"}, {"id": "JAH-TPL-0000008", "title": "Merry Music Works", "family": "Music & Band", "desc": "A royal gold music & band website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#16264a; #59d6ff", "mechanism": "A royal gold music & band website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000008.html"}, {"id": "JAH-TPL-0000009", "title": "Shiny Fitness Garden", "family": "Fitness & Health", "desc": "A earthy calm fitness & health website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#3a1b4a; #f0a6ff", "mechanism": "A earthy calm fitness & health website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000009.html"}, {"id": "JAH-TPL-0000010", "title": "Rapid Real Garden", "family": "Real Estate", "desc": "A earthy calm real estate website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#122a4a; #8fd0ff", "mechanism": "A earthy calm real estate website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000010.html"}, {"id": "JAH-TPL-0000011", "title": "Swift Salon Station", "family": "Salon & Beauty", "desc": "A ocean fresh salon & beauty website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#3a1b4a; #f0a6ff", "mechanism": "A ocean fresh salon & beauty website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000011.html"}, {"id": "JAH-TPL-0000012", "title": "Noble Auto Post", "family": "Auto & Repair", "desc": "A royal gold auto & repair website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#3a1b4a; #f0a6ff", "mechanism": "A royal gold auto & repair website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000012.html"}, {"id": "JAH-TPL-0000013", "title": "Merry Pet Garden", "family": "Pet Care", "desc": "A bold modern pet care website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#0f3a2e; #5ff2b8", "mechanism": "A bold modern pet care website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000013.html"}, {"id": "JAH-TPL-0000014", "title": "Golden Kids Harbor", "family": "Kids & Family", "desc": "A sunny bright kids & family website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#122a4a; #8fd0ff", "mechanism": "A sunny bright kids & family website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000014.html"}, {"id": "JAH-TPL-0000015", "title": "True Education Post", "family": "Education", "desc": "A earthy calm education website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#0f3a2e; #5ff2b8", "mechanism": "A earthy calm education website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000015.html"}, {"id": "JAH-TPL-0000016", "title": "Rapid Nonprofit Nest", "family": "Nonprofit", "desc": "A cozy classic nonprofit website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#0e2a3a; #7ef0d4", "mechanism": "A cozy classic nonprofit website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000016.html"}, {"id": "JAH-TPL-0000017", "title": "Warm Church Hub", "family": "Church & Faith", "desc": "A dark neon church & faith website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#122a4a; #8fd0ff", "mechanism": "A dark neon church & faith website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000017.html"}, {"id": "JAH-TPL-0000018", "title": "Happy Events Place", "family": "Events & Parties", "desc": "A bold modern events & parties website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#4a2a10; #ffc46b", "mechanism": "A bold modern events & parties website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000018.html"}, {"id": "JAH-TPL-0000019", "title": "Rapid Travel Post", "family": "Travel & Tours", "desc": "A earthy calm travel & tours website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#2a1a08; #ffd166", "mechanism": "A earthy calm travel & tours website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000019.html"}, {"id": "JAH-TPL-0000020", "title": "Happy Tech Shop", "family": "Tech & Apps", "desc": "A royal gold tech & apps website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#3a1b4a; #f0a6ff", "mechanism": "A royal gold tech & apps website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000020.html"}, {"id": "JAH-TPL-0000021", "title": "Warm Bakery Garden", "family": "Bakery & Food", "desc": "A soft pastel bakery & food website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#33122b; #ff8fb2", "mechanism": "A soft pastel bakery & food website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000021.html"}, {"id": "JAH-TPL-0000022", "title": "Zesty Portfolio Station", "family": "Portfolio", "desc": "A bold modern portfolio website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#3a1b4a; #f0a6ff", "mechanism": "A bold modern portfolio website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000022.html"}, {"id": "JAH-TPL-0000023", "title": "Noble Blog Post", "family": "Blog & Writing", "desc": "A earthy calm blog & writing website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#2a1a08; #ffd166", "mechanism": "A earthy calm blog & writing website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000023.html"}, {"id": "JAH-TPL-0000024", "title": "Vivid Local Studio", "family": "Local Business", "desc": "A sunny bright local business website template. Hero, intro, tab bar, archive and contact page included — ready to build.", "spec": {"materials": "#2a1a08; #ffd166", "mechanism": "A sunny bright local business website template. Hero, intro, tab bar, archive and contact page included — ready to build."}, "key_figures": {}, "url": "JAH-TPL-0000024.html"}], "twin": {"id": "websites-signature", "title": "Signature Website Creator Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-SITE-GEN-"}')
DEMO_CODE = '"""Numeric check — Warm Bakery Garden (JAH-TPL-0000021).\nMade for this page from text-derived counts (the record carries no usable numbers of its own).\nThis program checks the arithmetic of the stored figures; its outputs\nare check-sums, not physical quantities."""\nimport hashlib\ndef compute():\n    title_chars = 18; desc_chars = 119; source_count = 0; field_count = 8\n    total = round(title_chars + desc_chars + source_count + field_count, 2)\n    mean = round(total / 4, 2)\n    first_plus_second = round(title_chars + desc_chars, 2)\n    first_minus_second = round(title_chars - desc_chars, 2)\n    first_times_second = round(title_chars * desc_chars, 2)\n    return {"total": total, "mean": mean, "first_plus_second": first_plus_second, "first_minus_second": first_minus_second, "first_times_second": first_times_second}\ndef main():\n    a = compute(); b = compute()\n    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()\n    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()\n    for key in ["total", "mean", "first_plus_second", "first_minus_second", "first_times_second"]:\n        print(f"{key}: {a[key]}")\n    print(f"Run 1 SHA-256: {sa}")\n    print(f"Run 2 SHA-256: {sb}")\n    print(f"Deterministic: {\'MATCH\' if sa == sb else \'MISMATCH\'}")\nif __name__ == "__main__":\n    main()\n'

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
