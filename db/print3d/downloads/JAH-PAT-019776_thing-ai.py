#!/usr/bin/env python3
""""cabbage rolls filled with mussels" preserves production method — AI version of "cabbage rolls filled with mussels" preserves production method (JAH-PAT-019776).
No arguments: runs the thing's demo program. With a question:
answers as the thing, from its own numbers, using the same Q&A
logic as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/print3d/records/JAH-PAT-019776.html. Run: python3 <file>  OR  python3 <file> "question"
Free forever. Part of The 'Merica-L Internet."""
import json, re, sys
KB = json.loads('{"current": {"id": "JAH-PAT-019776", "title": "\\"cabbage rolls filled with mussels\\" preserves production method", "family": "3D model", "desc": "\\"cabbage rolls filled with mussels\\" preserves production method", "spec": {"mechanism": "\\"cabbage rolls filled with mussels\\" preserves production method"}, "key_figures": {}, "url": "JAH-PAT-019776.html"}, "records": [{"id": "JAH-PAT-000343", "title": "\\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids", "family": "3D model", "desc": "\\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids", "spec": {"mechanism": "\\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids"}, "key_figures": {}, "url": "JAH-PAT-000343.html"}, {"id": "JAH-PAT-050265", "title": "\\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids", "family": "3D model", "desc": "\\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids", "spec": {"mechanism": "\\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids"}, "key_figures": {}, "url": "JAH-PAT-050265.html"}, {"id": "JAH-PAT-054478", "title": "\\"ADJUSTMENT DEVICE FOR THE INCLINE OF A FRONT FORK OF A TWO OR THREE-WHEEL …", "family": "3D model", "desc": "\\"ADJUSTMENT DEVICE FOR THE INCLINE OF A FRONT FORK OF A TWO OR THREE-WHEEL …", "spec": {"mechanism": "\\"ADJUSTMENT DEVICE FOR THE INCLINE OF A FRONT FORK OF A TWO OR THREE-WHEEL …"}, "key_figures": {}, "url": "JAH-PAT-054478.html"}, {"id": "JAH-PAT-008520", "title": "\\"AEROBIC HARDENING PLASTICS\\"", "family": "3D model", "desc": "\\"AEROBIC HARDENING PLASTICS\\"", "spec": {"mechanism": "\\"AEROBIC HARDENING PLASTICS\\""}, "key_figures": {}, "url": "JAH-PAT-008520.html"}, {"id": "JAH-PAT-039322", "title": "\\"BLOOD PRESSURE MEASURING DEVICE\\"", "family": "3D model", "desc": "\\"BLOOD PRESSURE MEASURING DEVICE\\"", "spec": {"mechanism": "\\"BLOOD PRESSURE MEASURING DEVICE\\""}, "key_figures": {}, "url": "JAH-PAT-039322.html"}, {"id": "JAH-PAT-019776", "title": "\\"cabbage rolls filled with mussels\\" preserves production method", "family": "3D model", "desc": "\\"cabbage rolls filled with mussels\\" preserves production method", "spec": {"mechanism": "\\"cabbage rolls filled with mussels\\" preserves production method"}, "key_figures": {}, "url": "JAH-PAT-019776.html"}, {"id": "JAH-PAT-010726", "title": "\\"CHOCOLATE AROMA EXTRACT\\".", "family": "3D model", "desc": "\\"CHOCOLATE AROMA EXTRACT\\".", "spec": {"mechanism": "\\"CHOCOLATE AROMA EXTRACT\\"."}, "key_figures": {}, "url": "JAH-PAT-010726.html"}, {"id": "JAH-PAT-050629", "title": "\\"CLUTCH FOR A POWER TOOL\\"", "family": "3D model", "desc": "\\"CLUTCH FOR A POWER TOOL\\"", "spec": {"mechanism": "\\"CLUTCH FOR A POWER TOOL\\""}, "key_figures": {}, "url": "JAH-PAT-050629.html"}, {"id": "JAH-PAT-008479", "title": "\\"COLOR PHOTOGRAPHIC SILVER HALOGENIDE MATERIAL\\"", "family": "3D model", "desc": "\\"COLOR PHOTOGRAPHIC SILVER HALOGENIDE MATERIAL\\"", "spec": {"mechanism": "\\"COLOR PHOTOGRAPHIC SILVER HALOGENIDE MATERIAL\\""}, "key_figures": {}, "url": "JAH-PAT-008479.html"}, {"id": "JAH-PAT-054684", "title": "\\"conjunto para prender tecido ou um elemento protético em uma abertura …", "family": "3D model", "desc": "\\"conjunto para prender tecido ou um elemento protético em uma abertura …", "spec": {"mechanism": "\\"conjunto para prender tecido ou um elemento protético em uma abertura …"}, "key_figures": {}, "url": "JAH-PAT-054684.html"}, {"id": "JAH-PAT-059136", "title": "\\"CYLINDER CHANGE DEVICE FOR HIGH CYLINDER SEWING MACHINES\\"", "family": "3D model", "desc": "\\"CYLINDER CHANGE DEVICE FOR HIGH CYLINDER SEWING MACHINES\\"", "spec": {"mechanism": "\\"CYLINDER CHANGE DEVICE FOR HIGH CYLINDER SEWING MACHINES\\""}, "key_figures": {}, "url": "JAH-PAT-059136.html"}, {"id": "JAH-PAT-033255", "title": "\\"dezbel\\" disinfecting and bleaching agent", "family": "3D model", "desc": "\\"dezbel\\" disinfecting and bleaching agent", "spec": {"mechanism": "\\"dezbel\\" disinfecting and bleaching agent"}, "key_figures": {}, "url": "JAH-PAT-033255.html"}, {"id": "JAH-PAT-058094", "title": "\\"ECLIPSE\\" PORTABLE OBJECTS TROUSSE", "family": "3D model", "desc": "\\"ECLIPSE\\" PORTABLE OBJECTS TROUSSE", "spec": {"mechanism": "\\"ECLIPSE\\" PORTABLE OBJECTS TROUSSE"}, "key_figures": {}, "url": "JAH-PAT-058094.html"}, {"id": "JAH-PAT-039309", "title": "\\"ELECTRICAL CONNECTION OF SEMICONDUCTOR CABLES\\"", "family": "3D model", "desc": "\\"ELECTRICAL CONNECTION OF SEMICONDUCTOR CABLES\\"", "spec": {"mechanism": "\\"ELECTRICAL CONNECTION OF SEMICONDUCTOR CABLES\\""}, "key_figures": {}, "url": "JAH-PAT-039309.html"}, {"id": "JAH-PAT-039320", "title": "\\"ELECTRONIC TRANSLATION DEVICE\\"", "family": "3D model", "desc": "\\"ELECTRONIC TRANSLATION DEVICE\\"", "spec": {"mechanism": "\\"ELECTRONIC TRANSLATION DEVICE\\""}, "key_figures": {}, "url": "JAH-PAT-039320.html"}, {"id": "JAH-PAT-019786", "title": "\\"elite\\" fish roll production method", "family": "3D model", "desc": "\\"elite\\" fish roll production method", "spec": {"mechanism": "\\"elite\\" fish roll production method"}, "key_figures": {}, "url": "JAH-PAT-019786.html"}, {"id": "JAH-PAT-008518", "title": "\\"Grosse rote Fleischtomate\\", and \\"Weiterzüchtung 1981\\" bred from it", "family": "3D model", "desc": "\\"Grosse rote Fleischtomate\\", and \\"Weiterzüchtung 1981\\" bred from it", "spec": {"mechanism": "\\"Grosse rote Fleischtomate\\", and \\"Weiterzüchtung 1981\\" bred from it"}, "key_figures": {}, "url": "JAH-PAT-008518.html"}, {"id": "JAH-PAT-019293", "title": "\\"imperial\\"-brand vodka", "family": "3D model", "desc": "\\"imperial\\"-brand vodka", "spec": {"mechanism": "\\"imperial\\"-brand vodka"}, "key_figures": {}, "url": "JAH-PAT-019293.html"}, {"id": "JAH-PAT-008475", "title": "\\"INORGANIC FOAM PRODUCT\\"", "family": "3D model", "desc": "\\"INORGANIC FOAM PRODUCT\\"", "spec": {"mechanism": "\\"INORGANIC FOAM PRODUCT\\""}, "key_figures": {}, "url": "JAH-PAT-008475.html"}, {"id": "JAH-PAT-000451", "title": "\\"isoquinoline derivatives\\"", "family": "3D model", "desc": "\\"isoquinoline derivatives\\"", "spec": {"mechanism": "\\"isoquinoline derivatives\\""}, "key_figures": {}, "url": "JAH-PAT-000451.html"}, {"id": "JAH-PAT-028232", "title": "\\"Macro\\" Photographic lens having long focal length and vibration compensation", "family": "3D model", "desc": "\\"Macro\\" Photographic lens having long focal length and vibration compensation", "spec": {"mechanism": "\\"Macro\\" Photographic lens having long focal length and vibration compensation"}, "key_figures": {}, "url": "JAH-PAT-028232.html"}, {"id": "JAH-PAT-008473", "title": "\\"METHOD FOR PRODUCING A BLUE-GREEN DYE IMAGE\\"", "family": "3D model", "desc": "\\"METHOD FOR PRODUCING A BLUE-GREEN DYE IMAGE\\"", "spec": {"mechanism": "\\"METHOD FOR PRODUCING A BLUE-GREEN DYE IMAGE\\""}, "key_figures": {}, "url": "JAH-PAT-008473.html"}, {"id": "JAH-PAT-008468", "title": "\\"METHOD FOR PRODUCING POLYURETHANE ELASTOMERS\\"", "family": "3D model", "desc": "\\"METHOD FOR PRODUCING POLYURETHANE ELASTOMERS\\"", "spec": {"mechanism": "\\"METHOD FOR PRODUCING POLYURETHANE ELASTOMERS\\""}, "key_figures": {}, "url": "JAH-PAT-008468.html"}, {"id": "JAH-PAT-051144", "title": "\\"MODULATOR-DEMODULATOR FOR A SET OF DATA PACKET CARRIERS\\".", "family": "3D model", "desc": "\\"MODULATOR-DEMODULATOR FOR A SET OF DATA PACKET CARRIERS\\".", "spec": {"mechanism": "\\"MODULATOR-DEMODULATOR FOR A SET OF DATA PACKET CARRIERS\\"."}, "key_figures": {}, "url": "JAH-PAT-051144.html"}], "twin": {"id": "print3d-signature", "title": "The Signature 3D Print Mega Mall Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-3D-GEN-"}')
DEMO_CODE = '"""Numeric check — "cabbage rolls filled with mussels" preserves production method (JAH-PAT-019776).\nMade for this page from text-derived counts (the record carries no usable numbers of its own).\nThis program checks the arithmetic of the stored figures; its outputs\nare check-sums, not physical quantities."""\nimport hashlib\ndef compute():\n    title_chars = 63; desc_chars = 63; source_count = 0; field_count = 2\n    total = round(title_chars + desc_chars + source_count + field_count, 2)\n    mean = round(total / 4, 2)\n    first_plus_second = round(title_chars + desc_chars, 2)\n    first_minus_second = round(title_chars - desc_chars, 2)\n    first_times_second = round(title_chars * desc_chars, 2)\n    return {"total": total, "mean": mean, "first_plus_second": first_plus_second, "first_minus_second": first_minus_second, "first_times_second": first_times_second}\ndef main():\n    a = compute(); b = compute()\n    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()\n    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()\n    for key in ["total", "mean", "first_plus_second", "first_minus_second", "first_times_second"]:\n        print(f"{key}: {a[key]}")\n    print(f"Run 1 SHA-256: {sa}")\n    print(f"Run 2 SHA-256: {sb}")\n    print(f"Deterministic: {\'MATCH\' if sa == sb else \'MISMATCH\'}")\nif __name__ == "__main__":\n    main()\n'

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
