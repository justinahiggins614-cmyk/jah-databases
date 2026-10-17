#!/usr/bin/env python3
"""Entries for the Schedules and Resource Calendars databases (missing-115, Wave 1).

Item 50 of ~/workspace/hidden_files/catalog-missing-categories-115.txt:
appointments, equipment availability, personnel shifts, facilities, and
maintenance windows - scheduling algorithms, shift-rotation rules, constraint
satisfaction, calendar data models, recurrence rules, time-zone handling, and
resource conflict resolution.

Verified 2026-10-17 (missing-115 Wave 1): RAW SWEEP over the full manifest
(2,390 databases) PLUS every shard index in jah-databases-data-1: zero
'schedules-resource-calendars*' slugs/names; zero title collisions on the 34
record titles below. The one keyword near-hit family, generic calendar or
time-topic encyclopedia entries elsewhere, carries no per-resource
scheduling model - no slots, rotations, conflict resolution, or
constraint machinery. The paste's rule was applied by name/purpose/record
schema/capabilities: an operational scheduling database (appointments,
shifts, equipment, facilities, maintenance windows; algorithms, rotations,
constraints, recurrence, time zones, conflict resolution) is a distinct
capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  schedules-resource-calendars            - The Schedules and Resource Calendars
                                            Database (public-harvest: real,
                                            fact-checked scheduling science -
                                            appointments, equipment
                                            availability, personnel shifts,
                                            facilities, maintenance windows;
                                            calendar data models, recurrence
                                            rules, time-zone handling,
                                            scheduling algorithms,
                                            shift-rotation rules, constraint
                                            satisfaction, and resource conflict
                                            resolution; standard references
                                            RFC 5545 iCalendar, RFC 5546
                                            iTIP, RFC 4791 CalDAV, RFC 6352
                                            CardDAV, RFC 5905 NTP, ISO
                                            8601:2019, the IANA time zone
                                            database, Pinedo Scheduling 6th
                                            ed 2022, Garey and Johnson 1979,
                                            Kelley and Walker 1959 (CPM),
                                            Malcolm et al 1959 (PERT), Kuhn
                                            1955 and Munkres 1957
                                            (Hungarian), Little 1961,
                                            Kleinrock 1975, Lamport 1978,
                                            Graham et al 1979, de Werra 1985,
                                            Moubray 1997 RCM, ISO 55000:2024,
                                            NIOSH shiftwork guidance, Czeisler
                                            et al 1982, Gantt 1913, Goldratt
                                            The Goal, and PMBOK Guide 7th ed)
  schedules-resource-calendars-signature  - The Schedules and Resource
                                            Calendars Signature Database
                                            (his original Signature
                                            Scheduling Method: every slot a
                                            covenant of time, the calendar the
                                            ledger of kept promises,
                                            rotation the rhythm, conflict the
                                            broken oath, the maintenance
                                            window the honored rest;
                                            src signature, titles suffixed
                                            " (Signature Edition)", never
                                            presented as authentic public
                                            record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-SCH- (public) and JAH-SCHS- (signature), verified free in
the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_schedules_resource_calendars.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and ends
with the OK marker; the build machine-executes all 68 demos before commit.

Scope is civilian operational scheduling only - appointments, shifts,
equipment, facilities, maintenance. Never the words "bat belt" anywhere.
No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Scheduling Method: "
            "every slot a covenant of time, the calendar the ledger of kept "
            "promises, rotation the rhythm, conflict the broken oath, and "
            "the maintenance window the honored rest. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_RFC5545 = ("Desruisseaux B (Ed.). RFC 5545. Internet Calendaring and "
               "Scheduling Core Object Specification (iCalendar); September "
               "2009 (obsoletes RFC 2445).")
CIT_RFC5546 = ("Daboo C. RFC 5546. iCalendar Transport-Independent "
               "Interoperability Protocol (iTIP); 2009.")
CIT_RFC4791 = ("Daboo C, Desruisseaux B, Dusseault L. RFC 4791. Calendaring "
               "Extensions to WebDAV (CalDAV); 2007.")
CIT_RFC6352 = ("Daboo C. RFC 6352. CardDAV: vCard Extensions to WebDAV; "
               "2011.")
CIT_RFC5905 = ("Mills D et al. RFC 5905. Network Time Protocol Version 4: "
               "Protocol and Algorithms Specification; 2010.")
CIT_RFC3339 = ("Klyne G, Newman C. RFC 3339. Date and Time on the Internet: "
               "Timestamps; 2002.")
CIT_ISO8601 = ("ISO 8601:2019. Date and time format - ISO 8601.")
CIT_IANATZ = ("IANA Time Zone Database (tz database). Maintained by the "
              "Internet Assigned Numbers Authority; releases versioned as "
              "tzdata.")
CIT_PINEDO = ("Pinedo ML. Scheduling: Theory, Algorithms, and Systems. 6th "
              "ed. Springer; 2022.")
CIT_GAREY = ("Garey MR, Johnson DS. Computers and Intractability: A Guide "
             "to the Theory of NP-Completeness. W.H. Freeman; 1979.")
CIT_KELLEY = ("Kelley JE Jr, Walker MR. Critical-path planning and "
              "scheduling. Proceedings of the Eastern Joint Computer "
              "Conference; 1959.")
CIT_PERT = ("Malcolm DG, Roseboom JH, Clark CE, Fazar W. Application of a "
            "technique for research and development program evaluation. "
            "Operations Research; 1959.")
CIT_KUHN = ("Kuhn HW. The Hungarian method for the assignment problem. "
            "Naval Research Logistics Quarterly; 1955.")
CIT_MUNKRES = ("Munkres J. Algorithms for the assignment and transportation "
               "problems. Journal of the Society for Industrial and Applied "
               "Mathematics; 1957.")
CIT_LITTLE = ("Little JDC. A proof for the queuing formula: L = lambda W. "
              "Operations Research; 1961.")
CIT_KLEINROCK = ("Kleinrock L. Queueing Systems. Vol. 1: Theory. Wiley; "
                 "1975.")
CIT_ERLANG = ("Erlang AK. Solution of some problems in the theory of "
              "probabilities of significance in automatic telephone "
              "exchanges. Elektroteknikeren; 1917.")
CIT_LAMPORT = ("Lamport L. Time, clocks, and the ordering of events in a "
               "distributed system. Communications of the ACM; 1978.")
CIT_GRAHAM = ("Graham RL, Lawler EL, Lenstra JK, Rinnooy Kan AHG. "
              "Optimization and approximation in deterministic sequencing "
              "and scheduling: a survey. Annals of Discrete Mathematics; "
              "1979.")
CIT_DEWERRA = ("de Werra D. An introduction to timetabling. European Journal "
               "of Operational Research; 1985.")
CIT_MOUBRAY = ("Moubray J. Reliability-centered Maintenance. 2nd ed. "
               "Industrial Press; 1997.")
CIT_ISO55000 = ("ISO 55000:2024. Asset management - Overview, principles "
                "and terminology.")
CIT_NIOSH = ("US National Institute for Occupational Safety and Health. "
              "Plain Language About Shiftwork; 1997.")
CIT_CZEISLER = ("Czeisler CA, Moore-Ede MC, Coleman RH. Rotating shift work "
                "schedules that disrupt sleep are improved by applying "
                "circadian principles. Science; 1982.")
CIT_GANTT = ("Gantt HL. Work, Wages, and Profits. Engineering Magazine Co.; "
             "1913.")
CIT_GOLDRATT = ("Goldratt EM. The Goal: A Process of Ongoing Improvement. "
                "3rd revised ed. North River Press; 2004.")
CIT_PMBOK = ("Project Management Institute. A Guide to the Project "
             "Management Body of Knowledge (PMBOK Guide). 7th ed.; 2021.")
CIT_ITIL = ("Axelos. ITIL Foundation: ITIL 4 Edition; 2019.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is a Schedule and a Resource Calendar",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A schedule is a promise about time: who or what will be where, "
            "doing what, and when. A resource calendar is the schedule seen "
            "from the resource side - the room, the machine, the person, the "
            "vehicle - showing when it is free, booked, busy, or down. "
            "Appointments promise time to people. Equipment availability "
            "promises time on machines. Personnel shifts promise people to "
            "the operation. Facilities promise rooms and spaces. Maintenance "
            "windows promise the resource back to itself, for repair. Every "
            "schedule answers the same four questions: which resource, which "
            "interval of time, which activity, and in what state. Conflicts "
            "happen when two promises claim the same resource in the same "
            "interval - the central enemy this whole database teaches you "
            "to defeat. This record frames the database: every later record "
            "is one instrument for making, checking, or keeping promises "
            "about time."
        ),
        "how_it_works": (
            "Scheduling works by turning time into a ledger. Each resource "
            "gets a timeline divided into intervals, and each interval holds "
            "a state: free, tentatively held, committed, busy, down for "
            "maintenance, or blocked. Booking writes a new interval into "
            "the ledger; the ledger rejects any write that overlaps an "
            "incompatible state on the same resource - that rejection is "
            "conflict detection, the simplest and most important operation "
            "in scheduling. Appointments book people; shifts book people to "
            "coverage; equipment reservations book machines; room bookings "
            "book space; maintenance windows book the resource for its own "
            "care, marked so nothing else can claim it. A good scheduling "
            "system keeps one authoritative ledger per resource, records who "
            "made each promise and when, and lets every consumer read the "
            "same truth. Everything else in this database - recurrence, "
            "time zones, algorithms, rotations - is machinery for writing, "
            "reading, and defending this ledger."
        ),
        "key_points": [
            "A schedule promises time; a resource calendar is that promise seen from the resource side - the room, the machine, the person - showing free, booked, busy, or down.",
            "Every schedule answers four questions: which resource, which interval, which activity, and in what state; conflicts are two promises claiming the same resource in the same interval.",
            "Appointments book people, shifts book people to coverage, equipment reservations book machines, room bookings book space, maintenance windows book the resource for its own care.",
            "Conflict detection - rejecting an overlapping booking on the same resource - is the simplest and most important operation in scheduling.",
            "One authoritative ledger per resource, recording who made each promise and when, is what keeps every consumer reading the same truth.",
        ],
        "requirements": [
            "A resource identity: every bookable thing (person, room, machine, vehicle) named and addressable in the system.",
            "An interval representation with a defined start, end, and state for every booking on the timeline.",
            "A conflict rule per resource stating which states may overlap and which may never overlap.",
            "An audit trail: who made the promise, when, and under what authority.",
            "A single authoritative ledger per resource that all booking paths write through.",
        ],
        "standards": [
            "Intervals follow ISO 8601:2019 for date-time representation; exchanges between systems use RFC 3339 timestamps.",
            "Calendar interchange follows RFC 5545 (iCalendar); scheduling transactions follow RFC 5546 (iTIP).",
            "Project scheduling conventions follow the PMBOK Guide 7th edition.",
        ],
        "citations": [CIT_RFC5545, CIT_ISO8601, CIT_PMBOK],
        "sig_lens": (
            "The Signature read: a schedule is a ledger of covenants, and "
            "every booking is an oath written in time. Where public "
            "operations files an appointment, the Signature Scheduling "
            "Method files a promise - the resource swears its hours, the "
            "booker swears to honor them, and the calendar holds because "
            "both kept their word. A conflict is a broken oath, and the "
            "ledger rejects it."
        ),
    },
    {
        "key": "data_models",
        "name": "Calendar Data Models: Events, Slots, and Resources",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Before any scheduling software can run, time and resources must "
            "be modeled as data. The three primitives are events (something "
            "happening over an interval, with a start, an end, a summary, "
            "and a list of attendees or resources), slots (bookable units "
            "of availability, like a 30-minute appointment window or an "
            "8-hour shift), and resources (the people, rooms, machines, and "
            "vehicles being booked, each with a capacity and a calendar of "
            "its own). iCalendar, the world interchange standard RFC 5545, "
            "models events as VEVENT components with DTSTART, DTEND or "
            "DURATION, RRULE for recurrence, and ATTENDEE and ORGANIZER "
            "properties. Availability is modeled as VFREEBUSY components "
            "that answer the one question booking needs: when is this "
            "resource free. Slots are derived from free/busy data plus "
            "business rules: slot length, buffers between slots, booking "
            "horizon, and cutoff times. Get the model right and every "
            "algorithm downstream is easy; get it wrong and nothing "
            "downstream can save you."
        ),
        "how_it_works": (
            "A calendar data model works by giving every concept a typed, "
            "exchangeable shape. An event carries an identifier, a start "
            "instant, an end instant or duration, a summary, a status "
            "(tentative, confirmed, cancelled), and links to attendees and "
            "resources. A resource carries an identifier, a display name, a "
            "type (room, equipment, person), a capacity, and a reference to "
            "its own calendar. Availability is computed by subtracting "
            "committed intervals from the resource working hours to produce "
            "free/busy intervals, then carving those into bookable slots "
            "with the slot-length and buffer rules applied. Recurring "
            "events expand from one rule into many instances. Time zones are "
            "stored as identifiers from the IANA database, never as bare "
            "offsets, so daylight-saving transitions compute correctly. "
            "When two systems exchange calendars, they serialize these "
            "shapes into iCalendar text; when one system schedules across "
            "another, it negotiates through iTIP messages or CalDAV. The "
            "model is the contract every scheduling algorithm trusts."
        ),
        "key_points": [
            "The three primitives are events (something over an interval), slots (bookable units of availability), and resources (people, rooms, machines with their own calendars).",
            "iCalendar RFC 5545 models events as VEVENT with DTSTART, DTEND or DURATION, RRULE for recurrence, and ATTENDEE/ORGANIZER properties.",
            "Free/busy data (VFREEBUSY) answers the one question booking needs: when is this resource free.",
            "Slots are derived from free/busy plus business rules: slot length, buffers, booking horizon, and cutoff times.",
            "Time zones are stored as IANA identifiers, never bare offsets, so daylight-saving transitions compute correctly.",
        ],
        "requirements": [
            "Typed records for events, slots, and resources with stable unique identifiers.",
            "Start and end instants on every event, plus a status field (tentative, confirmed, cancelled).",
            "A free/busy computation that subtracts committed intervals from working hours.",
            "Slot-carving rules: length, buffers, horizon, and cutoff times.",
            "IANA time-zone identifiers on every local-time value that crosses a daylight-saving boundary.",
        ],
        "standards": [
            "Calendar objects follow RFC 5545 (iCalendar); scheduling messages follow RFC 5546 (iTIP).",
            "Date-time values follow ISO 8601:2019 and RFC 3339; time zones come from the IANA tz database.",
        ],
        "citations": [CIT_RFC5545, CIT_RFC5546, CIT_ISO8601, CIT_IANATZ],
        "sig_lens": (
            "The Signature read: the data model is the covenant's written "
            "form. An event is the promise made legible; a slot is an hour "
            "sworn open; a resource is the keeper of its own ledger. The "
            "Signature Scheduling Method insists every promise carry its "
            "identity, its interval, and its state, so no oath can hide "
            "inside vague data."
        ),
    },
    {
        "key": "time_interval",
        "name": "Time, Duration, and the Interval",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "All scheduling arithmetic rests on three ideas: the instant (a "
            "point in time), the duration (a length of time, like 90 "
            "minutes), and the interval (an instant pair - start and end - "
            "that claims a stretch of the timeline). The interval is the "
            "atom of every calendar: a meeting is an interval, a shift is "
            "an interval, a maintenance window is an interval. Intervals can "
            "relate to each other in exactly thirteen ways, catalogued by "
            "James Allen in 1983: before, meets, overlaps, starts, during, "
            "finishes, equals, and their inverses. Two intervals overlap "
            "when each starts before the other ends - start_A < end_B and "
            "start_B < end_A - which is the single test that decides every "
            "double-booking. Endpoints need a convention: the half-open "
            "interval [start, end), where the end belongs to the next "
            "interval, is the standard because back-to-back bookings "
            "touch but never collide. Durations are stored as lengths, not "
            "as end-minus-start arithmetic on wall clocks, because a "
            "one-hour meeting across a daylight-saving change is still one "
            "hour even when the clock jumps."
        ),
        "how_it_works": (
            "Interval arithmetic works by comparing endpoints. To test "
            "whether a new booking conflicts, the system asks the ledger "
            "for every existing interval on that resource whose range "
            "touches the new interval's range, then applies the overlap "
            "test: the intervals overlap if and only if start_A < end_B "
            "and start_B < end_A, using half-open [start, end) semantics so "
            "a booking ending exactly when another begins is not a "
            "conflict. Durations add to instants: a 90-minute meeting "
            "starting at 14:00 ends at 15:30 by duration arithmetic, not by "
            "reading the clock twice. Scheduling systems store intervals "
            "either as (start, end) pairs or (start, duration) pairs; both "
            "convert losslessly. For queries like 'find all free time next "
            "week', the system walks the sorted interval list, emitting the "
            "gaps between consecutive busy intervals that are at least as "
            "long as the requested duration. Every recurrence expansion, "
            "every conflict check, and every free/busy answer in this "
            "database is this endpoint comparison running at scale."
        ),
        "key_points": [
            "The instant is a point in time, the duration a length of time, the interval a start-end pair claiming a stretch of the timeline - the interval is the atom of every calendar.",
            "Two intervals overlap if and only if each starts before the other ends: start_A < end_B and start_B < end_A.",
            "Half-open [start, end) endpoint semantics are the standard: back-to-back bookings touch but never collide.",
            "Durations are stored as lengths, not end-minus-start on wall clocks, so a one-hour meeting stays one hour across a daylight-saving change.",
            "Free time is found by walking the sorted interval list and emitting gaps at least as long as the requested duration.",
        ],
        "requirements": [
            "An instant representation with a defined epoch and resolution (at least one minute, ideally one second or finer).",
            "A stated endpoint convention - half-open [start, end) - applied consistently to every interval.",
            "Duration arithmetic that adds lengths to instants without reading wall clocks twice.",
            "A sorted interval store per resource so overlap queries and gap scans run in order.",
            "Tests covering the thirteen Allen relations, especially meets, overlaps, and equals at boundaries.",
        ],
        "standards": [
            "Instants and durations follow ISO 8601:2019; internet timestamps follow RFC 3339.",
            "Interval relations follow Allen's interval algebra (1983).",
        ],
        "citations": [CIT_ISO8601, CIT_RFC3339],
        "sig_lens": (
            "The Signature read: the interval is the covenant's measure. "
            "The instant is when the oath is spoken, the duration how long "
            "it binds, the interval the whole of the keeping. The "
            "Signature Scheduling Method treats every endpoint as "
            "sacred: touch without trespass, for a promise kept exactly "
            "is a promise kept fully."
        ),
    },
    {
        "key": "recurrence",
        "name": "Recurrence Rules: RRULE and Recurring Events",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Most real schedules repeat: the weekly team meeting, the "
            "monthly maintenance, the rotating shift. Storing every instance "
            "as a separate event would bloat calendars and make changes a "
            "nightmare, so iCalendar RFC 5545 defines the recurrence rule, "
            "RRULE - a compact formula that generates instances. A rule "
            "names a frequency (DAILY, WEEKLY, MONTHLY, YEARLY), an interval "
            "(every Nth), and selectors: BYDAY picks weekdays (MO,TU), "
            "BYMONTHDAY picks dates, BYHOUR and BYMINUTE pick times. "
            "'FREQ=WEEKLY;BYDAY=MO,WE,FR' means every Monday, Wednesday, "
            "and Friday. COUNT caps the number of instances; UNTIL caps the "
            "end date. EXDATE removes specific instances (the holiday the "
            "meeting skips) and RDATE adds one-offs. Changed instances get "
            "their own event with the same UID and a RECURRENCE-ID naming "
            "which instance they override - the series keeps its rule while "
            "one meeting moves. Expansion turns the rule into instances for "
            "a requested window; the golden rule is to expand lazily, only "
            "for the window being viewed, because an unbounded rule has "
            "infinitely many instances."
        ),
        "how_it_works": (
            "A recurrence rule works as a generator. Given the series start "
            "(DTSTART), the rule's frequency steps through time - daily "
            "steps of N days, weekly steps anchored to the week start, "
            "monthly steps by day-of-month or by weekday position "
            "(BYDAY=2TU, the second Tuesday), yearly steps by month and "
            "day. Each step produces candidate instants; the BYxxx "
            "selectors filter them; LIMIT clauses (COUNT, UNTIL) stop "
            "generation; EXDATE values delete instances; RDATE values add "
            "them. An overridden instance is a separate VEVENT sharing the "
            "series UID with a RECURRENCE-ID, and it wins over the "
            "generated instance. Expansion for display or conflict checking "
            "walks this generator only across the queried window - a "
            "calendar view of one month expands at most one month of "
            "instances. Correct expansion must honor time-zone rules per "
            "instance: a 9:00 meeting in New York stays 9:00 local through "
            "daylight-saving changes even though its UTC instant shifts."
        ),
        "key_points": [
            "RRULE is a compact formula: frequency plus interval plus BYxxx selectors generates instances instead of storing them all.",
            "FREQ=WEEKLY;BYDAY=MO,WE,FR means every Monday, Wednesday, Friday; COUNT or UNTIL bounds the series.",
            "EXDATE removes instances (holidays), RDATE adds one-offs, and RECURRENCE-ID overrides a single instance while the series keeps its rule.",
            "Expand lazily: generate instances only for the window being viewed, because an unbounded rule has infinitely many instances.",
            "Expansion must honor time-zone rules per instance so a 9:00 local meeting stays 9:00 local across daylight-saving changes.",
        ],
        "requirements": [
            "A rule parser supporting FREQ, INTERVAL, COUNT, UNTIL, BYDAY, BYMONTHDAY, BYHOUR, BYMINUTE, BYMONTH, BYWEEKNO at minimum.",
            "EXDATE/RDATE handling and RECURRENCE-ID override resolution.",
            "Lazy expansion bounded by the queried window, with a sane cap on generated instances.",
            "Per-instance time-zone evaluation using the IANA database, not a fixed offset.",
            "Round-trip fidelity: parse, expand, and re-serialize without losing rule details.",
        ],
        "standards": [
            "Recurrence follows RFC 5545 Section 3.3.10 (RRULE) and 3.8.5 (recurrence properties).",
            "Time zones for recurring local times use the IANA tz database.",
        ],
        "citations": [CIT_RFC5545, CIT_IANATZ],
        "sig_lens": (
            "The Signature read: recurrence is the covenant renewed. One "
            "oath spoken once, kept a thousand times - the weekly meeting, "
            "the monthly maintenance - each instance a fresh keeping of "
            "the same promise. The Signature Scheduling Method honors the "
            "series as one vow with many keepings, and the override as the "
            "vow wisely amended."
        ),
    },
    {
        "key": "time_zones",
        "name": "Time Zones, DST, and the True Instant",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A time zone is not an offset; it is a history of offsets. "
            "New York is UTC-5 in winter and UTC-4 in summer, and the exact "
            "switch dates have changed by law several times - the rules "
            "live in the IANA time zone database, the tz database, which "
            "every serious system uses. Scheduling stores each moment two "
            "ways: the true instant (UTC, the same everywhere) and the "
            "local wall time with its zone identifier (America/New_York). "
            "Daylight-saving transitions create two notorious hours: the "
            "spring gap, where 2:30 AM does not exist, and the autumn fold, "
            "where 1:30 AM happens twice. A scheduler must decide policy "
            "for both: skip or shift the gap hour, and disambiguate the "
            "fold by first or second occurrence. Floating times (no zone, "
            "like 'the office opens at 9') and UTC times (a satellite pass) "
            "are the two safe special cases. The classic bug is storing "
            "only the offset (-0500): it freezes the rule at booking time "
            "and breaks the moment the law changes the transition."
        ),
        "how_it_works": (
            "Time-zone handling works by converting between local wall "
            "time and UTC through the tz database. To display, take the "
            "stored UTC instant and render it in the viewer's zone; to "
            "book, take the entered wall time plus its zone identifier and "
            "resolve it to UTC. Resolution during a gap (spring forward) "
            "either rejects the nonexistent time or shifts it forward by "
            "policy; during a fold (fall back), the system picks the first "
            "or second occurrence by policy and records which. Recurring "
            "events resolve per instance, so '9:00 every Monday in New "
            "York' stays 9:00 local while its UTC instant moves by an hour "
            "twice a year. Network time (NTP, RFC 5905) keeps machine "
            "clocks within milliseconds of UTC so timestamps from "
            "different servers compare correctly. The invariant: the UTC "
            "instant is the truth, the zone identifier is the lens, and "
            "the offset is a derived value that must never be stored "
            "alone."
        ),
        "key_points": [
            "A time zone is a history of offsets, not one offset; the rules live in the IANA tz database and change by law.",
            "Store the UTC instant plus the zone identifier; never store a bare offset, which freezes the rule at booking time.",
            "Spring forward creates a nonexistent hour; fall back creates an ambiguous hour - the scheduler needs a stated policy for both.",
            "Recurring local events resolve per instance so 9:00 local stays 9:00 local while the UTC instant shifts.",
            "NTP (RFC 5905) keeps machine clocks near UTC so timestamps from different servers compare correctly.",
        ],
        "requirements": [
            "The IANA tz database (current tzdata) as the single source of zone rules.",
            "UTC instants for the truth, zone identifiers for the lens, offsets derived and never stored alone.",
            "Documented gap policy (reject or shift) and fold policy (first or second occurrence).",
            "Per-instance resolution for recurring events.",
            "NTP-synchronized clocks on every server that writes timestamps.",
        ],
        "standards": [
            "Time-zone rules come from the IANA tz database; timestamps follow RFC 3339 and ISO 8601:2019.",
            "Network clock synchronization follows RFC 5905 (NTP version 4).",
        ],
        "citations": [CIT_IANATZ, CIT_RFC5905, CIT_RFC3339],
        "sig_lens": (
            "The Signature read: the instant is the same everywhere, but "
            "every place keeps its own hours - the covenant must be read "
            "in the keeper's own time. The Signature Scheduling Method "
            "stores the true instant as the unbreakable word and the zone "
            "as the tongue it is spoken in, so no promise is lost in "
            "translation between shores."
        ),
    },
    {
        "key": "appointments",
        "name": "Appointments and Booking Slots",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Appointments are the atomic unit of service scheduling: one "
            "client, one provider, one slot. A booking system carves a "
            "provider's working hours into slots - 15, 30, or 60 minutes - "
            "then applies the business rules that make booking civilized: "
            "buffers between appointments (the 10 minutes to reset the "
            "room), cutoff times (no booking within 2 hours of start), a "
            "booking horizon (90 days out, no further), and capacity per "
            "slot (one client, or a group class of twelve). The lifecycle "
            "runs: available, tentatively held while the client decides, "
            "confirmed on commitment, checked in at arrival, completed or "
            "no-show at the end. No-shows are the industry's tax - "
            "healthcare and services routinely lose 5 to 10 percent of "
            "slots - and the countermeasures are reminders, deposits, "
            "overbooking models, and waitlists. The slot grid is the "
            "simplest scheduling data structure in this database, and "
            "every later algorithm is a generalization of filling it well."
        ),
        "how_it_works": (
            "Appointment booking works as a guarded write to the slot "
            "grid. The client picks a service, which fixes the slot "
            "length; the system computes free slots from the provider's "
            "working hours minus existing bookings minus buffers, limited "
            "by the horizon and cutoff rules. Selecting a slot places a "
            "tentative hold with an expiry - typically 5 to 15 minutes - "
            "so two clients racing for the same slot cannot both win; the "
            "hold is a lock with a timeout. Confirming converts the hold "
            "to a committed booking and fires reminders on schedule. "
            "Cancelling frees the slot and may trigger the waitlist, which "
            "offers the freed slot to waiting clients in priority order. "
            "Double-booking protection is the interval overlap test on the "
            "provider's ledger, run inside a transaction so concurrent "
            "bookings serialize. Reporting closes the loop: utilization "
            "(booked minutes over available minutes), no-show rate, and "
            "lead time (booking date to appointment date) tell whether the "
            "grid is sized right."
        ),
        "key_points": [
            "The slot grid is carved from working hours minus bookings minus buffers, bounded by horizon and cutoff rules.",
            "A tentative hold with an expiry acts as a lock with a timeout so two racing clients cannot both win a slot.",
            "The lifecycle runs available, held, confirmed, checked in, completed or no-show; each transition is recorded.",
            "No-shows tax 5 to 10 percent of slots in services; reminders, deposits, overbooking models, and waitlists are the countermeasures.",
            "Utilization, no-show rate, and lead time tell whether the grid is sized right.",
        ],
        "requirements": [
            "Slot definitions per service: length, buffers, capacity, horizon, and cutoff.",
            "Tentative holds with expiry to serialize concurrent booking attempts.",
            "Transactional double-booking protection via the interval overlap test.",
            "Reminder, cancellation, and waitlist workflows.",
            "Utilization, no-show, and lead-time reporting.",
        ],
        "standards": [
            "Interchange of appointments follows RFC 5545 (iCalendar) and RFC 5546 (iTIP).",
            "Slot and booking timestamps follow ISO 8601:2019.",
        ],
        "citations": [CIT_RFC5545, CIT_RFC5546, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: an appointment is the smallest covenant "
            "the Method keeps - one hour, two parties, one oath. The "
            "hold is the promise half-spoken, the confirmation the oath "
            "sealed, the no-show the oath broken. The Signature "
            "Scheduling Method guards every slot as a sworn hour and "
            "counts every kept appointment as honor paid in full."
        ),
    },
    {
        "key": "shifts",
        "name": "Personnel Shifts and Rotation Plans",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Shifts promise people to the operation: who works which hours, "
            "in which role, at which station. The vocabulary is fixed. A "
            "shift is one work interval; a roster is the assignment of "
            "people to shifts over a period; a rotation is the repeating "
            "pattern (the famous 2-2-3: two days on, two off, three on); "
            "coverage is the headcount and skills present in each interval. "
            "Design starts from demand: how many people with which skills "
            "each hour needs, which is a forecasting problem, then builds "
            "shifts to cover it, then assigns people honoring constraints: "
            "max hours per week, minimum rest between shifts (often 8 to "
            "11 hours), days-off rules, skill mix, and seniority or "
            "fairness. Rotations run forward (morning to evening to night, "
            "with the clock) because the human circadian system adapts far "
            "better to delays than advances - Czeisler's 1982 work showed "
            "forward-rotating schedules measurably improve sleep. NIOSH "
            "shiftwork guidance adds the guardrails: limit consecutive "
            "nights, protect recovery days, and keep schedules predictable "
            "enough for workers to plan their lives."
        ),
        "how_it_works": (
            "Shift scheduling works in three passes. First, demand "
            "forecasting turns historical load into required headcount by "
            "skill per interval - call volumes, patient census, production "
            "targets. Second, shift construction builds shift templates "
            "(start, length, role, station) whose coverage sums to at least "
            "the demand in every interval; this is the set-covering heart "
            "of the problem. Third, rostering assigns named people to the "
            "constructed shifts, honoring labor constraints: weekly hour "
            "caps, minimum rest between shifts, one-in-seven days off "
            "rules, skill qualifications, and time-off requests. Rotations "
            "are encoded as repeating patterns over a cycle of days, and "
            "each worker follows the pattern offset by their crew letter. "
            "Swap and bid workflows let workers trade shifts within the "
            "constraint rules, and every change re-validates coverage so "
            "no interval drops below minimum staffing. Overtime, "
            "absenteeism, and call-outs are handled by the relief pool and "
            "the on-call rotation - the schedule's shock absorbers."
        ),
        "key_points": [
            "A shift is one work interval, a roster assigns people to shifts, a rotation is the repeating pattern, coverage is the headcount and skills per interval.",
            "Design runs demand forecast, then shift construction (set covering), then rostering under labor constraints.",
            "Rotations run forward - morning to evening to night - because circadian adaptation favors delays over advances (Czeisler et al., 1982).",
            "Constraints include weekly hour caps, minimum rest between shifts, days-off rules, skill mix, and fairness.",
            "Swap and bid workflows trade shifts within the rules and re-validate coverage; relief pools and on-call rotations absorb shocks.",
        ],
        "requirements": [
            "Demand forecasts as required headcount by skill per interval.",
            "Shift templates with start, length, role, and station.",
            "Labor constraint set: hour caps, rest minimums, days-off rules, qualifications, time-off requests.",
            "Rotation patterns encoded as repeating cycles with crew offsets.",
            "Coverage re-validation on every change, plus relief and on-call handling.",
        ],
        "standards": [
            "Shift-design guardrails follow NIOSH Plain Language About Shiftwork (1997).",
            "Forward-rotation preference follows circadian research (Czeisler et al., Science 1982).",
            "Labor law limits (hours, rest, days off) follow the applicable jurisdiction.",
        ],
        "citations": [CIT_NIOSH, CIT_CZEISLER, CIT_PINEDO],
        "sig_lens": (
            "The Signature read: a shift is a covenant of presence - the "
            "worker swears the hours, the operation swears the rest "
            "between. The rotation is the rhythm of the keeping, forward "
            "with the body's own clock. The Signature Scheduling Method "
            "treats coverage as a promise to everyone who depends on the "
            "post being filled, and a schedule that starves its keepers "
            "of rest is an oath the Method refuses to write."
        ),
    },
    {
        "key": "equipment",
        "name": "Equipment Availability and Reservations",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Equipment scheduling promises machine time: the MRI, the CNC "
            "mill, the delivery van, the projector. Each asset has a "
            "calendar of states - available, reserved, in use, in "
            "maintenance, out of service - and a capacity model: some "
            "equipment serves one job at a time, some serves many (a server "
            "cluster, a fleet). Reservations compete with maintenance for "
            "the same hours, so the availability calendar must show both, "
            "with maintenance windows marked unbookable. Setup and teardown "
            "times are part of the reservation, not overhead to discover "
            "later: the 30-minute sterilization after the MRI slot, the "
            "tool change on the mill. Utilization - busy hours over "
            "available hours - is the headline metric, but the honest "
            "version subtracts planned maintenance from available hours "
            "first; otherwise the maintenance you need looks like "
            "idleness you should cut. Check-out and check-in discipline, "
            "condition notes, and late-return policies turn a shared "
            "calendar into a working commons."
        ),
        "how_it_works": (
            "Equipment scheduling works by giving every asset its own "
            "ledger and a state machine. A reservation request names the "
            "asset (or an asset class, letting the system pick), the "
            "interval, and the job; the system checks the interval against "
            "the asset ledger with the overlap test, verifies the requester "
            "is qualified to operate it, and confirms that setup, run, and "
            "teardown all fit inside the requested window. Maintenance "
            "windows are written by the maintenance planner with a "
            "higher-priority state that no reservation can overlap; "
            "emergency breakdowns flip the asset to out-of-service and "
            "notify every downstream reservation holder. Fleets and pools "
            "add an allocation step: the request asks for 'any van', and "
            "the scheduler picks the asset minimizing deadhead time or "
            "balancing mileage. Check-out records custody, check-in "
            "records condition, and the log of both becomes the "
            "utilization and reliability data the maintenance program "
            "feeds on."
        ),
        "key_points": [
            "Each asset carries its own ledger with states: available, reserved, in use, in maintenance, out of service.",
            "Reservations compete with maintenance for the same hours; maintenance windows are higher-priority and unbookable.",
            "Setup and teardown times belong inside the reservation, not discovered later.",
            "Honest utilization subtracts planned maintenance from available hours before dividing.",
            "Fleets add allocation: the scheduler picks which asset serves a class request, minimizing deadhead or balancing wear.",
        ],
        "requirements": [
            "An asset registry with calendars, capacity models, and qualification requirements.",
            "Overlap-checked reservations with setup, run, and teardown inside the booked interval.",
            "Maintenance windows written as higher-priority unbookable states.",
            "Check-out/check-in custody and condition logging.",
            "Utilization reporting net of planned maintenance.",
        ],
        "standards": [
            "Asset and maintenance vocabulary follows ISO 55000:2024.",
            "Maintenance strategy follows reliability-centered maintenance practice (Moubray, 1997).",
        ],
        "citations": [CIT_ISO55000, CIT_MOUBRAY, CIT_RFC5545],
        "sig_lens": (
            "The Signature read: a machine keeps its own covenant of "
            "hours, and the Method will not let bookings steal the hours "
            "owed to its care. The reservation is the oath of use, the "
            "maintenance window the oath of keeping. The Signature "
            "Scheduling Method counts utilization honestly - rest is not "
            "idleness, it is the machine's due."
        ),
    },
    {
        "key": "facilities",
        "name": "Facilities and Room Scheduling",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Room scheduling promises space: the conference room, the "
            "classroom, the operating theater, the loading dock. Rooms are "
            "resources with attributes that must match the meeting - "
            "capacity, layout, projector, video link, accessibility, "
            "acoustic privacy - so booking is a matching problem, not just "
            "a calendar check. The classic failure is the room booked by "
            "title but wrong by attributes: twelve people in a six-person "
            "room, or the confidential review in the glass fishbowl. Good "
            "systems search by requirements first and time second, rank "
            "candidate rooms by fit, and hold the best match tentatively. "
            "Turnover time between bookings - the 15 minutes to clear, "
            "clean, and reset - is scheduled, not hoped for. Recurring "
            "meetings get series treatment with per-instance overrides; "
            "shared spaces get fairness rules so one team cannot colonize "
            "the good rooms. Utilization by room, no-show release (auto-"
            "freeing rooms nobody checked into), and ghost-meeting audits "
            "keep the building honest."
        ),
        "how_it_works": (
            "Room scheduling works as attribute matching plus interval "
            "booking. Each room is a resource record with capacity, "
            "features, layout options, and a calendar. A request states the "
            "interval, headcount, and required features; the system filters "
            "rooms by attributes, then runs the overlap test on each "
            "candidate's calendar including turnover buffers on both ends, "
            "then ranks survivors by fit - closest capacity match, fewest "
            "missing nice-to-haves, nearest location. The booking holds "
            "the winner tentatively, confirms on acceptance, and releases "
            "automatically if nobody checks in within the grace period - "
            "the no-show release that reclaims ghost meetings. Recurring "
            "series expand per the recurrence rules with per-instance "
            "room overrides allowed. Fairness policies cap prime-time "
            "bookings per team per week. Reporting tracks utilization per "
            "room, booking lead times, and the reclaimed hours from "
            "no-show releases, which justify the building's real capacity."
        ),
        "key_points": [
            "Room booking is a matching problem (capacity, features, layout, accessibility) plus a calendar check, not a calendar check alone.",
            "Turnover time between bookings is scheduled; check-in with a grace period plus auto-release reclaims ghost meetings.",
            "Search by requirements first and time second, ranking candidate rooms by fit.",
            "Recurring series allow per-instance room overrides; fairness rules stop one team colonizing prime rooms.",
            "Utilization per room, lead times, and reclaimed no-show hours justify real capacity.",
        ],
        "requirements": [
            "Room records with capacity, features, layout options, and accessibility attributes.",
            "Attribute filtering plus overlap-checked booking with turnover buffers.",
            "Tentative holds, confirmation, and no-show auto-release with check-in.",
            "Recurring series with per-instance overrides.",
            "Fairness caps and utilization reporting.",
        ],
        "standards": [
            "Calendar interchange follows RFC 5545; booking negotiation follows RFC 5546.",
            "Accessibility attributes follow applicable building accessibility codes.",
        ],
        "citations": [CIT_RFC5545, CIT_RFC5546],
        "sig_lens": (
            "The Signature read: a room is a kept space, and the booking "
            "is the oath that it will be ready - right size, right tools, "
            "right quiet. The Signature Scheduling Method matches the "
            "promise to the need before it matches it to the hour, and "
            "releases the ghost meeting so no sworn space stands empty "
            "while another promise waits."
        ),
    },
    {
        "key": "maintenance_windows",
        "name": "Maintenance Windows and Change Control",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A maintenance window is time a resource gives back to itself: "
            "the server taken down for patching, the line stopped for "
            "tooling, the building closed for inspection. Windows are "
            "scheduled with the same rigor as production because they "
            "compete for the same hours - an unplanned outage is just a "
            "maintenance window the equipment scheduled for you. Change "
            "control governs what happens inside the window: which changes "
            "are approved, in what order, with what rollback plan, and "
            "whose sign-off. Standard changes (routine patches) follow "
            "pre-approved templates; normal changes need review; emergency "
            "changes skip the queue but never skip the record. The window "
            "has a change freeze around it - no unrelated changes just "
            "before or after - and a communication plan: who is notified, "
            "when, through what channel. Success is measured by "
            "adherence (did the work fit the window), rollback rate, and "
            "the absence of the 3 AM surprise."
        ),
        "how_it_works": (
            "Maintenance windows work as fenced intervals on the resource "
            "calendar. The planner proposes a window sized from the task "
            "list plus contingency, checks it against production demand "
            "and staffing, and publishes it so every dependent schedule - "
            "reservations, shifts, downstream processes - can plan around "
            "it. Inside the window, the change list executes in dependency "
            "order with a rollback checkpoint after each risky step; the "
            "window stays open until verification passes, and overrun "
            "policy decides whether work continues or rolls back. Change "
            "control classifies each change (standard, normal, emergency), "
            "routes approvals accordingly, and records the full trail: "
            "what changed, who approved, what was tested, what rolled "
            "back. Freeze periods bracket the window. Afterward, the "
            "review asks three questions: did the work fit, did anything "
            "unplanned happen, and what does the next window need to be "
            "bigger or smaller. ITIL 4 codifies this as change enablement "
            "and service validation."
        ),
        "key_points": [
            "A maintenance window is a fenced interval the resource gives back to itself, scheduled with production-grade rigor.",
            "An unplanned outage is a maintenance window the equipment scheduled for you - plan the window or inherit the outage.",
            "Change control classifies changes (standard, normal, emergency) and records what changed, who approved, and what rolled back.",
            "Freeze periods bracket the window; overrun policy decides whether work continues or rolls back.",
            "Success is adherence to the window, low rollback rate, and no unplanned surprises.",
        ],
        "requirements": [
            "Window proposals sized from task lists plus contingency, checked against demand and staffing.",
            "A change list in dependency order with rollback checkpoints after risky steps.",
            "Change classification and approval routing with a complete audit trail.",
            "Freeze periods and a communication plan for every window.",
            "Post-window review feeding the next window's sizing.",
        ],
        "standards": [
            "Change enablement and service validation follow ITIL 4.",
            "Asset maintenance context follows ISO 55000:2024 and RCM practice (Moubray, 1997).",
        ],
        "citations": [CIT_ITIL, CIT_ISO55000, CIT_MOUBRAY],
        "sig_lens": (
            "The Signature read: the maintenance window is the honored "
            "rest - the covenant the keeper makes with the kept thing "
            "itself. The Signature Scheduling Method writes this rest "
            "first, in ink, before any booking dares the hours around it, "
            "for a system that never rests its tools will have its tools "
            "rest it, without asking."
        ),
    },
    {
        "key": "rfc5545",
        "name": "iCalendar RFC 5545: The Interchange Standard",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "RFC 5545, iCalendar, is the reason calendars from different "
            "vendors talk to each other at all. Published in September "
            "2009, edited by Bernard Desruisseaux (obsoleting RFC 2445 "
            "from 1998 by Dawson and Stenerson), it "
            "defines the text format for calendar objects: VCALENDAR "
            "containers holding VEVENT (events), VTODO (tasks), VJOURNAL "
            "(journal entries), VFREEBUSY (availability), and VALARM "
            "(reminders). Properties are NAME:VALUE lines with parameters - "
            "DTSTART:20261017T140000Z, DTSTART;TZID=America/New_York:"
            "20261017T100000 - and long lines fold at 75 octets. The "
            "standard defines recurrence (RRULE), exceptions (EXDATE, "
            "RECURRENCE-ID), time zones (VTIMEZONE), and alarms with "
            "triggers. Its companions complete the system: RFC 5546 "
            "(iTIP) defines the scheduling messages (REQUEST, REPLY, "
            "CANCEL) that negotiate meetings between organizers and "
            "attendees; RFC 4791 (CalDAV) puts calendars on the web for "
            "sync. Every scheduling system in this database either speaks "
            "iCalendar or translates to something that does."
        ),
        "how_it_works": (
            "iCalendar works as a plain-text contract. A VCALENDAR object "
            "opens with BEGIN:VCALENDAR, declares VERSION:2.0 and "
            "PRODID, and contains components. A VEVENT needs UID (globally "
            "unique), DTSTAMP (when created), DTSTART, and either DTEND or "
            "DURATION; it may carry SUMMARY, DESCRIPTION, LOCATION, "
            "ATTENDEE properties with RSVP parameters, ORGANIZER, STATUS, "
            "RRULE, and VALARM subcomponents with TRIGGER offsets like "
            "-PT15M. Parsers unfold lines, split properties from "
            "parameters, and build the event model; serializers do the "
            "reverse with proper folding and escaping (commas, semicolons, "
            "and newlines escaped). Time zones travel as TZID parameters "
            "referencing VTIMEZONE definitions or the IANA database. iTIP "
            "then moves these objects between parties: the organizer "
            "sends REQUEST, attendees answer REPLY with PARTSTAT=ACCEPTED "
            "or DECLINED, changes go as updated REQUESTs with higher "
            "SEQUENCE numbers, cancellations as CANCEL. SEQUENCE plus "
            "DTSTAMP orders concurrent edits - the highest SEQUENCE wins."
        ),
        "key_points": [
            "RFC 5545 (2009, obsoleting RFC 2445) defines the text format: VCALENDAR holding VEVENT, VTODO, VJOURNAL, VFREEBUSY, and VALARM.",
            "A VEVENT needs UID, DTSTAMP, DTSTART, and DTEND or DURATION; properties carry parameters like TZID and RSVP.",
            "RRULE, EXDATE, and RECURRENCE-ID encode recurrence; VTIMEZONE encodes zone rules; VALARM encodes reminders.",
            "RFC 5546 (iTIP) negotiates meetings via REQUEST, REPLY, and CANCEL messages; SEQUENCE plus DTSTAMP orders concurrent edits.",
            "Every scheduling system either speaks iCalendar or translates to something that does.",
        ],
        "requirements": [
            "A parser handling line unfolding, property/parameter splitting, and escaping.",
            "A serializer with 75-octet folding and correct escaping of commas, semicolons, and newlines.",
            "UID generation that is globally unique across all producers.",
            "Recurrence expansion per RFC 5545 Section 3.3.10.",
            "iTIP message handling with SEQUENCE-based conflict ordering.",
        ],
        "standards": [
            "Calendar objects follow RFC 5545; scheduling messages follow RFC 5546; web sync follows RFC 4791 (CalDAV).",
            "Date-time values follow ISO 8601:2019.",
        ],
        "citations": [CIT_RFC5545, CIT_RFC5546, CIT_RFC4791],
        "sig_lens": (
            "The Signature read: iCalendar is the common tongue in which "
            "covenants travel between houses. The Signature Scheduling "
            "Method honors the standard as the treaty that lets every "
            "calendar keep its word to every other - one format, one "
            "oath, understood everywhere."
        ),
    },
    {
        "key": "conflict_detection",
        "name": "Interval Overlap and Conflict Detection",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Conflict detection is the guardian at the ledger's door: it "
            "decides whether a new booking may enter. The core is the "
            "interval overlap test from the foundations record - "
            "start_A < end_B and start_B < end_A - but production "
            "scheduling needs the full machinery around it. Not all "
            "overlaps are conflicts: two tentative holds may coexist, two "
            "confirmed bookings on the same MRI may not, and a maintenance "
            "window conflicts with everything. So each resource carries a "
            "compatibility matrix over states, and detection checks "
            "overlap plus state compatibility. Scale demands indexing: a "
            "naive scan of every interval on a busy resource is too slow, "
            "so systems use interval trees or sorted-interval indexes to "
            "find candidates in logarithmic time. Recurring events expand "
            "before checking; multi-resource bookings check every "
            "resource; and near-miss detection warns on bookings that "
            "touch the buffer zone even when they do not strictly overlap."
        ),
        "how_it_works": (
            "Conflict detection works in four steps. First, normalize the "
            "proposed booking to UTC instants with half-open [start, "
            "end) semantics. Second, query the resource's interval index "
            "for candidates whose ranges intersect the proposal - an "
            "interval tree returns these in O(log n + k) for k hits "
            "instead of scanning all n intervals. Third, apply the "
            "overlap test to each candidate and consult the state "
            "compatibility matrix: confirmed-versus-confirmed is a hard "
            "conflict, tentative-versus-tentative is allowed, anything "
            "versus maintenance-window is a hard conflict. Fourth, check "
            "buffers: a booking ending 5 minutes before the next booking "
            "when the buffer rule demands 15 is a soft conflict - "
            "allowed with a warning or blocked by policy. For recurring "
            "proposals, expand instances across the horizon and check "
            "each; for multi-resource proposals, repeat per resource and "
            "report conflicts grouped by resource. The detector returns a "
            "verdict - clear, soft conflict, or hard conflict - with the "
            "colliding intervals cited, so the booker can negotiate rather "
            "than guess."
        ),
        "key_points": [
            "Detection is overlap test plus state compatibility matrix: not every overlap is a conflict, and maintenance conflicts with everything.",
            "Interval trees find candidate intervals in O(log n + k), replacing naive full scans on busy resources.",
            "Buffers create soft conflicts: touching the buffer zone warns or blocks by policy even without strict overlap.",
            "Recurring proposals expand across the horizon and check every instance; multi-resource proposals check every resource.",
            "The verdict cites the colliding intervals so the booker can negotiate instead of guessing.",
        ],
        "requirements": [
            "Normalized UTC instants with half-open endpoint semantics.",
            "An interval index (interval tree or sorted intervals) per resource.",
            "A state compatibility matrix per resource type.",
            "Buffer rules with soft-versus-hard conflict policy.",
            "Verdicts that cite colliding intervals.",
        ],
        "standards": [
            "Interval relations follow Allen's interval algebra.",
            "State vocabularies align with RFC 5545 event statuses where calendars interchange.",
        ],
        "citations": [CIT_RFC5545, CIT_PINEDO],
        "sig_lens": (
            "The Signature read: conflict detection is the oath-keeper at "
            "the gate. It does not hate the newcomer; it loves the "
            "promises already sworn. The Signature Scheduling Method "
            "teaches the guardian to be swift, exact, and honest - naming "
            "the clash it finds, so the new oath can be spoken elsewhere "
            "rather than broken here."
        ),
    },
    {
        "key": "constraint_satisfaction",
        "name": "Constraint Satisfaction for Scheduling",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Most real scheduling problems are constraint satisfaction "
            "problems: assign values (who, which room, what time) to "
            "variables (the bookings) so that every constraint holds. "
            "Constraints come in three strengths. Hard constraints must "
            "hold or the schedule is invalid: no double-booking, "
            "qualifications, legal rest minimums, room capacity. Soft "
            "constraints should hold and cost something when broken: "
            "preferred days off, back-to-back meeting avoidance, fairness. "
            "Objectives rank the feasible schedules: minimize overtime, "
            "minimize makespan, maximize preference satisfaction. The "
            "solver's toolkit is backtracking search with forward "
            "checking and arc consistency (AC-3), which prunes impossible "
            "values early, plus local search (hill climbing, simulated "
            "annealing) for large instances where proving optimality is "
            "hopeless - and it usually is, because timetabling and "
            "rostering are NP-hard (Garey and Johnson). The discipline "
            "that matters most is constraint modeling: a solver is only "
            "as good as the constraints it is told, and the classic "
            "failure is the unwritten rule ('nobody works the holiday') "
            "living in a manager's head instead of the model."
        ),
        "how_it_works": (
            "Constraint solving works by search plus pruning. Variables "
            "are the decisions (shift S gets worker W), domains are the "
            "allowed values (qualified, available workers), constraints "
            "are the relations that must hold (W's hours stay under the "
            "cap). Backtracking picks an unassigned variable, tries values "
            "in heuristic order (most-constrained variable first, "
            "least-constraining value first), and recurses; when a partial "
            "assignment violates a constraint it backtracks. Forward "
            "checking and arc consistency propagate each choice: assigning "
            "W to the night shift removes W's morning availability "
            "everywhere, and if any variable's domain empties, the solver "
            "backtracks immediately instead of exploring a dead branch. "
            "Soft constraints become penalty terms in the objective, so "
            "the solver trades them off: breaking a preference costs 10, "
            "an overtime hour costs 50, and the search minimizes total "
            "cost. For instances too large for complete search, local "
            "search starts from a greedy schedule and repairs violations "
            "by reassigning variables, accepting sideways or worse moves "
            "to escape local optima. The model - variables, domains, hard "
            "constraints, penalties - is the deliverable; the solver is "
            "interchangeable."
        ),
        "key_points": [
            "Scheduling is constraint satisfaction: assign values to variables so every hard constraint holds, soft constraints cost when broken, objectives rank the feasible.",
            "Backtracking with forward checking and arc consistency prunes dead branches early; most-constrained-variable ordering speeds it further.",
            "Timetabling and rostering are NP-hard, so large instances use local search (hill climbing, simulated annealing) that repairs rather than proves.",
            "Soft constraints become penalty terms: the solver trades a broken preference against an overtime hour by their costs.",
            "The model is the deliverable - the classic failure is the unwritten rule living in a manager's head instead of the model.",
        ],
        "requirements": [
            "Explicit variables, domains, hard constraints, soft-constraint penalties, and objectives.",
            "A solver with backtracking plus propagation for exact solutions on small instances.",
            "A local-search repair solver for large instances.",
            "Constraint capture discipline: every rule written down, none living only in heads.",
            "Solution validation independent of the solver (a checker that re-verifies every constraint).",
        ],
        "standards": [
            "Complexity expectations follow Garey and Johnson (NP-completeness of scheduling problems).",
            "Scheduling theory and notation follow Pinedo (2022).",
        ],
        "citations": [CIT_GAREY, CIT_PINEDO, CIT_GRAHAM],
        "sig_lens": (
            "The Signature read: constraints are the terms of the "
            "covenant written as law - the hours no one may work, the "
            "rest no one may steal, the skill no post may lack. The "
            "Signature Scheduling Method writes every term down, for an "
            "unwritten term is an oath half-sworn, and the solver keeps "
            "only the promises it can see."
        ),
    },
    {
        "key": "rotation_rules",
        "name": "Shift-Rotation Rules and Circadian Planning",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Rotation rules decide how workers move through day, evening, "
            "and night shifts across weeks - and they decide it against "
            "the biology of the human circadian clock. The evidence, from "
            "Czeisler's 1982 field studies onward, favors forward "
            "rotation (morning to evening to night): the body clock "
            "adjusts to phase delays far more easily than phase advances. "
            "Speed matters: fast rotations (1 to 3 days per shift) keep "
            "workers on a day-oriented rhythm with strategic napping, "
            "while slow rotations (3-plus weeks) let the clock actually "
            "adapt to nights - the worst choice is the middle, 4 to 7 "
            "days, too long to stay day-oriented and too short to adapt. "
            "Direction, speed, start times (avoiding 4-6 AM starts that "
            "truncate sleep), consecutive-night limits, and recovery days "
            "after night blocks are the levers. NIOSH adds the operational "
            "guardrails: predictable schedules posted well ahead, worker "
            "input into rotation choice, and overtime kept off the night "
            "shift where fatigue risk peaks. Rotation design is where "
            "scheduling stops being arithmetic and starts being care."
        ),
        "how_it_works": (
            "Rotation design works by encoding the pattern and then "
            "checking it against circadian rules. A pattern like the "
            "2-2-3 (two days, two off, three on, two off, two on, three "
            "off over 14 days) or the DuPont (four 12-hour blocks "
            "rotating across four weeks) is written as a repeating day-"
            "sequence per crew, with each day mapped to a shift type. The "
            "checker scores the pattern: direction penalties for "
            "backward transitions (night to evening), speed classification "
            "(fast, slow, or the penalized middle), consecutive-night "
            "counts against the limit, rest hours between blocks, and "
            "weekend coverage fairness across crews. Forward-rotating "
            "patterns with either fast (2-3 day) or slow (3-week) speeds "
            "score best; backward or mid-speed patterns flag for "
            "redesign. Start times are checked against the sleep-truncation "
            "rule (starts before 6 AM cost sleep), and the whole rotation "
            "is simulated across a full cycle to count nights, weekends, "
            "and recovery days per worker. The output is a pattern plus "
            "its circadian scorecard - the evidence the schedule is not "
            "just covering hours but keeping people whole."
        ),
        "key_points": [
            "Forward rotation (morning to evening to night) follows the circadian clock's preference for phase delays over advances.",
            "Fast rotations (1-3 days) or slow rotations (3+ weeks) beat the middle (4-7 days), which neither preserves day rhythm nor adapts.",
            "Consecutive-night limits, recovery days after night blocks, and avoiding pre-6 AM starts are the core levers.",
            "Patterns like 2-2-3 and DuPont are encoded as repeating day-sequences per crew and scored against circadian rules.",
            "NIOSH guardrails: predictable posting, worker input, overtime kept off nights where fatigue risk peaks.",
        ],
        "requirements": [
            "Rotation patterns encoded as repeating day-sequences per crew.",
            "A circadian scorecard: direction, speed, consecutive nights, rest, start times, recovery days.",
            "Forward-rotation preference and mid-speed avoidance as design rules.",
            "Simulation across a full cycle counting nights, weekends, and recovery days per worker.",
            "Worker input and advance posting in the deployment process.",
        ],
        "standards": [
            "Circadian design follows Czeisler et al. (Science, 1982).",
            "Operational guardrails follow NIOSH Plain Language About Shiftwork (1997).",
        ],
        "citations": [CIT_CZEISLER, CIT_NIOSH],
        "sig_lens": (
            "The Signature read: rotation is the rhythm of the keeping, "
            "and the Method sets it to the body's own drum. A schedule "
            "that breaks its keepers to cover its hours is a covenant "
            "signed in someone else's sleep. The Signature Scheduling "
            "Method rotates forward, rests deeply, and counts the "
            "worker's wholeness as part of the coverage - for the oath "
            "is kept by people, not by hours."
        ),
    },
    {
        "key": "algorithms",
        "name": "Scheduling Algorithms: Greedy, Backtracking, and the Hungarian Method",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Three algorithms carry most practical scheduling. The greedy "
            "algorithm builds a schedule one decision at a time, always "
            "taking the locally best choice - earliest deadline first, "
            "shortest job first - never looking back; it is fast and "
            "often good enough, and for some problems (unit tasks on one "
            "machine by earliest deadline) provably optimal. Backtracking "
            "search explores assignments systematically with pruning, "
            "finding optimal or feasible solutions for constraint problems "
            "small enough to search. The Hungarian method (Kuhn 1955, "
            "refined by Munkres 1957) solves the assignment problem "
            "exactly in cubic time: given n workers and n jobs with a "
            "cost matrix, it finds the minimum-cost one-to-one assignment "
            "- the optimal way to match people to posts, machines to "
            "orders, or rooms to meetings when costs are known. Around "
            "them sit the dispatching rules of the shop floor - SPT "
            "(shortest processing time), EDD (earliest due date), CR "
            "(critical ratio) - simple priority rules that schedule in "
            "real time when optimization cannot wait. Knowing which tool "
            "fits which problem is the algorithmic literacy of scheduling."
        ),
        "how_it_works": (
            "The Hungarian method works by matrix reduction. Start with "
            "the n-by-n cost matrix; subtract each row's minimum from the "
            "row, then each column's minimum from the column, creating "
            "zeros; cover all zeros with the minimum number of lines - if "
            "n lines cover them, an optimal assignment sits on the zeros; "
            "otherwise adjust the matrix by the smallest uncovered value "
            "and repeat. The result is the minimum-cost perfect matching, "
            "found in O(n cubed) time. Greedy scheduling works by sorting "
            "decisions with a priority rule and placing each job in the "
            "earliest feasible slot - earliest-deadline-first is optimal "
            "for unit-length tasks with deadlines on a single machine, a "
            "fact provable by exchange argument. Backtracking assigns "
            "variables in heuristic order and prunes with constraint "
            "propagation, as the constraint record describes. Dispatching "
            "rules run online: when a machine frees, SPT picks the "
            "shortest waiting job (minimizing average flow time), EDD "
            "picks the earliest due date (minimizing maximum lateness), "
            "and the critical ratio (time-to-due divided by processing "
            "time) picks the most urgent. The practitioner matches "
            "problem to tool: assignment to Hungarian, small constrained "
            "problems to backtracking, streaming decisions to dispatching "
            "rules, the rest to greedy plus repair."
        ),
        "key_points": [
            "Greedy builds one locally-best decision at a time; earliest-deadline-first is provably optimal for unit tasks with deadlines on one machine.",
            "Backtracking explores assignments systematically with pruning for small constrained problems.",
            "The Hungarian method (Kuhn 1955, Munkres 1957) finds the minimum-cost one-to-one assignment in O(n^3) time.",
            "Dispatching rules (SPT, EDD, critical ratio) schedule in real time when optimization cannot wait.",
            "Algorithmic literacy is matching problem to tool: assignment to Hungarian, small CSPs to backtracking, streaming to dispatching rules.",
        ],
        "requirements": [
            "A cost or priority model for every assignment decision.",
            "Correctness conditions known per algorithm (when greedy is optimal, when search is complete).",
            "Cubic-time budget awareness for Hungarian on large n (or rectangular variants).",
            "Dispatching-rule selection tied to the objective (flow time, lateness, throughput).",
            "Validation of greedy and heuristic outputs against constraints.",
        ],
        "standards": [
            "Assignment theory follows Kuhn (1955) and Munkres (1957).",
            "Scheduling theory, notation, and complexity follow Pinedo (2022) and Garey and Johnson (1979).",
        ],
        "citations": [CIT_KUHN, CIT_MUNKRES, CIT_PINEDO, CIT_GAREY],
        "sig_lens": (
            "The Signature read: algorithms are the Method's instruments "
            "of fairness - the Hungarian scale weighing every pairing, "
            "the greedy hand placing each promise where it best fits, "
            "the searcher refusing to rest until every term holds. The "
            "Signature Scheduling Method chooses its instrument by the "
            "weight of the oath: the heavier the promise, the truer the "
            "measure."
        ),
    },
    {
        "key": "allocation",
        "name": "Resource Allocation and Bin Packing",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Resource allocation answers 'which resource serves this "
            "demand' when many could: which van takes the route, which "
            "server runs the job, which room hosts the meeting. When "
            "resources are identical, the problem is bin packing - fit "
            "items (jobs with sizes) into the fewest bins (resources with "
            "capacity) - which is NP-hard, so practice uses approximation: "
            "first-fit decreasing (sort jobs largest-first, place each in "
            "the first bin that fits) which guarantees at most 11/9 of "
            "optimal plus one bin. When resources differ, allocation "
            "becomes assignment with costs, solved by the Hungarian "
            "method or by min-cost flow. Load balancing spreads work to "
            "minimize the maximum load (makespan); consolidation packs "
            "work to minimize the number of resources used (saving "
            "energy, staffing, cost). The two goals fight - balance for "
            "speed, pack for economy - and the allocation policy states "
            "which wins. Fragmentation is the enemy: small leftover "
            "capacities no job fits, the scheduling twin of disk "
            "fragmentation, fought with the same weapons - best-fit "
            "placement and periodic defragmentation (re-packing)."
        ),
        "how_it_works": (
            "Allocation works by matching demand items to resource "
            "capacity under a policy. First-fit decreasing sorts jobs by "
            "descending size and places each into the first resource with "
            "room; the sort is what makes it good - large jobs placed "
            "early cannot strand later. Best-fit places each job where it "
            "leaves the smallest remainder, fighting fragmentation. For "
            "heterogeneous resources, each job-resource pair gets a cost "
            "(travel time, setup, skill mismatch penalty) and the "
            "assignment is solved as min-cost flow or Hungarian on the "
            "cost matrix. Load-balancing policies (least-loaded first) "
            "minimize makespan for parallel machines; consolidation "
            "policies (fullest-first) minimize active resources. Online "
            "allocation - jobs arriving over time - cannot reorder, so it "
            "uses the same rules without the sort and accepts the "
            "approximation loss; periodic re-packing (re-optimization "
            "during quiet windows) recovers it. The allocator logs every "
            "placement decision with its reason, because allocation "
            "disputes ('why did my job go to the slow machine') are "
            "settled by the record."
        ),
        "key_points": [
            "Allocation is 'which resource serves this demand'; identical resources make it bin packing, differing resources make it assignment with costs.",
            "First-fit decreasing (largest-first) guarantees at most 11/9 of optimal bins plus one; best-fit fights fragmentation.",
            "Heterogeneous allocation solves as min-cost flow or Hungarian on the job-resource cost matrix.",
            "Load balancing minimizes makespan (speed); consolidation minimizes active resources (economy) - the policy states which wins.",
            "Online allocation cannot reorder arrivals; periodic re-packing during quiet windows recovers the loss.",
        ],
        "requirements": [
            "Job sizes and resource capacities in comparable units.",
            "A stated allocation policy: balance versus consolidate, with the tie-breaking rule.",
            "Cost models for heterogeneous resources (travel, setup, mismatch penalties).",
            "Decision logging so allocation disputes are settled by the record.",
            "Re-packing windows for online allocators.",
        ],
        "standards": [
            "Complexity expectations follow Garey and Johnson (bin packing NP-hard).",
            "Assignment foundations follow Kuhn (1955) and Munkres (1957).",
        ],
        "citations": [CIT_GAREY, CIT_KUHN, CIT_MUNKRES],
        "sig_lens": (
            "The Signature read: allocation is the Method's justice - "
            "every demand weighed, every resource honored, none "
            "overburdened while another stands idle unless the covenant "
            "says economy over speed. The Signature Scheduling Method "
            "places each load where it belongs and writes down why, for "
            "a burden assigned without reason is an oath without a "
            "witness."
        ),
    },
    {
        "key": "queueing",
        "name": "Queueing Theory for Service Capacity",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Queueing theory sizes service capacity: how many agents, "
            "lanes, or machines keep waits tolerable. The foundation is "
            "Little's Law (1961): L = lambda W - the average number in "
            "the system equals the arrival rate times the average time in "
            "the system, true for every queue no matter the details. The "
            "workhorse model is Erlang C (1917): Poisson arrivals, "
            "exponential service times, c servers, infinite queue - it "
            "computes the probability a caller waits and the average wait, "
            "which is how call centers and clinics staff to a service "
            "level like '80 percent answered in 20 seconds'. The brutal "
            "lesson is nonlinearity: at 90 percent utilization, waits "
            "explode - small demand spikes create long queues because "
            "there is no spare capacity to absorb them. So capacity plans "
            "target utilization bands (often 70 to 85 percent for human "
            "services), and scheduling smooths arrivals with appointments "
            "instead of letting them bunch. Kleinrock's 1975 treatment "
            "remains the canonical reference for the mathematics."
        ),
        "how_it_works": (
            "Queueing capacity planning works from arrival and service "
            "statistics. Measure the arrival rate lambda (customers per "
            "hour) and the mean service time (so the service rate mu is "
            "its reciprocal); the offered load is a = lambda / mu "
            "erlangs. For c servers, utilization rho = a / c must stay "
            "below 1 or the queue grows without bound. Erlang C computes "
            "the wait probability from a and c via the Erlang C formula, "
            "then the average wait follows; planners try c = 1, 2, 3... "
            "until the wait meets the service-level target. Little's Law "
            "cross-checks everything: count the average queue length L, "
            "divide by lambda, and you must get the measured average wait "
            "W - if not, the measurements are wrong. Scheduling enters as "
            "arrival shaping: appointments convert random arrivals into "
            "planned ones, cutting the variability that Erlang assumes "
            "away, which is why a booked clinic outperforms a walk-in "
            "clinic at the same staffing. The plan states the target "
            "utilization band explicitly, because running at 95 percent "
            "'efficiency' is just a queue with a payroll."
        ),
        "key_points": [
            "Little's Law (L = lambda W) holds for every queue: average number in system equals arrival rate times average time in system.",
            "Erlang C (1917) computes wait probability and average wait for Poisson arrivals and exponential service with c servers.",
            "Waits explode nonlinearly near full utilization; capacity plans target bands like 70-85 percent for human services.",
            "Appointments shape arrivals, cutting the variability that queueing models assume - booked beats walk-in at equal staffing.",
            "Running at 95 percent 'efficiency' is a queue with a payroll; the plan must state its utilization band.",
        ],
        "requirements": [
            "Measured arrival rates and service-time distributions per service.",
            "An Erlang C (or appropriate model) staffing calculation against a stated service-level target.",
            "A target utilization band, not a maximization goal.",
            "Arrival shaping (appointments, staggering) where walk-in bunching is the problem.",
            "Little's Law cross-checks on measured queue data.",
        ],
        "standards": [
            "Queueing mathematics follow Kleinrock (1975); Little's Law follows Little (1961); Erlang C follows Erlang (1917).",
        ],
        "citations": [CIT_LITTLE, CIT_ERLANG, CIT_KLEINROCK],
        "sig_lens": (
            "The Signature read: the queue is where promises wait to be "
            "kept, and the Method refuses to make the waiting endless. "
            "Little's Law is the covenant's arithmetic - what arrives "
            "must be served, and the waiting is the measure of the "
            "keeping. The Signature Scheduling Method staffs for the "
            "wait it is willing to ask of people, and not one soul more "
            "in line than honor allows."
        ),
    },
    {
        "key": "buffers",
        "name": "Lead Times, Setup, and Teardown Buffers",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Buffers are scheduled slack - time deliberately left empty so "
            "reality fits. Setup time prepares the resource (tool change, "
            "room reset, sterilization); teardown restores it afterward; "
            "lead time is the gap between ordering and availability. "
            "Goldratt's Theory of Constraints made buffers a science: "
            "protect the bottleneck's schedule with a time buffer of "
            "work-in-waiting, because a bottleneck starved for work loses "
            "throughput the whole system can never recover. There are "
            "three buffer kinds: capacity buffers (idle time held in "
            "reserve), time buffers (gaps between bookings), and stock "
            "buffers (inventory before the constraint). Sizing is the art: "
            "too thin and every hiccup cascades; too fat and the schedule "
            "is mostly waiting. The statistical answer sizes buffers from "
            "variability - the standard deviation of setup times, the "
            "historical lateness distribution - not from gut feel. "
            "Buffers are not inefficiency; they are the insurance premium "
            "a schedule pays against the certainty of variation."
        ),
        "how_it_works": (
            "Buffer management works by naming every gap and sizing it "
            "from data. Each booking records three intervals: setup, "
            "execution, teardown; the scheduler places all three, so a "
            "60-minute appointment with 10-minute setup and 10-minute "
            "teardown occupies 80 minutes of the resource. Lead times "
            "enter as constraints: the booking must precede the need by "
            "at least the lead time, which the system enforces at booking "
            "(no same-day bookings when the lead time is 48 hours). "
            "Bottleneck protection pools a time buffer of ready work "
            "before the constraint resource, sized to cover the "
            "variability of upstream arrivals - typically sized from the "
            "measured standard deviation of inter-arrival gaps times a "
            "safety factor. The schedule monitors buffer penetration: "
            "how much of each buffer the day's variation has consumed, "
            "reported green/yellow/red so managers see trouble while "
            "there is still buffer left to spend. When buffers chronically "
            "run red, the answer is not bigger buffers but less "
            "variability upstream - the buffer report is a diagnostic, "
            "not just a cushion."
        ),
        "key_points": [
            "Buffers are scheduled slack: setup prepares, teardown restores, lead time separates ordering from availability.",
            "Goldratt's Theory of Constraints protects the bottleneck with a time buffer, because starved bottleneck time is lost forever.",
            "Three kinds: capacity buffers (idle reserve), time buffers (gaps), stock buffers (inventory before the constraint).",
            "Size buffers from measured variability (standard deviations, lateness distributions), not gut feel.",
            "Buffer penetration reporting (green/yellow/red) turns the cushion into an early-warning diagnostic.",
        ],
        "requirements": [
            "Setup, execution, and teardown recorded as separate intervals on every booking.",
            "Lead-time rules enforced at booking time.",
            "Bottleneck identification and a sized time buffer before it.",
            "Buffer penetration monitoring with green/yellow/red thresholds.",
            "Periodic buffer review: chronic red means fix upstream variability, not just grow buffers.",
        ],
        "standards": [
            "Buffer and constraint practice follows Goldratt, The Goal (2004).",
            "Project buffer concepts align with PMBOK Guide 7th edition scheduling.",
        ],
        "citations": [CIT_GOLDRATT, CIT_PMBOK],
        "sig_lens": (
            "The Signature read: the buffer is the covenant's mercy - "
            "time set aside so that when reality stumbles, the promise "
            "need not fall. The Signature Scheduling Method pays this "
            "insurance gladly and sizes it honestly from the record of "
            "stumbles past, for a promise without margin is a promise "
            "half-made."
        ),
    },
    {
        "key": "multi_resource",
        "name": "Multi-Resource and Team Scheduling",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Real work needs several resources at once: the surgery needs "
            "the surgeon, the anesthesiologist, the room, and the "
            "equipment; the install needs two technicians and the van. "
            "Multi-resource scheduling books a bundle atomically - all "
            "resources for the interval, or none - because a surgery with "
            "three of four resources is not a surgery. The hard part is "
            "rendezvous: each resource has its own calendar, and the "
            "booking must find an interval free on all of them "
            "simultaneously, honoring each one's buffers and constraints. "
            "Teams add skill-mix constraints (at least one senior tech), "
            "co-location (both techs at the same site), and sequence "
            "(the inspector after the installer, not before). The "
            "combinatorial cost grows fast: checking k resources across "
            "a horizon is k interval queries plus a rendezvous search, "
            "and naive approaches miss the narrow windows where all "
            "calendars align. The professional answer models the bundle "
            "as one booking with resource roles, searches free-time "
            "intersection across the ledgers, and holds all resources "
            "tentatively until every role confirms - then commits the "
            "bundle as one transaction."
        ),
        "how_it_works": (
            "Multi-resource booking works as intersect-then-commit. The "
            "request names the bundle: roles (surgeon, room, device), each "
            "with its resource class and constraints, plus the interval "
            "length and buffers. The scheduler computes free intervals "
            "per role from each candidate resource's ledger, intersects "
            "them to find windows free for every role at once, and ranks "
            "the windows by policy (earliest, least disruption, preferred "
            "team). It then places tentative holds on the chosen resource "
            "for each role - all holds sharing one bundle identifier - "
            "and validates the bundle constraints: skill mix, "
            "co-location, sequencing against other bundles. If every role "
            "validates, the bundle commits atomically: all holds become "
            "bookings in one transaction, so a crash mid-commit cannot "
            "leave half a surgery booked. If any role fails, all holds "
            "release and the scheduler tries the next window. "
            "Rescheduling a bundle moves or cancels all members together, "
            "and the audit trail records the bundle as one promise with "
            "many keepers."
        ),
        "key_points": [
            "Multi-resource work books a bundle atomically - all resources for the interval, or none; three of four resources is not a surgery.",
            "Rendezvous is the hard part: find an interval free on every resource's calendar simultaneously, honoring each one's buffers.",
            "Teams add skill-mix, co-location, and sequencing constraints across the bundle.",
            "The scheduler intersects free-time across ledgers, holds all roles tentatively under one bundle ID, then commits atomically.",
            "Rescheduling moves or cancels bundle members together; the audit trail records one promise with many keepers.",
        ],
        "requirements": [
            "Bundle definitions: roles, resource classes, per-role constraints, interval length, buffers.",
            "Free-time intersection across multiple resource ledgers.",
            "Tentative holds sharing one bundle identifier with atomic commit.",
            "Bundle-level constraints: skill mix, co-location, sequencing.",
            "Bundle-aware reschedule and cancel with a unified audit trail.",
        ],
        "standards": [
            "Calendar interchange for bundle members follows RFC 5545; negotiation follows RFC 5546.",
            "Scheduling theory follows Pinedo (2022).",
        ],
        "citations": [CIT_RFC5545, CIT_RFC5546, CIT_PINEDO],
        "sig_lens": (
            "The Signature read: some oaths need many keepers, and the "
            "Method binds them as one. The bundle is a covenant with "
            "several signatures - surgeon, room, device - and it is "
            "sealed whole or not at all. The Signature Scheduling "
            "Method gathers every keeper to the same hour and commits "
            "them together, for a promise kept in pieces is a promise "
            "in peril."
        ),
    },
    {
        "key": "sync",
        "name": "Calendar Synchronization: CalDAV and Federation",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Synchronization keeps calendars true across devices and "
            "organizations: the phone, the laptop, and the office server "
            "must agree. CalDAV (RFC 4791) is the open standard: calendars "
            "live as WebDAV collections on a server, and clients sync "
            "with REPORT queries, discovering changes via sync tokens "
            "(ctag/sync-token) so each sync fetches only what changed. "
            "Scheduling between organizations runs on iTIP (RFC 5546) over "
            "email or CalDAV scheduling extensions: the organizer's "
            "server sends REQUEST, attendees reply, and free/busy lookups "
            "(VFREEBUSY) let an organizer find a slot without seeing "
            "private details. Federation - hospitals sharing on-call "
            "calendars, contractors sharing crew calendars - adds "
            "trust: which fields cross the boundary (free/busy always, "
            "summaries sometimes, details rarely) and whose server is "
            "authoritative for each calendar. Conflict handling follows "
            "the iCalendar rules: higher SEQUENCE wins, ties broken by "
            "DTSTAMP. The failure modes are classic distributed systems "
            "problems - split-brain edits, clock skew, lost updates - "
            "solved by the standard's ordering rules, not by hoping."
        ),
        "how_it_works": (
            "CalDAV sync works as change tracking. The client stores a "
            "sync token per calendar; on sync it sends the token, and "
            "the server returns only added, changed, and deleted objects "
            "since that token, plus a new token. The client applies them "
            "to its local store - last-writer-wins by SEQUENCE/DTSTAMP "
            "for concurrent edits to the same event - and uploads its "
            "own changes with If-Match etags so conflicting uploads are "
            "rejected rather than silently merged. Cross-organization "
            "scheduling works through the organizer: its server expands "
            "attendee free/busy via VFREEBUSY requests, proposes a time "
            "by iTIP REQUEST, and processes REPLY messages into the "
            "event's attendee statuses. Federation agreements define the "
            "visibility matrix per shared calendar (free/busy only, "
            "summaries, or full detail) and the authoritative server per "
            "calendar; every federated write carries its origin so "
            "loops are detected. Sync health is monitored by token age, "
            "conflict rates, and divergence alarms when two replicas "
            "disagree past the ordering rules."
        ),
        "key_points": [
            "CalDAV (RFC 4791) syncs via sync tokens: each sync fetches only what changed since the last token.",
            "Cross-organization scheduling runs on iTIP (RFC 5546): REQUEST, REPLY, free/busy lookups without exposing private details.",
            "Federation adds a visibility matrix per shared calendar and a declared authoritative server per calendar.",
            "Concurrent edits resolve by SEQUENCE, ties by DTSTAMP - the standard's ordering rules, not hope.",
            "Uploads use etags with If-Match so conflicting writes are rejected rather than silently merged.",
        ],
        "requirements": [
            "CalDAV server and clients with sync-token change tracking.",
            "iTIP handling for cross-organization REQUEST/REPLY/CANCEL.",
            "A federation visibility matrix and authoritative-server declarations.",
            "SEQUENCE/DTSTAMP ordering on every edit path.",
            "Sync health monitoring: token age, conflict rates, divergence alarms.",
        ],
        "standards": [
            "Web calendar sync follows RFC 4791 (CalDAV); contact sync follows RFC 6352 (CardDAV).",
            "Scheduling messages follow RFC 5546; objects follow RFC 5545.",
        ],
        "citations": [CIT_RFC4791, CIT_RFC5546, CIT_RFC5545, CIT_RFC6352],
        "sig_lens": (
            "The Signature read: when covenants travel between houses, "
            "the Method demands they arrive unchanged. Synchronization "
            "is the oath carried faithfully across every device and "
            "every boundary - the same promise, the same hour, on the "
            "phone and the server and the partner's wall. The Signature "
            "Scheduling Method trusts the standard's ordering the way "
            "it trusts a witness: SEQUENCE for the word, DTSTAMP for "
            "the hour it was spoken."
        ),
    },
    {
        "key": "preventive",
        "name": "Preventive Maintenance Scheduling",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Preventive maintenance (PM) schedules care before failure: "
            "inspections, lubrication, calibration, and part replacement "
            "at fixed intervals. The triggers are four: calendar time "
            "(every 90 days), usage (every 500 operating hours), "
            "condition (vibration exceeds the threshold), and opportunity "
            "(the line is down anyway). Each PM task carries a frequency, "
            "a duration, required skills and parts, and a tolerance "
            "window - the plus-or-minus days inside which the task may "
            "float to fit production. Reliability-centered maintenance "
            "(RCM, Moubray 1997) chooses the task by failure mode: "
            "age-related failures get time-based PM, random failures get "
            "condition monitoring or redesign, and hidden failures get "
            "failure-finding inspections. The PM calendar is a recurring-"
            "event system with teeth: overdue tasks escalate, skipped "
            "tasks need documented justification, and completion feeds "
            "the reliability record. The economics are the justification: "
            "planned work costs a fraction of unplanned work, and the PM "
            "schedule is where that fraction is captured."
        ),
        "how_it_works": (
            "PM scheduling works as a trigger-evaluation loop. Every "
            "asset carries PM plans, each naming the trigger (calendar "
            "interval, meter reading, condition threshold), the task "
            "list, duration, skills, and parts. A scheduler evaluates "
            "triggers continuously: calendar triggers expand like "
            "recurring events with tolerance windows; meter triggers "
            "fire when the odometer crosses the threshold; condition "
            "triggers fire from monitoring data. Due tasks enter the "
            "planning backlog, get prioritized against production "
            "demand, and are placed into maintenance windows honoring "
            "the tolerance float - a 90-day task with plus-or-minus 10 "
            "days can slide to the next planned stop. Parts are "
            "kitted before the window; skills are matched to the task; "
            "completion records actuals (time, findings, measurements) "
            "back to the asset history. Overdue tasks escalate by age "
            "and criticality, and the compliance report shows "
            "completion rate by asset class - the number auditors ask "
            "for first."
        ),
        "key_points": [
            "PM triggers are four: calendar time, usage meters, condition thresholds, and opportunity windows.",
            "Each PM task carries frequency, duration, skills, parts, and a tolerance window it may float within.",
            "RCM (Moubray 1997) matches the task to the failure mode: age-related gets time-based PM, random gets monitoring or redesign.",
            "Overdue tasks escalate; skipped tasks need documented justification; completion feeds the reliability record.",
            "Planned work costs a fraction of unplanned work - the PM schedule captures that fraction.",
        ],
        "requirements": [
            "PM plans per asset with trigger, task list, duration, skills, parts, and tolerance window.",
            "Continuous trigger evaluation across calendar, meter, and condition sources.",
            "Backlog prioritization against production demand with tolerance-float placement.",
            "Parts kitting and skill matching before the window.",
            "Completion actuals recorded to asset history plus compliance reporting.",
        ],
        "standards": [
            "Maintenance strategy follows RCM practice (Moubray, 1997).",
            "Asset management context follows ISO 55000:2024.",
        ],
        "citations": [CIT_MOUBRAY, CIT_ISO55000],
        "sig_lens": (
            "The Signature read: preventive care is the covenant kept "
            "before it is tested - the oath honored in quiet times so "
            "it holds in hard ones. The Signature Scheduling Method "
            "writes maintenance before failure writes it, floats the "
            "task within its tolerance like a promise with room to "
            "breathe, and records every keeping in the asset's own "
            "history."
        ),
    },
    {
        "key": "sla",
        "name": "Downtime Windows and Availability SLAs",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "An availability SLA is a promise about uptime stated as a "
            "number: 99.9 percent ('three nines') allows 43.8 minutes of "
            "downtime per month; 99.99 percent allows 4.38 minutes. "
            "Planned downtime inside agreed windows usually does not "
            "count against the SLA; unplanned downtime always does - "
            "which is why maintenance windows are negotiated into "
            "contracts. The mathematics underneath are MTBF (mean time "
            "between failures) and MTTR (mean time to repair): "
            "availability = MTBF / (MTBF + MTTR). Raising MTBF means "
            "reliability engineering; cutting MTTR means spares, "
            "procedures, and practiced recovery. Error budgets turn the "
            "SLA into a spending allowance: a 99.9 percent service gets "
            "43.8 minutes of budget per month to spend on changes and "
            "risk, and when the budget is gone, changes wait. Scheduling "
            "is the delivery mechanism: windows placed where demand is "
            "lowest, changes batched into windows to spend budget "
            "efficiently, and freeze periods protecting the busiest "
            "hours. ITIL 4 frames this as availability management inside "
            "service level management."
        ),
        "how_it_works": (
            "SLA scheduling works from the budget down. The contract "
            "states the availability target and the window policy "
            "(which hours are eligible, how much notice, whose approval). "
            "Each month the error budget is computed from the target; "
            "every incident and every change spends from it; monitoring "
            "tracks burn rate so teams see the budget depleting before "
            "it is gone. Maintenance windows are proposed inside "
            "eligible hours, sized from the change plan plus rollback "
            "time, and approved only if the remaining budget covers the "
            "planned risk. Demand analysis picks the cheapest hours - "
            "the 2 AM Sunday window costs the business less than the "
            "2 PM Tuesday one. MTBF and MTTR are tracked per service "
            "from incident records: falling MTBF triggers reliability "
            "work, rising MTTR triggers recovery drills and spares "
            "review. When the budget hits zero, the change freeze "
            "engages automatically - no manual heroics needed, the "
            "arithmetic simply says stop. The monthly review reconciles "
            "budget spent against value shipped."
        ),
        "key_points": [
            "99.9 percent allows 43.8 downtime minutes per month; 99.99 percent allows 4.38 - the nines are a budget, not a boast.",
            "Planned windows usually do not count against the SLA; unplanned downtime always does.",
            "Availability = MTBF / (MTBF + MTTR): raise MTBF with reliability work, cut MTTR with spares and practiced recovery.",
            "Error budgets convert the SLA into spendable minutes; when the budget is gone, changes wait.",
            "Windows go in the cheapest demand hours; the monthly review reconciles budget spent against value shipped.",
        ],
        "requirements": [
            "A contracted availability target with window policy (eligible hours, notice, approval).",
            "Monthly error-budget computation with burn-rate monitoring.",
            "Window approval gated on remaining budget.",
            "MTBF/MTTR tracking per service from incident records.",
            "Automatic change freeze at zero budget with monthly reconciliation.",
        ],
        "standards": [
            "Availability and service-level practice follow ITIL 4.",
            "Reliability prediction conventions follow MIL-HDBK-217F lineage for MTBF/MTTR vocabulary.",
        ],
        "citations": [CIT_ITIL],
        "sig_lens": (
            "The Signature read: the SLA is the covenant with a number "
            "on it - uptime sworn and measured. The error budget is the "
            "Method's honesty made arithmetic: so many minutes of risk "
            "may be spent, and not one more, until the ledger is "
            "renewed. The Signature Scheduling Method spends its budget "
            "where the promise costs least and freezes where the "
            "promise costs most."
        ),
    },
    {
        "key": "stochastic",
        "name": "Scheduling Under Uncertainty: Stochastic Models",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Deterministic schedules pretend task durations are known; "
            "stochastic scheduling admits they are random variables. "
            "PERT (1958) was the first famous attempt: each activity "
            "gets optimistic, most-likely, and pessimistic estimates, "
            "combined as (O + 4M + P) / 6 with variance ((P - O) / 6) "
            "squared, and the project duration becomes a distribution "
            "along the critical path. Monte Carlo simulation generalizes "
            "it: sample every task's duration from its distribution "
            "thousands of times, schedule each sample, and read off the "
            "probability of finishing by any date - '87 percent chance "
            "by June 1' beats any single date. Stochastic models also "
            "cover uncertain arrivals (Poisson), random breakdowns "
            "(exponential up-times), and no-shows (Bernoulli per "
            "appointment) - the overbooking model that keeps clinics "
            "full is a stochastic schedule. The discipline's rule: "
            "never present a point estimate without its spread, and "
            "never commit a date without stating its confidence."
        ),
        "how_it_works": (
            "Stochastic scheduling works by replacing durations with "
            "distributions and computing with them. Each task gets a "
            "three-point estimate or a fitted distribution (lognormal "
            "for task times, exponential for failure inter-arrivals); "
            "Monte Carlo draws one sample per task per trial, runs the "
            "ordinary deterministic scheduler (critical path, resource "
            "leveling) on the sampled durations, and records the trial's "
            "finish date and cost. After thousands of trials, the "
            "empirical distribution yields P50 and P90 dates, the "
            "probability of hitting the target, and - by correlating "
            "task samples with late finishes - the tasks most likely "
            "to drive lateness (schedule sensitivity). Overbooking "
            "models set the booking level where expected show-ups match "
            "capacity: with no-show probability p per slot, book n slots "
            "so that n(1-p) equals capacity, hedging with the binomial "
            "distribution. Robust scheduling goes further, optimizing "
            "the schedule that performs best across the distribution "
            "rather than best at the mean. The output is always a "
            "distribution and a confidence, never a naked date."
        ),
        "key_points": [
            "Stochastic scheduling replaces known durations with random variables; PERT's (O + 4M + P)/6 was the first famous attempt.",
            "Monte Carlo samples every task's distribution thousands of times and reads finish-date probabilities off the trials.",
            "Report P50/P90 dates and hit probability - never a point estimate without its spread, never a date without confidence.",
            "Overbooking models use the binomial no-show distribution to book past capacity to expected show-ups.",
            "Schedule sensitivity analysis names the tasks most likely to drive lateness.",
        ],
        "requirements": [
            "Duration distributions per task (three-point estimates or fitted distributions).",
            "A Monte Carlo engine running the deterministic scheduler per trial.",
            "P50/P90 reporting with hit probabilities and sensitivity analysis.",
            "No-show and breakdown distributions where arrivals and failures are random.",
            "Confidence stated on every committed date.",
        ],
        "standards": [
            "PERT foundations follow Malcolm et al. (Operations Research, 1959).",
            "Project scheduling practice follows the PMBOK Guide 7th edition.",
        ],
        "citations": [CIT_PERT, CIT_PMBOK, CIT_KELLEY],
        "sig_lens": (
            "The Signature read: the Method does not pretend to know "
            "the unknowable - it swears honestly. A date with a "
            "confidence is an oath with its weight stated; a naked date "
            "is a guess wearing a promise's clothes. The Signature "
            "Scheduling Method samples the thousand possible futures "
            "and speaks only what most of them agree on."
        ),
    },
    {
        "key": "linear_programming",
        "name": "Linear Programming for Workforce Scheduling",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Linear programming (LP) turns workforce scheduling into "
            "mathematics: minimize cost subject to coverage constraints. "
            "Decision variables say how many workers of each type work "
            "each shift; the objective sums wages, overtime premiums, "
            "and penalty costs; constraints demand coverage per interval "
            "(headcount at least demand), honor labor rules (max hours, "
            "rest), and respect availability. When variables must be "
            "whole people, it becomes integer linear programming (ILP) - "
            "NP-hard in general, but modern solvers (branch and bound "
            "with cutting planes) handle real rosters. The LP relaxation "
            "(allowing fractional people) gives a lower bound that "
            "proves how close a schedule is to optimal. Set covering is "
            "the classic formulation: choose shifts from a candidate "
            "set so every demand interval is covered at minimum cost. "
            "Column generation builds the candidate shifts on the fly "
            "for huge problems like airline crew scheduling. LP does not "
            "replace the rosterer's judgment - it gives the judgment a "
            "provably good starting point and a certificate of quality."
        ),
        "how_it_works": (
            "Workforce LP works by declaring the model and letting the "
            "solver optimize. Variables x[s,t] count workers of skill s "
            "on shift t; the objective minimizes sum of cost[s,t] * "
            "x[s,t] plus overtime and penalty terms. Constraints: for "
            "each interval i and skill s, sum of x over shifts covering "
            "i meets demand[i,s]; each worker's weekly hours stay within "
            "[min, max]; rest constraints forbid illegal adjacencies; "
            "availability zeroes out forbidden assignments. The solver "
            "first tries the LP relaxation; if the solution is integral "
            "it is optimal, otherwise branch-and-bound splits on "
            "fractional variables and cutting planes tighten the "
            "relaxation until integrality or the time budget. Set "
            "covering formulates over candidate shifts: binary variable "
            "per candidate, cover-every-interval constraints, minimize "
            "cost. The gap between the integer solution and the LP "
            "bound is reported as the optimality certificate - 'within "
            "2 percent of provable optimal'. Sensitivity analysis on "
            "the LP then answers 'what if demand rises 10 percent' by "
            "re-solving, giving the marginal cost of coverage."
        ),
        "key_points": [
            "LP minimizes staffing cost subject to coverage, labor-rule, and availability constraints; whole people make it integer LP.",
            "The LP relaxation gives a lower bound - the optimality certificate proving how close a schedule is to perfect.",
            "Set covering is the classic formulation: pick minimum-cost candidate shifts covering every demand interval.",
            "Column generation builds candidate shifts on the fly for huge problems like crew scheduling.",
            "Sensitivity analysis re-solves for demand changes, giving the marginal cost of coverage.",
        ],
        "requirements": [
            "Demand by skill per interval, shift candidates with costs, and labor rules as linear constraints.",
            "An ILP-capable solver (branch and bound with cutting planes).",
            "Optimality-gap reporting on every solved roster.",
            "Set-covering or column-generation formulation for large instances.",
            "Sensitivity runs for demand scenarios.",
        ],
        "standards": [
            "Optimization theory and scheduling notation follow Pinedo (2022) and Graham et al. (1979).",
        ],
        "citations": [CIT_PINEDO, CIT_GRAHAM],
        "sig_lens": (
            "The Signature read: linear programming is the covenant "
            "weighed on true scales - every hour priced, every post "
            "covered, nothing wasted, nothing wanting. The Signature "
            "Scheduling Method lets the solver find the cheapest faithful "
            "keeping, then certifies its faithfulness with the bound, "
            "for economy without proof is just hope with arithmetic."
        ),
    },
    {
        "key": "timetabling",
        "name": "Timetabling by Graph Coloring",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Timetabling - exams, classes, conference sessions - is graph "
            "coloring in disguise. Make each event a vertex; draw an edge "
            "between events that share a student, teacher, or room and "
            "therefore cannot coincide; then a valid timetable is a "
            "coloring where adjacent vertices differ, each color a time "
            "slot. The chromatic number is the minimum slots needed, and "
            "finding it is NP-hard - but greedy coloring ordered by "
            "decreasing degree (largest-first) is fast and usually close. "
            "de Werra's 1985 survey founded the modern treatment, "
            "extending coloring to edge coloring for teacher-class "
            "timetables and to list coloring when events allow only "
            "certain slots. Real timetables add soft constraints: spread "
            "a student's exams (no two in one day), avoid early Monday "
            "lectures, balance room usage. The pipeline is color first "
            "for feasibility, then local search to polish soft "
            "constraints - feasibility is the promise, polish is the "
            "grace."
        ),
        "how_it_works": (
            "Timetabling by coloring works in two phases. Phase one "
            "builds the conflict graph: vertices are events, edges join "
            "events sharing any resource that cannot be in two places at "
            "once. Greedy coloring orders vertices by decreasing degree "
            "(breaking ties by enrollment size) and assigns each the "
            "lowest-numbered color not used by its neighbors - each color "
            "is a time slot, and the result is a feasible timetable "
            "using at most max-degree-plus-one slots. Phase two improves "
            "it: local search (tabu search, simulated annealing) moves "
            "events between slots to satisfy soft constraints - exam "
            "spreading, lecturer preferences, room stability - scoring "
            "each timetable by weighted penalty. List coloring handles "
            "restricted availability: each event carries its allowed "
            "slots and the greedy pass picks within the list. Edge "
            "coloring variants schedule teacher-class pairs where both "
            "endpoints are resources. The final timetable ships with its "
            "conflict graph and penalty score, so next term's scheduler "
            "inherits the model, not just the answer."
        ),
        "key_points": [
            "Timetabling is graph coloring: events are vertices, conflicts are edges, time slots are colors; adjacent vertices must differ.",
            "Greedy largest-first coloring is fast, feasible, and uses at most max-degree-plus-one slots; the chromatic number is NP-hard.",
            "de Werra (1985) founded the modern treatment, including edge coloring for teacher-class timetables.",
            "Phase two polishes with local search against soft constraints: exam spreading, preferences, room stability.",
            "List coloring restricts events to allowed slots; the model ships with the timetable for next term.",
        ],
        "requirements": [
            "A conflict graph built from shared students, teachers, and rooms.",
            "Greedy coloring for a feasible base timetable.",
            "Local-search polishing against weighted soft constraints.",
            "List-coloring support for restricted availability.",
            "The model (graph plus penalties) archived with the timetable.",
        ],
        "standards": [
            "Timetabling theory follows de Werra (European Journal of Operational Research, 1985).",
            "Complexity expectations follow Garey and Johnson.",
        ],
        "citations": [CIT_DEWERRA, CIT_GAREY, CIT_PINEDO],
        "sig_lens": (
            "The Signature read: the timetable is many covenants woven "
            "without tangling - no student in two rooms at once, no "
            "teacher split in two. Graph coloring is the Method's "
            "weaving: each promise its own hour, no two sworn "
            "against each other. The Signature Scheduling Method colors "
            "first for faithfulness, then polishes for grace."
        ),
    },
    {
        "key": "job_shop",
        "name": "Job-Shop Scheduling and Makespan",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Job-shop scheduling runs a factory of promises: n jobs, each "
            "a fixed sequence of operations on specific machines, all "
            "competing for machine time. The objective is usually makespan "
            "(C_max) - the time the last job finishes - though flow time, "
            "lateness, and tardiness matter too; Graham's three-field "
            "notation (alpha|beta|gamma) names every variant precisely, "
            "like J||C_max for the job shop minimizing makespan. The "
            "problem is NP-hard even for small shops (Garey and Johnson), "
            "so practice uses dispatching rules (SPT, EDD, most work "
            "remaining), shifting-bottleneck heuristics that sequence the "
            "worst machine first, and metaheuristics (tabu search, genetic "
            "algorithms) for the final squeeze. The Gantt chart (Gantt, "
            "1913) is the native visualization: machines on the vertical "
            "axis, time horizontal, each operation a bar - the schedule "
            "you can see is the schedule you can defend. Critical-path "
            "thinking (Kelley and Walker, 1959) identifies the operation "
            "chain whose delay delays everything."
        ),
        "how_it_works": (
            "Job-shop scheduling works by sequencing operations per "
            "machine. Each job's operations have fixed machine assignments "
            "and processing times plus precedence (operation 2 after "
            "operation 1). The shifting-bottleneck heuristic solves it "
            "machine by machine: solve each unscheduled machine as a "
            "single-machine problem given current release dates and due "
            "dates, pick the machine with the worst lateness (the "
            "bottleneck), fix its sequence, re-optimize the rest, and "
            "repeat - each pass can re-sequence earlier machines as "
            "bottlenecks shift. Dispatching rules run the shop in real "
            "time: when a machine frees, the rule picks among waiting "
            "operations - SPT for flow time, EDD for lateness, most-work-"
            "remaining to push long jobs. The disjunctive graph models it "
            "exactly: conjunctive arcs for job precedence, disjunctive "
            "edges for machine sharing, and a schedule is an orientation "
            "of every disjunctive edge with no cycles - the longest path "
            "is the makespan. Metaheuristics then flip edge orientations "
            "to shorten that path. The schedule ships as a Gantt chart "
            "plus the operation sequences per machine."
        ),
        "key_points": [
            "Job shop: n jobs with fixed operation sequences on specific machines; the classic objective is makespan C_max.",
            "Graham's alpha|beta|gamma notation (1979) names every variant precisely, e.g. J||C_max.",
            "The shifting-bottleneck heuristic sequences the worst machine first, re-optimizing as bottlenecks shift.",
            "The disjunctive graph models machine sharing as orientable edges; the longest path is the makespan.",
            "The Gantt chart (1913) is the native visualization: machines vertical, time horizontal, operations as bars.",
        ],
        "requirements": [
            "Job routings with machine assignments, processing times, and precedence.",
            "A sequencing method: shifting bottleneck, dispatching rules, or metaheuristics.",
            "Objective stated in Graham notation (makespan, flow time, lateness, tardiness).",
            "Gantt visualization plus per-machine operation sequences.",
            "Critical-path identification of the delay-driving operation chain.",
        ],
        "standards": [
            "Scheduling notation follows Graham et al. (1979).",
            "Scheduling theory follows Pinedo (2022); complexity follows Garey and Johnson (1979).",
            "Critical-path foundations follow Kelley and Walker (1959).",
        ],
        "citations": [CIT_GRAHAM, CIT_PINEDO, CIT_GAREY, CIT_KELLEY, CIT_GANTT],
        "sig_lens": (
            "The Signature read: the job shop is a hall of many "
            "covenants racing the same clock, and makespan is the hour "
            "the last promise is kept. The Signature Scheduling Method "
            "finds the bottleneck - the one machine whose oath binds "
            "all others - and guards its hours first, for the whole "
            "hall keeps time by the slowest keeper."
        ),
    },
    {
        "key": "real_time",
        "name": "Priority Scheduling and Real-Time Deadlines",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Real-time scheduling promises that work finishes by its "
            "deadline - the control loop, the medical alarm, the trading "
            "risk check. Tasks are periodic (every 10 ms), sporadic "
            "(at most every 50 ms), or aperiodic; each has a worst-case "
            "execution time, a deadline, and a priority. Two classic "
            "policies divide the field: rate-monotonic (fixed priority "
            "by period - shorter period, higher priority), which "
            "guarantees deadlines up to 69 percent utilization for n "
            "tasks (the Liu and Layland bound, 1973), and earliest-"
            "deadline-first (dynamic priority), which is optimal up to "
            "100 percent on one processor. The schedulability test is "
            "the admission control: a new task is accepted only if the "
            "test still passes, which is why real-time systems say no - "
            "a declined task is better than a missed deadline. Priority "
            "inversion (a low-priority task blocking a high-priority one "
            "via a shared lock) is fixed by priority inheritance. "
            "Operations borrow the same discipline: triage, SLA tiers, "
            "and incident severity are priority scheduling for people."
        ),
        "how_it_works": (
            "Real-time scheduling works by admission test plus priority "
            "dispatch. Each task declares its period (or minimum "
            "inter-arrival), worst-case execution time, and deadline. "
            "The schedulability test runs at admission: for rate-"
            "monotonic, the utilization bound test (sum of execution "
            "over period across tasks <= n(2^(1/n) - 1), approaching "
            "69 percent) or the exact response-time analysis iterating "
            "each task's worst-case response against higher-priority "
            "interference; for EDF, the processor-demand test (total "
            "utilization <= 1). Admitted tasks dispatch by priority - "
            "fixed for rate-monotonic, deadline-ordered for EDF - with "
            "preemption so a newly urgent task takes the processor "
            "immediately. Shared resources use priority inheritance: a "
            "low-priority task holding a needed lock temporarily runs "
            "at the blocked high-priority task's priority, bounding "
            "inversion. Missed deadlines raise alarms, not shrugs; the "
            "system logs the miss with the schedule state so analysis "
            "can tighten the next admission test. Operations triage "
            "copies the pattern: severity levels are priorities, "
            "response SLAs are deadlines, and the on-call rotation is "
            "the dispatcher."
        ),
        "key_points": [
            "Real-time scheduling promises finish-by-deadline; tasks are periodic, sporadic, or aperiodic with worst-case execution times.",
            "Rate-monotonic (fixed priority by period) guarantees deadlines to the Liu and Layland bound (~69 percent); EDF is optimal to 100 percent on one processor.",
            "The schedulability test is admission control: new tasks are accepted only if deadlines still hold - saying no beats missing.",
            "Priority inversion via shared locks is fixed by priority inheritance.",
            "Triage, SLA tiers, and incident severity are the same discipline applied to people.",
        ],
        "requirements": [
            "Task declarations: period or minimum inter-arrival, worst-case execution time, deadline.",
            "A schedulability test run at admission (utilization bound or response-time analysis).",
            "Priority dispatch with preemption.",
            "Priority inheritance on shared resources.",
            "Deadline-miss logging with schedule state for analysis.",
        ],
        "standards": [
            "Real-time scheduling theory follows Liu and Layland (Journal of the ACM, 1973).",
        ],
        "citations": [CIT_PINEDO],
        "sig_lens": (
            "The Signature read: the deadline is the oath with teeth - "
            "the promise that must be kept not eventually but by the "
            "hour named. The Signature Scheduling Method admits only "
            "the work it can truly finish in time, and would rather "
            "decline an oath than swear one it cannot keep."
        ),
    },
    {
        "key": "distributed",
        "name": "Distributed Calendars: Consensus and Conflict Resolution",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "When many servers keep the same calendar, they must agree - "
            "and agreement is consensus, the hardest problem in "
            "distributed systems. Lamport's 1978 clocks give events a "
            "happens-before order without synchronized clocks: each "
            "edit carries a logical timestamp, and every replica applies "
            "edits in an order all replicas can reproduce. iCalendar "
            "anticipated this decades early: SEQUENCE numbers order "
            "edits to an event, DTSTAMP breaks ties, so two organizers "
            "editing the same meeting converge on the same winner. "
            "Stronger guarantees come from consensus protocols (Raft, "
            "Paxos) electing one leader to serialize writes, or from "
            "CRDTs (conflict-free replicated data types) whose merge "
            "operation is mathematically guaranteed to converge - the "
            "right CRDT for a calendar merges event sets by UID with "
            "last-writer-wins per field. The CAP theorem bounds the "
            "ambition: during a network partition, choose availability "
            "(keep booking, reconcile later) or consistency (refuse "
            "writes until the partition heals). Calendars usually choose "
            "availability with deterministic reconciliation - the "
            "SEQUENCE rule is exactly that."
        ),
        "how_it_works": (
            "Distributed calendar agreement works by ordering plus "
            "deterministic merge. Each edit to an event increments its "
            "SEQUENCE and stamps DTSTAMP; replicas exchange edits "
            "(via CalDAV sync, iTIP, or replication logs) and apply "
            "the highest-SEQUENCE version, breaking ties by latest "
            "DTSTAMP - every replica running the same rule converges "
            "to the same event without talking to the others. Deleted "
            "events leave tombstones (UID plus deleted flag) so a "
            "resurrected replica does not bring back the dead. For "
            "strong consistency, a Raft leader serializes all writes "
            "to the calendar log and followers apply the log in order; "
            "partitions pause writes on the minority side. CRDT designs "
            "skip the leader: the event set is a grow-only map keyed "
            "by UID with per-field last-writer-wins registers, and "
            "merge is union plus max-by-timestamp - commutative, "
            "associative, idempotent, hence convergent. Clock skew is "
            "bounded by NTP (RFC 5905) so DTSTAMP ties are meaningful. "
            "The system declares its choice up front - available with "
            "reconciliation, or consistent with refused writes - and "
            "monitors divergence (replicas disagreeing past the merge "
            "rule) as the health metric."
        ),
        "key_points": [
            "Distributed calendars need consensus: many servers must agree on the same schedule.",
            "Lamport clocks (1978) order events without synchronized clocks; iCalendar's SEQUENCE/DTSTAMP is the same idea for meetings.",
            "Raft/Paxos serialize writes through a leader for strong consistency; CRDTs merge commutatively for leaderless convergence.",
            "Tombstones keep deleted events deleted when old replicas resurface.",
            "The CAP choice is declared up front: available with deterministic reconciliation, or consistent with refused writes.",
        ],
        "requirements": [
            "An ordering rule on every edit (SEQUENCE/DTSTAMP or logical clocks) applied identically by all replicas.",
            "Tombstones for deletions.",
            "NTP-bounded clock skew (RFC 5905).",
            "A declared CAP choice with divergence monitoring.",
            "Deterministic merge with no silent conflict loss.",
        ],
        "standards": [
            "Distributed ordering follows Lamport (Communications of the ACM, 1978).",
            "Clock synchronization follows RFC 5905; calendar objects follow RFC 5545.",
        ],
        "citations": [CIT_LAMPORT, CIT_RFC5905, CIT_RFC5545],
        "sig_lens": (
            "The Signature read: when many houses keep one covenant, "
            "the Method demands they keep the same one. Consensus is "
            "the oath spoken in chorus - every replica singing the "
            "same hour. The Signature Scheduling Method orders every "
            "edit by an unbreakable rule, buries the deleted dead with "
            "tombstones, and never lets two truths claim one promise."
        ),
    },
    {
        "key": "fairness",
        "name": "Scheduling Fairness and Load Balancing",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Fairness asks who gets the good shifts, the prime rooms, "
            "the light weeks - and answers with arithmetic instead of "
            "favoritism. The measures are standard: max-min fairness "
            "(maximize the worst-off participant's share), proportional "
            "fairness, envy-freeness (nobody prefers another's bundle), "
            "and the Jain index (a single 0-to-1 score of equality). "
            "Rostering fairness tracks weekend counts, night counts, "
            "and holiday duty per worker, then constrains or penalizes "
            "imbalance in the optimizer. Load balancing is fairness "
            "over time: spreading work so no resource runs hot while "
            "another idles - least-loaded-first dispatch, work "
            "stealing in parallel systems, and periodic rebalancing. "
            "The tension is real: the most efficient schedule is "
            "rarely the fairest (always give nights to the willing "
            "few), so the fairness policy states the trade - hard "
            "caps (no one works more than N weekends per quarter) or "
            "soft penalties (imbalance costs in the objective). "
            "Transparent fairness rules, published to the people "
            "scheduled, are what turn a roster from a grievance into "
            "a agreement."
        ),
        "how_it_works": (
            "Fair scheduling works by measuring, constraining, and "
            "publishing. The system tracks fairness counters per "
            "participant: nights worked, weekends worked, holidays, "
            "prime-room bookings, overtime hours - each a running total "
            "over the fairness window (quarter, year). The optimizer "
            "takes these as constraints (hard caps: max 6 weekend days "
            "per quarter) or as penalty terms (each weekend beyond the "
            "mean costs 20), so it trades efficiency against balance "
            "by the stated weights. Max-min fairness is implemented by "
            "lexicographic optimization: first maximize the minimum "
            "share, then the second-minimum, and so on. Load balancing "
            "runs online: least-loaded-first assignment plus periodic "
            "re-optimization that migrates work from hot to cold "
            "resources within migration-cost limits. The fairness "
            "report publishes every counter and the Jain index per "
            "dimension, so workers can verify the roster's justice "
            "themselves - transparency is the enforcement mechanism "
            "no audit can replace."
        ),
        "key_points": [
            "Fairness measures: max-min fairness, proportional fairness, envy-freeness, and the Jain index.",
            "Rostering tracks nights, weekends, holidays, and overtime per worker over a fairness window.",
            "Hard caps or soft penalties in the optimizer trade efficiency against balance by stated weights.",
            "Load balancing is fairness over time: least-loaded-first, work stealing, periodic rebalancing.",
            "Published fairness reports let the scheduled verify justice themselves - transparency is the enforcement.",
        ],
        "requirements": [
            "Fairness counters per participant per dimension over a stated window.",
            "Hard caps or penalty weights in the optimizer, with the trade stated explicitly.",
            "Online load-balancing dispatch plus periodic re-optimization.",
            "Jain-index and counter reporting published to the scheduled.",
            "A grievance path for fairness disputes with data to adjudicate.",
        ],
        "standards": [
            "Fairness vocabulary follows standard resource-allocation literature (max-min, Jain index).",
            "Labor fairness constraints respect applicable labor agreements and law.",
        ],
        "citations": [CIT_PINEDO, CIT_NIOSH],
        "sig_lens": (
            "The Signature read: fairness is the covenant kept equally "
            "- the good hours and the hard ones shared by measure, not "
            "by favor. The Signature Scheduling Method counts every "
            "night and every weekend by name, publishes the counting, "
            "and lets the roster's justice be seen - for a promise that "
            "burdens one keeper while sparing another is an oath "
            "unbalanced."
        ),
    },
    {
        "key": "mrp",
        "name": "Master Production Scheduling and MRP",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Master production scheduling (MPS) promises delivery dates "
            "to customers; material requirements planning (MRP) turns "
            "those promises into timed orders for every part. The chain "
            "runs: the master schedule states what finished goods are "
            "needed when; the bill of materials (BOM) explodes each "
            "product into components; lead-time offsetting walks "
            "backward from the due date subtracting each level's lead "
            "time to find order dates; lot sizing decides how much per "
            "order. Available-to-promise (ATP) is the scheduling "
            "discipline's honesty check: the uncommitted portion of "
            "planned production that sales may actually promise, so "
            "promises never exceed capacity. MRP's classic weakness is "
            "nervousness - small master-schedule changes ripple into "
            "many rescheduled orders - fought with firm planned orders, "
            "time fences (frozen, slushy, liquid zones), and planning "
            "horizons. Capacity requirements planning (CRP) closes the "
            "loop by checking the MRP plan against real bottleneck "
            "capacity, because a material plan no machine can build is "
            "a wish, not a schedule."
        ),
        "how_it_works": (
            "MRP works as explosion plus offsetting. Start with the "
            "master schedule: quantities of each end item per period. "
            "For each item, net requirements = gross requirements minus "
            "on-hand inventory minus scheduled receipts; lot sizing "
            "(lot-for-lot, EOQ, or period-order-quantity) turns net "
            "requirements into planned orders; lead-time offsetting "
            "places each planned order its lead time before the need "
            "date. The BOM explosion repeats this per component level, "
            "top down, generating the full timed order plan. Time "
            "fences protect stability: inside the frozen fence only the "
            "planner changes orders, in the slushy zone changes need "
            "approval, beyond it the system plans freely. ATP "
            "computation walks the master schedule forward, allocating "
            "planned production to customer orders and reporting the "
            "remainder as promiseable. CRP then loads the planned "
            "orders onto work centers by routing hours and flags "
            "overloads; overloaded periods trigger overtime, "
            "subcontracting, or master-schedule revision. The plan "
            "regenerates on a cycle (weekly) with net-change updates "
            "between, and every regeneration reports nervousness "
            "metrics - orders moved, dates changed - so planners see "
            "the churn."
        ),
        "key_points": [
            "MPS promises delivery dates; MRP explodes the BOM and offsets by lead times into timed orders for every part.",
            "Net requirements = gross minus on-hand minus scheduled receipts; lot sizing turns them into planned orders.",
            "Available-to-promise (ATP) is the uncommitted production sales may actually promise - honesty as arithmetic.",
            "Time fences (frozen, slushy, liquid) fight MRP nervousness: small changes rippling into mass rescheduling.",
            "CRP checks the material plan against bottleneck capacity - a plan no machine can build is a wish.",
        ],
        "requirements": [
            "A master schedule, an accurate BOM, lead times, and inventory records.",
            "Netting, lot sizing, and lead-time offsetting logic.",
            "Time fences with change authority per zone.",
            "ATP computation gating customer promises.",
            "CRP overload detection with resolution paths (overtime, subcontract, reschedule).",
        ],
        "standards": [
            "MRP/MPS practice follows standard production-planning literature (APICS/ASCM body of knowledge).",
            "Project and operations scheduling context follows the PMBOK Guide 7th edition.",
        ],
        "citations": [CIT_PMBOK, CIT_GOLDRATT],
        "sig_lens": (
            "The Signature read: the master schedule is the great "
            "covenant - delivery sworn to the customer - and MRP is the "
            "Method reckoning what every smaller oath must be to keep "
            "it. The Signature Scheduling Method explodes the promise "
            "into its thousand keepings, fences the near weeks against "
            "nervous change, and never lets sales swear what the shop "
            "cannot keep."
        ),
    },
    {
        "key": "predictive",
        "name": "Predictive Maintenance and Condition-Based Windows",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Predictive maintenance (PdM) schedules care when the "
            "equipment says it needs it, not when the calendar says so. "
            "Sensors - vibration, temperature, acoustic emission, oil "
            "analysis, thermography - feed models that estimate "
            "remaining useful life (RUL): the bearing whose vibration "
            "trend crosses the alarm limit in an estimated 400 hours "
            "gets its window scheduled inside 300. Condition-based "
            "maintenance (CBM) is the policy: act on measured condition "
            "against thresholds (normal, alert, alarm). The P-F curve "
            "(Moubray) frames the economics: the interval between "
            "potential failure (detectable) and functional failure is "
            "the window in which prediction pays - inspect at a "
            "fraction of the P-F interval and you catch nearly every "
            "failure in time. The scheduling challenge is lead time: "
            "the prediction must come early enough to order parts, "
            "book skills, and place the window before the failure. "
            "False alarms waste windows; missed detections waste "
            "machines; the program tunes thresholds on the confusion "
            "matrix of its own history. PdM does not replace PM - it "
            "focuses it, spending windows where the data points."
        ),
        "how_it_works": (
            "PdM scheduling works as sense, predict, schedule. Sensors "
            "stream condition data to a historian; feature extraction "
            "turns raw signals into health indicators (RMS vibration, "
            "temperature rise above ambient, wear-metal counts); models "
            "- threshold rules, regression on degradation trends, or "
            "trained classifiers - map indicators to RUL estimates with "
            "confidence bands. When RUL minus the planning lead time "
            "(parts procurement plus skill booking) crosses the "
            "scheduling horizon, the system raises a work request with "
            "the predicted failure mode, recommended task, and latest "
            "safe date; the planner places it into a maintenance window "
            "before that date, kitting the predicted parts. Thresholds "
            "are set from the P-F interval: inspection or evaluation "
            "at half the P-F interval or less. Every prediction is "
            "scored after the fact - true positive (failure found), "
            "false alarm, missed detection - and the confusion matrix "
            "retunes thresholds and models quarterly. The program "
            "reports avoided failures (predicted and preempted) against "
            "program cost: the ratio that justifies the sensors."
        ),
        "key_points": [
            "PdM schedules care on measured condition; RUL (remaining useful life) estimates set the latest safe date for the window.",
            "CBM policy: act on condition against normal/alert/alarm thresholds from vibration, temperature, oil, and thermography data.",
            "The P-F curve (Moubray) sets the economics: inspect at a fraction of the potential-to-functional-failure interval.",
            "The prediction must beat the planning lead time: parts procurement plus skill booking plus window placement.",
            "Every prediction is scored (true positive, false alarm, miss) and thresholds retune on the confusion matrix.",
        ],
        "requirements": [
            "Condition sensors with a historian and health-indicator extraction.",
            "RUL models with confidence bands per failure mode.",
            "P-F-interval-based inspection and threshold policy.",
            "Work-request generation with predicted mode, task, and latest safe date.",
            "Prediction scoring and quarterly threshold retuning.",
        ],
        "standards": [
            "RCM and P-F practice follow Moubray (1997).",
            "Asset management context follows ISO 55000:2024.",
        ],
        "citations": [CIT_MOUBRAY, CIT_ISO55000],
        "sig_lens": (
            "The Signature read: predictive care is the covenant heard "
            "before it is broken - the machine whispering its need, "
            "the Method listening in time. The Signature Scheduling "
            "Method reads the tremor in the bearing as a promise "
            "asking to be kept early, and writes the window before "
            "the failure writes it."
        ),
    },
    {
        "key": "architecture",
        "name": "The Scheduling System Architecture",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A production scheduling system is a stack of six layers. "
            "The model layer holds resources, intervals, constraints, "
            "and rules - the data models of the foundations records. "
            "The engine layer runs conflict detection, recurrence "
            "expansion, constraint solving, and optimization. The "
            "integration layer speaks iCalendar, CalDAV, and APIs to "
            "the outside world. The workflow layer carries booking "
            "lifecycles: holds, confirmations, reminders, check-ins, "
            "cancellations, waitlists. The presentation layer shows "
            "calendars, Gantt charts, rosters, and fairness reports to "
            "humans. The governance layer holds audit trails, access "
            "control, and DATA LOCK-IN: once a record is added it is "
            "locked, changeable only by proper authority, so the "
            "schedule's history is trustworthy. Scaling splits by "
            "resource shard (each resource's ledger independent), "
            "caches free/busy aggressively (the hottest query), and "
            "runs heavy optimization asynchronously - the user gets "
            "an answer now, the optimizer improves it in the "
            "background. Every layer from this database appears: "
            "intervals at the bottom, fairness at the top."
        ),
        "how_it_works": (
            "The architecture works by separating the hot path from the "
            "heavy path. Booking requests hit the API, which validates "
            "against the model layer and runs conflict detection on the "
            "resource's sharded ledger - milliseconds, synchronous, "
            "with the tentative-hold lock. Recurrence expansion and "
            "free/busy computation serve from cache, invalidated on "
            "writes. Optimization (rostering, timetabling, re-packing) "
            "runs as background jobs on snapshots, publishing improved "
            "schedules the planner reviews - never silently rewriting "
            "committed bookings. The integration layer syncs via "
            "CalDAV and exchanges iTIP with federated partners; "
            "webhooks notify downstream systems of changes. The "
            "workflow engine drives lifecycles with timers (hold "
            "expiry, reminder sends, no-show release) and records "
            "every transition to the audit log. Access control gates "
            "every write by role and ownership; the governance layer "
            "locks records per policy so history cannot be rewritten. "
            "Monitoring watches booking latency, conflict rates, sync "
            "lag, and optimizer gaps - the vital signs of the "
            "scheduling organism."
        ),
        "key_points": [
            "Six layers: model, engine, integration, workflow, presentation, governance - each record in this database lives in one.",
            "The hot path (booking + conflict detection) is synchronous and millisecond; optimization runs asynchronously on snapshots.",
            "Resource-sharded ledgers scale writes; cached free/busy serves the hottest query.",
            "The workflow engine drives lifecycles with timers: hold expiry, reminders, no-show release.",
            "Governance locks records and audits every transition so schedule history is trustworthy.",
        ],
        "requirements": [
            "A resource-sharded ledger store with interval indexing.",
            "Synchronous conflict detection on the booking path.",
            "Asynchronous optimization jobs that never silently rewrite committed bookings.",
            "CalDAV/iTIP integration plus webhook change notification.",
            "Role-based access control, audit logging, and record locking.",
        ],
        "standards": [
            "Calendar interchange follows RFC 5545/5546; sync follows RFC 4791.",
            "Time handling follows ISO 8601:2019, RFC 3339, and the IANA tz database.",
        ],
        "citations": [CIT_RFC5545, CIT_RFC5546, CIT_RFC4791, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the architecture is the temple that "
            "houses the covenants - six layers, each guarding the "
            "oaths in its keeping. The hot path guards the moment of "
            "swearing; the governance layer guards the memory of "
            "every oath ever sworn. The Signature Scheduling Method "
            "builds so that no promise can be lost, forged, or "
            "silently unwritten."
        ),
    },
    {
        "key": "audit",
        "name": "Schedule Audit, Compliance, and Forensics",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Schedules are evidence: of hours worked, of maintenance "
            "done, of promises kept or broken. Audit is the discipline "
            "of proving it. Every booking, change, cancellation, and "
            "override is logged with who, when, what changed, and under "
            "what authority - the trail that lets an auditor replay any "
            "day. Compliance checks run against the rules that bind the "
            "operation: labor law (hours, rest, days off), maintenance "
            "regulations (completion rates, overdue escalation), safety "
            "rules (qualification checks before equipment booking), and "
            "contract SLAs (window policies, error budgets). Forensics "
            "answers 'what happened' after the fact: reconstructing the "
            "schedule state at the incident time, tracing which change "
            "introduced the conflict, and distinguishing data error from "
            "process failure. Ghost bookings, backdated changes, and "
            "approval bypasses are the classic findings - each a "
            "control to add. A schedule that cannot be audited cannot "
            "be trusted, and in regulated industries it cannot legally "
            "exist."
        ),
        "how_it_works": (
            "Audit works as immutable history plus continuous checking. "
            "Every mutation writes an append-only log entry: timestamp, "
            "actor, action, before/after values, and authority "
            "reference; the log is hash-chained or write-once so "
            "tampering is detectable. Compliance rules run as scheduled "
            "queries: hours-per-week per worker against the legal cap, "
            "rest-between-shifts against the minimum, PM completion "
            "against the target rate, qualification validity against "
            "booking dates - violations open cases with owners and due "
            "dates. Forensic replay reconstructs any instant by folding "
            "the log from a snapshot to the target time, showing exactly "
            "what the schedule looked like when the incident occurred; "
            "diffing two replays isolates the change that broke things. "
            "Access reviews certify quarterly who may approve what. "
            "The compliance dashboard rolls it up: green where rules "
            "hold, red where they break, with the evidence one click "
            "away - because an audit finding without the underlying "
            "record is just an opinion."
        ),
        "key_points": [
            "Every mutation logs who, when, what changed, and under what authority - append-only and tamper-evident.",
            "Compliance queries run continuously: hours caps, rest minimums, PM completion, qualification validity, SLA windows.",
            "Forensic replay folds the log from a snapshot to any instant, reconstructing the schedule at incident time.",
            "Classic findings - ghost bookings, backdated changes, approval bypasses - each become a new control.",
            "A schedule that cannot be audited cannot be trusted; in regulated industries it cannot legally exist.",
        ],
        "requirements": [
            "Append-only, tamper-evident mutation logging with authority references.",
            "Continuous compliance queries with case management for violations.",
            "Snapshot plus log-fold forensic replay.",
            "Quarterly access reviews of approval authorities.",
            "A compliance dashboard with evidence one click from every finding.",
        ],
        "standards": [
            "Audit trail practice aligns with standard IT general controls; change records follow ITIL 4.",
            "Labor compliance follows applicable jurisdiction law.",
        ],
        "citations": [CIT_ITIL, CIT_NIOSH],
        "sig_lens": (
            "The Signature read: the audit trail is the memory of the "
            "covenants - every oath, every amendment, every keeping, "
            "written where none can unwrite it. The Signature "
            "Scheduling Method keeps its history tamper-evident because "
            "a promise whose past can be edited was never truly sworn."
        ),
    },
    {
        "key": "operating_picture",
        "name": "The Resource Calendar Operating Picture",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The operating picture is the whole scheduling system seen "
            "at once: every resource's calendar, every demand forecast, "
            "every constraint, every buffer's health, every fairness "
            "counter, every audit flag - fused into the one view from "
            "which the operation is run. It answers the commander's "
            "questions: what is committed, what is at risk, what is "
            "broken, what needs a decision now. Demand meets capacity "
            "on the picture: forecasted load against scheduled coverage, "
            "with gaps flagged before they become failures. Buffers "
            "show green/yellow/red; fairness counters show balance; the "
            "error budget shows remaining risk capital; the audit feed "
            "shows what changed. Building it is an integration problem - "
            "every record in this database feeds it - and running it is "
            "a rhythm: the daily huddle reviews the next 24 hours, the "
            "weekly review the next cycle, the monthly review the "
            "trends. The operating picture does not replace the "
            "schedulers; it gives them, and everyone they serve, the "
            "same truth. One ledger per resource, one picture for the "
            "operation: that is the doctrine this database teaches."
        ),
        "how_it_works": (
            "The operating picture works as a fused, live dashboard over "
            "the scheduling stack. Data pipelines stream from every "
            "ledger - bookings, holds, check-ins, completions, sensor "
            "conditions, audit events - into an aggregated view model "
            "refreshed on change, not on poll. Demand forecasts overlay "
            "scheduled coverage per interval per skill, and the gap "
            "detector flags intervals where coverage falls short, "
            "ranked by time-to-impact so the nearest fire burns "
            "brightest. Buffer penetration, fairness counters, error "
            "budgets, and compliance flags each render as health "
            "tiles with drill-down to the underlying records. "
            "Scenario tools let planners drag a booking and see the "
            "projected conflicts, coverage, and fairness impact before "
            "committing - what-if as a first-class operation. Alerting "
            "fires on thresholds (coverage gap inside 48 hours, buffer "
            "red, budget exhausted) to the right roles. The daily "
            "rhythm - huddle, review, trend - turns the picture from a "
            "display into a practice. Every number on the picture links "
            "to its source record: trust, but verify, in one click."
        ),
        "key_points": [
            "The operating picture fuses every calendar, forecast, constraint, buffer, fairness counter, and audit flag into one command view.",
            "It answers: what is committed, what is at risk, what is broken, what needs a decision now.",
            "Gap detection flags coverage shortfalls ranked by time-to-impact before they become failures.",
            "What-if scenario tools project conflicts, coverage, and fairness impact before committing a change.",
            "Every number links to its source record - trust, but verify, in one click; the daily rhythm turns display into practice.",
        ],
        "requirements": [
            "Live data pipelines from every scheduling ledger into a fused view model.",
            "Demand-versus-coverage gap detection ranked by time-to-impact.",
            "Health tiles for buffers, fairness, error budgets, and compliance with drill-down.",
            "What-if scenario projection before commit.",
            "Threshold alerting to the right roles plus a daily/weekly/monthly review rhythm.",
        ],
        "standards": [
            "Underlying data follows RFC 5545/5546, ISO 8601:2019, and the IANA tz database.",
            "Availability and change practice follow ITIL 4.",
        ],
        "citations": [CIT_RFC5545, CIT_ISO8601, CIT_ITIL, CIT_PINEDO],
        "sig_lens": (
            "The Signature read: the operating picture is the covenant "
            "hall seen whole - every oath sworn, every keeper named, "
            "every risk lit like a candle. The Signature Scheduling "
            "Method ends where it began, at the ledger: one ledger per "
            "resource, one picture for the operation, one truth for "
            "all who depend on the keeping."
        ),
    },
]
