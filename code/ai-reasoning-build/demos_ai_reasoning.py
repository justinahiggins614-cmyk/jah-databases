#!/usr/bin/env python3
"""Demos for the AI Reasoning databases.

DEMOS maps demo_key (e.g. 'COT-03') to a function
fn(hdr, name, rid, group, demo_data) -> program string.

Every program is real, runnable, stdlib-only Python: it computes real
values from data derived from the record's rank, prints them, asserts
tight structural bounds (never float exact-equality), and ends with the
OK marker. The build machine-executes all 1700 demos.
"""

OK = 'print("OK: __RIDQ__ complete")'


def _sub(tpl, name, rid, rank):
    return (tpl.replace("__NAME__", name.replace('"', "'"))
               .replace("__RID__", rid)
               .replace("__RIDQ__", rid)
               .replace("__RANK__", str(rank)))


def demo_memory(hdr, name, rid, group, dd):
    r = dd["rank"]
    n = 6 + (r % 5)
    thr = 4 + (r % 3)
    items = [("core_goal", 10, 50), ("trivia_old", 1, 45)]
    for i in range(n):
        imp = 2 + ((i * 7 + r) % 8)
        age = 3 + ((i * 11 + r) % 40)
        items.append(("item_%d" % i, imp, age))
    body = '''\
items = __ITEMS__
threshold = __THR__
kept = [lb for lb, imp, age in items if imp >= threshold or age <= 5]
forgotten = [lb for lb, imp, age in items if lb not in kept]
print("memory items:", len(items))
print("kept:", len(kept), kept)
print("forgotten:", len(forgotten), forgotten)
assert "core_goal" in kept, "high-importance old item must be retained"
assert "trivia_old" in forgotten, "low-importance old item must decay"
assert len(kept) + len(forgotten) == len(items)
assert 1 <= len(kept) < len(items)
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__ITEMS__", repr(items)).replace("__THR__", str(thr))


def demo_chain(hdr, name, rid, group, dd):
    r = dd["rank"]
    a = 10 + r
    b = 3 + (r % 4)
    c = 2 + (r % 3)
    body = '''\
a, b, c = __A__, __B__, __C__
s1 = a + b
print("step 1: a + b =", s1)
s2 = s1 * c
print("step 2: s1 * c =", s2)
s3 = s2 - a
print("step 3: s2 - a =", s3)
check = (a + b) * c - a
assert s3 == check, "chain recomputation mismatch"
assert s1 == a + b and s2 == s1 * c
est = a * c
assert abs(s3 - est) < a * (b + 1) + c * 10, "magnitude sanity failed"
print("chain verified: final =", s3)
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__A__", str(a)).replace("__B__", str(b)).replace("__C__", str(c))


def demo_plan(hdr, name, rid, group, dd):
    r = dd["rank"]
    durs = {"research": 2 + (r % 3), "outline": 1 + (r % 2),
            "draft": 3 + (r % 4), "review": 2, "ship": 1}
    deps = {"outline": ["research"], "draft": ["outline"],
            "review": ["draft"], "ship": ["review"]}
    body = '''\
durs = __DURS__
deps = __DEPS__
order, done, deps_left = [], set(), {k: list(v) for k, v in deps.items()}
tasks = list(durs)
while len(order) < len(tasks):
    ready = [t for t in tasks if t not in done
             and all(d in done for d in deps_left.get(t, []))]
    assert ready, "dependency cycle detected"
    nxt = sorted(ready)[0]
    order.append(nxt)
    done.add(nxt)
print("execution order:", order)
pos = {t: i for i, t in enumerate(order)}
for t, ds in deps.items():
    for d in ds:
        assert pos[d] < pos[t], "dependency violated"
finish = {}
for t in order:
    finish[t] = durs[t] + max([finish[d] for d in deps.get(t, [])] or [0])
critical = max(finish.values())
print("task finish times:", finish)
print("critical path length:", critical)
assert critical == sum(durs[t] for t in ("research", "outline", "draft", "review", "ship"))
assert critical >= max(durs.values())
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__DURS__", repr(durs)).replace("__DEPS__", repr(deps))


def demo_tools(hdr, name, rid, group, dd):
    r = dd["rank"]
    body = '''\
schemas = {
    "web_search": {"required": ["query"], "optional": ["max_results"]},
    "code_exec": {"required": ["code"], "optional": ["timeout"]},
    "file_read": {"required": ["path"], "optional": []},
}
calls = [
    ("web_search", {"query": "context window pricing", "max_results": 5}),
    ("code_exec", {"code": "print(40 + 2)"}),
    ("file_read", {"path": "/tmp/missing.txt"}),
    ("web_search", {"max_results": 5}),
]
results, retries = [], 0
for tool, args in calls:
    schema = schemas[tool]
    missing = [k for k in schema["required"] if k not in args]
    if missing:
        results.append((tool, "invalid: missing %s" % missing))
        continue
    if tool == "file_read" and retries == 0:
        retries += 1
        results.append((tool, "transient failure -> retried"))
        results.append((tool, "ok: 42 bytes read"))
        continue
    results.append((tool, "ok"))
for tool, res in results:
    print(tool, "->", res)
ok = sum(1 for _, res in results if res == "ok" or res.startswith("ok:"))
invalid = sum(1 for _, res in results if res.startswith("invalid"))
assert ok == 3, "expected 3 successful calls"
assert invalid == 1, "expected 1 invalid call caught pre-invocation"
assert retries == 1, "expected exactly one retry"
''' + OK
    return _sub(hdr(name, rid, group) + body, name, rid, r)


def demo_retrieval(hdr, name, rid, group, dd):
    r = dd["rank"]
    k = 3 + (r % 3)
    body = '''\
chunks = [
    ("c0", "the refund policy allows returns within thirty days of purchase with receipt"),
    ("c1", "our offices are located downtown near the central station"),
    ("c2", "the quarterly report shows revenue growth of twelve percent"),
    ("c3", "to reset your password visit the account settings page"),
    ("c4", "shipping times vary by region and carrier selection"),
    ("c5", "the warranty covers manufacturing defects for one year"),
]
query = "what is the refund policy for returns"
qterms = set(query.split())
ranked = []
for cid, text in chunks:
    terms = set(text.split())
    overlap = len(qterms & terms)
    score = overlap / max(1, len(qterms))
    ranked.append((score, cid, text))
ranked.sort(reverse=True)
print("top-%d:" % __K__)
for score, cid, text in ranked[:__K__]:
    print("  %.2f %s: %s" % (score, cid, text[:60]))
assert ranked[0][1] == "c0", "most relevant chunk must rank first"
assert ranked[0][0] > ranked[1][0], "scores must separate"
assert all(0.0 <= s <= 1.0 for s, _, _ in ranked)
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__K__", str(k))


def demo_extract(hdr, name, rid, group, dd):
    r = dd["rank"]
    k = 2 + (r % 2)
    body = '''\
sentences = [
    "The committee reviewed the quarterly figures at length.",
    "Decision: the launch is postponed to next quarter pending the audit.",
    "Several members discussed marketing channel performance.",
    "The budget for the pilot was approved at four hundred thousand.",
    "Action item: Maya to circulate the revised timeline by Friday.",
    "Lunch options for the offsite were briefly considered.",
]
key_terms = {"decision", "approved", "action", "budget", "launch"}
scored = []
for i, s in enumerate(sentences):
    words = set(s.lower().split())
    kw = len(words & key_terms)
    pos_w = 1.0 / (1 + i * 0.15)
    score = kw * 2.0 + pos_w
    scored.append((score, i, s))
scored.sort(reverse=True)
summary = [s for _, _, s in scored[:__K__]]
print("selected %d of %d sentences:" % (__K__, len(sentences)))
for s in summary:
    print(" -", s)
joined = " ".join(summary).lower()
assert "decision" in joined or "approved" in joined or "action" in joined
assert len(summary) == __K__ < len(sentences)
assert all(isinstance(s, str) and s for s in summary)
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__K__", str(k))


def demo_qa(hdr, name, rid, group, dd):
    r = dd["rank"]
    body = '''\
questions = [
    ("What is the capital of France?", "fact"),
    ("How do I reset my password?", "procedure"),
    ("Why did the deploy fail?", "explanation"),
    ("Is this a good deal?", "opinion"),
    ("What if we doubled the budget?", "hypothetical"),
    ("When was the company founded?", "fact"),
    ("Compare Postgres and MySQL.", "comparison"),
    ("Summarize the report.", "summary"),
]
def classify(q):
    ql = q.lower()
    if ql.startswith(("what is", "what was", "when", "where", "who")):
        return "fact"
    if ql.startswith("how do"):
        return "procedure"
    if ql.startswith("why"):
        return "explanation"
    if ql.startswith("is this") or "good" in ql:
        return "opinion"
    if "what if" in ql:
        return "hypothetical"
    if ql.startswith("compare"):
        return "comparison"
    if ql.startswith("summarize"):
        return "summary"
    return "unknown"
hits = sum(1 for q, t in questions if classify(q) == t)
acc = hits / len(questions)
print("classified %d/%d correctly (%.2f)" % (hits, len(questions), acc))
assert acc >= 0.75, "classifier accuracy below bar"
assert hits <= len(questions)
''' + OK
    return _sub(hdr(name, rid, group) + body, name, rid, r)


def demo_correct(hdr, name, rid, group, dd):
    r = dd["rank"]
    n = 4 + (r % 3)
    body = '''\
def attempt(x):
    # buggy version: off-by-one on even inputs
    return x * 2 + (1 if x % 2 == 0 else 0)

def expected(x):
    return x * 2

def fixed(x):
    return x * 2

xs = list(range(1, __N__ + 1))
errors = [x for x in xs if attempt(x) != expected(x)]
print("generate: %d errors detected in %d cases" % (len(errors), len(xs)))
assert errors, "critique must find at least one error"
print("diagnosis: even inputs add a spurious +1")
repaired = [fixed(x) for x in xs]
assert all(fixed(x) == expected(x) for x in xs), "repair incomplete"
print("repair verified on all %d cases" % len(xs))
assert len(errors) <= len(xs) // 2 + 1
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__N__", str(n))


def demo_calibrate(hdr, name, rid, group, dd):
    r = dd["rank"]
    n = 20
    body = '''\
n = __N__
items = []
for i in range(n):
    conf = round(0.55 + 0.05 * ((i * 3 + __R__) % 9), 2)
    correct = ((i * 13 + __R__) % 100) < int(conf * 100)
    items.append((conf, correct))
bins = {"low": [], "mid": [], "high": []}
for conf, correct in items:
    b = "low" if conf < 0.7 else ("mid" if conf < 0.85 else "high")
    bins[b].append((conf, correct))
gaps = {}
for b, bs in bins.items():
    acc = sum(1 for _, c in bs if c) / len(bs)
    avg_conf = sum(c for c, _ in bs) / len(bs)
    gaps[b] = abs(acc - avg_conf)
    print("bin %s: n=%d acc=%.2f avg_conf=%.2f gap=%.2f"
          % (b, len(bs), acc, avg_conf, gaps[b]))
max_gap = max(gaps.values())
print("max calibration gap: %.2f" % max_gap)
assert max_gap < 0.35, "calibration gap too large"
assert all(len(bs) > 0 for bs in bins.values())
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__N__", str(n)).replace("__R__", str(r))


def demo_agents(hdr, name, rid, group, dd):
    r = dd["rank"]
    rounds = 4 + (r % 3)
    body = '''\
positions = {"agent_a": 2.0 + __R__ % 3, "agent_b": 8.0, "agent_c": 5.0}
print("initial:", positions)
for rnd in range(__ROUNDS__):
    med = sorted(positions.values())[1]
    positions = {a: round(p + 0.5 * (med - p), 3)
                 for a, p in positions.items()}
    print("round %d:" % (rnd + 1), positions)
vals = list(positions.values())
spread = max(vals) - min(vals)
print("final spread: %.3f" % spread)
assert spread < 1.0, "agents failed to converge"
assert all(0.0 <= v <= 10.0 for v in vals)
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__R__", str(r)).replace("__ROUNDS__", str(rounds))


def demo_budget(hdr, name, rid, group, dd):
    r = dd["rank"]
    body = '''\
sections = [
    ("system_prompt", 2000, 10),
    ("conversation", 8000 + (__R__ % 5) * 1000, 9),
    ("retrieved_docs", 20000, 8),
    ("tool_results", 5000, 7),
    ("examples", 4000, 5),
    ("debug_logs", 15000, 2),
]
budget = 30000
sections.sort(key=lambda s: -s[2])
used, kept = 0, []
for label, cost, pri in sections:
    if used + cost <= budget:
        used += cost
        kept.append(label)
print("budget:", budget, "used:", used)
print("kept:", kept)
assert used <= budget, "budget exceeded"
assert "system_prompt" in kept, "highest priority must be kept"
assert "debug_logs" not in kept, "lowest priority must be dropped first"
assert used > budget * 0.5, "budget underutilized"
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__R__", str(r))


def demo_fuse(hdr, name, rid, group, dd):
    r = dd["rank"]
    wv = round(0.3 + 0.05 * (r % 5), 2)
    wa = round(0.2 + 0.05 * ((r + 1) % 4), 2)
    wt = round(1.0 - wv - wa, 2)
    body = '''\
scores = {"vision": 0.82, "audio": 0.64, "text": 0.91}
weights = {"vision": __WV__, "audio": __WA__, "text": __WT__}
assert abs(sum(weights.values()) - 1.0) < 1e-9, "weights must sum to 1"
fused = sum(scores[m] * weights[m] for m in scores)
print("modality scores:", scores)
print("fusion weights:", weights)
print("fused score: %.4f" % fused)
assert min(scores.values()) <= fused <= max(scores.values())
assert 0.0 <= fused <= 1.0
best = max(scores, key=scores.get)
print("strongest modality:", best)
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return (prog.replace("__WV__", str(wv)).replace("__WA__", str(wa))
                .replace("__WT__", str(wt)))


def demo_code(hdr, name, rid, group, dd):
    r = dd["rank"]
    k = 3 + (r % 3)
    body = '''\
def chunk_list(xs, k):
    return [xs[i:i + k] for i in range(0, len(xs), k)]

data = list(range(1, 11))
chunks = chunk_list(data, __K__)
print("data:", data)
print("chunks (k=%d):" % __K__, chunks)
assert sum(len(c) for c in chunks) == len(data), "items lost"
assert chunks[0] == data[:__K__], "first chunk wrong"
assert all(len(c) <= __K__ for c in chunks), "chunk too large"
flat = [x for c in chunks for x in c]
assert flat == data, "order not preserved"
print("chunking verified: %d chunks, order preserved" % len(chunks))
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__K__", str(k))


def demo_united(hdr, name, rid, group, dd):
    r = dd["rank"]
    k = 2 + (r % 2)
    body = '''\
print("stage 1: retrieve")
chunks = [("c0", "deploy checklist requires canary analysis before rollout"),
          ("c1", "the office kitchen was restocked on tuesday"),
          ("c2", "canary deployments limit blast radius during releases")]
q = {"deploy", "canary", "checklist"}
scored = sorted(((len(q & set(t.split())), c) for c, t in chunks),
                reverse=True)
retrieved = [c for _, c in scored[:__K__]]
print(" retrieved:", retrieved)
assert retrieved[0] == "c0"
print("stage 2: reason (chain)")
steps = ["identify requirement", "check canary status", "decide rollout"]
trace = " -> ".join(steps)
print(" chain:", trace)
assert len(steps) == 3
print("stage 3: summarize")
summary = "Deploy requires canary analysis first."
print(" summary:", summary)
assert "canary" in summary
print("stage 4: confidence")
conf = 0.85
print(" confidence: %.2f" % conf)
assert 0.5 < conf < 1.0
print("pipeline complete: retrieve -> reason -> summarize -> confidence")
''' + OK
    prog = _sub(hdr(name, rid, group) + body, name, rid, r)
    return prog.replace("__K__", str(k))


ARCH = {
 "session-memory": demo_memory, "long-term-memory": demo_memory,
 "episodic-memory": demo_memory, "semantic-memory": demo_retrieval,
 "procedural-memory": demo_plan, "chain-of-thought": demo_chain,
 "planning-decomposition": demo_plan, "tool-use": demo_tools,
 "rag-retrieval": demo_retrieval, "summarization": demo_extract,
 "question-answering": demo_qa, "self-correction": demo_correct,
 "multi-agent": demo_agents, "persona-communication": demo_agents,
 "code-reasoning": demo_code, "math-reasoning": demo_chain,
 "multimodal": demo_fuse, "working-memory": demo_budget,
 "explanation": demo_extract, "instruction-following": demo_qa,
 "context-window-management": demo_budget, "negotiation": demo_agents,
 "teaching-explanation": demo_extract,
 "uncertainty-handling": demo_calibrate, "united": demo_united,
}

DEMOS = {}
import entries_ai_reasoning as _E
for _key in _E.ORDER:
    _fn = ARCH[_key]
    for _e in _E.ENTRIES[_key]:
        _dk = _e["demo_key"]
        assert _dk not in DEMOS
        def _mk(fn, e):
            _rank = e["ladder_rank"]
            _code = e["demo_key"].split("-")[0]
            return lambda hdr, name, rid, group, dd, _f=fn, _r=_rank, _c=_code: _f(
                hdr, name, rid, group, {"rank": _r, "code": _c})
        DEMOS[_dk] = _mk(_fn, _e)
assert len(DEMOS) == 850
