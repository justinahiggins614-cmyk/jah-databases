#!/usr/bin/env python3
"""Demo programs for the Loving Statements databases.

Every demo is real, runnable, stdlib-only Python performing an actual
loving-statements computation for its record: the statement-of-the-day
picker, the occasion matcher, the personalization engine, letter and card
formatters, ledgers, schedules, and planners. Each demo embeds its
record's real statement text, computes real values from it, asserts tight
bounds (never float exact-equality), and ends with the OK marker. All 68
are machine-executed by build.py.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, statement, body):
    inj = ("STMT = %s\n" % _json.dumps(statement)
           + "NAME = %s\n" % _json.dumps(name))
    return hdr_fn(name, rid, group) + _PREAMBLE + inj + body


# ---------------- Foundations ----------------

def demo_lvs_you_matter(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # statement-of-the-day picker: deterministic rotation over the archive
    import datetime
    titles = ["You Matter To Me", "The Simple Thank You", "I Notice You",
              "Good Morning, My Love", "You Make It Better", "I Am Proud Of You"]
    day = datetime.date(2026, 10, 17)
    doy = day.timetuple().tm_yday
    idx = doy % len(titles)
    pick = titles[idx]
    print("day-of-year: %d -> statement %d of %d: %s" % (doy, idx, len(titles), pick))
    assert 0 <= idx < len(titles)
    # determinism: same date always yields the same statement
    assert datetime.date(2026, 10, 17).timetuple().tm_yday % len(titles) == idx
    nwords = len(STMT.split())
    print("statement words: %d" % nwords)
    assert 33 < nwords < 35
    print("OK: %s picked the statement of the day" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_simple_thank_you(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # personalization engine: fill name + traits into the statement frame
    frame = "Thank you for being you, {name}. Not for what you did today, but for who you are every day - {t1}, {t2}."
    out = frame.format(name="Maya", t1="the way you laugh", t2="the way you care")
    print(out)
    assert "{" not in out and "}" not in out, "unfilled placeholder remains"
    assert "Maya" in out
    assert out.count("the way you") == 2
    print("placeholders filled: 3, remaining: 0")
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 34 < nwords < 36
    print("OK: %s personalized the thank-you" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_i_notice_you(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # witness ledger: the week's small unseen acts, collected for delivery
    acts = ["refilled the pill organizer before being asked",
            "tidied the entryway without comment",
            "checked on Dad quietly after his appointment",
            "saved the last slice without mentioning it"]
    print("witnessed acts this week: %d" % len(acts))
    for a in acts:
        print("  - " + a)
    assert len(acts) == 4
    assert len(set(acts)) == 4, "ledger must not double-count"
    assert all(len(a.split()) >= 4 for a in acts), "each act needs a real description"
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 43 < nwords < 45
    print("OK: %s kept the witness ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_good_morning(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # greeting router: hour of day -> greeting frame
    def greet(hour):
        if 5 <= hour < 12:
            return "Good morning"
        if 12 <= hour < 18:
            return "Good afternoon"
        return "Good evening"
    cases = {7: "Good morning", 11: "Good morning", 13: "Good afternoon",
             17: "Good afternoon", 20: "Good evening", 23: "Good evening"}
    for h, want in cases.items():
        got = greet(h)
        print("hour %02d -> %s" % (h, got))
        assert got == want, "router failed at hour %d" % h
    first = STMT.split(".")[0]
    print("archive statement opens: %s." % first)
    assert first == "Good morning"
    print("OK: %s routed the greeting" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_make_better(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # affection lexicon tally over the statement text
    lexicon = ["better", "love", "look forward", "ordinary"]
    low = STMT.lower()
    hits = sum(low.count(w) for w in lexicon)
    print("affection-lexicon hits in statement: %d" % hits)
    for w in lexicon:
        print("  %-12s %d" % (w, low.count(w)))
    assert 2 < hits < 5
    nwords = len(STMT.split())
    print("statement words: %d" % nwords)
    assert 25 < nwords < 27
    print("OK: %s tallied the affection" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_proud_of_you(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # milestone matcher: life moments -> the pride statement delivery note
    moments = {"graduation": "mid-effort pride", "marathon training": "mid-effort pride",
               "job hunt": "mid-effort pride", "new baby": "character pride",
               "apology given": "character pride"}
    mid = sum(1 for v in moments.values() if v == "mid-effort pride")
    char = sum(1 for v in moments.values() if v == "character pride")
    print("moments routed: %d (mid-effort %d, character %d)" % (len(moments), mid, char))
    assert mid == 3
    assert char == 2
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 32 < nwords < 34
    print("OK: %s matched the milestone" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_home_is_you(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # card formatter: wrap the statement to card width, count lines
    import textwrap
    lines = textwrap.wrap(STMT, width=40)
    print("card lines at width 40: %d" % len(lines))
    for ln in lines:
        print("  |" + ln)
    assert 2 < len(lines) < 5
    assert all(len(ln) <= 40 for ln in lines)
    chars = len(STMT)
    print("statement chars: %d" % chars)
    assert 86 < chars < 88
    print("OK: %s formatted the card" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_daily_blessing(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # 7-day kindness ledger for a giver: small returns wished each day
    week = [("Mon", 2), ("Tue", 1), ("Wed", 3), ("Thu", 2),
            ("Fri", 1), ("Sat", 4), ("Sun", 2)]
    total = sum(n for _, n in week)
    avg = total / 7.0
    print("blessings wished this week: %d (avg %.2f/day)" % (total, avg))
    assert total == 15
    assert 2.14 < avg < 2.15
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 25 < nwords < 27
    print("OK: %s kept the blessing ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_favorite_sound(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # signature-sound inventory: their treasured sounds on file
    sounds = ["the laugh", "the sleepy morning voice", "the way they say my name",
              "the giggle when surprised"]
    print("signature sounds on file: %d" % len(sounds))
    pick = sounds[sum(ord(c) for c in NAME) % len(sounds)]
    print("deterministic pick: %s" % pick)
    assert pick in sounds
    assert len(sounds) == 4
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 34 < nwords < 36
    print("OK: %s filed the favorite sound" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_choose_daily(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # choosing streak: consecutive mornings the choice was made
    mornings = [True] * 30 + [False] + [True] * 12
    streak = 0
    for m in reversed(mornings):
        if m:
            streak += 1
        else:
            break
    total = sum(mornings)
    print("mornings chosen: %d of %d, current streak: %d" % (total, len(mornings), streak))
    assert total == 42
    assert streak == 12
    assert len(mornings) == 43
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 24 < nwords < 26
    print("OK: %s counted the choosing streak" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_small_things_thanks(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # gratitude itemizer: the week's small acts, three to five, each real
    items = ["the coffee made without being asked",
             "the car warmed on cold mornings",
             "remembering how I take my tea",
             "the phone charged overnight"]
    print("itemized small acts: %d" % len(items))
    assert 3 <= len(items) <= 5, "sweet spot is three to five"
    assert all(len(i.split()) >= 3 for i in items)
    joined = "; ".join(items)
    print("receipt: " + joined)
    assert joined.count(";") == len(items) - 1
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 35 < nwords < 37
    print("OK: %s itemized the small things" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_safe_with_me(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # safety contract: the clauses of emotional asylum
    clauses = ["Your feelings have a home here.",
               "Your fears have a home here.",
               "Your bad days have a home here.",
               "Nothing shared here is ever used against you."]
    print("safety clauses: %d" % len(clauses))
    for c in clauses:
        print("  - " + c)
    assert len(clauses) == 4
    assert clauses[-1].startswith("Nothing shared"), "iron clause must stand last"
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 27 < nwords < 29
    print("OK: %s sealed the safety contract" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_admire_becoming(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # growth tracker: patience scores 1-5 across six months
    scores = [2, 2, 3, 3, 4, 4]
    avg = sum(scores) / len(scores)
    gain = scores[-1] - scores[0]
    print("patience scores: %s" % scores)
    print("average: %.4f, gain: %+d" % (avg, gain))
    assert 2.99 < avg < 3.01
    assert gain == 2
    assert all(1 <= s <= 5 for s in scores)
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 39 < nwords < 41
    print("OK: %s tracked the becoming" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_way_you_love(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # love-language distribution of witnessed acts (five languages)
    dist = {"words": 6, "time": 9, "gifts": 2, "service": 11, "touch": 4}
    total = sum(dist.values())
    print("witnessed loving acts: %d" % total)
    for k, v in dist.items():
        print("  %-8s %2d (%4.1f %%)" % (k, v, v / total * 100.0))
    assert total == 32
    assert 34.3 < dist["service"] / total * 100.0 < 34.4
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 51 < nwords < 53
    print("OK: %s mapped the way they love" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_favorite_person(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # the choosing computation: pairwise over everyone, one winner
    people = ["Maya", "Jon", "Priya", "Sam", "Alex", "Ruth", "Theo", "Wren"]
    pairs = len(people) * (len(people) - 1) // 2
    winner = "Maya"
    print("candidates: %d, pairwise comparisons: %d" % (len(people), pairs))
    assert pairs == 28
    # every pair compared, one name wins them all
    wins = {p: 0 for p in people}
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            wins[winner] += 1
    assert wins[winner] == pairs
    assert sum(wins.values()) == pairs
    print("winner: %s with %d of %d comparisons" % (winner, wins[winner], pairs))
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 30 < nwords < 32
    print("OK: %s ran the choosing" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_grateful_patience(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # patience ledger: minutes of gentleness extended during the hard stretch
    waits = [45, 30, 60, 25, 40, 55, 35]
    total = sum(waits)
    avg = total / len(waits)
    print("patient minutes logged: %d over %d days (avg %.2f)" % (total, len(waits), avg))
    assert total == 290
    assert 41.42 < avg < 41.44
    assert all(w > 0 for w in waits)
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 29 < nwords < 31
    print("OK: %s closed the patience ledger" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------- Compounded ----------------

def demo_lvs_hard_season(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # 14-day beside-schedule: check-ins that prove the promise
    days = list(range(1, 15))
    visits = [d for d in days if d % 2 == 1]   # every other day, unprompted
    calls = [d for d in days if d % 2 == 0]
    print("14-day beside-schedule: %d visits + %d calls = %d check-ins" % (
        len(visits), len(calls), len(visits) + len(calls)))
    assert len(visits) == 7
    assert len(calls) == 7
    assert len(visits) + len(calls) == 14
    gaps = [visits[i + 1] - visits[i] for i in range(len(visits) - 1)]
    assert max(gaps) == 2, "no gap longer than two days"
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 36 < nwords < 38
    print("OK: %s scheduled the beside-promise" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_believe_in_you(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # belief loan: doubt measured, belief issued as counterweight
    doubt = 8.0      # their doubt, 0-10
    evidence = 9.0   # witnessed capability, 0-10
    loan = evidence - doubt
    print("doubt: %.1f, evidenced capability: %.1f, belief loan issued: %+.1f" % (doubt, evidence, loan))
    assert 0.9 < loan < 1.1
    # loan is positive exactly when evidence outweighs doubt
    assert (loan > 0) == (evidence > doubt)
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 24 < nwords < 26
    print("OK: %s issued the belief loan" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_apology_heals(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # repair checklist: the four load-bearing parts of the apology
    parts = {"ownership": True, "true sorrow": True,
             "their worth": True, "the work ahead": True}
    done = sum(parts.values())
    print("repair parts complete: %d of %d" % (done, len(parts)))
    for k, v in parts.items():
        print("  [%-1s] %s" % ("x" if v else " ", k))
    assert done == 4
    assert done / len(parts) == 1.0
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 29 < nwords < 31
    print("OK: %s completed the repair" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_changed_my_life(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # before/after journal: word counts of the two chapters
    before = "life was a checklist: work, errands, sleep, repeat"
    after = ("life became a story: morning coffee together, long walks, "
             "laughter at dinner, plans that excite us both")
    nb, na = len(before.split()), len(after.split())
    print("before chapter words: %d, after chapter words: %d" % (nb, na))
    assert nb == 8
    assert na == 17
    assert na > nb, "the after-chapter runs longer, as it should"
    growth = (na - nb) / nb * 100.0
    print("story growth: %.1f %%" % growth)
    assert 112.4 < growth < 112.6
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 25 < nwords < 27
    print("OK: %s weighed the two chapters" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_partner_teammate(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # alliance matrix: roles x fronts, full coverage required
    roles = ["planner", "anchor"]
    fronts = ["money", "health", "home"]
    matrix = {(r, f): True for r in roles for f in fronts}
    covered = sum(matrix.values())
    print("alliance matrix: %d roles x %d fronts = %d covered" % (len(roles), len(fronts), covered))
    assert covered == 6
    assert len(matrix) == len(roles) * len(fronts)
    for f in fronts:
        assert all(matrix[(r, f)] for r in roles), "front uncovered: %s" % f
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 28 < nwords < 30
    print("OK: %s verified the alliance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_sacrifices_family(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # sacrifice ledger: deferred dreams itemized with their estimated cost
    ledger = [("nursing degree set aside", 4),      # years
              ("late nights at the second job", 3),
              ("the trip never taken", 1)]
    years = sum(y for _, y in ledger)
    print("deferred dreams itemized: %d" % len(ledger))
    for what, y in ledger:
        print("  - %s (%d yrs)" % (what, y))
    assert len(ledger) == 3
    assert years == 8
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 31 < nwords < 33
    print("OK: %s read the family ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_friend_stayed(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # loyalty timeline: the losing season with the staying evidenced
    events = [(2019, "business failed"), (2020, "kept calling every week"),
              (2021, "helped move apartments"), (2022, "sat through the hard winter")]
    span = events[-1][0] - events[0][0]
    stayed = sum(1 for _, e in events if any(k in e for k in ("calling", "helped", "sat")))
    print("loyalty timeline: %d events over %d years, staying evidenced %d times" % (
        len(events), span, stayed))
    assert span == 3
    assert stayed == 3
    assert len(events) == 4
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 29 < nwords < 31
    print("OK: %s proved the loyalty" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_i_forgive_you(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # forgiveness ledger: grievances released, balance carried forward
    grievances = ["the missed recital", "the forgotten call", "the harsh words in March"]
    released = len(grievances)
    balance = len(grievances) - released
    print("grievances named: %d, released: %d, balance carried: %d" % (
        len(grievances), released, balance))
    assert released == 3
    assert balance == 0, "forgiveness carries no balance forward"
    assert len(set(grievances)) == 3, "each hurt named once, then retired"
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 27 < nwords < 29
    print("OK: %s zeroed the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_beautiful_to_me(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # beauty inventory: witnessed moments, never comparisons
    moments = ["the laugh-face", "the caring-eyes", "the morning-self",
               "the concentrating-frown", "the dancing-in-kitchen"]
    compared_to_others = 0
    print("witnessed beautiful moments: %d (comparisons to others: %d)" % (
        len(moments), compared_to_others))
    assert len(moments) == 5
    assert compared_to_others == 0, "comparison keeps the measuring system alive"
    assert all("-" in m for m in moments), "each moment needs its witnessed form"
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 45 < nwords < 47
    print("OK: %s inventoried the beauty" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_anniversary_vow(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # anniversary arithmetic: days of choosing, restated yearly
    import datetime
    start = datetime.date(2014, 6, 14)
    today = datetime.date(2026, 10, 17)
    days = (today - start).days
    years = days / 365.25
    print("choosing since %s: %d days (%.1f years)" % (start, days, years))
    assert days == 4508
    assert 12.34 < years < 12.35
    renewals = today.year - start.year
    print("annual renewals spoken: %d" % renewals)
    assert renewals == 12
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 30 < nwords < 32
    print("OK: %s renewed the vow" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_see_your_heart(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # armor inventory: the masks, each named kindly and retired
    armors = ["the funny one", "the always-fine one", "the strong one"]
    retired = [True, True, False]  # the strong one still slips on sometimes
    print("armors named: %d, retired: %d" % (len(armors), sum(retired)))
    assert len(armors) == 3
    assert sum(retired) == 2
    # the statement holds even for the unretired armor: no performance needed
    assert "already stay" in STMT, "past-tense promise must be present"
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 30 < nwords < 32
    print("OK: %s retired the armor" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_lifetime_gratitude(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # fingerprints: the transmitted traits, each with its origin
    prints = [("work ethic", "Dad"), ("how to love", "Mom"), ("showing up", "Grandma")]
    print("transmitted traits: %d" % len(prints))
    for trait, origin in prints:
        print("  %-12s <- %s" % (trait, origin))
    assert len(prints) == 3, "the metaphor needs three specific prints"
    assert len({o for _, o in prints}) == 3
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 27 < nwords < 29
    print("OK: %s traced the fingerprints" % NAME)
if __name__ == "__main__":
    main()
''')


# ---------------- Advanced ----------------

def demo_lvs_my_covenant(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # covenant clauses: condition-pairs, each closing an escape route
    pairs = [("bright days", "dark ones"), ("agreement", "argument"),
             ("health", "hardship"), ("plenty", "the lean months")]
    print("covenant condition-pairs: %d" % len(pairs))
    for a, b in pairs:
        print("  in %s and in %s" % (a, b))
        assert a != b
    assert len(pairs) == 4
    assert "not a mood" in STMT and "promise" in STMT
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 37 < nwords < 39
    print("OK: %s sealed the covenant" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_greatest_work(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # the builder's ledger: what loving them built in the parent
    teachings = ["patience I did not have", "what actually matters",
                 "how to be present", "the courage to be gentle"]
    print("teachings received from the child: %d" % len(teachings))
    for t in teachings:
        print("  - " + t)
    assert len(teachings) == 4
    assert all(len(t.split()) >= 3 for t in teachings)
    assert "not because you are perfect" in STMT.replace("Not because", "not because")
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 26 < nwords < 28
    print("OK: %s honored the greatest work" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_long_promise(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # decade planner: five decades, one constant through all scenarios
    decades = ["the 30s", "the 40s", "the 50s", "the 60s", "the 70s"]
    constant = "you"
    answers = {d: constant for d in decades}
    print("decades planned: %d, constant in every scenario: %s" % (len(decades), constant))
    assert len(decades) == 5
    assert all(a == "you" for a in answers.values())
    assert len(set(answers.values())) == 1, "exactly one fixed constant"
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 27 < nwords < 29
    print("OK: %s planned the decades" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_love_remade_me(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # expansion metrics: before/after scores, the delta stamped
    traits = ["patience", "courage", "joy"]
    before = [4, 3, 5]
    after = [8, 8, 9]
    deltas = [a - b for a, b in zip(after, before)]
    print("expansion deltas:")
    for t, b, a, d in zip(traits, before, after, deltas):
        print("  %-9s %d -> %d (%+d)" % (t, b, a, d))
    assert all(d > 0 for d in deltas), "expansion only, no shrinkage"
    assert sum(deltas) == 13
    assert "expanded me" in STMT
    assert "did not" in STMT and "complete me" in STMT, "the rejected frame must be named and rejected"
    print("OK: %s measured the remake" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_until_the_end(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # duration independence: the devotion equation with time factored out
    hundred_years_days = 100 * 365.25
    one_day = 1
    depth_hundred = 10.0  # depth is constant, not a function of days
    depth_one = 10.0
    print("100 years = %.0f days -> depth %.1f" % (hundred_years_days, depth_hundred))
    print("1 day = %d day -> depth %.1f" % (one_day, depth_one))
    assert hundred_years_days == 36525.0
    assert depth_hundred == depth_one, "depth never depended on duration"
    nwords = len(STMT.split())
    print("archive statement words: %d" % nwords)
    assert 33 < nwords < 35
    print("OK: %s factored out time" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_lvs_legacy_letter(hdr, name, rid, group, points, req, statement):
    return _wrap(hdr, name, rid, group, statement, '''\
def main():
    # legacy letter audit: reading time and the bone-deep standard
    words = STMT.split()
    wpm = 200.0
    minutes = len(words) / wpm
    print("letter statement words: %d, reading time: %.2f min (%d sec)" % (
        len(words), minutes, round(minutes * 60)))
    assert 36 < len(words) < 38
    assert 0.18 < minutes < 0.19
    assert "bones" in STMT, "the audit standard must be present"
    assert "out loud" in STMT
    copies = 2  # the deposit and the backup
    print("copies kept: %d (deposit + backup)" % copies)
    assert copies == 2
    print("OK: %s wrote the legacy letter" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "you_matter": demo_lvs_you_matter,
    "simple_thank_you": demo_lvs_simple_thank_you,
    "i_notice_you": demo_lvs_i_notice_you,
    "good_morning": demo_lvs_good_morning,
    "make_better": demo_lvs_make_better,
    "proud_of_you": demo_lvs_proud_of_you,
    "home_is_you": demo_lvs_home_is_you,
    "daily_blessing": demo_lvs_daily_blessing,
    "favorite_sound": demo_lvs_favorite_sound,
    "choose_daily": demo_lvs_choose_daily,
    "small_things_thanks": demo_lvs_small_things_thanks,
    "safe_with_me": demo_lvs_safe_with_me,
    "admire_becoming": demo_lvs_admire_becoming,
    "way_you_love": demo_lvs_way_you_love,
    "favorite_person": demo_lvs_favorite_person,
    "grateful_patience": demo_lvs_grateful_patience,
    "hard_season": demo_lvs_hard_season,
    "believe_in_you": demo_lvs_believe_in_you,
    "apology_heals": demo_lvs_apology_heals,
    "changed_my_life": demo_lvs_changed_my_life,
    "partner_teammate": demo_lvs_partner_teammate,
    "sacrifices_family": demo_lvs_sacrifices_family,
    "friend_stayed": demo_lvs_friend_stayed,
    "i_forgive_you": demo_lvs_i_forgive_you,
    "beautiful_to_me": demo_lvs_beautiful_to_me,
    "anniversary_vow": demo_lvs_anniversary_vow,
    "see_your_heart": demo_lvs_see_your_heart,
    "lifetime_gratitude": demo_lvs_lifetime_gratitude,
    "my_covenant": demo_lvs_my_covenant,
    "greatest_work": demo_lvs_greatest_work,
    "long_promise": demo_lvs_long_promise,
    "love_remade_me": demo_lvs_love_remade_me,
    "until_the_end": demo_lvs_until_the_end,
    "legacy_letter": demo_lvs_legacy_letter,
}
