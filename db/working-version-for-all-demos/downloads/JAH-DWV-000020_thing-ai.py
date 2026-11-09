#!/usr/bin/env python3
"""The Signature AI to Robot Matcher Database -- Working Version — AI version of The Signature AI to Robot Matcher Database -- Working Version (JAH-DWV-000020).
No arguments: runs the thing's demo program. With a question:
answers as the thing, from its own numbers, using the same Q&A
logic as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/working-version-for-all-demos/records/JAH-DWV-000020.html. Run: python3 <file>  OR  python3 <file> "question"
Free forever. Part of The 'Merica-L Internet."""
import json, re, sys
KB = json.loads('{"current": {"id": "JAH-DWV-000020", "title": "The Signature AI to Robot Matcher Database -- Working Version", "family": "working version link record", "desc": "The Signature AI to Robot Matcher Database -- Working Version", "spec": {"mechanism": "The Signature AI to Robot Matcher Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 37010}, "url": "JAH-DWV-000020.html"}, "records": [{"id": "JAH-DWV-000001", "title": "Signature Universal Paradox Immune Calculator Database -- Working Version", "family": "working version link record", "desc": "Signature Universal Paradox Immune Calculator Database -- Working Version", "spec": {"mechanism": "Signature Universal Paradox Immune Calculator Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 132300}, "url": "JAH-DWV-000001.html"}, {"id": "JAH-DWV-000002", "title": "Globally Rejustered Patent Catalog Database -- Working Version", "family": "working version link record", "desc": "Globally Rejustered Patent Catalog Database -- Working Version", "spec": {"mechanism": "Globally Rejustered Patent Catalog Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 77275}, "url": "JAH-DWV-000002.html"}, {"id": "JAH-DWV-000003", "title": "Signature Spec Catalog Pending Patents Database -- Working Version", "family": "working version link record", "desc": "Signature Spec Catalog Pending Patents Database -- Working Version", "spec": {"mechanism": "Signature Spec Catalog Pending Patents Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 908995}, "url": "JAH-DWV-000003.html"}, {"id": "JAH-DWV-000004", "title": "The Signature Dictionary Database -- Working Version", "family": "working version link record", "desc": "The Signature Dictionary Database -- Working Version", "spec": {"mechanism": "The Signature Dictionary Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 1127335}, "url": "JAH-DWV-000004.html"}, {"id": "JAH-DWV-000005", "title": "JAH Wiki Database -- Working Version", "family": "working version link record", "desc": "https://justinahiggins614-cmyk.github.io/jah-databases/db/wiki/#p-demo", "spec": {"mechanism": "https://justinahiggins614-cmyk.github.io/jah-databases/db/wiki/#p-demo"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 1470175}, "url": "JAH-DWV-000005.html"}, {"id": "JAH-DWV-000006", "title": "JAH-N Wiki Leaks Database -- Working Version", "family": "working version link record", "desc": "JAH-N Wiki Leaks Database -- Working Version", "spec": {"mechanism": "JAH-N Wiki Leaks Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 121020}, "url": "JAH-DWV-000006.html"}, {"id": "JAH-DWV-000007", "title": "The Signature AI Phone Book Database -- Working Version", "family": "working version link record", "desc": "The Signature AI Phone Book Database -- Working Version", "spec": {"mechanism": "The Signature AI Phone Book Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 444}, "url": "JAH-DWV-000007.html"}, {"id": "JAH-DWV-000008", "title": "Signature Llama Database -- Working Version", "family": "working version link record", "desc": "Signature Llama Database -- Working Version", "spec": {"mechanism": "Signature Llama Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 125}, "url": "JAH-DWV-000008.html"}, {"id": "JAH-DWV-000009", "title": "Signature Math Database -- Working Version", "family": "working version link record", "desc": "Signature Math Database -- Working Version", "spec": {"mechanism": "Signature Math Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 3858}, "url": "JAH-DWV-000009.html"}, {"id": "JAH-DWV-000010", "title": "The Signature PC System Depository Database -- Working Version", "family": "working version link record", "desc": "The Signature PC System Depository Database -- Working Version", "spec": {"mechanism": "The Signature PC System Depository Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 23044}, "url": "JAH-DWV-000010.html"}, {"id": "JAH-DWV-000011", "title": "The Signature Book Depository Database -- Working Version", "family": "working version link record", "desc": "The Signature Book Depository Database -- Working Version", "spec": {"mechanism": "The Signature Book Depository Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 48100}, "url": "JAH-DWV-000011.html"}, {"id": "JAH-DWV-000012", "title": "The Signature Comic Store Database -- Working Version", "family": "working version link record", "desc": "The Signature Comic Store Database -- Working Version", "spec": {"mechanism": "The Signature Comic Store Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 18549}, "url": "JAH-DWV-000012.html"}, {"id": "JAH-DWV-000013", "title": "The Signature Global Newspaper Archive Database -- Working Version", "family": "working version link record", "desc": "The Signature Global Newspaper Archive Database -- Working Version", "spec": {"mechanism": "The Signature Global Newspaper Archive Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 98}, "url": "JAH-DWV-000013.html"}, {"id": "JAH-DWV-000014", "title": "The Signature AI Mix and Match Generator Database -- Working Version", "family": "working version link record", "desc": "The Signature AI Mix and Match Generator Database -- Working Version", "spec": {"mechanism": "The Signature AI Mix and Match Generator Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 2497}, "url": "JAH-DWV-000014.html"}, {"id": "JAH-DWV-000015", "title": "The Signature Boundless Generator Archive Database -- Working Version", "family": "working version link record", "desc": "The Signature Boundless Generator Archive Database -- Working Version", "spec": {"mechanism": "The Signature Boundless Generator Archive Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 137025}, "url": "JAH-DWV-000015.html"}, {"id": "JAH-DWV-000016", "title": "The Signature AI Mix Lab Database -- Working Version", "family": "working version link record", "desc": "The Signature AI Mix Lab Database -- Working Version", "spec": {"mechanism": "The Signature AI Mix Lab Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 38000}, "url": "JAH-DWV-000016.html"}, {"id": "JAH-DWV-000017", "title": "AI Olympics Database -- Working Version", "family": "working version link record", "desc": "https://justinahiggins614-cmyk.github.io/jah-databases/db/olympics/#p-gen", "spec": {"mechanism": "https://justinahiggins614-cmyk.github.io/jah-databases/db/olympics/#p-gen"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 38063}, "url": "JAH-DWV-000017.html"}, {"id": "JAH-DWV-000018", "title": "The Signature Computer Chip Maker and Archive Database -- Working Version", "family": "working version link record", "desc": "The Signature Computer Chip Maker and Archive Database -- Working Version", "spec": {"mechanism": "The Signature Computer Chip Maker and Archive Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 35601}, "url": "JAH-DWV-000018.html"}, {"id": "JAH-DWV-000019", "title": "The Signature App Archive Database -- Working Version", "family": "working version link record", "desc": "The Signature App Archive Database -- Working Version", "spec": {"mechanism": "The Signature App Archive Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 86194}, "url": "JAH-DWV-000019.html"}, {"id": "JAH-DWV-000020", "title": "The Signature AI to Robot Matcher Database -- Working Version", "family": "working version link record", "desc": "The Signature AI to Robot Matcher Database -- Working Version", "spec": {"mechanism": "The Signature AI to Robot Matcher Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 37010}, "url": "JAH-DWV-000020.html"}, {"id": "JAH-DWV-000021", "title": "The Signature Experiment Solver Database -- Working Version", "family": "working version link record", "desc": "The Signature Experiment Solver Database -- Working Version", "spec": {"mechanism": "The Signature Experiment Solver Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 35925}, "url": "JAH-DWV-000021.html"}, {"id": "JAH-DWV-000022", "title": "Signature AI Pixel Database -- Working Version", "family": "working version link record", "desc": "Signature AI Pixel Database -- Working Version", "spec": {"mechanism": "Signature AI Pixel Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 87000}, "url": "JAH-DWV-000022.html"}, {"id": "JAH-DWV-000023", "title": "Signature Music Studio Database -- Working Version", "family": "working version link record", "desc": "Signature Music Studio Database -- Working Version", "spec": {"mechanism": "Signature Music Studio Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 108050}, "url": "JAH-DWV-000023.html"}, {"id": "JAH-DWV-000024", "title": "The Signature Mr Fix-It Database -- Working Version", "family": "working version link record", "desc": "The Signature Mr Fix-It Database -- Working Version", "spec": {"mechanism": "The Signature Mr Fix-It Database -- Working Version"}, "key_figures": {"generator.cap_records": 1000000000000000, "target_record_count": 178}, "url": "JAH-DWV-000024.html"}], "twin": {"id": "working-version-for-all-demos-signature", "title": "The Working Version for All Demos Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-DWV-GEN-"}')
DEMO_CODE = '"""Numeric check — The Signature AI to Robot Matcher Database -- Working Version (JAH-DWV-000020).\nMade for this page from text-derived counts (the record carries no usable numbers of its own).\nThis program checks the arithmetic of the stored figures; its outputs\nare check-sums, not physical quantities."""\nimport hashlib\ndef compute():\n    title_chars = 61; desc_chars = 61; source_count = 0; field_count = 19\n    total = round(title_chars + desc_chars + source_count + field_count, 2)\n    mean = round(total / 4, 2)\n    first_plus_second = round(title_chars + desc_chars, 2)\n    first_minus_second = round(title_chars - desc_chars, 2)\n    first_times_second = round(title_chars * desc_chars, 2)\n    return {"total": total, "mean": mean, "first_plus_second": first_plus_second, "first_minus_second": first_minus_second, "first_times_second": first_times_second}\ndef main():\n    a = compute(); b = compute()\n    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()\n    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()\n    for key in ["total", "mean", "first_plus_second", "first_minus_second", "first_times_second"]:\n        print(f"{key}: {a[key]}")\n    print(f"Run 1 SHA-256: {sa}")\n    print(f"Run 2 SHA-256: {sb}")\n    print(f"Deterministic: {\'MATCH\' if sa == sb else \'MISMATCH\'}")\nif __name__ == "__main__":\n    main()\n'

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
