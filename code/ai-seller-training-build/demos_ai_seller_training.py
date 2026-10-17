#!/usr/bin/env python3
"""Demos for the AI Seller Training Database.

34 demo functions, one per entry, each returning a real, runnable,
stdlib-only Python program. Every demo computes real values from
hardcoded training data, prints them, asserts tight bounds (never float
exact-equality), and ends with the OK marker. The build machine-executes
all 68 (each demo runs for the public and the Signature record).
"""

def demo_promise(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
pitches = [
    "Act now, this offer expires tonight and never returns.",
    "Our system delivers guaranteed results in thirty days.",
    "Honestly, our starter plan covers up to 10 users; beyond that you need growth.",
    "All of our competitors are running scams, trust only us.",
    "Free forever, no limits ever, no catch whatsoever.",
]
flags = ["expires tonight", "guaranteed", "scams", "no limits ever"]
found = sum(1 for p in pitches for f in flags if f in p.lower())
honest = sum(1 for p in pitches if p.startswith("Honestly"))
print("pitches audited:", len(pitches))
print("deception flags found:", found)
print("honest pitches:", honest)
assert 3 < found < 5, found
assert 0 < honest < 2, honest
print("OK: promise audit flagged", found, "deceptive pitches and kept", honest, "honest one")
'''

def demo_aida(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
pitch = ("Imagine cutting your reporting time in half. A recent study shows teams "
         "waste six hours weekly on manual reports. Picture yourself leaving on time "
         "every Friday while the numbers compile themselves. Reply to this message "
         "and I will set up your trial today.")
stages = {
    "attention": ["imagine", "stop"],
    "interest": ["study shows", "fact"],
    "desire": ["picture yourself", "enjoy"],
    "action": ["reply", "click", "sign up"],
}
hits = {s: sum(1 for k in ks if k in pitch.lower()) for s, ks in stages.items()}
covered = sum(1 for s in stages if hits[s] > 0)
coverage = covered / len(stages)
print("stage hits:", hits)
print("coverage:", round(coverage, 4))
assert 0.99 < coverage <= 1.0, coverage
print("OK: AIDA coverage", round(coverage, 4), "across", covered, "stages")
'''

def demo_fab(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
triples = [
    ("3,100 RPM motor", "cuts hardwood without bogging", "you finish each board in one pass"),
    ("12 Ah battery", "runs all day on one charge", "you never hunt for an outlet mid-job"),
    ("laser guide", "shows the cut line exactly", "your cuts come out straight the first time"),
    ("dust port", "captures 95 percent of dust", "you breathe easy and skip cleanup"),
    ("5-year warranty", "covers parts and labor", "you buy once and stop worrying"),
    ("tool-free chuck", "swaps bits in seconds", "you keep momentum instead of fumbling"),
]
benefit_first = sum(1 for _, _, b in triples if b.startswith("you"))
print("FAB triples:", len(triples))
print("benefit-led lines:", benefit_first)
assert 5 < benefit_first < 7, benefit_first
print("OK:", benefit_first, "of", len(triples), "triples speak in buyer outcomes")
'''

def demo_questions(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
questions = [
    ("Tell me about your current process", "open"),
    ("What happens when tickets pile up", "open"),
    ("How do you measure response time today", "open"),
    ("Why did you switch vendors last time", "open"),
    ("Walk me through a typical escalation", "open"),
    ("Describe the team handling this", "open"),
    ("Who signs off on purchases", "open"),
    ("What would solving this be worth", "open"),
    ("How urgent is this for you", "open"),
    ("Do you handle support in-house", "closed"),
    ("Is the budget approved already", "closed"),
    ("Which plan are you leaning toward", "closed"),
]
openers = ("tell", "what", "how", "why", "walk", "describe", "who")
def is_open(q):
    return q.lower().startswith(openers)
checked = sum(1 for q, lab in questions if (is_open(q) and lab == "open") or (not is_open(q) and lab == "closed"))
opens = sum(1 for q, _ in questions if is_open(q))
ratio = opens / len(questions)
print("classified correctly:", checked, "/", len(questions))
print("open-question ratio:", round(ratio, 4))
assert checked == len(questions), checked
assert 0.74 < ratio < 0.76, ratio
print("OK: question toolkit classified", checked, "questions, open ratio", round(ratio, 4))
'''

def demo_listening(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
buyer_words = {"vendor", "three", "days", "answer", "ticket", "production", "waits", "slow", "support"}
paraphrase_words = {"response", "time", "costing", "three", "days", "hurts", "slow"}
overlap = buyer_words & paraphrase_words
coverage = len(overlap) / len(buyer_words)
print("buyer content words:", len(buyer_words))
print("restated words:", sorted(overlap))
print("listening coverage:", round(coverage, 4))
assert 0.33 < coverage < 0.34, coverage
print("OK: paraphrase covers", round(coverage, 4), "of buyer content words")
'''

def demo_rapport(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
turns = [
    "Hi Ana, thanks for making time today.",
    "You mentioned the rollout slipped in March; I looked into that before our call.",
    "I will call you at 2 PM Thursday as promised.",
    "I do not know the answer on data residency yet; I will find out.",
    "As promised, here is the summary I said I would send.",
    "Remember you said uptime matters more than features; I kept that in mind.",
    "Our platform is simply the best choice here.",
    "Let me check the exact number rather than guess.",
    "I will have the security doc to you by Friday.",
    "Thanks again for the honest answers today.",
]
signals = ["i will call you at", "as promised", "i do not know", "remember you said"]
found = sum(1 for t in turns if any(s in t.lower() for s in signals))
print("turns:", len(turns))
print("trust signals:", found)
assert 3 < found < 5, found
print("OK:", found, "trust signals across", len(turns), "turns")
'''

def demo_needs(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
worksheet = {
    "situation": ["40-person support team", "two offices"],
    "problem": ["3-day ticket response", "no escalation path"],
    "cost": ["about 12k per month in churn"],
    "desired_outcome": ["same-day response by Q3"],
    "decision_process": ["CFO approves over 10k", "trial then committee"],
}
filled = sum(1 for facts in worksheet.values() if len(facts) > 0)
facts_total = sum(len(f) for f in worksheet.values())
print("columns filled:", filled, "/ 5")
print("buyer-sourced facts:", facts_total)
assert 4 < filled <= 5, filled
assert 7 < facts_total < 10, facts_total
print("OK: needs worksheet complete with", facts_total, "buyer-sourced facts")
'''

def demo_valueprop(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
sentence = "We help small clinics cut patient no-shows by half without hiring extra staff."
jargon = ["leverage", "synergy", "paradigm", "holistic", "disruptive", "bandwidth"]
words = sentence.replace(".", "").split()
jargon_hits = sum(1 for w in words if w.lower() in jargon)
print("sentence:", sentence)
print("word count:", len(words))
print("jargon hits:", jargon_hits)
assert 12 < len(words) < 14, len(words)
assert jargon_hits < 1, jargon_hits
print("OK: value proposition in", len(words), "plain words, zero jargon")
'''

def demo_bant(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
legs = {"budget": True, "authority": True, "need": True, "timeline": False}
score = sum(1 for v in legs.values() if v)
actions = {4: "advance", 3: "develop the weak leg", 2: "nurture", 1: "nurture", 0: "redirect"}
weak = [k for k, v in legs.items() if not v]
print("BANT legs:", legs)
print("score:", score, "/ 4")
print("weak leg:", weak)
print("next action:", actions[score])
assert 2 < score < 4, score
assert weak == ["timeline"], weak
print("OK: lead scores", score, "- next action:", actions[score])
'''

def demo_arc(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
expected = ["greet", "agenda", "discovery", "presentation", "objections", "close", "next_steps"]
transcript_stages = ["greet", "agenda", "discovery", "presentation", "objections", "close", "next_steps"]
in_order = sum(1 for a, b in zip(transcript_stages, expected) if a == b)
complete = len(transcript_stages) == len(expected) and in_order == len(expected)
print("stages run:", transcript_stages)
print("stages in order:", in_order, "/", len(expected))
assert 6 < in_order < 8, in_order
assert complete, "arc incomplete or reordered"
print("OK: full seven-stage arc run in order")
'''

def demo_trial(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
signals = ["warm", "lukewarm", "warm", "warm", "cold", "warm"]
warm = sum(1 for s in signals if s == "warm")
ready = warm >= 3
print("trial signals:", signals)
print("warm count:", warm)
print("ready to close:", ready)
assert 3 < warm < 5, warm
assert ready, "gate failed"
print("OK:", warm, "warm trials - close attempt permitted")
'''

def demo_followup(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
touches = [
    (1, "thank-you plus promised summary", True),
    (3, "relevant customer proof point", True),
    (7, "new angle tied to stated need", True),
    (14, "polite breakup note", True),
]
days = [d for d, _, _ in touches]
gaps = [b - a for a, b in zip(days, days[1:])]
valued = sum(1 for _, _, v in touches if v)
print("touch days:", days)
print("gaps:", gaps)
print("touches carrying value:", valued, "/", len(touches))
assert gaps == [2, 4, 7], gaps
assert valued == len(touches), valued
print("OK: 4-touch cadence, every touch carries value")
'''

def demo_spin(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
questions = [
    ("How many tickets do you handle monthly", "S"),
    ("Who handles after-hours escalations", "S"),
    ("Are you satisfied with the 3-day response", "P"),
    ("What happens when tickets wait", "P"),
    ("What does a day of downtime cost", "I"),
    ("How does slow response affect renewals", "I"),
    ("If response were same-day, what changes", "N"),
    ("How would faster response help the team", "N"),
]
buckets = {}
for _, b in questions:
    buckets[b] = buckets.get(b, 0) + 1
print("SPIN buckets:", buckets)
assert all(1 < buckets[k] < 3 for k in ("S", "P", "I", "N")), buckets
print("OK: balanced SPIN sequence, 2 questions per bucket")
'''

def demo_discovery_corpus(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
seller_questions = ["open", "open", "open", "closed", "open", "open", "closed", "open", "open", "closed"]
paraphrases = 3
turns = 30
opens = sum(1 for q in seller_questions if q == "open")
ratio = opens / len(seller_questions)
print("seller question turns:", len(seller_questions))
print("open-question ratio:", round(ratio, 4))
print("paraphrases:", paraphrases, "in", turns, "turns")
assert 0.69 < ratio < 0.71, ratio
assert 2 < paraphrases < 4, paraphrases
print("OK: master discovery call - open ratio", round(ratio, 4), ",", paraphrases, "paraphrases")
'''

def demo_feel_felt_found(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
answers = [
    "I understand how you feel; others felt the same at first; what they found was the pilot answered it.",
    "I understand how you feel about switching; two clients felt the same; what they found was onboarding took a day.",
    "I understand how you feel; our first users felt the same way; what they found was support replied in hours.",
]
markers = ["understand how you feel", "felt the same", "what they found"]
complete = sum(1 for a in answers if all(m in a for m in markers))
print("answers:", len(answers))
print("with all three moves:", complete)
assert 2 < complete < 4, complete
print("OK:", complete, "objection answers carry feel, felt, and found")
'''

def demo_price(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
value_stack = [12000, 8000, 5000]
price = 9000
total = sum(value_stack)
roi = (total - price) / price
payback_months = price / (total / 12)
print("value stack:", value_stack, "=", total)
print("price:", price)
print("ROI:", round(roi, 4))
print("payback months:", round(payback_months, 4))
assert 1.77 < roi < 1.79, roi
assert 4.3 < payback_months < 4.4, payback_months
print("OK: value", total, "vs price", price, "- ROI", round(roi, 4))
'''

def demo_challenger(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
scores = {"teach": 8, "tailor": 7, "control": 9}
total = sum(scores.values())
norm = total / 30
print("challenger scores:", scores)
print("total:", total, "/ 30 =", round(norm, 4))
assert 0.79 < norm < 0.81, norm
print("OK: challenger pitch scores", round(norm, 4), "on teach/tailor/control")
'''

def demo_consultative(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
diagnostic_turns = 8
prescription_turns = 3
ratio = diagnostic_turns / prescription_turns
print("diagnostic turns:", diagnostic_turns)
print("prescription turns:", prescription_turns)
print("ratio:", round(ratio, 4))
assert 2.6 < ratio < 2.7, ratio
print("OK: consultative ratio", round(ratio, 4), "- diagnosing before prescribing")
'''

def demo_snap(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
first = {"simple": 1, "invaluable": 1, "aligned": 0, "priority": 1}
rewritten = {"simple": 1, "invaluable": 1, "aligned": 1, "priority": 1}
s1, s2 = sum(first.values()), sum(rewritten.values())
print("first draft SNAP:", s1, "/ 4")
print("rewritten SNAP:", s2, "/ 4")
assert 2 < s1 < 4, s1
assert 3 < s2 <= 4, s2
print("OK: SNAP rewrite lifted", s1, "to", s2)
'''

def demo_story(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
story = {
    "protagonist": "a 30-person support team like yours",
    "problem": "tickets waited three days",
    "attempts": "hiring two more agents did not help",
    "change": "they switched routing and added same-day SLA",
    "result": "response fell to 4 hours and churn dropped 18 percent",
}
filled = sum(1 for v in story.values() if v.strip())
quantified = any(ch.isdigit() for ch in story["result"])
completeness = filled / 5
print("story slots filled:", filled, "/ 5")
print("result quantified:", quantified)
assert 0.99 < completeness <= 1.0, completeness
assert quantified, "result not quantified"
print("OK: case-study story complete with measured result")
'''

def demo_stall(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
response = ("Of course, it deserves thought. When you say think about it, what are "
            "the open questions on your mind? Is it the timing, the fit, or something "
            "I have not addressed? Let us put thirty minutes Thursday to walk through "
            "those questions.")
moves = ["of course", "what are the open questions", "is it the timing", "thursday"]
present = sum(1 for m in moves if m in response.lower())
dated = "thursday" in response.lower()
print("stall-response moves present:", present, "/ 4")
print("dated next step:", dated)
assert 3 < present < 5, present
assert dated, "no dated next step"
print("OK: stall answered with", present, "moves and a dated next step")
'''

def demo_summary(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
needs = ["same-day response", "escalation path", "data residency", "team training", "Q3 go-live"]
matched = ["same-day SLA", "tiered escalation", "EU data region", "onboarding program", "March start plan"]
confirmed = [True, True, True, True, True]
coverage = sum(confirmed) / len(needs)
print("confirmed needs:", len(needs))
print("capabilities matched:", len(matched))
print("buyer confirmations:", sum(confirmed))
print("recap coverage:", round(coverage, 4))
assert 0.99 < coverage <= 1.0, coverage
print("OK: summary close recaps", len(needs), "confirmed needs into yes")
'''

def demo_choice_close(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
warm_trials = 3
explicit_signal = False
gate = warm_trials >= 3 or explicit_signal
close_line = "Would you prefer the March or the April start, or is neither right?"
has_exit = "neither" in close_line.lower()
print("warm trials:", warm_trials)
print("readiness gate:", gate)
print("graceful exit present:", has_exit)
assert 2 < warm_trials < 4, warm_trials
assert gate and has_exit, "close not properly gated"
print("OK: choice close gated on", warm_trials, "warm trials with an easy exit")
'''

def demo_negotiation(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
ledger = [
    ("seller gives 500 discount", -500, 0),
    ("buyer commits 2-year term", 0, 800),
    ("seller gives free training", -300, 0),
    ("buyer gives case study", 0, 400),
]
balance = sum(give + get for _, give, get in ledger)
print("ledger rounds:", len(ledger))
for label, give, get in ledger:
    print("  ", label)
print("seller balance:", balance)
assert 399 < balance < 401, balance
print("OK: concession ledger balanced at", balance, "- every give earned a get")
'''

def demo_meddic(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
scores = [2, 2, 1, 2, 1, 2]
letters = ["metrics", "economic buyer", "decision criteria", "decision process", "identify pain", "champion"]
total = sum(scores)
forecast = total >= 8
print("MEDDIC:", dict(zip(letters, scores)))
print("total:", total, "/ 12")
print("forecastable:", forecast)
assert 9 < total < 11, total
assert forecast, "below forecast threshold"
print("OK: MEDDIC", total, "- deal is forecastable")
'''

def demo_committee(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
stakeholders = [
    {"role": "CFO", "win": "cut cost", "fear": "overrun", "stance": "neutral", "next": "exec alignment"},
    {"role": "support lead", "win": "faster tools", "fear": "learning curve", "stance": "ally", "next": "demo"},
    {"role": "IT security", "win": "compliance", "fear": "data risk", "stance": "blocker", "next": "security review"},
    {"role": "end users", "win": "ease", "fear": "change", "stance": "neutral", "next": "pilot"},
    {"role": "procurement", "win": "terms", "fear": "lock-in", "stance": "neutral", "next": "paperwork"},
]
cols = ["role", "win", "fear", "stance", "next"]
cells = sum(1 for s in stakeholders for c in cols if s[c])
completeness = cells / (len(stakeholders) * len(cols))
blockers = sum(1 for s in stakeholders if s["stance"] == "blocker")
print("stakeholders mapped:", len(stakeholders))
print("map completeness:", round(completeness, 4))
print("blockers found:", blockers)
assert 0.99 < completeness <= 1.0, completeness
assert 0 < blockers < 2, blockers
print("OK: committee of", len(stakeholders), "mapped, hidden blocker surfaced")
'''

def demo_rubric(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
criteria = ["discovery", "questions", "listening", "needs doc", "value translation",
            "objections", "trial closes", "ethics", "next steps", "buyer experience"]
scores = [8, 7, 9, 8, 7, 8, 9, 10, 8, 7]
total = sum(scores)
print("criteria:", len(criteria))
print("scores:", dict(zip(criteria, scores)))
print("total:", total, "/ 100")
assert 80 < total < 82, total
print("OK: dialogue rubric total", total, "- ethics at full marks")
'''

def demo_angry(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
response = ("I hear you, and I am not going to interrupt. That sounds like it cost you "
            "real production time, and I am sorry you went through that. Help me understand "
            "exactly which shipment was late so I can trace it. I will have the trace and "
            "a recovery plan to you by 5 PM today.")
moves = ["not going to interrupt", "cost you real", "sorry you went through",
         "which shipment", "by 5 pm today"]
present = sum(1 for m in moves if m in response.lower())
interruptions = 0
print("de-escalation moves:", present, "/ 5")
print("interruptions:", interruptions)
assert 4 < present < 6, present
assert interruptions < 1, interruptions
print("OK: angry buyer met with all", present, "de-escalation moves, zero interruptions")
'''

def demo_expert(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
questions = 6
unknowns = 2
admissions = 2
bluffs = 0
admission_rate = admissions / unknowns if unknowns else 1.0
print("expert questions:", questions)
print("unknowns admitted:", admissions, "/", unknowns)
print("bluffs:", bluffs)
assert 0.99 < admission_rate <= 1.0, admission_rate
assert bluffs < 1, bluffs
print("OK: expert buyer -", admissions, "admissions with dated fetches, zero bluffs")
'''

def demo_persona_consult(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
seller_turns = [
    "Let me make sure I have this right: response time is the top pain.",
    "I do not know our exact latency there; I will get engineering numbers tomorrow.",
    "Here is what I suggest for our Thursday review.",
    "Two clients in your position saw the same issue.",
    "Shall we walk through the findings before I mention any product?",
    "If neither date works, just say so and we will find another.",
    "What would solving this be worth to the team?",
    "I will send the summary I promised by end of day.",
]
forbidden = ["guaranteed", "act now", "competitors are", "limited time", "trust only us"]
violations = sum(1 for t in seller_turns for f in forbidden if f in t.lower())
print("persona turns:", len(seller_turns))
print("forbidden moves:", violations)
assert violations < 1, violations
print("OK: consultative persona -", len(seller_turns), "turns, zero forbidden moves")
'''

def demo_persona_chall(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
insight_verified = True
control_offers = 3
turns = 10
rate = control_offers / turns
print("commercial insight verified:", insight_verified)
print("control offers:", control_offers, "in", turns, "turns")
print("guidance rate:", round(rate, 4))
assert insight_verified, "unverified insight"
assert 0.29 < rate < 0.31, rate
print("OK: challenger persona teaches truth and guides at rate", round(rate, 4))
'''

def demo_fullcycle(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
gates = [
    ("first touch", True),
    ("discovery", True),
    ("evaluation", True),
    ("proposal", True),
    ("negotiation", True),
    ("close", True),
    ("handoff", True),
]
passed = sum(1 for _, ok in gates if ok)
promise_log = 6
print("stages:", len(gates))
print("gates passed:", passed)
print("promises logged for delivery:", promise_log)
assert 6 < passed < 8, passed
assert 5 < promise_log < 7, promise_log
print("OK: full cycle -", passed, "gates passed, promise log handed to delivery")
'''

def demo_guardrails(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
dialogue = ("I understand how you feel about the timeline. Others felt the same; "
            "what they found was the pilot settled it in two weeks. Our starter plan "
            "covers up to 10 users honestly, and I will send the security doc Friday. "
            "If neither date works, just say so.")
patterns = ["expires tonight", "guaranteed", "competitors are", "no limits ever",
            "act now", "trust only us", "limited time"]
violations = sum(1 for p in patterns if p in dialogue.lower())
print("guardrail patterns scanned:", len(patterns))
print("violations found:", violations)
assert violations < 1, violations
print("OK: dialogue clean -", violations, "ethical violations across", len(patterns), "patterns")
'''

def demo_selfreview(hdr, name, rid, group, points, req):
    return hdr(name, rid, group) + '''\
self_score = 82
coach_score = 85
calibration = abs(self_score - coach_score)
improvement = "ask one more implication question before presenting"
violations = 0
print("self score:", self_score)
print("coach score:", coach_score)
print("calibration gap:", calibration)
print("next improvement:", improvement)
assert 2 < calibration < 4, calibration
assert violations < 1, violations
print("OK: self-review calibrated within", calibration, "points, one improvement named")
'''

DEMOS = {
    "ai-seller-promise": demo_promise,
    "aida-model": demo_aida,
    "fab-outcomes": demo_fab,
    "question-toolkit": demo_questions,
    "active-listening": demo_listening,
    "rapport-trust": demo_rapport,
    "needs-analysis": demo_needs,
    "value-prop-one-sentence": demo_valueprop,
    "bant-qualification": demo_bant,
    "conversation-arc": demo_arc,
    "trial-closes": demo_trial,
    "followup-discipline": demo_followup,
    "spin-selling": demo_spin,
    "discovery-call-corpus": demo_discovery_corpus,
    "feel-felt-found": demo_feel_felt_found,
    "price-objections": demo_price,
    "challenger-sale": demo_challenger,
    "consultative-selling": demo_consultative,
    "snap-selling": demo_snap,
    "storytelling-close": demo_story,
    "stall-handling": demo_stall,
    "summary-close": demo_summary,
    "choice-assumptive-close": demo_choice_close,
    "negotiation-give-take": demo_negotiation,
    "meddic-qualification": demo_meddic,
    "multi-stakeholder-selling": demo_committee,
    "evaluation-rubric": demo_rubric,
    "drill-angry-buyer": demo_angry,
    "drill-expert-buyer": demo_expert,
    "persona-consultative-ai": demo_persona_consult,
    "persona-challenger-ai": demo_persona_chall,
    "full-cycle-playbook": demo_fullcycle,
    "ethical-guardrails": demo_guardrails,
    "self-review": demo_selfreview,
}
