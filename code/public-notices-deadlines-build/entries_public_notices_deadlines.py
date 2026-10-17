#!/usr/bin/env python3
"""Entries for the Public Notices and Deadlines databases (missing-115 #58).

RAW SWEEP over the full manifest (2,095 prefixes) plus every shard index
title in jah-databases-data-1 (790 index files): zero 'public-notices*'
slugs/names; zero title collisions on all 68 planned titles (gate run
2026-10-17 before authoring, zero refusals). No existing database covers
recalls, regulatory changes, tenders, filings, advisories, and expiration
dates as an operational deadline-tracking discipline - BUILD NEW is the
verdict.

This build creates two NEW databases, 34 ladder-ordered records each:

  public-notices-deadlines              - The Public Notices and Deadlines
                                         Database
                                         (public-harvest: real, fact-checked
                                         operational knowledge - recalls,
                                         regulatory changes, tenders,
                                         filings, advisories, expiration
                                         dates; the anatomy of a public
                                         notice; deadline computation with
                                         business days and jurisdiction
                                         rules; compliance calendars; notice
                                         tracking workflows; advisory
                                         severity classification; standard
                                         references the Federal Register
                                         Act 44 U.S.C. 1501-1511; the
                                         Administrative Procedure Act
                                         5 U.S.C. 553; FDA recall classes
                                         21 CFR Part 7; NHTSA 49 U.S.C.
                                         30118-30120; CPSC 15 U.S.C. 2064;
                                         FRCP Rule 6; the FAR 48 CFR Part 5;
                                         the Exchange Act reporting rules;
                                         IRC 26 U.S.C. 6072; 35 U.S.C. 41(b)
                                         maintenance fees; the Lanham Act
                                         15 U.S.C. 1058-1059; ISO 8601:2019;
                                         and the other landmarks cited per
                                         record)
  public-notices-deadlines-signature   - The Public Notices and Deadlines
                                         Signature Database
                                         (his original Signature Deadline
                                         Doctrine: every notice a summons,
                                         every deadline a covenant kept in
                                         public, the compliance calendar the
                                         honor roll, severity classification
                                         the measure of the warning, and the
                                         tracking workflow the chain of
                                         custody; src signature, titles
                                         suffixed " (Signature Edition)",
                                         never presented as authentic public
                                         record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-PNDT- (public) and JAH-PNDTS- (signature). NOTE: the
first-choice prefixes JAH-PND- / JAH-PNDS- were taken (two pre-existing
databases share JAH-PND-: park-naturalists and public-neuropsychologists,
an anomaly outside this build), so the PNDT form (Public Notices and
Deadlines Tracking) was chosen; verified free in the manifest and in all
shard indexes.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_public_notices_deadlines.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
the records ship.

Screening: civilian operational scope only. Nothing hate-adjacent,
profane, or inappropriate; no religious talk; nothing on neutralizing or
defeating military or defense-grade systems.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Deadline Doctrine: "
            "every notice a summons, every deadline a covenant kept in "
            "public, the compliance calendar the honor roll, severity "
            "classification the measure of the warning, and the tracking "
            "workflow the chain of custody. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_FR_ACT = ("Federal Register Act, 44 U.S.C. sections 1501-1511 (1935; "
              "publication of federal rules, proposed rules, and notices in "
              "the Federal Register).")
CIT_APA = ("Administrative Procedure Act, 5 U.S.C. section 553 (1946; "
           "notice-and-comment rulemaking for federal agencies).")
CIT_FDA_RECALL = ("21 CFR Part 7, sections 7.3 and 7.41-7.59 (FDA "
                  "enforcement policy: recall definitions, Class I, II, and "
                  "III classifications, and recall procedures).")
CIT_FDCA = ("Federal Food, Drug, and Cosmetic Act, 21 U.S.C. sections "
            "301-399 (adulteration, misbranding, and FDA enforcement "
            "authority).")
CIT_NHTSA = ("49 U.S.C. sections 30118-30120 (National Traffic and Motor "
             "Vehicle Safety Act: manufacturer notification and remedy of "
             "defects and noncompliance).")
CIT_CPSC = ("Consumer Product Safety Act, 15 U.S.C. section 2064 (section "
            "15: reporting of substantial product hazards and corrective "
            "action).")
CIT_FRCP6 = ("Federal Rules of Civil Procedure, Rule 6 (computing and "
             "extending time; periods stated in days, the 3-day addition for "
             "service by mail).")
CIT_FAR = ("Federal Acquisition Regulation, 48 CFR Part 5 (publicizing "
           "contract actions) and Parts 14-15 (sealed bidding and "
           "contracting by negotiation).")
CIT_EXCHANGE = ("Securities Exchange Act of 1934, sections 13 and 15(d); "
                "17 CFR 240.13a-1 and 240.15d-1 (periodic reporting: Forms "
                "10-K, 10-Q, 8-K).")
CIT_IRC = ("Internal Revenue Code, 26 U.S.C. section 6072 (time for filing "
           "income tax returns; April 15 general rule for calendar-year "
           "individuals).")
CIT_MAINT = ("35 U.S.C. section 41(b) (patent maintenance fees due at 3.5, "
             "7.5, and 11.5 years after grant); Manual of Patent Examining "
             "Procedure (MPEP), U.S. Patent and Trademark Office.")
CIT_LANHAM = ("Lanham Act, 15 U.S.C. sections 1058-1059 (trademark affidavit "
              "of use under section 8 and renewal under section 9).")
CIT_ISO8601 = ("ISO 8601:2019 (date and time format - information "
               "interchange; YYYY-MM-DD ordering).")
CIT_FTC = ("Federal Trade Commission Act, 15 U.S.C. section 45 (unfair or "
           "deceptive acts or practices).")
CIT_OSHA = ("Occupational Safety and Health Act; 29 CFR 1904 (recording and "
            "reporting occupational injuries and illness) and 29 CFR 1910 "
            "(occupational safety and health standards).")
CIT_NEPA = ("National Environmental Policy Act, 42 U.S.C. sections "
            "4321-4347 (environmental review; public notice of proposed "
            "federal actions).")
CIT_PCT = ("Patent Cooperation Treaty (1970), Article 22 (national phase "
           "entry; 30-month time limit from the priority date).")
CIT_DEL = ("Delaware General Corporation Law, 8 Del. C. section 502 "
           "(annual franchise tax report and payment; representative state "
           "corporate filing duty).")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is a Public Notice",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A public notice is a formal announcement that a government "
            "body, regulator, court, or responsible organization is required "
            "or chooses to publish so that the public - and the people or "
            "businesses affected - can learn about it, respond to it, or "
            "obey it. Notices are how a society keeps its decisions visible: "
            "a new rule is proposed in the open, a defective product is "
            "recalled in the open, a government contract is offered in the "
            "open, a court case proceeds in the open. Without published "
            "notice, none of those actions could fairly bind anyone who did "
            "not know about them. That is the legal heart of the idea: due "
            "process depends on notice, and notice depends on publication. "
            "The United States built this into statute with the Federal "
            "Register Act, which created a daily journal where federal "
            "rules, proposed rules, and notices must appear so every citizen "
            "has constructive knowledge of them. Courts, agencies, and "
            "companies publish notices through gazettes, bulletins, posted "
            "signs, newspaper announcements, and now agency websites and "
            "email alert systems. A notice always answers the same core "
            "questions: who is speaking, what is happening, whom does it "
            "affect, what must be done, and by when. The 'by when' is the "
            "deadline, and the deadline is what turns information into "
            "obligation. This database treats notices and deadlines as one "
            "operational discipline: find the notice, read it correctly, "
            "compute the deadline, track it, and close it with proof."
        ),
        "how_it_works": (
            "A public notice works by moving information through a fixed "
            "chain: issuance, publication, awareness, response, and record. "
            "First an authority issues the notice - an agency finalizes a "
            "rule, a manufacturer discovers a defect, a court sets a hearing, "
            "a procurement office releases a solicitation. Then the notice "
            "is published in the channel the law or the situation requires: "
            "the Federal Register for federal rules, a court docket for "
            "legal proceedings, a company website and press release for a "
            "recall, a procurement portal for a tender. Publication creates "
            "constructive notice - the law treats you as informed whether or "
            "not you personally read it. Awareness is your job: subscribe to "
            "the feeds, scan the bulletins, watch the dockets. Response is "
            "the action the notice demands: file a comment, return the "
            "product, submit the bid, appear in court, pay the fee. And "
            "record is the proof you keep that you responded on time. Every "
            "notice in this database is handled the same way: intake it, "
            "classify it, extract its deadline, put the deadline on a "
            "compliance calendar, act before it, and file the evidence that "
            "you did."
        ),
        "key_points": [
            "A public notice is a formal published announcement that creates constructive knowledge: the law treats the public as informed once the notice is properly published.",
            "Due process depends on notice; the Federal Register Act made federal rules, proposed rules, and notices visible in one daily journal.",
            "Every notice answers five questions: who is speaking, what is happening, whom it affects, what must be done, and by when.",
            "The deadline is what turns information into obligation; missing it can mean fines, default judgments, lost rights, or unsafe products in the field.",
            "The operational discipline is always the same: intake, classify, extract the deadline, calendar it, act before it, and keep proof.",
        ],
        "requirements": [
            "A named issuing authority with the legal power to make the announcement it is making.",
            "Publication in the channel the governing law, rule, or situation requires - gazette, docket, bulletin, portal, or press.",
            "A clear statement of what is happening and who is affected, in plain enough language to act on.",
            "The required action stated explicitly, so the reader knows what response is expected.",
            "A deadline or effective date, so the notice creates a time-bound obligation rather than open-ended information.",
        ],
        "standards": [
            "Federal rules, proposed rules, and notices are published in the Federal Register under the Federal Register Act, 44 U.S.C. 1501-1511.",
            "Federal agency rulemaking follows notice-and-comment procedure under the Administrative Procedure Act, 5 U.S.C. 553.",
            "Dates in notices are read in ISO 8601 order (YYYY-MM-DD) to remove day/month ambiguity across jurisdictions.",
        ],
        "citations": [CIT_FR_ACT, CIT_APA, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: a public notice is a summons issued in "
            "the open, and the Signature Deadline Doctrine treats every "
            "summons as sacred. Where public procedure files a notice to "
            "satisfy due process, Signature procedure files it to keep a "
            "covenant with the public: nothing decided in shadow, nothing "
            "owed in silence. The notice is the call; the deadline is the "
            "promise; keeping it is the signature."
        ),
    },
    {
        "key": "anatomy",
        "name": "The Anatomy of a Public Notice",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every public notice, from a one-paragraph court posting to a "
            "two-hundred-page proposed rule, is built from the same parts. "
            "Learning the anatomy means you can read any notice in minutes "
            "instead of hours, because you know where each part lives and "
            "which parts carry legal weight. The header names the issuing "
            "authority and the notice type - rule, recall, solicitation, "
            "advisory, filing requirement. The identifier is the notice "
            "number, docket number, or solicitation number: the key you will "
            "use to track it, cite it, and search for it later. The "
            "authority statement cites the statute or rule that empowers the "
            "notice; if it cites nothing, treat it as informational rather "
            "than binding. The subject states what the notice is about in "
            "one line. The body describes the action, the affected parties, "
            "and the facts. The action section states exactly what the "
            "reader must do - comment, file, return, bid, appear, pay. The "
            "deadline block gives the dates: publication date, effective "
            "date, comment-close date, compliance date. And the contact "
            "block names the office, person, address, and method for "
            "response. A notice missing its authority statement is "
            "suspicious; a notice missing its deadline block is incomplete; "
            "a notice missing its contact block is unactionable. Professionals "
            "check the anatomy first and read the prose second."
        ),
        "how_it_works": (
            "Dissecting a notice works by scanning its parts in priority "
            "order rather than reading top to bottom. First read the header "
            "and identifier to know what you are holding and whether it "
            "concerns you. Second, read the authority statement to learn "
            "whether the notice binds you or merely informs you. Third, "
            "jump to the action section and the deadline block: these two "
            "together define your obligation and your clock, and they are "
            "the parts a tracking workflow extracts first. Fourth, read the "
            "body for the facts that shape your response - the scope of the "
            "recall, the terms of the solicitation, the text of the proposed "
            "rule. Fifth, note the contact block and the response method, "
            "because a comment filed to the wrong docket or a bid sent to "
            "the wrong office does not count. Finally, record the "
            "identifier, the deadline, and the source in your tracking "
            "system before you do anything else; notices get lost, "
            "calendars do not. This dissection takes minutes once the "
            "anatomy is memorized, and it is the same for recalls, "
            "rulemakings, tenders, and court notices."
        ),
        "key_points": [
            "Every notice has the same parts: header, identifier, authority statement, subject, body, action section, deadline block, and contact block.",
            "The authority statement decides whether the notice binds you; a notice citing no statute or rule is informational, not obligatory.",
            "The action section plus the deadline block define your obligation and your clock - extract these first, read prose second.",
            "The identifier (docket, solicitation, or notice number) is the tracking key: cite it in every response and search.",
            "A response sent to the wrong office or docket does not count; the contact block defines the only valid response path.",
        ],
        "requirements": [
            "A header naming the issuing authority and the notice type so the reader knows what kind of instrument it is.",
            "A unique identifier - notice, docket, or solicitation number - usable as a tracking and citation key.",
            "An authority statement citing the statute, rule, or power behind the notice.",
            "An explicit action section stating what the reader must do, and a deadline block with publication, effective, and compliance dates.",
            "A contact block with the office, address, and accepted response methods for the required action.",
        ],
        "standards": [
            "Federal notices carry docket or document numbers and cite their statutory authority in the Federal Register format under 44 U.S.C. 1501-1511.",
            "Procurement solicitations carry solicitation numbers and reference the FAR part governing the action (48 CFR Part 5 for publicizing).",
            "Recall notices carry the recall number and classify the hazard under 21 CFR Part 7 (FDA) or the applicable agency scheme.",
        ],
        "citations": [CIT_FR_ACT, CIT_FAR, CIT_FDA_RECALL],
        "sig_lens": (
            "The Signature read: the anatomy of a notice is the anatomy of "
            "a summons, and the Signature Deadline Doctrine inspects every "
            "joint. Where the public reader skims for the date, the "
            "Signature reader audits the authority first, because a summons "
            "without authority is noise and a summons with authority is "
            "law. Eight parts, each a covenant: the header swears identity, "
            "the deadline swears the clock."
        ),
    },
    {
        "key": "six_families",
        "name": "The Six Families of Notices and Deadlines",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "All public notices and deadlines fall into six families, and "
            "naming the family tells you which rules, which channels, and "
            "which consequences apply. Recalls order the return, repair, or "
            "replacement of unsafe products: FDA food and drug recalls, "
            "NHTSA vehicle recalls, CPSC consumer-product recalls - each "
            "with classes that grade the hazard. Regulatory changes propose, "
            "amend, or repeal the rules themselves, and they run on "
            "notice-and-comment clocks with published closing dates. Tenders "
            "invite the public to bid for government contracts, with "
            "solicitation numbers, specifications, and hard submission "
            "deadlines. Filings are the reports the law demands on schedule: "
            "tax returns, SEC 10-K and 10-Q reports, corporate annual "
            "reports, each with a statutory due date and penalties for "
            "lateness. Advisories warn without ordering: safety alerts, "
            "health advisories, weather and travel advisories, graded by "
            "severity so the public knows how urgently to act. Expiration "
            "dates end rights and permissions: licenses, certifications, "
            "patents pending maintenance fees, trademarks needing renewal - "
            "all of which die quietly if the calendar is not watched. The "
            "families overlap in practice - a regulatory change can create "
            "new filing duties, a recall can follow an advisory - but each "
            "keeps its own anatomy, its own channel, and its own clock. "
            "Classifying the notice into its family is the first act of "
            "tracking, because the family decides everything downstream."
        ),
        "how_it_works": (
            "The six families work as a classification system for triage. "
            "When a notice arrives, the first question is which family it "
            "belongs to, and the answer routes the work. A recall routes to "
            "the recall playbook: identify affected units, notify owners, "
            "provide the remedy, report to the regulator. A regulatory "
            "change routes to the comment calendar: read the proposal, "
            "assess the impact, draft and file comments before the docket "
            "closes. A tender routes to the bid workflow: check eligibility, "
            "build the proposal, submit before the solicitation deadline - "
            "late bids are rejected unopened. A filing routes to the "
            "reporting calendar: prepare the report, file by the statutory "
            "date, keep the acceptance receipt. An advisory routes to the "
            "severity scale: informational notices get logged, warnings get "
            "acted on, critical alerts get escalated. An expiration routes "
            "to the renewal calendar with a lead-time alarm set before the "
            "grace period. Each family has its own canonical sources, its "
            "own deadline arithmetic, and its own evidence of compliance, "
            "which is why the classification must happen at intake, before "
            "anything else is decided."
        ),
        "key_points": [
            "The six families are recalls, regulatory changes, tenders, filings, advisories, and expiration dates; each has its own anatomy, channel, and clock.",
            "Recalls order return, repair, or replacement of unsafe products and are graded by hazard class (FDA Class I, II, III).",
            "Regulatory changes run on notice-and-comment clocks; tenders run on hard submission deadlines where late bids are rejected unopened.",
            "Advisories warn without ordering and are graded by severity; expirations end rights quietly and need lead-time alarms.",
            "Classifying the notice into its family at intake routes all downstream work: playbook, calendar, arithmetic, and evidence.",
        ],
        "requirements": [
            "A family label assigned at intake, before any other processing, so the correct workflow is chosen.",
            "The family-specific source channel monitored continuously: recall portals, the Federal Register, procurement sites, docket systems.",
            "Family-specific deadline arithmetic applied: business-day rules, statutory dates, grace periods, comment periods.",
            "Family-specific evidence of compliance retained: remedy records, filed comments, bid receipts, filing acceptances, renewal confirmations.",
            "Cross-family awareness: a regulatory change that creates filing duties or a recall that follows an advisory must link its records.",
        ],
        "standards": [
            "FDA recalls are classified Class I, II, or III under 21 CFR Part 7, sections 7.3 and 7.41-7.59.",
            "Federal rulemaking follows notice-and-comment under the Administrative Procedure Act, 5 U.S.C. 553.",
            "Federal contract actions are publicized under the Federal Acquisition Regulation, 48 CFR Part 5.",
        ],
        "citations": [CIT_FDA_RECALL, CIT_APA, CIT_FAR],
        "sig_lens": (
            "The Signature read: six families, six kinds of summons, one "
            "doctrine. The Signature Deadline Doctrine keeps a separate "
            "honor roll for each family, because a missed recall kills and "
            "a missed comment period only silences - the doctrine weighs "
            "the covenant by what is at stake. Classify at intake, the way "
            "a sentry names the approaching party before deciding the "
            "response."
        ),
    },
    {
        "key": "deadline_anatomy",
        "name": "What Is a Deadline: Trigger, Computation, Consequence",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A deadline is not just a date. It is a three-part machine: a "
            "trigger that starts the clock, a computation that counts the "
            "time, and a consequence that fires when the time runs out. The "
            "trigger is the event the rule points at: publication of the "
            "notice, service of the papers, the end of the tax year, the "
            "grant of the patent, the issuance of the license. Nothing is "
            "due until the trigger fires, which is why professionals always "
            "ask 'when did the clock start' before they ask 'when is it "
            "due.' The computation is the counting rule: calendar days or "
            "business days, whether the trigger day counts, what happens "
            "when the last day falls on a weekend or holiday, which "
            "jurisdiction's holiday calendar applies. Two people can read "
            "the same '30 days' and land on different dates if they use "
            "different counting rules - and the one using the wrong rule "
            "loses. The consequence is what happens at zero: a late bid is "
            "rejected, a late comment is ignored, a late filing draws "
            "penalties and interest, a late patent fee kills the patent, a "
            "missed court deadline can default the case. Understanding all "
            "three parts is what separates deadline tracking from date "
            "collecting. A calendar full of dates with no triggers, no "
            "counting rules, and no consequences is decoration; a deadline "
            "system records all three for every entry."
        ),
        "how_it_works": (
            "A deadline works by converting the trigger event into a due "
            "date through the counting rule, then enforcing the consequence. "
            "Take a concrete example: a federal agency publishes a proposed "
            "rule on March 1 with a 60-day comment period. The trigger is "
            "publication. The computation under the Administrative Procedure "
            "Act convention counts calendar days forward, so day 60 is "
            "April 30; if that date fell on a Sunday, most agency dockets "
            "accept comments through the next business day, but the safe "
            "practice is to file by the preceding Friday. The consequence "
            "of missing it is that the comment is not part of the record "
            "the agency must consider. Now contrast a court deadline under "
            "Federal Rule of Civil Procedure 6: periods are stated in days, "
            "the trigger day is excluded from the count, every day counts "
            "including weekends, but if the last day is a Saturday, Sunday, "
            "or legal holiday, the period extends to the next business day, "
            "and three extra days are added when service was by mail. Same "
            "'count the days' idea, completely different machine. The "
            "professional habit is to write all three parts next to every "
            "deadline: trigger event and date, counting rule applied, and "
            "the exact consequence of missing it."
        ),
        "key_points": [
            "Every deadline has three parts: the trigger that starts the clock, the computation that counts the time, and the consequence that fires at zero.",
            "Always establish the trigger first - publication, service, year-end, grant, issuance - because nothing is due until the clock starts.",
            "The counting rule decides the date: calendar vs business days, whether the trigger day counts, weekend/holiday rollover, and whose holiday calendar.",
            "Consequences are specific and severe: rejected bids, ignored comments, penalties and interest, dead patents, defaulted cases.",
            "Record all three parts for every deadline; a date without its trigger, rule, and consequence is decoration, not tracking.",
        ],
        "requirements": [
            "An identified trigger event with its date, cited to the notice, statute, or rule that defines it.",
            "A stated computation rule: calendar or business days, trigger-day inclusion, weekend/holiday rollover, applicable holiday calendar.",
            "A computed due date with the arithmetic shown, so it can be rechecked by anyone.",
            "A stated consequence of missing the deadline, with the authority that imposes it.",
            "A verification step: an independent recomputation or a second pair of eyes before the deadline is calendared as final.",
        ],
        "standards": [
            "Federal court time computation follows FRCP Rule 6: exclude the trigger day, count every day, roll weekend/holiday endings to the next business day.",
            "Federal agency comment periods follow the APA notice-and-comment convention, 5 U.S.C. 553, with the closing date stated in the notice.",
            "Deadline dates are recorded in ISO 8601 (YYYY-MM-DD) with the jurisdiction and counting rule noted alongside.",
        ],
        "citations": [CIT_FRCP6, CIT_APA, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: trigger, computation, consequence - the "
            "doctrine calls these the summons, the measure, and the "
            "reckoning. Where the public tracker writes down a date, the "
            "Signature tracker writes down the covenant in full: what "
            "started it, how it is counted, and what honor demands at the "
            "end. A covenant half-written is a covenant half-kept."
        ),
    },
    {
        "key": "business_days",
        "name": "Business Days and Calendar Rules",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Not all days are equal in deadline arithmetic, and the "
            "difference between calendar days and business days has decided "
            "real cases, real bids, and real fines. Calendar days count "
            "every day on the calendar - weekends and holidays included. "
            "Business days count only the days the relevant offices are "
            "open: usually Monday through Friday, excluding public holidays "
            "of the governing jurisdiction. A '10 business days' deadline "
            "starting Monday lands two full weeks later, while '10 calendar "
            "days' lands on the following Thursday - a four-day gap that "
            "has sunk bids and filings. The complication is that 'business "
            "day' is jurisdiction-specific: a U.S. federal deadline skips "
            "federal holidays, a New York court deadline skips New York "
            "holidays, a London contract deadline skips English bank "
            "holidays, and some Middle Eastern jurisdictions treat Friday "
            "and Saturday as the weekend. Holiday observance rules add "
            "another layer: when a holiday falls on a weekend, many "
            "jurisdictions observe it on the adjacent Friday or Monday, and "
            "that observed day is the one skipped in the count. Then there "
            "is the rollover rule: when a computed deadline lands on a "
            "non-business day, most systems roll it forward to the next "
            "business day - but some roll it backward, and a few let it "
            "stand, meaning the real deadline was the preceding Friday. "
            "The only safe practice is to read the counting rule in the "
            "governing instrument, apply that jurisdiction's calendar, and "
            "file early enough that the rollover direction never matters."
        ),
        "how_it_works": (
            "Business-day computation works by walking the calendar and "
            "counting only qualifying days. Start from the trigger date and "
            "apply the trigger-day rule: many systems exclude the trigger "
            "day (FRCP Rule 6), some include it - the governing rule "
            "decides. Then step forward one day at a time, skipping "
            "Saturdays, Sundays, and the holidays of the governing "
            "jurisdiction, counting each qualifying day until the required "
            "number is reached. Check the holiday list first, including "
            "observed-holiday shifts: in the United States, when July 4 "
            "falls on a Saturday, it is observed on Friday July 3, and that "
            "Friday is skipped. When the count lands on a non-business day, "
            "apply the rollover rule from the governing instrument - usually "
            "forward to the next business day. Worked example: a 5-business-"
            "day response period triggered Thursday, June 30, 2022, "
            "excluding the trigger day, under the U.S. federal calendar "
            "(July 4 observed Monday July 4, 2022). Count: Friday July 1 "
            "(1), Monday July 4 is a holiday (skip), Tuesday July 5 (2), "
            "Wednesday July 6 (3), Thursday July 7 (4), Friday July 8 (5). "
            "Due date: Friday, July 8, 2022. Miss the holiday and you would "
            "have said July 7 - one day early, which is the safe direction "
            "to err, but the wrong answer on an exam or in a filing log. "
            "Always show the walk in writing so it can be audited."
        ),
        "key_points": [
            "Calendar days count every day; business days count only days the relevant offices are open - the gap between them decides real outcomes.",
            "Business day is jurisdiction-specific: federal, state, and foreign calendars skip different holidays and sometimes different weekends.",
            "Observed holidays (the Friday/Monday shift when a holiday falls on a weekend) are the skipped day, not the calendar date.",
            "The rollover rule decides what happens when a deadline lands on a non-business day: usually forward, sometimes backward, occasionally it stands.",
            "Show the day-by-day walk in writing and file early enough that the rollover direction never matters.",
        ],
        "requirements": [
            "The governing instrument's counting rule identified and quoted before any arithmetic is done.",
            "The correct jurisdiction's holiday calendar loaded, including observed-holiday shifts for the years spanned.",
            "A stated trigger-day rule: whether the trigger day is counted or excluded.",
            "A stated rollover rule for deadlines landing on non-business days.",
            "The full day-by-day walk recorded alongside the computed date, so the result is auditable.",
        ],
        "standards": [
            "Federal court computation follows FRCP Rule 6, including the 3-day addition for service by mail.",
            "Federal holidays are defined by 5 U.S.C. 6103 (New Year's, MLK Day, Presidents Day, Memorial Day, Juneteenth, Independence Day, Labor Day, Columbus Day, Veterans Day, Thanksgiving, Christmas).",
            "Deadline dates are recorded in ISO 8601 (YYYY-MM-DD) with the jurisdiction and calendar noted.",
        ],
        "citations": [CIT_FRCP6, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the doctrine counts days the way a sentry "
            "counts watches - only the days that stand count. Where the "
            "public counter skips a holiday by habit, the Signature counter "
            "names the jurisdiction, walks the calendar aloud, and writes "
            "down every step, because a covenant measured sloppily is a "
            "covenant broken. The walk is the proof."
        ),
    },
    {
        "key": "sources",
        "name": "Where Public Notices Come From",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Notices live in specific places, and each family of notices "
            "has its canonical sources - the feeds and bulletins where the "
            "notice first appears and carries authority. Federal regulatory "
            "notices live in the Federal Register, the daily journal "
            "created by the Federal Register Act, and in the dockets at "
            "Regulations.gov where comments are filed. Product recalls live "
            "with their regulators: FDA recalls at FDA.gov, vehicle recalls "
            "at NHTSA.gov, consumer-product recalls at CPSC.gov - each with "
            "searchable recall databases carrying the official notice "
            "text. Tenders live on procurement portals: SAM.gov for U.S. "
            "federal solicitations, plus state and municipal portals for "
            "their own buys. Court notices live on dockets: PACER for "
            "federal courts, state court e-filing systems for the rest. "
            "SEC filings live in EDGAR, the commission's public database. "
            "Patent and trademark deadlines are tracked against USPTO "
            "records and the MPEP's timing rules. Tax deadlines come from "
            "the Internal Revenue Code and IRS publications. Beyond the "
            "official channels there are aggregators, trade press, and "
            "alert services - useful for awareness, but never authoritative: "
            "when the aggregator and the official source disagree, the "
            "official source wins, always. The professional builds a source "
            "map: for each family, the canonical source, the backup source, "
            "the alert mechanism, and the check frequency. A notice that "
            "is never seen is a deadline that is never met."
        ),
        "how_it_works": (
            "Source monitoring works as a coverage map with a watch "
            "schedule. List the notice families you are exposed to - the "
            "products you sell, the regulations you operate under, the "
            "contracts you bid on, the filings you owe. For each family, "
            "identify the canonical source: the Federal Register for "
            "rulemakings, the three recall portals for product safety, "
            "SAM.gov for federal tenders, EDGAR for securities filings, the "
            "relevant dockets for litigation. Subscribe to every official "
            "alert mechanism available: Federal Register email updates, "
            "recall subscription feeds, SAM saved searches, docket "
            "notifications. Set a check frequency proportional to the "
            "stakes and the speed of the family: recall portals and "
            "procurement portals daily when active, the Federal Register "
            "daily for regulated industries, dockets on their briefing "
            "schedules. Log every check with its date so gaps are visible. "
            "Treat aggregators as tripwires and official sources as truth: "
            "when an aggregator flags something, verify it at the canonical "
            "source before acting, and cite the canonical source in your "
            "records. Review the source map quarterly - portals move, feeds "
            "change, new dockets open - because a dead feed is a blind spot."
        ),
        "key_points": [
            "Each notice family has canonical sources: the Federal Register for rulemakings, FDA/NHTSA/CPSC portals for recalls, SAM.gov for tenders, EDGAR for securities filings, dockets for courts.",
            "Aggregators and alert services are tripwires for awareness; the official source is the truth and wins every disagreement.",
            "Build a source map: canonical source, backup source, alert mechanism, and check frequency for every family you are exposed to.",
            "Set check frequency by stakes and speed: daily for active recalls and procurements, on-schedule for dockets and comment periods.",
            "Log every check with its date and review the source map quarterly, because portals move and dead feeds become blind spots.",
        ],
        "requirements": [
            "An exposure inventory: the products, regulations, contracts, filings, and cases that create your notice surface.",
            "The canonical source identified for each family, with its URL and alert mechanism recorded.",
            "Official alert subscriptions activated wherever the source offers them.",
            "A check schedule with frequencies tied to stakes, logged with dates.",
            "A quarterly source-map review to catch moved portals, changed feeds, and new dockets.",
        ],
        "standards": [
            "Federal rules and notices are authoritative in the Federal Register under 44 U.S.C. 1501-1511; docket comments file at Regulations.gov.",
            "FDA, NHTSA, and CPSC recall notices are authoritative on the agencies' own portals under 21 CFR Part 7, 49 U.S.C. 30118-30120, and 15 U.S.C. 2064.",
            "Federal solicitations are authoritative on SAM.gov under the FAR, 48 CFR Part 5.",
        ],
        "citations": [CIT_FR_ACT, CIT_FDA_RECALL, CIT_NHTSA, CIT_CPSC, CIT_FAR],
        "sig_lens": (
            "The Signature read: the doctrine posts sentries, not "
            "subscribers. Where the public watcher hopes the feed catches "
            "it, the Signature watcher maps every gate a summons can enter "
            "through and stands a watch at each - canonical source, backup "
            "source, alert, and schedule. A summons unseen is a covenant "
            "broken before it began."
        ),
    },
    {
        "key": "channels",
        "name": "Notice Channels and Publication Requirements",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A notice is only legally effective if it travels through the "
            "channel the law requires, which is why publication requirements "
            "matter as much as the notice text. The channel is the medium "
            "and venue: the Federal Register, a newspaper of general "
            "circulation, a posted sign at the site, a court docket, a "
            "procurement portal, certified mail to the affected party. The "
            "publication requirement is the rule that names the channel, "
            "the frequency, and the duration: publish once a week for three "
            "weeks, post for thirty days, mail by certified mail return "
            "receipt requested. These requirements exist because notice must "
            "be reasonably calculated to reach the affected people - the "
            "constitutional standard from Mullane v. Central Hanover Bank "
            "(1950). A zoning change published only on an obscure webpage "
            "when the ordinance requires newspaper publication can be "
            "voided; a recall announced only by press release when the "
            "statute requires direct notification to known owners fails its "
            "duty. Channels have also modernized: the Federal Register is "
            "electronic, dockets are e-filed, SAM.gov replaced paper "
            "solicitation postings, and agencies run email and text alert "
            "systems. But modernization does not relax the requirement - it "
            "moves it. The professional reads the publication requirement "
            "in the governing instrument before trusting that a notice was "
            "properly given, and when issuing a notice, follows the "
            "requirement to the letter and keeps the affidavit or receipt "
            "that proves it."
        ),
        "how_it_works": (
            "Publication requirements work as a checklist attached to the "
            "notice type. Identify the governing instrument - the statute, "
            "rule, or ordinance that requires the notice - and read its "
            "publication section. It will name the channel (which "
            "publication, which portal, which posting location), the "
            "frequency (how many times), the duration (over how many days "
            "or weeks), the timing (how far before the hearing, the "
            "effective date, the deadline), and the proof (affidavit of "
            "publication, certified mail receipt, posting photograph with "
            "date). Execute each element and collect the proof as you go: "
            "the newspaper's affidavit, the portal's confirmation screen, "
            "the mail receipt, the dated photograph of the posted sign. "
            "For incoming notices, reverse the checklist: was this notice "
            "published where the law requires, for the required duration? "
            "If a required channel is missing, the notice may be "
            "defective - which can extend your response time or invalidate "
            "the action, a point to raise with counsel rather than to "
            "assume. Keep the proof of your own publications permanently; "
            "challenges to notice arrive years later, and the affidavit is "
            "the only witness that does not forget."
        ),
        "key_points": [
            "A notice is legally effective only through the channel the governing law requires; the wrong channel can void the notice.",
            "The constitutional standard is notice reasonably calculated to reach affected people (Mullane v. Central Hanover Bank, 1950).",
            "Publication requirements name the channel, frequency, duration, timing, and the proof required.",
            "For incoming notices, verify the channel against the requirement - a defective notice may extend response time or invalidate the action.",
            "Keep proof of every publication permanently: affidavits, receipts, and confirmations are the witnesses that do not forget.",
        ],
        "requirements": [
            "The governing instrument's publication section read and quoted before any notice is issued or trusted.",
            "The required channel, frequency, duration, and timing each executed and documented.",
            "Proof of publication collected at the time: affidavits, mail receipts, portal confirmations, dated photographs.",
            "For incoming notices, a channel-validity check against the governing requirement.",
            "Permanent retention of publication proof, filed by notice identifier.",
        ],
        "standards": [
            "Federal notices publish in the Federal Register under the Federal Register Act, 44 U.S.C. 1501-1511.",
            "Notice must be reasonably calculated to inform affected parties (Mullane v. Central Hanover Bank, 339 U.S. 306 (1950)).",
            "Federal contract actions are publicized per the FAR, 48 CFR Part 5, including synopsis timing thresholds.",
        ],
        "citations": [CIT_FR_ACT, CIT_FAR],
        "sig_lens": (
            "The Signature read: the channel is the road the summons "
            "travels, and the doctrine walks the road before trusting the "
            "message. Where the public reader accepts a notice at face "
            "value, the Signature reader checks the publication "
            "requirement first - because a summons delivered by the wrong "
            "road may be no summons at all, and a summons properly "
            "published binds like iron."
        ),
    },
    {
        "key": "severity",
        "name": "Advisory Severity Classification",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Not every warning deserves the same response, so advisory "
            "systems grade severity - and reading the grade correctly is a "
            "core tracking skill. Severity classification answers one "
            "question: how bad is it, and how fast must we act. The common "
            "pattern across agencies is a four-level scale. Informational "
            "advisories share knowledge with no required action: a new "
            "guidance document, a data release, a scheduled maintenance "
            "window. Watch advisories flag a developing situation worth "
            "monitoring: an emerging defect pattern, a proposed rule that "
            "could affect you, a weather system that might turn. Warning "
            "advisories demand action within a stated window: a product "
            "with a confirmed defect, a comment period closing, a storm "
            "likely to strike. Critical or emergency advisories demand "
            "immediate action: a Class I recall with deaths reported, an "
            "imminent safety threat, a filing deadline today. The FDA's "
            "recall classes are the sharpest example: Class I means "
            "reasonable probability of serious adverse health consequences "
            "or death, Class II means reversible or remote probability of "
            "serious harm, Class III means no adverse health consequences "
            "expected. Misreading severity in either direction is costly: "
            "treating a warning as informational leaves people exposed, "
            "while treating information as critical burns attention and "
            "budget on noise. The professional habit is to record the "
            "severity level as issued, map it to the local response scale, "
            "and let the level - not the headline - set the tempo."
        ),
        "how_it_works": (
            "Severity classification works by scoring the hazard on two "
            "axes - likelihood and impact - and mapping the score to a "
            "response level. Likelihood asks how probable the harm is: "
            "confirmed and occurring, probable, possible but remote, or "
            "theoretical. Impact asks how bad it is: death or serious "
            "injury, reversible injury, economic loss, or mere "
            "inconvenience. The combination sets the level: confirmed "
            "likelihood with severe impact is critical; remote likelihood "
            "with mild impact is informational. Agencies publish their own "
            "mappings - the FDA's three recall classes, the National "
            "Weather Service's advisory/watch/warning ladder, CISA's alert "
            "levels - and the tracker records the level as issued rather "
            "than inventing its own. Then the local response matrix maps "
            "each level to a tempo: informational gets logged and filed, "
            "watch gets a monitoring owner and a check-in date, warning "
            "gets an action owner and a deadline, critical gets an incident "
            "commander and immediate escalation. When an advisory's severity "
            "changes - and they do, as investigations develop - the tracker "
            "updates the level, re-maps the response, and logs the change "
            "with its timestamp, because the audit trail must show what "
            "was known when."
        ),
        "key_points": [
            "Severity classification answers how bad it is and how fast to act, usually on a four-level scale: informational, watch, warning, critical.",
            "The FDA recall classes are the sharpest model: Class I (serious harm or death probable), Class II (reversible or remote), Class III (no harm expected).",
            "Score severity on likelihood times impact, then map the level to a response tempo: log, monitor, act, escalate.",
            "Record the severity as issued by the authority; do not invent private grades that confuse the audit trail.",
            "When severity changes as facts develop, update the level, re-map the response, and log the change with its timestamp.",
        ],
        "requirements": [
            "The issued severity level recorded verbatim from the advisory or recall notice.",
            "A local response matrix mapping each level to an owner, a tempo, and a deadline rule.",
            "Likelihood and impact assessed separately before the level is accepted or challenged.",
            "Severity changes logged with timestamps, showing what was known when.",
            "Periodic review of watch-level items so developing situations are re-graded before they become warnings.",
        ],
        "standards": [
            "FDA recall classifications follow 21 CFR Part 7, sections 7.3 and 7.41-7.59 (Class I, II, III).",
            "Consumer-product hazard reporting follows 15 U.S.C. 2064 (CPSC section 15).",
            "Motor-vehicle defect notification follows 49 U.S.C. 30118-30120 (NHTSA).",
        ],
        "citations": [CIT_FDA_RECALL, CIT_CPSC, CIT_NHTSA],
        "sig_lens": (
            "The Signature read: severity is the measure of the warning, "
            "and the doctrine measures twice. Where the public reader feels "
            "the headline, the Signature reader scores likelihood against "
            "impact and lets the level set the tempo - log, monitor, act, "
            "escalate. A warning misread is a covenant misjudged: too "
            "light and people are exposed, too heavy and the watch is "
            "exhausted before the real alarm."
        ),
    },
    {
        "key": "compliance_read",
        "name": "Reading a Notice: The Compliance Read",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A compliance read is a disciplined way of reading a notice "
            "that extracts every obligation, every date, and every trap in "
            "a single pass. Ordinary reading follows the prose; a "
            "compliance read hunts the operative language. Start with the "
            "verbs: shall, must, and required create duties; may and should "
            "create permissions and expectations; will states what the "
            "authority itself intends to do. Circle every date and ask what "
            "it triggers - publication, effectiveness, comment close, "
            "compliance, expiration - because notices routinely carry five "
            "or six dates and only one or two bind you. Flag the "
            "definitions section, because regulatory notices redefine "
            "ordinary words: 'business day,' 'affected product,' 'small "
            "entity' may all carry special meanings that change who must "
            "act. Extract the scope: which products, which facilities, "
            "which transactions, which people are covered, and just as "
            "important, the exemptions and exclusions that carve you out. "
            "Note the response mechanics: where to file, in what format, "
            "with what fee, by what method - a comment filed to the wrong "
            "docket or a form filed on paper when electronic filing is "
            "required does not count. And read the penalty section before "
            "you decide how urgently to act; the consequence calibrates the "
            "tempo. The output of a compliance read is not understanding - "
            "it is a one-page extraction sheet: obligations, dates, scope, "
            "mechanics, penalties, and open questions for counsel. File the "
            "sheet with the notice; it becomes the tracking record."
        ),
        "how_it_works": (
            "The compliance read works as a six-pass extraction. Pass one: "
            "verbs - mark every shall, must, required, may, should, and "
            "will, and list the duties they create. Pass two: dates - list "
            "every date, label what each triggers, and identify which bind "
            "you. Pass three: definitions - read the defined terms and "
            "rewrite the duties with the definitions substituted, because "
            "the plain-English reading is often wrong. Pass four: scope - "
            "write down exactly who and what is covered and who is "
            "exempted, in your own words, and check your operations against "
            "both lists. Pass five: mechanics - record where, how, in what "
            "format, and with what fee each response must be made. Pass six: "
            "penalties - record the consequence of each missed duty. Then "
            "produce the extraction sheet: a single page with obligations "
            "as checkable items, dates in ISO order with their triggers, "
            "scope as covered/exempt lists, mechanics as filing "
            "instructions, penalties as the cost of failure, and open "
            "questions flagged for counsel. Two readers should do passes "
            "one and two independently on high-stakes notices; "
            "disagreements between readers are where the traps hide."
        ),
        "key_points": [
            "Hunt operative language: shall/must/required create duties, may/should create expectations, will states the authority's intent.",
            "Circle every date and label its trigger; notices carry many dates but only one or two bind you.",
            "Read the definitions and substitute them into the duties - the plain-English reading is often wrong.",
            "Extract scope as covered and exempted lists, and check your operations against both.",
            "Output a one-page extraction sheet - obligations, dates, scope, mechanics, penalties, open questions - and file it as the tracking record.",
        ],
        "requirements": [
            "The full notice text preserved as received, with its identifier and publication date.",
            "A verb pass marking every operative shall, must, required, may, and should.",
            "A date inventory with each date labeled by what it triggers and whether it binds the reader.",
            "A scope statement in the reader's own words, listing covered and exempted items.",
            "The extraction sheet filed with the notice, signed and dated by the reader.",
        ],
        "standards": [
            "Regulatory text is read with its defined terms substituted, per standard administrative-law practice under the APA, 5 U.S.C. 553.",
            "Filing mechanics follow the notice's stated method; federal docket comments file at Regulations.gov.",
            "Dates on the extraction sheet use ISO 8601 (YYYY-MM-DD) with the trigger labeled.",
        ],
        "citations": [CIT_APA, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the compliance read is the doctrine's "
            "interrogation of the summons. Where the casual reader absorbs "
            "the prose, the Signature reader puts the notice through six "
            "passes - verbs, dates, definitions, scope, mechanics, "
            "penalties - until the summons confesses everything it "
            "demands. The extraction sheet is the signed testimony: what "
            "is owed, when, and what honor costs if it is not paid."
        ),
    },
    {
        "key": "tracking_workflow",
        "name": "Notice Tracking Workflows",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A notice tracking workflow is the standard path a notice "
            "travels from arrival to closure, and running every notice "
            "through the same path is what makes deadlines stop slipping. "
            "The workflow has six stages. Intake captures the notice: the "
            "full text, its identifier, its source, the date received, and "
            "who received it. Triage classifies it: which of the six "
            "families, what severity, who owns it, how urgent. Extraction "
            "pulls the operative parts: obligations, dates, scope, "
            "mechanics, penalties - the compliance read, filed as the "
            "extraction sheet. Calendaring computes every deadline with its "
            "trigger, counting rule, and consequence, and places alarms at "
            "lead times before each date. Action executes the response: the "
            "comment filed, the product returned, the bid submitted, the "
            "report filed, the renewal paid. Closure verifies completion: "
            "the acceptance receipt, the confirmation number, the filed "
            "copy - and only with evidence in hand is the notice closed. "
            "Notices stall at predictable points: triage without an owner, "
            "extraction without dates, calendaring without alarms, action "
            "without confirmation, closure without evidence. The workflow "
            "defeats each stall with a rule: no notice advances without an "
            "owner, no deadline is calendared without its counting rule, no "
            "action counts without its receipt, no notice closes without "
            "evidence. Run on paper, on a spreadsheet, or in software - the "
            "discipline is the same, and the discipline is the product."
        ),
        "how_it_works": (
            "The workflow works as a state machine with entry and exit "
            "rules for each stage. A notice enters intake when it is "
            "received; it leaves intake when the text, identifier, source, "
            "and receipt date are recorded. It enters triage; it leaves "
            "when family, severity, owner, and urgency are assigned - a "
            "notice with no owner cannot leave triage. It enters "
            "extraction; it leaves when the extraction sheet is filed. It "
            "enters calendaring; it leaves when every deadline is computed "
            "with trigger, rule, and consequence, and alarms are set. It "
            "enters action; it leaves when the response is executed and the "
            "receipt or confirmation is captured. It enters closure; it "
            "leaves - and the record is archived - when the evidence is "
            "verified against the obligation: does the receipt match what "
            "the notice demanded, filed where it demanded, by when it "
            "demanded. A weekly review sweeps all open notices: anything "
            "past its alarm without action escalates to the owner's "
            "manager; anything in triage more than two business days old "
            "gets an owner assigned by force. Metrics keep the workflow "
            "honest: notices closed on time, average days in each stage, "
            "escalations per month. The numbers reveal whether the "
            "workflow is working or merely existing."
        ),
        "key_points": [
            "The six stages are intake, triage, extraction, calendaring, action, and closure - every notice travels the same path.",
            "Each stage has exit rules: no owner, no exit from triage; no counting rule, no exit from calendaring; no receipt, no exit from action.",
            "Closure requires evidence verified against the obligation: the right thing, filed the right way, in the right place, on time.",
            "A weekly sweep escalates stalled notices: past-alarm items go to management, ownerless triage items get owners by force.",
            "Metrics - on-time closure rate, days per stage, escalations - reveal whether the workflow works or merely exists.",
        ],
        "requirements": [
            "A single intake point where every notice is captured with text, identifier, source, and receipt date.",
            "Mandatory triage fields: family, severity, owner, urgency - no notice advances without them.",
            "An extraction sheet filed per notice, with obligations, dates, scope, mechanics, and penalties.",
            "Calendared deadlines carrying trigger, counting rule, consequence, and lead-time alarms.",
            "Closure evidence verified against the original obligation before the record is archived.",
        ],
        "standards": [
            "Tracking records carry the notice identifier and ISO 8601 dates with triggers labeled.",
            "Evidence of compliance is retained per the governing record-retention rule for the notice family.",
            "Audit access: every stage transition is timestamped and attributable to a person.",
        ],
        "citations": [CIT_ISO8601, CIT_FR_ACT],
        "sig_lens": (
            "The Signature read: the workflow is the doctrine's chain of "
            "custody for a summons. Where the public office hopes the "
            "notice gets handled, the Signature office moves it through "
            "six guarded gates - intake, triage, extraction, calendaring, "
            "action, closure - and no gate opens without its toll: an "
            "owner, a counting rule, a receipt, evidence. A summons that "
            "stalls is a covenant abandoned; the sweep finds it."
        ),
    },
    {
        "key": "compliance_calendar",
        "name": "Compliance Calendars",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A compliance calendar is the single view of every deadline "
            "you owe, and it is the most important artifact in notice "
            "tracking. Scattered deadlines - one in email, one on a "
            "lawyer's desk, one remembered by the office manager - are how "
            "obligations die. The compliance calendar gathers them into one "
            "place where each entry carries the full deadline anatomy: the "
            "obligation in plain words, the notice it came from, the "
            "trigger event and date, the counting rule, the computed due "
            "date, the consequence of missing it, the owner, and the alarm "
            "schedule. Alarms are set at lead times, not at the deadline: "
            "a filing due April 15 gets alarms at 60, 30, 14, 7, and 2 "
            "days, because the work of complying takes time and the alarm "
            "at the deadline is a eulogy. The calendar distinguishes hard "
            "deadlines from soft ones: hard deadlines are imposed by law "
            "or contract and carry penalties, soft deadlines are internal "
            "targets that protect the hard ones. It also carries recurring "
            "obligations - quarterly filings, annual renewals, monthly "
            "reports - generated forward for the full year so nothing "
            "depends on memory. Review the calendar weekly: confirm owners, "
            "advance preparations, close completed items with evidence. The "
            "calendar is a living document, updated at intake of every new "
            "notice and at closure of every completed obligation. An "
            "organization with one current compliance calendar has a "
            "nervous system; without one, it has only hope."
        ),
        "how_it_works": (
            "A compliance calendar works by making every deadline visible, "
            "owned, and alarmed. Build it as a table - spreadsheet or "
            "software - with columns for obligation, source notice and "
            "identifier, trigger, counting rule, due date, consequence, "
            "owner, status, and evidence. Populate it from three streams: "
            "new notices at intake, recurring obligations generated for the "
            "year ahead, and expirations with their renewal lead times. For "
            "each entry, compute the due date with the governing counting "
            "rule, then set alarms backward from the due date at lead times "
            "matched to the work: a 10-K needs months of lead time, a "
            "comment letter needs weeks, a renewal payment needs days. "
            "Mark each entry hard or soft. Each week, the owner reviews "
            "their entries: upcoming alarms become work plans, completed "
            "obligations get their evidence attached and their status set "
            "to closed, and anything without an owner gets one. Monthly, "
            "audit the calendar itself: are all open notices represented, "
            "are recurring obligations generated forward, are alarms firing "
            "to the right people. The calendar earns trust by being "
            "complete and current; the day it is doubted, people keep "
            "private lists, and the discipline collapses back into hope."
        ),
        "key_points": [
            "One calendar holds every deadline with its full anatomy: obligation, source, trigger, counting rule, due date, consequence, owner, alarms.",
            "Set alarms at lead times before the deadline - 60, 30, 14, 7, 2 days - because the work of complying takes time.",
            "Distinguish hard deadlines (law or contract, with penalties) from soft ones (internal targets protecting the hard ones).",
            "Generate recurring obligations forward for the full year: quarterly filings, annual renewals, monthly reports.",
            "Review weekly by owner and audit monthly for completeness; a doubted calendar breeds private lists and collapses the discipline.",
        ],
        "requirements": [
            "A single calendar artifact - one table, one system - holding every deadline owed.",
            "Full deadline anatomy on each entry: trigger, counting rule, due date, consequence, owner.",
            "Lead-time alarms on every entry, scaled to the work the obligation requires.",
            "Recurring obligations generated forward twelve months with their renewal lead times.",
            "Weekly owner reviews and monthly completeness audits, with evidence attached at closure.",
        ],
        "standards": [
            "Calendar dates use ISO 8601 (YYYY-MM-DD) with the trigger and counting rule noted per entry.",
            "Recurring statutory dates follow their governing codes (e.g., IRC 26 U.S.C. 6072 for tax filings).",
            "Closed entries retain their evidence per the applicable record-retention rule.",
        ],
        "citations": [CIT_ISO8601, CIT_IRC],
        "sig_lens": (
            "The Signature read: the compliance calendar is the doctrine's "
            "honor roll - every covenant owed, written where all can see. "
            "Where the public office keeps dates, the Signature office "
            "keeps promises: each entry a sworn debt with its trigger, its "
            "measure, and its reckoning named. Alarms are the sentries "
            "posted before the debt comes due. An honor roll doubted is "
            "honor abandoned."
        ),
    },
    {
        "key": "expiration",
        "name": "Expiration Dates, Renewals, and Grace Periods",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Expiration dates are the quietest killers in the deadline "
            "world: unlike a recall or a lawsuit, nothing announces them "
            "except the calendar you keep. A license expires, a "
            "certification lapses, a patent dies for unpaid maintenance "
            "fees, a trademark registration cancels for a missed affidavit, "
            "a domain name drops, an insurance policy terminates - and in "
            "most cases the world does not send a reminder. The anatomy of "
            "an expiration has four dates, not one: the expiration date "
            "itself, the renewal window (the period before expiration when "
            "renewal is accepted, often 90 days to one year), the grace "
            "period (the period after expiration when late renewal is still "
            "allowed, usually with a surcharge), and the death date (when "
            "the right is truly gone). Confusing the grace period for an "
            "extension is the classic error: during grace you still hold a "
            "diminished right - a patent in grace cannot be enforced the "
            "same way, a lapsed license may forbid practice - and after the "
            "death date, revival ranges from expensive to impossible. Patent "
            "maintenance fees illustrate the stakes: due at 3.5, 7.5, and "
            "11.5 years after grant, with a six-month grace period and "
            "surcharges, and an unintentionally lapsed patent requires a "
            "petition and fee to revive. Trademark registrations need "
            "affidavits of use between years five and six and renewal every "
            "ten years. The defense is a renewal calendar with alarms at "
            "the renewal window opening, not at expiration - by expiration, "
            "you are already in grace."
        ),
        "how_it_works": (
            "Expiration management works by tracking four dates per right "
            "and alarming on the earliest. For each license, certification, "
            "registration, or right, record the grant or issuance date, the "
            "term length, and the governing renewal rule. Compute the "
            "expiration date, then work backward: find the renewal window "
            "opening (often 90 days to a year before expiration), the grace "
            "period length and its surcharge, and the death date after "
            "which revival is unavailable or punitive. Set the primary "
            "alarm at the renewal window opening - that is when action "
            "should start - with follow-ups at 60, 30, and 7 days before "
            "expiration, and a final alarm at the grace period midpoint for "
            "anything still open. Example: a trademark registered March "
            "10, 2020 needs its section 8 affidavit between March 10, 2025 "
            "and March 10, 2026, with a six-month grace period to September "
            "10, 2026 carrying a surcharge. The alarm goes at March 10, "
            "2025 - the window opening - not at the 2026 deadline. For "
            "portfolios of many rights, sort the calendar by window-opening "
            "date and work it like a production line. Never let an "
            "expiration be discovered at expiration; discovered at the "
            "window opening, it is routine paperwork."
        ),
        "key_points": [
            "Every expiration has four dates: expiration, renewal window opening, grace period, and death date - track all four.",
            "Alarm at the renewal window opening, not at expiration; by expiration you are already in grace with diminished rights.",
            "Grace is not extension: rights during grace are diminished, surcharges apply, and after the death date revival is expensive or impossible.",
            "Patent maintenance fees fall at 3.5, 7.5, and 11.5 years with six-month grace; trademarks need section 8 affidavits and ten-year renewals.",
            "Run portfolios by window-opening date like a production line; never discover an expiration at expiration.",
        ],
        "requirements": [
            "A register of every time-limited right: licenses, certifications, registrations, patents, trademarks, domains, policies.",
            "All four dates computed and recorded per right: expiration, window opening, grace end, death date.",
            "Primary alarms at renewal window openings with escalating follow-ups.",
            "The governing renewal rule cited per right, with surcharge and revival terms noted.",
            "Renewal confirmations filed as closure evidence before the record is archived.",
        ],
        "standards": [
            "U.S. patent maintenance fees follow 35 U.S.C. 41(b): due at 3.5, 7.5, and 11.5 years after grant, with a six-month grace period.",
            "U.S. trademark affidavits of use and renewals follow the Lanham Act, 15 U.S.C. 1058-1059.",
            "State corporate filings follow state law, e.g., 8 Del. C. 502 for Delaware franchise tax reports.",
        ],
        "citations": [CIT_MAINT, CIT_LANHAM, CIT_DEL],
        "sig_lens": (
            "The Signature read: expirations are the silent summonses, and "
            "the doctrine fears silence most. Where the public holder "
            "waits for a reminder that never comes, the Signature holder "
            "posts the alarm at the window opening - the covenant renewed "
            "before it is even threatened. Four dates, one honor: the "
            "right kept alive is the promise kept early."
        ),
    },
    {
        "key": "recall_anatomy",
        "name": "Product Recalls: Anatomy of a Recall",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A product recall is the most urgent family of public notices: "
            "it orders unsafe products out of the field, and its anatomy "
            "is designed for speed. The recall notice opens with "
            "identification: the product name, model numbers, serial "
            "number ranges, date codes, and manufacturing dates that "
            "define exactly which units are affected - precision here is "
            "everything, because over-broad recalls waste millions and "
            "under-broad recalls leave hazards in homes. Next comes the "
            "hazard description: what goes wrong, under what conditions, "
            "and what injuries or damage have been reported, with incident "
            "counts. Then the remedy: what the consumer or owner should do "
            "- stop using it, return it, bring it to a dealer, accept a "
            "repair kit - stated as imperative steps with a contact method. "
            "The notice carries its classification (FDA Class I, II, III, "
            "or the agency's equivalent), the recall number for tracking, "
            "and the distribution scope: how many units, sold where, over "
            "what dates. For the recalling company, the anatomy extends "
            "behind the notice: the decision record showing when the "
            "defect was known, the notification plan for distributors and "
            "owners, the remedy logistics, and the progress reports the "
            "regulator requires until closure. Recalls are graded by "
            "severity, tracked by number, and closed only when the remedy "
            "reaches a satisfactory share of the affected units. Reading a "
            "recall notice means answering three questions in order: is my "
            "unit in the affected range, what is the hazard, and what is "
            "the remedy - everything else is context."
        ),
        "how_it_works": (
            "A recall works through a chain that starts before the public "
            "notice ever appears. A company learns of a defect pattern - "
            "from warranty claims, incident reports, or its own testing - "
            "and evaluates whether it constitutes a substantial product "
            "hazard. For consumer products, 15 U.S.C. 2064 requires "
            "reporting to the CPSC; for vehicles, 49 U.S.C. 30118 requires "
            "notification of defects; for FDA-regulated products, 21 CFR "
            "Part 7 governs the recall procedure. The company and the "
            "agency agree on the scope (which units), the classification "
            "(how severe), and the remedy (repair, replace, refund). The "
            "public notice issues through the agency portal, press "
            "release, and direct notification to known owners - dealers "
            "and retailers are notified through the distribution chain. "
            "Consumers respond by following the remedy steps. The company "
            "files periodic status reports: notices sent, responses "
            "received, remedies completed, units still outstanding. The "
            "regulator closes the recall when the response rate satisfies "
            "the plan or when further effort is deemed unproductive - but "
            "the duty to remedy typically survives closure for owners who "
            "appear later. For the tracker, a recall notice creates "
            "immediate obligations: check inventory and installed base "
            "against the affected range today, quarantine suspect units, "
            "notify downstream customers, and calendar the status-report "
            "deadlines the regulator sets."
        ),
        "key_points": [
            "A recall notice identifies affected units precisely (models, serials, date codes), describes the hazard with incident counts, and states the remedy as imperative steps.",
            "The recall chain starts before publication: defect evaluation, agency reporting, agreed scope, classification, and remedy plan.",
            "Distribution flows through agency portals, press, direct owner notification, and the dealer/retailer chain.",
            "Status reports track notices sent, responses, remedies completed, and outstanding units until the regulator closes the recall.",
            "On receipt: check inventory against the affected range today, quarantine suspects, notify downstream customers, calendar the report deadlines.",
        ],
        "requirements": [
            "The affected-unit definition precise enough to sort inventory: models, serial ranges, date codes, manufacturing dates.",
            "The hazard description with conditions of failure and reported incident counts.",
            "The remedy stated as ordered steps with contact methods and any cost coverage.",
            "The recall number, classification, and distribution scope recorded as tracking keys.",
            "The regulator's status-report schedule calendared with owners assigned.",
        ],
        "standards": [
            "FDA recalls follow 21 CFR Part 7 (classification, notification, and termination procedures).",
            "Motor-vehicle defect notification and remedy follow 49 U.S.C. 30118-30120.",
            "Consumer-product hazard reporting follows 15 U.S.C. 2064 (CPSC section 15).",
        ],
        "citations": [CIT_FDA_RECALL, CIT_NHTSA, CIT_CPSC],
        "sig_lens": (
            "The Signature read: a recall is the loudest summons the "
            "doctrine knows - the call to pull danger out of the world. "
            "Where the public company weighs the cost of the remedy, the "
            "Signature company weighs the covenant: the product was a "
            "promise, the defect broke it, and the recall is the "
            "promise repaired in public. Speed is honor; precision is "
            "mercy; the status report is the testimony."
        ),
    },
    {
        "key": "recall_classes",
        "name": "Recall Classes and Severity Levels",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Recall classes are the severity grades that tell everyone - "
            "regulators, companies, and the public - how dangerous a "
            "defect is and how urgently it must be handled. The FDA's "
            "three-class system is the reference model used across "
            "industries. Class I is the most serious: a reasonable "
            "probability that use of the product will cause serious "
            "adverse health consequences or death - think contaminated "
            "food, a failing pacemaker lead, a vehicle airbag that "
            "explodes. Class II is moderate: use may cause temporary or "
            "medically reversible harm, or the probability of serious harm "
            "is remote - a mislabeled drug at the wrong strength, a "
            "vehicle defect affecting handling. Class III is the least "
            "severe: use is not likely to cause adverse health "
            "consequences - a minor labeling violation, a cosmetic defect "
            "in packaging. The classification is assigned by the agency "
            "after evaluating the hazard, the exposure, and the population "
            "at risk - not by the recalling company, though the company "
            "proposes it. The class drives everything downstream: the "
            "urgency of public notification, the depth of the distribution "
            "check, the intensity of the effectiveness monitoring, and the "
            "speed the regulator demands. Other agencies run parallel "
            "scales - NHTSA grades by safety risk, CPSC by substantial "
            "hazard - but the logic is identical: likelihood times impact "
            "sets the class, and the class sets the tempo. For the "
            "tracker, the class is recorded verbatim at intake and mapped "
            "to the local response matrix: Class I means incident command "
            "today, Class III means orderly correction on schedule."
        ),
        "how_it_works": (
            "Classification works as a hazard evaluation with a fixed "
            "output scale. The evaluator gathers the facts: the defect "
            "mechanism, the conditions that trigger it, the exposed "
            "population, the incident history with injury counts, and any "
            "vulnerable subpopulations (children, the elderly, the "
            "immunocompromised). Then it scores the two axes. Likelihood: "
            "is serious harm reasonably probable, possible but remote, or "
            "not expected. Impact: death or serious injury, temporary or "
            "reversible harm, or no health consequence. The matrix maps the "
            "combination to the class: probable serious harm is Class I; "
            "remote or reversible harm is Class II; no expected harm is "
            "Class III. The agency reviews the company's proposed "
            "classification and issues the final one - the tracker records "
            "the issued class, never the proposed one, because the issued "
            "class is what the audit trail and the public record carry. "
            "Reclassification happens when facts change: new injuries can "
            "raise a Class II to Class I, and the tracker must update the "
            "level, re-map the response tempo, and log the change with its "
            "date. Worked rule of thumb: if you are debating between Class "
            "I and Class II, treat it as Class I until the agency says "
            "otherwise - the cost of over-response is money, the cost of "
            "under-response is harm."
        ),
        "key_points": [
            "Class I: reasonable probability of serious harm or death. Class II: temporary/reversible or remote serious harm. Class III: no adverse health consequences expected.",
            "The agency assigns the final classification after evaluating hazard, exposure, and population at risk - not the recalling company.",
            "The class drives notification urgency, distribution-check depth, monitoring intensity, and regulator-demanded speed.",
            "Record the issued class verbatim; reclassifications are logged with dates as facts develop.",
            "When debating Class I vs Class II, respond as Class I until the agency rules - over-response costs money, under-response costs harm.",
        ],
        "requirements": [
            "The hazard facts assembled: defect mechanism, trigger conditions, exposed population, incident and injury counts.",
            "Likelihood and impact scored separately before the class is accepted.",
            "The issued classification recorded verbatim with the recall number.",
            "A response matrix mapping each class to owner, tempo, and deadline rules.",
            "Reclassification events logged with timestamps and re-mapped responses.",
        ],
        "standards": [
            "FDA recall classifications are defined at 21 CFR 7.3 and the classification process at 21 CFR 7.41-7.59.",
            "Health-hazard evaluation is the formal basis for FDA classification decisions.",
            "NHTSA and CPSC apply their parallel severity frameworks under 49 U.S.C. 30118-30120 and 15 U.S.C. 2064.",
        ],
        "citations": [CIT_FDA_RECALL, CIT_NHTSA, CIT_CPSC],
        "sig_lens": (
            "The Signature read: three classes, three measures of the "
            "warning, and the doctrine honors each exactly. Where the "
            "public debater argues the class down to save the quarter, "
            "the Signature evaluator argues it up to save the person - "
            "Class I means the full alarm today. The class is the "
            "covenant's weight; carry it at its true weight."
        ),
    },
    {
        "key": "regulatory_comment",
        "name": "Regulatory Changes and Comment Periods",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Regulatory changes are the notices that rewrite the rules "
            "themselves, and the comment period is the public's formal "
            "chance to shape them. Under the Administrative Procedure Act, "
            "a federal agency proposing a rule must publish a notice of "
            "proposed rulemaking in the Federal Register, describe the "
            "proposal and its legal basis, and give interested persons an "
            "opportunity to submit written comments - typically 30 to 90 "
            "days, sometimes longer for major rules. The agency must then "
            "consider the comments and respond to significant issues in "
            "the final rule's preamble; a comment ignored on a material "
            "point can be grounds for a court to vacate the rule. This "
            "makes the comment deadline one of the highest-leverage dates "
            "in public life: a well-supported comment filed on time "
            "becomes part of the record the agency must answer and the "
            "court will review, while the same argument made a day late "
            "is not in the record at all. Tracking regulatory change "
            "means watching three stages: the advance notice or agenda "
            "that signals what is coming, the proposed rule with its "
            "comment deadline, and the final rule with its effective date "
            "and compliance deadlines. States run parallel systems with "
            "their own registers and comment rules. The professional "
            "maintains a rulemaking watchlist: the dockets that affect "
            "their operations, the comment deadlines open now, and the "
            "final rules whose compliance dates are approaching - because "
            "a rule you did not comment on can still bind you on its "
            "effective date."
        ),
        "how_it_works": (
            "The notice-and-comment cycle works in four beats. Beat one: "
            "the agency publishes the notice of proposed rulemaking with "
            "the proposal text, the legal authority, the issues on which "
            "comment is sought, and the closing date and docket for "
            "comments. Beat two: the public comments - anyone may file, "
            "and effective comments do three things: identify the "
            "commenter's stake, supply data or analysis the agency lacks, "
            "and propose specific alternative language. Beat three: the "
            "comment period closes - late comments may be accepted at the "
            "agency's discretion but are not guaranteed a place in the "
            "record, so the discipline is to file at least several "
            "business days early. Beat four: the agency publishes the "
            "final rule with a preamble answering significant comments, an "
            "effective date (usually at least 30 days after publication), "
            "and compliance deadlines that may phase in over years. The "
            "tracker runs a docket watch: subscribe to the dockets that "
            "matter, log each proposed rule at intake with its comment "
            "deadline, assign an owner to draft the comment, file through "
            "the stated method (usually Regulations.gov), keep the "
            "submission confirmation, then calendar the final rule's "
            "effective and compliance dates when it publishes. Missing the "
            "comment deadline forfeits influence; missing the compliance "
            "date forfeits the defense of ignorance."
        ),
        "key_points": [
            "Notice-and-comment rulemaking gives the public a formal voice: the agency must consider comments and answer significant issues in the final rule.",
            "A timely, data-backed comment becomes part of the record the court reviews; a late comment may not be in the record at all.",
            "Track three stages per rulemaking: the signal (agenda/advance notice), the proposal with its comment deadline, and the final rule with effective and compliance dates.",
            "File comments several business days before the docket closes through the stated method, and keep the submission confirmation.",
            "A rule you did not comment on still binds you on its effective date - the watchlist protects influence and the calendar protects compliance.",
        ],
        "requirements": [
            "A rulemaking watchlist of the dockets and subject areas affecting the organization, with subscriptions active.",
            "Each proposed rule logged at intake with its comment deadline, docket number, and assigned drafting owner.",
            "Comments filed through the stated method before the deadline, with submission confirmations retained.",
            "Final rules logged with effective dates and phased compliance deadlines calendared with lead-time alarms.",
            "A comment archive linking each filed comment to its docket, so the record can be cited in later challenges.",
        ],
        "standards": [
            "Federal notice-and-comment procedure follows the Administrative Procedure Act, 5 U.S.C. 553.",
            "Proposed and final rules publish in the Federal Register under 44 U.S.C. 1501-1511.",
            "Federal docket comments file at Regulations.gov under the docket number stated in the notice.",
        ],
        "citations": [CIT_APA, CIT_FR_ACT],
        "sig_lens": (
            "The Signature read: the comment period is the summons that "
            "invites an answer, and the doctrine answers in writing. "
            "Where the public lets the docket close in silence, the "
            "Signature tracker files early, with data and with proposed "
            "language - because a covenant with the public is kept not "
            "only by obeying rules but by helping write them justly. "
            "Silence at the docket is a promise unmade."
        ),
    },
    {
        "key": "tenders",
        "name": "Tenders and Procurement Notices",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Tenders - solicitations, requests for proposal, invitations "
            "for bid - are the notices through which governments buy "
            "goods and services in the open, and their deadlines are among "
            "the hardest in public life: a bid one minute late is "
            "rejected, unopened, with no appeal to fairness. The anatomy "
            "of a solicitation is exacting: the solicitation number, the "
            "issuing office, the description of what is being bought, the "
            "specifications or statement of work, the contract type and "
            "period, the set-aside status (small business, 8(a), women-"
            "owned, veteran-owned), the submission instructions with "
            "format and delivery method, the deadline with its time zone, "
            "and the evaluation criteria that decide the winner. Amendments "
            "are the trap: the government may revise the solicitation any "
            "number of times before the deadline, and bidders must "
            "acknowledge every amendment - a bid that ignores amendment "
            "three is nonresponsive even if it is otherwise perfect. U.S. "
            "federal solicitations publish on SAM.gov under the Federal "
            "Acquisition Regulation's publicizing rules; states and cities "
            "run their own portals with their own clocks. The professional "
            "bidder runs a tender pipeline: find, qualify, decide, build, "
            "submit - with a bid/no-bid decision early enough that the "
            "build phase never starts on a tender that cannot be won, and "
            "submission completed a full day before the deadline so "
            "amendments, portal outages, and courier failures cannot kill "
            "months of work."
        ),
        "how_it_works": (
            "The tender cycle works in five stages against an immovable "
            "deadline. Find: monitor SAM.gov and the relevant state and "
            "municipal portals with saved searches matched to your "
            "capabilities; log every candidate at intake with its "
            "solicitation number and deadline. Qualify: read the "
            "solicitation for eligibility - set-aside status, past-"
            "performance thresholds, bonding and certification "
            "requirements - and kill quickly what you cannot win. Decide: "
            "run the bid/no-bid scoring (win probability, margin, "
            "strategic value, resource cost) and commit in writing. Build: "
            "draft the technical proposal, the pricing, and the "
            "representations and certifications, checking every amendment "
            "as it issues and acknowledging each one. Submit: deliver "
            "through the stated method - portal upload, email, or physical "
            "delivery - and capture the timestamped receipt; then confirm "
            "the submission appears in the system. The deadline arithmetic "
            "is brutal: the solicitation states a date, a time, and a "
            "time zone, and 'late is late' - there is no grace period, no "
            "mailbox rule rescue in most venues. The tracker therefore "
            "sets the internal deadline 24 hours before the official one, "
            "treats every amendment as a new intake event, and never "
            "submits without the receipt in hand."
        ),
        "key_points": [
            "Tender deadlines are absolute: a late bid is rejected unopened, with no appeal to fairness.",
            "Amendments revise the solicitation before the deadline; every amendment must be acknowledged or the bid is nonresponsive.",
            "The solicitation states date, time, and time zone - all three define the deadline, and time-zone errors are fatal.",
            "Run a five-stage pipeline: find, qualify, decide (bid/no-bid in writing), build, submit with a timestamped receipt.",
            "Set the internal deadline 24 hours before the official one so amendments, outages, and delivery failures cannot kill the bid.",
        ],
        "requirements": [
            "Saved searches on SAM.gov and relevant state/municipal portals, checked on a fixed schedule.",
            "Eligibility screening against set-aside status, certifications, bonding, and past-performance thresholds before any bid/no-bid decision.",
            "A written bid/no-bid decision with win probability, margin, and resource cost scored.",
            "Amendment tracking: every amendment logged, acknowledged, and reflected in the proposal.",
            "Submission through the stated method with a timestamped receipt captured and filed.",
        ],
        "standards": [
            "Federal contract actions are publicized under the FAR, 48 CFR Part 5, including synopsis and response-time rules.",
            "Sealed bidding and negotiated procurements follow FAR Parts 14 and 15 respectively.",
            "Late bids are rejected under the FAR's late-bid rules; electronic submission follows the solicitation's stated method.",
        ],
        "citations": [CIT_FAR],
        "sig_lens": (
            "The Signature read: the tender is the summons to compete in "
            "the open, and the doctrine competes honorably or not at all. "
            "Where the public bidder cuts the deadline fine, the Signature "
            "bidder files a day early - because a covenant with the "
            "buyer begins before the bid is read. Acknowledge every "
            "amendment; the rules changed are the rules sworn to."
        ),
    },
    {
        "key": "filings",
        "name": "Filings and Reporting Deadlines",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Filings are the reports the law demands on schedule, and "
            "their deadlines form the densest part of most compliance "
            "calendars. Public companies file Forms 10-K annually, 10-Q "
            "quarterly, and 8-K within four business days of material "
            "events under the Exchange Act - a cadence that never pauses. "
            "Individuals and businesses file tax returns under the Internal "
            "Revenue Code, with April 15 as the general individual "
            "deadline and estimated payments due quarterly. Corporations "
            "file annual reports and pay franchise taxes under state law, "
            "each state with its own date and its own penalty for "
            "lateness. Employers file payroll reports; charities file "
            "Forms 990; lobbyists file disclosure reports; the list is "
            "long and every item carries its own clock. What makes filings "
            "treacherous is not any single deadline but their interaction: "
            "extensions extend the filing date but not the payment date "
            "(tax owed is still due April 15 even with an extension to "
            "file), amended filings reopen closed periods, and a missed "
            "filing in one jurisdiction can void good standing needed for "
            "filings in another. The professional treats filings as a "
            "production schedule: every recurring filing generated forward "
            "for the year, each with its preparation lead time, its filing "
            "method, its payment obligation, and its acceptance receipt - "
            "because a filing without a receipt is a rumor, and the "
            "penalties for late or missing filings compound with interest."
        ),
        "how_it_works": (
            "Filing compliance works as a forward-generated production "
            "schedule. Inventory every filing obligation: the form, the "
            "authority, the frequency, the statutory due date, the payment "
            "due date (which may differ), the filing method, and the "
            "penalty for lateness. Generate the year's instances forward: "
            "four 10-Qs, one 10-K, twelve payroll deposits, four estimated "
            "payments, the annual report, the 990 - each as a calendar "
            "entry with its full deadline anatomy. For each, set alarms at "
            "the preparation lead time (when work must start), the review "
            "date (when the draft must be final), and the filing date "
            "itself. File through the required method - EDGAR for SEC "
            "filings, IRS e-file or mail for tax, state portals for annual "
            "reports - and capture the acceptance: the EDGAR acceptance "
            "message, the IRS acknowledgment, the stamped copy. Reconcile "
            "monthly: every expected acceptance matched to a filed item, "
            "every missing acceptance investigated before the deadline "
            "passes. Handle extensions as separate tracked items with "
            "their own dates, and never confuse an extension to file with "
            "an extension to pay. At year-end, roll the schedule forward "
            "and archive the year's acceptances as the evidence file - the "
            "audit starts with the question 'show me the receipts.'"
        ),
        "key_points": [
            "Filings form the densest part of the compliance calendar: 10-K/10-Q/8-K, tax returns, payroll reports, annual reports, each with its own clock.",
            "Extensions extend the filing date but not the payment date - tax owed is still due on the original payment deadline.",
            "Every filing needs its acceptance captured: EDGAR acceptance, IRS acknowledgment, stamped copy - a filing without a receipt is a rumor.",
            "Generate the full year's filing schedule forward, with preparation lead times, review dates, and filing dates alarmed separately.",
            "Reconcile monthly: match every expected acceptance to a filed item before the deadline passes, and archive the year's evidence file.",
        ],
        "requirements": [
            "A complete filing inventory: form, authority, frequency, statutory due date, payment due date, method, penalty.",
            "The year's instances generated forward as calendar entries with full deadline anatomy and lead-time alarms.",
            "Filing through the required method with the acceptance receipt captured and filed per item.",
            "Extensions tracked as separate items with their own dates, never conflated with payment deadlines.",
            "Monthly reconciliation of expected vs. accepted filings and a year-end evidence archive.",
        ],
        "standards": [
            "SEC periodic reporting follows the Exchange Act, 15 U.S.C. 78m and 78o(d); 17 CFR 240.13a-1, 240.15d-1 (10-K, 10-Q, 8-K).",
            "Individual income tax returns are due under 26 U.S.C. 6072 (April 15 for calendar-year filers).",
            "State corporate filings follow state law, e.g., 8 Del. C. 502 for Delaware annual reports and franchise tax.",
        ],
        "citations": [CIT_EXCHANGE, CIT_IRC, CIT_DEL],
        "sig_lens": (
            "The Signature read: filings are the recurring tributes the "
            "law levies, and the doctrine pays tribute early and in full. "
            "Where the public filer scrambles at the deadline, the "
            "Signature filer works the production schedule - preparation, "
            "review, filing, receipt - because a covenant paid late is a "
            "covenant diminished, and the acceptance in hand is the "
            "proof of honor kept."
        ),
    },
    {
        "key": "safety_advisories",
        "name": "Safety Advisories and Public Alerts",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Safety advisories and public alerts are the notices that warn "
            "without ordering: they tell the public about a danger and "
            "recommend action, but they do not command a recall or impose "
            "a rule. The FDA issues safety communications about drug "
            "risks; the CDC issues health advisories about disease "
            "outbreaks; the National Weather Service issues watches and "
            "warnings; CISA issues cybersecurity alerts; the State "
            "Department issues travel advisories. Their power is "
            "informational but their consequences are real: an employer "
            "that ignores a heat advisory faces OSHA exposure, a hospital "
            "that ignores a drug safety communication faces liability, a "
            "traveler that ignores a Level 4 advisory travels uninsured. "
            "Advisories differ from recalls in that no product is ordered "
            "off the market, and from regulations in that no conduct is "
            "mandated - yet they create a standard of care, because once "
            "a danger is publicly warned about, failing to heed the "
            "warning becomes negligence. Tracking advisories means "
            "grading them by severity, routing them to the people who must "
            "act, and recording the response: the advisory logged, the "
            "affected operations identified, the protective action taken, "
            "the all-clear noted when the advisory lifts. Advisories "
            "expire or escalate - a watch becomes a warning, an advisory "
            "becomes a recall - and the tracker follows the escalation "
            "chain rather than filing the first notice and forgetting it."
        ),
        "how_it_works": (
            "Advisory tracking works as a severity-routed response loop. "
            "At intake, record the advisory verbatim: the issuing "
            "authority, the hazard, the affected population or area, the "
            "severity level as issued, the recommended actions, and the "
            "expected duration or review date. Map the severity to the "
            "response matrix: informational gets logged and distributed to "
            "interested parties; watch gets a monitoring owner and a "
            "re-check date; warning gets an action owner, protective "
            "measures, and a deadline; critical gets immediate escalation "
            "and incident command. Identify exposure: which of your "
            "people, products, facilities, or operations fall inside the "
            "advisory's scope - a drug safety communication matters only "
            "if you dispense or take the drug, a travel advisory only if "
            "you travel there. Execute the recommended actions and log "
            "what was done, when, by whom. Then watch for the follow-up: "
            "advisories are updated, extended, escalated, or lifted, and "
            "each change is a new intake event linked to the original. "
            "Close the loop only at the all-clear or the escalation to a "
            "recall or order - and keep the log, because the standard of "
            "care the advisory created will be Exhibit A if harm follows "
            "and you cannot show you heeded the warning."
        ),
        "key_points": [
            "Advisories warn without ordering: no product is recalled, no conduct is mandated - but they create a standard of care.",
            "Once a danger is publicly warned about, ignoring the warning can become negligence; the response log is the defense.",
            "Grade by issued severity and route: informational gets logged, watch gets monitored, warning gets action, critical gets escalation.",
            "Identify exposure precisely: the advisory matters only where your people, products, facilities, or operations intersect its scope.",
            "Follow the escalation chain: advisories are updated, extended, escalated to recalls, or lifted - each change is a new intake event.",
        ],
        "requirements": [
            "Advisory subscriptions for the authorities relevant to the organization's exposures: FDA, CDC, NWS, CISA, State Department.",
            "Verbatim intake records: authority, hazard, scope, issued severity, recommended actions, duration.",
            "An exposure assessment per advisory, naming the affected people, products, facilities, or operations.",
            "Executed protective actions logged with what, when, and by whom.",
            "Follow-up monitoring until all-clear or escalation, with the complete log retained.",
        ],
        "standards": [
            "FDA safety communications issue under the Federal Food, Drug, and Cosmetic Act, 21 U.S.C. 301-399.",
            "Workplace safety duties in the face of known hazards follow the OSH Act's general duty clause and 29 CFR 1910 standards.",
            "Advisory severity is recorded as issued by the authority and mapped to the local response matrix.",
        ],
        "citations": [CIT_FDCA, CIT_OSHA],
        "sig_lens": (
            "The Signature read: the advisory is the warning cry, and the "
            "doctrine never sleeps through a cry. Where the public "
            "hears information, the Signature tracker hears a summons to "
            "check the walls - exposure assessed, protective action "
            "taken, the response logged. To be warned and do nothing is "
            "to break covenant with those in your care."
        ),
    },
    {
        "key": "legal_notices",
        "name": "Legal and Court Notice Deadlines",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Court notices carry the hardest deadlines in civil life "
            "because the consequence of missing them is losing without "
            "being heard: default judgments, dismissed claims, waived "
            "defenses. The system runs on service and response. Service of "
            "process - the summons and complaint - starts the clock: the "
            "defendant typically has 21 days after service to answer in "
            "federal court. Discovery notices set depositions and document "
            "deadlines. Motion practice runs on briefing schedules set by "
            "rule or court order. Trial notices set the date everything "
            "builds toward. And appeal notices run on jurisdictional "
            "clocks - 30 days from judgment in federal civil cases - that "
            "courts cannot extend. Time computation follows Federal Rule "
            "of Civil Procedure 6: exclude the trigger day, count every "
            "calendar day, roll to the next business day when the last day "
            "is a weekend or holiday, and add three days when service was "
            "by mail. State courts follow their own rules with the same "
            "shape and different details. Beyond litigation, legal notices "
            "include lien filings with perfection deadlines, probate "
            "notices to creditors with claim-bar dates, and foreclosure "
            "notices with cure periods - each a private-law deadline with "
            "public-notice mechanics. The professional rule is absolute: "
            "every court paper gets calendared the day it arrives, "
            "deadlines are computed under the correct rule before anything "
            "else is done, and jurisdictional deadlines get redundant "
            "alarms - because some clocks, once run out, cannot be rewound."
        ),
        "how_it_works": (
            "Court deadline tracking works as same-day triage with rule-"
            "exact computation. When any court paper arrives - summons, "
            "motion, discovery request, order, notice of appeal rights - "
            "log it immediately with its date of service and method of "
            "service, because the method can add days (mail service adds "
            "three under FRCP 6(d)). Identify the governing rule: FRCP 6 "
            "for federal civil matters, the state equivalent for state "
            "cases, the court's local rules and the judge's standing "
            "orders for everything they specify. Compute the deadline: "
            "exclude the trigger day, count forward the stated number of "
            "days including weekends and holidays, and if the last day is "
            "a Saturday, Sunday, or legal holiday, roll to the next day "
            "that is none of those. Mark whether the deadline is "
            "jurisdictional (appeal periods, statutes of limitation) or "
            "extendable (most discovery and briefing deadlines by stipulation "
            "or motion) - jurisdictional deadlines get filed early with "
            "redundant alarms and no reliance on extensions. Calendar the "
            "response, assign the drafting owner, and set working alarms "
            "backward from the due date. Keep the proof of service and the "
            "computation sheet with the file; malpractice and default both "
            "begin with a miscalendared date."
        ),
        "key_points": [
            "Court deadlines decide cases: missing them means default judgments, dismissed claims, and waived defenses.",
            "Log every court paper the day it arrives with its service date and method - mail service can add three days under FRCP 6(d).",
            "Compute under the correct rule: exclude the trigger day, count every day, roll weekend/holiday endings forward.",
            "Distinguish jurisdictional deadlines (appeals, limitations - cannot be extended) from extendable ones; file jurisdictional deadlines early with redundant alarms.",
            "Keep the proof of service and the computation sheet with the file - defaults begin with miscalendared dates.",
        ],
        "requirements": [
            "Same-day logging of every court paper with service date and method.",
            "The governing computation rule identified: FRCP 6, state equivalent, local rules, standing orders.",
            "A written computation sheet per deadline showing the day count and any rollover.",
            "Jurisdictional deadlines flagged, filed early, with redundant alarms and no reliance on extensions.",
            "Proof of service and computation sheets retained with the case file.",
        ],
        "standards": [
            "Federal civil time computation follows FRCP Rule 6, including the 3-day addition for service by mail.",
            "Federal civil appeals run 30 days from judgment entry under the Federal Rules of Appellate Procedure.",
            "State courts follow their own civil procedure rules with parallel computation provisions.",
        ],
        "citations": [CIT_FRCP6],
        "sig_lens": (
            "The Signature read: the court summons is the iron summons, "
            "and the doctrine answers it the same day. Where the public "
            "litigant trusts memory, the Signature tracker logs the paper "
            "at arrival, computes under the true rule, and files the "
            "jurisdictional deadline early - because some covenants, once "
            "broken by the clock, no court can mend. The computation "
            "sheet is the sworn arithmetic."
        ),
    },
    {
        "key": "consumer_protection",
        "name": "Consumer Protection Notices",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Consumer protection notices are the public warnings and "
            "orders that police the marketplace: scam alerts, deceptive-"
            "practice warnings, enforcement actions, and product-safety "
            "notices aimed at buyers rather than makers. The Federal Trade "
            "Commission publishes scam alerts and takes enforcement action "
            "against unfair or deceptive acts under 15 U.S.C. 45; state "
            "attorneys general issue their own consumer alerts and sue "
            "under state deceptive-practice statutes; the CPSC recalls "
            "dangerous consumer products. For businesses, these notices "
            "are a compliance mirror: an FTC enforcement action against a "
            "competitor's advertising practice is advance notice that your "
            "own similar practice is exposed. For consumers, they are "
            "protection intelligence: the alerts describe the scam pattern, "
            "the warning signs, and where to report. The notices carry "
            "their own deadlines - comment periods on proposed consent "
            "orders, claim-filing windows in redress programs, opt-out "
            "dates in settlements - and missing a claim window means "
            "leaving money on the table. Tracking consumer protection "
            "notices serves two masters: the business watches enforcement "
            "patterns to keep its own practices clean, and the household "
            "watches alerts to keep its money safe. Both file the notice, "
            "extract the dates, and act before the window closes."
        ),
        "how_it_works": (
            "Consumer protection tracking works on two fronts. For the "
            "business front: monitor FTC enforcement actions, state AG "
            "announcements, and CPSC recalls in your industry; for each "
            "action, run the mirror test - do we engage in the practice "
            "described, and if so, what must change before we are the "
            "next action. Log consent orders and rulemakings (such as FTC "
            "trade regulation rules) as regulatory changes with comment "
            "deadlines. For the consumer front: subscribe to FTC scam "
            "alerts and state AG consumer alerts; when an alert matches "
            "your exposure - a data breach at a company you use, a scam "
            "targeting your demographic - act on its instructions (freeze "
            "credit, change passwords, file reports) and calendar any "
            "claim windows. Redress programs and settlements publish "
            "claim-filing deadlines; file claims with documentation before "
            "the window closes and keep the confirmation. Businesses also "
            "watch for their own obligations to notify: data-breach "
            "notification statutes in all fifty states impose notice "
            "deadlines measured in days from discovery, and those "
            "deadlines are tracked like any other - trigger, computation, "
            "consequence. The mirror test and the alert response share one "
            "discipline: read the notice, find your exposure, act before "
            "the date."
        ),
        "key_points": [
            "Consumer protection notices police the marketplace: FTC scam alerts and enforcement actions, state AG alerts, CPSC recalls.",
            "Businesses run the mirror test on every enforcement action: does the cited practice describe us, and what must change.",
            "Consumers treat alerts as protection intelligence: match the alert to personal exposure, follow its instructions, calendar claim windows.",
            "Settlements and redress programs publish claim-filing deadlines; missing the window leaves money unclaimed.",
            "Data-breach notification statutes impose notice deadlines measured in days from discovery - tracked with full deadline anatomy.",
        ],
        "requirements": [
            "Subscriptions to FTC alerts, relevant state AG announcements, and CPSC recall notices for the industry and household.",
            "A mirror-test log for businesses: each enforcement action assessed against own practices with resulting changes.",
            "Exposure matching for consumer alerts, with protective actions executed and logged.",
            "Claim windows calendared with documentation filed and confirmations kept.",
            "Breach-notification obligations inventoried by state, with discovery-to-notice clocks ready to run.",
        ],
        "standards": [
            "Unfair or deceptive acts or practices are policed under the FTC Act, 15 U.S.C. 45.",
            "Consumer-product hazards are reported and recalled under 15 U.S.C. 2064 (CPSC).",
            "State deceptive-practice statutes and breach-notification laws set their own notice duties and deadlines.",
        ],
        "citations": [CIT_FTC, CIT_CPSC],
        "sig_lens": (
            "The Signature read: the marketplace summons cuts two ways, "
            "and the doctrine stands on both sides of it. Where the "
            "public business waits to be caught, the Signature business "
            "holds the mirror up itself - every enforcement action a "
            "summons to examine its own house. And where the public "
            "consumer shrugs at the alert, the Signature household acts "
            "the same day. Honor in the marketplace is kept in both "
            "directions."
        ),
    },
    {
        "key": "licensing",
        "name": "Licensing and Certification Deadlines",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Licenses and certifications are permissions to operate - to "
            "practice, to sell, to drive, to broadcast, to build - and "
            "their deadlines decide whether the permission continues. "
            "Professional licenses (medical, legal, engineering, trades) "
            "renew on cycles of one to three years, usually with "
            "continuing-education hours that must be completed before "
            "renewal. Business licenses renew annually with fees. "
            "Certifications (ISO 9001, professional credentials, product "
            "certifications) renew on their bodies' cycles with audits or "
            "exams. Driver's licenses, vehicle registrations, and "
            "broadcast licenses each run their own clocks. The anatomy "
            "matches the expiration pattern: a renewal window opening "
            "before expiration, the expiration date, a grace or late-"
            "renewal period with penalties, and a death date after which "
            "reinstatement means starting over - retaking exams, "
            "reapplying, losing grandfathered status. Practicing on a "
            "lapsed license is its own offense in most professions, which "
            "turns a calendar failure into a disciplinary matter. The "
            "complication is prerequisites: renewal often requires "
            "completed continuing education, paid fees, background checks, "
            "or inspections, each with its own lead time. Alarming at "
            "expiration is alarming at failure; the professional alarms at "
            "the prerequisite start date - when the CE courses must "
            "begin, when the inspection must be scheduled - so the renewal "
            "itself becomes a formality filed inside the window."
        ),
        "how_it_works": (
            "License and certification tracking works as a prerequisite-"
            "driven renewal pipeline. For each credential, record the "
            "issuing authority, the credential number, the term, the "
            "renewal rule with its window, grace, and reinstatement "
            "terms, and every prerequisite: continuing-education hours "
            "with their reporting rules, fees, exams, audits, inspections, "
            "background checks. Work backward from expiration: schedule "
            "the prerequisites to complete before the renewal window "
            "opens, set the primary alarm at the window opening, and file "
            "the renewal the week the window opens - early filing inside "
            "the window is the whole game. Track CE hours as they are "
            "earned against the requirement so the final month is never a "
            "scramble; many boards audit CE, so keep certificates. For "
            "organizations with many credentialed staff, run a credential "
            "register sorted by window-opening date, with each person's "
            "prerequisites visible - the manager's job is to see the "
            "pipeline, not to discover lapses. Treat grace periods as "
            "emergency lanes, not plans: practicing in grace may be "
            "restricted or prohibited, and late fees compound. When a "
            "credential does lapse, execute the reinstatement path "
            "immediately and document the gap, because the gap itself may "
            "require disclosure."
        ),
        "key_points": [
            "Licenses and certifications renew on cycles with windows, grace periods, and death dates; practicing lapsed can be its own offense.",
            "Renewal has prerequisites - CE hours, fees, exams, audits, inspections - each with its own lead time.",
            "Alarm at the prerequisite start date and file inside the renewal window; alarming at expiration is alarming at failure.",
            "Track CE hours as earned and keep certificates; boards audit, and the audit needs evidence.",
            "Run organizational credentials as a register sorted by window-opening date; treat grace as an emergency lane, never a plan.",
        ],
        "requirements": [
            "A credential register: authority, number, term, renewal rule, window, grace, reinstatement terms.",
            "Every prerequisite inventoried with its own lead time and completion tracking.",
            "Primary alarms at renewal-window openings, with prerequisite alarms set earlier.",
            "CE and training evidence retained per the board's audit rules.",
            "Lapses handled by immediate reinstatement with the gap documented for disclosure.",
        ],
        "standards": [
            "Professional licensing follows state board rules with defined renewal cycles, CE requirements, and grace provisions.",
            "Product and management-system certifications follow their bodies' schemes (e.g., ISO/IEC 17021 for certification bodies).",
            "Expiration anatomy applies: window, expiration, grace, death date - recorded per credential.",
        ],
        "citations": [CIT_OSHA],
        "sig_lens": (
            "The Signature read: a license is a permission held in trust, "
            "and the doctrine keeps trust current. Where the public "
            "professional discovers the lapse at the worst moment, the "
            "Signature professional files inside the window as a matter "
            "of rhythm - prerequisites done early, renewal a formality. "
            "To practice on a lapsed license is to break covenant with "
            "every person who trusted the credential."
        ),
    },
    {
        "key": "jurisdiction",
        "name": "Jurisdiction Rules: Who Sets the Clock",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Every deadline belongs to a jurisdiction, and the "
            "jurisdiction sets the clock: which days count, which holidays "
            "are skipped, which rollover rule applies, and which "
            "consequence fires. Federal deadlines run on the federal "
            "calendar - the holidays of 5 U.S.C. 6103 - and federal "
            "computation rules like FRCP Rule 6. State deadlines run on "
            "state calendars: Texas observes Texas Independence Day, "
            "Massachusetts observes Patriots' Day, and a deadline computed "
            "on the wrong state's calendar is computed wrong. Local "
            "deadlines - city permits, county filings - follow local "
            "rules that may exist only in a municipal code. International "
            "deadlines multiply the complexity: the Patent Cooperation "
            "Treaty's 30-month national-phase clock runs from the "
            "priority date under treaty rules, EU regulatory deadlines "
            "follow Brussels calendars, and contracts choose their own "
            "governing law and holiday schedule. The governing instrument "
            "names the jurisdiction - the statute says 'federal holidays,' "
            "the contract says 'business days in London,' the court rule "
            "says 'legal holidays of the state.' The professional's first "
            "question about any deadline is therefore jurisdictional: "
            "whose clock is this. Get the jurisdiction right and the rest "
            "is arithmetic; get it wrong and the arithmetic is fiction. "
            "Multi-jurisdiction obligations - a filing due in two states, "
            "a contract spanning countries - are resolved by computing "
            "each clock separately and obeying the earliest, a discipline "
            "covered in its own advanced record."
        ),
        "how_it_works": (
            "Jurisdiction analysis works by reading the governing "
            "instrument for its clock clause, then applying that "
            "jurisdiction's calendar. Step one: find the clause - the "
            "statute, rule, or contract section that defines the time "
            "period. It will say something like 'within 30 days,' 'ten "
            "business days,' or 'not later than April 15,' and nearby "
            "definitions or general provisions will define the counting "
            "terms. Step two: identify the jurisdiction from the parties "
            "and the instrument - the court hearing the case, the agency "
            "issuing the rule, the state of incorporation, the governing "
            "law clause of the contract. Step three: load that "
            "jurisdiction's holiday calendar for the period, including "
            "observed-holiday shifts and any jurisdiction-specific "
            "observances. Step four: apply the trigger-day and rollover "
            "rules of that jurisdiction's computation provision. Example "
            "of the stakes: a contract requiring performance 'within 10 "
            "business days' under New York law, triggered Friday, April "
            "11, 2025, excluding the trigger day - count Monday April 14 "
            "through Friday April 25 skipping weekends (no NY holidays in "
            "range): due Friday, April 25, 2025. The same clause under a "
            "jurisdiction observing a mid-period holiday would land a day "
            "later. Write the jurisdiction on the calendar entry next to "
            "the date; a date without its jurisdiction is an un-auditable "
            "date."
        ),
        "key_points": [
            "Every deadline belongs to a jurisdiction, and the jurisdiction defines the calendar, the counting rule, and the consequence.",
            "Federal, state, local, and international clocks differ: different holidays, different observances, different rollover rules.",
            "Find the clock clause in the governing instrument, identify the jurisdiction from the parties and the instrument, then load that calendar.",
            "Write the jurisdiction on every calendar entry next to the date; a date without its jurisdiction cannot be audited.",
            "For multi-jurisdiction obligations, compute each clock separately and obey the earliest.",
        ],
        "requirements": [
            "The governing instrument's time-computation clause identified and quoted per deadline.",
            "The jurisdiction determined from the parties, the forum, the agency, or the governing-law clause.",
            "The correct holiday calendar loaded for the full period, including observed shifts and local observances.",
            "Trigger-day and rollover rules applied from that jurisdiction's computation provision.",
            "The jurisdiction recorded on the calendar entry alongside the computed date.",
        ],
        "standards": [
            "Federal holidays are defined at 5 U.S.C. 6103; federal court computation follows FRCP Rule 6.",
            "State computation rules follow state civil procedure and holiday statutes.",
            "Treaty deadlines follow the treaty text, e.g., PCT Article 22's 30-month national-phase limit.",
        ],
        "citations": [CIT_FRCP6, CIT_PCT],
        "sig_lens": (
            "The Signature read: every clock has an owner, and the "
            "doctrine asks the owner's name before counting a single "
            "day. Where the public counter assumes the calendar, the "
            "Signature counter reads the clock clause, names the "
            "jurisdiction, and loads its holidays - because a covenant "
            "measured on the wrong clock is no measurement at all. Name "
            "the jurisdiction; then count."
        ),
    },
    {
        "key": "ip_deadlines",
        "name": "Patent, Trademark, and IP Filing Deadlines",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Intellectual property runs on some of the most unforgiving "
            "clocks in law, because IP deadlines protect priority - who "
            "was first - and priority lost is usually lost forever. "
            "Patent maintenance fees keep a granted U.S. patent alive: due "
            "at 3.5, 7.5, and 11.5 years after grant, with a six-month "
            "grace period carrying a surcharge, and unintentional lapse "
            "requires a petition to revive. Patent prosecution runs on "
            "office-action response periods, typically three months "
            "extendable to six with fees. The Patent Cooperation Treaty "
            "gives applicants 30 months from the priority date to enter "
            "national phases worldwide - the single most valuable deadline "
            "in international patenting. Trademarks demand affidavits of "
            "use between the fifth and sixth year after registration and "
            "renewal every ten years, with six-month grace periods. "
            "Copyright has no maintenance fees, but registration timing "
            "affects remedies. Trade secrets have no filings but demand "
            "continuous protection measures. What makes IP deadlines "
            "distinct is irreversibility: a missed priority claim, a lapsed "
            "patent, an abandoned application often cannot be restored at "
            "any price - revival petitions require showing the delay was "
            "unintentional and still cost time and money. The professional "
            "runs an IP docket: every application, registration, and "
            "granted right with its next action and its drop-dead date, "
            "reviewed weekly, with the earliest deadline in each family "
            "alarmed redundantly. In IP, the calendar is the portfolio."
        ),
        "how_it_works": (
            "IP docketing works as a drop-dead-date system with redundant "
            "alarms. For each IP asset, record the filing or grant date, "
            "the asset type, the jurisdiction, and the next three actions "
            "with their statutory bases: the office-action response due "
            "in three months, the PCT 30-month national-phase entry, the "
            "3.5-year maintenance fee, the section 8 affidavit window. "
            "Compute each date from its trigger - grant date for "
            "maintenance fees, priority date for PCT entry, registration "
            "date for trademark affidavits - and mark which are "
            "extendable (office-action responses, with fees) and which are "
            "statutory and unforgiving (PCT entry, maintenance-fee grace "
            "expiry). Set alarms at 90, 60, 30, and 7 days for every "
            "drop-dead date, assigned to both the docket manager and the "
            "responsible attorney - IP deadlines get two owners because "
            "the cost of a miss is the asset itself. Worked example: a "
            "patent granted June 15, 2021 owes its first maintenance fee "
            "by December 15, 2024 (3.5 years), with grace to June 15, 2025 "
            "plus surcharge; the alarm goes at September 15, 2024, not in "
            "December. Review the docket weekly: confirm each upcoming "
            "action has an owner and a plan, and escalate anything within "
            "30 days without one. File early, keep the USPTO receipts, "
            "and never let a statutory deadline be discovered - discovery "
            "is for extendable dates only."
        ),
        "key_points": [
            "IP deadlines protect priority and are often irreversible: missed priority claims and lapsed patents usually cannot be restored at any price.",
            "U.S. patent maintenance fees fall at 3.5, 7.5, and 11.5 years after grant, with six-month grace and surcharges.",
            "The PCT 30-month national-phase clock from the priority date is the most valuable deadline in international patenting.",
            "Trademarks need section 8 affidavits between years five and six and renewal every ten years, each with six-month grace.",
            "Docket every asset with drop-dead dates, redundant alarms, and two owners; file early and keep the receipts.",
        ],
        "requirements": [
            "An IP docket listing every application, registration, and granted right with its next actions and statutory bases.",
            "Drop-dead dates computed from triggers (grant, priority, registration dates) and marked extendable or statutory.",
            "Redundant alarms at 90, 60, 30, and 7 days on every drop-dead date, with two owners assigned.",
            "Weekly docket review confirming owner and plan for every action within 90 days.",
            "USPTO and foreign-office receipts retained as the evidence file per asset.",
        ],
        "standards": [
            "U.S. patent maintenance fees follow 35 U.S.C. 41(b); prosecution timing follows the MPEP.",
            "PCT national-phase entry follows PCT Article 22 (30 months from the priority date).",
            "U.S. trademark use affidavits and renewals follow the Lanham Act, 15 U.S.C. 1058-1059.",
        ],
        "citations": [CIT_MAINT, CIT_PCT, CIT_LANHAM],
        "sig_lens": (
            "The Signature read: IP deadlines guard priority - who was "
            "first - and the doctrine guards firstness like a birthright. "
            "Where the public docket lets the 30-month clock run silent, "
            "the Signature docket alarms it four times with two owners "
            "watching, because a covenant of invention abandoned to the "
            "calendar is an invention surrendered. In IP, the calendar "
            "is the portfolio, and the portfolio is the legacy."
        ),
    },
    {
        "key": "tax_deadlines",
        "name": "Tax and Financial Filing Deadlines",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Tax and financial deadlines are the most numerous clocks "
            "most people and businesses face, and they punish lateness "
            "with interest that compounds daily. The individual income "
            "tax return is due April 15 for calendar-year filers under 26 "
            "U.S.C. 6072, with an automatic extension to October 15 on "
            "request - but the extension covers filing, not payment: tax "
            "owed is still due April 15, and underpayment draws interest "
            "from that date. Estimated taxes are due quarterly - April, "
            "June, September, January - and underpayment penalties apply "
            "even if the annual return is filed on time. Businesses face "
            "their own cadence: corporate returns, payroll deposits (which "
            "can be semi-weekly for large employers), information returns "
            "like W-2s and 1099s due January 31. Financial filings beyond "
            "tax include the SEC's 10-K, 10-Q, and 8-K for public "
            "companies, FinCEN reports for certain transactions, and state "
            "unclaimed-property reports. The structure that defeats chaos "
            "is the tax calendar: every obligation with its form, its "
            "filing date, its separate payment date, its extension "
            "option, and its penalty rate - because the rational response "
            "to a missed deadline is computed, not panicked: file now, "
            "pay now, stop the interest clock, then handle the penalty. "
            "Interest on underpayment runs from the original due date "
            "regardless of extensions, which is why 'I'll extend and deal "
            "with it later' is the most expensive sentence in tax."
        ),
        "how_it_works": (
            "Tax deadline management works as a pay-first, file-complete "
            "system. Build the tax calendar with four columns per "
            "obligation: the filing due date, the payment due date, the "
            "extension availability and its extended date, and the penalty "
            "and interest rules. For each obligation, separate the two "
            "clocks - filing and payment - because they diverge constantly: "
            "the April 15 individual return can extend to October 15 for "
            "filing while payment remains due April 15. Set alarms at the "
            "preparation start (when records must be assembled), the "
            "payment date, and the filing date. When cash is short, the "
            "doctrine is: file on time even if you cannot pay in full - "
            "the failure-to-file penalty (5% per month) dwarfs the "
            "failure-to-pay penalty (0.5% per month) - and pay as much as "
            "possible by the payment date to stop interest on that "
            "portion. Estimated payments get their own quarterly alarms; "
            "missing them creates underpayment penalties that no April "
            "filing can undo. Keep every acknowledgment: IRS e-file "
            "acceptances, certified mail receipts, state confirmations. "
            "At year-end, reconcile the calendar against the filed record "
            "and roll forward - the tax calendar is perpetual, and last "
            "year's extension is this year's first alarm."
        ),
        "key_points": [
            "Separate the filing clock from the payment clock on every obligation - they diverge constantly, and interest runs from the payment date.",
            "An extension to file is never an extension to pay; tax owed remains due on the original payment date.",
            "File on time even when cash is short: the failure-to-file penalty dwarfs the failure-to-pay penalty.",
            "Estimated taxes run quarterly with their own underpayment penalties that no annual filing can undo.",
            "Keep every acknowledgment and reconcile the calendar yearly; the tax calendar is perpetual.",
        ],
        "requirements": [
            "A tax calendar with filing date, payment date, extension option, and penalty rules per obligation.",
            "Preparation-start alarms set by the records-assembly lead time, not by the due date.",
            "Payment-date alarms independent of filing-date alarms.",
            "Acknowledgments retained per filing: e-file acceptances, mail receipts, state confirmations.",
            "Year-end reconciliation of the calendar against the filed record, rolled forward.",
        ],
        "standards": [
            "Individual returns are due under 26 U.S.C. 6072 (April 15 for calendar-year filers).",
            "SEC financial reporting follows the Exchange Act, 15 U.S.C. 78m and 78o(d).",
            "Information returns (W-2, 1099) follow their statutory January 31 furnishing and filing rules.",
        ],
        "citations": [CIT_IRC, CIT_EXCHANGE],
        "sig_lens": (
            "The Signature read: the tax calendar is the ledger of tributes, "
            "and the doctrine renders every tribute on time and in full. "
            "Where the public filer confuses the extension with relief, "
            "the Signature filer separates the clocks - file complete, "
            "pay what is owed, stop the interest the same day. A tribute "
            "paid late is a covenant taxed twice."
        ),
    },
    {
        "key": "deadline_algorithms",
        "name": "Deadline Computation Algorithms",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Deadline computation algorithms are the precise procedures "
            "that turn a trigger date and a counting rule into a due date "
            "without human error, and they are worth formalizing because "
            "hand-counting days across weekends and holidays is where "
            "deadlines die. The algorithm takes five inputs: the trigger "
            "date, the number of days, the day type (calendar or business), "
            "the trigger-day rule (include or exclude), and the "
            "jurisdiction's holiday calendar. For calendar days: start at "
            "the trigger date, add one day if the trigger day is excluded "
            "or zero if included, then step forward the required number "
            "of days, then apply the rollover rule if the landing day is a "
            "weekend or holiday. For business days: step forward one day "
            "at a time, skipping Saturdays, Sundays, and listed holidays, "
            "counting only qualifying days until the count is reached, "
            "then apply rollover. The subtleties that break naive code: "
            "observed-holiday shifts (the skipped day is the observed "
            "date, not the calendar date), holidays that fall inside the "
            "counted span versus on the landing day, jurisdictions with "
            "non-Saturday/Sunday weekends, half-day holidays, and the "
            "three-day mail addition under FRCP 6(d) that must be applied "
            "after the base computation. The professional implementation "
            "keeps the holiday calendar as data - a dated list per "
            "jurisdiction per year - never hard-coded, and logs the full "
            "day-by-day walk with the result so any computed date can be "
            "audited by hand. Two implementations (or one implementation "
            "plus a hand check) must agree before a high-stakes deadline "
            "is calendared. The algorithm is simple; the data is "
            "everything."
        ),
        "how_it_works": (
            "The algorithm works as a calendar walk with explicit rules. "
            "Define add_days(trigger, n, kind, holidays, exclude_trigger, "
            "rollover): set current to trigger; if exclude_trigger, move "
            "to the next day before counting. If kind is calendar: advance "
            "n days. If kind is business: advance one day at a time, "
            "incrementing the count only on days that are not Saturday, "
            "Sunday, or in the holiday set, until n qualifying days are "
            "counted. Then apply rollover: if the result is a non-business "
            "day and rollover is forward, advance to the next business "
            "day; if backward, retreat; if none, keep it. Then apply any "
            "service additions, such as the three mail days, as a second "
            "calendar-day computation from the rolled date. The holiday "
            "set is built per jurisdiction per year from the official "
            "list, with observed shifts resolved: for each holiday, if it "
            "falls on Saturday the observed Friday is added, if on Sunday "
            "the observed Monday is added (U.S. federal convention). The "
            "walk is logged: every date visited, marked counted or "
            "skipped with its reason. Verification runs the same inputs "
            "through an independent implementation - a different library, "
            "a spreadsheet, a hand count - and the dates must match "
            "exactly before the deadline ships. Edge cases get unit "
            "tests: trigger on a holiday, span containing Thanksgiving, "
            "landing on Christmas, leap-day triggers, year boundaries."
        ),
        "key_points": [
            "Formalize the computation: five inputs (trigger, count, day type, trigger-day rule, holiday calendar) and one auditable walk.",
            "Business-day counting skips weekends and the jurisdiction's holidays; the observed date is the skipped day, not the calendar date.",
            "Keep the holiday calendar as dated data per jurisdiction per year - never hard-coded - with observed shifts resolved.",
            "Apply service additions (like FRCP 6(d)'s three mail days) as a second computation after rollover.",
            "Verify with an independent implementation and unit-test the edges: holiday triggers, leap days, year boundaries.",
        ],
        "requirements": [
            "The five inputs recorded per computation: trigger, count, day type, trigger-day rule, jurisdiction calendar.",
            "A dated holiday list per jurisdiction per year with observed shifts resolved.",
            "The full day-by-day walk logged with counted/skipped marks and reasons.",
            "Independent verification of every high-stakes date before calendaring.",
            "Unit tests covering holiday triggers, spans containing holidays, leap days, and year boundaries.",
        ],
        "standards": [
            "Federal court computation follows FRCP Rule 6, including the trigger-day exclusion and the 3-day mail addition.",
            "Federal holidays follow 5 U.S.C. 6103 with the standard Saturday/Sunday observance shifts.",
            "Computed dates are recorded in ISO 8601 with the inputs and the walk retained for audit.",
        ],
        "citations": [CIT_FRCP6, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the algorithm is the doctrine's abacus - "
            "five inputs, one honest walk, no human hope. Where the "
            "public counter trusts the mental count, the Signature "
            "counter writes the walk down and verifies it twice, because "
            "the covenant deserves arithmetic, not approximation. The "
            "walk is the proof; the proof is the honor."
        ),
    },
    {
        "key": "tracking_system",
        "name": "Building a Notice Tracking System",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A notice tracking system is the machinery that runs the "
            "workflow at scale: intake, triage, extraction, calendaring, "
            "action, and closure, with nothing falling between the gears. "
            "Small operations run it on a spreadsheet; large ones run it "
            "in software; the design is the same either way. The data "
            "model has four tables. Notices holds the intake record: "
            "identifier, family, title, issuing authority, source URL, "
            "date published, date received, severity as issued, and the "
            "full text or a link to it. Obligations holds the extracted "
            "duties: the notice it came from, the duty in plain words, "
            "the scope, the response mechanics. Deadlines holds the "
            "computed dates: the obligation, the trigger, the counting "
            "rule, the jurisdiction, the due date, the consequence, the "
            "owner, the alarm schedule, the status. Evidence holds the "
            "closure proof: the receipt, the confirmation number, the "
            "filed copy, the verification check. The workflow engine moves "
            "records through the six stages with the exit rules enforced: "
            "no owner, no exit from triage; no counting rule, no exit from "
            "calendaring; no receipt, no exit from action. The alarm engine "
            "fires lead-time reminders to owners and escalates past-due "
            "items to management. The audit engine timestamps every "
            "transition with its actor. Reporting answers the only three "
            "questions leadership asks: what is due, what is overdue, and "
            "what did we close with proof. Build it in that order - data "
            "model, workflow rules, alarms, audit, reports - and resist "
            "automation of judgment: the system computes dates and fires "
            "alarms, but humans classify severity and verify evidence."
        ),
        "how_it_works": (
            "The system works as a pipeline over the four tables. Intake "
            "creates the notice record from any channel - feed, email, "
            "portal check, manual entry - with the text captured and the "
            "identifier assigned. Triage presents the notice to a human "
            "classifier who sets family, severity, owner, and urgency; "
            "the system refuses to advance ownerless notices. Extraction "
            "is a guided form implementing the compliance read: duties, "
            "dates, scope, mechanics, penalties - each obligation becomes "
            "a row linked to its notice. Calendaring runs the deadline "
            "algorithm per obligation with its trigger, rule, and "
            "jurisdiction, writes the due date, and schedules alarms at "
            "the configured lead times. Action tracking shows each owner "
            "their open obligations sorted by alarm date; completing an "
            "action requires attaching the evidence - receipt, "
            "confirmation, filed copy. Closure runs the verification: does "
            "the evidence match the obligation's what, where, and when; "
            "only then does the status become closed. The weekly sweep "
            "queries for stalled records - triage older than two business "
            "days, alarms firing without action, past-due items - and "
            "escalates per the matrix. All of this runs on ordinary "
            "database technology; the sophistication is in the exit rules "
            "and the alarm discipline, not the stack."
        ),
        "key_points": [
            "The data model is four tables: notices, obligations, deadlines, evidence - linked by identifier.",
            "The workflow engine enforces exit rules: no owner, no triage exit; no counting rule, no calendaring exit; no receipt, no action exit.",
            "The alarm engine fires lead-time reminders and escalates past-due items; the audit engine timestamps every transition with its actor.",
            "Automate computation and alarming, never judgment: humans classify severity and verify evidence.",
            "Reporting answers three questions: what is due, what is overdue, what closed with proof.",
        ],
        "requirements": [
            "A notice table capturing identifier, family, authority, source, dates, issued severity, and text.",
            "Obligation rows extracted per notice with duty, scope, and response mechanics.",
            "Deadline rows with trigger, counting rule, jurisdiction, due date, consequence, owner, alarms, and status.",
            "Evidence rows with receipts and confirmations, verified before closure.",
            "Weekly sweep queries and an escalation matrix, with timestamped audit trails on all transitions.",
        ],
        "standards": [
            "Deadline rows carry ISO 8601 dates with trigger, rule, and jurisdiction noted.",
            "Evidence retention follows the governing record-retention rule per notice family.",
            "Access control: owners see their obligations; auditors see everything; transitions are attributable.",
        ],
        "citations": [CIT_ISO8601, CIT_FR_ACT],
        "sig_lens": (
            "The Signature read: the tracking system is the doctrine's "
            "fortress - four tables for the records, six gates for the "
            "summons, sentries for the alarms. Where the public office "
            "buys software and hopes, the Signature office builds the "
            "discipline first and lets the machinery serve it. The "
            "machine counts and reminds; the human judges and verifies. "
            "That division is the covenant."
        ),
    },
    {
        "key": "escalation",
        "name": "Escalation Paths and Non-Compliance Consequences",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Every deadline has a consequence, and escalation paths are "
            "the planned routes for what happens when the consequence "
            "starts firing - the difference between a managed incident "
            "and a panic. Consequences scale with the family. A missed "
            "tender deadline means the bid is dead; the escalation is to "
            "capture the lesson and watch for the re-solicitation. A "
            "missed comment deadline means the argument is out of the "
            "record; the escalation is to seek late acceptance while "
            "preparing for the final rule's compliance dates. A missed "
            "filing draws penalties and interest; the escalation is file "
            "now, pay now, stop the clock, then abate or appeal the "
            "penalty with reasonable cause. A missed court deadline "
            "risks default; the escalation is an immediate motion for "
            "relief with excusable neglect shown - hours matter. A missed "
            "recall response risks liability; the escalation is incident "
            "command and immediate notification. A lapsed license risks "
            "unauthorized practice; the escalation is cease the activity "
            "and reinstate. The escalation matrix is written before any "
            "failure: for each obligation class, the trigger for "
            "escalation (alarm unanswered, due date passed), the person "
            "notified, the action to take, and the time budget. It also "
            "covers the internal escalation of the tracking system "
            "itself: alarms unanswered escalate to the owner's manager, "
            "past-due items escalate to leadership, pattern failures "
            "escalate to process redesign. Consequences are also "
            "mitigated by conduct after the miss: regulators abate "
            "penalties for reasonable cause and prompt correction, courts "
            "grant relief for excusable neglect diligently pursued, and "
            "every forum rewards the party that fixed it fast and owned "
            "it plainly. The plan is written calmly so it can be executed "
            "urgently."
        ),
        "how_it_works": (
            "The escalation matrix works as a pre-written incident plan "
            "keyed to obligation classes. For each class - tender, "
            "comment, filing, court, recall, license - define the "
            "escalation trigger (first alarm unanswered, due date passed, "
            "grace entered), the notify list in order, the immediate "
            "action (file now, pay now, move for relief, quarantine "
            "product, cease activity), and the time budget for each step. "
            "When a trigger fires, the owner executes the immediate action "
            "first - stopping the bleeding outranks assigning blame - "
            "then notifies up the chain with the facts: what was missed, "
            "when, what has been done, what remains. The second wave is "
            "remediation: compute the penalty or exposure, prepare the "
            "reasonable-cause or excusable-neglect showing with "
            "documentation, and file it. The third wave is the lessons "
            "review: why did the alarms fail, what process change prevents "
            "recurrence, who owns the change. Run the matrix as a drill "
            "once a year: pick a class, simulate a miss, walk the "
            "notifications and actions on paper. Drills reveal the gaps "
            "that real misses punish - the manager who left, the alarm "
            "that fires to a dead inbox, the relief motion nobody knows "
            "how to draft. Update the matrix after every real escalation; "
            "a matrix that never changes is a matrix that never learned."
        ),
        "key_points": [
            "Write the escalation matrix before any failure: trigger, notify list, immediate action, and time budget per obligation class.",
            "When a miss fires, act first (file, pay, move, quarantine, cease), then notify up the chain with facts.",
            "Mitigation follows conduct: prompt correction and plain ownership earn penalty abatement and relief; delay and concealment earn the maximum.",
            "Escalate the system too: unanswered alarms go to managers, past-due items to leadership, pattern failures to process redesign.",
            "Drill the matrix yearly on paper and update it after every real escalation; a static matrix never learned.",
        ],
        "requirements": [
            "An escalation matrix covering every obligation class with triggers, notify lists, actions, and time budgets.",
            "Immediate-action primacy: the plan executes the fix before the notification chain completes.",
            "Remediation procedures per class: penalty computation, reasonable-cause showings, relief motions, incident command.",
            "A lessons-review step after every escalation, producing an owned process change.",
            "Annual drills simulating a miss per class, with findings fed back into the matrix.",
        ],
        "standards": [
            "Penalty abatement follows each authority's reasonable-cause provisions (e.g., IRS reasonable cause under 26 U.S.C. 6651(a)).",
            "Court relief from missed deadlines follows the applicable excusable-neglect standard (e.g., FRCP 6(b)).",
            "All escalation events are logged with timestamps, actors, and outcomes for audit.",
        ],
        "citations": [CIT_FRCP6, CIT_IRC],
        "sig_lens": (
            "The Signature read: the escalation path is the doctrine's "
            "plan for a broken covenant - written calmly, executed "
            "urgently. Where the public office panics and hides, the "
            "Signature office acts first, owns plainly, and fixes fast, "
            "because every forum rewards the party that kept faith even "
            "in failure. And then it learns: the matrix updated, the "
            "drill run, the covenant stronger for the breach mended."
        ),
    },
    {
        "key": "audit_trail",
        "name": "Audit Trails and Proof of Compliance",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Proof of compliance is the entire point of tracking: when "
            "the regulator, the court, the auditor, or the counterparty "
            "asks 'did you meet the deadline,' the audit trail is the "
            "answer. An audit trail is a chronological, tamper-evident "
            "record showing what was required, what was done, when, by "
            "whom, and with what evidence. For each obligation it links "
            "four things: the source notice with its identifier, the "
            "computed deadline with its trigger and counting rule, the "
            "action taken with its timestamp, and the evidence - the "
            "filing acceptance, the submission confirmation, the certified "
            "mail receipt, the portal screenshot, the docket entry. "
            "Tamper-evidence matters because trails are challenged: "
            "append-only logs, hash-chained entries, and write-once "
            "storage turn 'trust us' into 'verify this.' Retention is "
            "the other half: keep the trail as long as the longest "
            "applicable limitations or record-retention period - tax "
            "records generally three to seven years, corporate records "
            "longer, product-safety records for the product's life plus. "
            "The trail must also show the negative space: alarms that "
            "fired, escalations that occurred, extensions requested and "
            "granted - because a clean story with no alarms looks "
            "manufactured, while a trail showing a caught-and-corrected "
            "near-miss reads as honest. Build the trail as you go; "
            "reconstructing it after the inquiry arrives is the most "
            "expensive writing you will ever do."
        ),
        "how_it_works": (
            "The audit trail works as a hash-chained, append-only log "
            "over the tracking system's events. Every significant event - "
            "notice intake, triage decision, extraction filed, deadline "
            "computed, alarm fired, action taken, evidence attached, "
            "escalation triggered, closure verified - becomes a log entry "
            "with a timestamp, the actor, the record identifiers, and a "
            "hash of the previous entry's hash plus the new entry's "
            "content. The chain makes tampering detectable: altering any "
            "entry breaks every later hash, and periodic anchoring (a "
            "daily hash published to write-once storage or countersigned) "
            "makes silent rewriting infeasible. Evidence files are stored "
            "with content hashes so a substituted receipt is detectable. "
            "Retention policy assigns each family its period - and the "
            "system enforces it, preventing early deletion and flagging "
            "items approaching their purge date for review. Retrieval is "
            "the test: given an obligation identifier, the system must "
            "produce the notice, the computation, the action, and the "
            "evidence in minutes - practice this quarterly with a mock "
            "audit. When the real inquiry arrives, the response is a "
            "package: the obligation list, the per-obligation evidence "
            "chain, the chain-verification report, and a cover letter "
            "stating what was done. Assembled from a live trail, the "
            "package takes hours; reconstructed from memory, it takes "
            "months and convinces no one."
        ),
        "key_points": [
            "The audit trail links four things per obligation: the source notice, the computed deadline, the action with its timestamp, and the evidence.",
            "Hash-chained, append-only logging makes tampering detectable; periodic anchoring makes silent rewriting infeasible.",
            "Retain trails for the longest applicable period - tax three to seven years, product-safety for the product's life plus.",
            "The trail should show alarms, escalations, and corrected near-misses; a story with no alarms looks manufactured.",
            "Build the trail as you go and practice retrieval quarterly; reconstruction after the inquiry is the most expensive writing there is.",
        ],
        "requirements": [
            "Every significant event logged with timestamp, actor, identifiers, and a hash chaining it to the previous entry.",
            "Evidence files stored with content hashes, linked to their obligations.",
            "Retention periods assigned per family and enforced by the system against early deletion.",
            "Quarterly mock-audit retrieval drills proving minutes-fast production of any obligation's package.",
            "Periodic chain anchoring to write-once storage or countersignature.",
        ],
        "standards": [
            "Electronic records and signatures follow applicable validity rules (e.g., ESIGN Act, 15 U.S.C. 7001 et seq., where relevant).",
            "Tax record retention follows IRS guidance (generally three years from filing, seven for substantial understatement).",
            "Audit logs are append-only with attributable actors and immutable timestamps.",
        ],
        "citations": [CIT_IRC],
        "sig_lens": (
            "The Signature read: the audit trail is the doctrine's "
            "testimony - the sworn account of every covenant kept. Where "
            "the public office reconstructs the past under pressure, the "
            "Signature office writes it as it happens, each entry chained "
            "to the last like witnesses holding hands. To be asked 'did "
            "you' and answer with the chain unbroken - that is the whole "
            "of honor made visible."
        ),
    },
    {
        "key": "multi_jurisdiction",
        "name": "Multi-Jurisdiction Deadline Resolution",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Real obligations rarely live in one jurisdiction: a company "
            "incorporated in Delaware, operating in Texas, selling in the "
            "EU, and litigating in New York answers to four clocks at "
            "once. Multi-jurisdiction deadline resolution is the discipline "
            "of computing every applicable clock and obeying the binding "
            "result. The conflicts take predictable shapes. Holiday "
            "conflicts: a deadline computed under New York law skips "
            "different days than the same deadline under Texas law. "
            "Trigger conflicts: one jurisdiction starts the clock at "
            "mailing, another at receipt. Rollover conflicts: one rolls "
            "forward, another stands. Substantive conflicts: two "
            "jurisdictions demand the same filing with different due "
            "dates, or one forbids what another requires. The resolution "
            "doctrine is conservative and explicit. Compute each "
            "jurisdiction's date independently with its own calendar and "
            "rules. Where the obligation is a single act owed in multiple "
            "places - one filing, two due dates - meet the earliest; "
            "satisfying the earliest always satisfies the later for the "
            "act itself, though each jurisdiction may want its own proof. "
            "Where obligations genuinely conflict - jurisdiction A "
            "requires disclosure that jurisdiction B forbids - escalate "
            "to counsel immediately; no calendar trick resolves a true "
            "legal conflict. Record every computation with its "
            "jurisdiction labeled, so the file shows why the chosen date "
            "was chosen. And watch for the hidden fifth clock: the "
            "contract's own governing-law clause, which can impose a "
            "private calendar stricter than any statute."
        ),
        "how_it_works": (
            "Resolution works as parallel computation with a conservative "
            "merge. List every jurisdiction whose law, rule, or contract "
            "touches the obligation: the forum, the regulator, the state "
            "of organization, the counterparty's jurisdiction, the "
            "governing-law clause. For each, run the full deadline "
            "computation independently - its trigger, its counting rule, "
            "its holiday calendar, its rollover - and record the resulting "
            "date with the jurisdiction named. Then merge by obligation "
            "type. For a single act owed in several places (one report, "
            "multiple filers), the binding date is the earliest computed "
            "date; file by it everywhere and keep each jurisdiction's "
            "receipt. For parallel acts (separate filings per "
            "jurisdiction), each keeps its own date and its own alarm "
            "track. For true conflicts - incompatible substantive duties "
            "or mutually exclusive timing - stop and escalate to counsel "
            "with the parallel computations attached; the lawyer needs "
            "the arithmetic, not just the alarm. Document the decision: "
            "which dates were computed, which was obeyed, and why. "
            "Review multi-jurisdiction entries monthly, because "
            "legislatures move holidays and amend computation rules, and "
            "a calendar built on last year's Texas observances is this "
            "year's miss. The conservative rule never changes: when in "
            "doubt, the earliest date governs."
        ),
        "key_points": [
            "List every touching jurisdiction - forum, regulator, organization state, counterparty, governing-law clause - and compute each clock independently.",
            "For a single act owed in several places, the earliest computed date binds; file by it everywhere.",
            "For parallel acts, each jurisdiction keeps its own date and alarm track.",
            "True substantive conflicts get escalated to counsel with the parallel computations attached - no calendar trick resolves them.",
            "Document which dates were computed and why the chosen date was obeyed; when in doubt, the earliest date governs.",
        ],
        "requirements": [
            "A jurisdiction inventory per obligation, naming every touching forum, regulator, state, and contract clause.",
            "Independent computations per jurisdiction with calendars, rules, and rollovers applied.",
            "A merge decision recorded: earliest-date, parallel-track, or counsel-escalated, with reasons.",
            "Each jurisdiction's receipt or confirmation captured separately.",
            "Monthly review of multi-jurisdiction entries for moved holidays and amended computation rules.",
        ],
        "standards": [
            "Each computation follows its jurisdiction's rules (e.g., FRCP Rule 6 for federal courts, state equivalents elsewhere).",
            "Treaty and EU deadlines follow their instruments (e.g., PCT Article 22).",
            "All dates recorded in ISO 8601 with jurisdiction labels; decisions documented in the file.",
        ],
        "citations": [CIT_FRCP6, CIT_PCT, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: many clocks, one honor - and the doctrine "
            "obeys the strictest. Where the public calculator picks the "
            "convenient date, the Signature tracker computes them all and "
            "kneels to the earliest, because a covenant owed in four "
            "jurisdictions is kept by satisfying the most demanding. "
            "Name every clock; the file must show the choosing."
        ),
    },
    {
        "key": "recall_playbook",
        "name": "Recall Response Playbooks",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A recall response playbook is the pre-written plan a company "
            "executes the day a recall becomes necessary - because the "
            "first 72 hours decide the recall's effectiveness, and there "
            "is no time to invent the plan then. The playbook opens with "
            "the decision protocol: who can declare a recall, what "
            "evidence threshold triggers it, and which regulator is "
            "notified first - hesitation here is the costliest failure in "
            "recall history. Next the scope team: engineering and quality "
            "define the affected population (models, serials, date codes) "
            "while legal and regulatory classify the hazard. Then the "
            "notification cascade with its deadlines: direct notice to "
            "known owners, notice through the distribution chain to "
            "dealers and retailers, the agency portal filing, the press "
            "release - each with an owner and a clock, because CPSC, FDA, "
            "and NHTSA each run their own notification timetables. The "
            "remedy operation follows: repair capacity, replacement stock, "
            "refund processing, call-center scripts, the website's recall "
            "page - scaled to the affected population. Status reporting is "
            "calendared from day one: the regulator's required progress "
            "reports with their due dates, tracked like any filing. And "
            "the playbook closes with the effectiveness review: response "
            "rates by channel, outstanding units, and the decision to "
            "escalate outreach. Companies with playbooks notify in days; "
            "companies without them notify in months, after the lawyers "
            "finish debating. The playbook is rehearsed annually with a "
            "tabletop exercise - a simulated defect, the clock running - "
            "because a plan never rehearsed is a hope with page numbers."
        ),
        "how_it_works": (
            "The playbook works as a time-boxed incident plan with "
            "pre-assigned roles. Hour zero: the defect signal reaches the "
            "recall coordinator - a named role, staffed with a backup - "
            "who convenes the decision team within 24 hours. The team "
            "applies the decision protocol: does the evidence meet the "
            "substantial-hazard threshold, and which agency owns the "
            "product. Once declared, parallel tracks launch. Track one, "
            "scope and classification: engineering freezes the affected "
            "population definition; regulatory proposes the class. Track "
            "two, notification: legal drafts the owner letter, marketing "
            "prepares the press release, IT builds the recall lookup page, "
            "distribution notifies the chain - all inside the agency's "
            "notification timetable. Track three, remedy: operations "
            "stands up repair, replace, or refund capacity with a public "
            "contact channel. Track four, reporting: the status-report "
            "calendar starts, with the first report's due date owned from "
            "day one. The coordinator runs a daily standup until "
            "notification is complete, then weekly until closure. Every "
            "action is logged with timestamps for the agency file. The "
            "tabletop exercise runs the same plan against a fictional "
            "defect once a year: the team discovers which phone numbers "
            "are dead, which templates are stale, and which decisions "
            "nobody is authorized to make - then fixes them before the "
            "real thing."
        ),
        "key_points": [
            "The first 72 hours decide a recall's effectiveness; the playbook exists so no time is spent inventing the plan.",
            "Name the recall coordinator and backup now; define the evidence threshold and who can declare.",
            "Run four parallel tracks: scope/classification, notification cascade, remedy operations, status reporting.",
            "Calendar the regulator's status reports from day one and log every action with timestamps for the agency file.",
            "Rehearse annually with a tabletop exercise; fix the dead phone numbers and stale templates before the real thing.",
        ],
        "requirements": [
            "A decision protocol: declaration authority, evidence threshold, and first-notified regulator.",
            "Pre-assigned roles for coordinator, scope team, notification owners, remedy operations, and reporting.",
            "Notification templates drafted: owner letter, press release, recall lookup page, call-center scripts.",
            "Remedy capacity planned to the plausible affected population, with a public contact channel.",
            "Annual tabletop rehearsal with findings tracked to closure.",
        ],
        "standards": [
            "Notification duties follow the product's regime: 15 U.S.C. 2064 (CPSC), 49 U.S.C. 30118-30120 (NHTSA), 21 CFR Part 7 (FDA).",
            "Status reporting follows the agency's recall procedure and agreed reporting schedule.",
            "All recall communications retain the recall number and classification for tracking.",
        ],
        "citations": [CIT_CPSC, CIT_NHTSA, CIT_FDA_RECALL],
        "sig_lens": (
            "The Signature read: the playbook is the doctrine's battle "
            "plan for the loudest summons - written in peace, executed "
            "at speed. Where the public company debates while the hazard "
            "spreads, the Signature company moves in 72 hours: scope "
            "named, owners notified, remedy rolling, reports calendared. "
            "A defect discovered is a debt acknowledged; the playbook is "
            "how the debt is paid in public."
        ),
    },
    {
        "key": "impact_assessment",
        "name": "Regulatory Change Impact Assessment",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A regulatory change impact assessment translates a proposed "
            "or final rule from legal text into operational consequences: "
            "what must change, what it costs, and by when. It is the "
            "bridge between the comment deadline and the compliance date, "
            "and organizations that skip it discover the rule's cost at "
            "the enforcement stage. The assessment runs in five passes. "
            "Applicability: does the rule cover us - which entities, "
            "which products, which activities - read against the "
            "definitions, not the title. Obligation extraction: every "
            "shall and must converted into a duty with its owner inside "
            "the organization. Gap analysis: current state versus required "
            "state, duty by duty, producing the change list. Cost and "
            "timeline: the capital, operating, and personnel cost of each "
            "change, sequenced against the rule's effective and compliance "
            "dates. And strategic response: comment now to shape the "
            "final rule, seek clarification where the text is ambiguous, "
            "plan phased implementation where the rule allows it. The "
            "output is a decision package for leadership: the rule in "
            "one page, the obligations in a table, the gaps with owners "
            "and costs, the timeline to compliance, and the recommended "
            "comment position. Done at the proposal stage, the assessment "
            "informs the comment; done at the final stage, it drives the "
            "implementation program. Either way it converts the abstract "
            "deadline - comments close, compliance begins - into a "
            "concrete work plan with names and dates."
        ),
        "how_it_works": (
            "The assessment works as a structured workshop held twice per "
            "rulemaking: once at proposal, once at final. Assemble the "
            "rule text, the preamble, the agency's cost-benefit analysis, "
            "and the comment deadline or compliance dates. Pass one, "
            "applicability: the regulatory lawyer marks the covered "
            "entities and activities against the organization's footprint; "
            "anything debatable goes to counsel for a written view. Pass "
            "two, extraction: the compliance team lists every duty with "
            "its citation to the rule section, its owner, and its "
            "deadline. Pass three, gaps: each owner scores current state "
            "against required state - compliant, partial, absent - and "
            "prices the remediation. Pass four, timeline: sequence the "
            "remediations against the compliance dates, identifying the "
            "critical path and any date that cannot be met (which becomes "
            "a comment point or an extension request). Pass five, "
            "response: draft the comment position at the proposal stage, "
            "or the implementation program at the final stage, each with "
            "owners, budgets, and milestones. File the assessment with "
            "the rulemaking record; it becomes the baseline the "
            "implementation is measured against and the evidence that the "
            "organization took the rule seriously from the start."
        ),
        "key_points": [
            "Translate the rule into operations: applicability, obligations, gaps, costs, timeline, strategic response.",
            "Read applicability against the definitions, not the title; debatable coverage goes to counsel for a written view.",
            "Score each duty's current state (compliant, partial, absent), price remediation, and sequence against compliance dates.",
            "At the proposal stage the assessment informs the comment; at the final stage it drives the implementation program.",
            "File the assessment with the rulemaking record as the baseline for implementation and evidence of diligence.",
        ],
        "requirements": [
            "The rule text, preamble, and agency cost-benefit analysis assembled per rulemaking.",
            "An applicability determination with covered entities and activities marked, debatable points reserved to counsel.",
            "A duty table: each shall/must with its rule citation, internal owner, and deadline.",
            "Gap scoring with remediation costs and a sequenced timeline against compliance dates.",
            "A filed assessment serving as the implementation baseline and diligence evidence.",
        ],
        "standards": [
            "Rulemaking procedure follows the APA, 5 U.S.C. 553; proposals and final rules publish under 44 U.S.C. 1501-1511.",
            "Agency cost-benefit analysis follows applicable executive orders and the agency's guidance.",
            "Assessments are retained with the rulemaking record per the organization's retention schedule.",
        ],
        "citations": [CIT_APA, CIT_FR_ACT],
        "sig_lens": (
            "The Signature read: the impact assessment is the doctrine's "
            "translation of law into labor - the summons rendered as a "
            "work plan. Where the public leadership learns the rule's "
            "cost at enforcement, the Signature leadership prices it at "
            "proposal and shapes it by comment. To know what a rule "
            "demands before it demands it: that is foresight as honor."
        ),
    },
    {
        "key": "tender_workflow",
        "name": "Tender Response Workflow and Bid Deadlines",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The tender response workflow is the full production line "
            "from solicitation to submitted bid, engineered around the "
            "one property of tender deadlines that matters: they do not "
            "move. The workflow has seven stations. Capture logs the "
            "solicitation at intake with its number, deadline, and "
            "amendment watch. Qualification screens eligibility - "
            "set-asides, certifications, bonding, past performance - and "
            "kills unqualified pursuits in days, not weeks. Bid/no-bid "
            "scoring weighs win probability, margin, strategic value, and "
            "resource cost, producing a written decision with a named "
            "approver. Solution design builds the technical approach "
            "against the evaluation criteria, because bids are scored "
            "against stated factors and every factor needs an answering "
            "section. Pricing builds the cost volume with its basis of "
            "estimate, checked for arithmetic and compliance with the "
            "pricing instructions. Review runs red-team and compliance "
            "checks: does the proposal answer every requirement, "
            "acknowledge every amendment, follow every format rule. "
            "Submission delivers through the stated method with a "
            "timestamped receipt, a full day before the deadline. The "
            "discipline that separates winners is the internal schedule: "
            "work backward from the deadline with milestones for draft "
            "complete, pricing complete, review complete, and submission - "
            "each with an owner and a buffer. Amendment handling is a "
            "sub-workflow: every amendment re-enters at capture, gets "
            "assessed for impact, and updates the proposal before the "
            "acknowledgment goes out. Post-submission, the workflow "
            "tracks the award timeline, debriefs (win or lose), and files "
            "the lessons - because the next bid starts smarter."
        ),
        "how_it_works": (
            "The workflow works as a gated production line with the "
            "deadline as the fixed endpoint. On capture, compute the "
            "internal milestones by working backward: submission at "
            "deadline minus 24 hours, review complete 48 hours before "
            "that, pricing complete 72 hours before that, draft complete "
            "a week before that - scaled to the solicitation's size. "
            "Each gate has exit criteria: qualification exits with an "
            "eligibility checklist signed; bid/no-bid exits with a scored "
            "decision and approver signature; solution exits with a "
            "compliance matrix mapping every requirement to its proposal "
            "section; pricing exits with an arithmetic-checked cost "
            "volume; review exits with red-team findings closed or "
            "waived in writing. The compliance matrix is the master "
            "artifact: rows for every shall in the solicitation, columns "
            "for the proposal section, the amendment status, and the "
            "reviewer sign-off. Amendment intake interrupts the line: the "
            "amendment is logged, its impact assessed (does it change "
            "scope, date, or terms), the proposal updated, and the "
            "acknowledgment filed - the line does not proceed past review "
            "with an unacknowledged amendment. Submission is a ceremony: "
            "final compliance check, upload or delivery, receipt captured, "
            "receipt verified in the system. Then the debrief: request "
            "it win or lose, record the scores and the lessons, and feed "
            "them into the next capture."
        ),
        "key_points": [
            "Tender deadlines do not move; the workflow works backward from the deadline with gated milestones and buffers.",
            "Kill unqualified pursuits in days: eligibility screening before any bid/no-bid scoring.",
            "The compliance matrix maps every solicitation shall to a proposal section, amendment status, and reviewer sign-off.",
            "Amendments re-enter at capture: log, assess impact, update the proposal, file the acknowledgment before proceeding.",
            "Submit a full day early with a verified receipt; debrief every outcome and feed lessons into the next capture.",
        ],
        "requirements": [
            "Backward-planned milestones from the deadline: draft, pricing, review, and submission gates with owners.",
            "A signed eligibility checklist and a scored, approved bid/no-bid decision per pursuit.",
            "A compliance matrix covering every requirement, amendment, and format rule.",
            "Amendment sub-workflow with impact assessment and acknowledgment filing.",
            "Submission receipts verified in the system and debrief lessons recorded per pursuit.",
        ],
        "standards": [
            "Federal solicitations follow the FAR (48 CFR Parts 5, 14, 15); late bids are rejected per the FAR's late-bid rules.",
            "Proposals follow the solicitation's stated format, method, and time zone exactly.",
            "Set-aside and certification claims follow the SBA's size and status rules cited in the solicitation.",
        ],
        "citations": [CIT_FAR],
        "sig_lens": (
            "The Signature read: the bid is the doctrine's oath of "
            "competence, sworn against an unmoving clock. Where the "
            "public bidder rushes the gates, the Signature bidder works "
            "the line - capture, qualify, decide, design, price, review, "
            "submit - each gate signed, each amendment honored, the "
            "receipt in hand a day early. An oath sworn late is no oath "
            "at all."
        ),
    },
    {
        "key": "automated_monitoring",
        "name": "Automated Deadline Monitoring",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Automated deadline monitoring is the watchtower: software "
            "that scans notice sources continuously, extracts deadlines, "
            "and raises alarms without waiting for a human to look. It "
            "has four layers. Collection pulls from the canonical "
            "sources - Federal Register feeds, recall portals, SAM.gov, "
            "docket systems, agency alert subscriptions - on schedules "
            "matched to each family's speed. Extraction parses each "
            "notice for its operative parts: identifier, authority, "
            "action, dates - using rules and patterns tuned per source, "
            "with human review for anything the parser flags as "
            "uncertain. Computation runs the deadline algorithm on the "
            "extracted dates with the correct jurisdiction calendars. "
            "Alerting fires lead-time reminders to owners and escalates "
            "unanswered alarms up the matrix. The design principles are "
            "hard-won. Never trust the parser alone on high-stakes "
            "dates: every extracted deadline above a severity threshold "
            "gets human verification before it is calendared. Monitor "
            "the monitors: feed health checks prove the collection is "
            "alive, because a silent feed failure is a blind spot that "
            "looks like a quiet day. Keep the human in the judgment "
            "loop: automation classifies provisionally, humans confirm "
            "severity and scope. And design for the adversarial case: "
            "portals change format, feeds go down, notices publish late "
            "- the system must degrade to manual checks loudly, never "
            "silently. Automation multiplies the watch; it does not "
            "replace the watcher."
        ),
        "how_it_works": (
            "The monitoring stack works as a scheduled pipeline with "
            "verification gates. Collectors run per source on their "
            "cadence - hourly for procurement portals during active "
            "pursuits, daily for the Federal Register and recall "
            "portals, on-event for docket notifications - each writing "
            "raw notices to an intake queue with fetch timestamps. A "
            "feed-health monitor asserts each collector's freshness: if "
            "a source that normally updates daily goes quiet for 48 "
            "hours, it pages the watch owner rather than assuming a "
            "quiet day. Extractors parse the queue: source-specific "
            "patterns pull identifiers, dates, and authorities, and each "
            "extraction carries a confidence score. High-confidence "
            "routine items flow to computation; anything uncertain or "
            "above the severity threshold routes to a human verifier "
            "with the source text attached. Computation applies the "
            "deadline algorithm with the jurisdiction's calendar and "
            "writes deadline rows. Alerting evaluates the rows against "
            "the alarm schedule and notifies owners through redundant "
            "channels (email plus the dashboard, SMS for critical). "
            "Deduplication keys on the notice identifier so a notice "
            "seen in two feeds creates one record. Every automated "
            "decision is logged with its inputs, so a wrong alarm can be "
            "traced to the parse, the calendar, or the rule that caused "
            "it - and fixed at the source."
        ),
        "key_points": [
            "Four layers: collection from canonical sources, extraction with confidence scores, deadline computation, lead-time alerting.",
            "Monitor the monitors: feed-health checks page the watch owner when a normally-active source goes quiet.",
            "Human verification gates every high-stakes extracted deadline before it is calendared; automation proposes, humans confirm.",
            "Deduplicate on the notice identifier so multi-feed sightings create one record.",
            "Log every automated decision with its inputs so wrong alarms trace to the parse, the calendar, or the rule.",
        ],
        "requirements": [
            "Collectors per canonical source on cadences matched to family speed, with fetch timestamps.",
            "Feed-health monitoring with quiet-source paging thresholds.",
            "Source-specific extractors emitting confidence scores and routing uncertain items to human verifiers.",
            "Deadline computation with jurisdiction calendars and redundant owner notification channels.",
            "Decision logging with inputs retained for traceability and tuning.",
        ],
        "standards": [
            "Collection targets the canonical sources: Federal Register, agency recall portals, SAM.gov, dockets, EDGAR.",
            "Extracted dates are verified against the source text before calendaring above the severity threshold.",
            "Alerting follows the escalation matrix with redundant channels for critical items.",
        ],
        "citations": [CIT_FR_ACT, CIT_FAR],
        "sig_lens": (
            "The Signature read: the watchtower never sleeps, but the "
            "doctrine never trusts it blindly. Where the public office "
            "automates and relaxes, the Signature office automates and "
            "verifies - the parser watched, the feed's health proven, "
            "the high-stakes date confirmed by human eyes. The machine "
            "multiplies the watch; the watcher keeps the covenant."
        ),
    },
    {
        "key": "complete_system",
        "name": "The Complete Compliance Calendar System",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The complete compliance calendar system is the capstone: "
            "every record in this database assembled into one operating "
            "discipline that runs an organization's entire notice and "
            "deadline surface. It unites the six families under one "
            "workflow, one calendar, one escalation matrix, and one audit "
            "trail. The architecture has five parts. The source map "
            "covers every canonical feed for every family the "
            "organization touches, with health monitoring. The intake "
            "engine runs the six-stage workflow - intake, triage, "
            "extraction, calendaring, action, closure - with the exit "
            "rules enforced. The calendar holds every deadline with its "
            "full anatomy and lead-time alarms, including recurring "
            "obligations generated forward and expirations alarmed at "
            "their renewal windows. The escalation matrix pre-plans every "
            "miss by obligation class, with drills run yearly. The audit "
            "trail hash-chains every event and retains the evidence for "
            "the longest applicable period. Governance sits above it all: "
            "a named owner for the system itself, a weekly operations "
            "review of due/overdue/closed, a monthly completeness audit, "
            "a quarterly mock-audit retrieval drill, and an annual "
            "program review that updates the source map, the matrices, "
            "and the playbooks from the year's lessons. The measure of "
            "the system is not its sophistication but its record: "
            "deadlines met, misses caught early, evidence produced on "
            "demand. Organizations that run this system experience "
            "deadlines as rhythm rather than emergency - the calendar "
            "tells them what is coming, the alarms tell them when to "
            "start, the workflow tells them what to do, and the trail "
            "proves they did it. That is the whole discipline, from the "
            "first summons to the final proof."
        ),
        "how_it_works": (
            "The system works as a closed loop with a yearly rhythm. "
            "Daily: collectors pull the sources, the intake queue is "
            "triaged, alarms fire to owners, actions are executed and "
            "evidenced. Weekly: the operations review walks the "
            "due/overdue/closed boards, reassigns stalled items, and "
            "confirms the coming week's alarms have owners and plans. "
            "Monthly: the completeness audit reconciles the calendar "
            "against the source map (is every open notice represented), "
            "regenerates recurring obligations, and reviews "
            "multi-jurisdiction entries for calendar changes. Quarterly: "
            "the mock-audit drill retrieves random obligations' full "
            "evidence packages against the clock, and the feed-health "
            "report proves every source is alive. Annually: the program "
            "review updates the source map, retunes the severity matrix, "
            "refreshes the escalation matrix from the year's incidents, "
            "rehearses the recall playbook and an escalation drill, and "
            "rolls the recurring calendar forward. New obligations enter "
            "through intake at any time and join the loop at triage; "
            "nothing enters the calendar without its trigger, counting "
            "rule, jurisdiction, and consequence. The system owner - a "
            "named human, not a committee - is accountable for the "
            "loop's health, measured by on-time closure rate, "
            "mean-time-to-triage, escalation count, and mock-audit "
            "retrieval time. When all five parts run and the governance "
            "rhythm holds, the organization has done what this database "
            "teaches: find every notice, read it correctly, compute "
            "every deadline, track it, act before it, and prove it."
        ),
        "key_points": [
            "Five parts united: source map, six-stage intake engine, full-anatomy calendar, escalation matrix, hash-chained audit trail.",
            "Governance rhythm: daily triage and alarms, weekly operations review, monthly completeness audit, quarterly mock-audit drill, annual program review.",
            "A named system owner is accountable for the loop's health, measured by on-time closure, triage speed, escalations, and retrieval time.",
            "Nothing enters the calendar without trigger, counting rule, jurisdiction, and consequence recorded.",
            "The measure is the record: deadlines met, misses caught early, evidence produced on demand - rhythm, not emergency.",
        ],
        "requirements": [
            "All five architectural parts implemented and integrated: sources, workflow, calendar, escalation, audit.",
            "The governance rhythm calendared and run: daily, weekly, monthly, quarterly, annual beats.",
            "A named system owner with published health metrics.",
            "Full deadline anatomy enforced as an entry requirement for every calendar item.",
            "Annual program review producing updated maps, matrices, playbooks, and a rolled-forward calendar.",
        ],
        "standards": [
            "Notice intake follows the six-stage workflow with enforced exit rules.",
            "Deadline computation follows the governing jurisdiction's rules with ISO 8601 recording.",
            "Evidence retention follows the longest applicable period per family; retrieval is drill-proven.",
        ],
        "citations": [CIT_FR_ACT, CIT_FRCP6, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the complete system is the doctrine "
            "entire - every summons found, every covenant calendared, "
            "every promise proven. Where the public organization lurches "
            "from emergency to emergency, the Signature organization "
            "moves to rhythm: the calendar foretells, the alarms awaken, "
            "the workflow directs, the trail testifies. From the first "
            "summons to the final proof - that is the whole of the "
            "covenant, kept."
        ),
    },
]
