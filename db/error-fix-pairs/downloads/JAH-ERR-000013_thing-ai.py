#!/usr/bin/env python3
"""def handler(): — AI version of def handler(): (JAH-ERR-000013).
No arguments: runs the thing's demo program. With a question:
answers as the thing, from its own numbers, using the same Q&A
logic as the ask box on https://justinahiggins614-cmyk.github.io/jah-databases/db/error-fix-pairs/records/JAH-ERR-000013.html. Run: python3 <file>  OR  python3 <file> "question"
Free forever. Part of The 'Merica-L Internet."""
import json, re, sys
KB = json.loads('{"current": {"id": "JAH-ERR-000013", "title": "def handler():", "family": "error fix", "desc": "def handler():\\n        x = 1\\n      y = 2\\nIndentationError: unindent does not match any outer indentation level", "spec": {"mechanism": "def handler():\\n        x = 1\\n      y = 2\\nIndentationError: unindent does not match any outer indentation level"}, "key_figures": {}, "url": "JAH-ERR-000013.html"}, "records": [{"id": "JAH-ERR-000001", "title": "Traceback (most recent call last):", "family": "error fix", "desc": "Traceback (most recent call last):\\n  File \\"utils.py\\", line 3, in <module>\\n    result = recurse()\\nRecursionError: maximum recursion depth exceeded", "spec": {"mechanism": "Traceback (most recent call last):\\n  File \\"utils.py\\", line 3, in <module>\\n    result = recurse()\\nRecursionError: maximum recursion depth exceeded"}, "key_figures": {}, "url": "JAH-ERR-000001.html"}, {"id": "JAH-ERR-000002", "title": "ReferenceError: window is not defined", "family": "error fix", "desc": "ReferenceError: window is not defined\\n    at render (utils.js:325:201)", "spec": {"mechanism": "ReferenceError: window is not defined\\n    at render (utils.js:325:201)"}, "key_figures": {}, "url": "JAH-ERR-000002.html"}, {"id": "JAH-ERR-000003", "title": "ERROR: column \\"total\\" does not exist", "family": "error fix", "desc": "ERROR: column \\"total\\" does not exist\\nLINE 39: SELECT total FROM (SELECT sum(amount) AS s FROM sales) t;", "spec": {"mechanism": "ERROR: column \\"total\\" does not exist\\nLINE 39: SELECT total FROM (SELECT sum(amount) AS s FROM sales) t;"}, "key_figures": {}, "url": "JAH-ERR-000003.html"}, {"id": "JAH-ERR-000004", "title": "error: remote origin already exists.", "family": "error fix", "desc": "The name `origin` is already taken in this repo.", "spec": {"mechanism": "The name `origin` is already taken in this repo."}, "key_figures": {}, "url": "JAH-ERR-000004.html"}, {"id": "JAH-ERR-000005", "title": "Got permission denied while trying to connect to the Docker daemon socket at uni", "family": "error fix", "desc": "Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock", "spec": {"mechanism": "Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock"}, "key_figures": {}, "url": "JAH-ERR-000005.html"}, {"id": "JAH-ERR-000006", "title": "SSL certificate problem: certificate has expired", "family": "error fix", "desc": "SSL certificate problem: certificate has expired", "spec": {"mechanism": "SSL certificate problem: certificate has expired"}, "key_figures": {}, "url": "JAH-ERR-000006.html"}, {"id": "JAH-ERR-000007", "title": "Traceback (most recent call last):", "family": "error fix", "desc": "Traceback (most recent call last):\\n  File \\"config.py\\", line 62, in <module>\\n    resp = unknown_func()\\nNameError: name \'unknown_func\' is not defined", "spec": {"mechanism": "Traceback (most recent call last):\\n  File \\"config.py\\", line 62, in <module>\\n    resp = unknown_func()\\nNameError: name \'unknown_func\' is not defined"}, "key_figures": {}, "url": "JAH-ERR-000007.html"}, {"id": "JAH-ERR-000008", "title": "ReferenceError: resp is not defined", "family": "error fix", "desc": "ReferenceError: resp is not defined\\n    at init (api.js:625:328)", "spec": {"mechanism": "ReferenceError: resp is not defined\\n    at init (api.js:625:328)"}, "key_figures": {}, "url": "JAH-ERR-000008.html"}, {"id": "JAH-ERR-000009", "title": "ERROR: column reference \\"id\\" is ambiguous", "family": "error fix", "desc": "ERROR: column reference \\"id\\" is ambiguous\\nLINE 851: SELECT id FROM users JOIN orders ON users.id = orders.user_id;", "spec": {"mechanism": "ERROR: column reference \\"id\\" is ambiguous\\nLINE 851: SELECT id FROM users JOIN orders ON users.id = orders.user_id;"}, "key_figures": {}, "url": "JAH-ERR-000009.html"}, {"id": "JAH-ERR-000010", "title": "error: src refspec main does not match any", "family": "error fix", "desc": "error: src refspec main does not match any", "spec": {"mechanism": "error: src refspec main does not match any"}, "key_figures": {}, "url": "JAH-ERR-000010.html"}, {"id": "JAH-ERR-000011", "title": "Error response from daemon: network mynet not found", "family": "error fix", "desc": "Error response from daemon: network mynet not found", "spec": {"mechanism": "Error response from daemon: network mynet not found"}, "key_figures": {}, "url": "JAH-ERR-000011.html"}, {"id": "JAH-ERR-000012", "title": "404 Not Found — {\\"error\\":\\"no_such_resource\\"}", "family": "error fix", "desc": "404 Not Found — {\\"error\\":\\"no_such_resource\\"}", "spec": {"mechanism": "404 Not Found — {\\"error\\":\\"no_such_resource\\"}"}, "key_figures": {}, "url": "JAH-ERR-000012.html"}, {"id": "JAH-ERR-000013", "title": "def handler():", "family": "error fix", "desc": "def handler():\\n        x = 1\\n      y = 2\\nIndentationError: unindent does not match any outer indentation level", "spec": {"mechanism": "def handler():\\n        x = 1\\n      y = 2\\nIndentationError: unindent does not match any outer indentation level"}, "key_figures": {}, "url": "JAH-ERR-000013.html"}, {"id": "JAH-ERR-000014", "title": "TypeError: data.map is not a function", "family": "error fix", "desc": "TypeError: data.map is not a function\\n    at list (server.js:426:270)", "spec": {"mechanism": "TypeError: data.map is not a function\\n    at list (server.js:426:270)"}, "key_figures": {}, "url": "JAH-ERR-000014.html"}, {"id": "JAH-ERR-000015", "title": "ERROR: column reference \\"id\\" is ambiguous", "family": "error fix", "desc": "ERROR: column reference \\"id\\" is ambiguous\\nLINE 404: SELECT id FROM users JOIN orders ON users.id = orders.user_id;", "spec": {"mechanism": "ERROR: column reference \\"id\\" is ambiguous\\nLINE 404: SELECT id FROM users JOIN orders ON users.id = orders.user_id;"}, "key_figures": {}, "url": "JAH-ERR-000015.html"}, {"id": "JAH-ERR-000016", "title": "Permission denied (publickey).", "family": "error fix", "desc": "Permission denied (publickey).\\nfatal: Could not read from remote repository.", "spec": {"mechanism": "Permission denied (publickey).\\nfatal: Could not read from remote repository."}, "key_figures": {}, "url": "JAH-ERR-000016.html"}, {"id": "JAH-ERR-000017", "title": "Got permission denied while trying to connect to the Docker daemon socket at uni", "family": "error fix", "desc": "Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock", "spec": {"mechanism": "Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock"}, "key_figures": {}, "url": "JAH-ERR-000017.html"}, {"id": "JAH-ERR-000018", "title": "500 Internal Server Error — {\\"error\\":\\"unexpected\\"}", "family": "error fix", "desc": "500 Internal Server Error — {\\"error\\":\\"unexpected\\"}", "spec": {"mechanism": "500 Internal Server Error — {\\"error\\":\\"unexpected\\"}"}, "key_figures": {}, "url": "JAH-ERR-000018.html"}, {"id": "JAH-ERR-000019", "title": "Traceback (most recent call last):", "family": "error fix", "desc": "Traceback (most recent call last):\\n  File \\"utils.py\\", line 327, in <module>\\n    total = count + \\"5\\"\\nTypeError: unsupported operand type(s) for +: \'int\' and \'str\'", "spec": {"mechanism": "Traceback (most recent call last):\\n  File \\"utils.py\\", line 327, in <module>\\n    total = count + \\"5\\"\\nTypeError: unsupported operand type(s) for +: \'int\' and \'str\'"}, "key_figures": {}, "url": "JAH-ERR-000019.html"}, {"id": "JAH-ERR-000020", "title": "ReferenceError: window is not defined", "family": "error fix", "desc": "ReferenceError: window is not defined\\n    at render (index.js:385:292)", "spec": {"mechanism": "ReferenceError: window is not defined\\n    at render (index.js:385:292)"}, "key_figures": {}, "url": "JAH-ERR-000020.html"}, {"id": "JAH-ERR-000021", "title": "ERROR: deadlock detected", "family": "error fix", "desc": "ERROR: deadlock detected\\nDETAIL: Process 447 waits for ShareLock on transaction 9030; blocked by process 349.", "spec": {"mechanism": "ERROR: deadlock detected\\nDETAIL: Process 447 waits for ShareLock on transaction 9030; blocked by process 349."}, "key_figures": {}, "url": "JAH-ERR-000021.html"}, {"id": "JAH-ERR-000022", "title": "Permission denied (publickey).", "family": "error fix", "desc": "Permission denied (publickey).\\nfatal: Could not read from remote repository.", "spec": {"mechanism": "Permission denied (publickey).\\nfatal: Could not read from remote repository."}, "key_figures": {}, "url": "JAH-ERR-000022.html"}, {"id": "JAH-ERR-000023", "title": "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docke", "family": "error fix", "desc": "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?", "spec": {"mechanism": "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?"}, "key_figures": {}, "url": "JAH-ERR-000023.html"}, {"id": "JAH-ERR-000024", "title": "500 Internal Server Error — {\\"error\\":\\"unexpected\\"}", "family": "error fix", "desc": "500 Internal Server Error — {\\"error\\":\\"unexpected\\"}", "spec": {"mechanism": "500 Internal Server Error — {\\"error\\":\\"unexpected\\"}"}, "key_figures": {}, "url": "JAH-ERR-000024.html"}], "twin": {"id": "error-fix-pairs-signature", "title": "JAH Error Fix Database — Signature edition", "url": "../website/mirror/index.html"}, "sources": [], "gen_prefix": "JAH-ERR-GEN-"}')
DEMO_CODE = '"""Numeric check — def handler(): (JAH-ERR-000013).\nMade for this page from text-derived counts (the record carries no usable numbers of its own).\nThis program checks the arithmetic of the stored figures; its outputs\nare check-sums, not physical quantities."""\nimport hashlib\ndef compute():\n    title_chars = 14; desc_chars = 110; source_count = 0; field_count = 9\n    total = round(title_chars + desc_chars + source_count + field_count, 2)\n    mean = round(total / 4, 2)\n    first_plus_second = round(title_chars + desc_chars, 2)\n    first_minus_second = round(title_chars - desc_chars, 2)\n    first_times_second = round(title_chars * desc_chars, 2)\n    return {"total": total, "mean": mean, "first_plus_second": first_plus_second, "first_minus_second": first_minus_second, "first_times_second": first_times_second}\ndef main():\n    a = compute(); b = compute()\n    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()\n    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()\n    for key in ["total", "mean", "first_plus_second", "first_minus_second", "first_times_second"]:\n        print(f"{key}: {a[key]}")\n    print(f"Run 1 SHA-256: {sa}")\n    print(f"Run 2 SHA-256: {sb}")\n    print(f"Deterministic: {\'MATCH\' if sa == sb else \'MISMATCH\'}")\nif __name__ == "__main__":\n    main()\n'

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
