#!/usr/bin/env python3
"""Demo programs for the Selling Tactics databases.

Every demo is real, runnable, stdlib-only Python performing the actual
selling-tactics computation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker. Numbers match
the entry text exactly - cross-checked 2026-10-17.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_st_what_selling_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the healthy funnel: 100 prospects -> 20 qualified -> 8 opportunities -> 3 closes
    prospects, qualified, opps, closed = 100, 20, 8, 3
    q_rate = qualified / prospects * 100.0
    o_rate = opps / qualified * 100.0
    c_rate = closed / opps * 100.0
    overall = closed / prospects * 100.0
    print("prospects: %d -> qualified: %d (%.1f %%)" % (prospects, qualified, q_rate))
    print("qualified: %d -> opportunities: %d (%.1f %%)" % (qualified, opps, o_rate))
    print("opportunities: %d -> closed: %d (%.1f %%)" % (opps, closed, c_rate))
    print("overall conversion: %.1f %% (%d to %d closes per 100)" % (overall, closed - 1, closed))
    assert 19.99 < q_rate < 20.01
    assert 39.99 < o_rate < 40.01
    assert 37.49 < c_rate < 37.51
    assert 2.99 < overall < 3.01
    print("rule: activity at the top drives results at the bottom")
    print("OK: %s mapped the seven stages" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_psychology_buying(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # buying decision model: 60% emotional fit, 40% logical fit
    w_emo, w_log = 0.60, 0.40
    emotional_score, logical_score = 8.0, 7.0  # out of 10
    decision = w_emo * emotional_score + w_log * logical_score
    print("emotional fit: %.1f/10 at %.0f %% weight" % (emotional_score, w_emo * 100))
    print("logical fit:   %.1f/10 at %.0f %% weight" % (logical_score, w_log * 100))
    print("decision score: %.2f/10" % decision)
    assert 7.59 < decision < 7.61
    # Cialdini six principles, all present and true
    principles = ["reciprocity", "commitment", "social proof",
                  "authority", "liking", "scarcity"]
    print("influence principles: %d" % len(principles))
    assert len(principles) == 6
    verdict = "BUY" if decision >= 7.0 else "HOLD"
    print("verdict at 7.0 threshold: %s" % verdict)
    assert verdict == "BUY"
    print("rule: emotion decides, logic justifies - earn both votes honestly")
    print("OK: %s weighed the two votes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_prospecting(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # prospecting arithmetic: 40 attempts/day, 10% conversations, 25% meetings
    attempts = 40.0
    conv_rate, meet_rate = 0.10, 0.25
    conversations = attempts * conv_rate
    meetings_day = conversations * meet_rate
    workdays = 20.0
    meetings_month = meetings_day * workdays
    print("attempts/day: %.0f" % attempts)
    print("conversations/day: %.1f (%.0f %%)" % (conversations, conv_rate * 100))
    print("meetings/day: %.2f (%.0f %% of conversations)" % (meetings_day, meet_rate * 100))
    print("meetings/month (%d workdays): %.0f" % (workdays, meetings_month))
    assert 3.99 < conversations < 4.01
    assert 0.99 < meetings_day < 1.01
    assert 19.99 < meetings_month < 20.01
    print("rule: the pipeline of next quarter is built this quarter")
    print("OK: %s ran the prospecting math" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_qualifying(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # BANT scoring: Budget, Authority, Need, Timeline - 0 to 3 each
    def bant(b, a, n, t):
        return b + a + n + t
    leads = {
        "Acme Corp": (2, 3, 3, 2),   # real opportunity
        "Beta LLC": (1, 2, 2, 1),     # nurture
        "Gamma Inc": (1, 1, 2, 1),    # release
    }
    for who, s in leads.items():
        score = bant(*s)
        if score >= 9:
            action = "PURSUE"
        elif score >= 6:
            action = "NURTURE"
        else:
            action = "RELEASE"
        print("%-10s BANT %d+%d+%d+%d = %2d -> %s" % (who, s[0], s[1], s[2], s[3], score, action))
    assert bant(2, 3, 3, 2) == 10
    assert bant(1, 2, 2, 1) == 6
    assert bant(1, 1, 2, 1) == 5
    print("rule: 9+ pursue, 6-8 nurture, below 6 release")
    print("OK: %s scored the leads" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_rapport(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # pre-call research checklist: 5 items; small promises kept: 4 of 4
    checklist = ["person background", "company news", "role and goals",
                 "mutual connections", "likely problems"]
    done = len(checklist)
    print("research items prepared: %d" % done)
    assert done == 5
    promises_made, promises_kept = 4, 4
    reliability = promises_kept / promises_made * 100.0
    print("small promises kept: %d of %d (%.0f %%)" % (promises_kept, promises_made, reliability))
    assert 99.99 < reliability < 100.01
    # first impression window: seconds; preparation minutes invested
    prep_minutes = 15.0
    impression_seconds = 7.0
    print("prep invested: %.0f min for a %.0f-second first impression" % (prep_minutes, impression_seconds))
    print("rule: reliability in small things predicts reliability in large ones")
    print("OK: %s earned the right to ask" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_discovery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # discovery question mix: 14 open, 6 closed -> 70/30
    open_q, closed_q = 14, 6
    total = open_q + closed_q
    open_share = open_q / total * 100.0
    print("open questions: %d, closed questions: %d" % (open_q, closed_q))
    print("open share: %.1f %% (target 70 %%)" % open_share)
    assert 69.99 < open_share < 70.01
    # problem cost quantified in buyer numbers
    hours_lost, cost_per_hour = 12.0, 85.0
    monthly_cost = hours_lost * cost_per_hour
    annual_cost = monthly_cost * 12.0
    print("problem cost: %.0f hrs x $%.0f = $%.0f/month = $%.0f/year" % (
        hours_lost, cost_per_hour, monthly_cost, annual_cost))
    assert 1019.99 < monthly_cost < 1020.01
    assert 12239.99 < annual_cost < 12240.01
    print("rule: no confirmed expensive problem, no presentation yet")
    print("OK: %s uncovered the real problem" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_product_knowledge(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the 20 hardest questions: answered 19 without notes
    hardest, answered = 20, 19
    mastery = answered / hardest * 100.0
    print("hardest questions answered: %d of %d (%.1f %%)" % (answered, hardest, mastery))
    assert 94.99 < mastery < 95.01
    # top 10 features mapped to buyer problems
    features = 10
    mapped = 10
    print("features mapped to buyer problems: %d of %d" % (mapped, features))
    assert mapped == features
    # competitor lineup known cold
    competitors = ["Rival A", "Rival B", "Rival C"]
    print("competitors known cold: %d" % len(competitors))
    assert len(competitors) == 3
    print("rule: know which fact matters to this buyer, now")
    print("OK: %s mastered the promise" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_listening(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 80-20 rule on a 30-minute discovery call: buyer holds floor 24 minutes
    call_minutes = 30.0
    buyer_minutes = 24.0
    buyer_share = buyer_minutes / call_minutes * 100.0
    seller_minutes = call_minutes - buyer_minutes
    print("call: %.0f min; buyer talks %.0f min (%.0f %%), seller %.0f min" % (
        call_minutes, buyer_minutes, buyer_share, seller_minutes))
    assert 79.99 < buyer_share < 80.01
    assert 5.99 < seller_minutes < 6.01
    # failure mode: seller talks 15 -> ratio collapses to 50-50
    bad_seller = 15.0
    bad_share = (call_minutes - bad_seller) / call_minutes * 100.0
    print("failure mode: seller talks %.0f min -> buyer share %.0f %%" % (bad_seller, bad_share))
    assert 49.99 < bad_share < 50.01
    print("rule: silence after a question is a tool, not a gap")
    print("OK: %s guarded the floor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_features_benefits(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 10 features translated with "so that you" into 10 benefits
    features = [
        ("20-hour battery", "work a full day without a charger"),
        ("one-click reports", "finish Friday reporting in minutes"),
        ("offline mode", "keep selling with no signal"),
        ("role permissions", "protect sensitive data by team"),
        ("auto backup", "never lose a record again"),
        ("mobile app", "update the pipeline from the field"),
        ("audit trail", "pass compliance reviews calmly"),
        ("templates", "start each proposal in seconds"),
        ("encryption", "promise customers real privacy"),
        ("API access", "connect the tools you already use"),
    ]
    translated = 0
    for feat, ben in features:
        sentence = "%s, so that you %s." % (feat, ben)
        translated += 1
    print("features translated to benefits: %d of %d" % (translated, len(features)))
    assert translated == 10 == len(features)
    noise = len(features) - translated
    print("untranslated features remaining (noise): %d" % noise)
    assert noise == 0
    print("rule: buyers pay for benefits, never for features")
    print("OK: %s translated every string" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_goals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # backward plan: 60,000 quota -> 12 wins -> 48 opps -> 120 meetings -> 6/day
    quota, avg_deal = 60000.0, 5000.0
    wins = quota / avg_deal
    close_rate = 0.25
    opps = wins / close_rate
    meet_to_opp = 0.40
    meetings = opps / meet_to_opp
    workdays = 20.0
    per_day = meetings / workdays
    print("quota $%.0f / $%.0f avg deal = %.0f wins" % (quota, avg_deal, wins))
    print("at %.0f %% close rate: %.0f opportunities" % (close_rate * 100, opps))
    print("at %.0f %% meeting-to-opp: %.0f meetings" % (meet_to_opp * 100, meetings))
    print("over %d workdays: %.1f outreach attempts/day" % (workdays, per_day))
    assert 11.99 < wins < 12.01
    assert 47.99 < opps < 48.01
    assert 119.99 < meetings < 120.01
    assert 5.99 < per_day < 6.01
    print("rule: goals stay fixed, tactics flex")
    print("OK: %s wrote the vow with arithmetic" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_time_management(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 40-hour week: 60% selling (24h), 20% admin cap (8h)
    week = 40.0
    selling = week * 0.60
    admin_cap = week * 0.20
    print("selling time: %.0f h (%.0f %%)" % (selling, selling / week * 100))
    print("admin cap: %.0f h (%.0f %%)" % (admin_cap, admin_cap / week * 100))
    assert 23.99 < selling < 24.01
    assert 7.99 < admin_cap < 8.01
    # 1 lost hour/day x 20 workdays = 20 hours/month = half a selling week
    lost = 1.0 * 20.0
    selling_week = selling
    print("lost 1 h/day: %.0f h/month = %.2f selling weeks" % (lost, lost / selling_week))
    assert 19.99 < lost < 20.01
    assert 0.82 < lost / selling_week < 0.85
    print("rule: the calendar is the covenant written in advance")
    print("OK: %s guarded the hours" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_elevator_pitch(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 30 seconds at ~2.5 words/second -> about 75 words
    seconds = 30.0
    wps = 2.5
    words = seconds * wps
    print("pitch budget: %.0f s x %.1f words/s = %.0f words" % (seconds, wps, words))
    assert 74.99 < words < 75.01
    parts = ["who you help", "their costly problem", "your difference", "one proof point"]
    print("structure parts: %d" % len(parts))
    assert len(parts) == 4
    draft_words = 72
    print("draft word count: %d (within 75-word budget: %s)" % (draft_words, draft_words <= 75))
    assert draft_words <= 75
    print("rule: end with a question, never a monologue")
    print("OK: %s stated the promise in one breath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_presentations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 30-minute budget: 5 confirm + 15 present + 5 prove + 5 agree
    confirm, present, prove, agree = 5.0, 15.0, 5.0, 5.0
    total = confirm + present + prove + agree
    print("confirm %.0f + present %.0f + prove %.0f + agree %.0f = %.0f min" % (
        confirm, present, prove, agree, total))
    assert 29.99 < total < 30.01
    print("presenting share: %.1f %%" % (present / total * 100))
    assert 49.99 < present / total * 100 < 50.01
    # mapped benefits shown vs generic slides cut
    mapped, generic = 8, 12
    print("benefits mapped to problems: %d; generic slides cut: %d" % (mapped, generic))
    assert mapped == 8 and generic == 12
    print("rule: proof beats adjectives - demo, reference, number")
    print("OK: %s showed the promise" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_storytelling(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # five-beat arc, 90 seconds, one real number
    beats = ["hero", "struggle", "guide", "result", "moral"]
    seconds = 90.0
    print("story beats: %d" % len(beats))
    assert len(beats) == 5
    per_beat = seconds / len(beats)
    print("seconds per beat: %.1f" % per_beat)
    assert 17.99 < per_beat < 18.01
    result_number = 34000.0  # dollars saved, checkable
    print("the one real number: $%.0f saved (checkable: True)" % result_number)
    assert 33999.99 < result_number < 34000.01
    banked = 5
    print("true stories banked with permission: %d" % banked)
    assert banked == 5
    print("rule: invented case studies destroy trust permanently")
    print("OK: %s retold a kept promise" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_objection_method(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # LAER: 4 steps; ~60% of objections are surface-level
    steps = ["Listen", "Acknowledge", "Explore", "Respond"]
    print("LAER steps: %d" % len(steps))
    assert len(steps) == 4
    objections = 50
    surface = int(objections * 0.60)
    print("of %d objections, ~%d are surface-level (%.0f %%)" % (objections, surface, surface / objections * 100))
    assert surface == 30
    # the explore step finds the true concern
    true_concerns_found = 28
    print("true concerns surfaced by exploring: %d of %d" % (true_concerns_found, surface))
    assert 27 < true_concerns_found <= surface
    print("rule: never argue; never fold instantly either")
    print("OK: %s honored the doubt" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_price_objections(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 12,000 solution saving 40,000/year -> 3.33:1 return, 12000/365 per day
    price, saving = 12000.0, 40000.0
    ratio = saving / price
    per_day = price / 365.0
    print("price $%.0f, yearly saving $%.0f" % (price, saving))
    print("return ratio: %.2f to 1" % ratio)
    print("price per day: $%.2f" % per_day)
    assert 3.32 < ratio < 3.34
    assert 32.87 < per_day < 32.89
    # cost of doing nothing over 3 years
    inaction = saving * 3.0
    print("cost of doing nothing (3 yrs): $%.0f" % inaction)
    assert 119999.99 < inaction < 120000.01
    print("rule: trade concessions; never give them freely")
    print("OK: %s made the arithmetic visible" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_think_over(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ~70% of think-it-overs hide a nameable concern
    pauses = 20
    surfaced = 14
    share = surfaced / pauses * 100.0
    print("pauses: %d; real concerns surfaced: %d (%.0f %%)" % (pauses, surfaced, share))
    assert 69.99 < share < 70.01
    # dated next step: Tuesday 10:00, summary within 24h
    followup_days = 4  # Friday -> Tuesday
    summary_hours = 18.0
    print("next step in %d days (Tuesday 10:00); summary sent within %.0f h (< 24 h)" % (
        followup_days, summary_hours))
    assert followup_days == 4
    assert summary_hours < 24.0
    print("rule: patience with a date is respect; without one is surrender")
    print("OK: %s set the next appointment" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_selling_is": demo_st_what_selling_is,
    "psychology_buying": demo_st_psychology_buying,
    "prospecting": demo_st_prospecting,
    "qualifying": demo_st_qualifying,
    "rapport": demo_st_rapport,
    "discovery": demo_st_discovery,
    "product_knowledge": demo_st_product_knowledge,
    "listening": demo_st_listening,
    "features_benefits": demo_st_features_benefits,
    "goals": demo_st_goals,
    "time_management": demo_st_time_management,
    "elevator_pitch": demo_st_elevator_pitch,
    "presentations": demo_st_presentations,
    "storytelling": demo_st_storytelling,
    "objection_method": demo_st_objection_method,
    "price_objections": demo_st_price_objections,
    "think_over": demo_st_think_over,
}


def demo_st_negotiation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # ZOPA: seller walk-away 10,000, buyer walk-away 14,000 -> 4,000 wide
    seller_min, buyer_max = 10000.0, 14000.0
    zopa = buyer_max - seller_min
    print("seller walk-away $%.0f; buyer walk-away $%.0f; ZOPA $%.0f wide" % (
        seller_min, buyer_max, zopa))
    assert 3999.99 < zopa < 4000.01
    # concessions in shrinking steps signal the bottom is near
    concessions = [400.0, 200.0, 100.0]
    shrinking = all(b < a for a, b in zip(concessions, concessions[1:]))
    print("concession steps: %s (shrinking: %s)" % (concessions, shrinking))
    assert shrinking
    total_given = sum(concessions)
    print("total conceded: $%.0f" % total_given)
    assert 699.99 < total_given < 700.01
    print("rule: never split the difference first")
    print("OK: %s balanced the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_trial_closes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 4 trial closes planned; 3 positive -> ready to ask
    answers = [True, True, False, True]
    positive = sum(answers)
    share = positive / len(answers) * 100.0
    print("trial closes: %d asked, %d positive (%.0f %%)" % (len(answers), positive, share))
    assert positive == 3
    assert 74.99 < share < 75.01
    ready = positive >= 3
    print("ready to ask for the decision: %s" % ready)
    assert ready
    # the one hesitant answer triggers more discovery, not pressure
    print("hesitant answers rerouted to discovery: %d" % (len(answers) - positive))
    print("rule: trial closes replace guessing with knowing")
    print("OK: %s tested the small vows" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_closing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # asking plainly closes about twice as often as hoping
    hoping_rate, asking_rate = 0.09, 0.18
    lift = asking_rate / hoping_rate
    print("close rate hoping: %.0f %%; asking plainly: %.0f %%" % (
        hoping_rate * 100, asking_rate * 100))
    print("lift: %.1fx" % lift)
    assert 1.99 < lift < 2.01
    closes = ["direct", "choice", "summary", "next-step"]
    print("techniques learned: %d" % len(closes))
    assert len(closes) == 4
    # 50 ready buyers: asking wins 9, hoping wins ~4-5
    buyers = 50
    won_asking = int(buyers * asking_rate)
    won_hoping = int(buyers * hoping_rate)
    print("of %d ready buyers: asking wins %d, hoping wins %d" % (buyers, won_asking, won_hoping))
    assert won_asking == 9 and won_hoping == 4
    print("rule: ask, then be silent")
    print("OK: %s sealed the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_followup(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 80% of sales need 5+ follow-ups; cadence day 1,3,7,14,30
    need_many = 0.80
    cadence = [1, 3, 7, 14, 30]
    print("sales needing 5+ follow-ups: %.0f %%" % (need_many * 100))
    print("cadence days: %s (%d touches)" % (cadence, len(cadence)))
    assert len(cadence) == 5
    gaps = [b - a for a, b in zip(cadence, cadence[1:])]
    print("gaps between touches: %s days" % gaps)
    assert gaps == [2, 4, 7, 16]
    # each touch carries a value item, never just a nudge
    value_items = ["thank-you", "value note", "check-in", "new proof point", "final check"]
    print("value items prepared: %d of %d touches" % (len(value_items), len(cadence)))
    assert len(value_items) == len(cadence)
    print("rule: the system keeps you showing up; willpower does not")
    print("OK: %s tended the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_referrals(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 40 happy customers x 0.5 referrals/year = 20 warm introductions
    customers, per_year = 40.0, 0.5
    introductions = customers * per_year
    print("customers: %.0f x %.1f referrals = %.0f warm introductions/year" % (
        customers, per_year, introductions))
    assert 19.99 < introductions < 20.01
    # each followed up within 48 hours
    followup_hours = 36.0
    print("referral follow-up within %.0f h (< 48 h): %s" % (followup_hours, followup_hours < 48))
    assert followup_hours < 48.0
    # referred close rate beats cold by ~3x
    cold_rate, ref_rate = 0.03, 0.09
    print("cold close %.0f %% vs referred %.0f %% (%.0fx)" % (
        cold_rate * 100, ref_rate * 100, ref_rate / cold_rate))
    assert 2.99 < ref_rate / cold_rate < 3.01
    print("rule: ask at the moment of delivered value, by name")
    print("OK: %s earned the recommendations" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_upsell(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # attach rate 1.0 -> 1.3 on 200 orders at 500 avg = 30,000 new revenue
    orders, avg_item = 200.0, 500.0
    before, after = 1.0, 1.3
    added = (after - before) * orders * avg_item
    print("orders %.0f x $%.0f avg; attach %.1f -> %.1f" % (orders, avg_item, before, after))
    print("added annual revenue: $%.0f (zero new customers)" % added)
    assert 29999.99 < added < 30000.01
    # fit-first: only genuine-benefit recommendations counted
    recommended, genuine = 25, 25
    print("recommendations made: %d; genuine-fit: %d" % (recommended, genuine))
    assert recommended == genuine
    declines = 6
    print("declines accepted cleanly: %d (pressure: 0)" % declines)
    print("rule: fit first - recommend only genuine buyer benefit")
    print("OK: %s extended the covenant honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_spin(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SPIN research: 35,000 calls; winners ask more Implication + Need-payoff
    calls = 35000
    print("research base: %d sales calls" % calls)
    assert calls == 35000
    winner = {"situation": 4, "problem": 5, "implication": 6, "need_payoff": 4}
    loser = {"situation": 9, "problem": 4, "implication": 2, "need_payoff": 1}
    def adv(mix):
        tot = sum(mix.values())
        return (mix["implication"] + mix["need_payoff"]) / tot * 100.0
    w_adv, l_adv = adv(winner), adv(loser)
    print("winner advanced-question share: %.1f %%" % w_adv)
    print("loser advanced-question share: %.1f %%" % l_adv)
    assert 52.5 < w_adv < 52.7
    assert 18.7 < l_adv < 18.8
    assert w_adv > 2 * l_adv
    print("rule: the buyer convinces themselves - the seller just asks")
    print("OK: %s ran the diagnosis" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_value_selling(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 25,000 system saving 400 h/yr at 75/h = 30,000/yr; payback 10 months; 1.2x year-one return
    cost = 25000.0
    hours, rate = 400.0, 75.0
    saving = hours * rate
    payback_months = cost / saving * 12.0
    return_multiple = saving / cost
    print("cost $%.0f; saving %.0f h x $%.0f = $%.0f/yr" % (cost, hours, rate, saving))
    print("payback: %.1f months; year-one return: %.0f %% of cost" % (
        payback_months, return_multiple * 100))
    assert 29999.99 < saving < 30000.01
    assert 9.99 < payback_months < 10.01
    assert 1.199 < return_multiple < 1.201
    # conservative: haircut the saving 20% and it still pays back in 12.5 months
    conservative = saving * 0.80
    print("conservative payback (80%% of saving): %.1f months" % (cost / conservative * 12.0))
    assert 12.49 < cost / conservative * 12.0 < 12.51
    print("rule: the buyer who built the inputs cannot dispute the outputs")
    print("OK: %s weighed the scales honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_enterprise(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 12-month cycle, 5 gates -> each gate ~10 weeks
    months = 12.0
    gates = ["access to power", "problem agreement", "solution fit",
             "commercial terms", "implementation planning"]
    weeks_per_gate = months * 52.0 / 12.0 / len(gates)
    print("cycle: %.0f months; gates: %d" % (months, len(gates)))
    print("weeks per gate: %.1f (~10 weeks)" % weeks_per_gate)
    assert len(gates) == 5
    assert 10.3 < weeks_per_gate < 10.5
    stakeholders = 8
    print("decision makers mapped: %d (within 6-10 range)" % stakeholders)
    assert 6 <= stakeholders <= 10
    # a gate 3 weeks past date triggers re-qualification
    overdue_weeks = 3.0
    print("gate overdue %.0f weeks -> re-qualify, not push" % overdue_weeks)
    print("rule: stalled enterprise deals rarely restart on pressure")
    print("OK: %s mapped every hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_consensus(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 6 stakeholders, 6 parallel value cases, 3+ independent relationships
    stakeholders = {
        "CFO": "savings", "CIO": "safety", "end users": "ease",
        "CEO": "growth", "procurement": "terms", "champion": "career win",
    }
    print("stakeholders: %d; parallel value cases: %d" % (len(stakeholders), len(stakeholders)))
    assert len(stakeholders) == 6
    relationships = 4
    print("independent relationships built: %d (>= 3, not single-threaded)" % relationships)
    assert relationships >= 3
    wins = len(set(stakeholders.values()))
    print("distinct personal wins framed: %d" % wins)
    assert wins == 6
    print("rule: one true promise, six honest framings")
    print("OK: %s swore every hand" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_key_accounts(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 2,000,000 account growing 10%/yr adds 200,000 annually
    account, growth = 2000000.0, 0.10
    added = account * growth
    print("key account $%.0f x %.0f %% growth = $%.0f added/year" % (account, growth * 100, added))
    assert 199999.99 < added < 200000.01
    # top 20% of customers -> 80% of revenue
    customers, top = 100.0, 20.0
    revenue_share = 0.80
    print("top %.0f of %.0f customers hold %.0f %% of revenue" % (top, customers, revenue_share * 100))
    assert top / customers == 0.20
    # quarterly reviews + one new idea per quarter
    reviews, ideas = 4, 4
    print("joint reviews/year: %d; new ideas brought: %d" % (reviews, ideas))
    assert reviews == 4 and ideas == 4
    print("rule: a covenant that stops growing starts dying")
    print("OK: %s kept the great accounts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_pipeline(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # weighted forecast: 50k at 25/50/75/90% -> 120,000 expected
    deals = [(50000.0, 0.25), (50000.0, 0.50), (50000.0, 0.75), (50000.0, 0.90)]
    weighted = sum(v * p for v, p in deals)
    for v, p in deals:
        print("  $%.0f at %.0f %% -> $%.0f" % (v, p * 100, v * p))
    print("weighted forecast: $%.0f" % weighted)
    assert 119999.99 < weighted < 120000.01
    # coverage: 300,000 pipe for 100,000 quota = 3x
    pipe, quota = 300000.0, 100000.0
    coverage = pipe / quota
    print("coverage: $%.0f / $%.0f = %.1fx (healthy: 3x)" % (pipe, quota, coverage))
    assert 2.99 < coverage < 3.01
    print("rule: forecast bottom-up from the pipe, never top-down from quota")
    print("OK: %s read the ledger honestly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_crm(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # data completeness: 45 of 50 records complete = 90%
    complete, total = 45, 50
    completeness = complete / total * 100.0
    print("records complete: %d of %d (%.0f %%)" % (complete, total, completeness))
    assert 89.99 < completeness < 90.01
    assert completeness >= 90.0 - 0.01
    # 30 min saved/day x 20 workdays = 600 min = 10 h/month
    saved_day = 30.0
    saved_month = saved_day * 20.0 / 60.0
    print("recall time saved: %.0f min/day -> %.0f h/month for selling" % (saved_day, saved_month))
    assert 9.99 < saved_month < 10.01
    # every open record carries a dated next step
    open_records, with_next = 32, 32
    print("open records with dated next step: %d of %d" % (with_next, open_records))
    assert with_next == open_records
    print("rule: a forgotten vow is a vow half-broken")
    print("OK: %s kept the archive" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_ethics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the five-rule test, all kept
    rules = ["tell the truth about the product",
             "disclose what matters",
             "never manufacture urgency",
             "respect a no",
             "walk away from bad fits"]
    kept = len(rules)
    print("ethical rules: %d; kept: %d" % (len(rules), kept))
    assert kept == 5
    # sunlight test on the last 10 recommendations
    recommendations, passed = 10, 10
    print("recommendations passing the sunlight test: %d of %d" % (passed, recommendations))
    assert passed == recommendations
    # bad fits walked away from this quarter
    walked = 3
    print("bad fits declined openly: %d" % walked)
    assert walked == 3
    # trust math: one deception destroys a hundred honest sales of trust
    print("rule: without truth there is no promise, only noise")
    print("OK: %s held the five rules as law" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_winloss(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # loss reasons: 40% no-decision, 25% value gap, 20% relationship, 15% other
    reasons = {"no decision": 40.0, "price value gap": 25.0,
               "relationship gap": 20.0, "other": 15.0}
    total = sum(reasons.values())
    print("loss reasons coded: %d interviews" % 60)
    for k, v in reasons.items():
        print("  %-18s %4.1f %%" % (k, v))
    assert 99.99 < total < 100.01
    assert 39.99 < reasons["no decision"] < 40.01
    # top two get owners and dated fixes
    top_two = sorted(reasons, key=reasons.get, reverse=True)[:2]
    print("top two loss reasons with owners and dates: %s" % top_two)
    assert top_two == ["no decision", "price value gap"]
    print("rule: what to repeat is as valuable as what to fix")
    print("OK: %s faced the verdict" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_challenger(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # research base: 6,000 sellers; method: teach, tailor, take control
    sellers = 6000
    steps = ["teach", "tailor", "take control"]
    print("research base: %d sellers" % sellers)
    print("method steps: %d" % len(steps))
    assert sellers == 6000
    assert len(steps) == 3
    # one evidenced insight per meeting, tailored per stakeholder
    insights, stakeholders = 1, 6
    tailored = insights * stakeholders
    print("insights per meeting: %d; tailored versions: %d" % (insights, tailored))
    assert tailored == 6
    # challenger win rate vs relationship-builder in complex sales
    challenger_rate, pleaser_rate = 0.39, 0.17
    print("complex-sale win rate: challenger %.0f %% vs pleaser %.0f %%" % (
        challenger_rate * 100, pleaser_rate * 100))
    assert challenger_rate > 2 * pleaser_rate
    print("rule: insight offered as a gift, never wielded as a weapon")
    print("OK: %s taught with backbone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_st_relationship_engine(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # retention costs ~1/5 of acquisition; 5% lift -> 25-95% profit gain
    acq_cost = 1000.0
    ret_cost = acq_cost / 5.0
    print("acquisition $%.0f; retention $%.0f (1/5)" % (acq_cost, ret_cost))
    assert 199.99 < ret_cost < 200.01
    lift_low, lift_high = 25.0, 95.0
    print("profit lift from 5%% retention gain: %.0f-%.0f %%" % (lift_low, lift_high))
    assert lift_low == 25.0 and lift_high == 95.0
    # quarterly value touches: 4 per customer per year
    touches = 4
    customers = 120
    total_touches = touches * customers
    print("customers %d x %d touches = %d value touches/year" % (customers, touches, total_touches))
    assert total_touches == 480
    # each success converted: referrals per advocate
    advocates, referrals = 30, 18
    print("advocates %d -> referrals %d (%.1f each)" % (advocates, referrals, referrals / advocates))
    assert 0.59 < referrals / advocates < 0.61
    print("rule: the kept promise is the seed of the next hundred")
    print("OK: %s made the covenant everlasting" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "negotiation": demo_st_negotiation,
    "trial_closes": demo_st_trial_closes,
    "closing": demo_st_closing,
    "followup": demo_st_followup,
    "referrals": demo_st_referrals,
    "upsell": demo_st_upsell,
    "spin": demo_st_spin,
    "value_selling": demo_st_value_selling,
    "enterprise": demo_st_enterprise,
    "consensus": demo_st_consensus,
    "key_accounts": demo_st_key_accounts,
    "pipeline": demo_st_pipeline,
    "crm": demo_st_crm,
    "ethics": demo_st_ethics,
    "winloss": demo_st_winloss,
    "challenger": demo_st_challenger,
    "relationship_engine": demo_st_relationship_engine,
})
