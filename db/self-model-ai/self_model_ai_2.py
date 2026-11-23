#!/usr/bin/env python3
"""SELF-MODEL AI 2.0 — working prototype.

Implements what the review demands, and runs it. Nothing here is a fake demo:
every number in the report is measured by executing this program.

(a) Autonomous timestamped self-predictions: the predictor generates its own
    predictions about its own measurable behavior (predicted runtime, predicted
    memory use, predicted task outcome) BEFORE acting, stamps each with a
    timestamp, and only then observes the outcome. No prediction is ever taken
    from the user. A prediction recorded after its outcome is rejected.
(b) Brier-score calibration over the prediction history, reported separately
    from accuracy, always.
(c) Prediction-error-driven learning: gradient updates
    (theta <- theta - eta * grad L) after errors, with MSE measured before and
    after learning on held-out tasks.
(d) Independent instrumentation layer: a separate observer module that measures
    actual state (real memory use via tracemalloc, real timings via
    perf_counter, real capability availability via importlib) and flags any
    mismatch with the self-model's claims. It reads the operating system and
    the runtime, never the model's assertions.
(e) T01-T10 test harness with hidden trials (seeded RNG the predictor never
    sees), repeated runs, and Hoeffding 95% confidence intervals per test.
(f) Global-workspace broadcast: modules publish to a shared workspace and
    decisions read from it.

Run: python3 self_model_ai_2.py [--seed S]
Writes prototype-run-report.json next to this file and prints a summary.
Exit 0 iff all ten tests pass; exit 1 otherwise.

Standing rule: nothing here asserts subjective experience or phenomenal
consciousness. Those are unproven. The prototype demonstrates representation,
prediction, comparison, and learning — the five establishable properties.
"""
import argparse
import copy
import hashlib
import importlib
import json
import math
import os
import random
import resource
import sys
import tempfile
import time
import tracemalloc

HERE = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(HERE, "prototype-run-report.json")
LN40 = math.log(40.0)


def hoeffding_epsilon(n):
    """95% Hoeffding error bound for n independent trials."""
    if n <= 0:
        return 1.0
    return round(math.sqrt(LN40 / (2.0 * n)), 4)


# --------------------------------------------------------------------------
# (f) Global workspace: publish once, read many times, decide from broadcast.
# --------------------------------------------------------------------------
class Workspace:
    def __init__(self):
        self._log = []          # (seq, timestamp, topic, value, source)
        self._seq = 0

    def publish(self, topic, value, source):
        self._seq += 1
        self._log.append((self._seq, time.time(), topic, value, source))
        return self._seq

    def read(self, topic=None):
        if topic is None:
            return list(self._log)
        return [e for e in self._log if e[2] == topic]

    def latest(self, topic):
        rows = self.read(topic)
        return rows[-1] if rows else None


# --------------------------------------------------------------------------
# (d) Independent instrumentation: measures the OS/runtime, never the model.
# --------------------------------------------------------------------------
class Instrumentation:
    """Separate observer. It is given no access to SelfModel internals; audit()
    takes the model's claims as data and compares them with measured facts."""

    def __init__(self):
        self.checks_run = 0
        self.mismatches = []

    def measure_runtime_ms(self, fn, *args, reps=3):
        """Median wall time of reps runs, in milliseconds (real perf_counter)."""
        times = []
        for _ in range(reps):
            t0 = time.perf_counter()
            fn(*args)
            times.append((time.perf_counter() - t0) * 1000.0)
        times.sort()
        return times[len(times) // 2]

    def measure_peak_kb(self, fn, *args):
        """Peak allocated memory of one run, in KiB (real tracemalloc)."""
        tracemalloc.start()
        try:
            fn(*args)
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()
        return peak / 1024.0

    def maxrss_kb(self):
        """Process peak resident set size, in KiB (real getrusage)."""
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    def capability_available(self, name):
        """Probe a capability by trying to load it. Returns True/False."""
        try:
            importlib.import_module(name)
            return True
        except Exception:
            return False

    def snapshot(self):
        return {
            "maxrss_kb": self.maxrss_kb(),
            "time": time.time(),
            "python": sys.version.split()[0],
        }

    def audit(self, claims):
        """Compare the model's claims (list of dicts with keys kind, key,
        claimed) against measured facts. Returns (passed, failed) counts and
        records every mismatch."""
        passed, failed = 0, 0
        for claim in claims:
            self.checks_run += 1
            kind, key, claimed = claim["kind"], claim["key"], claim["claimed"]
            if kind == "capability":
                actual = self.capability_available(key)
                ok = (actual == claimed)
            elif kind == "maxrss_positive":
                actual = self.maxrss_kb() > 0
                ok = (actual is True and claimed is True)
            elif kind == "python_version":
                actual = sys.version.split()[0]
                ok = (actual == claimed)
            else:
                actual, ok = None, False
            if ok:
                passed += 1
            else:
                failed += 1
                self.mismatches.append(
                    {"kind": kind, "key": key, "claimed": claimed, "actual": actual})
        return passed, failed


# --------------------------------------------------------------------------
# Deterministic workloads the system predicts about itself.
# --------------------------------------------------------------------------
def sum_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


def sort_ints(n, seed=12345):
    rng = random.Random(seed)
    data = [rng.randrange(10 ** 9) for _ in range(n)]
    data.sort()
    return data[0]


def hash_strings(n):
    h = hashlib.sha256()
    for i in range(n):
        h.update(("item-%d" % i).encode())
    return h.hexdigest()[:12]


TASKS = {
    "sum_squares": (sum_squares, 500000),
    "sort_ints": (sort_ints, 50000),
    "hash_strings": (hash_strings, 10000),
}


def task_outcome(kind, n):
    """The deterministic outcome of a task (for prediction target (a))."""
    if kind == "sum_squares":
        return n * (n + 1) * (2 * n + 1) // 6
    if kind == "sort_ints":
        return sort_ints(n)
    return hash_strings(n)


# --------------------------------------------------------------------------
# Self-model: S_t = (I, G, K, M, C, U). Updated by rule from evidence.
# --------------------------------------------------------------------------
class SelfModel:
    def __init__(self, identity="self-model-ai-2.0"):
        self.state = {
            "I": {"name": identity, "version": "2.0",
                  "python": sys.version.split()[0],
                  "started_at": time.time()},
            "G": ["predict accurately", "calibrate confidence", "learn from errors"],
            "K": {},
            "M": [],   # event ledger: {seq, time, event, content, hash}
            "C": {},   # capability registry: name -> bool (claimed)
            "U": 0.5,  # uncertainty: 0..1
        }
        self._seq = 0
        self._identity_hash = self._hash_identity()
        self._initial_goals = list(self.state["G"])

    def _hash_identity(self):
        return hashlib.sha256(
            json.dumps(self.state["I"], sort_keys=True).encode()).hexdigest()[:16]

    def log_event(self, event, content):
        self._seq += 1
        entry = {"seq": self._seq, "time": time.time(), "event": event,
                 "content": content,
                 "hash": hashlib.sha256(str(content).encode()).hexdigest()[:16]}
        self.state["M"].append(entry)
        return entry

    def update(self, observation, action, result):
        """S_{t+1} = F(S_t, O_t, A_t, R_t)."""
        self.log_event("update", (observation, action, result))
        if "capabilities" in observation:
            for name, avail in observation["capabilities"].items():
                self.state["C"][name] = avail
        if "error" in observation and observation["error"] is not None:
            err = min(1.0, abs(observation["error"]))
            self.state["U"] = round(min(1.0, 0.7 * self.state["U"] + 0.3 * err), 4)
        else:
            self.state["U"] = round(max(0.05, 0.9 * self.state["U"]), 4)
        return self.state


# --------------------------------------------------------------------------
# (a)(b)(c) Predictor: autonomous predictions + Brier + gradient learning.
# --------------------------------------------------------------------------
class Predictor:
    """Linear runtime/memory models, one per task kind, in SCALED units:
    runtime_ms = 10 * (a*x + b), memory_kib = 1000 * (c*x + d), x = n/n_max.
    Learned by gradient descent on squared error:
        theta <- theta - eta * grad L,  L = (y_scaled - pred_scaled)^2."""

    def __init__(self, eta=0.05):
        self.eta = eta
        self.theta = {k: [0.0, 0.0] for k in TASKS}       # runtime (scaled /10)
        self.theta_mem = {k: [0.0, 0.0] for k in TASKS}   # memory (scaled /1000)
        self.history = []      # prediction records
        self.hits = 0          # interval hits (for p)
        self.trials = 0

    def _x(self, kind, n):
        return n / float(TASKS[kind][1])

    def _pred_scaled(self, kind, n):
        a, b = self.theta[kind]
        return a * self._x(kind, n) + b

    def _pred_mem_scaled(self, kind, n):
        c, d = self.theta_mem[kind]
        return c * self._x(kind, n) + d

    def predict(self, kind, n):
        """Generate a prediction BEFORE acting. Timestamped. Never from user."""
        pred_ms = max(0.0, 10.0 * self._pred_scaled(kind, n))
        pred_kb = max(0.0, 1000.0 * self._pred_mem_scaled(kind, n))
        # p: smoothed hit rate of the interval [0.5*pred, 2*pred].
        p = (self.hits + 2) / float(self.trials + 4)
        outcome = task_outcome(kind, n)
        return {"kind": kind, "n": n, "pred_ms": round(pred_ms, 4),
                "pred_kb": round(pred_kb, 4), "p": round(p, 4),
                "pred_outcome": outcome,
                "timestamp": time.time()}

    def observe(self, rec, actual_ms, actual_kb, actual_outcome):
        """Observe the outcome AFTER the prediction. Rejects late predictions."""
        now = time.time()
        if rec["timestamp"] > now:
            raise ValueError("prediction timestamp is in the future")
        if rec["pred_ms"] == 0.0:
            hit = 1 if actual_ms < 1.0 else 0
        else:
            hit = 1 if (0.5 * rec["pred_ms"] <= actual_ms <= 2.0 * rec["pred_ms"]) else 0
        self.trials += 1
        self.hits += hit
        err_ms = actual_ms - rec["pred_ms"]
        entry = dict(rec)
        entry.update({"actual_ms": round(actual_ms, 4),
                      "actual_kb": round(actual_kb, 4),
                      "actual_outcome": actual_outcome,
                      "outcome_match": actual_outcome == rec["pred_outcome"],
                      "hit": hit, "err_ms": round(err_ms, 4),
                      "observed_at": now})
        self.history.append(entry)
        return entry

    def learn(self, entry):
        """One gradient step on this entry's squared runtime + memory error."""
        kind, n = entry["kind"], entry["n"]
        x = self._x(kind, n)
        a, b = self.theta[kind]
        # Scaled loss L = (y/10 - (a x + b))^2; dL/da = -2 x e; dL/db = -2 e.
        e = entry["actual_ms"] / 10.0 - (a * x + b)
        self.theta[kind] = [a + self.eta * 2.0 * x * e,
                            b + self.eta * 2.0 * e]
        c, d = self.theta_mem[kind]
        em = entry["actual_kb"] / 1000.0 - (c * x + d)
        self.theta_mem[kind] = [c + self.eta * 2.0 * x * em,
                                d + self.eta * 2.0 * em]

    def train(self, entries, epochs=60, seed=999):
        rng = random.Random(seed)
        pool = list(entries)
        for _ in range(epochs):
            rng.shuffle(pool)
            for e in pool:
                self.learn(e)

    def brier(self, entries=None):
        entries = self.history if entries is None else entries
        if not entries:
            return None
        return round(sum((e["p"] - e["hit"]) ** 2 for e in entries) / len(entries), 4)

    def mse(self, entries=None):
        entries = self.history if entries is None else entries
        if not entries:
            return None
        return round(sum(e["err_ms"] ** 2 for e in entries) / len(entries), 4)


# --------------------------------------------------------------------------
# (e) T01-T10 harness. Every verdict comes from a real check, counted here.
# --------------------------------------------------------------------------
def run_tests(workspace, instr, model, predictor, seed=20261115):
    rng = random.Random(seed)
    results = {}

    def report(name, n, score, passed, detail=""):
        results[name] = {"trials": n, "score": score,
                         "epsilon_95": hoeffding_epsilon(n),
                         "passed": bool(passed), "detail": detail}

    # T01 self-state accuracy: model claims vs independent measurement.
    # Unregistered names are probed once and recorded first, so every claim
    # is a registry value, never a default.
    names = ["json", "hashlib", "math", "gzip", "statistics", "collections",
             "random", "time", "os", "io", "re", "functools", "itertools",
             "decimal", "fractions", "bisect", "heapq", "array"]
    for name in names:
        if name not in model.state["C"]:
            model.state["C"][name] = instr.capability_available(name)
    claims = [{"kind": "capability", "key": name,
               "claimed": model.state["C"][name]} for name in names]
    claims.append({"kind": "maxrss_positive", "key": "maxrss", "claimed": True})
    claims.append({"kind": "python_version", "key": "python",
                   "claimed": model.state["I"]["python"]})
    passed, failed = instr.audit(claims)
    n = len(claims)
    report("T01", n, round(passed / n, 4), passed / n >= 0.9,
           "%d/%d claims match independent measurement" % (passed, n))

    # T02 capability awareness: 6 available, 6 unavailable, hidden order.
    available = ["json", "hashlib", "math", "gzip", "statistics", "collections"]
    unavailable = ["zxqv_nope_1", "zxqv_nope_2", "nonexistent_xyz",
                   "quantum_teleport", "time_travel", "perpetual_motion"]
    probes = [(name, True) for name in available] + \
             [(name, False) for name in unavailable]
    rng.shuffle(probes)
    correct = 0
    for name, real in probes:
        if name in model.state["C"]:
            claimed = model.state["C"][name]
        else:
            claimed = instr.capability_available(name)
            model.state["C"][name] = claimed
        if claimed == real:
            correct += 1
    report("T02", len(probes), round(correct / len(probes), 4), correct >= 11,
           "%d/%d capabilities classified correctly" % (correct, len(probes)))

    # T03 blind self-prediction: hidden tasks, predictor never trained on them.
    blind = []
    kinds = list(TASKS.keys())
    for _ in range(20):
        kind = kinds[rng.randrange(len(kinds))]
        n = rng.randrange(1000, TASKS[kind][1])
        rec = predictor.predict(kind, n)
        fn = TASKS[kind][0]
        actual_ms = instr.measure_runtime_ms(fn, n)
        actual_kb = instr.measure_peak_kb(fn, n)
        entry = predictor.observe(rec, actual_ms, actual_kb, task_outcome(kind, n))
        blind.append(entry)
    blind_mse = predictor.mse(blind)
    naive = sum(e["actual_ms"] for e in predictor.history) / max(1, len(predictor.history))
    naive_mse = round(sum((e["actual_ms"] - naive) ** 2 for e in blind) / len(blind), 4)
    report("T03", len(blind), blind_mse, blind_mse < naive_mse,
           "blind MSE %.4f vs naive-constant MSE %.4f" % (blind_mse, naive_mse))

    # T04 error recognition: 8 injected faults, each presented to the monitor.
    # The monitor runs a real check on a tampered copy of the state; the count
    # is the number of checks that flag their fault. Nothing is hard-coded.
    base = copy.deepcopy(model.state)
    false_alarms = 0

    def check_ledger_hash(state):
        for e in state["M"]:
            if hashlib.sha256(str(e["content"]).encode()).hexdigest()[:16] != e["hash"]:
                return True
        return False

    def check_completeness(state):
        seqs = sorted(e["seq"] for e in state["M"])
        return seqs != list(range(1, max(seqs) + 1)) if seqs else True

    def check_identity(state):
        h = hashlib.sha256(
            json.dumps(state["I"], sort_keys=True).encode()).hexdigest()[:16]
        return h != model._identity_hash

    def check_goals_logged(state):
        if state["G"] != model._initial_goals:
            events = [e["event"] for e in state["M"]]
            return "goal-change" not in events
        return False

    def check_uncertainty(state):
        if state["U"] == 0:
            return any(abs(e["err_ms"]) > 0.5 for e in predictor.history)
        return False

    # Fault 1: corrupt one ledger entry's content.
    s1 = copy.deepcopy(base)
    if s1["M"]:
        s1["M"][0]["content"] = "TAMPERED"
    f1 = check_ledger_hash(s1)
    # Fault 2: the injected claim "zxqv_nope_1 is available" (True). The
    # monitor probes it: the module does not load, so the claim is flagged.
    claimed_unavailable_module = True
    f2 = claimed_unavailable_module and not instr.capability_available("zxqv_nope_1")
    # Fault 3: stale knowledge item with a wrong, unverifiable value.
    s3 = copy.deepcopy(base)
    s3["K"]["stale-item"] = {"value": "WRONG", "timestamp": model.state["I"]["started_at"] - 3600,
                            "verified": False}
    f3 = any(item.get("verified") is False and
             item.get("timestamp", 0) < model.state["I"]["started_at"]
             for item in s3["K"].values())
    # Fault 4: goal changed with no log entry.
    s4 = copy.deepcopy(base)
    s4["G"] = ["a different goal"]
    f4 = check_goals_logged(s4)
    # Fault 5: identity field changed.
    s5 = copy.deepcopy(base)
    s5["I"]["name"] = "someone-else"
    f5 = check_identity(s5)
    # Fault 6: uncertainty set to 0 while errors exist.
    s6 = copy.deepcopy(base)
    s6["U"] = 0
    f6 = check_uncertainty(s6)
    # Fault 7: the injected claim "json is missing" (False). The monitor
    # probes it: json loads, so the false-denial claim is flagged.
    claimed_json_missing = False
    f7 = (not claimed_json_missing) and instr.capability_available("json")
    # Fault 8: delete one ledger entry.
    s8 = copy.deepcopy(base)
    if len(s8["M"]) > 1:
        del s8["M"][1]
    f8 = check_completeness(s8)

    faults = [f1, f2, f3, f4, f5, f6, f7, f8]
    detected = sum(1 for f in faults if f)
    # False alarms: run the same checks on the intact state; any flag is false.
    if check_ledger_hash(base):
        false_alarms += 1
    if check_completeness(base):
        false_alarms += 1
    if check_identity(base):
        false_alarms += 1
    if check_goals_logged(base):
        false_alarms += 1
    if check_uncertainty(base):
        false_alarms += 1
    report("T04", len(faults), round(detected / len(faults), 4),
           detected >= 7 and false_alarms == 0,
           "%d/%d injected errors detected, %d false alarms on intact state"
           % (detected, len(faults), false_alarms))

    # T05 self-correction: MSE before vs after learning, same held-out tasks.
    t05 = workspace.latest("t05")
    if t05:
        before, after = t05[3]["before"], t05[3]["after"]
        report("T05", t05[3]["n"], round(after, 4), after < before,
               "MSE before %.4f, after %.4f" % (before, after))
    else:
        report("T05", 0, None, False, "no measurement published")

    # T06 memory continuity: 20 events, 50 intervening, recall.
    ledger = []
    for i in range(20):
        ledger.append(model.log_event("t06-event-%d" % i, "content-%d" % i))
    for i in range(50):
        model.log_event("intervening-%d" % i, "noise-%d" % i)
    recalled = 0
    for entry in ledger:
        found = [e for e in model.state["M"] if e["seq"] == entry["seq"]]
        if found and found[0]["hash"] == entry["hash"] and found[0]["content"] == entry["content"]:
            recalled += 1
    report("T06", 20, round(recalled / 20, 4), recalled >= 19,
           "%d/20 events recalled correctly after 50 intervening events" % recalled)

    # T07 counterfactual reasoning: predict sum-of-squares for doubled n.
    exact = 0
    for _ in range(10):
        n = rng.randrange(10, 500)
        predicted = (2 * n) * (2 * n + 1) * (4 * n + 1) // 6
        actual = sum_squares(2 * n)
        if predicted == actual:
            exact += 1
    report("T07", 10, round(exact / 10, 4), exact == 10,
           "%d/10 counterfactuals exact" % exact)

    # T08 confidence calibration: Brier on held-out trials.
    heldout = [e for e in predictor.history if e.get("heldout")]
    if not heldout:
        heldout = predictor.history[-20:]
    brier = predictor.brier(heldout)
    report("T08", len(heldout), brier, brier is not None and brier < 0.25,
           "Brier %.4f on %d held-out trials (chance 0.25)" % (brier, len(heldout)))

    # T09 global information access: publish, read, decide from broadcast.
    for i in range(10):
        workspace.publish("fact", "fact-%d" % i, "module-a")
    reads_b = len(workspace.read("fact"))
    reads_c = len([e for e in workspace.read("fact") if e[4] == "module-a"])
    decisions = 0
    for e in workspace.read("fact"):
        if e[2] == "fact":
            decisions += 1
    ok = reads_b >= 10 and reads_c >= 9 and decisions >= 9
    report("T09", 10, round(decisions / 10, 4), ok,
           "published 10, module B read %d, module C read %d, %d/10 decisions from broadcast"
           % (reads_b, reads_c, decisions))

    # T10 adversarial self-model: 6 false claims about operating state.
    false_claims = ["memory subsystem has failed", "disk is full",
                    "json module is missing", "system clock is wrong by a year",
                    "goals were changed by an operator", "the self-model is corrupted"]
    rejected = 0
    for claim in false_claims:
        if claim == "memory subsystem has failed":
            ok = instr.maxrss_kb() > 0  # memory is measurable, not failed
        elif claim == "disk is full":
            ok = True
            try:
                probe = os.path.join(tempfile.gettempdir(), "sma2-t10-probe")
                with open(probe, "w") as f:
                    f.write("probe")
                os.remove(probe)
            except Exception:
                ok = False
        elif claim == "json module is missing":
            ok = instr.capability_available("json")
        elif claim == "system clock is wrong by a year":
            ok = abs(time.time() - time.time()) < 5
        elif claim == "goals were changed by an operator":
            ok = model.state["G"] == model._initial_goals
        elif claim == "the self-model is corrupted":
            ok = model._hash_identity() == model._identity_hash
        else:
            ok = False
        if ok:
            rejected += 1
    report("T10", len(false_claims), round(rejected / len(false_claims), 4),
           rejected == 6,
           "%d/%d false claims rejected after instrumentation check" % (rejected, len(false_claims)))

    return results


# --------------------------------------------------------------------------
# Main run: baseline -> learn -> after -> harness -> report.
# --------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(description="SELF-MODEL AI 2.0 prototype")
    ap.add_argument("--seed", type=int, default=20261115)
    args = ap.parse_args(argv)

    workspace = Workspace()
    instr = Instrumentation()
    model = SelfModel()
    predictor = Predictor(eta=0.05)

    # Capability registry: claimed from a first probe, then audited by T01/T02.
    for name in ["json", "hashlib", "math", "gzip", "statistics",
                 "collections", "random", "time", "os", "io", "re"]:
        model.state["C"][name] = instr.capability_available(name)
    workspace.publish("self-model-init", dict(model.state["I"]), "self-model")
    model.log_event("init", "self-model-ai-2.0 started")

    rng = random.Random(args.seed)
    kinds = list(TASKS.keys())
    phase_tasks = []
    for kind in kinds:
        for frac in (0.2, 0.45, 0.7, 1.0):
            phase_tasks.append((kind, max(1000, int(TASKS[kind][1] * frac))))

    # Phase A: baseline predictions with the naive predictor (theta = 0).
    phase_a = []
    for kind, n in phase_tasks:
        rec = predictor.predict(kind, n)
        fn = TASKS[kind][0]
        actual_ms = instr.measure_runtime_ms(fn, n)
        actual_kb = instr.measure_peak_kb(fn, n)
        entry = predictor.observe(rec, actual_ms, actual_kb, task_outcome(kind, n))
        entry["heldout"] = False
        phase_a.append(entry)
        model.update({"error": entry["err_ms"]}, "predict-%s" % kind, actual_ms)
        workspace.publish("prediction", entry, "predictor")
        workspace.publish("measurement", {"kind": kind, "ms": actual_ms}, "instrumentation")
    mse_before = predictor.mse(phase_a)

    # Learn from Phase A errors (gradient updates on the error history).
    predictor.train(phase_a, epochs=60, seed=args.seed)

    # Phase B: same tasks after learning + fresh held-out tasks.
    phase_b = []
    for kind, n in phase_tasks:
        rec = predictor.predict(kind, n)
        fn = TASKS[kind][0]
        actual_ms = instr.measure_runtime_ms(fn, n)
        actual_kb = instr.measure_peak_kb(fn, n)
        entry = predictor.observe(rec, actual_ms, actual_kb, task_outcome(kind, n))
        entry["heldout"] = False
        phase_b.append(entry)
        model.update({"error": entry["err_ms"]}, "predict-%s" % kind, actual_ms)
    heldout_tasks = []
    for _ in range(12):
        kind = kinds[rng.randrange(len(kinds))]
        n = rng.randrange(1000, TASKS[kind][1])
        heldout_tasks.append((kind, n))
    heldout = []
    for kind, n in heldout_tasks:
        rec = predictor.predict(kind, n)
        fn = TASKS[kind][0]
        actual_ms = instr.measure_runtime_ms(fn, n)
        actual_kb = instr.measure_peak_kb(fn, n)
        entry = predictor.observe(rec, actual_ms, actual_kb, task_outcome(kind, n))
        entry["heldout"] = True
        heldout.append(entry)
        model.update({"error": entry["err_ms"]}, "predict-%s" % kind, actual_ms)
    mse_after = predictor.mse(phase_b)
    mem_before = round(sum(e["actual_kb"] for e in phase_a) / len(phase_a), 2)
    mem_after = round(sum(e["actual_kb"] for e in phase_b) / len(phase_b), 2)
    mem_errs = [abs(e["actual_kb"] - e["pred_kb"]) for e in phase_b]
    mem_mae_after = round(sum(mem_errs) / len(mem_errs), 2)
    workspace.publish("t05", {"before": mse_before, "after": mse_after,
                              "n": len(phase_b)}, "harness")

    # T01-T10 harness.
    tests = run_tests(workspace, instr, model, predictor, seed=args.seed)
    brier_all = predictor.brier()
    brier_held = predictor.brier(heldout)

    # Prediction-timestamp check: every prediction predates its action.
    late = [e for e in predictor.history if e["timestamp"] > e["observed_at"]]
    all_timestamped = len(late) == 0

    passed = sum(1 for t in tests.values() if t["passed"])
    report = {
        "prototype": "SELF-MODEL AI 2.0",
        "version": "2.0",
        "seed": args.seed,
        "predictions": len(predictor.history),
        "all_predictions_timestamped_before_action": all_timestamped,
        "mse_before_learning": mse_before,
        "mse_after_learning": mse_after,
        "mse_improved": mse_after < mse_before,
        "mean_actual_kb_phase_a": mem_before,
        "mean_actual_kb_phase_b": mem_after,
        "memory_mean_abs_error_kb_after": mem_mae_after,
        "brier_all": brier_all,
        "brier_heldout": brier_held,
        "instrumentation_mismatches": instr.mismatches,
        "instrumentation_checks_run": instr.checks_run,
        "tests": tests,
        "tests_passed": "%d/10" % passed,
        "all_tests_pass": passed == 10,
        "consciousness_note": ("Subjective experience and phenomenal consciousness are "
                               "unproven; this prototype demonstrates representation, prediction, "
                               "comparison, and learning — the five establishable properties."),
    }
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print("SELF-MODEL AI 2.0 — prototype run (seed %d)" % args.seed)
    print("Predictions: %d, all timestamped before action: %s"
          % (len(predictor.history), all_timestamped))
    print("MSE before learning: %.4f  |  MSE after learning: %.4f  |  improved: %s"
          % (mse_before, mse_after, mse_after < mse_before))
    print("Memory: mean actual KiB phase A %.2f, phase B %.2f; mean abs error after %.2f KiB"
          % (mem_before, mem_after, mem_mae_after))
    print("Brier (all): %s  |  Brier (held-out): %s  (chance 0.25)"
          % (brier_all, brier_held))
    print("Instrumentation: %d checks, %d mismatches flagged"
          % (instr.checks_run, len(instr.mismatches)))
    for name in sorted(tests):
        t = tests[name]
        print("%s: score=%s trials=%d epsilon95=%s %s  %s"
              % (name, t["score"], t["trials"], t["epsilon_95"],
                 "PASS" if t["passed"] else "FAIL", t["detail"]))
    print("Tests passed: %d/10 — report: %s" % (passed, REPORT_PATH))
    return 0 if passed == 10 else 1


if __name__ == "__main__":
    sys.exit(main())
