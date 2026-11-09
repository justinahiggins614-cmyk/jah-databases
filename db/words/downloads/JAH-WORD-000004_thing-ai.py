#!/usr/bin/env python3
""""4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids — AI version of "4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids (JAH-WORD-000004).
No arguments: runs the thing's demo program. With a question:
answers as the thing, from its own numbers, using the same Q&A
logic as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/words/records/JAH-WORD-000004.html. Run: python3 <file>  OR  python3 <file> "question"
Free forever. Part of The 'Merica-L Internet."""
import json, re, sys
KB = json.loads('{"current": {"id": "JAH-WORD-000004", "title": "\\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids", "family": "dictionary entry", "desc": "Public patent AU518848B2 — \\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids. Assignee: Ishihara Sangyo Kaisha Ltd.. Class: A44", "spec": {"mechanism": "Public patent AU518848B2 — \\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids. Assignee: Ishihara Sangyo Kaisha Ltd.. Class: A44"}, "key_figures": {}, "url": "JAH-WORD-000004.html"}, "records": [{"id": "JAH-WORD-000001", "title": "\\"1-hydroxyalkanamine pyrano (3,4-beta) indole derivatives\\"", "family": "dictionary entry", "desc": "Public patent AU4642279A — \\"1-hydroxyalkanamine pyrano (3,4-beta) indole derivatives\\". Assignee: American Home Products Corporation. Class: A46", "spec": {"mechanism": "Public patent AU4642279A — \\"1-hydroxyalkanamine pyrano (3,4-beta) indole derivatives\\". Assignee: American Home Products Corporation. Class: A46"}, "key_figures": {}, "url": "JAH-WORD-000001.html"}, {"id": "JAH-WORD-000002", "title": "\\"15-deoxy-16-hydroxyprostaglandins\\"", "family": "dictionary entry", "desc": "Public patent AU4449379A — \\"15-deoxy-16-hydroxyprostaglandins\\". Assignee: Miles Laboratories Inc.. Class: A46", "spec": {"mechanism": "Public patent AU4449379A — \\"15-deoxy-16-hydroxyprostaglandins\\". Assignee: Miles Laboratories Inc.. Class: A46"}, "key_figures": {}, "url": "JAH-WORD-000002.html"}, {"id": "JAH-WORD-000003", "title": "\\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids", "family": "dictionary entry", "desc": "Public patent AU4462979A — \\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids. Assignee: Ishihara Sangyo Kaisha Ltd.. Class: A24", "spec": {"mechanism": "Public patent AU4462979A — \\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids. Assignee: Ishihara Sangyo Kaisha Ltd.. Class: A24"}, "key_figures": {}, "url": "JAH-WORD-000003.html"}, {"id": "JAH-WORD-000004", "title": "\\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids", "family": "dictionary entry", "desc": "Public patent AU518848B2 — \\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids. Assignee: Ishihara Sangyo Kaisha Ltd.. Class: A44", "spec": {"mechanism": "Public patent AU518848B2 — \\"4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids. Assignee: Ishihara Sangyo Kaisha Ltd.. Class: A44"}, "key_figures": {}, "url": "JAH-WORD-000004.html"}, {"id": "JAH-WORD-000005", "title": "\\"ADJUSTMENT DEVICE FOR THE INCLINE OF A FRONT FORK OF A TWO OR THREE-WHEEL &hellip;", "family": "dictionary entry", "desc": "Public patent ITTO20080132A1 — \\"ADJUSTMENT DEVICE FOR THE INCLINE OF A FRONT FORK OF A TWO OR THREE-WHEEL &hellip;. Assignee: Romano Clari. Class: A44", "spec": {"mechanism": "Public patent ITTO20080132A1 — \\"ADJUSTMENT DEVICE FOR THE INCLINE OF A FRONT FORK OF A TWO OR THREE-WHEEL &hellip;. Assignee: Romano Clari. Class: A44"}, "key_figures": {}, "url": "JAH-WORD-000005.html"}, {"id": "JAH-WORD-000006", "title": "\\"AEROBIC HARDENING PLASTICS\\"", "family": "dictionary entry", "desc": "Public patent DE3201731A1 — \\"AEROBIC HARDENING PLASTICS\\". Assignee: Henkel KGaA, 4000 Düsseldorf. Class: A22", "spec": {"mechanism": "Public patent DE3201731A1 — \\"AEROBIC HARDENING PLASTICS\\". Assignee: Henkel KGaA, 4000 Düsseldorf. Class: A22"}, "key_figures": {}, "url": "JAH-WORD-000006.html"}, {"id": "JAH-WORD-000007", "title": "\\"AMINOCYCLOPENTANAL ACID ACIDS AND ESTERS AND THEIR PRODUCTION AND &hellip;", "family": "dictionary entry", "desc": "Public patent DE3117087A1 — \\"AMINOCYCLOPENTANAL ACID ACIDS AND ESTERS AND THEIR PRODUCTION AND &hellip;. Assignee: Glaxo Group Ltd., London. Class: A46", "spec": {"mechanism": "Public patent DE3117087A1 — \\"AMINOCYCLOPENTANAL ACID ACIDS AND ESTERS AND THEIR PRODUCTION AND &hellip;. Assignee: Glaxo Group Ltd., London. Class: A46"}, "key_figures": {}, "url": "JAH-WORD-000007.html"}, {"id": "JAH-WORD-000008", "title": "\\"BLOOD PRESSURE MEASURING DEVICE\\"", "family": "dictionary entry", "desc": "Public patent DE3133410A1 — \\"BLOOD PRESSURE MEASURING DEVICE\\". Assignee: Matsushita Electric Works Ltd., Kadoma, Osaka. Class: A42", "spec": {"mechanism": "Public patent DE3133410A1 — \\"BLOOD PRESSURE MEASURING DEVICE\\". Assignee: Matsushita Electric Works Ltd., Kadoma, Osaka. Class: A42"}, "key_figures": {}, "url": "JAH-WORD-000008.html"}, {"id": "JAH-WORD-000009", "title": "\\"cabbage rolls filled with mussels\\" preserves production method", "family": "dictionary entry", "desc": "Public patent RU2483643C1 — \\"cabbage rolls filled with mussels\\" preserves production method. Assignee: Олег Иванович Квасенков. Class: A23", "spec": {"mechanism": "Public patent RU2483643C1 — \\"cabbage rolls filled with mussels\\" preserves production method. Assignee: Олег Иванович Квасенков. Class: A23"}, "key_figures": {}, "url": "JAH-WORD-000009.html"}, {"id": "JAH-WORD-000010", "title": "\\"CHOCOLATE AROMA EXTRACT\\".", "family": "dictionary entry", "desc": "Public patent ES2255456B1 — \\"CHOCOLATE AROMA EXTRACT\\".. Assignee: Natraceutical, S.A.. Class: A21", "spec": {"mechanism": "Public patent ES2255456B1 — \\"CHOCOLATE AROMA EXTRACT\\".. Assignee: Natraceutical, S.A.. Class: A21"}, "key_figures": {}, "url": "JAH-WORD-000010.html"}, {"id": "JAH-WORD-000011", "title": "\\"CLUTCH FOR A POWER TOOL\\"", "family": "dictionary entry", "desc": "Public patent DE3101080A1 — \\"CLUTCH FOR A POWER TOOL\\". Assignee: Desoutter Ltd., London. Class: A44", "spec": {"mechanism": "Public patent DE3101080A1 — \\"CLUTCH FOR A POWER TOOL\\". Assignee: Desoutter Ltd., London. Class: A44"}, "key_figures": {}, "url": "JAH-WORD-000011.html"}, {"id": "JAH-WORD-000012", "title": "\\"COLOR PHOTOGRAPHIC SILVER HALOGENIDE MATERIAL\\"", "family": "dictionary entry", "desc": "Public patent DE3100961A1 — \\"COLOR PHOTOGRAPHIC SILVER HALOGENIDE MATERIAL\\". Assignee: Konishiroku Photo Industry Co., Ltd., Tokyo. Class: A21", "spec": {"mechanism": "Public patent DE3100961A1 — \\"COLOR PHOTOGRAPHIC SILVER HALOGENIDE MATERIAL\\". Assignee: Konishiroku Photo Industry Co., Ltd., Tokyo. Class: A21"}, "key_figures": {}, "url": "JAH-WORD-000012.html"}, {"id": "JAH-WORD-000013", "title": "\\"conjunto para prender tecido ou um elemento protético em uma abertura &hellip;", "family": "dictionary entry", "desc": "Public patent BR112012018010B1 — \\"conjunto para prender tecido ou um elemento protético em uma abertura &hellip;. Assignee: Sportwelding Gmbh. Class: A44", "spec": {"mechanism": "Public patent BR112012018010B1 — \\"conjunto para prender tecido ou um elemento protético em uma abertura &hellip;. Assignee: Sportwelding Gmbh. Class: A44"}, "key_figures": {}, "url": "JAH-WORD-000013.html"}, {"id": "JAH-WORD-000014", "title": "\\"CYLINDER CHANGE DEVICE FOR HIGH CYLINDER SEWING MACHINES\\"", "family": "dictionary entry", "desc": "Public patent ITMI20040411U1 — \\"CYLINDER CHANGE DEVICE FOR HIGH CYLINDER SEWING MACHINES\\". Assignee: Chee Siang Ind Co Ltd. Class: A45", "spec": {"mechanism": "Public patent ITMI20040411U1 — \\"CYLINDER CHANGE DEVICE FOR HIGH CYLINDER SEWING MACHINES\\". Assignee: Chee Siang Ind Co Ltd. Class: A45"}, "key_figures": {}, "url": "JAH-WORD-000014.html"}, {"id": "JAH-WORD-000015", "title": "\\"dezbel\\" disinfecting and bleaching agent", "family": "dictionary entry", "desc": "Public patent SU1189877A1 — \\"dezbel\\" disinfecting and bleaching agent. Assignee: Закавказский Комплексный Отдел Московского Филиала Всесоюзного Научно- &hellip;. Class: A41", "spec": {"mechanism": "Public patent SU1189877A1 — \\"dezbel\\" disinfecting and bleaching agent. Assignee: Закавказский Комплексный Отдел Московского Филиала Всесоюзного Научно- &hellip;. Class: A41"}, "key_figures": {}, "url": "JAH-WORD-000015.html"}, {"id": "JAH-WORD-000016", "title": "\\"ECLIPSE\\" PORTABLE OBJECTS TROUSSE", "family": "dictionary entry", "desc": "Public patent ITME970021A1 — \\"ECLIPSE\\" PORTABLE OBJECTS TROUSSE. Assignee: Monica Raffa. Class: A45", "spec": {"mechanism": "Public patent ITME970021A1 — \\"ECLIPSE\\" PORTABLE OBJECTS TROUSSE. Assignee: Monica Raffa. Class: A45"}, "key_figures": {}, "url": "JAH-WORD-000016.html"}, {"id": "JAH-WORD-000017", "title": "\\"elan\\" electric analgesia apparatus", "family": "dictionary entry", "desc": "Public patent SU605620A1 — \\"elan\\" electric analgesia apparatus. Assignee: Научно-Исследовательский Институт Акушерства И Гинекологии. Class: A61", "spec": {"mechanism": "Public patent SU605620A1 — \\"elan\\" electric analgesia apparatus. Assignee: Научно-Исследовательский Институт Акушерства И Гинекологии. Class: A61"}, "key_figures": {}, "url": "JAH-WORD-000017.html"}, {"id": "JAH-WORD-000018", "title": "\\"ELECTRICAL CONNECTION OF SEMICONDUCTOR CABLES\\"", "family": "dictionary entry", "desc": "Public patent DE3102106A1 — \\"ELECTRICAL CONNECTION OF SEMICONDUCTOR CABLES\\". Assignee: RCA Corp., 10020 New York, N.Y.. Class: A42", "spec": {"mechanism": "Public patent DE3102106A1 — \\"ELECTRICAL CONNECTION OF SEMICONDUCTOR CABLES\\". Assignee: RCA Corp., 10020 New York, N.Y.. Class: A42"}, "key_figures": {}, "url": "JAH-WORD-000018.html"}, {"id": "JAH-WORD-000019", "title": "\\"ELECTRONIC TRANSLATION DEVICE\\"", "family": "dictionary entry", "desc": "Public patent DE3129011A1 — \\"ELECTRONIC TRANSLATION DEVICE\\". Assignee: Sharp K.K., Osaka. Class: A42", "spec": {"mechanism": "Public patent DE3129011A1 — \\"ELECTRONIC TRANSLATION DEVICE\\". Assignee: Sharp K.K., Osaka. Class: A42"}, "key_figures": {}, "url": "JAH-WORD-000019.html"}, {"id": "JAH-WORD-000020", "title": "\\"elite\\" fish roll production method", "family": "dictionary entry", "desc": "Public patent RU2506000C2 — \\"elite\\" fish roll production method. Assignee: Федеральное государственное бюджетное образовательное учреждение высшего &hellip;. Class: A23", "spec": {"mechanism": "Public patent RU2506000C2 — \\"elite\\" fish roll production method. Assignee: Федеральное государственное бюджетное образовательное учреждение высшего &hellip;. Class: A23"}, "key_figures": {}, "url": "JAH-WORD-000020.html"}, {"id": "JAH-WORD-000021", "title": "\\"Grosse rote Fleischtomate\\", and \\"Weiterzüchtung 1981\\" bred from it", "family": "dictionary entry", "desc": "Public patent DE3201661A1 — \\"Grosse rote Fleischtomate\\", and \\"Weiterzüchtung 1981\\" bred from it. Assignee: Manfred Otto 6742 Herxheim Müller. Class: A01", "spec": {"mechanism": "Public patent DE3201661A1 — \\"Grosse rote Fleischtomate\\", and \\"Weiterzüchtung 1981\\" bred from it. Assignee: Manfred Otto 6742 Herxheim Müller. Class: A01"}, "key_figures": {}, "url": "JAH-WORD-000021.html"}, {"id": "JAH-WORD-000022", "title": "\\"imperial\\"-brand vodka", "family": "dictionary entry", "desc": "Public patent RU1782238C — \\"imperial\\"-brand vodka. Assignee: Назим Аллахверди-Оглы Ибрагимов. Class: A22", "spec": {"mechanism": "Public patent RU1782238C — \\"imperial\\"-brand vodka. Assignee: Назим Аллахверди-Оглы Ибрагимов. Class: A22"}, "key_figures": {}, "url": "JAH-WORD-000022.html"}, {"id": "JAH-WORD-000023", "title": "\\"INORGANIC FOAM PRODUCT\\"", "family": "dictionary entry", "desc": "Public patent DE3100655A1 — \\"INORGANIC FOAM PRODUCT\\". Assignee: Imperial Chemical Industries Ltd., London. Class: A24", "spec": {"mechanism": "Public patent DE3100655A1 — \\"INORGANIC FOAM PRODUCT\\". Assignee: Imperial Chemical Industries Ltd., London. Class: A24"}, "key_figures": {}, "url": "JAH-WORD-000023.html"}, {"id": "JAH-WORD-000024", "title": "\\"isoquinoline derivatives\\"", "family": "dictionary entry", "desc": "Public patent AU540284B2 — \\"isoquinoline derivatives\\". Assignee: F. Hoffmann-La Roche & Co.. Class: A23", "spec": {"mechanism": "Public patent AU540284B2 — \\"isoquinoline derivatives\\". Assignee: F. Hoffmann-La Roche & Co.. Class: A23"}, "key_figures": {}, "url": "JAH-WORD-000024.html"}], "twin": {"id": "words-signature", "title": "The Signature Dictionary Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-WORD-GEN-"}')
DEMO_CODE = '"""Numeric check — "4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids (JAH-WORD-000004).\nMade for this page from text-derived counts (the record carries no usable numbers of its own).\nThis program checks the arithmetic of the stored figures; its outputs\nare check-sums, not physical quantities."""\nimport hashlib\ndef compute():\n    title_chars = 52; desc_chars = 130; source_count = 0; field_count = 7\n    total = round(title_chars + desc_chars + source_count + field_count, 2)\n    mean = round(total / 4, 2)\n    first_plus_second = round(title_chars + desc_chars, 2)\n    first_minus_second = round(title_chars - desc_chars, 2)\n    first_times_second = round(title_chars * desc_chars, 2)\n    return {"total": total, "mean": mean, "first_plus_second": first_plus_second, "first_minus_second": first_minus_second, "first_times_second": first_times_second}\ndef main():\n    a = compute(); b = compute()\n    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()\n    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()\n    for key in ["total", "mean", "first_plus_second", "first_minus_second", "first_times_second"]:\n        print(f"{key}: {a[key]}")\n    print(f"Run 1 SHA-256: {sa}")\n    print(f"Run 2 SHA-256: {sb}")\n    print(f"Deterministic: {\'MATCH\' if sa == sb else \'MISMATCH\'}")\nif __name__ == "__main__":\n    main()\n'

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
