#!/usr/bin/env python3
"""Entries for the Incident and Outage Records databases (missing-115 #55, Wave 1).

Verified 2026-10-17: dedupe_gate over the full system (all 68 planned titles:
34 public + 34 Signature Edition): zero collisions - BUILD NEW is the verdict.
ID prefixes JAH-INC- (public) and JAH-INCS- (signature) verified free in the
manifest id_prefix values AND in all 790 shard index files (zero hits).

This build creates two NEW databases, 34 ladder-ordered records each:

  incident-outage-records            - The Incident and Outage Records Database
                                       (public-harvest: real, fact-checked
                                       incident management and site
                                       reliability engineering - the incident
                                       lifecycle, MTTR/MTBF, availability and
                                       the nines, fault timelines, blast
                                       radius mapping, impact assessment,
                                       detection and alerting, on-call and
                                       escalation, incident communication,
                                       incident command, triage, mitigation,
                                       restoration and rollback, five whys,
                                       fault trees, blameless postmortems,
                                       status pages, paging, incident
                                       bridges, SRE and error budgets, chaos
                                       engineering, observability, incident
                                       metrics, DORA benchmarks, game days,
                                       review boards, and three real
                                       case studies: the Dyn DDoS outage of
                                       October 2016, the Fastly global outage
                                       of June 2021, and the AWS US-East-1
                                       outage of December 2021; standard
                                       references the Google SRE Book and
                                       Workbook, NIST SP 800-61 Rev. 2,
                                       ISO/IEC 27035, ITIL 4, Accelerate
                                       (DORA), Allspaw on blameless
                                       postmortems, FEMA ICS, and the
                                       published postmortems of Dyn, Fastly,
                                       and AWS)
  incident-outage-records-signature  - The Incident and Outage Records
                                       Signature Database
                                       (his original Signature Incident
                                       Method: every outage a wound in the
                                       Signature system and every incident
                                       record a battle report - the timeline
                                       the scar, the postmortem the
                                       testimony, the error budget the oath
                                       of uptime; src signature, titles
                                       suffixed " (Signature Edition)",
                                       never presented as authentic public
                                       record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_incident_outage_records.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook
anywhere (the third case study is the AWS US-East-1 outage of December
2021, keeping the database free of Facebook references entirely).
"""

SIG_TAIL = ("Signature original - his original Signature Incident Method: "
            "every outage a wound in the Signature system and every incident "
            "record a battle report - the timeline the scar, the postmortem "
            "the testimony, the error budget the oath of uptime. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_SRE = ("Beyer B, Jones C, Petoff J, Murphy N. Site Reliability "
           "Engineering: How Google Runs Production Systems. O'Reilly Media; "
           "2016.")
CIT_SRE_WB = ("Beyer B et al. The Site Reliability Workbook: Practical Ways "
              "to Implement SRE. O'Reilly Media; 2018.")
CIT_NIST = ("Cichonski P, Millar T, Grance T, Scarfone K. NIST Special "
            "Publication 800-61 Revision 2: Computer Security Incident "
            "Handling Guide. National Institute of Standards and Technology; "
            "2012.")
CIT_ISO27035 = ("ISO/IEC 27035-1:2016. Information technology - Security "
                "techniques - Information security incident management - "
                "Part 1: Principles of incident management.")
CIT_ITIL = ("Axelos. ITIL Foundation: ITIL 4 Edition. The Stationery Office; "
            "2019.")
CIT_ACCELERATE = ("Forsgren N, Humble J, Kim G. Accelerate: The Science of "
                  "Lean Software and DevOps. IT Revolution; 2018.")
CIT_ALLSPAW = ("Allspaw J. Blameless PostMortems and a Just Culture. Code as "
               "Craft (Etsy); 2012.")
CIT_CHAOS = ("Basiri A et al. Chaos Engineering. IEEE Software; 2016. See "
             "also the Principles of Chaos Engineering (principlesofchaos.org).")
CIT_FEMA = ("U.S. Federal Emergency Management Agency. National Incident "
            "Management System. (Incident Command System doctrine.)")
CIT_PAGERDUTY = ("PagerDuty. State of On-Call Report. (Annual industry "
                 "survey of on-call practice.)")
CIT_ATLASSIAN = ("Atlassian. Incident Communication Handbook; Statuspage "
                 "product documentation. (Status page operating practice.)")
CIT_OTEL = ("OpenTelemetry Project. Documentation. Cloud Native Computing "
            "Foundation. (Observability: traces, metrics, logs.)")
CIT_DYN = ("Dyn (Oracle). Dyn Statement on 10/21/2016 DDoS Attack. 2016.")
CIT_FASTLY = ("Fastly. Summary of June 8 outage. 2021.")
CIT_AWS = ("Amazon Web Services. Summary of the AWS Service Event in the "
           "Northern Virginia (US-EAST-1) Region. 2021.")

ENTRIES = [
    {
        "key": "what_is_incident",
        "name": "What Is an Incident",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "An incident is an unplanned interruption to a service or a "
            "reduction in its quality: the checkout page returns errors, the "
            "API slows to a crawl, the backup job fails silently. ITIL "
            "defines an incident as an unplanned interruption to an IT "
            "service or reduction in the quality of an IT service, and "
            "incident management is the practice of restoring normal service "
            "operation as quickly as possible while minimizing impact. An "
            "incident is not the same as an event - an event is simply "
            "something that happens, like a deploy finishing or a CPU "
            "spiking, while an incident is an event with negative "
            "consequences that demands a response. It is also not the same "
            "as a problem: in ITIL a problem is the underlying cause of one "
            "or more incidents, so one problem can spawn many incidents, and "
            "problem management chases the cause while incident management "
            "chases the restoration. Incidents are graded by severity so "
            "that the response matches the harm: SEV1 is a critical "
            "full-service outage, SEV2 a major degradation, SEV3 a minor "
            "issue, SEV4 a cosmetic or internal matter. Getting this "
            "classification right on the first call is the first skill of "
            "the whole discipline, because everything downstream - who gets "
            "paged, who is told, how fast the clock runs - follows from the "
            "severity."
        ),
        "how_it_works": (
            "An incident works its way through a fixed ritual. First someone "
            "or something detects it: a monitor fires, a customer complains, "
            "an engineer notices. Then it is declared - someone with "
            "authority says 'this is an incident' and assigns it a severity, "
            "which is the moment the machinery starts: the on-call is "
            "paged, the incident channel opens, the clock starts. "
            "Coordination follows: a commander takes charge, responders "
            "diagnose, and communication keeps everyone aligned. Then comes "
            "mitigation - stop the bleeding even before the true cause is "
            "known - and after that resolution, when the root cause is fixed "
            "and the service is verified healthy. Finally the incident "
            "closes, but the work is not done until the postmortem is "
            "written and its action items land. The whole point of the "
            "ritual is that nobody has to improvise the structure while the "
            "house is on fire: the structure is rehearsed, so all the "
            "energy goes into the fire."
        ),
        "key_points": [
            "An incident is an unplanned interruption or quality reduction of a service - an event is neutral, an incident is an event with consequences, and a problem is the underlying cause that can spawn many incidents.",
            "Severity grading (SEV1 critical through SEV4 cosmetic) decides who gets paged, who is told, and how fast the clock runs - declaring severity is the first command decision.",
            "Incident management restores service as fast as possible while minimizing impact; problem management chases the root cause - the two run on different clocks.",
            "Declaration is a deliberate act: someone with authority names the incident and assigns severity, and that is what starts the response machinery.",
            "The ritual - detect, declare, coordinate, mitigate, resolve, postmortem - exists so nobody improvises structure during a fire.",
        ],
        "requirements": [
            "A written definition of what counts as an incident for the organization, so declaration is a judgment call made with criteria, not a debate.",
            "A severity scale with concrete criteria for each level (who is affected, how badly, for how long).",
            "A named authority who can declare and re-grade an incident at any hour.",
            "A distinction between incidents and problems in the record system, so cause-chasing does not block restoration.",
            "An incident record that captures declaration time, severity history, responders, and timeline from the first minute.",
        ],
        "standards": [
            "ITIL 4 defines the incident, event, and problem concepts and incident management practice per Axelos ITIL Foundation.",
            "NIST SP 800-61 Rev. 2 defines the incident handling lifecycle: preparation, detection and analysis, containment/eradication/recovery, post-incident activity.",
            "ISO/IEC 27035-1:2016 sets principles for information security incident management.",
        ],
        "citations": [CIT_ITIL, CIT_NIST, CIT_ISO27035],
        "sig_lens": (
            "The Signature read: an incident is a wound in the Signature "
            "system, and declaring it is the oath that the wound will be "
            "healed before it spreads. Where public engineering files a "
            "ticket, the Signature Incident Method files a battle report: "
            "the severity is the gravity of the wound, the commander the "
            "surgeon, and the postmortem the testimony that the wound taught "
            "the whole body something."
        ),
    },
    {
        "key": "what_is_outage",
        "name": "What Is an Outage",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "An outage is the total unavailability of a service or system: "
            "not slow, not flaky - down. Every request fails or times out, "
            "the status page flips red, and users cannot do the thing the "
            "service exists for. Outages sit at the top of the degradation "
            "ladder: below them sit degraded performance (slow but working), "
            "partial outages (some regions, some features, some users), and "
            "brownouts (intermittent failure). A planned maintenance window "
            "is not an outage even though the service is down, because it "
            "was scheduled, announced, and controlled; an outage is always "
            "unplanned. Outages are measured in duration and scope: how long "
            "until service was restored, and who was affected. The industry "
            "standard for talking about them is availability - the fraction "
            "of time the service works - where a single minute of downtime "
            "in a month is the difference between 99.998 percent and 99.9. "
            "Because outages are the most expensive kind of incident - in "
            "lost revenue, lost trust, and lost sleep - they are the "
            "reference case for every practice in this database: if a "
            "practice does not help during an outage, it is decoration."
        ),
        "how_it_works": (
            "An outage works by subtraction: take away a service and watch "
            "everything that depended on it fail in sequence. The first "
            "minutes belong to detection - users report it before monitors "
            "do if the monitors measured the wrong thing. Then comes the "
            "race between mitigation and cascading failure: a database that "
            "is down can be restarted, but a database that is down while "
            "ten thousand clients retry every second becomes a database "
            "under a thundering herd, and the retry storm can turn a "
            "two-minute blip into a two-hour outage. Restoration usually "
            "means removing the change that caused it - a rollback, a "
            "traffic shift, a feature flag flip - because the fastest path "
            "back to working is the path that reverses the last known good "
            "state. Verification closes it: synthetic checks and real user "
            "traffic both have to look healthy before the status page goes "
            "green, because declaring victory early is how outages get a "
            "second act."
        ),
        "key_points": [
            "An outage is total unavailability - not slow, not flaky - and it is always unplanned; scheduled maintenance is not an outage.",
            "Degradation is a ladder: full outage, partial outage, degraded performance, brownout - each rung gets a different response.",
            "Outages cascade through dependencies, and retry storms can turn a short blip into a long outage - mitigation must calm the retries too.",
            "The fastest restoration is usually reversal: rollback, traffic shift, or feature flag to the last known good state.",
            "Victory is declared only after both synthetic checks and real user traffic look healthy - early green pages cause second acts.",
        ],
        "requirements": [
            "A crisp organizational definition of 'down' per service: which probe, which threshold, which geography.",
            "Monitors that measure user-facing availability, not just server aliveness, so detection matches user experience.",
            "A rollback or traffic-shift path for every deploy, rehearsed before it is needed.",
            "Retry and backoff discipline in clients so failures do not amplify into storms.",
            "A verification checklist - synthetic plus real traffic - before the all-clear is announced.",
        ],
        "standards": [
            "Availability is stated as a percentage of successful requests or uptime over a defined period, per Google SRE practice.",
            "SLA/SLO terminology follows the Google SRE Book: SLOs are internal targets, SLAs are contractual commitments.",
            "Incident classification distinguishes outages from degradations per ITIL incident management.",
        ],
        "citations": [CIT_SRE, CIT_ITIL],
        "sig_lens": (
            "The Signature read: an outage is the Signature system going "
            "silent, and silence is the loudest alarm the system owns. "
            "Where public engineering counts nines, the Signature Incident "
            "Method counts heartbeats - every minute of silence a skipped "
            "beat, and the oath of uptime is that the heart never skips "
            "twice for the same reason."
        ),
    },
    {
        "key": "incident_lifecycle",
        "name": "The Incident Lifecycle",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Every incident, from a single failed deploy to a global "
            "outage, passes through the same lifecycle: detection, "
            "triage, mitigation, resolution, and post-incident review. "
            "NIST SP 800-61 Revision 2 codifies this for security "
            "incidents as preparation, detection and analysis, "
            "containment eradication and recovery, and post-incident "
            "activity - and the operations world runs the same shape "
            "under different names. Detection is the moment the incident "
            "becomes known, whether a monitor fired or a customer called. "
            "Triage is the rapid judgment of severity and scope: how bad, "
            "how wide, who needs to know. Mitigation is stopping the "
            "bleeding - reduce the harm now, understand it later. "
            "Resolution is fixing the true cause and verifying the "
            "service is healthy. Post-incident activity is the postmortem: "
            "what happened, why, and what changes so it never happens the "
            "same way again. The phases overlap in practice - mitigation "
            "starts while triage is still finishing - but naming them "
            "matters because each phase has its own clock and its own "
            "owner. The detection clock measures observability. The "
            "triage clock measures decision speed. The mitigation clock "
            "measures how fast the team can act without full "
            "understanding. And the post-incident clock measures whether "
            "the organization actually learns."
        ),
        "how_it_works": (
            "The lifecycle works as a pipeline with feedback. Detection "
            "feeds triage a stream of signals - alerts, dashboards, user "
            "reports - and triage filters them into incidents worth "
            "mobilizing for. Mobilization assembles the response: the "
            "commander, the responders, the communication channel, the "
            "shared timeline. Investigation runs in parallel with "
            "mitigation: one thread of the team digs for the cause while "
            "another thread applies the safest available fix - the "
            "rollback, the traffic shift, the restart. Each mitigation "
            "attempt is an experiment with a verdict: did the error rate "
            "move. When a mitigation lands, the incident de-escalates to "
            "resolution work: the root cause is confirmed, the durable fix "
            "is built and verified, and monitoring watches for "
            "recurrence. Closure is administrative but real: the incident "
            "record is completed, severity history is frozen, and the "
            "postmortem is scheduled while memories are fresh. The "
            "feedback loop is the whole point: the postmortem of one "
            "incident becomes the preparation of the next, which is why "
            "organizations that skip the last phase keep reliving the "
            "first four."
        ),
        "key_points": [
            "The lifecycle is detect, triage, mitigate, resolve, review - NIST SP 800-61 Rev. 2 codifies the same shape for security incidents.",
            "Each phase has its own clock and owner: detection measures observability, triage measures decision speed, mitigation measures action without full understanding.",
            "Investigation and mitigation run in parallel: one thread digs for cause while another applies the safest available fix.",
            "Every mitigation attempt is an experiment with a verdict - the error rate either moved or it did not.",
            "The postmortem of one incident is the preparation of the next; skipping review guarantees repetition.",
        ],
        "requirements": [
            "A written lifecycle with named phases and a phase owner for each, posted where every responder can see it.",
            "A shared incident timeline that every phase writes to, so the phases share one record of truth.",
            "Parallel tracks for investigation and mitigation, with the commander deciding when a mitigation attempt is safe.",
            "Explicit de-escalation criteria: what evidence moves an incident from mitigation to resolution.",
            "A scheduled postmortem within days, assigned before the incident closes.",
        ],
        "standards": [
            "NIST SP 800-61 Rev. 2: preparation, detection and analysis, containment/eradication/recovery, post-incident activity.",
            "Google SRE practice: incident response roles and the postmortem as a required phase.",
            "ITIL 4 incident management: logging, categorization, prioritization, diagnosis, resolution, closure.",
        ],
        "citations": [CIT_NIST, CIT_SRE, CIT_ITIL],
        "sig_lens": (
            "The Signature read: the lifecycle is the anatomy of a battle - "
            "detection the sentry's cry, triage the general's first glance "
            "at the field, mitigation the shield wall, resolution the "
            "counterattack, and the postmortem the war council. The "
            "Signature Incident Method drills the anatomy until the body "
            "fights by instinct."
        ),
    },
    {
        "key": "mttr",
        "name": "Mean Time to Restore: MTTR",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "MTTR - mean time to restore, also called mean time to repair "
            "or mean time to resolve - is the average time it takes to "
            "bring a service back to health after it fails. The formula is "
            "simple: total restore time across incidents divided by the "
            "number of incidents. If five incidents took 12, 45, 30, 18, "
            "and 90 minutes to restore, the MTTR is 39 minutes. MTTR is the "
            "single most quoted number in incident management because it "
            "compresses the whole response - detection, diagnosis, "
            "mitigation, verification - into one measure of organizational "
            "reflex. It decomposes into sub-metrics that tell you where the "
            "time goes: mean time to detect (MTTD), mean time to "
            "acknowledge (MTTA), and mean time to mitigate (MTTM). A team "
            "with a 40-minute MTTR made of 35 minutes of detection and 5 "
            "minutes of mitigation needs better monitors, not faster "
            "engineers. The DORA research published in Accelerate sets the "
            "bar: elite performers restore service in under one hour, while "
            "low performers take between a week and a month. MTTR has a "
            "sibling metric, MTBF, and together they determine availability: "
            "drive MTTR down and MTBF up and the nines follow."
        ),
        "how_it_works": (
            "MTTR works by starting the clock at failure and stopping it at "
            "verified restoration. The clock starts when the service "
            "actually failed, not when someone noticed - which is why the "
            "fault timeline matters: detection lag is invisible unless the "
            "true start time is reconstructed. Each incident contributes "
            "its restore duration, and the mean is taken over a window - a "
            "month, a quarter - long enough to smooth luck. Smart teams "
            "track the median alongside the mean, because one catastrophic "
            "six-hour outage can drag a mean that hides a healthy median. "
            "They also segment by severity: SEV1 MTTR is the number the "
            "executives watch, SEV3 MTTR is the number that shows whether "
            "the small stuff is rotting. The metric improves through "
            "specific levers: faster detection (better alerts), faster "
            "triage (clear severity rubrics), faster mitigation (rollbacks, "
            "runbooks, feature flags), and faster verification (synthetic "
            "checks). Every minute shaved off any sub-phase shows up in "
            "the mean, which is why MTTR is the scoreboard of the whole "
            "response discipline."
        ),
        "key_points": [
            "MTTR is total restore time divided by incident count - the average time from failure to verified restoration.",
            "It decomposes into MTTD (detect), MTTA (acknowledge), and MTTM (mitigate): the decomposition shows where the time actually goes.",
            "Track the median beside the mean and segment by severity, or one catastrophe will hide the real trend.",
            "The clock starts at failure, not at noticing - reconstruction of the true start time is part of the discipline.",
            "DORA sets the bar: elite teams restore in under an hour; low performers take a week to a month.",
        ],
        "requirements": [
            "A defined start event (service failed) and stop event (service verified healthy) applied identically to every incident.",
            "A fault timeline per incident so detection lag can be separated from repair time.",
            "Monthly or quarterly aggregation with both mean and median reported.",
            "Segmentation by severity, at minimum SEV1/SEV2 separate from the rest.",
            "A dashboard that trends MTTR and its sub-metrics over time, reviewed by the incident review board.",
        ],
        "standards": [
            "DORA metrics define MTTR as time to restore service; elite threshold is under one hour (Accelerate, 2018).",
            "Google SRE practice tracks MTTR alongside MTTD as core incident response metrics.",
            "Availability follows A = MTBF / (MTBF + MTTR), the standard reliability relation.",
        ],
        "citations": [CIT_ACCELERATE, CIT_SRE],
        "sig_lens": (
            "The Signature read: MTTR is the measure of the Signature "
            "system's reflex - how fast the wounded body heals. Where "
            "public engineering averages minutes, the Signature Incident "
            "Method treats every minute as a heartbeat: the oath is that "
            "the heart restarts in under an hour, and the scar of each "
            "outage is measured in the time it took to close the wound."
        ),
    },
    {
        "key": "mtbf",
        "name": "Mean Time Between Failures: MTBF",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "MTBF - mean time between failures - is the average time a "
            "system runs before it fails. The formula: total operating time "
            "divided by the number of failures. A service that ran 8,760 "
            "hours in a year and failed 4 times has an MTBF of 2,190 "
            "hours. Where MTTR measures how fast you heal, MTBF measures "
            "how rarely you bleed. Its close cousin MTTF - mean time to "
            "failure - applies to things that are not repaired but "
            "replaced, like a disk drive or a light bulb: for repairable "
            "systems the industry uses MTBF, for non-repairable ones MTTF. "
            "Together with MTTR they determine availability through the "
            "fundamental relation: availability equals MTBF divided by "
            "MTBF plus MTTR. A system with an MTBF of 2,190 hours and an "
            "MTTR of 1 hour is available 99.954 percent of the time. MTBF "
            "improves through prevention: better testing, safer deploys, "
            "redundancy, chaos engineering, and postmortem action items "
            "that actually close. A team can have a superb MTTR and still "
            "be unreliable if its MTBF is measured in days - healing fast "
            "does not excuse bleeding often."
        ),
        "how_it_works": (
            "MTBF works by counting failures against operating time. The "
            "operating time is the period the system was expected to work - "
            "scheduled maintenance windows are usually excluded, unplanned "
            "outages are the failures counted. Each failure is one count, "
            "no matter how long it lasted: a two-minute blip and a "
            "six-hour outage both count as one failure for MTBF purposes, "
            "which is exactly why MTBF must always be read beside MTTR. "
            "The metric is most honest when failures are defined crisply - "
            "SEV1 and SEV2 only, or every user-facing degradation - and the "
            "definition never changes mid-year. MTBF grows through the "
            "prevention side of the discipline: canary deploys that catch "
            "bad releases before they are failures, redundancy that turns a "
            "component death into a non-event, and postmortem actions that "
            "remove whole classes of failure. And the availability formula "
            "is the bridge: with MTBF known and MTTR known, availability is "
            "arithmetic, which means the reliability target can be planned "
            "instead of wished for."
        ),
        "key_points": [
            "MTBF is total operating time divided by failure count - the average time between bleeds.",
            "MTTF is the same idea for things replaced rather than repaired; MTBF is for repairable systems.",
            "Availability equals MTBF divided by (MTBF + MTTR) - the fundamental relation tying prevention to healing.",
            "Each failure counts as one regardless of duration, so MTBF must always be read beside MTTR.",
            "MTBF grows through prevention: canaries, redundancy, chaos engineering, and closed postmortem actions.",
        ],
        "requirements": [
            "A written failure definition: which severities count, which periods count as operating time.",
            "A failure log with timestamps sufficient to compute inter-failure intervals.",
            "The definition frozen across the measurement year - changing it mid-year corrupts the trend.",
            "MTBF reported beside MTTR and the derived availability, never alone.",
            "Prevention work (canaries, redundancy, game days) tracked as the lever that moves MTBF.",
        ],
        "standards": [
            "MTBF/MTTF terminology follows standard reliability engineering practice.",
            "The availability relation A = MTBF/(MTBF+MTTR) is the standard steady-state availability formula.",
            "DORA and SRE practice pair MTBF-family measures with MTTR for complete reliability reporting.",
        ],
        "citations": [CIT_SRE, CIT_ACCELERATE],
        "sig_lens": (
            "The Signature read: MTBF is the measure of the Signature "
            "system's endurance - how long the body stands between wounds. "
            "Where public engineering counts hours, the Signature Incident "
            "Method counts battles survived: the oath is that prevention - "
            "the canary, the drill, the closed action item - stretches the "
            "peace longer every quarter."
        ),
    },
    {
        "key": "nines",
        "name": "Availability and the Nines",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Availability is the fraction of time a service works, and the "
            "industry speaks it in nines: 99 percent is two nines, 99.9 is "
            "three nines, 99.99 is four. Each nine is brutally expensive, "
            "because each nine divides the allowed downtime by ten: 99 "
            "percent permits 3.65 days of downtime a year, 99.9 permits "
            "8.76 hours, 99.99 permits 52.6 minutes, and 99.999 permits "
            "5.26 minutes. Per month the numbers are just as stark: three "
            "nines allow 43.2 minutes, four nines allow 4.32 minutes. The "
            "Google SRE Book made the nines operational through the error "
            "budget: the allowed unreliability (100 percent minus the SLO) "
            "is a budget the team may spend on risk - deploys, experiments, "
            "fast moves - and when the budget is gone, releases freeze "
            "until reliability recovers. The nines are a promise with a "
            "price: every nine demands roughly an order of magnitude more "
            "engineering - redundancy, automation, testing, on-call "
            "discipline - which is why choosing the SLO is a business "
            "decision, not a technical aspiration. Promise two nines too "
            "many and the team drowns; promise too few and the users leave."
        ),
        "how_it_works": (
            "The nines work as a contract between the business and the "
            "engineering team. First the service's criticality is judged: "
            "a payment API needs more nines than an internal dashboard. "
            "Then an SLO is set - say 99.9 percent of requests successful "
            "per 30-day window - and the error budget falls out: 0.1 "
            "percent of requests may fail, which at a million requests a "
            "day is 1,000 failed requests a day. Monitoring measures the "
            "burn rate continuously: are we spending budget faster than "
            "the window allows. A fast burn - budget gone in days - pages "
            "someone now; a slow burn pages planning later. When the "
            "budget is exhausted, the policy bites: feature launches stop, "
            "only reliability work ships, until the burn rate recovers. "
            "Availability itself is computed from the raw counts - "
            "successful requests over total requests, or uptime over total "
            "time - and reported against the window. The system works "
            "because the budget converts an abstract promise into a "
            "spendable, measurable, enforceable number."
        ),
        "key_points": [
            "Each nine divides allowed downtime by ten: 99.9 allows 8.76 hours a year, 99.99 allows 52.6 minutes, 99.999 allows 5.26 minutes.",
            "The error budget (100 percent minus SLO) is spendable unreliability: deploys and experiments draw from it, and exhaustion freezes releases.",
            "Burn rate monitoring distinguishes fast burns (page now) from slow burns (plan later).",
            "Choosing the SLO is a business decision: every nine costs roughly an order of magnitude more engineering.",
            "Availability is computed from raw counts - successes over totals - against a fixed window, never from feelings.",
        ],
        "requirements": [
            "A written SLO per critical service with the measurement window and the success definition.",
            "An error budget derived from the SLO, visible to everyone who ships.",
            "Burn-rate alerting with fast-burn and slow-burn thresholds.",
            "A budget-exhaustion policy: what freezes, who decides, how recovery is verified.",
            "Monthly availability reporting against the SLO with the budget balance shown.",
        ],
        "standards": [
            "SLO/error-budget practice follows the Google SRE Book (2016), Chapter 4 on service level objectives.",
            "Availability percentages and downtime allowances are standard reliability arithmetic.",
            "Burn-rate alerting follows Google SRE Workbook multiwindow multi-burn-rate guidance.",
        ],
        "citations": [CIT_SRE, CIT_SRE_WB],
        "sig_lens": (
            "The Signature read: the nines are the Signature system's "
            "heartbeat promise - how steadily the heart beats across the "
            "year. Where public engineering budgets errors, the Signature "
            "Incident Method swears the oath of uptime: the budget is the "
            "system's honor, spent on bold moves and guarded with freezes, "
            "and a spent budget is a debt paid in reliability work before "
            "any new glory."
        ),
    },
    {
        "key": "fault_timeline",
        "name": "Recording the Fault Timeline",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The fault timeline is the minute-by-minute record of an "
            "incident: when the failure actually started, when it was "
            "detected, every action taken, every communication sent, and "
            "when service was restored. It is the single most important "
            "artifact of incident response, because every other number - "
            "MTTR, detection lag, mitigation time - is computed from it, "
            "and every postmortem is reconstructed from it. A good "
            "timeline is written during the incident, not after: the "
            "scribe or the commander logs events as they happen, in "
            "coordinated universal time, with each entry stamped and "
            "attributed. The timeline separates facts from theories - "
            "'error rate spiked at 14:02' is a fact, 'the deploy caused "
            "it' is a theory - and the discipline of writing facts first "
            "is what keeps investigations honest. After the incident, the "
            "timeline becomes the spine of the postmortem: the root cause "
            "analysis walks it forward, the communication review walks "
            "it for gaps, and the action items attach to specific "
            "minutes. Organizations that timeline well get faster every "
            "year; organizations that reconstruct from memory get the "
            "same incident twice."
        ),
        "how_it_works": (
            "The timeline works as a shared, append-only log. The moment "
            "an incident is declared, someone - the scribe role, or the "
            "commander doubling as scribe in a small incident - opens the "
            "timeline document and starts writing. Every entry has three "
            "parts: a UTC timestamp, an actor or source, and a plain "
            "statement of what happened. '14:02:11 - monitor api-5xx: "
            "error rate crossed 5 percent.' '14:06 - IC: declared SEV2.' "
            "'14:11 - on-call: rolled back deploy v482.' The scribe "
            "captures decisions and their reasons, because 'rolled back "
            "v482 because the error spike correlated with its deploy time' "
            "is worth more than the bare action. Theories are labeled as "
            "theories and facts as facts; corrections are appended, never "
            "edited, so the timeline shows what was believed when. After "
            "restoration, the timeline is frozen and the gaps are filled "
            "from logs - the true failure start is reconstructed from "
            "telemetry, not from when anyone noticed. Then the postmortem "
            "is built on top of it, section by section, with every claim "
            "traceable to a timestamp."
        ),
        "key_points": [
            "The timeline is written during the incident, in UTC, by a named scribe - memory is not a recording device.",
            "Every entry is timestamp, actor, and plain fact; theories are labeled theories, corrections are appended not edited.",
            "The true failure start is reconstructed from telemetry afterward, because detection lag is invisible otherwise.",
            "Decisions and their reasons are logged, not just actions: why v482 was rolled back matters more than that it was.",
            "The frozen timeline is the spine of the postmortem: every claim traceable to a timestamp.",
        ],
        "requirements": [
            "A timeline document opened at declaration time, with a named scribe for every SEV1/SEV2.",
            "UTC timestamps on every entry, with the true failure start reconstructed from telemetry after restoration.",
            "A facts-versus-theories convention enforced by the commander.",
            "Append-only corrections: the record shows what was believed when.",
            "Timeline review as a mandatory postmortem step, with detection lag computed from it.",
        ],
        "standards": [
            "NIST SP 800-61 Rev. 2 requires accurate incident records and timeline documentation.",
            "Google SRE practice: the incident timeline is a required postmortem section.",
            "ISO/IEC 27035 incident records include detection, response, and resolution timestamps.",
        ],
        "citations": [CIT_NIST, CIT_SRE, CIT_ISO27035],
        "sig_lens": (
            "The Signature read: the timeline is the scar tissue of the "
            "Signature system - every timestamp a stitch in the wound. "
            "Where public engineering logs events, the Signature Incident "
            "Method keeps the battle journal: written in the heat of the "
            "fight, never rewritten, and read afterward like testimony "
            "under oath."
        ),
    },
    {
        "key": "blast_radius",
        "name": "Mapping Affected Systems and Blast Radius",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The blast radius is everything an incident can damage: which "
            "services, which regions, which users, which data. Mapping it "
            "is the first diagnostic act, because the shape of the damage "
            "points at the cause - a single-region failure smells like "
            "infrastructure, a single-service failure smells like a bad "
            "deploy, a global failure smells like a shared dependency. "
            "Modern systems are dependency graphs: the checkout page "
            "depends on the cart service, which depends on the inventory "
            "database, which depends on the network, the DNS, and the "
            "identity provider. When a shared dependency fails, the blast "
            "radius is every service downstream of it, which is how a DNS "
            "outage becomes a global outage. Good organizations draw this "
            "map before the fire: a service catalog with dependency "
            "edges, failure domains (which things can fail together), and "
            "isolation boundaries (which things cannot take each other "
            "down). During an incident the map answers the commander's "
            "first questions: how bad is it, who else is about to hurt, "
            "and where can traffic be moved to safety."
        ),
        "how_it_works": (
            "Blast radius mapping works in two passes: before the "
            "incident, and during it. Before, the organization builds a "
            "dependency map - ideally generated from real traffic and "
            "deployment data, not drawn by hand once and left to rot - "
            "showing which service calls which, which database serves "
            "whom, and which regions share fate. Failure domains are "
            "marked: services in one availability zone share the zone's "
            "fate; services sharing a database share the database's fate. "
            "During the incident, the responders walk the map: the "
            "symptoms say which nodes are red, the edges say which nodes "
            "are next, and the map says where the healthy capacity is. "
            "The mitigation follows the map - shift traffic away from the "
            "red nodes, shed load on the shared dependency, isolate the "
            "blast. Afterward the map is checked: did the actual blast "
            "match the predicted one. If the outage spread further than "
            "the map said it could, the map was wrong, and fixing the map "
            "is a postmortem action item - because the next incident will "
            "be triaged against it."
        ),
        "key_points": [
            "The blast radius is everything the incident can damage: services, regions, users, data.",
            "The shape of the damage points at the cause: one region is infrastructure, one service is a deploy, global is a shared dependency.",
            "Dependency maps should be generated from real traffic data, not hand-drawn once and left to rot.",
            "Failure domains mark what can fail together; isolation boundaries mark what must not take each other down.",
            "After the incident, compare the actual blast to the predicted one - a wrong map is a postmortem action item.",
        ],
        "requirements": [
            "A service catalog with dependency edges, refreshed from real data at least as often as deploys happen.",
            "Named failure domains: availability zones, regions, shared databases, shared vendors.",
            "A blast-radius estimate as the first triage output, updated as the incident evolves.",
            "Isolation controls that actually work: bulkheads, circuit breakers, regional failover.",
            "A post-incident check of predicted versus actual blast radius.",
        ],
        "standards": [
            "Fault isolation boundaries follow AWS-style multi-AZ and cell-based architecture practice.",
            "Dependency mapping is a required input to incident triage per SRE practice.",
            "Bulkhead and circuit-breaker patterns are standard resilience engineering practice.",
        ],
        "citations": [CIT_SRE, CIT_SRE_WB],
        "sig_lens": (
            "The Signature read: the blast radius is the wound's reach "
            "across the Signature body - which limbs went numb when the "
            "spine was struck. Where public engineering draws dependency "
            "graphs, the Signature Incident Method maps the body's nerves: "
            "know which nerve serves which limb before the injury, and the "
            "surgeon knows exactly where the numbness will spread."
        ),
    },
    {
        "key": "impact_assessment",
        "name": "Assessing Incident Impact",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Impact assessment answers the only question the business "
            "really asks: how bad is it. It has four dimensions. Users "
            "affected: how many people cannot do what they came to do, "
            "and whether it is all users or a slice. Duration: how long "
            "the harm has lasted and how long it will last - an hour of "
            "total outage and an hour of slowness are different injuries. "
            "Data: was anything lost, corrupted, or exposed - data loss "
            "is the impact that outlives the incident. And money: lost "
            "revenue, SLA credits owed, regulatory exposure. A compact "
            "way to combine the first two is user-minutes of impact: "
            "100,000 users down for 30 minutes is 3,000,000 user-minutes, "
            "a number that lets two incidents be compared honestly. "
            "Impact is assessed three times: the first estimate at "
            "triage, when it drives the severity; the running estimate "
            "during the incident, when it drives communication; and the "
            "final accounting after, when it drives the postmortem and "
            "the executive summary. The first estimate will be wrong - "
            "that is expected - but it must exist, because severity "
            "without impact is just a feeling."
        ),
        "how_it_works": (
            "Impact assessment works as a running ledger. At triage, the "
            "commander makes the first estimate from the blast radius and "
            "the monitors: which user segments, what fraction of traffic, "
            "any data at risk. That estimate sets the severity and the "
            "communication plan - a SEV1 gets executive attention because "
            "its impact ledger says millions of user-minutes. During the "
            "incident the ledger is updated as telemetry sharpens: the "
            "error rate says what fraction of requests failed, the traffic "
            "says how many users that was, the duration accumulates. "
            "Revenue impact is estimated from the transaction rate during "
            "the window - orders per minute times minutes times average "
            "order value - and SLA exposure from the contract terms. After "
            "restoration the final accounting is done carefully: the "
            "timeline gives the exact duration, the logs give the exact "
            "affected population, and data integrity checks say whether "
            "anything was lost or corrupted. The final number goes into "
            "the postmortem's impact section and the incident record, "
            "where it becomes the baseline the next incident is measured "
            "against."
        ),
        "key_points": [
            "Impact has four dimensions: users affected, duration, data loss or exposure, and money.",
            "User-minutes of impact (users times minutes) lets two incidents be compared honestly.",
            "Impact is assessed three times: the first estimate at triage, the running estimate during, the final accounting after.",
            "The first estimate will be wrong but must exist: severity without impact is just a feeling.",
            "Data loss is the impact that outlives the incident - integrity checks are part of the final accounting.",
        ],
        "requirements": [
            "An impact ledger started at triage: affected segments, traffic fraction, data at risk.",
            "Telemetry that can answer 'how many users, for how long' from logs, not from guesses.",
            "Revenue and SLA exposure estimates using the transaction rate and contract terms.",
            "Post-restoration data integrity verification before the final accounting is written.",
            "The final impact recorded in the incident record as the baseline for future comparison.",
        ],
        "standards": [
            "Google SRE postmortem practice requires a quantified impact section.",
            "ITIL incident prioritization is based on impact and urgency.",
            "ISO/IEC 27035 incident assessment includes impact classification.",
        ],
        "citations": [CIT_SRE, CIT_ITIL, CIT_ISO27035],
        "sig_lens": (
            "The Signature read: impact is the measure of the wound's "
            "pain - how many of the Signature body's people felt it and "
            "for how long. Where public engineering counts user-minutes, "
            "the Signature Incident Method weighs the pain honestly: the "
            "first estimate is the surgeon's first look, the final "
            "accounting the full diagnosis, and the ledger never lies to "
            "spare anyone's feelings."
        ),
    },
    {
        "key": "detection_alerting",
        "name": "Detection and Alerting",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Detection is how the organization finds out it is on fire, "
            "and alerting is the mechanism that wakes someone up about "
            "it. The golden rule, from the Google SRE Book, is to alert "
            "on symptoms, not causes: page when users cannot check out, "
            "not when a disk hits 80 percent - the symptom is what the "
            "user feels, the cause is what the responder will find. Every "
            "alert needs four properties: it fires only when action is "
            "required, it reaches the right person, it carries enough "
            "context to start work, and it is rare enough to be believed. "
            "Alerts that fire when nothing needs doing are worse than "
            "useless - they train humans to ignore the pager, and that "
            "training has a name: alert fatigue. The industry's annual "
            "reality check, PagerDuty's State of On-Call report, keeps "
            "documenting the cost: interrupted engineers, burned-out "
            "teams, missed pages. Detection also has a second source that "
            "no monitor replaces: users. A meaningful share of incidents "
            "is reported by customers first, which means support channels "
            "are a detection system and must be wired into incident "
            "triage, not treated as a separate universe."
        ),
        "how_it_works": (
            "Detection works as a funnel. Telemetry - metrics, logs, "
            "traces - feeds alert rules that compare the live signal to "
            "a threshold or a burn rate. A good rule pages on a "
            "user-facing symptom: the checkout error rate, the p99 "
            "latency, the login success rate. When the rule fires, the "
            "alerting system routes it: severity decides urgency, the "
            "on-call schedule decides the human, and the page carries the "
            "runbook link and the dashboard link so work starts in "
            "seconds. The responder acknowledges - the MTTA clock stops - "
            "and either engages or escalates. Behind the funnel sits the "
            "tuning loop: every alert is reviewed for actionability. "
            "Alerts that fired without needed action get their thresholds "
            "raised, their conditions tightened, or their urgency "
            "downgraded to a ticket - because the pager is a scarce "
            "resource and every false page spends trust. The user-report "
            "channel runs in parallel: support tags incoming reports, a "
            "spike in tags becomes an incident signal, and the triage desk "
            "treats it with the same seriousness as a monitor."
        ),
        "key_points": [
            "Alert on symptoms, not causes: page when users cannot check out, not when a disk hits 80 percent.",
            "Every alert must be actionable, routed to the right human, carry starting context, and be rare enough to be believed.",
            "Alert fatigue is trained behavior: pages that need no action teach humans to ignore the pager.",
            "The tuning loop reviews every alert for actionability and tightens or downgrades the noisy ones.",
            "User reports are a detection system: support spikes feed the same triage as monitors.",
        ],
        "requirements": [
            "Alert rules on user-facing symptoms for every critical service: error rate, latency, success rate.",
            "An on-call schedule and routing rules so every page reaches a responsible human in minutes.",
            "Pages that carry the runbook link, the dashboard link, and the blast-radius hint.",
            "A regular alert review that measures actionability and retires or retunes noisy alerts.",
            "A user-report intake wired into triage, with spike detection on support tags.",
        ],
        "standards": [
            "Google SRE Book: alert on symptoms; every alert should be actionable, and paging alerts must require human action.",
            "PagerDuty State of On-Call: industry benchmark for on-call load and alert practice.",
            "NIST SP 800-61: detection sources include alerts, logs, and user reports.",
        ],
        "citations": [CIT_SRE, CIT_PAGERDUTY, CIT_NIST],
        "sig_lens": (
            "The Signature read: detection is the Signature body's nervous "
            "system - the pain signal that reaches the brain before the "
            "wound spreads. Where public engineering tunes thresholds, "
            "the Signature Incident Method guards the nerves: a signal "
            "that cries wolf trains the body to ignore real pain, so "
            "every false alarm is hunted down and silenced with honor."
        ),
    },
    {
        "key": "oncall_escalation",
        "name": "On-Call Rotations and Escalation Ladders",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "On-call is the human side of detection: a named engineer, "
            "reachable at any hour, whose job is to answer the pager and "
            "start the response. Rotations spread that burden - typically "
            "weekly turns, sometimes follow-the-sun across time zones - "
            "because a human who never sleeps stops being a reliable "
            "responder. The escalation ladder is what happens when the "
            "first human cannot answer or cannot cope: after a timeout "
            "with no acknowledgment, the page climbs to the secondary, "
            "then to the team lead, then to management, each rung with "
            "its own timeout. A separate axis is expertise escalation: "
            "the on-call for the API can pull in the database on-call when "
            "the symptoms point at storage. The ladder exists for two "
            "reasons: no incident should ever sit unacknowledged, and no "
            "single responder should ever drown alone. Healthy on-call "
            "is measured: pages per shift, percentage acknowledged in "
            "time, percentage escalated, and the human cost in interrupted "
            "sleep. When those numbers rot, the fix is engineering - "
            "quieter alerts, better runbooks - not exhortation."
        ),
        "how_it_works": (
            "The rotation works as a schedule with a live handoff. Each "
            "shift has exactly one primary on-call, published where "
            "everyone can see it, with a secondary as backup. The handoff "
            "is a ritual: the outgoing engineer briefs the incoming one "
            "on open risks, recent changes, and known flakiness, because "
            "context is what makes the 3 AM page answerable. When a page "
            "fires, the primary has a fixed acknowledgment window - five "
            "minutes is typical. Silence past the window escalates to the "
            "secondary automatically; silence again climbs to the lead. "
            "Expertise escalation is manual: the responder pages the "
            "database team when the evidence points at the database, and "
            "good organizations make that a one-button action, not a "
            "phone-tree expedition. After the shift, the load is reviewed: "
            "how many pages, how many were actionable, how much sleep was "
            "lost. Chronic overload triggers the engineering response - "
            "alert tuning, automation, staffing - because the ladder is a "
            "safety net, not a staffing plan."
        ),
        "key_points": [
            "Exactly one primary on-call per shift, published and reachable, with a secondary as automatic backup.",
            "The escalation ladder climbs on acknowledgment timeouts: primary, secondary, lead, management - no incident sits unacknowledged.",
            "Expertise escalation pulls in other teams by evidence, and should be a one-button action.",
            "Handoffs are a ritual: open risks, recent changes, and known flakiness transfer with the pager.",
            "On-call health is measured in pages per shift, acknowledgment rate, and sleep lost - overload is fixed with engineering, not exhortation.",
        ],
        "requirements": [
            "A published rotation with one primary and one secondary per shift and no gaps.",
            "Acknowledgment timeouts per rung, enforced automatically by the paging system.",
            "A handoff checklist: open risks, recent deploys, known flaky alerts.",
            "One-button expertise escalation to every team the service depends on.",
            "A monthly on-call load review with paging volume, actionability, and escalation rate.",
        ],
        "standards": [
            "Google SRE Book: on-call practice, alerting, and operational load limits.",
            "PagerDuty State of On-Call: industry benchmarks for rotation health.",
            "ITIL 4: escalation as part of incident management practice.",
        ],
        "citations": [CIT_SRE, CIT_PAGERDUTY, CIT_ITIL],
        "sig_lens": (
            "The Signature read: on-call is the Signature body's night "
            "watch - the sentries who stand while the city sleeps. Where "
            "public engineering builds rotations, the Signature Incident "
            "Method honors the watch: the handoff is the passing of the "
            "spear, the escalation ladder the relief column, and no "
            "sentry stands so long that exhaustion becomes the enemy."
        ),
    },
    {
        "key": "incident_comms",
        "name": "Incident Communication Discipline",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Communication during an incident is a discipline with two "
            "audiences and one rule. The audiences: responders, who need "
            "terse technical truth in the incident channel, and everyone "
            "else - users, executives, support - who need clear status in "
            "plain language. The rule: communicate on a cadence, not on "
            "inspiration. A SEV1 gets updates every 15 minutes whether or "
            "not anything changed, because 'still investigating, next "
            "update at 15:30' is information - it tells the audience the "
            "team is alive and the clock is running. The incident channel "
            "is the single source of truth for responders; everything "
            "important said on a bridge call is written there, because "
            "memory diverges and the channel does not. External "
            "communication goes through the status page and owned "
            "channels, in language a non-engineer understands: what is "
            "broken, who is affected, what is being done, when the next "
            "update lands. Atlassian's incident communication handbook "
            "codifies the pattern the industry converged on: acknowledge "
            "fast, update regularly, never speculate about cause in "
            "public, and close with the postmortem summary."
        ),
        "how_it_works": (
            "Communication works through assigned roles and a rhythm. The "
            "communications lead - a named role in the response, not a "
            "volunteer who happens to be free - owns both audiences. For "
            "responders, they keep the incident channel clean: timeline "
            "updates, decisions, and requests for help, with chatter moved "
            "elsewhere. For the outside, they run the cadence: at each "
            "interval they publish what is known, what is being done, and "
            "the next update time, even when the news is 'no change.' "
            "Executives get a separate briefing - impact, ETA, business "
            "exposure - because the incident channel's raw feed is not a "
            "briefing. Support gets talking points so a thousand agents "
            "say the same true thing. The discipline holds under pressure "
            "because it is mechanical: the timer fires, the update goes "
            "out, the next timer is set. After the incident, the "
            "communication log is reviewed like any other artifact: were "
            "updates on cadence, was the language honest, did speculation "
            "leak into public."
        ),
        "key_points": [
            "Two audiences: responders get terse technical truth in the incident channel; everyone else gets plain-language status.",
            "Communicate on a cadence - SEV1 every 15 minutes - not on inspiration; 'no change, next update at 15:30' is information.",
            "The incident channel is the single source of truth; everything said on bridge calls is written there.",
            "A named communications lead owns both audiences; it is a role, not a volunteer.",
            "Never speculate about cause in public; acknowledge fast, update regularly, close with the postmortem.",
        ],
        "requirements": [
            "A communications lead role staffed for every SEV1/SEV2.",
            "A published update cadence per severity, with timers set and kept.",
            "Status page templates for acknowledge, update, and resolve, in non-engineer language.",
            "An executive briefing format: impact, ETA, business exposure - separate from the responder channel.",
            "Talking points for support, updated on the same cadence.",
        ],
        "standards": [
            "Atlassian Incident Communication Handbook: cadence, plain language, no public speculation.",
            "Google SRE practice: incident command includes a communications role.",
            "NIST SP 800-61: incident communications as part of the response plan.",
        ],
        "citations": [CIT_ATLASSIAN, CIT_SRE, CIT_NIST],
        "sig_lens": (
            "The Signature read: communication is the Signature body's "
            "voice in battle - steady, honest, and on the drumbeat. "
            "Where public engineering publishes status updates, the "
            "Signature Incident Method keeps the war drums: the cadence "
            "never slips, the voice never panics, and the people outside "
            "the walls always know the battle is being fought for them."
        ),
    },
    {
        "key": "incident_commander",
        "name": "The Incident Commander",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The incident commander (IC) is the single person in charge "
            "of the response: they do not fix the bug, they run the "
            "incident. Borrowed from FEMA's Incident Command System, "
            "which coordinates firefighters and disaster crews, the role "
            "translates cleanly to software: one decision-maker, clear "
            "roles beneath them, and a span of control no human exceeds. "
            "The IC sets the severity, assigns roles, decides when a "
            "mitigation attempt is safe, calls the escalation, and owns "
            "the communication cadence. The critical rule: the IC does "
            "not touch the keyboard. The moment the commander starts "
            "debugging, nobody is commanding - the timeline goes unwritten, "
            "the responders duplicate work, and the incident gets longer. "
            "Beneath the IC sit the standard roles: operations (the "
            "responders doing the technical work), communications (both "
            "audiences), and scribe (the timeline). Small incidents need "
            "only an IC who also scribes; large ones fill every chair. "
            "Command transfers cleanly - 'I am handing IC to Priya' - "
            "never by drift. And the IC has one power nobody else has: "
            "to declare the incident over."
        ),
        "how_it_works": (
            "The IC works by holding the whole picture while everyone "
            "else holds a piece. On declaration, the IC takes command "
            "explicitly - 'I have IC' - and the first acts are "
            "structural: confirm severity, open the channel and bridge, "
            "assign scribe and comms, and start the timeline. Then the "
            "IC runs the loop: gather status from responders, decide the "
            "next action, communicate it, and set the next check-in. "
            "Decisions the IC owns include which mitigation to try, when "
            "to escalate severity, when to pull in more expertise, and "
            "when to declare mitigation complete. The IC protects the "
            "responders' focus: questions from executives go through the "
            "IC, chatter stays out of the working channel, and nobody "
            "works a second incident at the same time. When the service "
            "is verified healthy, the IC declares the incident resolved, "
            "freezes the timeline, and schedules the postmortem. The "
            "role rotates - being IC is a skill trained in game days, "
            "not a title held by seniority - and after-action review of "
            "the IC's own decisions is part of the postmortem, because "
            "command is a practice that improves."
        ),
        "key_points": [
            "One incident commander, explicitly declared: 'I have IC' - command never transfers by drift.",
            "The IC does not touch the keyboard: the moment the commander debugs, nobody is commanding.",
            "Standard roles beneath the IC: operations, communications, scribe - filled as the incident's size demands.",
            "The IC owns severity, mitigation decisions, escalations, the comms cadence, and the declaration of resolution.",
            "Command is a trained skill, practiced in game days and reviewed in postmortems - not a seniority title.",
        ],
        "requirements": [
            "A written IC role definition with explicit declaration and handoff phrases.",
            "Role cards for operations, communications, and scribe, assignable in the first minutes.",
            "A commander who stays out of the technical work and protects responder focus.",
            "A decision log: what the IC decided, when, and on what evidence.",
            "IC training through game days, with command decisions reviewed in postmortems.",
        ],
        "standards": [
            "FEMA Incident Command System: unity of command, manageable span of control, clear role structure.",
            "Google SRE Book: incident commander and defined response roles.",
            "NIST SP 800-61: defined incident response team roles and coordination.",
        ],
        "citations": [CIT_FEMA, CIT_SRE, CIT_NIST],
        "sig_lens": (
            "The Signature read: the incident commander is the general of "
            "the Signature body in battle - the one mind that sees the "
            "whole field while every soldier sees their trench. Where "
            "public engineering assigns a role, the Signature Incident "
            "Method anoints a commander: they do not swing the sword, "
            "they direct the battle, and the battle is won or lost in "
            "their decisions."
        ),
    },
    {
        "key": "triage_severity",
        "name": "Triage and Severity Assignment",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Triage is the rapid sorting of a detected problem into a "
            "response: is this an incident, how bad, who must act now. "
            "Severity assignment is its sharpest instrument. The industry "
            "standard scale runs SEV1 (critical: service down or data at "
            "risk, all hands) through SEV2 (major degradation, urgent "
            "response), SEV3 (minor: limited scope, business hours), to "
            "SEV4 (cosmetic or internal, backlog). Good severity rubrics "
            "are concrete: SEV1 means 'users cannot complete core flows' "
            "or 'data loss is possible,' not 'very bad.' Triage weighs "
            "three factors - impact (who is hurt and how badly), scope "
            "(how wide the blast radius), and urgency (is it getting "
            "worse) - and the commander makes the call in minutes, with "
            "permission to be wrong and re-grade as evidence arrives. "
            "Under-triage kills: a SEV1 treated as a SEV3 gets no "
            "commander, no cadence, no urgency, and the minutes bleed. "
            "Over-triage taxes: everything declared SEV1 burns out the "
            "responders and trains the organization to ignore the top "
            "grade. The discipline is to triage fast, write down the "
            "reasoning, and re-triage on a timer as the picture sharpens."
        ),
        "how_it_works": (
            "Triage works as a decision procedure run under time "
            "pressure. The inputs arrive together: the alert or report, "
            "the dashboard showing the symptom's shape, and the blast "
            "radius estimate. The triager - usually the on-call, with the "
            "IC confirming for anything large - scores impact, scope, and "
            "urgency against the rubric and picks the severity. The "
            "rubric is a table, not a vibe: rows for user impact, data "
            "risk, revenue exposure, and columns for the four severities "
            "with concrete thresholds. Once graded, the severity drives "
            "the machinery automatically: SEV1 opens the bridge and pages "
            "the executives' channel, SEV2 opens the incident channel with "
            "the on-call team, SEV3 becomes a tracked ticket with an "
            "owner and a deadline. Re-triage is scheduled - every 30 "
            "minutes for a SEV1, every few hours for a SEV2 - because "
            "incidents evolve and the grade must follow the facts. Every "
            "grade change is logged with its reason, so the postmortem "
            "can ask whether the triage was right and the rubric can be "
            "sharpened."
        ),
        "key_points": [
            "Triage sorts detected problems into responses; severity assignment is its sharpest instrument.",
            "The standard scale: SEV1 critical, SEV2 major, SEV3 minor, SEV4 cosmetic - each with concrete criteria, not vibes.",
            "Grade on impact, scope, and urgency; decide in minutes with permission to be wrong and re-grade.",
            "Under-triage kills through neglect; over-triage kills through exhaustion - both are failure modes.",
            "Re-triage on a timer as evidence arrives, and log every grade change with its reason.",
        ],
        "requirements": [
            "A written severity rubric with concrete thresholds per level: user impact, data risk, revenue exposure.",
            "A triage decision procedure the on-call can run in minutes, with IC confirmation for large incidents.",
            "Automatic response machinery per severity: channels, pages, bridges, executive notification.",
            "Scheduled re-triage intervals per severity while the incident is open.",
            "A log of every severity change with its reasoning, reviewed in the postmortem.",
        ],
        "standards": [
            "ITIL 4: prioritization based on impact and urgency.",
            "Google SRE practice: severity levels driving response coordination.",
            "NIST SP 800-61: incident prioritization by functional impact and recoverability.",
        ],
        "citations": [CIT_ITIL, CIT_SRE, CIT_NIST],
        "sig_lens": (
            "The Signature read: triage is the Signature surgeon's first "
            "glance at the wounded - the instant judgment of how deep the "
            "cut runs and how fast the blood flows. Where public "
            "engineering fills a rubric, the Signature Incident Method "
            "trains the eye: grade in minutes, write the reasoning, and "
            "let the grade follow the facts as the wound reveals itself."
        ),
    },
    {
        "key": "mitigation_resolution",
        "name": "Mitigation Before Resolution",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Mitigation stops the bleeding; resolution heals the wound. "
            "They are different jobs on different clocks, and confusing "
            "them is one of the costliest mistakes in incident response. "
            "Mitigation is any action that reduces user harm right now "
            "without necessarily understanding the cause: roll back the "
            "deploy, shift traffic away from the broken region, flip the "
            "feature flag off, restart the wedged service, shed load. "
            "Resolution is fixing the true root cause so the incident "
            "cannot recur: the code fix, the schema migration, the "
            "capacity added, the config corrected. The rule is "
            "mitigation first, because users cannot wait for "
            "understanding - a rollback in five minutes beats a perfect "
            "diagnosis in five hours. Mitigation buys the calm in which "
            "resolution can be done properly: with tests, with review, "
            "with a deploy plan, instead of a panicked hotfix at 4 AM. "
            "The incident is not resolved when the mitigation lands - it "
            "is mitigated. Resolution is declared only when the root "
            "cause is fixed, verified, and monitored for recurrence."
        ),
        "how_it_works": (
            "The practice works as two parallel tracks with a gate "
            "between them. Track one, mitigation, starts immediately: "
            "the IC asks 'what is the safest action that reduces harm in "
            "the next ten minutes,' and the team executes the reversible "
            "moves first - rollback, traffic shift, flag flip, restart. "
            "Each mitigation is an experiment: apply it, watch the error "
            "rate, keep it if the graph moves, revert it if it does not. "
            "Track two, investigation, digs for the root cause without "
            "the pressure of the bleeding, because the bleeding is being "
            "handled. The gate between the tracks is the commander's "
            "decision: mitigation attempts must be safe and reversible, "
            "and risky fixes wait for understanding. When the root cause "
            "is confirmed, resolution work begins - the real fix, built "
            "with the normal engineering rigor, tested, reviewed, "
            "deployed through the normal pipeline. Verification closes "
            "the loop: the monitors that caught the incident must show "
            "green, and a watch period confirms no recurrence. Only then "
            "does the IC declare resolution."
        ),
        "key_points": [
            "Mitigation reduces user harm now without requiring understanding; resolution fixes the root cause so it cannot recur.",
            "Mitigation first: a rollback in five minutes beats a perfect diagnosis in five hours.",
            "Mitigations are experiments - apply, watch the error rate, keep or revert on the evidence.",
            "The commander gates the tracks: mitigation attempts must be safe and reversible; risky fixes wait for understanding.",
            "Mitigated is not resolved: resolution requires the true fix, verification, and a watch period.",
        ],
        "requirements": [
            "Reversible mitigation paths for every service: rollback, traffic shift, feature flags, restarts.",
            "An explicit mitigation-first policy, stated in the incident runbook.",
            "Parallel investigation and mitigation tracks with the IC gating risky actions.",
            "A verification checklist and watch period before resolution is declared.",
            "MTTM (mean time to mitigate) tracked separately from MTTR.",
        ],
        "standards": [
            "NIST SP 800-61: containment before eradication - the same mitigation-then-resolution shape.",
            "Google SRE practice: mitigate first, then fix the root cause with normal engineering rigor.",
            "ITIL 4: incident resolution versus problem resolution as distinct activities.",
        ],
        "citations": [CIT_NIST, CIT_SRE, CIT_ITIL],
        "sig_lens": (
            "The Signature read: mitigation is the tourniquet, resolution "
            "the surgery. Where public engineering separates the tracks, "
            "the Signature Incident Method honors the order: stop the "
            "bleeding before studying the wound, because the body's "
            "people cannot wait for the surgeon's understanding - and "
            "only a calm field allows a true healing."
        ),
    },
    {
        "key": "restoration_rollback",
        "name": "Restoration and Rollback Plans",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Restoration is the return to verified health, and the "
            "rollback plan is the fastest road there. Every deploy should "
            "ship with its own undo: the previous version ready to run, "
            "the database migration reversible or backward-compatible, "
            "the feature flag able to turn the new behavior off without "
            "a redeploy. The industry learned this the hard way - a "
            "large share of incidents are caused by changes, and the "
            "teams that recover fastest are the teams that can reverse "
            "a change in minutes. A real rollback plan names the "
            "mechanism (redeploy previous artifact, flip flag, restore "
            "snapshot), the decision-maker (who may order it, at 3 AM, "
            "without a meeting), the verification (which monitors prove "
            "health after), and the limits (what cannot be rolled back - "
            "a destructive schema migration, a published API contract). "
            "Restoration also covers the paths when rollback is "
            "impossible: rolling forward with a fix, failing over to "
            "another region, restoring from backup. The plan is written "
            "before the change ships and tested in game days, because a "
            "rollback procedure discovered during an outage is a second "
            "outage waiting to happen."
        ),
        "how_it_works": (
            "The rollback plan works as a pre-committed decision. Before "
            "the change ships, the team writes down the undo: which "
            "artifact to redeploy, which flag to flip, which snapshot to "
            "restore, and the exact commands or buttons. The decision "
            "authority is named in advance - the on-call or the IC may "
            "order the rollback on evidence, no meeting required - "
            "because the cost of waiting for permission is measured in "
            "user-minutes. During the incident, the rollback is executed "
            "as a drill: run the documented steps, watch the health "
            "signals, and verify with the same monitors that detected "
            "the failure. If the rollback does not move the graph, it "
            "is itself evidence - the cause is elsewhere - and the team "
            "moves to the next mitigation. Database changes get special "
            "treatment: migrations ship backward-compatible (expand then "
            "contract), so the old code runs against the new schema, "
            "which is what makes the code rollback safe. After "
            "restoration, the rollback itself is reviewed: did it work "
            "as documented, how long did it take, what was missing."
        ),
        "key_points": [
            "Every deploy ships with its undo: previous artifact, reversible migration, kill-switch flag.",
            "The rollback decision authority is named in advance - no meetings at 3 AM.",
            "Rollback is a drill: documented steps, health signals watched, verified by the detecting monitors.",
            "A rollback that does not move the graph is evidence: the cause is elsewhere.",
            "Database migrations ship backward-compatible (expand then contract) so code rollback stays safe.",
        ],
        "requirements": [
            "A written rollback procedure per service: mechanism, commands, decision-maker, verification signals.",
            "Backward-compatible database migrations as the default; destructive migrations flagged as non-rollbackable.",
            "Feature flags on risky changes so behavior can be disabled without a redeploy.",
            "Rollback drills in game days, timed and reviewed.",
            "A post-restoration review of the rollback itself: duration, gaps, documentation fixes.",
        ],
        "standards": [
            "Google SRE Book: safe rollout and rollback as core release engineering practice.",
            "DORA/Accelerate: deployment reversibility as a capability of elite performers.",
            "NIST SP 800-61: recovery procedures documented and tested in the incident response plan.",
        ],
        "citations": [CIT_SRE, CIT_ACCELERATE, CIT_NIST],
        "sig_lens": (
            "The Signature read: the rollback plan is the Signature "
            "body's memory of health - the exact path back to the last "
            "whole state. Where public engineering documents procedures, "
            "the Signature Incident Method keeps the way home: every "
            "step forward mapped with its step back, so no advance is "
            "ever a trap."
        ),
    },
    {
        "key": "five_whys",
        "name": "The Five Whys",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The Five Whys is the simplest root-cause technique in "
            "existence: ask 'why' five times. Developed in the Toyota "
            "Production System under Taiichi Ohno, it drills past the "
            "symptom to the systemic cause by refusing to stop at the "
            "first answer. The site went down - why. The deploy script "
            "failed - why. It was never tested on the new OS - why. "
            "There is no deploy test in the pipeline - why. Nobody owned "
            "adding one - and there is the root cause, four layers below "
            "the outage. The power is in the discipline: each answer must "
            "be a fact, not a guess, and each 'why' must follow from the "
            "previous answer, not jump to a favorite theory. The technique "
            "has a known failure mode: asked carelessly, it becomes a "
            "blame chain ending at a human - 'why did the engineer push "
            "the bad config' - which is why the Five Whys must be run "
            "blamelessly, with every answer pointing at the system that "
            "allowed the action, not the person who took it. Done right, "
            "five honest whys turn an outage into an organizational "
            "improvement with a name on it."
        ),
        "how_it_works": (
            "The Five Whys works as a facilitated chain. After the "
            "timeline is frozen, the postmortem facilitator states the "
            "problem in one sentence - 'checkout was down for 47 minutes' "
            "- and asks why. The team answers with a verified fact from "
            "the timeline, the facilitator writes it down, and asks why "
            "again. The chain continues, each link a fact that explains "
            "the previous link, until the answers stop changing the "
            "remedy - usually around five, sometimes three, sometimes "
            "seven. The facilitator guards two rules: no skipping links "
            "(every why must follow from the last answer) and no human "
            "as the final answer (if the chain ends at a person, ask why "
            "the system let the person do it). The final link is the "
            "root cause candidate, and it must be actionable: 'nobody "
            "owned deploy testing' becomes the action item 'assign a "
            "deploy-test owner and add the pipeline stage.' The chain is "
            "published in the postmortem so anyone can check the links, "
            "because a Five Whys that cannot be audited is just a story."
        ),
        "key_points": [
            "Ask 'why' repeatedly - usually five - drilling from symptom to systemic cause; from the Toyota Production System via Taiichi Ohno.",
            "Each answer must be a verified fact from the timeline, and each why must follow from the previous answer.",
            "Run it blamelessly: if the chain ends at a person, ask why the system allowed the action.",
            "Stop when the answers stop changing the remedy; the final link must be actionable.",
            "Publish the chain in the postmortem so the links can be audited.",
        ],
        "requirements": [
            "A frozen timeline to source every answer as fact, not memory.",
            "A facilitator who guards the no-skipping and no-blame rules.",
            "The problem stated in one sentence before the first why.",
            "A root cause that names a system gap with an owner, not a human with a fault.",
            "The full chain published in the postmortem with its action item attached.",
        ],
        "standards": [
            "Toyota Production System practice (Ohno): the Five Whys as root-cause technique.",
            "Blameless analysis per Allspaw: system-focused, not person-focused.",
            "Postmortem root-cause sections per Google SRE practice.",
        ],
        "citations": [CIT_ALLSPAW, CIT_SRE],
        "sig_lens": (
            "The Signature read: the Five Whys are the Signature "
            "surgeon's probe - five careful questions that trace the "
            "wound to the weakness that let it happen. Where public "
            "engineering facilitates a chain, the Signature Incident "
            "Method digs with honor: never stopping at the symptom, "
            "never ending at a person, always ending at the system that "
            "must be made stronger."
        ),
    },
    {
        "key": "fishbone_faulttree",
        "name": "Fishbone Diagrams and Fault Trees",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "When the Five Whys give you a chain, fishbone diagrams and "
            "fault trees give you the whole skeleton. The fishbone - the "
            "Ishikawa diagram - lays the incident's effect at the head "
            "and arrays candidate causes along the bones, grouped by "
            "category: people, process, tools, environment, materials, "
            "measurement. It is a brainstorming structure that forces "
            "breadth: the team must fill every bone before arguing about "
            "any of them, which stops the loudest theory from winning by "
            "default. The fault tree is its quantitative sibling: a "
            "top-down logic diagram where the undesired event sits at the "
            "top and branches down through AND and OR gates to basic "
            "causes. An OR gate means any single cause triggers the "
            "event - the probabilities add - while an AND gate means all "
            "causes must coincide, so the probabilities multiply and the "
            "joint event is rarer. Fault trees turn 'what could cause "
            "this' into arithmetic: if three independent components each "
            "fail with probability 0.01 and any one fails the system, "
            "the system fails with probability about 0.03. The two tools "
            "serve different moments: the fishbone organizes the "
            "postmortem's search, the fault tree hardens the design "
            "before the incident."
        ),
        "how_it_works": (
            "The fishbone works in a facilitated session. The effect - "
            "'checkout down 47 minutes' - is written at the head. The "
            "team fills the bones by category, one fact or hypothesis per "
            "rib, with no debate allowed during filling; the rule is "
            "quantity first. Then the team prunes: each rib is checked "
            "against the timeline and telemetry, survivors become "
            "candidate causes, and the strongest candidates get owners "
            "and action items. The fault tree works on paper before "
            "systems are built or after they fail: the top event is "
            "defined crisply ('payment authorization unavailable'), the "
            "tree is drawn down through gates to basic events with "
            "estimated probabilities, and the arithmetic shows which "
            "branches dominate the risk. An OR-dominated tree says the "
            "system has single points of failure - fix with redundancy. "
            "An AND-dominated tree says the system needs coincidences to "
            "fail - the design is already resilient, and the incident "
            "probably came from a common cause the tree missed, like a "
            "bad deploy hitting all replicas at once. Both diagrams end "
            "as postmortem exhibits: the reasoning, visible and checkable."
        ),
        "key_points": [
            "The fishbone (Ishikawa) arrays candidate causes by category - people, process, tools, environment - forcing breadth before debate.",
            "The fault tree is top-down logic: the undesired event branches through AND/OR gates to basic causes.",
            "OR gates add probabilities (any cause triggers); AND gates multiply them (all must coincide, so rarer).",
            "OR-dominated trees reveal single points of failure; fix with redundancy.",
            "Both diagrams are postmortem exhibits: the reasoning made visible and checkable.",
        ],
        "requirements": [
            "A facilitated fishbone session per significant postmortem, with fill-before-debate enforced.",
            "Fault trees for critical paths, with basic-event probabilities estimated from history or vendor data.",
            "Pruning of every fishbone rib against the timeline and telemetry.",
            "Common-cause checks on AND-dominated trees: shared deploys, shared configs, shared vendors.",
            "The diagrams published in the postmortem with candidate causes, owners, and actions.",
        ],
        "standards": [
            "Ishikawa cause-and-effect diagramming: standard quality-engineering practice.",
            "Fault tree analysis per IEC 61025 conventions for AND/OR gate logic.",
            "Root-cause analysis as a required postmortem element per SRE practice.",
        ],
        "citations": [CIT_SRE, CIT_SRE_WB],
        "sig_lens": (
            "The Signature read: the fishbone is the full skeleton of the "
            "wound, the fault tree the arithmetic of fate. Where public "
            "engineering draws diagrams, the Signature Incident Method "
            "reads the bones: every rib a possible cause given its "
            "hearing, every gate a judgment of how the fates combine - "
            "and the skeleton, once read, teaches the body where its "
            "armor was thin."
        ),
    },
    {
        "key": "blameless_postmortems",
        "name": "Blameless Postmortems",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A blameless postmortem is an incident review that assumes "
            "everyone did their best with the information they had, and "
            "asks what about the system allowed the failure instead of "
            "who caused it. John Allspaw's 2012 essay 'Blameless "
            "PostMortems and a Just Culture,' written at Etsy, is the "
            "founding document: engineers who fear punishment hide "
            "information, and hidden information is what makes the next "
            "incident worse. The logic is practical, not sentimental. "
            "Complex systems fail through the interaction of many small "
            "conditions - a confusing flag name, a missing alert, a "
            "deploy at the worst moment - and the human at the keyboard "
            "is usually the last link, not the cause. Punish the link "
            "and the conditions stay; fix the conditions and the link "
            "cannot fail the same way again. Blameless does not mean "
            "accountless: action items still have owners and deadlines, "
            "and patterns of negligence are still addressed - but they "
            "are addressed as system problems (training, tooling, "
            "guardrails), not as blame. Organizations that practice this "
            "get something blame cultures never do: honest timelines, "
            "because people tell the truth about what they did when the "
            "truth cannot hurt them."
        ),
        "how_it_works": (
            "A blameless postmortem works through language discipline and "
            "structure. The facilitator - never the participants' manager "
            "- opens by stating the rule: we assume competence and good "
            "intent, and we are here to improve the system. The timeline "
            "is walked fact by fact, and every human action is examined "
            "for the conditions around it: what did the engineer see, "
            "what did the runbook say, what was ambiguous, what would a "
            "reasonable person have done. The write-up uses blameless "
            "language throughout: 'the deploy proceeded without a canary "
            "check' instead of 'Priya skipped the canary check' - the "
            "sentence structure itself refuses to aim at a person. When "
            "a human error is found, the analysis asks why the system "
            "made the error easy: confusing UI, missing confirmation, no "
            "guardrail. The action items that result are systemic - add "
            "the confirmation dialog, require the canary gate in the "
            "pipeline - and each has an owner and a date. The postmortem "
            "is published where the whole organization can read it, "
            "because the lesson belongs to everyone, and the honesty of "
            "the next timeline depends on the safety of this one."
        ),
        "key_points": [
            "Assume competence and good intent: ask what about the system allowed the failure, not who caused it - from Allspaw at Etsy, 2012.",
            "Engineers who fear punishment hide information; hidden information makes the next incident worse.",
            "Blameless is not accountless: action items have owners and deadlines; negligence is addressed as a system problem.",
            "Use blameless language structurally: 'the deploy proceeded without a canary check,' never 'Priya skipped the check.'",
            "Publish the postmortem organization-wide: the lesson belongs to everyone, and the next timeline's honesty depends on this one's safety.",
        ],
        "requirements": [
            "A written blameless policy, stated at the opening of every postmortem.",
            "A facilitator who is not the participants' manager.",
            "Language discipline in the write-up: system-focused sentences, no person as the cause.",
            "Human-error findings converted to system action items: guardrails, confirmations, automation.",
            "Organization-wide publication of postmortems.",
        ],
        "standards": [
            "Allspaw: Blameless PostMortems and a Just Culture (Etsy, 2012).",
            "Google SRE Book: blameless postmortem culture as a core SRE tenet.",
            "Just culture principles: honest reporting protected, systemic fixes preferred.",
        ],
        "citations": [CIT_ALLSPAW, CIT_SRE],
        "sig_lens": (
            "The Signature read: the blameless postmortem is the "
            "Signature body's oath of honesty - the testimony given "
            "freely because testimony can never be punished. Where "
            "public engineering writes blamelessly, the Signature "
            "Incident Method swears it: the wound is examined, never "
            "the warrior, and the body's strength grows from truth "
            "told without fear."
        ),
    },
    {
        "key": "postmortem_template",
        "name": "The Postmortem Template",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The postmortem template is the canonical shape of an "
            "incident's written record: the same sections every time, so "
            "every incident is reviewed with the same rigor and every "
            "postmortem is comparable to the last. The industry-converged "
            "sections, from Google's SRE practice, are: summary (what "
            "happened in a paragraph), impact (who was affected, for how "
            "long, quantified), timeline (the frozen fault timeline, "
            "facts first), root cause (the Five Whys chain or the fault "
            "analysis, ending at a system cause), what went well (the "
            "practices that worked - detection, mitigation, comms - so "
            "they are protected), what went poorly (the gaps, stated "
            "blamelessly), and action items (each with an owner and a due "
            "date). The template's power is comparability: with the same "
            "sections every time, the review board can trend which "
            "sections keep producing action items, which root causes "
            "recur, and whether 'what went well' is growing quarter over "
            "quarter. A postmortem without the template is an essay; "
            "with it, it is data."
        ),
        "how_it_works": (
            "The template works as a fill-in discipline with a "
            "facilitator and a deadline. Within days of the incident - "
            "while memories are fresh but the adrenaline is gone - the "
            "owner drafts each section from the frozen timeline: the "
            "summary in plain language, the impact in numbers, the "
            "timeline as the timestamped facts, the root cause as the "
            "auditable chain. 'What went well' is written deliberately, "
            "because organizations that only document failure slowly "
            "stop noticing what saves them. 'What went poorly' is "
            "written blamelessly, each item pointing at a system gap. "
            "Action items are the template's teeth: each names a single "
            "owner, a due date, and the verification - how will we know "
            "it worked. The draft is reviewed in a postmortem meeting "
            "with the responders and stakeholders, corrected, and then "
            "published to the organization. The review board tracks the "
            "template's output: action items per postmortem, closure "
            "rate, and recurrence of root-cause classes - because the "
            "template exists to make the organization measurably better, "
            "not to file paperwork."
        ),
        "key_points": [
            "The canonical sections: summary, impact, timeline, root cause, what went well, what went poorly, action items.",
            "Same sections every time makes postmortems comparable: trends in causes, actions, and closure rates become visible.",
            "'What went well' is written deliberately, so the practices that save the team are protected, not just the gaps fixed.",
            "Action items are the template's teeth: single owner, due date, and verification of effectiveness.",
            "Drafted within days from the frozen timeline, reviewed in a meeting, published organization-wide.",
        ],
        "requirements": [
            "A fixed postmortem template with the seven canonical sections, used for every qualifying incident.",
            "A named owner and a drafting deadline within days of resolution.",
            "Quantified impact and a frozen timeline as mandatory inputs.",
            "Action items with owner, due date, and verification criteria.",
            "Publication to the organization and tracking by the review board.",
        ],
        "standards": [
            "Google SRE Book and Workbook: postmortem structure and blameless culture.",
            "NIST SP 800-61: post-incident activity and lessons-learned documentation.",
            "ITIL 4: problem investigation records feeding known-error documentation.",
        ],
        "citations": [CIT_SRE, CIT_SRE_WB, CIT_NIST],
        "sig_lens": (
            "The Signature read: the postmortem template is the "
            "Signature body's war chronicle - every battle recorded in "
            "the same honored form so the generals of the future can "
            "study every campaign. Where public engineering fills "
            "sections, the Signature Incident Method keeps the chronicle: "
            "the summary the battle's name, the timeline its hour-by-hour "
            "truth, the action items its sworn reforms."
        ),
    },
    {
        "key": "action_items",
        "name": "Tracking Remediation Action Items",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Action items are where postmortems either change the "
            "organization or die. Every other part of incident response "
            "is about the past; action items are about the future - the "
            "specific changes that make the failure class impossible, "
            "unlikely, or less harmful. A real action item has four "
            "properties: it names a single owner (not a team, a human), "
            "it has a due date, it describes a verifiable outcome ('the "
            "pipeline rejects deploys without a canary stage' - testable), "
            "and it targets the system, not the person. Tracking is the "
            "discipline: every action item lives in the same tracker, "
            "aging is visible, overdue items escalate, and closure "
            "requires evidence - the fix deployed, the test passing, the "
            "runbook updated - not a checkbox clicked. The metrics that "
            "matter: action items per postmortem (too few means shallow "
            "analysis), closure rate (the honesty metric of the whole "
            "program), mean days to close, and recurrence - whether the "
            "same root-cause class appears again after its actions "
            "closed. A postmortem whose actions all close is an "
            "organization learning; a tracker full of year-old items is "
            "an organization performing learning."
        ),
        "how_it_works": (
            "Action tracking works as a pipeline with teeth. Items are "
            "born in the postmortem review meeting, where each is "
            "challenged: is it systemic, is it verifiable, who owns it, "
            "when is it due. They enter the tracker with those four "
            "fields plus a link to the postmortem, and the review board "
            "watches the aging: items approaching due get reminders, "
            "overdue items escalate to the owner's manager, and chronic "
            "overdue becomes a board-level discussion - because an "
            "organization that tolerates overdue safety work has decided "
            "safety is optional. Closure is a ceremony with evidence: "
            "the owner demonstrates the outcome - the pipeline gate "
            "working, the alert firing in a drill, the runbook updated - "
            "and a reviewer confirms it. Then comes the effectiveness "
            "check, months later: did the failure class recur. If it "
            "did, the action is reopened and the analysis was wrong, "
            "which is itself a lesson. The loop closes when the "
            "quarterly review shows closure rates high, aging low, and "
            "recurrence falling - the measurable signature of an "
            "organization that learns."
        ),
        "key_points": [
            "A real action item: single human owner, due date, verifiable outcome, systemic target.",
            "Closure requires evidence - the fix deployed and demonstrated - not a checked box.",
            "Aging is visible and overdue escalates: tolerated overdue safety work means safety is optional.",
            "The metrics: items per postmortem, closure rate, mean days to close, and recurrence of the failure class.",
            "Effectiveness is checked months later: if the class recurs, the analysis was wrong and the item reopens.",
        ],
        "requirements": [
            "A single tracker for all postmortem action items with owner, due date, outcome, and postmortem link.",
            "Challenge of every item at birth: systemic, verifiable, owned, dated.",
            "Escalation rules for aging and overdue items, up to board level.",
            "Evidence-based closure with independent confirmation.",
            "Quarterly effectiveness review: closure rate, aging, recurrence.",
        ],
        "standards": [
            "Google SRE Workbook: postmortem action items with owners and follow-through.",
            "NIST SP 800-61: post-incident activity must produce implemented improvements.",
            "ITIL 4 problem management: known errors and workaround/fix tracking to closure.",
        ],
        "citations": [CIT_SRE_WB, CIT_NIST, CIT_ITIL],
        "sig_lens": (
            "The Signature read: action items are the Signature body's "
            "sworn reforms - the vows the body takes after every wound, "
            "tracked until they are kept. Where public engineering tracks "
            "tickets, the Signature Incident Method keeps the oath-book: "
            "every vow named, dated, and witnessed, and no vow is "
            "considered kept until the body proves it in battle."
        ),
    },
    {
        "key": "status_page",
        "name": "Status Page Operations",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The status page is the organization's public truth during an "
            "incident: the one place users, customers, and executives "
            "check instead of flooding support. Atlassian's Statuspage "
            "product defined the modern pattern, and the operating "
            "discipline around it is what this record covers. A status "
            "page lists the service's components - API, website, mobile, "
            "per region - each with a state: operational, degraded "
            "performance, partial outage, major outage, under maintenance. "
            "During an incident the page moves through states in order: "
            "investigating (we know something is wrong), identified (we "
            "know what), monitoring (we believe it is fixed, we are "
            "watching), resolved. Each state change carries a timestamped "
            "message in plain language, on the communication cadence - "
            "the page is the external half of incident communication "
            "discipline. The page must live on separate infrastructure "
            "from the services it reports on; a status page hosted on the "
            "same cloud that is down is a dark joke. History matters too: "
            "the page keeps a permanent incident history, which becomes "
            "the organization's public reliability record - and a "
            "powerful incentive to keep the red days rare."
        ),
        "how_it_works": (
            "Status page operations work as a parallel track owned by the "
            "communications lead. At declaration, the IC confirms the "
            "public state and the comms lead posts the first update: "
            "which components are affected, what users experience, what "
            "is being done, when the next update lands. Templates keep "
            "the language consistent and fast - the team is not composing "
            "prose during a SEV1. As the incident evolves, the component "
            "states move through investigating, identified, monitoring, "
            "resolved, each transition timestamped and messaged. "
            "Subscribers - users who registered for notifications - get "
            "pushed updates by email, SMS, or webhook on the same "
            "cadence. The discipline's hard rules: update on the timer "
            "even with no news, never speculate about cause in public, "
            "never mark resolved until verification is complete, and "
            "post the postmortem summary to the history when it is "
            "published. Between incidents, the page is maintained: "
            "component lists match the real architecture, on-call "
            "rotation includes page-duty for the page itself, and the "
            "separate hosting is tested - because the page is most "
            "needed exactly when everything else is broken."
        ),
        "key_points": [
            "The status page is the public truth: components with states, timestamped plain-language updates, on the comms cadence.",
            "States move in order: investigating, identified, monitoring, resolved - each transition messaged.",
            "Templates keep incident language consistent and fast; no composing prose during a SEV1.",
            "The page must live on infrastructure independent of the services it reports on.",
            "The permanent incident history is the organization's public reliability record - an incentive to keep red days rare.",
        ],
        "requirements": [
            "A status page with component-level states matching the real architecture.",
            "Pre-written templates for acknowledge, update, and resolve in plain language.",
            "Subscriber notifications (email, SMS, webhook) wired to state changes.",
            "Independent hosting, tested, with page-duty in the on-call rotation.",
            "Postmortem summaries published to the incident history.",
        ],
        "standards": [
            "Atlassian Statuspage operating pattern: component states and incident state machine.",
            "Atlassian Incident Communication Handbook: public update discipline.",
            "NIST SP 800-61: external communications as part of incident response.",
        ],
        "citations": [CIT_ATLASSIAN, CIT_NIST],
        "sig_lens": (
            "The Signature read: the status page is the Signature body's "
            "banner on the city walls - the honest signal to the people "
            "outside, raised on its own pole so it flies even when the "
            "city burns. Where public engineering posts updates, the "
            "Signature Incident Method flies the banner: green in peace, "
            "red in battle, and always true, because the people's trust "
            "is the city's wall."
        ),
    },
    {
        "key": "paging_routing",
        "name": "Paging and Alert Routing",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Paging is the act of summoning a human; routing is deciding "
            "which human. Together they are the last mile of detection, "
            "and they fail in predictable ways: the page goes to someone "
            "on vacation, to a team that does not own the service, to "
            "everyone at once (so nobody feels responsible), or to a "
            "phone that has been silenced by alert fatigue. Good routing "
            "is a rule system, not a phone tree. Alerts carry routing "
            "labels - service, severity, component - and the rules map "
            "them to the owning team's on-call, with urgency deciding "
            "the channel: page for SEV1/SEV2, ticket for SEV3, backlog "
            "for SEV4. Escalation policies sit behind the rules: if the "
            "primary does not acknowledge in five minutes, the secondary "
            "is paged automatically; the chain climbs until a human "
            "answers. Routing rules are living configuration: every "
            "misrouted page is a bug in the rules, reviewed in the "
            "alert tuning loop, because a page that reaches the wrong "
            "engineer is detection time thrown away."
        ),
        "how_it_works": (
            "Routing works as a decision tree evaluated in seconds. The "
            "alert arrives with its labels; the rule engine matches "
            "service to team, severity to urgency, and component to the "
            "specialist rotation if one exists. The page goes out through "
            "the channel the urgency demands - push notification plus "
            "phone call for SEV1, push only for SEV2 - carrying the "
            "runbook link, the dashboard link, and the acknowledge "
            "action. The acknowledgment timer starts: silence past the "
            "threshold triggers the escalation policy automatically, no "
            "human dispatcher needed. If the responder needs another "
            "team, one-button escalation pages that team's on-call with "
            "the incident context attached. Behind it all, the routing "
            "table is versioned and reviewed: on-call schedules are "
            "published, overrides (vacation swaps) are first-class, and "
            "every page is logged with its route so misroutes can be "
            "found and fixed. The system is tested in game days - pages "
            "fired deliberately to verify they reach a human - because "
            "an untested pager is a hope, not a system."
        ),
        "key_points": [
            "Routing is a rule system: alert labels map to owning teams, severity maps to urgency and channel.",
            "Escalation policies climb automatically on acknowledgment timeouts - no human dispatcher needed.",
            "Every misrouted page is a bug in the rules, fixed in the alert tuning loop.",
            "Pages carry runbook, dashboard, and acknowledge action: work starts in seconds.",
            "The routing table is versioned, overrides are first-class, and paging is tested in game days.",
        ],
        "requirements": [
            "Routing rules mapping service, severity, and component to the owning on-call.",
            "Urgency-to-channel mapping: page for SEV1/SEV2, ticket for SEV3, backlog for SEV4.",
            "Automatic escalation policies with acknowledgment timeouts per rung.",
            "One-button cross-team escalation with incident context attached.",
            "Routing review in the alert tuning loop, fed by the page log.",
        ],
        "standards": [
            "Google SRE Book: alerting, on-call, and escalation design.",
            "PagerDuty operational practice: escalation policies and schedules.",
            "ITIL 4: incident escalation (hierarchic and functional).",
        ],
        "citations": [CIT_SRE, CIT_PAGERDUTY, CIT_ITIL],
        "sig_lens": (
            "The Signature read: paging is the Signature body's alarm "
            "bell, routing the knowledge of whose post guards which "
            "wall. Where public engineering writes routing rules, the "
            "Signature Incident Method stations the guard: every alarm "
            "knows its soldier, every silence summons the relief, and "
            "no wall ever stands unwatched because the bell rang in the "
            "wrong tower."
        ),
    },
    {
        "key": "incident_bridge",
        "name": "The Incident Bridge and War Room",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The incident bridge - the war room, the call - is the live "
            "coordination space where responders work an incident "
            "together. In the remote era it is usually a video call plus "
            "the incident channel; the discipline is the same as the "
            "physical war rooms it replaced. The bridge has one purpose: "
            "shared situational awareness at the speed of speech. The "
            "IC runs it with a rhythm: round-robin status from each "
            "responder, decisions stated aloud and written to the "
            "channel, and a next check-in time so nobody wonders what to "
            "do. Bridge etiquette is enforced because chaos is the "
            "default: one speaker at a time, no side conversations in "
            "the main channel, new joiners announce themselves and read "
            "the timeline before asking questions, and everything "
            "decided on voice is written down. The bridge scales with "
            "the incident: a SEV3 might be two engineers in a channel, "
            "a SEV1 is the full role structure on a staffed call. And "
            "the bridge has an end: the IC closes it at resolution, "
            "because a bridge that stays open becomes a hangout, and "
            "hangouts do not restore services."
        ),
        "how_it_works": (
            "The bridge works through the IC's cadence. On opening, the "
            "IC states the known facts, the severity, the roles, and the "
            "first check-in time - usually 15 minutes for a SEV1. Each "
            "check-in runs the loop: every responder reports status in "
            "one minute (what I checked, what I found, what I need), the "
            "IC states the next actions and their owners, the scribe "
            "writes it all to the channel. Between check-ins, responders "
            "work in parallel threads and post findings to the channel, "
            "not to voice - voice is for decisions and coordination, "
            "text is for the record. New joiners are onboarded in one "
            "motion: 'read the pinned timeline, you own the database "
            "thread, next check-in at :45.' The IC watches the clock and "
            "the energy: responders rotate off for rest on long "
            "incidents, because exhausted engineers make the incident "
            "longer. At resolution the IC runs the closing loop - "
            "verification confirmed, timeline frozen, postmortem owner "
            "named - and closes the bridge explicitly. The channel "
            "stays as the record; the call ends."
        ),
        "key_points": [
            "The bridge exists for shared situational awareness at the speed of speech: one purpose, run on rhythm.",
            "The IC runs check-in loops: status round-robin, decisions stated aloud and written down, next check-in set.",
            "Bridge etiquette: one speaker, no side chatter in the main channel, newcomers read the timeline first.",
            "Voice is for decisions and coordination; text is for the record - everything decided on voice is written down.",
            "The IC closes the bridge explicitly at resolution and rotates exhausted responders on long incidents.",
        ],
        "requirements": [
            "A standing bridge line and incident channel template, openable in one action at declaration.",
            "IC-run check-in cadence per severity, with the loop: status, decisions, next check-in.",
            "Published bridge etiquette, enforced by the IC from the first minute.",
            "A scribe capturing every voice decision into the channel in real time.",
            "Responder rotation rules for incidents past a defined duration.",
        ],
        "standards": [
            "FEMA ICS: incident command post and communications discipline.",
            "Google SRE practice: coordinated incident response with defined roles.",
            "NIST SP 800-61: incident coordination and communication procedures.",
        ],
        "citations": [CIT_FEMA, CIT_SRE, CIT_NIST],
        "sig_lens": (
            "The Signature read: the bridge is the Signature war council "
            "in session - the generals gathered around the map while the "
            "battle rages. Where public engineering opens a call, the "
            "Signature Incident Method convenes the council: the commander "
            "holds the rhythm, every voice reports, every decision is "
            "written into the chronicle, and the council disbands only "
            "when the field is won."
        ),
    },
    {
        "key": "sre_error_budgets",
        "name": "Site Reliability Engineering and Error Budgets",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Site Reliability Engineering, as Google defined it in the "
            "2016 SRE Book, is what happens when you ask software "
            "engineers to design an operations function: reliability "
            "treated as a feature, toil automated away, and risk managed "
            "with mathematics instead of fear. The error budget is the "
            "mathematics. An SLO of 99.9 percent over 30 days leaves a "
            "0.1 percent budget of allowable failure - the team may "
            "'spend' it on velocity: deploys, experiments, risky "
            "migrations. Spend within the budget and the business gets "
            "both speed and reliability; exhaust it and the policy "
            "freezes launches until reliability recovers. The burn rate "
            "is the speedometer: how fast budget is being consumed "
            "relative to the window. A fast burn - the whole monthly "
            "budget gone in two days - pages someone immediately; a "
            "slow burn informs planning. The deeper SRE ideas travel "
            "with the budget: toil (manual repetitive operational work) "
            "is capped, usually at 50 percent of an SRE's time, because "
            "toil scales linearly with the service and engineering does "
            "not; automation is the only way out. And the SRE Book's "
            "central bargain: 100 percent reliability is the wrong "
            "target for almost every product - users cannot tell the "
            "difference, and the engineering cost is infinite. The "
            "budget makes that bargain explicit and enforceable."
        ),
        "how_it_works": (
            "SRE works as a control loop around the budget. The SLO is "
            "set from the business need - 99.9 for the checkout API, 99 "
            "for the internal dashboard - and the budget is computed: "
            "(1 - SLO) times the window's request volume. Monitoring "
            "tracks consumption continuously with burn-rate alerts: a "
            "multiwindow setup pages on fast burns (high burn over one "
            "hour and six hours) and tickets on slow burns (moderate "
            "burn over days). The team watches the budget like a bank "
            "balance: plenty remaining means ship fast; running low "
            "means extra canaries, extra review, smaller batches; "
            "exhausted means the freeze policy engages - feature work "
            "stops, only reliability work ships, and launches resume "
            "when the burn rate has recovered for a defined period. In "
            "parallel, toil is measured and capped: every manual task "
            "is logged, toil above the cap triggers automation work, "
            "and the automation permanently removes the toil. The loop "
            "closes quarterly: SLOs are revisited against business "
            "reality, budgets recomputed, and the reliability report "
            "shows whether the bargain held."
        ),
        "key_points": [
            "SRE treats reliability as a feature and manages risk with mathematics: the error budget makes the reliability-velocity bargain explicit.",
            "Burn rate is the speedometer: fast burns page now, slow burns inform planning, exhaustion freezes launches.",
            "100 percent reliability is the wrong target for almost every product; the budget prices the nines honestly.",
            "Toil - manual repetitive operations work - is measured and capped (classically 50 percent), because toil scales linearly and engineering does not.",
            "The loop closes quarterly: SLOs revisited, budgets recomputed, the reliability report judging the bargain.",
        ],
        "requirements": [
            "SLOs set from business need per critical service, with the error budget computed and visible.",
            "Multiwindow burn-rate alerting: fast-burn pages, slow-burn tickets.",
            "A written budget-exhaustion policy: what freezes, who decides, what reopens launches.",
            "Toil measurement with a cap and automation as the relief valve.",
            "Quarterly SLO and budget review against business reality.",
        ],
        "standards": [
            "Google SRE Book (2016): SLOs, error budgets, and the reliability bargain.",
            "Google SRE Workbook: implementing burn-rate alerting (multiwindow, multi-burn-rate).",
            "DORA/Accelerate: reliability outcomes of high-performing teams.",
        ],
        "citations": [CIT_SRE, CIT_SRE_WB, CIT_ACCELERATE],
        "sig_lens": (
            "The Signature read: SRE is the Signature body's covenant "
            "with risk - the mathematics of how bold the body may be. "
            "Where public engineering budgets errors, the Signature "
            "Incident Method signs the covenant in full: the budget is "
            "honor made countable, the freeze its enforcement, and the "
            "bargain its wisdom - that perfection is the enemy of the "
            "good the people actually need."
        ),
    },
    {
        "key": "chaos_engineering",
        "name": "Chaos Engineering",
        "group": "Advanced",
        "ladder_rank": 7,
        "ladder_tier": "advanced",
        "description": (
            "Chaos engineering is the discipline of breaking systems on "
            "purpose, in controlled experiments, to prove they survive "
            "the breaks they will meet by accident. Netflix pioneered it "
            "with Chaos Monkey in 2011 - a program that randomly "
            "terminated production instances - on the theory that the "
            "only way to be sure the system tolerates failure is to "
            "fail it continuously. The Principles of Chaos Engineering "
            "formalized the method: start by defining steady state - "
            "the measurable normal behavior, like 'checkout succeeds 99.9 "
            "percent of the time'; form a hypothesis - 'killing one "
            "availability zone will not move the steady state'; run the "
            "experiment on production-like or production systems with a "
            "limited blast radius; and measure whether the steady state "
            "held. The blast radius is the ethics of the discipline: "
            "experiments start tiny (one instance, one zone, off-peak), "
            "carry an automatic abort when the steady state moves too "
            "far, and expand only with evidence. Chaos engineering "
            "finds the failures that only appear at scale and under "
            "real conditions - the retry storm, the cascading timeout, "
            "the failover that never actually failed over - and it finds "
            "them on a Tuesday morning instead of during the holiday "
            "peak."
        ),
        "how_it_works": (
            "A chaos experiment works as a controlled hypothesis test. "
            "First the steady state is defined with metrics that matter "
            "to users: success rate, latency percentiles, error budget "
            "burn. Then the hypothesis is written - 'if we terminate 10 "
            "percent of instances in one zone, the steady state will not "
            "move beyond the tolerance' - with the tolerance stated as a "
            "number. Guardrails go in before the fault: the blast radius "
            "(which instances, which zone, what time window), the abort "
            "conditions (steady state moves past tolerance, or a real "
            "incident starts), and the automatic halt that enforces "
            "them. The fault is injected - instance termination, latency "
            "injection, network partition, DNS failure, clock skew - and "
            "the steady state is watched in real time. If the hypothesis "
            "holds, the system's resilience is proven for that fault; if "
            "it breaks, the team has found a real weakness with a full "
            "observability record of how it broke, which becomes a "
            "postmortem-style action item. Experiments graduate: from "
            "dev to staging to production, from tiny blast radius to "
            "larger, each step gated on the previous step's evidence."
        ),
        "key_points": [
            "Define steady state in user-facing metrics, hypothesize that a fault will not move it, inject the fault, measure - from the Principles of Chaos Engineering.",
            "Netflix's Chaos Monkey (2011) proved the premise: continuous controlled failure builds real tolerance.",
            "Blast radius is the ethics: start tiny, abort automatically when tolerance is exceeded, expand only with evidence.",
            "Chaos finds scale-only failures - retry storms, cascading timeouts, untested failovers - on a Tuesday morning, not during the peak.",
            "Failed hypotheses become action items with full observability records of how the system broke.",
        ],
        "requirements": [
            "Steady-state definitions in user-facing metrics for the systems under experiment.",
            "Written hypotheses with numeric tolerances before any fault is injected.",
            "Guardrails on every experiment: blast radius, abort conditions, automatic halt.",
            "Graduation path: dev to staging to production, tiny to larger, each step gated on evidence.",
            "Experiment results recorded like postmortems, with action items for every broken hypothesis.",
        ],
        "standards": [
            "Principles of Chaos Engineering (principlesofchaos.org): steady state, hypothesis, blast radius, automation.",
            "Basiri et al., Chaos Engineering, IEEE Software (2016).",
            "Google SRE Workbook: disaster and failure testing practice.",
        ],
        "citations": [CIT_CHAOS, CIT_SRE_WB],
        "sig_lens": (
            "The Signature read: chaos engineering is the Signature "
            "body's sparring - the controlled wounds that teach the "
            "body to fight. Where public engineering injects faults, "
            "the Signature Incident Method spars with honor: the "
            "hypothesis the vow, the blast radius the padded blade, "
            "and every lost sparring bout a lesson the real battle "
            "will never have to teach."
        ),
    },
    {
        "key": "observability",
        "name": "Observability in Incident Response",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Observability is the ability to ask arbitrary questions "
            "about a system's internals without shipping new code - the "
            "difference between having the answers instrumented in "
            "advance and discovering mid-incident that the one metric "
            "you need does not exist. It rests on three pillars. "
            "Metrics: numbers over time - request rates, error rates, "
            "latencies - cheap to store, fast to query, the first thing "
            "the responder looks at. Logs: discrete event records with "
            "context - the request that failed, with its ID, its user, "
            "its parameters - the detail that explains the metric's "
            "shape. Traces: the journey of a single request across "
            "services, showing where the milliseconds went - the map "
            "that turns 'the API is slow' into 'the inventory lookup "
            "takes 800 milliseconds.' OpenTelemetry, the Cloud Native "
            "Computing Foundation project, is the industry's converged "
            "instrumentation standard across all three. In incident "
            "response, observability is what makes the timeline honest: "
            "the true failure start comes from metrics, the mechanism "
            "from logs, the culprit service from traces. Teams that "
            "invest in it triage in minutes; teams that do not triage "
            "in hours, by guessing."
        ),
        "how_it_works": (
            "Observability works as an instrumentation-to-investigation "
            "pipeline. Services emit telemetry through standard "
            "libraries - OpenTelemetry SDKs - producing metrics on a "
            "scrape or push interval, structured logs with correlation "
            "IDs, and traces sampled at a configured rate. The "
            "collection layer aggregates it into queryable stores: a "
            "time-series database for metrics, a log index for events, "
            "a trace store for journeys. During an incident the "
            "responder works top-down: the dashboard shows which "
            "symptom moved and when (metrics give the true start time), "
            "the trace view shows which service in the call graph "
            "introduced the latency or errors, and the logs for the "
            "failing request IDs show the mechanism - the exception, "
            "the timeout, the bad value. Sampling keeps the volume "
            "affordable: head-based sampling keeps a fixed fraction of "
            "traces, tail-based sampling keeps the interesting ones "
            "(errors, slow requests) at higher rates. After the "
            "incident, the investigation's questions become permanent "
            "dashboards and alerts - the observability gap that the "
            "incident exposed is closed as an action item."
        ),
        "key_points": [
            "Observability is asking arbitrary questions about internals without shipping new code.",
            "Three pillars: metrics (numbers over time, the first look), logs (event detail, the explanation), traces (request journeys, the map).",
            "OpenTelemetry (CNCF) is the converged instrumentation standard across all three.",
            "Incident investigation runs top-down: metrics for when, traces for where, logs for how.",
            "Sampling (head and tail-based) keeps telemetry affordable; every incident's unanswered question becomes a permanent dashboard.",
        ],
        "requirements": [
            "OpenTelemetry-standard instrumentation on every service: metrics, structured logs with correlation IDs, traces.",
            "Queryable stores with retention covering at least the incident review window.",
            "A sampling strategy documented and budgeted: head-based baseline plus tail-based capture of errors and slow requests.",
            "Dashboards per service showing the symptom signals the alerts fire on.",
            "Observability gaps found in incidents closed as action items.",
        ],
        "standards": [
            "OpenTelemetry specification (CNCF): traces, metrics, logs instrumentation.",
            "Google SRE Book and Workbook: monitoring, alerting, and debugging practice.",
            "The three-pillar observability model: industry-standard framing.",
        ],
        "citations": [CIT_OTEL, CIT_SRE, CIT_SRE_WB],
        "sig_lens": (
            "The Signature read: observability is the Signature body's "
            "senses - sight, hearing, and memory extended into the "
            "machine. Where public engineering instruments services, "
            "the Signature Incident Method sharpens the senses: metrics "
            "the pulse, logs the memory, traces the map of the nerves - "
            "and a body that feels itself can never be ambushed by its "
            "own wounds."
        ),
    },
    {
        "key": "metrics_dashboards",
        "name": "Incident Metrics Dashboards",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The incident metrics dashboard is the organization's "
            "reliability scoreboard: the numbers that say whether the "
            "whole discipline is working, reviewed on a cadence by the "
            "people who own it. The core panels are the vital signs. "
            "Incident volume: how many incidents per period, by severity "
            "- rising SEV1s mean the system is getting sicker, falling "
            "ones mean the prevention work is landing. MTTR and its "
            "components (MTTD, MTTA, MTTM): the reflex trend, segmented "
            "by severity, mean and median both. MTBF or failure rate: "
            "the bleeding trend. Error budget consumption per service: "
            "who is spending reliability fastest. Postmortem health: "
            "action items opened versus closed, mean days to close, "
            "overdue count. And recurrence: the same failure class "
            "appearing twice is the dashboard's red alarm, because it "
            "means the learning loop broke. Good dashboards are boring: "
            "the same panels every month, the same definitions, so the "
            "trend is honest. They are reviewed in the incident review "
            "board on a fixed cadence, and every red trend gets an "
            "owner and a plan - a dashboard nobody reviews is wallpaper."
        ),
        "how_it_works": (
            "The dashboard works as a measurement pipeline with a "
            "review ritual. Incident records feed it automatically: "
            "declaration and resolution timestamps give MTTR, severity "
            "history gives the volume mix, the timeline gives detection "
            "lag. Error budget burn comes from the SLO monitoring; "
            "action-item aging comes from the tracker. The panels are "
            "computed on a fixed cadence - weekly for operational "
            "panels, monthly for trend panels - with definitions frozen "
            "so month-to-month comparison is valid. The review board "
            "meets on the cadence and walks the dashboard in order: "
            "volume, MTTR, MTBF, budgets, postmortem health, recurrence. "
            "Each panel gets a verdict - improving, stable, degrading - "
            "and degrading panels get what incidents get: an owner, a "
            "hypothesis, and a date to report back. The dashboard also "
            "feeds planning: teams spending error budget fastest get "
            "reliability investment, and the quarterly business review "
            "gets the availability numbers against the SLOs. The loop "
            "is complete when the dashboard's trends move the "
            "organization's priorities - measurement that changes "
            "nothing is ceremony."
        ),
        "key_points": [
            "The dashboard is the reliability scoreboard: volume by severity, MTTR and components, MTBF, budget burn, postmortem health, recurrence.",
            "Recurrence of a failure class is the red alarm: it means the learning loop broke.",
            "Definitions stay frozen so trends are honest; panels are the same every month.",
            "The review board walks the dashboard on cadence: every degrading panel gets an owner, a hypothesis, and a date.",
            "Measurement that changes nothing is ceremony: dashboard trends must move priorities and investment.",
        ],
        "requirements": [
            "Automatic feeds from incident records, SLO monitoring, and the action-item tracker.",
            "Frozen metric definitions with mean and median for time-based measures.",
            "Weekly operational and monthly trend review cadences with the review board.",
            "A verdict per panel (improving, stable, degrading) with owners for degrading trends.",
            "Quarterly reporting of availability against SLOs to business leadership.",
        ],
        "standards": [
            "Google SRE Workbook: service level objectives and error budget reporting.",
            "DORA metrics: MTTR and failure-rate trending per Accelerate.",
            "NIST SP 800-61: incident metrics for program improvement.",
        ],
        "citations": [CIT_SRE_WB, CIT_ACCELERATE, CIT_NIST],
        "sig_lens": (
            "The Signature read: the metrics dashboard is the Signature "
            "body's medical chart - the vital signs read every morning "
            "by the physicians of reliability. Where public engineering "
            "builds panels, the Signature Incident Method keeps the "
            "chart: honest numbers, frozen definitions, and every "
            "worsening line given a healer and a date - because a chart "
            "no one reads is a patient no one treats."
        ),
    },
    {
        "key": "dora_metrics",
        "name": "DORA Metrics and Elite Performer Benchmarks",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The DORA metrics are the four numbers that predict "
            "organizational performance, from the research program "
            "published as Accelerate by Forsgren, Humble, and Kim in "
            "2018. Deployment frequency: how often the organization "
            "ships to production. Lead time for changes: how long from "
            "commit to production. Mean time to restore: how fast "
            "service recovers from failure. Change failure rate: what "
            "fraction of changes cause a failure. The research sorted "
            "teams into elite, high, medium, and low performers, and "
            "the elite thresholds became the industry's scoreboard: "
            "deploys on demand (multiple per day), lead time under one "
            "hour, MTTR under one hour, change failure rate between 0 "
            "and 15 percent. Low performers, by contrast, deploy "
            "between monthly and every six months, take a week to a "
            "month to restore service, and fail 16 to 30 percent of "
            "changes - or worse. The metrics matter for incident "
            "management because two of the four are incident metrics "
            "directly, and the other two drive them: small frequent "
            "deploys fail less catastrophically and roll back faster "
            "than rare big ones. The DORA program continues as an "
            "annual industry report, and the thresholds are the "
            "closest thing the field has to an objective definition of "
            "'good at shipping software.'"
        ),
        "how_it_works": (
            "DORA metrics work as a classification system with levers. "
            "Each metric is measured from the delivery pipeline and the "
            "incident record: deploy counts from the release system, "
            "lead time from commit timestamps to production, MTTR from "
            "incident records, change failure rate from incidents "
            "traced to changes. The team is classified against the "
            "thresholds - elite, high, medium, low - per metric and "
            "overall. The classification then drives improvement "
            "through the capabilities the research validated: trunk-"
            "based development and small batches move deployment "
            "frequency and lead time; automated testing and deployment "
            "automation move change failure rate; and the incident "
            "discipline in this database - fast detection, reversible "
            "changes, blameless learning - moves MTTR. The key insight "
            "for incident management: the metrics move together. Teams "
            "that deploy on demand do not achieve it by being reckless; "
            "they achieve it with the automation and reversibility that "
            "also make their MTTR elite. Speed and stability are not a "
            "trade-off in the data - they are the same capability."
        ),
        "key_points": [
            "Four metrics: deployment frequency, lead time for changes, MTTR, change failure rate - from Accelerate (Forsgren, Humble, Kim, 2018).",
            "Elite thresholds: on-demand deploys, lead time under 1 hour, MTTR under 1 hour, change failure 0-15 percent.",
            "Low performers: monthly-to-half-yearly deploys, week-to-month MTTR, 16-30 percent change failure.",
            "Small frequent deploys fail less catastrophically and roll back faster than rare big ones.",
            "Speed and stability are not a trade-off in the data: the same capabilities drive both.",
        ],
        "requirements": [
            "Pipeline instrumentation for deploy counts and commit-to-production lead time.",
            "Incident records that trace failures to their causing changes.",
            "Classification of the team against the four thresholds, reviewed quarterly.",
            "Improvement plans targeting the validated capabilities: small batches, automation, trunk-based development.",
            "Annual re-benchmarking against the DORA report's current thresholds.",
        ],
        "standards": [
            "Forsgren, Humble, Kim: Accelerate (2018) - the four metrics and performance tiers.",
            "DORA annual reports: current industry benchmarks.",
            "Google SRE practice: MTTR as a core operational metric.",
        ],
        "citations": [CIT_ACCELERATE, CIT_SRE],
        "sig_lens": (
            "The Signature read: the DORA metrics are the Signature "
            "body's fitness trials - the four tests that prove whether "
            "the body is elite or ailing. Where public research "
            "classifies teams, the Signature Incident Method takes the "
            "trials as oath: deploy like breathing, heal within the "
            "hour, and let the numbers - not the boasting - declare "
            "the body's rank."
        ),
    },
    {
        "key": "game_days",
        "name": "Game Days and Incident Drills",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A game day is a scheduled, controlled incident: the team "
            "deliberately breaks something - or pretends to - and "
            "practices the response end to end. Amazon originated the "
            "practice for operational readiness; the industry adopted it "
            "as the fire drill for software. A game day has a scenario "
            "('the primary database is gone'), a scope (staging, or "
            "production with guardrails), participants (the real on-call "
            "rotation, not a special team), and objectives ('fail over "
            "within 30 minutes using only the runbook'). The team runs "
            "the full incident machinery: declaration, IC, timeline, "
            "mitigation, comms - and then holds a postmortem on the "
            "drill itself, because the drill is where the runbook's "
            "lies are found. Game days find the failures of the "
            "response, not the system: the runbook step that references "
            "a decommissioned host, the escalation policy that pages a "
            "person who left, the dashboard nobody can find at 3 AM. "
            "They are also where incident commanders are trained - "
            "command is a skill, and skills need practice under "
            "pressure. The cadence is regular - monthly or quarterly - "
            "because response muscle atrophies, and the scenarios rotate "
            "through the failure modes the risk register fears most."
        ),
        "how_it_works": (
            "A game day works as a rehearsal with a script and a "
            "safety net. Planning picks the scenario from the risk "
            "register, defines the objectives in measurable terms, and "
            "sets the guardrails: blast radius limits, abort conditions, "
            "and a game-day commander with the authority to stop the "
            "exercise. On the day, the fault is injected - a real "
            "failure in a safe environment, or a simulated one announced "
            "to the responders - and the team responds for real: the "
            "on-call is paged (sometimes without warning, sometimes "
            "with), the IC takes command, the timeline runs, "
            "mitigation is attempted with the actual runbooks. Observers "
            "watch for the response failures: where the runbook was "
            "wrong, where the tools were missing, where the "
            "communication broke. The exercise ends with a hot wash - "
            "immediate impressions while fresh - and then a proper "
            "postmortem of the drill with action items, owned and "
            "tracked like any incident's. The metrics: detection time "
            "in the drill versus the last real incident, mitigation "
            "time, and the count of runbook defects found. Each game "
            "day makes the next real incident shorter."
        ),
        "key_points": [
            "A game day is a scheduled controlled incident: real scenario, real on-call, full incident machinery, then a postmortem of the drill.",
            "Game days find response failures: wrong runbooks, dead escalation paths, missing dashboards - not system failures.",
            "Objectives are measurable: fail over within 30 minutes using only the runbook.",
            "Guardrails bound every drill: blast radius limits, abort conditions, a commander who can stop the exercise.",
            "Incident commanders are trained here: command is a skill, and skills need practice under pressure.",
        ],
        "requirements": [
            "A scenario library drawn from the risk register, rotated across failure modes.",
            "Measurable objectives and guardrails (blast radius, abort conditions) for every drill.",
            "Participation by the real on-call rotation, with observers capturing response defects.",
            "A hot wash immediately after and a tracked postmortem with action items.",
            "Regular cadence - monthly or quarterly - with drill metrics trended against real incidents.",
        ],
        "standards": [
            "Amazon operational readiness practice: game day origins and method.",
            "Google SRE Workbook: disaster testing and failure injection exercises.",
            "NIST SP 800-61: incident response testing and exercises.",
        ],
        "citations": [CIT_SRE_WB, CIT_NIST],
        "sig_lens": (
            "The Signature read: game days are the Signature body's war "
            "games - the battles fought in practice so the real battles "
            "are won. Where public engineering schedules drills, the "
            "Signature Incident Method musters the troops: the scenario "
            "the enemy, the runbook the battle plan, and every defect "
            "found in practice a casualty prevented in war."
        ),
    },
    {
        "key": "review_boards",
        "name": "Incident Review Boards",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The incident review board is the governing body of the "
            "whole discipline: the group that reads every significant "
            "postmortem, tracks every action item, watches the metrics "
            "dashboard, and decides where reliability investment goes. "
            "It meets on a fixed cadence - weekly for operations, "
            "monthly for trends - with a fixed membership: engineering "
            "leaders, SRE, product, and support, because incidents touch "
            "all of them. The board's agenda is mechanical: new "
            "postmortems reviewed for action-item quality (are they "
            "systemic, owned, dated), aging action items escalated, the "
            "metrics dashboard walked panel by panel, and recurrence "
            "hunted - the same failure class twice is the board's "
            "personal failure. The board also owns the budget "
            "conversation: which services are burning error budget "
            "fastest, which teams need reliability investment, whether "
            "the SLOs still match the business. Its authority must be "
            "real: a board that can only recommend is a book club. When "
            "the board works, the organization learns faster than "
            "incidents can teach it; when it does not meet, or meets "
            "without teeth, the postmortems pile up unread and the same "
            "outages recur on schedule."
        ),
        "how_it_works": (
            "The board works through cadence, agenda, and authority. "
            "Before each meeting, the members read the new postmortems - "
            "the meeting is for decisions, not narration. The agenda "
            "runs: postmortem review (action items challenged for "
            "systemic quality and ownership), action-item aging (overdue "
            "items escalated with names attached), metrics review (the "
            "dashboard walked, degrading panels assigned owners), and "
            "investment decisions (reliability work prioritized against "
            "feature work, with the error budgets as evidence). The "
            "board's decisions are recorded with the same rigor as "
            "incident timelines: what was decided, who owns it, when it "
            "is due. Between meetings, the board's staff - usually the "
            "SRE team - keeps the machinery running: the dashboard "
            "fed, the tracker current, the postmortems scheduled. The "
            "board reports upward quarterly: availability against SLOs, "
            "incident trends, reliability investment and its results. "
            "The measure of the board is the recurrence metric and the "
            "action-item closure rate - a board that drives those is "
            "governing; anything else is theater."
        ),
        "key_points": [
            "The board governs the discipline: postmortems reviewed, action items tracked, dashboard walked, recurrence hunted.",
            "Fixed cadence, fixed cross-functional membership: engineering, SRE, product, support.",
            "The same failure class twice is the board's personal failure - recurrence is the metric that matters.",
            "Its authority must be real: it directs reliability investment against feature work, with error budgets as evidence.",
            "Members read postmortems before the meeting; the meeting is for decisions, not narration.",
        ],
        "requirements": [
            "A chartered board with named members, a fixed cadence, and real authority over reliability investment.",
            "A mechanical agenda: postmortem review, action-item aging, metrics walk, investment decisions.",
            "Recorded decisions with owners and due dates, tracked like action items.",
            "Pre-read discipline: postmortems read before the meeting.",
            "Quarterly upward reporting: availability vs SLOs, trends, investment results.",
        ],
        "standards": [
            "Google SRE practice: postmortem review and operational oversight.",
            "NIST SP 800-61: incident response program management and metrics.",
            "ITIL 4: continual improvement practice applied to incident management.",
        ],
        "citations": [CIT_SRE, CIT_NIST, CIT_ITIL],
        "sig_lens": (
            "The Signature read: the review board is the Signature "
            "body's council of elders - the keepers of the chronicle "
            "who ensure no battle's lesson is lost. Where public "
            "engineering charters a board, the Signature Incident "
            "Method convenes the elders: they read every testimony, "
            "chase every sworn reform to completion, and guard the "
            "body's memory with the authority of law."
        ),
    },
    {
        "key": "dyn_2016",
        "name": "Case Study: The Dyn DDoS Outage of October 2016",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "On October 21, 2016, the internet learned what a shared "
            "dependency means. Dyn, a major managed DNS provider, was "
            "hit by a massive distributed denial-of-service attack "
            "launched from the Mirai botnet - hundreds of thousands of "
            "compromised Internet-of-Things devices, cameras and routers "
            "with default passwords, marshaled into a flood of DNS "
            "queries. The attack came in waves: the first began around "
            "11:10 UTC and was mitigated by about 13:20 UTC; a second, "
            "more sophisticated wave began around 15:50 UTC and lasted "
            "until about 17:00 UTC. Dyn reported the assault as among "
            "the largest ever seen, with peak traffic reported around "
            "1.2 terabits per second. Because DNS is the internet's "
            "phone book, Dyn's customers - Twitter, Netflix, Reddit, "
            "GitHub, Airbnb, and many others - became unreachable or "
            "degraded for users across large regions, even though their "
            "own systems were healthy: the blast radius of a DNS "
            "provider is every customer downstream. The incident became "
            "the canonical lesson in shared-dependency risk, IoT "
            "security, and DDoS absorption capacity, and it reshaped how "
            "the industry thinks about DNS redundancy - no single "
            "provider, however large, should be the only phone book."
        ),
        "how_it_works": (
            "The attack worked by overwhelming Dyn's DNS infrastructure "
            "with query floods from the Mirai botnet, exploiting the "
            "fact that DNS must answer every query to be useful - there "
            "is no 'busy signal' in the protocol's design that helps "
            "under flood. Dyn's mitigation followed the incident "
            "playbook under extreme pressure: traffic scrubbing and "
            "filtering to separate attack traffic from legitimate "
            "queries, scaling and redistributing DNS capacity, and "
            "coordination with upstream providers and law enforcement. "
            "The two-wave structure is the timeline's key lesson: the "
            "attackers adapted after the first mitigation, shifting "
            "tactics for the second wave, which is why 'mitigated' is "
            "not 'resolved' against an adaptive adversary. For Dyn's "
            "customers, the incident demonstrated dependency risk in "
            "its purest form: their mitigation options were limited to "
            "waiting, failing over to secondary DNS where it existed, "
            "and communicating. The industry's systemic fixes came "
            "afterward: multi-provider DNS as standard practice, "
            "anycast absorption capacity as a purchasing criterion, "
            "and the long, still-unfinished work of securing IoT "
            "devices at manufacture - because Mirai recruited its army "
            "from devices that shipped with default credentials."
        ),
        "key_points": [
            "October 21, 2016: the Mirai IoT botnet attacked Dyn's managed DNS in two waves (about 11:10-13:20 UTC and 15:50-17:00 UTC), with peak traffic reported near 1.2 Tbps.",
            "DNS is a shared dependency: Twitter, Netflix, Reddit, GitHub, and others went dark for users while their own systems were healthy.",
            "The attackers adapted between waves: mitigated is not resolved against an adaptive adversary.",
            "Customer mitigation was limited to waiting, secondary-DNS failover where it existed, and communication.",
            "The systemic lessons: multi-provider DNS, anycast absorption capacity, and securing IoT devices at manufacture.",
        ],
        "requirements": [
            "Critical shared dependencies identified in the blast-radius map before the incident, not during.",
            "Multi-provider redundancy for DNS and other single-point-of-failure services.",
            "DDoS absorption capacity - anycast, scrubbing - sized against the current threat record, not the last decade's.",
            "Customer communication plans for dependency failures where the organization cannot fix the root cause itself.",
            "IoT and supply-chain device hygiene: no default credentials on anything that touches the network.",
        ],
        "standards": [
            "Dyn's published statement on the 10/21/2016 attack: timeline and scale.",
            "NIST SP 800-61: handling denial-of-service as an incident class.",
            "Industry practice post-2016: redundant DNS providers as standard resilience architecture.",
        ],
        "citations": [CIT_DYN, CIT_NIST],
        "sig_lens": (
            "The Signature read: the Dyn outage is the Signature body's "
            "lesson in the shared nerve - when one nerve serves a "
            "thousand limbs, its wound is a thousand wounds. Where "
            "public engineering studies the case, the Signature Incident "
            "Method takes the vow: no single nerve shall ever again be "
            "the body's only path, and the body's phone book is written "
            "in more than one hand."
        ),
    },
    {
        "key": "fastly_2021",
        "name": "Case Study: The Fastly Global Outage of June 2021",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "On June 8, 2021, a large part of the internet went dark for "
            "under an hour - and the cause was a single customer "
            "configuration change. Fastly, the edge cloud and content "
            "delivery network, suffered a global outage from about 09:58 "
            "UTC to about 10:44 UTC: 46 minutes during which roughly 85 "
            "percent of its network returned errors. Major sites and "
            "services - news outlets, retailers, government pages - "
            "showed error pages worldwide. Fastly's published postmortem "
            "is a model of the form: a valid customer configuration "
            "change on May 12 had exposed a latent software bug that had "
            "been introduced in a deployment weeks earlier; the "
            "configuration change on June 8 triggered it, and the bug "
            "took down the serving path across the network. Detection "
            "was fast - within a minute - and the fix was a rollback of "
            "the triggering configuration, followed by a software fix "
            "for the underlying bug. The case is taught because it "
            "compresses so many lessons into 46 minutes: latent bugs "
            "armed by routine changes, the blast radius of edge "
            "infrastructure, fast detection with slower full recovery, "
            "and a postmortem honest enough to name the exact mechanism."
        ),
        "how_it_works": (
            "The failure worked as a two-stage trap. Stage one, May 12: "
            "a software deployment introduced a bug that lay dormant - "
            "no customer configuration exercised the faulty code path, "
            "so every test and every monitor stayed green for weeks. "
            "Stage two, June 8 at 09:58 UTC: a customer made a valid, "
            "ordinary configuration change that happened to exercise "
            "the faulty path, and the bug propagated across the edge "
            "network, returning errors for about 85 percent of traffic. "
            "Fastly's response shows the mitigation-first discipline: "
            "detect in about a minute, identify the trigger, roll back "
            "the configuration to disarm the bug - service largely "
            "restored by 10:44 UTC - and then fix the underlying "
            "software defect properly afterward. The postmortem, "
            "published the same day, named the mechanism precisely and "
            "listed the systemic fixes: broader testing of "
            "configuration-triggered code paths, faster global "
            "rollback of edge configuration, and review of how a "
            "single customer's valid change could have network-wide "
            "effect. For students of incident response, the timeline "
            "math is the lesson: 46 minutes at 85 percent errors "
            "consumed more than a full month's error budget for a "
            "99.9 percent SLO in under an hour."
        ),
        "key_points": [
            "June 8, 2021, about 09:58-10:44 UTC: 46 minutes, roughly 85 percent of Fastly's network returning errors, major sites dark worldwide.",
            "Two-stage trap: a latent bug deployed May 12, armed weeks later by a valid ordinary customer configuration change.",
            "Mitigation-first done right: detect in about a minute, roll back the triggering config, fix the software defect afterward.",
            "Fastly's same-day postmortem named the exact mechanism - the model of honest incident writing.",
            "46 minutes at 85 percent errors exceeds a full month of error budget at 99.9 percent: edge infrastructure has an enormous blast radius.",
        ],
        "requirements": [
            "Configuration changes treated with the same rigor as code changes: testing, canaries, rollback plans.",
            "Code-path coverage for configuration-triggered behavior, not just API-triggered behavior.",
            "Global configuration rollback measured in minutes, drilled in game days.",
            "Blast-radius limits on edge configuration: no single customer's valid change should have network-wide effect.",
            "Same-day postmortem publication for customer-facing outages, naming the mechanism precisely.",
        ],
        "standards": [
            "Fastly's published Summary of June 8 outage (2021): timeline, mechanism, remediation.",
            "Google SRE practice: blameless postmortem with precise mechanism and systemic actions.",
            "Change-management rigor per ITIL 4 applied to configuration as well as code.",
        ],
        "citations": [CIT_FASTLY, CIT_SRE, CIT_ITIL],
        "sig_lens": (
            "The Signature read: the Fastly outage is the Signature "
            "body's lesson in the sleeping serpent - the bug that waits "
            "weeks for the footstep that wakes it. Where public "
            "engineering studies the timeline, the Signature Incident "
            "Method keeps the vigil: every change, however ordinary, is "
            "a footstep near sleeping serpents, and the body's rollback "
            "is the hand that can put the serpent back to sleep in "
            "minutes."
        ),
    },
    {
        "key": "aws_2021",
        "name": "Case Study: The AWS US-East-1 Outage of December 2021",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "On December 7, 2021, the cloud itself stumbled. Beginning "
            "around 10:48 AM Eastern, AWS's US-EAST-1 region - Northern "
            "Virginia, the company's oldest and largest region - began "
            "showing increased error rates and latencies across multiple "
            "services. The cause, per AWS's published summary, was an "
            "automated capacity-scaling activity on the internal AWS "
            "network that triggered unexpected behavior from clients "
            "inside the network, congesting the connections between the "
            "internal network and the AWS backbone. The damage was "
            "worst in the control plane: the APIs and consoles used to "
            "manage infrastructure - launching instances, changing "
            "configurations - degraded, along with services including "
            "EC2, Connect, and others. Downstream, household names "
            "built on AWS - streaming, smart-home, delivery services - "
            "showed errors to their own users, demonstrating the blast "
            "radius of a region that hosts a large share of the "
            "internet. Recovery took hours: AWS disabled the scaling "
            "activity, added capacity, and worked through the afternoon "
            "until services were substantially restored by the evening. "
            "The case is the definitive lesson in control-plane versus "
            "data-plane separation - much of the data plane kept "
            "serving while the control plane could not be managed - and "
            "in regional concentration risk: when one region holds "
            "enough of the internet, its bad day is everyone's."
        ),
        "how_it_works": (
            "The failure worked as automation turning on its owner. The "
            "trigger: a routine automated scaling of internal network "
            "capacity, the kind of activity that runs constantly and "
            "safely. The amplifier: unexpected behavior from internal "
            "clients under the scaled configuration, producing "
            "congestion on the links between the internal network and "
            "the AWS network - the automation's own traffic choking the "
            "paths it needed. The impact concentrated where those "
            "paths mattered most: the control plane, the APIs and "
            "consoles through which every customer manages their "
            "infrastructure, so engineers across thousands of companies "
            "could not launch, stop, or reconfigure resources, and "
            "services with control-plane dependencies degraded. The "
            "data plane - the actual serving of traffic - largely kept "
            "working, which is why the outage looked patchy from the "
            "outside: some things fine, some things broken, management "
            "impossible. Mitigation meant stopping the automation, "
            "adding capacity by hand, and draining the congestion - "
            "hours of work because the very tools for fast remediation "
            "depended on the degraded control plane. AWS's published "
            "summary listed the systemic fixes: better guardrails on "
            "internal network automation, improved congestion handling, "
            "and continued investment in control-plane isolation. The "
            "generalized lesson: automate the network, but bound the "
            "automation's blast radius - and never let one region be a "
            "single point of failure for the whole architecture."
        ),
        "key_points": [
            "December 7, 2021, from about 10:48 AM Eastern: automated internal-network capacity scaling congested AWS's US-EAST-1 region for hours.",
            "The control plane suffered most: management APIs and consoles degraded, so thousands of companies could not manage their infrastructure.",
            "The data plane largely kept serving: the outage looked patchy - some things fine, management impossible.",
            "Downstream household services showed errors: the blast radius of the internet's most concentrated region.",
            "The systemic fixes: guardrails on network automation, congestion handling, and control-plane isolation.",
        ],
        "requirements": [
            "Control-plane/data-plane separation designed and tested: management must survive serving failures and vice versa.",
            "Blast-radius bounds on all infrastructure automation: staged rollouts, automatic halt on anomaly.",
            "Multi-region architecture for critical services: no single region as a single point of failure.",
            "Manual remediation paths that do not depend on the degraded control plane.",
            "Published post-incident summaries for customer-impacting events, naming the mechanism.",
        ],
        "standards": [
            "AWS: Summary of the AWS Service Event in the Northern Virginia (US-EAST-1) Region (2021) - the authoritative postmortem.",
            "NIST SP 800-61: contingency planning and control-plane resilience.",
            "Google SRE practice: automation with guardrails and bounded blast radius.",
        ],
        "citations": [CIT_AWS, CIT_NIST, CIT_SRE],
        "sig_lens": (
            "The Signature read: the AWS outage is the Signature body's "
            "lesson in the automation that turned - the trusted servant "
            "that choked the halls it was built to widen. Where public "
            "engineering studies the summary, the Signature Incident "
            "Method binds every automation: serve the body, but never "
            "grow teeth the body cannot pull, and never let one hall "
            "hold the keys to every room."
        ),
    },
]
