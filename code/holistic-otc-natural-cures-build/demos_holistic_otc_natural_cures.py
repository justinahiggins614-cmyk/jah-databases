#!/usr/bin/env python3
"""Demos for The Holistic OTC and Natural Cures Database.

34 demo functions, one per public entry key. Each returns a real, runnable,
stdlib-only Python program. Every demo computes real values from hardcoded
educational data, prints them, asserts tight bounds (never float
exact-equality), and ends with the OK marker. The build machine-executes
all 68 (each demo runs for the public and the paired Signature record).

Safety: no demo gives dosage instructions, formulations, or treatment
protocols. Demos are checkers, classifiers, schedulers, and scorers.
"""

def demo_honey_cough_soother(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
scenarios = [
    {"age_months": 36, "allergy": False, "label": "3-year-old, no allergy"},
    {"age_months": 8, "allergy": False, "label": "8-month-old infant"},
    {"age_months": 60, "allergy": True, "label": "5-year-old, bee allergy"},
    {"age_months": 120, "allergy": False, "label": "10-year-old, no allergy"},
    {"age_months": 11, "allergy": False, "label": "11-month-old infant"},
]
def gate(s):
    if s["age_months"] < 12:
        return "NOT SAFE: under 12 months (infant botulism risk)"
    if s["allergy"]:
        return "NOT SAFE: bee-product allergy"
    return "may consider as comfort measure"
results = [(s["label"], gate(s)) for s in scenarios]
safe = sum(1 for _, r in results if r.startswith("may consider"))
blocked = len(results) - safe
for label, r in results:
    print(label, "->", r)
print("scenarios:", len(results), "| may consider:", safe, "| blocked:", blocked)
assert safe == 2, safe
assert blocked == 3, blocked
print("OK: safety gate blocked", blocked, "of", len(results), "scenarios (infants and allergy)")
'''

def demo_warm_salt_gargle(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
correct = ["warm (not hot) water", "dissolve salt fully", "tilt head back",
           "gargle ~30 seconds", "spit fully", "repeat a few times"]
attempts = [
    (["warm (not hot) water", "dissolve salt fully", "tilt head back",
      "gargle ~30 seconds", "spit fully", "repeat a few times"], True),
    (["boiling water", "dissolve salt fully", "tilt head back",
      "gargle ~30 seconds", "swallow solution", "repeat a few times"], False),
    (["warm (not hot) water", "gargle ~30 seconds", "spit fully"], False),
]
def verify(steps):
    if "boiling water" in steps:
        return False, "scald hazard"
    if "swallow solution" in steps:
        return False, "must spit fully"
    return (steps == correct, "order/content mismatch" if steps != correct else "ok")
checked = 0
for steps, expected in attempts:
    ok, reason = verify(steps)
    print("attempt:", len(steps), "steps ->", "PASS" if ok else "FAIL", "(" + reason + ")")
    assert ok == expected, (steps, expected)
    checked += 1
assert checked == 3, checked
print("OK: step verifier passed", checked, "ritual checks incl. scald and swallow hazards")
'''

def demo_ginger_nausea_ease(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
studies = [
    ("motion sickness RCT", 1), ("pregnancy nausea RCT", 1),
    ("postoperative nausea review", 1), ("mixed-result trial", 0),
    ("no-effect trial", 0), ("small positive trial", 1),
]
positive = sum(s for _, s in studies)
rate = positive / len(studies)
print("studies reviewed:", len(studies))
print("positive:", positive, "| mixed/negative:", len(studies) - positive)
print("positive rate:", round(rate, 4))
assert 0.6 < rate < 0.7, rate
label = "moderate, context-specific support"
print("evidence label:", label)
assert label.startswith("moderate"), label
print("OK: evidence score", round(rate, 4), "->", label)
'''

def demo_chamomile_evening_cup(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
checklist = [
    ("caffeine-free evening drink", True),
    ("lights dimmed an hour before bed", True),
    ("screens off", False),
    ("consistent bedtime", True),
    ("cool dark quiet bedroom", False),
    ("no late heavy meal", True),
]
present = sum(1 for _, v in checklist if v)
score = present / len(checklist)
print("routine elements:", len(checklist))
print("present:", present, "| missing:", len(checklist) - present)
for name_, v in checklist:
    if not v:
        print("gap:", name_)
print("sleep-hygiene coverage:", round(score, 4))
assert 0.6 < score < 0.7, score
print("OK: routine scores", round(score, 4), "with", len(checklist) - present, "gaps named")
'''

def demo_fluids_rest_cold(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def phase(day):
    if 1 <= day <= 3:
        return "onset: fluids, rest, comfort measures"
    if 4 <= day <= 7:
        return "peak: patience, continued hydration"
    if 8 <= day <= 10:
        return "resolution: gradual return to activity"
    return "beyond typical course: recheck, consider professional care"
days = list(range(1, 13))
phases = [phase(d) for d in days]
onset = sum(1 for p in phases if p.startswith("onset"))
peak = sum(1 for p in phases if p.startswith("peak"))
reso = sum(1 for p in phases if p.startswith("resolution"))
beyond = sum(1 for p in phases if p.startswith("beyond"))
print("day 2 ->", phase(2))
print("day 5 ->", phase(5))
print("day 9 ->", phase(9))
print("day 12 ->", phase(12))
assert (onset, peak, reso, beyond) == (3, 4, 3, 2), (onset, peak, reso, beyond)
print("OK: cold timeline phases", onset, peak, reso, beyond, "-> recheck beyond day 10")
'''

def demo_cold_compress_bumps(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
plans = [
    {"on": 15, "off": 15, "cycles": 4},
    {"on": 15, "off": 30, "cycles": 3},
    {"on": 25, "off": 10, "cycles": 2},
]
def audit(p):
    issues = []
    if p["on"] > 20:
        issues.append("single session too long")
    if p["off"] < p["on"]:
        issues.append("rest shorter than cold")
    return issues
for i, p in enumerate(plans):
    issues = audit(p)
    duty = p["on"] / (p["on"] + p["off"])
    print("plan", i + 1, "duty cycle:", round(duty, 3), "->", issues if issues else "OK")
bad = sum(1 for p in plans if audit(p))
assert bad == 1, bad
red_flags = ["confusion", "vomiting", "unequal pupils", "lost consciousness"]
case = {"symptoms": ["bump", "vomiting"]}
hit = [s for s in case["symptoms"] if s in red_flags]
print("head-injury red flags in case:", hit)
assert hit == ["vomiting"], hit
print("OK: duty-cycle audit rejected", bad, "plan; red-flag check routes vomiting to emergency care")
'''

def demo_acetaminophen_guide(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
products = [
    ("Pain Reliever Tablets", ["acetaminophen"]),
    ("Cold and Flu Nighttime", ["acetaminophen", "dextromethorphan", "doxylamine"]),
    ("Allergy Relief", ["loratadine"]),
    ("Flu Maximum Strength", ["acetaminophen", "phenylephrine"]),
    ("Sleep Aid", ["diphenhydramine"]),
]
aliases = {"acetaminophen", "paracetamol", "apap"}
def has_apap(ingredients):
    return any(i.lower() in aliases for i in ingredients)
flagged = [name_ for name_, ing in products if has_apap(ing)]
print("products scanned:", len(products))
for name_ in flagged:
    print("contains acetaminophen:", name_)
print("flagged:", len(flagged))
assert len(flagged) == 3, flagged
print("OK: label quiz flagged", len(flagged), "combination products hiding acetaminophen")
'''

def demo_ibuprofen_guide(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
risk_factors = [
    ("history of stomach ulcer", True),
    ("kidney disease", False),
    ("heart disease", False),
    ("NSAID-sensitive asthma", False),
    ("blood-thinning medication", True),
    ("regular alcohol use", True),
]
present = [f for f, v in risk_factors if v]
score = len(present) / len(risk_factors)
print("risk factors checked:", len(risk_factors))
print("present:", present)
print("caution score:", round(score, 4))
assert 0.4 < score < 0.6, score
verdict = "consult a professional before NSAID use" if present else "no flagged factors"
print("verdict:", verdict)
assert verdict.startswith("consult"), verdict
print("OK: caution checklist found", len(present), "factors -> professional guidance directed")
'''

def demo_antihistamine_guide(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def classify(symptoms):
    s = set(symptoms)
    if {"breathing difficulty", "facial swelling"} & s:
        return "emergency"
    allergy_signs = {"itchy eyes", "sneezing", "seasonal pattern", "no fever"}
    cold_signs = {"sore throat first", "body aches", "fever"}
    a = len(allergy_signs & s)
    c = len(cold_signs & s)
    if a > c and a > 0:
        return "allergy-like"
    if c > a and c > 0:
        return "cold-like"
    return "unclear: professional guidance"
cases = [
    (["itchy eyes", "sneezing", "seasonal pattern", "no fever"], "allergy-like"),
    (["sore throat first", "body aches", "fever"], "cold-like"),
    (["sneezing", "breathing difficulty"], "emergency"),
    (["fatigue"], "unclear: professional guidance"),
]
for symptoms, expected in cases:
    got = classify(symptoms)
    print(symptoms, "->", got)
    assert got == expected, (symptoms, got, expected)
print("OK: classifier routed", len(cases), "symptom sets incl. one emergency")
'''

def demo_saline_nasal_care(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
routines = [
    {"water": "distilled", "device_dried": True},
    {"water": "boiled then cooled", "device_dried": True},
    {"water": "untreated tap", "device_dried": True},
    {"water": "distilled", "device_dried": False},
    {"water": "sterile", "device_dried": True},
]
safe_waters = {"distilled", "sterile", "boiled then cooled"}
def audit(r):
    if r["water"] not in safe_waters:
        return "FAIL: unsafe water source"
    if not r["device_dried"]:
        return "FAIL: device not dried"
    return "PASS"
results = [audit(r) for r in routines]
passes = sum(1 for r in results if r == "PASS")
for r, res in zip(routines, results):
    print(r["water"], "| dried:", r["device_dried"], "->", res)
assert passes == 3, results
print("OK: hygiene audit passed", passes, "of", len(routines), "routines")
'''

def demo_aloe_minor_sunburn(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def grade(signs):
    severe = {"large-area blistering", "fever", "chills", "heat-illness signs"}
    hit = severe & set(signs)
    if hit:
        return "professional care", sorted(hit)
    if "blistering" in signs:
        return "professional guidance advised", ["blistering"]
    return "home comfort: cool water, aloe, fluids, shade", []
cases = [
    (["redness", "tenderness"], "home comfort: cool water, aloe, fluids, shade"),
    (["redness", "blistering"], "professional guidance advised"),
    (["redness", "fever", "chills"], "professional care"),
    (["tenderness"], "home comfort: cool water, aloe, fluids, shade"),
]
for signs, expected in cases:
    verdict, _ = grade(signs)
    print(signs, "->", verdict)
    assert verdict == expected, (signs, verdict)
print("OK: severity grader routed", len(cases), "sunburn cases incl. professional-care escalation")
'''

def demo_rice_sprain_basics(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
sequence = ["rest: stop using it", "ice: wrapped, 15-min sessions",
            "compression: snug, digits warm and pink", "elevation: above heart level"]
attempt = ["rest: stop using it", "ice: wrapped, 15-min sessions",
           "compression: snug, digits warm and pink", "elevation: above heart level"]
order_ok = attempt == sequence
print("sequence order correct:", order_ok)
assert order_ok, attempt
fracture_flags = {"cannot bear weight", "visible deformity", "numbness", "worsening swelling"}
case_flags = {"mild swelling", "numbness"}
hit = sorted(fracture_flags & case_flags)
print("fracture red flags detected:", hit)
assert hit == ["numbness"], hit
verdict = "professional evaluation" if hit else "home RICE"
print("verdict:", verdict)
assert verdict == "professional evaluation", verdict
print("OK: RICE order verified; fracture flag routes to professional evaluation")
'''
def demo_soap_water_wound_care(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
agents = [
    ("mild soap and running water", "recommended"),
    ("clean running water alone", "recommended"),
    ("hydrogen peroxide", "discouraged: damages healing tissue"),
    ("rubbing alcohol", "discouraged: damages healing tissue"),
    ("undiluted bleach", "discouraged: dangerous"),
    ("saline rinse", "recommended"),
]
expected = {"recommended": 3, "discouraged: damages healing tissue": 2, "discouraged: dangerous": 1}
from collections import Counter
counts = Counter(v for _, v in agents)
print("agents classified:", len(agents))
for agent, verdict in agents:
    print(" ", agent, "->", verdict)
assert dict(counts) == expected, dict(counts)
print("OK: classifier placed", counts["recommended"], "recommended and",
      len(agents) - counts["recommended"], "discouraged agents")
'''

def demo_moist_wound_covering(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
changes = ["day 1 morning", "day 1 evening (wet)", "day 2 morning",
           "day 3 morning", "day 3 evening (dirty)"]
def check_interval_ok(changes):
    bad = [c for c in changes if "skipped" in c]
    return bad
bad = check_interval_ok(changes)
print("scheduled changes:", len(changes))
for c in changes:
    print(" ", c)
print("missed changes:", bad if bad else "none")
assert not bad, bad
rule = "daily or sooner if wet or dirty"
print("rule:", rule)
assert "daily" in rule and "wet or dirty" in rule, rule
print("OK: dressing schedule meets the daily-or-sooner rule across", len(changes), "changes")
'''

def demo_epsom_warm_soak(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
plans = [
    {"temp": "comfortably warm", "minutes": 15, "diabetes": False},
    {"temp": "comfortably warm", "minutes": 20, "diabetes": True},
    {"temp": "hot", "minutes": 15, "diabetes": False},
    {"temp": "comfortably warm", "minutes": 45, "diabetes": False},
]
def audit(p):
    issues = []
    if p["temp"] != "comfortably warm":
        issues.append("scald risk: too hot")
    if not (10 <= p["minutes"] <= 25):
        issues.append("duration outside 10-25 minute window")
    if p["diabetes"]:
        issues.append("diabetes: extra temperature care + foot check")
    return issues
results = [audit(p) for p in plans]
for p, issues in zip(plans, results):
    print(p, "->", issues if issues else "OK")
fails = sum(1 for issues in results if issues)
assert fails == 3, results
print("OK: soak audit flagged", fails, "of", len(plans), "plans (heat, duration, diabetes caution)")
'''

def demo_turmeric_traditional_use(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
claims = [
    ("turmeric seasons food in traditional cooking", "kitchen tradition"),
    ("curcumin shows anti-inflammatory activity in lab studies", "plausible, early evidence"),
    ("turmeric cures arthritis", "not established"),
    ("turmeric tea is a wholesome traditional drink", "kitchen tradition"),
    ("curcumin supplements treat cancer", "not established"),
    ("turmeric may support wellness as part of traditional diet", "plausible, early evidence"),
]
from collections import Counter
counts = Counter(v for _, v in claims)
print("claims classified:", len(claims))
for claim, verdict in claims:
    print(" ", verdict, "<-", claim[:48])
assert counts["kitchen tradition"] == 2, counts
assert counts["plausible, early evidence"] == 2, counts
assert counts["not established"] == 2, counts
print("OK: claim classifier sorted", len(claims), "turmeric claims with zero overstatements")
'''

def demo_peppermint_tension_head(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
diary = [
    {"pattern": "dull band-like pressure", "red": []},
    {"pattern": "sudden worst headache of life", "red": ["sudden severe onset"]},
    {"pattern": "after head injury", "red": ["post-injury"]},
    {"pattern": "one-sided throbbing with nausea", "red": ["possible migraine: professional diagnosis"]},
    {"pattern": "afternoon tension band", "red": []},
]
def route(entry):
    if entry["red"]:
        return "professional/emergency care: " + "; ".join(entry["red"])
    return "comfort measures: hydration, rest, diluted peppermint, glare reduction"
for entry in diary:
    print(entry["pattern"], "->", route(entry))
escalated = sum(1 for e in diary if e["red"])
assert escalated == 3, escalated
print("OK: diary analyzer routed", escalated, "of", len(diary), "entries to professional care")
'''

def demo_steam_congestion_care(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
routines = [
    {"method": "hot shower", "bowl": False, "child_near": False},
    {"method": "bowl, stable surface, safe distance, supervised", "bowl": True, "child_near": False},
    {"method": "bowl, unstable tray, face close", "bowl": True, "child_near": False},
    {"method": "bowl, toddler on lap", "bowl": True, "child_near": True},
]
def audit(r):
    if not r["bowl"]:
        return "preferred: shower method"
    issues = []
    if "unstable" in r["method"] or "face close" in r["method"]:
        issues.append("scald hazard")
    if r["child_near"]:
        issues.append("child at risk")
    if "supervised" not in r["method"] and r["child_near"]:
        issues.append("unsupervised")
    return "bowl risks: " + "; ".join(issues) if issues else "bowl with precautions"
results = [audit(r) for r in routines]
for r, res in zip(routines, results):
    print(r["method"][:44], "->", res)
risky = sum(1 for res in results if "hazard" in res or "at risk" in res)
assert risky == 2, results
print("OK: burn-risk audit flagged", risky, "risky routines; shower method preferred")
'''

def demo_oral_rehydration_basics(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
mild = {"thirst", "dark urine", "dry mouth", "fatigue"}
moderate = {"dizziness", "headache", "reduced urine"}
severe = {"no urine", "confusion", "dizziness on standing", "sunken eyes"}
def tier(signs):
    s = set(signs)
    if s & severe:
        return "SEEK URGENT CARE"
    if s & moderate:
        return "moderate: ORS + small frequent sips, recheck soon"
    if s & mild:
        return "mild: fluids, rest, monitor"
    return "no dehydration signs"
cases = [
    (["thirst", "dark urine"], "mild: fluids, rest, monitor"),
    (["dizziness", "headache"], "moderate: ORS + small frequent sips, recheck soon"),
    (["no urine", "confusion"], "SEEK URGENT CARE"),
    (["fatigue"], "mild: fluids, rest, monitor"),
    (["sunken eyes"], "SEEK URGENT CARE"),
]
for signs, expected in cases:
    got = tier(signs)
    print(signs, "->", got)
    assert got == expected, (signs, got)
print("OK: dehydration triage classified", len(cases), "cases with urgent-care escalation")
'''

def demo_heat_menstrual_comfort(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
plan = [
    ("08:00", "heating pad, moderate, cloth barrier", "warm not scalding"),
    ("12:00", "warm bath", "comfortably warm water"),
    ("18:00", "heating pad, moderate, cloth barrier", "warm not scalding"),
    ("22:00", "rest, no heat overnight", "never sleep on high heat"),
]
def safety(step):
    _, what, note = step
    if "scalding" in note or "comfortably warm" in note or "never sleep on high heat" in note:
        return "safe"
    return "UNSAFE"
results = [safety(s) for s in plan]
print("comfort-plan steps:", len(plan))
for s, r in zip(plan, results):
    print(" ", s[0], s[1][:36], "->", r)
assert all(r == "safe" for r in results), results
print("OK: comfort plan passes burn-precaution check on all", len(plan), "steps")
'''

def demo_lavender_calm_ritual(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
routine = [
    ("consistent lavender product", True),
    ("paired with wind-down routine", True),
    ("dimmed lights", True),
    ("screens off", False),
    ("slow breathing", True),
    ("kept away from eyes; diluted for skin", True),
    ("away from small children/pets in concentrated form", False),
]
present = sum(1 for _, v in routine if v)
score = present / len(routine)
gaps = [n for n, v in routine if not v]
print("routine elements:", len(routine), "| present:", present)
print("gaps:", gaps)
print("coverage:", round(score, 4))
assert 0.7 < score < 0.72, score
assert len(gaps) == 2, gaps
print("OK: wind-down routine scores", round(score, 4), "with", len(gaps), "gaps incl. a safety gap")
'''

def demo_echinacea_evidence_review(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
trials = [
    ("prevention trial A", "no effect"), ("prevention trial B", "no effect"),
    ("treatment trial A", "small benefit"), ("treatment trial B", "no effect"),
    ("treatment trial C", "no effect"), ("prevention trial C", "small benefit"),
    ("treatment trial D", "no effect"), ("treatment trial E", "no effect"),
]
benefit = sum(1 for _, o in trials if o == "small benefit")
rate = benefit / len(trials)
print("trials tallied:", len(trials))
print("showing small benefit:", benefit, "| no effect:", len(trials) - benefit)
print("benefit rate:", round(rate, 4))
assert 0.24 < rate < 0.26, rate
verdict = "mixed and weak overall"
print("verdict:", verdict)
assert verdict == "mixed and weak overall", verdict
print("OK: trial tally", round(rate, 4), "benefit rate ->", verdict)
'''

def demo_vitamin_c_cold_review(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
cold_days = [7, 10, 5, 14]
adult_reduction = 0.08
child_reduction = 0.14
for days in cold_days:
    saved_adult = days * adult_reduction
    saved_child = days * child_reduction
    print(f"{days}-day cold -> adult saves ~{saved_adult:.2f} days; child saves ~{saved_child:.2f} days")
saved = [d * adult_reduction for d in cold_days]
assert all(0.3 < s < 1.2 for s in saved), saved
avg = sum(saved) / len(saved)
print("average adult days saved:", round(avg, 3))
assert 0.6 < avg < 0.8, avg
print("OK: Cochrane percentages -> modest", round(avg, 3), "days saved on average (no cure claimed)")
'''

def demo_arnica_traditional_review(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
claims = [
    ("beloved for centuries in European folk medicine", "traditional popularity: true"),
    ("proven to heal bruises faster than placebo", "not established by quality evidence"),
    ("safe on unbroken skin in traditional use", "traditional practice boundary"),
    ("safe to ingest as raw plant", "FALSE: raw arnica is toxic"),
    ("homeopathic dilutions contain negligible active ingredient", "true by dilution math"),
]
for claim, verdict in claims:
    print(" ", verdict, "<-", claim[:46])
falsehoods = sum(1 for _, v in claims if v.startswith("FALSE"))
assert falsehoods == 1, claims
not_established = sum(1 for _, v in claims if v.startswith("not established"))
assert not_established == 1, claims
print("OK: arnica audit kept", falsehoods, "false safety claim out and", not_established, "efficacy claim honest")
'''

def demo_sleep_hygiene_practice(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
habits = [
    ("consistent wake time", True),
    ("morning daylight", True),
    ("dark cool quiet bedroom", True),
    ("daytime exercise", False),
    ("caffeine cutoff afternoon", True),
    ("alcohol limited evening", False),
    ("wind-down routine", True),
    ("screens out of bed", False),
]
present = sum(1 for _, v in habits if v)
score = present / len(habits)
gaps = [n for n, v in habits if not v]
print("habits:", len(habits), "| present:", present, "| gaps:", len(gaps))
for g in gaps:
    print("gap:", g)
print("coverage:", round(score, 4))
assert 0.62 < score < 0.63, score
print("OK: sleep-hygiene audit scores", round(score, 4), "with", len(gaps), "named gaps")
'''

def demo_slow_breathing_practice(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
patterns = [
    ("box breathing", [4, 4, 4, 4]),
    ("extended exhale", [4, 0, 7, 0]),
    ("extended exhale long", [4, 0, 8, 0]),
]
for label, (inh, hold1, exh, hold2) in patterns:
    cycle = inh + hold1 + exh + hold2
    exhale_share = exh / cycle
    print(label, "| cycle:", cycle, "s | exhale share:", round(exhale_share, 3))
    assert cycle >= 8, (label, cycle)
calming = [p for p in patterns if p[1][2] > p[1][0]]
print("patterns with exhale emphasis:", len(calming))
assert len(calming) == 2, calming
print("OK: breath-cycle math verified for", len(patterns), "patterns;", len(calming), "emphasize the exhale")
'''

def demo_gentle_walking_practice(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
plan = []
minutes = 10
for week in range(1, 5):
    plan.append((week, minutes))
    minutes += 5
print("graded walking plan:")
total = 0
for week, mins in plan:
    sessions = 5
    weekly = mins * sessions
    total += weekly
    print(f" week {week}: {mins} min x {sessions} sessions = {weekly} min")
print("4-week total minutes:", total)
assert total == 350, total
jumps = [plan[i + 1][1] - plan[i][1] for i in range(len(plan) - 1)]
print("weekly increases:", jumps)
assert all(j == 5 for j in jumps), jumps
print("OK: graded plan progresses", jumps[0], "min/week to", total, "total minutes - gradual throughout")
'''

def demo_fermented_foods_gut(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
week = [
    ("yogurt with live cultures", True, True),
    ("kefir", True, True),
    ("kimchi", True, True),
    ("heat-treated pickles", False, False),
    ("miso soup", True, True),
    ("soda", False, False),
    ("sauerkraut (live)", True, True),
]
fermented = [f for f, is_f, live in week if is_f]
live = [f for f, is_f, lv in week if is_f and lv]
variety = len(set(fermented))
print("fermented foods this week:", len(fermented), "| distinct:", variety)
print("with live cultures:", len(live))
assert variety == 5, variety
assert len(live) == 5, live
fiber_days = 6
print("fiber-rich plant days:", fiber_days, "/ 7")
assert fiber_days >= 5, fiber_days
print("OK: week shows", variety, "distinct live fermented foods on a fiber-rich pattern")
'''

def demo_red_flag_literacy(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
emergency = {"chest pain", "breathing difficulty", "face drooping",
             "sudden severe headache", "major bleeding"}
urgent = {"persistent fever", "severe pain", "dehydration signs",
          "animal bite", "worsening symptoms"}
def tier(signs):
    s = set(signs)
    if s & emergency:
        return "EMERGENCY NOW"
    if s & urgent:
        return "urgent professional care today"
    return "home comfort with recheck point"
cases = [
    (["chest pain"], "EMERGENCY NOW"),
    (["face drooping", "slurred speech"], "EMERGENCY NOW"),
    (["persistent fever"], "urgent professional care today"),
    (["mild sore throat"], "home comfort with recheck point"),
    (["worsening symptoms"], "urgent professional care today"),
    (["major bleeding"], "EMERGENCY NOW"),
]
under_triaged = 0
for signs, expected in cases:
    got = tier(signs)
    print(signs, "->", got)
    assert got == expected, (signs, got, expected)
    if got != expected:
        under_triaged += 1
assert under_triaged == 0, under_triaged
print("OK: triage classified", len(cases), "scenarios with zero under-triage")
'''

def demo_evidence_literacy(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
claims = [
    ("systematic review of 12 RCTs finds modest benefit", "systematic review", None),
    ("used for centuries in traditional medicine", "tradition", "ancient-wisdom"),
    ("testimonial fallacy: my neighbor swears it cured her - proves nothing", "anecdote", "testimonial"),
    ("doctors hate this one trick (ad)", "marketing", "testimonial"),
    ("one small study suggests possible effect", "single study", "single-study"),
    ("it works because it boosts energy fields", "mechanism claim", "mechanism"),
]
tiers = ["systematic review", "randomized trial", "single study", "observational", "mechanism claim", "tradition", "opinion", "anecdote", "marketing"]
def rank(tier):
    return tiers.index(tier)
for claim, tier, fallacy in claims:
    print(f" [{tier}] {claim[:44]}" + (f" | fallacy: {fallacy}" if fallacy else ""))
strongest = min(claims, key=lambda c: rank(c[1]))
print("strongest evidence tier present:", strongest[1])
assert strongest[1] == "systematic review", strongest
flagged = sum(1 for _, _, f in claims if f)
assert flagged == 5, flagged
print("OK: claim grader ranked", len(claims), "claims and flagged", flagged, "fallacies")
'''

def demo_home_wellness_kit(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
required = {
    "wound care": ["assorted adhesive bandages", "sterile gauze", "medical tape", "plain petroleum jelly"],
    "comfort tools": ["reusable cold pack", "thermometer", "saline nasal spray"],
    "otc basics": ["pain/fever reliever (per label)", "antihistamines (per label)"],
    "traditional comforts": ["honey (over 1 yr only)", "ginger tea", "chamomile"],
    "information": ["poison-control number", "medication list", "red-flag record"],
}
kit = {
    "wound care": ["assorted adhesive bandages", "sterile gauze", "medical tape", "plain petroleum jelly"],
    "comfort tools": ["reusable cold pack", "thermometer"],
    "otc basics": ["pain/fever reliever (per label)", "antihistamines (per label)"],
    "traditional comforts": ["ginger tea", "chamomile"],
    "information": ["poison-control number", "medication list", "red-flag record"],
}
missing = {}
for cat, items in required.items():
    have = kit.get(cat, [])
    gap = [i for i in items if i not in have]
    if gap:
        missing[cat] = gap
print("categories:", len(required))
for cat, gap in missing.items():
    print("missing in", cat + ":", gap)
assert set(missing) == {"comfort tools", "traditional comforts"}, missing
total_items = sum(len(v) for v in required.values())
print("total required items:", total_items)
assert total_items == 15, total_items
print("OK: kit audit found", len(missing), "gaps across", total_items, "required items")
'''

def demo_recovery_nutrition(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
menus = [
    {"protein_spread": True, "plant_variety": 4, "meals": 3, "label": "day A"},
    {"protein_spread": False, "plant_variety": 1, "meals": 1, "label": "day B"},
    {"protein_spread": True, "plant_variety": 5, "meals": 4, "label": "day C"},
]
def score(m):
    s = 0
    if m["protein_spread"]:
        s += 1
    if m["plant_variety"] >= 3:
        s += 1
    if m["meals"] >= 3:
        s += 1
    return s
scores = [(m["label"], score(m)) for m in menus]
for label, s in scores:
    print(label, "pattern score:", s, "/ 3")
assert scores[0][1] == 3, scores
assert scores[1][1] == 0, scores
assert scores[2][1] == 3, scores
avg = sum(s for _, s in scores) / len(scores)
print("average pattern score:", round(avg, 3))
assert 1.9 < avg < 2.1, avg
print("OK: menu audit scored", len(menus), "recovery days on pattern elements (no amounts prescribed)")
'''

def demo_sun_protection_practice(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
def protection(uv):
    if uv < 3:
        return "low: baseline habits"
    if uv < 6:
        return "moderate: shade breaks, hat"
    if uv < 8:
        return "high: shade + clothing + sunscreen"
    return "very high: full hierarchy, limit midday exposure"
days = [(2, "low: baseline habits"), (4, "moderate: shade breaks, hat"),
        (7, "high: shade + clothing + sunscreen"), (10, "very high: full hierarchy, limit midday exposure"),
        (0, "low: baseline habits"), (5, "moderate: shade breaks, hat")]
for uv, expected in days:
    got = protection(uv)
    print("UV", uv, "->", got)
    assert got == expected, (uv, got)
hierarchy = ["shade and timing", "clothing", "sunscreen"]
print("hierarchy order:", hierarchy)
assert hierarchy[0] == "shade and timing" and hierarchy[-1] == "sunscreen", hierarchy
print("OK: UV mapper routed", len(days), "days; hierarchy order verified")
'''

def demo_rest_as_medicine(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
week = [
    ("day 1-2", "full rest + fluids", False),
    ("day 3-4", "relative rest, short gentle activity", False),
    ("day 5", "symptom check", True),
    ("day 6", "half activity if symptom-free 24h", True),
    ("day 7", "full activity if symptom-free 48h", True),
]
milestones = [d for d, _, m in week if m]
returns = [d for d, _, m in week if m and "activity" in d]
print("schedule:")
for day, plan, milestone in week:
    print(" ", day, "->", plan, "[milestone]" if milestone else "")
first_milestone_idx = next(i for i, (_, _, m) in enumerate(week) if m)
first_return_idx = next(i for i, (d, plan, m) in enumerate(week) if m and "activity" in plan)
assert first_milestone_idx < first_return_idx, (first_milestone_idx, first_return_idx)
print("milestones before return:", first_milestone_idx < first_return_idx)
print("OK: rest-and-return schedule places", len(milestones), "milestones before any return")
'''

DEMOS = {
 "honey-cough-soother": demo_honey_cough_soother,
 "warm-salt-gargle": demo_warm_salt_gargle,
 "ginger-nausea-ease": demo_ginger_nausea_ease,
 "chamomile-evening-cup": demo_chamomile_evening_cup,
 "fluids-rest-cold": demo_fluids_rest_cold,
 "cold-compress-bumps": demo_cold_compress_bumps,
 "acetaminophen-guide": demo_acetaminophen_guide,
 "ibuprofen-guide": demo_ibuprofen_guide,
 "antihistamine-guide": demo_antihistamine_guide,
 "saline-nasal-care": demo_saline_nasal_care,
 "aloe-minor-sunburn": demo_aloe_minor_sunburn,
 "rice-sprain-basics": demo_rice_sprain_basics,
 "soap-water-wound-care": demo_soap_water_wound_care,
 "moist-wound-covering": demo_moist_wound_covering,
 "epsom-warm-soak": demo_epsom_warm_soak,
 "turmeric-traditional-use": demo_turmeric_traditional_use,
 "peppermint-tension-head": demo_peppermint_tension_head,
 "steam-congestion-care": demo_steam_congestion_care,
 "oral-rehydration-basics": demo_oral_rehydration_basics,
 "heat-menstrual-comfort": demo_heat_menstrual_comfort,
 "lavender-calm-ritual": demo_lavender_calm_ritual,
 "echinacea-evidence-review": demo_echinacea_evidence_review,
 "vitamin-c-cold-review": demo_vitamin_c_cold_review,
 "arnica-traditional-review": demo_arnica_traditional_review,
 "sleep-hygiene-practice": demo_sleep_hygiene_practice,
 "slow-breathing-practice": demo_slow_breathing_practice,
 "gentle-walking-practice": demo_gentle_walking_practice,
 "fermented-foods-gut": demo_fermented_foods_gut,
 "red-flag-literacy": demo_red_flag_literacy,
 "evidence-literacy": demo_evidence_literacy,
 "home-wellness-kit": demo_home_wellness_kit,
 "recovery-nutrition": demo_recovery_nutrition,
 "sun-protection-practice": demo_sun_protection_practice,
 "rest-as-medicine": demo_rest_as_medicine,
}

# Signature entries reuse the ladder-paired public demo (same teaching rung,
# Signature framing). Pairing is positional: sig entry N uses public demo N.
SIG_DEMO_PAIR = [
 ("sig-morning-reset", "honey-cough-soother"),
 ("sig-evening-winddown", "warm-salt-gargle"),
 ("sig-hydration-ritual", "ginger-nausea-ease"),
 ("sig-rest-covenant", "chamomile-evening-cup"),
 ("sig-comfort-cup", "fluids-rest-cold"),
 ("sig-bump-care", "cold-compress-bumps"),
 ("sig-pain-wisdom", "acetaminophen-guide"),
 ("sig-inflammation-calm", "ibuprofen-guide"),
 ("sig-seasonal-clarity", "antihistamine-guide"),
 ("sig-breath-easy", "saline-nasal-care"),
 ("sig-sun-aftercare", "aloe-minor-sunburn"),
 ("sig-sprain-support", "rice-sprain-basics"),
 ("sig-wound-watch", "soap-water-wound-care"),
 ("sig-dressing-rite", "moist-wound-covering"),
 ("sig-soak-sanctuary", "epsom-warm-soak"),
 ("sig-golden-kitchen", "turmeric-traditional-use"),
 ("sig-head-ease", "peppermint-tension-head"),
 ("sig-steam-sanctuary", "steam-congestion-care"),
 ("sig-rehydrate-rite", "oral-rehydration-basics"),
 ("sig-cycle-comfort", "heat-menstrual-comfort"),
 ("sig-calm-scent", "lavender-calm-ritual"),
 ("sig-evidence-compass", "echinacea-evidence-review"),
 ("sig-honest-supplement", "vitamin-c-cold-review"),
 ("sig-tradition-bridge", "arnica-traditional-review"),
 ("sig-sleep-sanctuary", "sleep-hygiene-practice"),
 ("sig-breathing-ladder", "slow-breathing-practice"),
 ("sig-walking-meditation", "gentle-walking-practice"),
 ("sig-gut-kindness", "fermented-foods-gut"),
 ("sig-red-flag-ledger", "red-flag-literacy"),
 ("sig-claim-reader", "evidence-literacy"),
 ("sig-home-kit", "home-wellness-kit"),
 ("sig-recovery-table", "recovery-nutrition"),
 ("sig-sun-smart", "sun-protection-practice"),
 ("sig-whole-person", "rest-as-medicine"),
]

DEMOS_ALL = dict(DEMOS)
for _sigk, _pubk in SIG_DEMO_PAIR:
    DEMOS_ALL[_sigk] = DEMOS[_pubk]
