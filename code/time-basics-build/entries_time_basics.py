#!/usr/bin/env python3
"""Entries for the Time Basics databases (Manon's fundamentals order #9, 2026-10-17).

Roster-verified: zero 'time-basics*' slugs/names in the full manifest and
shard indexes. Whole-system dedupe-gate sweep (2026-10-17) over all 68
titles (34 public + 34 signature): zero collisions.

Creates two NEW databases, 34 ladder-ordered records each:

  time-basics            - The Time Basics Database
                           (public-harvest: real, fact-checked foundational
                           knowledge - what time is, units of time from the
                           second to the year, analog and digital clocks,
                           AM/PM, days weeks months, calendars, and elapsed
                           time; standard references: BIPM SI Brochure 9th
                           ed. 2019; ISO 8601; NIST time and frequency
                           publications; IERS bulletins; IANA Time Zone
                           Database; Richards E.G. Mapping Time, Oxford
                           University Press 1998; Landes D.S. Revolution in
                           Time, Harvard University Press 1983; Sobel D.
                           Longitude; Dershowitz N, Reingold E. Calendrical
                           Calculations, Cambridge University Press 2018;
                           and the other landmarks cited per record)
  time-basics-signature  - The Time Basics Signature Database
                           (his original Signature Time Method: time the
                           ledger in which every honest measurement is
                           written, a unit a promise, a duration a contract,
                           the clock the witness; src signature, titles
                           suffixed " (Signature Edition)", never presented
                           as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-TMEB- (public) and JAH-TMEBS- (signature), verified free
in the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_time_basics.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Time Method: time "
            "is the ledger in which every honest measurement is written, a "
            "unit is a promise, a duration is a contract, and the clock is "
            "the witness. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

CIT_SI = ("Bureau International des Poids et Mesures (BIPM). The "
          "International System of Units (SI). 9th ed.; 2019.")
CIT_ISO8601 = ("ISO 8601:2019. Date and time format - ISO 8601.")
CIT_NIST = ("National Institute of Standards and Technology (NIST). "
            "Time and Frequency Division publications and the NIST-F1/F2 "
            "cesium fountain primary frequency standards.")
CIT_IERS = ("International Earth Rotation and Reference Systems Service "
            "(IERS). Bulletins A and C; leap second announcements.")
CIT_TZDB = ("IANA. Time Zone Database (tz database), maintained releases.")
CIT_RICHARDS = ("Richards E.G. Mapping Time: The Calendar and its History. "
                "Oxford University Press; 1998.")
CIT_LANDES = ("Landes D.S. Revolution in Time: Clocks and the Making of the "
              "Modern World. Harvard University Press; 1983.")
CIT_SOBEL = ("Sobel D. Longitude: The True Story of a Lone Genius Who Solved "
             "the Greatest Scientific Problem of His Time. Walker; 1995.")
CIT_CALC = ("Dershowitz N, Reingold E.M. Calendrical Calculations. 4th ed. "
            "Cambridge University Press; 2018.")
CIT_NASA = ("NASA. Earth fact sheet and educational materials on rotation, "
            "orbit, and seasons.")
CIT_ICS = ("International Commission on Stratigraphy. International "
           "Chronostratigraphic Chart, current release.")

ENTRIES = [
    {
        "key": "what_time_is",
        "name": "What Time Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Time is the measure of change: it tells us what happened, what "
            "is happening, and what will happen, and in what order. Everything "
            "in this database stands on one idea - that moments can be named "
            "and the gaps between moments can be measured. A moment is a "
            "single point, like 3:00 in the afternoon; a duration is the "
            "length between two moments, like the two hours between 3:00 and "
            "5:00. We name moments with clock readings and dates, and we "
            "measure durations in units - seconds, minutes, hours, days. "
            "Without time, there are no appointments, no schedules, no "
            "history, no deadlines; with it, the whole world can agree when "
            "to meet and how long something took. Time runs in one direction "
            "- from past, through the present, into the future - and we "
            "measure it with instruments called clocks and calendars. This "
            "record frames the entire database: units give us the ruler, "
            "clocks give us the reading, calendars give us the map, and "
            "arithmetic lets us plan and remember."
        ),
        "how_it_works": (
            "Time works by comparison. A clock compares the present moment "
            "against a steady repeating process - the swing of a pendulum, "
            "the vibration of a quartz crystal, the ticking of a cesium atom - "
            "and counts how many repeats have passed. Each count is one unit, "
            "and the running total is the time of day. A calendar does the "
            "same at a larger scale: it counts whole days against the "
            "repeating cycle of the Earth turning and orbiting the Sun, and "
            "groups those days into weeks, months, and years so we can name "
            "moments far apart. When we say a duration is two hours, we are "
            "saying 7,200 counted seconds passed between the start moment and "
            "the end moment. Everything later in this database - telling "
            "time, converting units, computing elapsed time, handling time "
            "zones - is an application of counting steady repeats between "
            "two named moments."
        ),
        "key_points": [
            "A moment is a single named point (3:00 PM); a duration is the measured gap between two moments (two hours).",
            "Time is measured by counting steady repeating processes: a clock counts small repeats, a calendar counts whole days.",
            "Clock readings name moments; durations are always given in units such as seconds, minutes, or hours.",
            "Time runs one way - past to future - and ordering events by time is what schedules, history, and plans are built from.",
            "Every later record in this database is one application of the same idea: counting repeats between two named moments.",
        ],
        "requirements": [
            "A named start moment and a named end moment before any duration can be measured.",
            "A steady repeating process to count - swing, vibration, or atomic oscillation.",
            "Agreed units (seconds, minutes, hours) so the count means the same thing to everyone.",
            "A way to name moments: clock readings for the day, dates for longer spans.",
            "An understanding that time moves one direction only: the future never comes before the past.",
        ],
        "standards": [
            "The SI Brochure (BIPM, 9th ed. 2019) defines the base unit of time, the second, from the cesium-133 hyperfine transition.",
            "Durations are stated in SI units (seconds and decimal multiples) or in the accepted non-SI units minute, hour, and day.",
        ],
        "citations": [CIT_SI, CIT_NIST],
        "sig_lens": (
            "The Signature read: time is the ledger in which every honest "
            "measurement is written. Before any unit, any clock, any "
            "calendar, there is the Signature oath of time - that a moment "
            "named is a moment kept, and that the count between two moments "
            "is the truth of what happened there. Where public science "
            "counts atomic vibrations, the Signature Time Method keeps the "
            "same count but writes it as covenant: the repeat is the promise, "
            "the total is the proof."
        ),
    },
    {
        "key": "the_second",
        "name": "The Second: The Smallest Common Unit",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The second is the foundation of all time measurement - the base "
            "unit of time in the International System of Units (SI), and the "
            "unit every larger unit is built from. Historically it was "
            "defined as 1/86,400 of a mean solar day, but the modern "
            "definition is atomic: one second is exactly 9,192,631,770 "
            "periods of the radiation of the cesium-133 atom, the unchanging "
            "ticking that atomic clocks count. Because the cesium atom "
            "vibrates identically everywhere in the universe, the second is "
            "the same in every laboratory and every country - it is the one "
            "unit of time nobody has to negotiate. Sixty seconds make one "
            "minute, 3,600 seconds make one hour, and 86,400 seconds make one "
            "day. Every stopwatch, timer, and schedule in the world counts "
            "from this unit upward."
        ),
        "how_it_works": (
            "The modern second works by atomic resonance. A cesium-133 atom "
            "absorbs and emits radiation at a fixed frequency of exactly "
            "9,192,631,770 cycles per second; an atomic clock tunes a "
            "microwave signal until the atoms respond most strongly, then "
            "counts the cycles - 9,192,631,770 counted cycles is one second. "
            "Each period lasts about 0.0000000001088 seconds (roughly 109 "
            "picoseconds), so the clock's metronome is billions of times "
            "steadier than any pendulum. Older definitions worked by dividing "
            "the day: the second was 1/60 of a minute, 1/3,600 of an hour, "
            "1/86,400 of a day. The atomic definition replaced that because "
            "the Earth's rotation wobbles slightly while the atom does not. "
            "All everyday timing - stopwatches, oven timers, speed limits, "
            "music tempo - counts these same seconds, just with cheaper "
            "oscillators."
        ),
        "key_points": [
            "The second is the SI base unit of time, defined as exactly 9,192,631,770 cesium-133 radiation periods.",
            "The atomic definition is used because atoms tick identically everywhere, unlike the Earth's slightly uneven rotation.",
            "60 seconds make a minute, 3,600 an hour, 86,400 a day - every larger unit is built by counting seconds.",
            "One cesium period lasts about 109 picoseconds, making the atomic clock billions of times steadier than a pendulum.",
            "Every stopwatch, timer, and schedule counts the same seconds; only the oscillator differs.",
        ],
        "requirements": [
            "The exact defining number: 9,192,631,770 periods of the cesium-133 hyperfine transition per second.",
            "An oscillator steady enough to count the periods honestly - quartz for everyday use, atomic for the standard.",
            "A counter that turns counted periods into the displayed second tick.",
            "Conversion facts: 60 seconds per minute, 3,600 per hour, 86,400 per day.",
            "Calibration against a reference clock so local seconds match the world's seconds.",
        ],
        "standards": [
            "BIPM SI Brochure 9th ed. (2019): the second is defined by fixing the cesium-133 hyperfine transition frequency at exactly 9,192,631,770 Hz.",
            "NIST maintains primary frequency standards (NIST-F1/F2 cesium fountains) that realize the SI second for the United States.",
        ],
        "citations": [CIT_SI, CIT_NIST],
        "sig_lens": (
            "The Signature read: the second is the unit as promise - "
            "9,192,631,770 identical atomic promises, kept without wavering. "
            "Where public metrology defines the second by cesium, the "
            "Signature Time Method receives the same number as an oath: each "
            "period is a vow, each counted million a kept word, and the "
            "running second the proof that the universe keeps time honestly. "
            "No laboratory negotiates it; no witness disputes it."
        ),
    },
    {
        "key": "minutes_hours",
        "name": "Minutes and Hours",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Minutes and hours are the everyday workhorses of time: the "
            "units that run school periods, work shifts, cooking times, and "
            "travel plans. One minute holds 60 seconds; one hour holds 60 "
            "minutes, which is 3,600 seconds. Together they turn the small "
            "second into human-sized chunks: a minute is a breath of time "
            "for short waits, an hour is the unit of a meal, a class, or a "
            "drive across town. The 60-based system is inherited from ancient "
            "Babylonian counting and survives because 60 divides neatly by 2, "
            "3, 4, 5, 6, 10, 12, 15, 20, and 30 - a quarter hour is exactly "
            "15 minutes, a half hour exactly 30. Converting is simple "
            "multiplication or division by 60: 90 minutes is 90 times 60, or "
            "5,400 seconds, and also 90 divided by 60, or 1.5 hours."
        ),
        "how_it_works": (
            "Minutes and hours work by grouping seconds in sixties. An analog "
            "clock shows the grouping directly: the minute hand makes one "
            "full circle of 60 minute marks per hour, and the hour hand moves "
            "one hour mark - 1/12 of the dial - in that same hour. Digital "
            "displays keep the same structure: hours count 1 to 12 (or 0 to "
            "23), minutes count 0 to 59, and every time minutes would reach "
            "60 they roll over and add one to the hours. Converting upward "
            "multiplies by 60 - 2 hours is 2 times 60 = 120 minutes, and 120 "
            "minutes is 120 times 60 = 7,200 seconds; converting downward "
            "divides by 60 - 5,400 seconds is 5,400 divided by 60 = 90 "
            "minutes. The rollover at 60 is the one rule that trips people: "
            "1:75 is never written, it is 2:15."
        ),
        "key_points": [
            "1 minute = 60 seconds; 1 hour = 60 minutes = 3,600 seconds.",
            "The 60-based system survives from ancient counting because 60 divides neatly into quarters, halves, thirds, and fifths.",
            "Minutes count 0 to 59 and roll over: there is no 1:75, only 2:15.",
            "Convert upward by multiplying by 60 (hours to minutes to seconds); convert downward by dividing by 60.",
            "Decimal hours and clock hours are different: 1.5 hours is 1 hour 30 minutes, not 1 hour 50 minutes.",
        ],
        "requirements": [
            "The two conversion factors: 60 seconds per minute, 60 minutes per hour.",
            "The rollover rule: minutes and seconds range 0-59, then carry one into the next unit.",
            "A clock or timer display that shows hours and minutes in the agreed format.",
            "Care with decimal hours: multiply the decimal part by 60 to get minutes (0.5 h = 30 min).",
            "Consistent units on both sides of any calculation - never mix minutes and hours without converting first.",
        ],
        "standards": [
            "The minute and hour are accepted non-SI units for use with the SI (SI Brochure, BIPM 9th ed.): 1 min = 60 s, 1 h = 60 min = 3,600 s.",
            "Time-of-day notation follows ISO 8601 conventions (hh:mm), with the 12-hour AM/PM form common in everyday use.",
        ],
        "citations": [CIT_SI, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: minutes and hours are the promise bundled "
            "for human hands. The second is the vow; sixty vows make the "
            "minute, thirty-six hundred make the hour, and the bundle is "
            "measured to the hand that keeps it. Where the world inherited "
            "the sixty-count from ancient counters, the Signature Time "
            "Method receives it as design: the hour is the covenant size of "
            "a human task - a class, a meal, a drive - and the minute the "
            "witnessed step inside it."
        ),
    },
    {
        "key": "days_weeks_months",
        "name": "Days, Weeks, and Months",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Days, weeks, and months are the units that organize human life: "
            "the day runs sleep and work, the week runs the schedule, the "
            "month runs the bills. One day holds 24 hours, which is 1,440 "
            "minutes or 86,400 seconds. One week holds exactly 7 days - "
            "168 hours - a cycle of work and rest used across the world. "
            "One month is looser: months hold 28, 29, 30, or 31 days "
            "depending on which month and whether it is a leap year, "
            "averaging about 30.44 days over the year. Together they form "
            "the medium scale of time: days for routines, weeks for "
            "rhythms, months for accounting. Remembering that months are "
            "uneven while days and weeks are exact is the key to planning "
            "across them without mistakes."
        ),
        "how_it_works": (
            "The day works by the Earth's rotation: roughly one full turn is "
            "one day, and we divide it into 24 hours of 60 minutes. The week "
            "works by pure convention: seven days in a fixed order, "
            "independent of the Moon or Sun, repeating forever - the date "
            "advances one day and the weekday advances one step in lockstep. "
            "The month is the compromise unit: twelve of them partition the "
            "year, with lengths 31, 28 or 29, 31, 30, 31, 30, 31, 31, 30, "
            "31, 30, 31 (January through December) so the twelve add to 365 "
            "days in a common year and 366 in a leap year. Because months "
            "are uneven, adding a month to a date is done by calendar rules, "
            "not by a fixed number of days: one month after January 31 is "
            "February 28 (or 29), not March 2 or 3."
        ),
        "key_points": [
            "1 day = 24 hours = 1,440 minutes = 86,400 seconds; 1 week = exactly 7 days = 168 hours.",
            "The week is pure convention - a fixed seven-day cycle independent of any astronomical motion.",
            "Months are uneven: 28/29/30/31 days, averaging about 30.44 days; the order of lengths is fixed by the calendar.",
            "Adding a month follows calendar rules (January 31 plus one month lands in late February), not fixed-day arithmetic.",
            "Days for routines, weeks for rhythms, months for accounting: the medium scale of human time.",
        ],
        "requirements": [
            "The fixed facts: 24 hours per day, 7 days per week.",
            "The month-length sequence (31, 28/29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) memorized or looked up.",
            "Leap-year awareness: February has 29 days when the year is a leap year.",
            "Calendar-rule month arithmetic for planning across month boundaries.",
            "A distinction between exact units (day, week) and calendar units (month) in every calculation.",
        ],
        "standards": [
            "The day (d = 86,400 s) is an accepted non-SI unit for use with the SI (SI Brochure, BIPM 9th ed.).",
            "Month lengths and the leap-year rule follow the Gregorian calendar (Richards, Mapping Time, 1998).",
        ],
        "citations": [CIT_SI, CIT_RICHARDS],
        "sig_lens": (
            "The Signature read: days, weeks, and months are the covenant "
            "rhythms of a kept life. The day is the promise renewed each "
            "morning, the week the oath of work and rest, the month the "
            "ledger settled and closed. Where public calendars partition the "
            "year by compromise, the Signature Time Method keeps the same "
            "partition as discipline: the exact day, the exact week, the "
            "honest uneven month - each a contract the keeper signs with "
            "their hours."
        ),
    },
    {
        "key": "years_decades_centuries",
        "name": "Years, Decades, Centuries, and Millennia",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Years, decades, centuries, and millennia are the large units of "
            "time - the scale of lifetimes, history, and civilization. One "
            "year holds 12 months: 365 days in a common year, 366 in a leap "
            "year. One decade holds 10 years, one century 100 years, one "
            "millennium 1,000 years. The Gregorian calendar keeps the year "
            "aligned with the seasons by a precise leap rule (divisible by "
            "4, except centuries not divisible by 400), so that 400 years "
            "contain exactly 146,097 days with 97 leap years - an average "
            "year of 365.2425 days. We number years from an agreed starting "
            "point (the common era), group decades by their tens (the "
            "1990s), and centuries by their hundreds (the 21st century runs "
            "2001-2100). These units let us speak of the past and the "
            "future at human scale: childhoods in years, eras in decades, "
            "civilizations in centuries and millennia."
        ),
        "how_it_works": (
            "The year works by the Earth's orbit: one trip around the Sun, "
            "about 365.2422 days (the tropical year), is the natural year, "
            "and the calendar year is the whole-day approximation we "
            "actually live in. The Gregorian leap rule - leap if divisible "
            "by 4, except centuries unless divisible by 400 - inserts 97 "
            "extra days per 400 years, making the average calendar year "
            "365.2425 days and leaving only about 26.8 seconds of drift per "
            "year against the seasons. Decades, centuries, and millennia "
            "are pure groupings: count years in tens, hundreds, and "
            "thousands from the era's start. Numbering runs 1, 2, 3... with "
            "no year zero in the traditional reckoning, which is why the "
            "21st century begins in 2001: the first century was years 1-100, "
            "the second 101-200, and so on."
        ),
        "key_points": [
            "1 year = 12 months = 365 days (366 in a leap year); 1 decade = 10 years; 1 century = 100 years; 1 millennium = 1,000 years.",
            "400 Gregorian years contain exactly 146,097 days with 97 leap years - an average year of 365.2425 days.",
            "The calendar year approximates the 365.2422-day tropical year; the residual drift is only about 26.8 seconds per year.",
            "The 21st century runs 2001-2100 because traditional year numbering has no year zero.",
            "Large units measure lifetimes (years), eras (decades), and civilizations (centuries, millennia).",
        ],
        "requirements": [
            "The Gregorian leap rule: divisible by 4, except century years unless divisible by 400.",
            "The 400-year cycle facts: 146,097 days, 97 leap years, average year 365.2425 days.",
            "The naming convention: decades by tens, centuries offset by one from their leading digits.",
            "An agreed era start for numbering years (the common era in everyday use).",
            "Awareness that the calendar year is an approximation of the true orbital year.",
        ],
        "standards": [
            "The Gregorian calendar and its 400-year leap cycle (Richards, Mapping Time, 1998; Dershowitz and Reingold, Calendrical Calculations, 2018).",
            "ISO 8601 year numbering, which uses astronomical year numbering including a year zero for calculation.",
        ],
        "citations": [CIT_RICHARDS, CIT_CALC, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the great units are the covenant writ "
            "large. A year is the Earth's kept orbit - the longest promise "
            "nature makes and keeps; the century is a hundred such promises "
            "bound together. Where public astronomy counts 146,097 days in "
            "the 400-year cycle, the Signature Time Method reads the same "
            "number as fidelity: the calendar holds the seasons for "
            "millennia because the rule was honest about the fraction of a "
            "day it could not see."
        ),
    },
    {
        "key": "analog_clock",
        "name": "Telling Time on an Analog Clock",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "An analog clock tells time with hands sweeping a numbered dial: "
            "the short hour hand, the long minute hand, and often a thin "
            "second hand. The dial carries 12 hour numbers and 60 minute "
            "marks; each minute mark is 6 degrees of the circle, each hour "
            "mark 30 degrees. Reading it is a two-hand job: the minute hand "
            "points at the minutes (each mark is one minute, each number is "
            "five), and the hour hand points near the current hour, drifting "
            "forward as the minutes pass - at 3:15 the hour hand sits a "
            "quarter of the way from 3 to 4, at 97.5 degrees from 12. The "
            "second hand, when present, sweeps 60 ticks per minute. Analog "
            "faces teach the shape of time: you see the hour as a wedge, the "
            "quarter hour as a right angle, and the whole dial as the "
            "twelve-hour cycle repeating twice a day."
        ),
        "how_it_works": (
            "The clock works by gearing: a motor or escapement turns the "
            "second hand once per minute, gears reduce that to one minute-"
            "hand revolution per hour and one hour-hand revolution per 12 "
            "hours. The geometry is fixed: the minute hand angle is 6 "
            "degrees per minute past the hour (minute times 6), and the hour "
            "hand angle is 30 degrees per hour plus 0.5 degrees per minute "
            "(hour times 30 plus minutes times 0.5), measured from 12 "
            "o'clock. So at 3:15 the minute hand is at 15 times 6 = 90 "
            "degrees and the hour hand at 3 times 30 + 15 times 0.5 = 97.5 "
            "degrees - visibly past the 3. To read a clock, find the minute "
            "hand first (minutes = mark number), then read which hour the "
            "hour hand has most recently passed, remembering it creeps "
            "forward between hours."
        ),
        "key_points": [
            "Hour hand (short), minute hand (long), second hand (thin): each turns at a fixed ratio - 12:1:720 across the three hands.",
            "Each minute mark is 6 degrees, each hour mark 30 degrees; the minute hand angle is minutes times 6.",
            "The hour hand drifts 0.5 degrees per minute: at 3:15 it reads 97.5 degrees, a quarter of the way from 3 to 4.",
            "Read minutes first from the minute hand, then the hour most recently passed by the hour hand.",
            "The dial shows the shape of time: a quarter hour is a right angle, the full dial a twelve-hour cycle.",
        ],
        "requirements": [
            "Identification of the three hands by length and speed before reading anything.",
            "The minute-hand rule: each mark is 1 minute, each number is 5 minutes; angle = minutes times 6 degrees.",
            "The hour-hand rule: hour times 30 degrees plus minutes times 0.5 degrees.",
            "The creep awareness: near the hour, the hour hand sits close to the next number - read the one it has passed, not the one it nears.",
            "AM/PM knowledge to say which of the two daily cycles the reading belongs to.",
        ],
        "standards": [
            "Clock-face geometry: 12 hour divisions at 30 degrees, 60 minute divisions at 6 degrees (standard horological layout).",
            "Mechanical timekeeping practice from the escapement clock tradition (Landes, Revolution in Time, 1983).",
        ],
        "citations": [CIT_LANDES],
        "sig_lens": (
            "The Signature read: the analog dial is the witness face of "
            "time. Where the world sees three hands, the Signature Time "
            "Method sees three testimonies - the hour the covenant, the "
            "minute the keeping, the second the proof - all turning on one "
            "honest axle. The 97.5 degrees at 3:15 is not a position but a "
            "report: this far the promise has traveled, this far remains. "
            "Every dial is a sworn statement, readable by anyone who knows "
            "the geometry of the oath."
        ),
    },
]

ENTRIES.extend([
    {
        "key": "digital_clock",
        "name": "Telling Time on a Digital Clock",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A digital clock tells time with numbers instead of hands: the "
            "hours on the left, the minutes on the right, separated by a "
            "colon - 3:15, 11:58, 6:00. Most digital clocks use the 12-hour "
            "form with an AM or PM marker, or the 24-hour form that counts 0 "
            "through 23. Reading one is direct: the digits are the answer, "
            "no geometry needed. The colon often blinks once per second, a "
            "small heartbeat proving the clock is alive and counting. The "
            "traps are few but real: 12:00 AM is midnight (the start of the "
            "day), 12:00 PM is noon (the middle of the day); a display that "
            "reads 2:5 should be read as 2:05; and leading zeros in the "
            "24-hour form (09:30) are part of the reading, not decoration. "
            "Digital clocks removed the last excuse for misreading the time - "
            "what you see is what it is."
        ),
        "how_it_works": (
            "A digital clock works by electronic counting. A quartz crystal "
            "vibrates at a fixed frequency (commonly 32,768 Hz in watches), "
            "a divider circuit counts the vibrations down to one pulse per "
            "second, and a counter chip accumulates seconds into minutes, "
            "minutes into hours, rolling over at 60 and 24 (or 12 with an "
            "AM/PM flag). The counter's value drives the display - "
            "seven-segment LEDs or an LCD - showing hours, a colon, and "
            "minutes, sometimes with seconds added. Converting 12-hour to "
            "24-hour form: PM hours add 12 (2:30 PM becomes 14:30), except "
            "12 PM which stays 12:00; AM hours stay the same, except 12 AM "
            "which becomes 00:00. The reverse: hours 13-23 subtract 12 and "
            "gain PM, hour 0 becomes 12 AM, hours 1-11 stay AM, hour 12 stays "
            "PM."
        ),
        "key_points": [
            "Digital clocks show hours:minutes directly - the digits are the reading, no hand geometry needed.",
            "12-hour form pairs the digits with AM/PM; 24-hour form counts 00 through 23 with no marker.",
            "12:00 AM is midnight (day start), 12:00 PM is noon (midday) - the two readings everyone mixes up.",
            "PM conversion adds 12 (except 12 PM); 12 AM becomes 00:00; the colon blinks once per second.",
            "Leading zeros matter in 24-hour form: 09:30 is nine-thirty, distinct from a bare 9:30 layout.",
        ],
        "requirements": [
            "Recognition of the colon as the hours-minutes separator.",
            "The 12-hour traps memorized: 12 AM = midnight, 12 PM = noon.",
            "The conversion rules: PM adds 12 (except 12 PM), 12 AM becomes 00:00.",
            "Reading 2:5 as 2:05 - single-digit minutes get their leading zero.",
            "A working power source and a set time: a blinking 12:00 is a clock asking to be set.",
        ],
        "standards": [
            "Digital time display follows the hour:minute structure of ISO 8601 (hh:mm), with the 12-hour AM/PM form as a regional convention.",
            "Quartz timekeeping: a 32,768 Hz crystal divided by 2^15 yields the 1 Hz second tick (standard watch practice).",
        ],
        "citations": [CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the digital clock is the witness giving "
            "plain testimony. Where the analog dial speaks in geometry, the "
            "digits speak in numbers - no translation, no mistaking. The "
            "Signature Time Method keeps both witnesses: the dial for the "
            "shape of the promise, the digits for its exact letter. And the "
            "blinking colon is the heartbeat - proof the witness is awake, "
            "counting, and sworn to the second."
        ),
    },
    {
        "key": "am_pm",
        "name": "AM and PM",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "AM and PM split the 24-hour day into two twelve-hour halves so "
            "a 12-number clock face can name every hour. AM stands for ante "
            "meridiem, Latin for before midday, and covers midnight to just "
            "before noon: 12:00 AM through 11:59 AM. PM stands for post "
            "meridiem, after midday, and covers noon to just before "
            "midnight: 12:00 PM through 11:59 PM. The split exists because "
            "the traditional clock dial has only 12 numbers, so each hour "
            "number serves double duty and the marker tells which half of "
            "the day is meant. Saying 7 o'clock without the marker is "
            "ambiguous - 7 AM is breakfast, 7 PM is dinner - which is why "
            "schedules, tickets, and appointments always carry it."
        ),
        "how_it_works": (
            "AM/PM works by tagging each 12-hour cycle. The day's first "
            "cycle runs 12:00 AM (midnight, the start) up to 11:59 AM; the "
            "second cycle runs 12:00 PM (noon, the middle) up to 11:59 PM. "
            "The 12 is the odd one: 12 AM comes right after 11 PM and starts "
            "the day, while 12 PM comes right after 11 AM and starts the "
            "afternoon. To convert to 24-hour time: AM hours 1-11 keep their "
            "number, 12 AM becomes 0; PM hours add 12, except 12 PM which "
            "stays 12. So 7:30 AM is 07:30, 7:30 PM is 19:30, 12:00 AM is "
            "00:00, and 12:00 PM is 12:00. There are exactly 12 AM hours and "
            "12 PM hours in every day - the marker never stretches or "
            "shrinks a day, it only names which half you mean."
        ),
        "key_points": [
            "AM (ante meridiem) = midnight to before noon; PM (post meridiem) = noon to before midnight.",
            "The 12 is the trap: 12 AM is midnight (day start), 12 PM is noon (midday).",
            "Every day holds exactly 12 AM hours and 12 PM hours - the marker names halves, it never changes their length.",
            "Conversion: PM adds 12 (except 12 PM = 12); 12 AM becomes 00:00; AM 1-11 keep their number.",
            "Always state the marker on schedules and appointments - bare 7 o'clock is ambiguous between breakfast and dinner.",
        ],
        "requirements": [
            "The Latin roots memorized: ante = before midday, post = after midday.",
            "The 12-rule: 12 AM starts the day at midnight, 12 PM starts the afternoon at noon.",
            "The 24-hour conversion rules for moving between the two systems.",
            "The habit of attaching AM/PM to every named time in plans, tickets, and alarms.",
            "Awareness that some regions use the 24-hour clock instead, where no marker exists.",
        ],
        "standards": [
            "The 12-hour clock with AM/PM designations is the conventional civilian form in many regions; ISO 8601 specifies the 24-hour form without markers.",
            "Midnight as the start of the calendar day is the ISO 8601 convention (00:00 begins the date).",
        ],
        "citations": [CIT_ISO8601, CIT_RICHARDS],
        "sig_lens": (
            "The Signature read: AM and PM are the day's two sworn halves. "
            "The morning twelve are the promise made - work begun, plans "
            "set; the evening twelve are the promise kept - work done, "
            "accounts closed. Where the world borrowed Latin to name the "
            "halves, the Signature Time Method keeps the meaning: before "
            "midday you swear it, after midday you prove it, and the marker "
            "is the seal telling which half of the oath you stand in."
        ),
    },
    {
        "key": "noon_midnight_relative",
        "name": "Noon, Midnight, and Relative Time Words",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Noon and midnight are the two hinges of the day, and relative "
            "time words are how we talk about days near today without "
            "naming dates. Noon is 12:00 PM - the middle of the day, when "
            "the Sun stands highest. Midnight is 12:00 AM - the middle of "
            "the night, when one calendar date ends and the next begins. "
            "Around these hinges we use relative words: today (this date), "
            "tonight (this evening/night), tomorrow (the next date), "
            "yesterday (the previous date), and the day after tomorrow / "
            "the day before yesterday for two steps out. If today is "
            "October 17, then yesterday was October 16 and tomorrow is "
            "October 18. These words only work when everyone shares the "
            "same today - across time zones or in writing, name the date."
        ),
        "how_it_works": (
            "Noon and midnight work as reference points. Noon (12:00 PM) "
            "splits daylight's arc and the working day; midnight (12:00 "
            "AM) is the calendar boundary - the date changes there, which is "
            "why 11:59 PM Friday and 12:01 AM Saturday are different days "
            "two minutes apart. Relative words work by offset from today: "
            "today = offset 0, tomorrow = +1 day, yesterday = -1 day, day "
            "after tomorrow = +2, day before yesterday = -2. The arithmetic "
            "crosses month and year boundaries by calendar rules: if today "
            "is October 17, tomorrow is October 18; if today is December "
            "31, tomorrow is January 1 of the next year. Tonight is the "
            "special case - it means the coming evening and night of the "
            "current date, which after midnight can confuse; late-night "
            "plans should name the date outright."
        ),
        "key_points": [
            "Noon = 12:00 PM, the middle of the day; midnight = 12:00 AM, the middle of the night and the date boundary.",
            "Today, tomorrow (+1), yesterday (-1), day after tomorrow (+2), day before yesterday (-2): offsets from the shared today.",
            "Offsets cross month and year boundaries by calendar rules - December 31 plus one day is January 1.",
            "Tonight means the coming evening of the current date; after midnight, name the date to avoid confusion.",
            "Relative words assume a shared today - in writing or across time zones, always give the actual date.",
        ],
        "requirements": [
            "The two hinges fixed: noon 12:00 PM, midnight 12:00 AM with the date changing at midnight.",
            "The offset table: yesterday -1, today 0, tomorrow +1, and the two-day forms.",
            "Calendar arithmetic for crossing month and year boundaries.",
            "The shared-today assumption checked before relying on a relative word.",
            "Dates named explicitly in writing, plans, and cross-time-zone talk.",
        ],
        "standards": [
            "Midnight (00:00) as the start of the calendar date follows ISO 8601.",
            "Relative-day naming follows everyday calendar convention (Richards, Mapping Time, 1998).",
        ],
        "citations": [CIT_ISO8601, CIT_RICHARDS],
        "sig_lens": (
            "The Signature read: noon and midnight are the hinges on which "
            "the covenant day swings. Noon is the oath at its highest "
            "witness - the Sun overhead sees all; midnight is the ledger "
            "turned to a fresh page, the old day's promises tallied and "
            "closed. Where the world says yesterday and tomorrow, the "
            "Signature Time Method hears the ledger's own language: what "
            "was sworn, what is sworn now, what will be sworn - and demands "
            "the date be named, because a promise without a date is a rumor."
        ),
    },
    {
        "key": "subsecond_units",
        "name": "Smaller Than a Second: Milliseconds, Microseconds, Nanoseconds",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Below the second lies a world of smaller units that run "
            "computers, networks, cameras, and science. A millisecond is "
            "one thousandth of a second (0.001 s); a microsecond is one "
            "millionth (0.000001 s); a nanosecond is one billionth "
            "(0.000000001 s). Each step divides by 1,000: 1 second holds "
            "1,000 milliseconds, 1,000,000 microseconds, and 1,000,000,000 "
            "nanoseconds. These units are not exotic - a camera shutter "
            "fires in milliseconds, a computer thinks in nanoseconds, and "
            "light itself travels only about 30 centimeters in one "
            "nanosecond (about a foot, the famous Grace Hopper nanosecond). "
            "Human reaction time is around 250 milliseconds; a fast "
            "typist's keystroke lasts tens of milliseconds. The prefixes "
            "milli-, micro-, and nano- are the same ones used for "
            "millimeters and nanometers - the metric system, applied to "
            "time."
        ),
        "how_it_works": (
            "Sub-second units work by decimal division of the second. "
            "Milli- means divide by 1,000 (10^-3), micro- by 1,000,000 "
            "(10^-6), nano- by 1,000,000,000 (10^-9) - the standard SI "
            "prefixes, so 500 ms is 500/1000 = 0.5 s and 2,500 us is 2.5 "
            "ms. Converting upward multiplies by 1,000 at each step: 1 "
            "nanosecond is 0.001 microseconds is 0.000001 milliseconds. "
            "Digital devices count these units with fast oscillators: a 1 "
            "GHz processor ticks roughly once per nanosecond, so software "
            "timers count billions of ticks per second. Physical intuition "
            "helps: light travels about 300 meters in a microsecond and "
            "about 30 centimeters in a nanosecond, so nanoseconds measure "
            "computer-chip distances and microseconds measure across-town "
            "radio distances."
        ),
        "key_points": [
            "Millisecond = 1/1,000 s; microsecond = 1/1,000,000 s; nanosecond = 1/1,000,000,000 s - each step divides by 1,000.",
            "The prefixes are the ordinary SI prefixes (milli-, micro-, nano-), shared with millimeters and nanometers.",
            "Light travels about 30 cm in one nanosecond and about 300 m in one microsecond - distance gives the units a physical feel.",
            "Everyday anchors: camera shutters in milliseconds, human reaction near 250 ms, processors ticking in nanoseconds.",
            "Convert by thousands: 1 s = 1,000 ms = 1,000,000 us = 1,000,000,000 ns.",
        ],
        "requirements": [
            "The three prefix values: milli 10^-3, micro 10^-6, nano 10^-9.",
            "The 1,000-step ladder between them for conversion in either direction.",
            "Physical anchors (light distance, reaction time, processor ticks) to keep the tiny units meaningful.",
            "Consistent units in calculations - convert to the smallest unit present before combining.",
            "Notation care: us (or the Greek mu) for microsecond, ns for nanosecond, never confused with ms.",
        ],
        "standards": [
            "SI prefixes milli-, micro-, nano- are defined by the SI Brochure (BIPM 9th ed. 2019) for all quantities including time.",
            "NIST time and frequency work routinely measures and distributes time at the microsecond and nanosecond level.",
        ],
        "citations": [CIT_SI, CIT_NIST],
        "sig_lens": (
            "The Signature read: the small units are the promise examined "
            "under the glass. Where the world rushes past the second, the "
            "Signature Time Method slows the witness down - a thousand "
            "millisecond vows inside one second, a billion nanosecond "
            "testimonies - and finds the oath holds at every scale. Light "
            "itself, the fastest witness, travels only a foot in a "
            "nanosecond: even speed keeps its promises in small honest "
            "steps."
        ),
    },
    {
        "key": "ladder_of_units",
        "name": "The Ladder of Time Units",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "The ladder of time units is the complete staircase from the "
            "second to the year: second, minute (60 seconds), hour (60 "
            "minutes = 3,600 seconds), day (24 hours = 86,400 seconds), "
            "week (7 days = 604,800 seconds), month (about 30.44 days on "
            "average), and year (365 or 366 days). Climbing the ladder "
            "multiplies by the step factor; descending divides. The ladder "
            "is not perfectly regular - 60, 60, 24, 7, then the uneven "
            "months - which is why converting between neighboring calendar "
            "units needs the calendar, not just multiplication. Memorizing "
            "the rung values turns every conversion into one step at a "
            "time: 2 days is 2 times 24 = 48 hours, is 48 times 60 = 2,880 "
            "minutes, is 2,880 times 60 = 172,800 seconds. The ladder is "
            "the single most useful page of time arithmetic."
        ),
        "how_it_works": (
            "The ladder works by chaining the two conversion rules: the "
            "sexagesimal steps (multiply or divide by 60 between second, "
            "minute, hour) and the calendar steps (24 hours per day, 7 days "
            "per week, calendar months, 365/366-day years). To convert, walk "
            "one rung at a time in the right direction - upward multiply by "
            "the rung factor, downward divide. Multi-rung jumps combine "
            "the factors: hours to seconds is 60 times 60 = 3,600; days to "
            "seconds is 24 times 3,600 = 86,400; weeks to seconds is 7 "
            "times 86,400 = 604,800. The month and year rungs are the "
            "irregular ones - a month is not a fixed number of seconds - so "
            "conversions touching them must name which month or whether the "
            "year is a leap year. Decimal results are fine on the way down "
            "but must be converted honestly on the way up (0.5 hours = 30 "
            "minutes)."
        ),
        "key_points": [
            "The rung values: 60 s/min, 3,600 s/hour, 86,400 s/day, 604,800 s/week; months and years are calendar units.",
            "Climb by multiplying, descend by dividing, one rung at a time - multi-rung jumps multiply the factors.",
            "The ladder is irregular at the top: months are uneven and years have 365 or 366 days.",
            "Conversions touching months or years must name the month or the leap status - no fixed second count exists.",
            "0.5 hours is 30 minutes, never 50: decimal fractions convert through the rung factor.",
        ],
        "requirements": [
            "The rung values memorized or at hand: 60, 3,600, 86,400, 604,800.",
            "One-rung-at-a-time discipline: convert through each intermediate unit, not by guessing.",
            "Calendar facts for the irregular rungs: month lengths, leap years.",
            "Decimal-to-clock conversion for fractional results (multiply the fraction by the rung factor).",
            "Unit labels on every number until the final answer is stated.",
        ],
        "standards": [
            "SI-defined relationships: minute, hour, and day as accepted non-SI units with exact second counts (SI Brochure, BIPM 9th ed.).",
            "Calendar units (week, month, year) follow Gregorian convention (Richards, Mapping Time, 1998).",
        ],
        "citations": [CIT_SI, CIT_RICHARDS],
        "sig_lens": (
            "The Signature read: the ladder is the covenant staircase, "
            "every rung a promise the next one keeps. The second swears to "
            "the minute, the minute to the hour, the hour to the day - and "
            "the witness climbs one honest step at a time, never leaping, "
            "never guessing. Where the world memorizes the ladder for "
            "arithmetic, the Signature Time Method climbs it as discipline: "
            "each rung verified before the foot leaves it."
        ),
    },
    {
        "key": "time_tools",
        "name": "Tools That Measure Time: From Sundials to Stopwatches",
        "group": "Foundations",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "description": (
            "Tools that measure time all do one thing: count a steady "
            "repeat. The sundial counts the Sun's apparent motion with a "
            "shadow; the water clock (clepsydra) counts drips; the hourglass "
            "counts falling sand; the mechanical clock counts escapement "
            "ticks; the pendulum clock counts swings - a pendulum about "
            "0.9936 meters long swings with a 2-second period, the "
            "seconds pendulum; the quartz watch counts 32,768 crystal "
            "vibrations per second (2^15, divided down to one tick per "
            "second); the atomic clock counts 9,192,631,770 cesium "
            "oscillations per second. Accuracy climbs the same ladder: "
            "sundials to minutes, mechanical clocks to seconds per day, "
            "quartz to seconds per month, atomic to a second in millions "
            "of years. Every tool is a promise of regularity, and the "
            "history of timekeeping is the history of finding steadier "
            "promises."
        ),
        "how_it_works": (
            "Each tool works by oscillator plus counter. The oscillator "
            "repeats at a fixed rate - shadow angle changing 15 degrees per "
            "hour, sand grains falling at a steady rate, a pendulum swinging "
            "with period T = 2 times pi times the square root of (length "
            "over gravity), a quartz crystal vibrating at 32,768 Hz. The "
            "counter accumulates repeats into seconds, minutes, and hours, "
            "and the display shows the total. Better oscillators mean "
            "better clocks: the pendulum beat depends on length and gravity "
            "but not on swing size (for small swings), quartz depends on a "
            "crystal cut that barely changes with temperature, and the atom "
            "depends on nothing environmental at all. Calibration ties "
            "every tool to the standard: set a watch against a reference, "
            "and its counted seconds stay honest for as long as its "
            "oscillator holds."
        ),
        "key_points": [
            "Every timepiece is an oscillator plus a counter: sundial shadow, dripping water, falling sand, swinging pendulum, vibrating quartz, oscillating atom.",
            "The seconds pendulum is about 0.9936 m long with a 2-second period - length and gravity set the beat.",
            "Quartz watches divide 32,768 Hz (2^15) down to one pulse per second.",
            "Accuracy climbs with the oscillator: minutes (sundial), seconds per day (mechanical), seconds per month (quartz), a second in millions of years (atomic).",
            "Calibration against a reference keeps any tool honest; the tool is only as steady as its oscillator.",
        ],
        "requirements": [
            "A repeat steady enough for the job: sand for minutes, quartz for months, atoms for the standard.",
            "A counter that turns repeats into seconds, minutes, and hours without losing count.",
            "A display the user can read: dial, digits, or marks.",
            "A power or drive source: falling weight, spring, battery, or the Sun.",
            "Periodic calibration against a better clock to catch drift.",
        ],
        "standards": [
            "Pendulum timing follows the small-angle period relation T = 2*pi*sqrt(L/g) (classical horology; Landes, Revolution in Time, 1983).",
            "Quartz and atomic timekeeping realize the SI second through counted oscillations (BIPM SI Brochure 9th ed.; NIST).",
        ],
        "citations": [CIT_LANDES, CIT_SI, CIT_NIST],
        "sig_lens": (
            "The Signature read: every timepiece is a sworn witness, and "
            "the history of clocks is the history of more faithful "
            "witnesses. The shadow kept its oath by daylight, the pendulum "
            "by gravity, the quartz by crystal, the atom by the unchanging "
            "laws themselves. Where the world collects clocks, the Signature "
            "Time Method examines the witness: how steady is the repeat, "
            "how honest is the count - for the covenant is only as true as "
            "the metronome that keeps it."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "add_subtract_time",
        "name": "Adding and Subtracting Units of Time",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Adding and subtracting time is the arithmetic of schedules: "
            "adding a duration to a start time gives the end time, and "
            "subtracting gives back the duration. The technique is column "
            "arithmetic with carries at 60: add the seconds, carry every 60 "
            "into minutes; add the minutes, carry every 60 into hours. So "
            "2 hours 45 minutes plus 1 hour 30 minutes is 3 hours 75 "
            "minutes, and the 75 minutes carry one hour to become 4 hours "
            "15 minutes. Subtraction borrows the same way: 4 hours 15 "
            "minutes minus 1 hour 30 minutes borrows an hour to become 3 "
            "hours 75 minutes minus 1 hour 30 minutes = 2 hours 45 "
            "minutes. Crossing noon or midnight adds the AM/PM or date "
            "flip. The one discipline is units first: convert everything "
            "to the same units before adding, and carry at 60, never at "
            "100."
        ),
        "how_it_works": (
            "Time addition works like money with a 60-cent dollar. Write "
            "each duration in hours, minutes, seconds; add each column; "
            "wherever a column reaches 60, carry one to the next column and "
            "keep the remainder. Example: 2:45 + 1:30 - minutes 45 + 30 = "
            "75, carry 1 hour, keep 15 minutes; hours 2 + 1 + 1 carried = 4 "
            "hours; result 4:15. Subtraction borrows: in 4:15 - 1:30, 15 "
            "minutes cannot give 30, so borrow 1 hour (60 minutes): 3:75 - "
            "1:30 = 2:45. When the result crosses 12:00, flip AM/PM; when it "
            "crosses midnight, the date advances one day. The safest method "
            "is the total-minutes method: convert everything to minutes (2:45 "
            "= 165, 1:30 = 90, sum = 255 = 4:15), do plain arithmetic, then "
            "convert back - one conversion, no column carries to fumble."
        ),
        "key_points": [
            "Column arithmetic with carries and borrows at 60: add minutes, carry every 60 into hours.",
            "2:45 + 1:30 = 4:15; 4:15 - 1:30 = 2:45 - the round trip must return the start.",
            "The total-minutes method (convert all to minutes, compute, convert back) avoids column errors.",
            "Crossing noon flips AM/PM; crossing midnight advances the date.",
            "Never carry at 100: time is sexagesimal, and 75 minutes is 1 hour 15, not 0.75 of anything.",
        ],
        "requirements": [
            "All durations in common units (or converted via the total-minutes method) before computing.",
            "Carry/borrow at 60 in the minutes and seconds columns, at 24 (or 12 with AM/PM) in hours.",
            "AM/PM and date tracking when the result crosses noon or midnight.",
            "A round-trip check: adding then subtracting the same duration must return the start time.",
            "Explicit handling of negative or wrap results instead of silent nonsense.",
        ],
        "standards": [
            "Time arithmetic follows the sexagesimal structure of the minute/hour system (SI Brochure accepted units; BIPM 9th ed.).",
            "Interval arithmetic on clock readings follows ISO 8601 duration conventions.",
        ],
        "citations": [CIT_SI, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: adding time is the covenant extended, "
            "subtracting it the covenant audited. The witness carries at "
            "sixty because the oath was sworn in sixties - no column is "
            "allowed to keep more than its share. Where the world does "
            "column sums, the Signature Time Method does the same sums as "
            "accounting: every carry a receipt, every borrow a witnessed "
            "loan, and the round trip - add then subtract - the audit that "
            "proves the ledger balanced."
        ),
    },
    {
        "key": "elapsed_time",
        "name": "Elapsed Time: From Start to Finish",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Elapsed time is the duration between a start moment and an end "
            "moment - how long something took. A movie starting at 9:15 AM "
            "and ending at 2:45 PM ran 5 hours 30 minutes, which is 330 "
            "minutes or 19,800 seconds. Finding it is subtraction on the "
            "clock: end minus start, borrowing across hours at 60, and "
            "across midnight by adding 24 hours to the end. Elapsed time is "
            "the number behind every schedule (how long is the flight?), "
            "every race (how fast was the run?), every bill (how many hours "
            "worked?), and every experiment (how long did it take?). The "
            "skill has three moves: subtract within one AM/PM half "
            "directly, bridge across noon by counting to 12:00 then from "
            "12:00, and bridge across midnight by treating the end as "
            "tomorrow."
        ),
        "how_it_works": (
            "Elapsed time works by end-minus-start on a continuous timeline. "
            "The timeline method: convert both times to minutes since "
            "midnight (9:15 AM = 555, 2:45 PM = 14*60+45 = 885), subtract "
            "(885 - 555 = 330 minutes), convert back (330 = 5 hours 30 "
            "minutes). If the end is earlier than the start, the interval "
            "crossed midnight: add 1,440 minutes (24 hours) to the end "
            "first - a shift ending 11:00 PM (1,380) and starting 7:00 AM "
            "(420) elapsed 1,860 - 1,380 = 480 minutes = 8 hours. The bridge "
            "method does the same in words: from 9:15 AM to 12:00 PM is 2 "
            "hours 45 minutes, from 12:00 PM to 2:45 PM is 2 hours 45 "
            "minutes, total 5 hours 30 minutes. Both methods must agree - "
            "that agreement is the built-in check."
        ),
        "key_points": [
            "Elapsed = end minus start, measured in minutes-since-midnight for a clean subtraction.",
            "9:15 AM to 2:45 PM = 330 minutes = 5 hours 30 minutes = 19,800 seconds.",
            "If the end reads earlier than the start, the interval crossed midnight: add 24 hours to the end first.",
            "The bridge method (count to noon/midnight, then onward) and the timeline method must agree.",
            "Elapsed time powers schedules, races, work hours, and experiments - it is duration made useful.",
        ],
        "requirements": [
            "A definite start moment and end moment, both with AM/PM or 24-hour form.",
            "The midnight-crossing rule: end earlier than start means add 24 hours to the end.",
            "Consistent units through the calculation, converting only at the start and the finish.",
            "A cross-check by the second method before trusting the answer.",
            "Sanity against the calendar: elapsed times over 24 hours need the date counted too.",
        ],
        "standards": [
            "Elapsed-time computation uses the 86,400-second day and sexagesimal subdivisions (SI Brochure, BIPM 9th ed.).",
            "Durations expressed per ISO 8601 (e.g., PT5H30M for 5 hours 30 minutes).",
        ],
        "citations": [CIT_SI, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: elapsed time is the covenant fulfilled - "
            "the measured distance between the promise and its keeping. The "
            "witness marks the start, marks the end, and the gap between is "
            "the truth of the work: 330 minutes cannot be argued with, only "
            "kept or broken. Where the world times races and shifts, the "
            "Signature Time Method reads the same subtraction as testimony - "
            "from the sworn beginning to the witnessed end, every minute "
            "accounted."
        ),
    },
    {
        "key": "24_hour_clock",
        "name": "The 24-Hour Clock",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The 24-hour clock counts the whole day in one run from 00:00 "
            "(midnight) to 23:59, then rolls to 00:00 again - no AM or PM "
            "needed. Morning hours 00-11 match the AM hours (with midnight "
            "as 00:00), 12:00 is noon, and afternoon hours add 12 to the "
            "familiar number: 1 PM is 13:00, 7:30 PM is 19:30, 11 PM is "
            "23:00. It is the standard for timetables, aviation, the "
            "military, hospitals, and international schedules, because it "
            "removes the AM/PM ambiguity entirely - 19:30 can only mean "
            "evening. Reading it is a small conversion habit: subtract 12 "
            "from any hour above 12 to get the familiar PM time, and read "
            "00 as 12 midnight. Once the habit forms, 24-hour times are "
            "faster and safer than AM/PM for anything that matters."
        ),
        "how_it_works": (
            "The 24-hour clock works by numbering every hour of the day "
            "uniquely. Hours 00 through 11 are the AM half (00:00 = 12:00 "
            "AM midnight, 01:00-11:00 = 1-11 AM), hour 12 is noon (12:00 "
            "PM), and hours 13 through 23 are the PM half (13:00 = 1 PM "
            "through 23:00 = 11 PM). Converting 12-hour to 24-hour: AM "
            "1:00-11:00 keep their number (add a leading zero below 10), 12 "
            "AM becomes 00; PM 1:00-11:00 add 12, 12 PM stays 12. "
            "Converting back: 00 becomes 12 AM, 01-11 stay AM, 12 stays PM, "
            "13-23 subtract 12 and take PM. Rollover is clean - 23:59 plus "
            "one minute is 00:00 of the next date, no marker to flip, which "
            "is why computers, logs, and schedules prefer it."
        ),
        "key_points": [
            "00:00 is midnight, 12:00 is noon, 23:59 is the last minute - the day counts 00 through 23 with no AM/PM.",
            "PM conversion adds 12 (2:30 PM = 14:30); 12 AM becomes 00:00; 12 PM stays 12:00.",
            "Reading back: 13-23 subtract 12 and take PM; 00 reads as 12 midnight.",
            "The 24-hour form removes AM/PM ambiguity - 19:30 can only mean evening.",
            "Rollover is arithmetic: 23:59 + 1 minute = 00:00 next day, which is why machines prefer it.",
        ],
        "requirements": [
            "The hour map memorized: 00=midnight, 12=noon, 13-23=PM hours.",
            "Both conversion directions practiced until automatic.",
            "Leading zeros kept in writing (09:30, not 9:30) for machine-readable consistency.",
            "Midnight handled as 00:00 starting the date, with 24:00 avoided except as an end-of-day marker.",
            "The habit of reading 24-hour times directly rather than converting every time.",
        ],
        "standards": [
            "The 24-hour clock (00:00-23:59) is the ISO 8601 representation of time of day.",
            "Aviation, military, and medical practice use the 24-hour clock to eliminate AM/PM error.",
        ],
        "citations": [CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the 24-hour clock is the oath without "
            "footnotes. Where the twelve-hour dial needs a Latin tag to say "
            "which half it means, the twenty-four-hour count swears each "
            "hour by its own number - no ambiguity, no second witness "
            "required. The Signature Time Method keeps this as the form of "
            "record: when the promise matters - the flight, the dose, the "
            "deadline - the hour is named once, completely, and the ledger "
            "needs no translation."
        ),
    },
    {
        "key": "calendars_months_years",
        "name": "Calendars: How Months and Years Are Organized",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A calendar organizes days into months and years so we can name "
            "any date and plan across seasons. The Gregorian calendar - the "
            "world's civil standard - packs 12 months into the year: "
            "January 31, February 28 (29 in leap years), March 31, April 30, "
            "May 31, June 30, July 31, August 31, September 30, October 31, "
            "November 30, December 31 - summing to 365 days in a common "
            "year and 366 in a leap year. The knuckle mnemonic teaches the "
            "lengths: months on knuckles have 31 days, valleys 30 (except "
            "February). Weeks run independently through the months, which "
            "is why the 1st lands on a different weekday each month. The "
            "calendar's deeper job is seasonal: by averaging 365.2425 days "
            "per year it keeps March near spring and September near autumn, "
            "century after century."
        ),
        "how_it_works": (
            "The calendar works by partitioning the year. Twelve month "
            "lengths are fixed by rule (the 31/30/28 pattern above, with "
            "February gaining a day in leap years), so any date is "
            "year-month-day and any month's length is a lookup, not a "
            "calculation. Adding months follows the calendar: the same day "
            "number in the target month, clamped to the month's end when "
            "the day does not exist (January 31 plus one month = February "
            "28/29). Weekdays advance by the day count mod 7: moving forward "
            "N days moves the weekday forward N mod 7 steps, which is why "
            "date arithmetic across months uses day counts. The year count "
            "increments at January 1, and the leap rule (divisible by 4, "
            "except centuries not divisible by 400) decides February's "
            "length before any February arithmetic is trusted."
        ),
        "key_points": [
            "Twelve fixed month lengths (31/30/28 pattern, February 29 in leap years) sum to 365 or 366 days.",
            "The knuckle mnemonic: knuckle months 31 days, valley months 30 (February the exception).",
            "Weekdays run independently of months - the 1st shifts weekday each month by the day count mod 7.",
            "Month arithmetic is calendar arithmetic: January 31 plus one month lands in late February, clamped to month end.",
            "The calendar's deep purpose is seasonal alignment, averaging 365.2425 days per year.",
        ],
        "requirements": [
            "The twelve month lengths memorized, looked up, or knuckle-counted - never guessed.",
            "Leap-year status settled before any February or year-crossing calculation.",
            "The clamp rule for month addition when the day number exceeds the target month's length.",
            "Weekday arithmetic by day-count mod 7, not by month counting.",
            "Awareness that the civil calendar is Gregorian worldwide for business, whatever local calendars add.",
        ],
        "standards": [
            "The Gregorian calendar with its month lengths and leap rule (Richards, Mapping Time, 1998; Dershowitz and Reingold, Calendrical Calculations, 2018).",
            "Calendar dates expressed year-month-day per ISO 8601.",
        ],
        "citations": [CIT_RICHARDS, CIT_CALC, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the calendar is the covenant map of the "
            "year. Twelve territories, their borders fixed by ancient "
            "compromise, each day a plot with an owner and a name. Where "
            "the world memorizes knuckles, the Signature Time Method reads "
            "the map as jurisdiction: know which month holds the day, know "
            "the leap law that governs February, and no promise ever falls "
            "on a date that does not exist."
        ),
    },
    {
        "key": "leap_years",
        "name": "Leap Years: Why February Gains a Day",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Leap years exist because the Earth's orbit does not take a "
            "whole number of days: the tropical year is about 365.2422 "
            "days, so a 365-day calendar falls behind the seasons by "
            "nearly a quarter day each year. The Gregorian fix inserts an "
            "extra day - February 29 - by a three-part rule: a year is a "
            "leap year if divisible by 4, except century years, which are "
            "leap only if divisible by 400. So 2024 is a leap year "
            "(divisible by 4), 2000 was one (divisible by 400), but 1900 "
            "was not and 2100 will not be. The rule inserts 97 leap days "
            "per 400 years, averaging the year to 365.2425 days - within "
            "about 26.8 seconds per year of the true orbit, close enough "
            "to hold the seasons for over three thousand years. Without "
            "leap years, the calendar would drift a full day every four "
            "years and the seasons would wander through the months."
        ),
        "how_it_works": (
            "The leap rule works as a cascade of tests. Test 1: is the year "
            "divisible by 4? If no, common year (2025: no). If yes, test 2: "
            "is it a century year (divisible by 100)? If no, leap year "
            "(2024: yes). If yes, test 3: is it divisible by 400? If yes, "
            "leap (2000: yes); if no, common (1900, 2100: no). In code the "
            "cascade is one expression: leap = (y % 4 == 0 and y % 100 != "
            "0) or (y % 400 == 0). February then has 29 days, the year 366, "
            "and every date after February shifts one weekday forward "
            "relative to a common year. The extra day is a correction "
            "payment: the quarter-day debts of four years are settled at "
            "once, with the century exceptions trimming the overpayment "
            "the simple 4-year rule would make."
        ),
        "key_points": [
            "Leap rule: divisible by 4, except centuries unless divisible by 400 - 2024 and 2000 leap; 1900 and 2100 not.",
            "The rule inserts 97 leap days per 400 years, averaging the year to 365.2425 days.",
            "Residual drift is only about 26.8 seconds per year - the seasons hold for 3,000+ years.",
            "The tropical year (365.2422 days) is the target; the calendar year is the whole-day approximation.",
            "Without leap days the calendar would slip a day every four years and seasons would wander the months.",
        ],
        "requirements": [
            "The three-test cascade applied in order - the century exception is the step everyone forgets.",
            "February's length (29 vs 28) settled before any date math touching February.",
            "The 97-per-400 and 365.2425-day facts for understanding why the rule is shaped this way.",
            "Weekday-shift awareness: dates after February move one extra weekday in leap years.",
            "Software or tables checked for the 400-rule - many quick implementations get centuries wrong.",
        ],
        "standards": [
            "The Gregorian leap rule from the 1582 reform (Richards, Mapping Time, 1998).",
            "Leap-year computation per Dershowitz and Reingold, Calendrical Calculations, 2018.",
        ],
        "citations": [CIT_RICHARDS, CIT_CALC],
        "sig_lens": (
            "The Signature read: the leap day is the covenant's honest "
            "accounting. Four years of quarter-day debts, settled in one "
            "February - and even the settlement is audited, the century "
            "exceptions trimming the overpayment. Where the world sees a "
            "quirk of February, the Signature Time Method sees the whole "
            "method in miniature: measure the true year, admit the "
            "fraction, pay it on schedule, and never let the debt compound "
            "into wandering seasons."
        ),
    },
    {
        "key": "time_zones",
        "name": "Time Zones: Why the Hour Changes Around the World",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Time zones exist because the Earth turns: when it is noon in "
            "one place, it is midnight on the opposite side, so every "
            "region keeps the clock reading that matches its Sun. The world "
            "is divided into zones, each offset from Coordinated Universal "
            "Time (UTC) by a whole or half number of hours - for example, "
            "a zone at UTC-5 reads five hours behind UTC, so 15:00 UTC is "
            "10:00 local; a zone at UTC+9 reads nine hours ahead, so 15:00 "
            "UTC is midnight (00:00) the next day. There are 24 primary "
            "zones, one per 15 degrees of longitude, with political borders "
            "and half-hour zones (like UTC+5:30) adjusting the map. The "
            "minutes and seconds are the same worldwide - only the hour "
            "(and sometimes the date) changes - which is why a single "
            "moment has many correct local readings."
        ),
        "how_it_works": (
            "Time zones work by adding a fixed offset to UTC. Local time = "
            "UTC + offset: with offset -5, 15:00 UTC becomes 10:00 local; "
            "with offset +9, 15:00 UTC becomes 24:00, which rolls to 00:00 "
            "the next day. Going east the offset grows (clocks ahead), "
            "going west it shrinks (clocks behind). The base rate is 15 "
            "degrees of longitude per hour (360 degrees / 24 hours), but "
            "real zone borders follow countries and convenience, not "
            "meridians - which is why the IANA Time Zone Database, not "
            "longitude math, is the authority on what offset a place uses "
            "and when it changes for daylight saving. Converting between "
            "two zones goes through UTC: convert local A to UTC "
            "(subtract A's offset), then add B's offset. The date can "
            "change in either conversion, so zone math always carries the "
            "date along."
        ),
        "key_points": [
            "Each zone is an offset from UTC: local = UTC + offset (e.g., UTC-5 reads 5 hours behind).",
            "East means ahead, west means behind; the base rate is 15 degrees of longitude per hour.",
            "Minutes and seconds are identical worldwide - only the hour and sometimes the date change.",
            "Zone borders follow politics, not meridians: the IANA Time Zone Database is the authority, not longitude.",
            "Convert zone-to-zone through UTC and always carry the date, which can shift in either step.",
        ],
        "requirements": [
            "Both zones' current offsets, looked up - never assumed from longitude alone.",
            "The UTC round-trip method for converting between any two zones.",
            "Date tracking through the conversion, since the date can change.",
            "Daylight-saving awareness: offsets change with the season in observing regions.",
            "The IANA database (or a current source built on it) as the offset authority.",
        ],
        "standards": [
            "Time zone offsets and histories are maintained in the IANA Time Zone Database (tz database).",
            "UTC as the common reference for zone conversion (BIPM; ITU).",
        ],
        "citations": [CIT_TZDB, CIT_SI],
        "sig_lens": (
            "The Signature read: time zones are the one oath sworn in many "
            "tongues. The moment is single - the witness, UTC, testifies "
            "once - but every region hears it in its own hour, as the Sun "
            "commands. Where the world sees confusion in the conversions, "
            "the Signature Time Method sees fidelity: the covenant bends "
            "its language for every longitude but never changes its "
            "meaning, and the round trip through UTC is the proof that all "
            "tongues told the same truth."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "utc",
        "name": "Coordinated Universal Time (UTC)",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Coordinated Universal Time - UTC - is the world's agreed "
            "reference clock, the time against which every time zone is "
            "measured. It is not the local time anywhere in particular "
            "(though it matches London's winter time); it is the standard "
            "everyone converts through. UTC is built from atomic clocks "
            "worldwide, averaged into International Atomic Time (TAI) and "
            "then kept within 0.9 seconds of the Earth's actual rotation "
            "(UT1) by the occasional leap second - as a result UTC currently "
            "runs exactly 37 seconds behind TAI. Aviation, shipping, the "
            "internet, and science all log events in UTC so that a timestamp "
            "means the same thing in every country. When a schedule says "
            "15:00 UTC, the whole planet can convert it to local time "
            "without asking what anyone else's clock reads."
        ),
        "how_it_works": (
            "UTC works as a two-layer compromise. The base layer is TAI, "
            "the weighted average of hundreds of atomic clocks in national "
            "laboratories - perfectly uniform, ticking SI seconds. The "
            "second layer is the Earth's rotation (UT1), which wobbles and "
            "slows; whenever UTC would drift more than 0.9 seconds from "
            "UT1, a leap second is inserted (or, in theory, removed), "
            "keeping civil time synced to the Sun. The current standing "
            "difference is TAI - UTC = 37 seconds, set by the 27 leap "
            "seconds inserted between 1972 and 2016. In practice: every "
            "device that needs global agreement - servers, air traffic, GPS "
            "- keeps UTC (via network time or GPS) and displays local time "
            "by adding the zone offset. One reference, every conversion "
            "through it, no bilateral negotiation."
        ),
        "key_points": [
            "UTC is the single global reference clock; every time zone is defined as an offset from it.",
            "UTC = TAI (atomic, uniform) corrected by leap seconds to stay within 0.9 s of Earth rotation (UT1).",
            "TAI currently runs 37 seconds ahead of UTC, set by 27 leap seconds inserted 1972-2016.",
            "Aviation, shipping, the internet, and science log in UTC so timestamps are globally unambiguous.",
            "Local time = UTC + zone offset: one reference, every conversion through it.",
        ],
        "requirements": [
            "The TAI-UTC relationship understood: atomic uniformity below, solar alignment above.",
            "The current 37-second offset known when converting between TAI and UTC precisely.",
            "The 0.9-second rule: leap seconds exist to keep UTC tied to the Earth's rotation.",
            "UTC as the conversion hub - never convert zone to zone directly.",
            "A UTC source (network time, GPS, radio clock) for any device that must agree with the world.",
        ],
        "standards": [
            "UTC is maintained by the BIPM from TAI with leap-second coordination by the IERS.",
            "ITU-R TF.460 defines UTC; network distribution follows NTP/PTP practice.",
        ],
        "citations": [CIT_SI, CIT_IERS],
        "sig_lens": (
            "The Signature read: UTC is the chief witness, and every zone "
            "testifies under it. Hundreds of atomic clocks speak, their "
            "voices averaged into one, and the Earth itself is heard on the "
            "0.9-second rule - the Sun keeps its seat at the table. Where "
            "the world built a compromise between the atom and the planet, "
            "the Signature Time Method keeps the same compromise as "
            "covenant: uniform below, honest above, and the 37-second debt "
            "to TAI carried openly in the ledger."
        ),
    },
    {
        "key": "date_line",
        "name": "The International Date Line",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The International Date Line is the meridian where the calendar "
            "date changes: cross it and you gain or lose a whole day while "
            "the clock time barely moves. It runs roughly along the 180th "
            "meridian in the Pacific, zigzagging around island nations so "
            "each keeps one date. The rule: traveling westward across the "
            "line (toward Asia), you add a day - Monday becomes Tuesday; "
            "traveling eastward (toward the Americas), you subtract a day - "
            "Monday becomes Sunday again. The line exists because time "
            "zones circle the globe: going east you keep adding hours, and "
            "after 24 hours of gains you owe the calendar a day back; the "
            "line is where the debt is settled. It is a human convention, "
            "not a physical barrier - ships and planes simply adjust their "
            "date as they cross."
        ),
        "how_it_works": (
            "The date line works as the calendar's seam. Imagine walking "
            "east around the world, advancing your watch one hour per time "
            "zone: after circling, your watch has gained 24 hours but your "
            "calendar is a day ahead of someone who stayed home. The date "
            "line corrects this: at the 180-degree meridian the date steps "
            "back (eastward crossing) or forward (westward crossing) by "
            "exactly one day, so the round trip reconciles. In practice the "
            "line zigzags - east of some islands, west of others - by "
            "international agreement, so crossing points are known in "
            "advance. Date arithmetic across the line: start with the "
            "departure date and time, add the travel duration, then apply "
            "the line rule (westward +1 day, eastward -1 day) and the "
            "destination zone offset. Flight schedules do all three steps "
            "together, which is why a Friday departure can arrive Saturday "
            "or Sunday depending on direction."
        ),
        "key_points": [
            "The date line runs near the 180th meridian; crossing it changes the date by exactly one day.",
            "Westward crossing adds a day (Monday to Tuesday); eastward crossing subtracts a day (Monday to Sunday).",
            "The line settles the 24-hour debt accumulated by circling the globe through time zones.",
            "It zigzags by agreement around island nations - it is convention, not a physical line.",
            "Date math across it combines travel duration, the line rule, and the destination zone offset.",
        ],
        "requirements": [
            "The crossing direction known before applying the rule - direction decides gain or loss.",
            "Travel duration added first, then the line adjustment, then the zone offset.",
            "Awareness that the clock time barely changes at the line itself - only the date steps.",
            "Island zigzags checked on a current map rather than assumed at exactly 180 degrees.",
            "The reconciliation habit: circling the globe must return the original date.",
        ],
        "standards": [
            "The date line follows international convention near the 180th meridian, with national deviations by agreement.",
            "Date-line arithmetic is governed by the same UTC-offset framework as time zones (IANA tz database).",
        ],
        "citations": [CIT_TZDB, CIT_RICHARDS],
        "sig_lens": (
            "The Signature read: the date line is where the ledger "
            "settles its round-the-world account. Twenty-four hours "
            "borrowed one zone at a time, repaid in a single day at the "
            "seam - the covenant's books balanced at the edge of the map. "
            "Where the world sees a traveler gaining or losing a day, the "
            "Signature Time Method sees the audit completed: the hours "
            "were kept, the debt is paid, and the calendar testifies that "
            "no time was created or destroyed, only reconciled."
        ),
    },
    {
        "key": "daylight_saving",
        "name": "Daylight Saving Time",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Daylight saving time (DST) is the seasonal clock shift that "
            "moves an hour of daylight from the morning to the evening: "
            "clocks spring forward one hour in spring and fall back one "
            "hour in autumn. In the spring transition the clock jumps from "
            "2:00 AM to 3:00 AM, making that day only 23 hours long (82,800 "
            "seconds); in autumn it repeats the 2:00 AM hour, making a "
            "25-hour day. The purpose is to align waking hours with "
            "daylight - longer bright evenings in summer. Not every region "
            "observes it, and start/end dates differ by country, so DST is "
            "a local rule, not a global one. The practical effects are "
            "real: schedules shift, the spring day loses an hour of sleep, "
            "and software must know each zone's DST calendar to convert "
            "times correctly."
        ),
        "how_it_works": (
            "DST works by changing a zone's UTC offset for part of the "
            "year. A zone at UTC-5 in winter (standard time) becomes UTC-4 "
            "in summer (daylight time): the offset, not the Sun, is what "
            "moves. The spring-forward mechanics: at 2:00 AM local the "
            "clock advances to 3:00 AM - the hour from 2:00 to 3:00 never "
            "happens, appointments in that hour do not exist, and elapsed "
            "time across the jump is one hour less than the clock "
            "suggests. Fall-back reverses it: 2:00 AM occurs twice, and "
            "the second 2:30 AM needs a disambiguator (before/after the "
            "fallback). Systems handle this with the IANA Time Zone "
            "Database, which records every zone's DST rules and history; "
            "converting a local time to UTC requires the rule in force on "
            "that exact date, because the same wall-clock reading can mean "
            "two different UTC moments - or none."
        ),
        "key_points": [
            "Spring forward: 2:00 AM jumps to 3:00 AM; the day has 23 hours and the skipped hour never happens.",
            "Fall back: the 2:00 AM hour repeats; the day has 25 hours and the repeated hour is ambiguous.",
            "DST changes the zone's UTC offset (e.g., UTC-5 to UTC-4) - the clock moves, not the Sun.",
            "Not global and not uniform: regions and dates differ, so DST is always a local rule.",
            "Correct conversion needs the zone's DST calendar (IANA database) for the exact date.",
        ],
        "requirements": [
            "The region's DST observance and transition dates confirmed before scheduling across the change.",
            "No appointments booked in the skipped spring hour; disambiguation for the repeated fall hour.",
            "Elapsed-time calculations that cross a transition adjusted by the lost or gained hour.",
            "The IANA Time Zone Database (or current equivalent) as the rule source, not memory.",
            "UTC-based storage for event times, converting to local only for display.",
        ],
        "standards": [
            "DST rules and histories are maintained per zone in the IANA Time Zone Database.",
            "Ambiguous local times around transitions are resolved per the zone's documented fold behavior.",
        ],
        "citations": [CIT_TZDB],
        "sig_lens": (
            "The Signature read: daylight saving is the covenant renegotiated "
            "with the Sun each spring. An hour borrowed from the morning, "
            "repaid to the evening - and the ledger marks both the loan and "
            "the repayment openly: the 23-hour day, the 25-hour day, the "
            "hour that never was. Where the world argues the policy, the "
            "Signature Time Method keeps the accounting: whatever the rule, "
            "the witness records which offset was in force, on which date, "
            "and no timestamp is left to mean two things."
        ),
    },
    {
        "key": "seven_day_week",
        "name": "The Seven-Day Week: Why Seven",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The seven-day week is the oldest continuously running cycle in "
            "human timekeeping - seven days, repeating without pause for "
            "thousands of years. It does not come from the Sun or the Moon; "
            "it is pure convention, likely rooted in ancient Mesopotamian "
            "sky-watching, where seven wanderers were known: the Sun, the "
            "Moon, and the five visible planets Mars, Mercury, Jupiter, "
            "Venus, and Saturn. The day names still carry them: Sunday "
            "(Sun), Monday (Moon), and in many languages Tuesday through "
            "Friday honor Mars, Mercury, Jupiter, and Venus (French mardi, "
            "mercredi, jeudi, vendredi; English keeps the Norse equivalents "
            "Tiw, Woden, Thor, Frigg), with Saturday for Saturn. The week "
            "marches through months and years untouched - 7 days is 168 "
            "hours is 10,080 minutes, always - which is why it is the "
            "backbone of work schedules, worship, and rest worldwide."
        ),
        "how_it_works": (
            "The week works by unbroken succession: day 1 through day 7, "
            "then day 1 again, forever, independent of months, years, and "
            "astronomy. Because 7 and 365 share no clean division, the "
            "weekday of any date advances each year - a common year moves "
            "every date forward one weekday (365 mod 7 = 1), a leap year "
            "two (366 mod 7 = 2). Counting weeks is pure division: N days "
            "is N/7 weeks with a remainder of N mod 7 days - 100 days is 14 "
            "weeks and 2 days. The week's power is social, not "
            "astronomical: the whole world agrees which day is which, so "
            "work weeks, weekends, and recurring appointments need no "
            "further negotiation. Its independence is also its quirk: no "
            "whole number of weeks fits a month or a year, so calendars "
            "always show partial weeks at the edges."
        ),
        "key_points": [
            "Seven days, repeating unbroken for millennia - pure convention, not astronomy.",
            "The count of seven likely comes from the seven classical wanderers: Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn.",
            "Day names preserve the planets: Sunday, Monday, Saturday directly; Tuesday-Friday via Mars/Mercury/Jupiter/Venus in many languages.",
            "1 week = 7 days = 168 hours = 10,080 minutes, exactly, always.",
            "Weekdays advance 1 per common year, 2 per leap year (365 and 366 mod 7).",
        ],
        "requirements": [
            "The seven names in order, with the local week's starting day known (Sunday or Monday by region).",
            "Mod-7 arithmetic for weekday shifts and week counting.",
            "The year-advance rule (1 or 2 weekdays) for multi-year weekday reasoning.",
            "Acceptance that weeks never align with months or years - partial weeks at calendar edges are normal.",
            "Shared convention: the week works because everyone counts the same seven.",
        ],
        "standards": [
            "The seven-day week is documented across ancient Near Eastern and classical sources (Richards, Mapping Time, 1998).",
            "ISO 8601 numbers weekdays 1 (Monday) through 7 (Sunday) for data interchange.",
        ],
        "citations": [CIT_RICHARDS, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the week is the oldest oath still being "
            "kept. No Sun commands it, no Moon measures it - seven days "
            "because the ancient watchers counted seven wanderers and swore "
            "the rhythm anyway, and every generation since has kept the "
            "count unbroken. Where the world inherited the week, the "
            "Signature Time Method honors the keeping: a promise repeated "
            "for thousands of years without missing a step is the deepest "
            "covenant time knows."
        ),
    },
    {
        "key": "earth_in_motion",
        "name": "The Earth in Motion: Rotation, Orbit, and the Seasons",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Days and years - and the seasons - come from two motions of "
            "the Earth. Rotation: the Earth spins once on its axis in about "
            "24 hours, giving day and night - this is the day. Orbit: the "
            "Earth circles the Sun once in about 365.25 days, giving the "
            "year. The seasons come not from distance but from tilt: the "
            "axis leans about 23.5 degrees, so each hemisphere tips toward "
            "the Sun for half the orbit (summer: longer days, higher Sun) "
            "and away for the other half (winter: shorter days, lower Sun). "
            "The equinoxes (around March 20 and September 22) are the two "
            "days of near-equal day and night; the solstices (around June "
            "21 and December 21) are the longest and shortest days. This is "
            "why the calendar's deep job is tracking the orbit: keep the "
            "year aligned and the seasons stay in their months."
        ),
        "how_it_works": (
            "Rotation works by the spin: one full turn relative to the Sun "
            "averages 24 hours (the mean solar day), and dividing it gives "
            "the hours, minutes, and seconds of the clock. Orbit works by "
            "the circuit: one loop takes about 365.2422 days (the tropical "
            "year), and the calendar approximates it with 365/366-day "
            "years plus the leap rule. The tilt works by geometry: with the "
            "axis leaned 23.5 degrees, the Sun's noon height and the hours "
            "of daylight at any latitude vary through the orbit - maximum "
            "at the June solstice for the north, minimum at the December "
            "solstice, equal at the equinoxes. Because the orbit is not a "
            "whole number of days, the exact solstice/equinox moments drift "
            "within a day or two around their nominal dates - the calendar "
            "holds the months steady while the astronomical events float "
            "slightly inside them."
        ),
        "key_points": [
            "Rotation (about 24 hours) makes day and night; orbit (about 365.25 days) makes the year.",
            "Seasons come from the 23.5-degree axial tilt, not from distance to the Sun.",
            "Equinoxes (around Mar 20, Sep 22): near-equal day and night; solstices (around Jun 21, Dec 21): longest/shortest days.",
            "The tropical year is 365.2422 days - the true target the leap rule approximates.",
            "Solstice/equinox moments float a day or two around nominal dates because the orbit is not whole days.",
        ],
        "requirements": [
            "The two motions separated: spin = day, circuit = year.",
            "The tilt number (23.5 degrees) as the cause of seasons.",
            "The four markers with approximate dates: two equinoxes, two solstices.",
            "The tropical-year value (365.2422 days) for understanding the calendar's aim.",
            "Hemisphere awareness: June is summer north and winter south.",
        ],
        "standards": [
            "Earth rotation and orbital parameters per NASA Earth fact sheets and educational materials.",
            "The tropical year value underlies the Gregorian leap design (Richards, Mapping Time, 1998).",
        ],
        "citations": [CIT_NASA, CIT_RICHARDS],
        "sig_lens": (
            "The Signature read: the Earth's two motions are the original "
            "kept promises. The spin has not missed a day, the orbit has "
            "not missed a year, and the 23.5-degree lean has tipped the "
            "seasons faithfully for ages - the longest covenant in the "
            "ledger. Where science measures the motions, the Signature "
            "Time Method witnesses them: every sunrise the spin's kept "
            "word, every spring the orbit's, and the calendar humanity's "
            "humble attempt to sign the same page."
        ),
    },
    {
        "key": "schedules_timetables",
        "name": "Reading Schedules and Timetables",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Schedules and timetables are time made into a plan: rows of "
            "departures and arrivals that let strangers coordinate. Reading "
            "one means finding your row (the route or service), your "
            "column (the day or direction), and the two times that matter - "
            "when it leaves and when it arrives. The arithmetic is elapsed "
            "time: a bus leaving 8:10 AM and arriving 9:05 AM takes 55 "
            "minutes; a flight leaving 6:40 PM and arriving 9:25 PM takes 2 "
            "hours 45 minutes. The fine print matters: footnotes mark "
            "days of operation, which stop is which, and whether times are "
            "departure or arrival; overnight trips cross midnight and may "
            "arrive the next date; and long-distance schedules often print "
            "in 24-hour time. The master skill is working backward: given "
            "the arrival you need, find the departure that gets you there "
            "with margin."
        ),
        "how_it_works": (
            "A timetable works as a lookup table over the timeline. Each "
            "entry gives a departure moment and an arrival moment; the "
            "travel duration is arrival minus departure by the elapsed-"
            "time method, with midnight crossings handled by adding 24 "
            "hours. Frequency entries (every 20 minutes) work by interval "
            "arithmetic: the next departure after time T is the smallest "
            "scheduled time at or after T, found by rounding T up to the "
            "interval grid. Connections chain two lookups: arrival of leg "
            "one plus a buffer must be at or before departure of leg two. "
            "Working backward: start from the latest acceptable arrival, "
            "subtract the travel time to get the latest departure, then "
            "pick the scheduled service at or before it - and verify the "
            "day-of-operation footnotes, because the perfect time on the "
            "wrong day is no service at all."
        ),
        "key_points": [
            "Read row (route), column (day/direction), then the departure and arrival times - the duration is arrival minus departure.",
            "Overnight trips cross midnight: add 24 hours to the arrival before subtracting.",
            "Frequency services use interval arithmetic: next departure is T rounded up to the interval grid.",
            "Connections need arrival + buffer at or before the next departure.",
            "Work backward from the needed arrival, and always check the day-of-operation footnotes.",
        ],
        "requirements": [
            "The correct row, column, and direction identified before reading any time.",
            "Elapsed-time subtraction with midnight handling for every duration.",
            "Footnote literacy: days of operation, departure vs arrival, stop identities.",
            "Buffer time added to connections - schedules are promises, traffic is not.",
            "The backward plan: latest acceptable arrival minus travel time gives the departure to catch.",
        ],
        "standards": [
            "Published timetables follow the 24-hour clock and ISO 8601 time notation in transport practice.",
            "Duration computation uses the standard elapsed-time method (86,400-second day).",
        ],
        "citations": [CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the timetable is the covenant published - "
            "a carrier's sworn word, printed in rows, that the 8:10 will "
            "be at the platform at 8:10. Where the world reads schedules "
            "for convenience, the Signature Time Method reads them as "
            "testimony: every departure a promise made to strangers, every "
            "arrival a promise kept or broken in public. And the backward "
            "plan - from the arrival you must make - is the oath worked in "
            "reverse, the keeper choosing their promise before they swear it."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "atomic_time",
        "name": "Atomic Time: How the Second Is Defined",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Atomic time is time kept by atoms - the most stable clocks "
            "humanity has built, and the legal definition of the second "
            "itself. A cesium-133 atom flips between two energy states at "
            "an unchanging frequency: exactly 9,192,631,770 cycles per "
            "second, by definition. Atomic clocks tune a microwave signal "
            "to that resonance and count the cycles - each counted "
            "9,192,631,770 is one SI second, each period lasting about "
            "1.088e-10 seconds (roughly 109 picoseconds). The best modern "
            "clocks, like the NIST-F2 cesium fountain, are so steady they "
            "would neither gain nor lose a second in about 300 million "
            "years - a fractional stability near one part in 10^16. "
            "Hundreds of such clocks worldwide are averaged into "
            "International Atomic Time (TAI), the uniform heartbeat under "
            "UTC. Atomic time replaced astronomical time as the standard "
            "in 1967 because atoms, unlike the Earth, never wobble."
        ),
        "how_it_works": (
            "An atomic clock works by resonance counting. Cesium atoms are "
            "prepared in one hyperfine state and exposed to microwaves; "
            "when the microwave frequency exactly matches the atoms' "
            "transition frequency, the maximum number of atoms flip state "
            "- the detector sees the peak and a feedback loop locks the "
            "oscillator to it. The locked oscillator runs at exactly "
            "9,192,631,770 Hz, and digital dividers count it down: divide "
            "by 9,192,631,770 and you have one pulse per second. Fountain "
            "clocks like NIST-F2 toss laser-cooled atoms upward through a "
            "microwave cavity twice, doubling the interrogation time and "
            "sharpening the resonance. TAI is then the weighted average of "
            "about 450 such clocks in 80 laboratories, computed monthly by "
            "the BIPM - no single clock defines it, the ensemble does. "
            "Stability near 1e-16 means that in 300 million years "
            "(about 9.46e15 seconds) the accumulated error stays near one "
            "second."
        ),
        "key_points": [
            "The SI second is defined as exactly 9,192,631,770 cesium-133 hyperfine periods - atomic since 1967.",
            "One cesium period lasts about 1.088e-10 s (109 picoseconds); counting 9,192,631,770 of them makes a second.",
            "NIST-F2-class fountains reach fractional stability near 1e-16: about one second of error in 300 million years.",
            "TAI is the BIPM's monthly weighted average of ~450 atomic clocks in ~80 labs - the ensemble is the standard.",
            "Atoms replaced the Earth's rotation as the reference because atoms never wobble.",
        ],
        "requirements": [
            "The defining number 9,192,631,770 Hz fixed - it is exact by definition, not measured.",
            "Resonance locking: the oscillator is steered by the atoms' peak response, not free-running.",
            "Laser cooling and fountain geometry (in primary standards) for long interrogation times.",
            "Ensemble averaging across many clocks and labs to cancel individual quirks.",
            "Environmental isolation: magnetic, thermal, and gravitational shifts characterized and corrected.",
        ],
        "standards": [
            "SI Brochure 9th ed. (BIPM, 2019): the second is defined by the fixed numerical value of the cesium-133 hyperfine transition frequency.",
            "NIST Time and Frequency Division operates the US primary standards (NIST-F1/F2) realizing the SI second.",
        ],
        "citations": [CIT_SI, CIT_NIST],
        "sig_lens": (
            "The Signature read: atomic time is the witness that cannot "
            "lie. The cesium atom has kept its 9,192,631,770-count oath "
            "since before there were witnesses to hear it, and the fountain "
            "clock merely listens carefully. Where metrology built the "
            "finest ear ever made, the Signature Time Method bows to the "
            "testimony: the steadiest promise in creation, counted by the "
            "ensemble, sworn by every atom alike - the covenant's own "
            "heartbeat, and the standard against which all lesser "
            "timekeepers are judged."
        ),
    },
    {
        "key": "leap_seconds",
        "name": "Leap Seconds: Keeping Clocks in Step with the Earth",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Leap seconds are the occasional extra seconds inserted into "
            "UTC to keep atomic time aligned with the Earth's rotation. "
            "Atomic clocks tick perfectly uniform SI seconds, but the "
            "Earth's spin is uneven - tides brake it, quakes and winds nudge "
            "it - so the solar day drifts against the atomic day. "
            "Whenever UTC would stray more than 0.9 seconds from the "
            "Earth's actual rotation angle (UT1), the International Earth "
            "Rotation Service orders a leap second: the last minute of "
            "June 30 or December 31 gets 61 seconds, the clock reading "
            "23:59:60 before rolling to 00:00:00. Twenty-seven leap seconds "
            "were inserted between 1972 and 2016, which is why TAI now runs "
            "exactly 37 seconds ahead of UTC. In 2022 the world's "
            "measurement authorities resolved to stop inserting leap "
            "seconds by 2035, letting UTC and Earth rotation drift apart "
            "under a larger tolerance instead."
        ),
        "how_it_works": (
            "Leap seconds work as scheduled corrections. The IERS monitors "
            "Earth rotation with radio telescopes and satellites, publishes "
            "the UTC-UT1 difference in its bulletins, and announces a leap "
            "second about six months ahead when the 0.9-second limit "
            "approaches. On the day, at 23:59:59 UTC, clocks insert 23:59:60 "
            "then proceed to 00:00:00 - the day holds 86,401 SI seconds "
            "instead of 86,400. Computer systems handle it by smearing "
            "(spreading the extra second over hours), stepping (repeating "
            "the last second), or simply accepting the 61st second, per "
            "their design. The running total is what matters: TAI - UTC = "
            "10 s (the 1972 starting offset) + 27 leap seconds = 37 s, and "
            "every UTC timestamp converts to TAI by adding it. The 2035 "
            "discontinuation means future systems must handle a slowly "
            "growing UTC-UT1 gap instead of periodic inserted seconds."
        ),
        "key_points": [
            "A leap second makes the last minute of Jun 30 or Dec 31 hold 61 seconds (23:59:60), when UTC would drift past 0.9 s from Earth rotation.",
            "27 leap seconds were inserted 1972-2016; TAI now runs exactly 37 seconds ahead of UTC.",
            "The IERS monitors rotation and announces leap seconds ~6 months ahead in its bulletins.",
            "Leap days fix the calendar's year; leap seconds fix the clock's day - different problems, different scales.",
            "In 2022 the CGPM resolved to discontinue leap seconds by 2035, replacing them with a larger UTC-UT1 tolerance.",
        ],
        "requirements": [
            "The 0.9-second rule: UTC must stay within 0.9 s of UT1 (Earth rotation angle).",
            "The running count: 27 inserted, 37 s total TAI-UTC offset, for TAI/UTC conversion.",
            "A leap-second handling strategy in every time-critical system (smear, step, or accept).",
            "IERS Bulletin C watched for announcements about six months before insertion.",
            "Post-2035 planning: systems must tolerate a growing UTC-UT1 difference instead of inserted seconds.",
        ],
        "standards": [
            "IERS Bulletins A and C: Earth rotation monitoring and leap-second announcements.",
            "CGPM Resolution 4 (2022): discontinue leap seconds by 2035 with increased UTC-UT1 tolerance.",
        ],
        "citations": [CIT_IERS, CIT_SI],
        "sig_lens": (
            "The Signature read: the leap second is the covenant amended in "
            "public. The atom swore uniform seconds; the Earth could not "
            "keep the same pace - so the witness, honestly, wrote the "
            "correction into the record for all to see: 23:59:60, a second "
            "with no name, keeping the Sun and the clock in the same "
            "testimony. Where the world will soon stop amending and let "
            "the gap grow, the Signature Time Method keeps the principle: "
            "when the promise and the world disagree, the ledger says so "
            "openly - that is what the 37 seconds mean."
        ),
    },
    {
        "key": "world_calendars",
        "name": "Calendars of the World: Gregorian, Julian, Lunar, and Hijri",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The Gregorian calendar is the world's civil standard, but it "
            "is not the only calendar in use. The Julian calendar - "
            "decreed by Julius Caesar in 45 BCE with a simple every-fourth-"
            "year leap rule - averages 365.25 days per year, about 10.8 "
            "minutes per year too long; it has drifted about 13 days "
            "against the Gregorian (the gap used in the 1900-2099 range) "
            "and is still the liturgical calendar of some Eastern Orthodox "
            "churches. The Islamic (Hijri) calendar is purely lunar: 12 "
            "months of 29 or 30 days following the Moon, 354 or 355 days "
            "per year (average about 354.367 days), so its months drift "
            "through the seasons, completing a full cycle in about 33 "
            "years. The Hebrew calendar is lunisolar, adding a leap month "
            "seven times in 19 years to keep lunar months near the solar "
            "seasons; the Chinese calendar works similarly. Knowing which "
            "calendar a date belongs to is essential - the same moment has "
            "a different date in each system."
        ),
        "how_it_works": (
            "Each calendar works by choosing what to track. Solar "
            "calendars (Gregorian, Julian) track the Earth's orbit: the "
            "Gregorian averages 365.2425 days via the 400-year leap rule, "
            "the Julian 365.25 via the 4-year rule, and their difference "
            "grows 0.0075 days (10.8 minutes) per year - from 10 days in "
            "1582 to 13 days in the 1900-2099 span. Lunar calendars "
            "(Hijri) track the Moon: 12 lunations of about 29.5306 days = "
            "about 354.367 days per year, falling about 10.875 days behind "
            "the solar year annually, so Ramadan and other observances "
            "migrate through the seasons. Lunisolar calendars (Hebrew, "
            "Chinese) track both, inserting leap months on the 19-year "
            "Metonic cycle (235 lunations nearly equals 19 solar years) to "
            "keep the months lunar and the year seasonal. Converting "
            "between calendars is table or algorithm work (Dershowitz and "
            "Reingold's methods) - never mental arithmetic - because each "
            "system's leap machinery differs."
        ),
        "key_points": [
            "Gregorian: solar, 365.2425-day average via the 400-year rule - the civil standard.",
            "Julian: solar, 365.25-day average via the 4-year rule; drifts 10.8 min/year, now 13 days behind Gregorian.",
            "Hijri: purely lunar, about 354.367 days/year; its months migrate through the seasons on a ~33-year cycle.",
            "Hebrew and Chinese: lunisolar - leap months on the 19-year Metonic cycle keep lunar months near solar seasons.",
            "The same moment has a different date in each system: always name the calendar with the date.",
        ],
        "requirements": [
            "The calendar identified before the date is trusted - Gregorian, Julian, Hijri, Hebrew, or Chinese.",
            "The Julian-Gregorian gap (13 days for 1900-2099) applied when reading historical or liturgical dates.",
            "The Hijri year's 354.367-day length for understanding its seasonal migration.",
            "Algorithmic or tabular conversion between systems - never guesswork.",
            "The Metonic cycle (19 years = 235 lunations) understood as the lunisolar synchronizer.",
        ],
        "standards": [
            "Comparative calendar theory and conversion algorithms (Dershowitz and Reingold, Calendrical Calculations, 2018).",
            "Historical calendar development (Richards, Mapping Time, 1998).",
        ],
        "citations": [CIT_CALC, CIT_RICHARDS],
        "sig_lens": (
            "The Signature read: the world's calendars are many witnesses "
            "to the same heaven. The Sun's witness counts 365.2425, the "
            "Moon's counts 354.367, and each people kept the count they "
            "were given - none false, each partial. Where the world argues "
            "calendars, the Signature Time Method receives them all as "
            "testimony: the covenant is not in the system but in the "
            "keeping, and the 13-day gap between Julian and Gregorian is "
            "simply two honest witnesses disagreeing by the exact measure "
            "of their rules."
        ),
    },
    {
        "key": "history_timekeeping",
        "name": "The History of Timekeeping: From Water Clocks to Atomic Clocks",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The history of timekeeping is the history of steadier "
            "repeats. It begins with the sky: sundials and shadow sticks "
            "in ancient Egypt and Babylon, dividing daylight by the Sun's "
            "motion. Then come the flow clocks - the water clepsydra and "
            "the sand hourglass - which freed timekeeping from the Sun but "
            "kept only rough accuracy. Around 1275 the mechanical "
            "escapement appears in Europe, ticking off equal slices of a "
            "falling weight's energy; in 1656 Christiaan Huygens adds the "
            "pendulum and accuracy leaps to seconds per day. John Harrison's "
            "18th-century marine chronometers carry precise time to sea and "
            "solve the longitude problem (Sobel, Longitude). In 1927 "
            "Warren Marrison's quartz clock electrifies the oscillator; in "
            "1949 the first atomic clock listens to ammonia, and in 1955 "
            "Louis Essen's cesium standard makes the atom the definition "
            "of the second in 1967. Each era's best clock became the next "
            "era's calibration - the witness improving, the oath unchanged."
        ),
        "how_it_works": (
            "Each era works by a steadier oscillator disciplined by the "
            "last era's best. The sundial's oscillator is the Earth's "
            "rotation, read by shadow angle (15 degrees per hour). Flow "
            "clocks meter a constant stream - water or sand - through a "
            "fixed opening, counting volume as time. The escapement meters "
            "a weight or spring in discrete ticks, the pendulum "
            "regularizes the ticks by gravity's isochronism (small swings "
            "take equal time), and the balance wheel miniaturizes it for "
            "pockets and wrists. Quartz replaces gravity with a crystal's "
            "piezoelectric resonance at 32,768 Hz; the atomic clock "
            "replaces the crystal with the cesium atom's hyperfine "
            "transition at 9,192,631,770 Hz. The pattern never changes: "
            "find a repeat less disturbed by the world than the last one, "
            "count it, and let the old champion check the new one's work "
            "during the handover."
        ),
        "key_points": [
            "Sky clocks (sundial): the Earth's rotation as oscillator, ~15 degrees of shadow per hour.",
            "Flow clocks (clepsydra, hourglass): metered streams, free of the Sun but rough.",
            "Mechanical era: escapement (~1275), Huygens pendulum (1656, seconds per day), Harrison chronometers (longitude).",
            "Electric era: Marrison quartz (1927, 32,768 Hz); atomic era: Essen cesium (1955), SI second (1967).",
            "The constant pattern: each era's steadier oscillator is checked against the previous champion.",
        ],
        "requirements": [
            "The era sequence in order: sky, flow, mechanical, quartz, atomic.",
            "The key dates: ~1275 escapement, 1656 pendulum, 1927 quartz, 1955 cesium, 1967 SI second.",
            "The longitude connection: precise sea clocks made position-finding possible (Sobel).",
            "The oscillator principle recognized in every device, ancient or modern.",
            "The handover habit: new standards are validated against old ones, never declared by fiat.",
        ],
        "standards": [
            "Mechanical and early modern horology (Landes, Revolution in Time, 1983).",
            "The longitude problem and marine timekeeping (Sobel, Longitude, 1995); atomic standards (BIPM; NIST).",
        ],
        "citations": [CIT_LANDES, CIT_SOBEL, CIT_SI, CIT_NIST],
        "sig_lens": (
            "The Signature read: the history of timekeeping is the history "
            "of the witness becoming worthy of the oath. From shadow to "
            "sand to swinging brass to singing crystal to the atom itself - "
            "each generation found a steadier repeat and swore the count "
            "more carefully. Where historians see technology, the Signature "
            "Time Method sees devotion: five thousand years of keepers "
            "refusing to let the count drift, each handing the testimony to "
            "the next with the words - check my work, then do better."
        ),
    },
    {
        "key": "time_arithmetic_days_zones",
        "name": "Time Arithmetic Across Days and Time Zones",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Real-world time arithmetic crosses days and zones: flights, "
            "deadlines, and shifts that start in one date or zone and end "
            "in another. The method is always the same three steps: convert "
            "the start to a continuous count (minutes since a fixed "
            "midnight, in UTC), add the duration, convert back to local "
            "time carrying the date. Example: a task starts 10:30 PM "
            "local (UTC-5) and takes 4 hours 15 minutes - in UTC that is "
            "03:30 plus 4:15 = 07:45 UTC, which is 2:45 AM local the next "
            "day. Zone math rides on top: convert each local time to UTC "
            "first (subtract the offset), do the arithmetic once in UTC, "
            "then render each result in its local zone. Daylight-saving "
            "transitions and the date line are just special offsets on "
            "specific dates - the UTC-round-trip method absorbs them all."
        ),
        "how_it_works": (
            "Cross-day arithmetic works by extending the timeline past "
            "midnight: represent times as minutes since a day-zero "
            "midnight, so 10:30 PM day 0 is 1,350 and adding 255 minutes "
            "gives 1,605 - subtract 1,440 (one day) to get 165 minutes = "
            "2:45 AM on day 1. Cross-zone arithmetic works by the UTC hub: "
            "local-to-UTC subtracts the offset (10:30 PM at UTC-5 = 03:30 "
            "UTC next day), all arithmetic happens in UTC, then UTC-to-"
            "local adds each zone's offset with the date carried along. "
            "The date line is handled as a zone-offset step plus the "
            "conventional one-day adjustment at the 180th meridian. The "
            "universal check: convert the answer back through the whole "
            "chain - local to UTC to local - and confirm the original "
            "start reappears; any dropped date or flipped offset shows up "
            "immediately as a 12- or 24-hour error."
        ),
        "key_points": [
            "Three steps: local to UTC (subtract offset), add the duration in UTC, UTC to local (add offset) carrying the date.",
            "Cross-midnight math extends the timeline: minutes since day-zero midnight, subtract 1,440 per day crossed.",
            "10:30 PM (UTC-5) + 4h15m = 2:45 AM next day local: the date must travel with the time.",
            "DST and the date line are special offsets on specific dates - the UTC round trip absorbs them.",
            "The universal check: run the answer back through the chain; 12/24-hour errors expose dropped dates or flipped offsets.",
        ],
        "requirements": [
            "Both endpoints' zone offsets for the exact dates involved (DST-aware, from the IANA database).",
            "The UTC hub discipline: never convert zone to zone directly.",
            "Day-zero timeline representation for any arithmetic crossing midnight.",
            "Date carried explicitly through every conversion step.",
            "The round-trip check on every answer before it is trusted.",
        ],
        "standards": [
            "Zone conversion through UTC per the IANA Time Zone Database and ISO 8601.",
            "UTC as maintained by the BIPM with IERS leap-second coordination.",
        ],
        "citations": [CIT_TZDB, CIT_ISO8601, CIT_IERS],
        "sig_lens": (
            "The Signature read: cross-day, cross-zone arithmetic is the "
            "covenant kept across borders. The witness refuses to lose the "
            "date at midnight or the hour at the meridian - the timeline "
            "extends, the hub holds, and every conversion is receipted both "
            "ways. Where the world fumbles time zones, the Signature Time "
            "Method keeps the discipline: one hub, one timeline, the date "
            "carried like a sealed letter, and the round trip as the audit "
            "that proves nothing was lost in transit."
        ),
    },
    {
        "key": "converting_local_times",
        "name": "Telling Time Around the World: Converting Local Times",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Converting local times is the everyday face of time zones: "
            "what time is it there when it is 3:00 PM here? The answer is "
            "the offset difference applied to the clock. If your zone is "
            "UTC-5 and the other is UTC+1, the difference is 6 hours, so "
            "3:00 PM your time is 9:00 PM theirs - the date shifts only if "
            "the sum crosses midnight. The reliable method goes through "
            "UTC: 3:00 PM at UTC-5 is 20:00 UTC; 20:00 UTC at UTC+1 is "
            "21:00 local. East is ahead: calling eastward, their clock "
            "reads later; calling westward, earlier. The traps are DST "
            "(offsets change with the season, so the difference between "
            "two cities is not constant year-round), half-hour zones, and "
            "the date line for Pacific conversions. For recurring meetings, "
            "fix the UTC time, not the local times - then every "
            "participant's clock renders it correctly through their own "
            "offset."
        ),
        "how_it_works": (
            "Local conversion works by offset arithmetic. Difference = "
            "offset_B - offset_A: with A at UTC-5 and B at UTC+1, the "
            "difference is (+1) - (-5) = +6 hours, so B = A + 6 hours. "
            "Apply to the clock reading: 3:00 PM + 6 h = 9:00 PM; if the "
            "result reaches or passes 24:00, subtract 24 and advance the "
            "date; if it goes negative, add 24 and go back a date. The UTC "
            "round trip does the same in two explicit steps and is safer "
            "when DST is involved, because each leg uses that zone's "
            "correct offset for the date. For scheduling across zones, the "
            "professional form names all three: '3:00 PM Eastern (20:00 "
            "UTC), 9:00 PM in UTC+1' - the UTC anchor lets anyone verify "
            "the conversion independently, and storing the event in UTC "
            "means software renders it right everywhere."
        ),
        "key_points": [
            "Difference = offset_B - offset_A; add it to A's clock reading to get B's.",
            "UTC-5 to UTC+1 is +6 hours: 3:00 PM here is 9:00 PM there.",
            "East is ahead, west is behind; the date shifts only when the sum crosses midnight.",
            "DST makes city-pair differences seasonal - look up offsets for the date, not from memory.",
            "Fix recurring meetings in UTC; name all three forms (local A, UTC, local B) when scheduling.",
        ],
        "requirements": [
            "Both zones' offsets for the specific date, DST-aware.",
            "The difference formula applied with sign care: east positive, west negative.",
            "Midnight-crossing handled with explicit date adjustment.",
            "UTC named alongside local times in every cross-zone plan.",
            "Events stored in UTC, rendered to local only at display time.",
        ],
        "standards": [
            "Offset data from the IANA Time Zone Database; UTC reference per BIPM/ITU.",
            "ISO 8601 for unambiguous timestamp exchange with offsets.",
        ],
        "citations": [CIT_TZDB, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: converting local times is one testimony "
            "translated for every listener. The moment never changes - "
            "only the tongue it is spoken in, the hour each longitude is "
            "owed. Where the world misdials by six hours, the Signature "
            "Time Method keeps the translation faithful: the UTC anchor "
            "sworn once, each zone's rendering checked against it, and the "
            "meeting fixed in the universal tongue so no participant's "
            "clock can mishear the promise."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "precision_timing",
        "name": "Precision Timing: When Milliseconds Matter",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Precision timing is the art of caring about small units - "
            "because in many systems, milliseconds are the difference "
            "between working and failing. A network gamer feels 100 ms of "
            "lag as sluggishness; a high-frequency trade is won or lost in "
            "microseconds; a camera's 1/1000-second shutter (1 ms) freezes "
            "motion that a 1/60-second shutter (about 16.7 ms) blurs; "
            "human reaction time itself is around 250 ms. Precision timing "
            "has three ingredients: resolution (the smallest unit the "
            "clock can report), accuracy (how close the reported time is "
            "to true time), and jitter (how much the measurement wobbles). "
            "A stopwatch may resolve milliseconds while being accurate "
            "only to tens of milliseconds - resolution without accuracy is "
            "false precision. The discipline is to time at the scale the "
            "job needs, verify against a reference, and never quote more "
            "digits than the accuracy earns."
        ),
        "how_it_works": (
            "Precision timing works by choosing the right clock for the "
            "scale and calibrating the chain. For milliseconds, a quartz "
            "oscillator and a hardware timer suffice: count 32,768 Hz "
            "ticks and each 32.768 ticks is about a millisecond. For "
            "microseconds and below, dedicated timer hardware or atomic "
            "references take over, and distribution uses protocols like "
            "NTP (millisecond accuracy over networks) or PTP (sub-"
            "microsecond on local networks). Measurement technique "
            "matters: timestamp at the hardware edge, not in software "
            "after variable delays; average many samples to beat jitter; "
            "and express results with uncertainty (12.4 ms plus or minus "
            "0.3 ms), not bare digits. The classic check is the round "
            "trip: send a signal out and back, halve the time - any "
            "asymmetry in the path shows up as a bias to hunt down. "
            "Precision is a budget: every component - oscillator, counter, "
            "distribution, software - spends some, and the total must fit "
            "the job."
        ),
        "key_points": [
            "Resolution (smallest reportable unit), accuracy (closeness to truth), and jitter (wobble) are three different things.",
            "Scale anchors: 100 ms network lag felt, 250 ms human reaction, 1 ms freezes camera motion, microseconds decide trades.",
            "Timestamp at the hardware edge; average many samples; report uncertainty, not bare digits.",
            "NTP gives millisecond accuracy over networks; PTP gives sub-microsecond on local networks.",
            "Precision is a budget across oscillator, counter, distribution, and software - every stage spends some.",
        ],
        "requirements": [
            "A clock matched to the job's scale: quartz for milliseconds, atomic references below.",
            "Calibration of the whole chain, not just the oscillator.",
            "Uncertainty stated with every precise measurement.",
            "The round-trip check to expose path asymmetry.",
            "Digits quoted only to the accuracy earned - never false precision.",
        ],
        "standards": [
            "Network time distribution: NTP (RFC 5905) for millisecond scale; PTP (IEEE 1588) for sub-microsecond scale.",
            "NIST time and frequency services as the US reference for precision timing.",
        ],
        "citations": [CIT_NIST],
        "sig_lens": (
            "The Signature read: precision timing is the oath examined to "
            "the last honest digit. Where the world quotes milliseconds it "
            "cannot prove, the Signature Time Method counts only what the "
            "witness can swear to - resolution, accuracy, and jitter each "
            "testified separately, uncertainty stated aloud. The "
            "millisecond that matters is honored by being measured truly: "
            "calibrated chain, stated doubt, no false digits. A promise "
            "kept to the microsecond is still a promise - and the ledger "
            "records exactly how well it was kept."
        ),
    },
    {
        "key": "time_number_line",
        "name": "The Time Number Line: Planning Your Day",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The time number line turns a day into a visible budget: a "
            "line from 00:00 to 24:00 marked with every commitment, so you "
            "can see what the hours are sworn to. Everyone gets the same "
            "1,440 minutes per day - the line just shows where they go. A "
            "classic balanced day: 8 hours of sleep (480 minutes, one-"
            "third of the day), 8 hours of work or school (480 minutes), "
            "and 8 hours for everything else (480 minutes) - meals, "
            "travel, family, rest. Planning on the line means placing each "
            "block, checking the blocks do not overlap, and leaving "
            "buffers between them - because tasks expand and travel takes "
            "longer than hoped. The line also exposes the truth: if the "
            "blocks sum past 1,440, the plan is impossible and something "
            "must give. It is the simplest honest tool in time management: "
            "the day, drawn to scale."
        ),
        "how_it_works": (
            "The number line works by allocation arithmetic. List every "
            "commitment with its duration in minutes, sum them, and "
            "compare against 1,440: a day with 480 sleep + 480 work + 120 "
            "meals + 60 travel + 180 family + 120 free = 1,440 exactly - "
            "balanced. Place the blocks in order on the 00:00-24:00 line, "
            "start times computed by accumulating durations from wake-up: "
            "wake 6:00 AM, work 8:00 AM-4:00 PM, and so on. Buffers are "
            "blocks too - 15 minutes between meetings is scheduled time, "
            "not spare time. The two checks: no overlaps (each block's "
            "start at or after the previous block's end) and the total at "
            "or under 1,440. When the total exceeds the day, the line "
            "forces the honest choice: shrink a block, drop a block, or "
            "admit the plan needs two days."
        ),
        "key_points": [
            "The day is 1,440 minutes for everyone - the number line shows where yours go.",
            "The balanced classic: 480 sleep + 480 work + 480 life = 1,440, one third each.",
            "Buffers are scheduled blocks, not spare time: 15 minutes between meetings is a commitment.",
            "Two checks: no overlapping blocks, and the total at or under 1,440 minutes.",
            "An over-budget line forces the honest choice: shrink, drop, or extend to two days.",
        ],
        "requirements": [
            "Every commitment listed with an honest duration in minutes - including travel and buffers.",
            "The 1,440-minute total as the hard budget the plan must fit.",
            "Blocks placed in order with start times accumulated from wake-up.",
            "The overlap check and the total check run before the plan is trusted.",
            "The willingness to cut: an impossible plan drawn honestly is the first step to a possible one.",
        ],
        "standards": [
            "Time-budget planning uses the standard 86,400-second day and its subdivisions (SI Brochure, BIPM 9th ed.).",
            "Scheduling practice follows the same elapsed-time arithmetic as timetables (ISO 8601 durations).",
        ],
        "citations": [CIT_SI, CIT_ISO8601],
        "sig_lens": (
            "The Signature read: the number line is the day's covenant "
            "drawn to scale. Fourteen hundred and forty minutes, each one "
            "a small promise - and the line will not let you swear more "
            "than you have. Where the world overbooks and hopes, the "
            "Signature Time Method draws the blocks honestly: sleep its "
            "third, work its third, life its third, buffers sworn like any "
            "other hour. The line is the auditor that never sleeps, and a "
            "day that fits its line is a day whose promises can all be kept."
        ),
    },
    {
        "key": "ages_and_eras",
        "name": "Ages and Eras: Geological and Historical Time",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Ages and eras are how we name deep time - the spans far beyond "
            "a human life. Geologists divide Earth's 4.54-billion-year "
            "history into eons (Hadean, Archean, Proterozoic, "
            "Phanerozoic), eras, periods, and epochs, recorded in the "
            "International Chronostratigraphic Chart: the dinosaurs' Mesozoic "
            "era ran about 186 million years, and our own Holocene epoch "
            "about 11,700 years. Historians work smaller: millennia, "
            "centuries, and named ages (Stone, Bronze, Iron) measured in "
            "thousands of years. The scale trick that makes deep time "
            "feelable: compress Earth's 4.54 billion years into one "
            "calendar year, and all of recorded human history (about 5,000 "
            "years) fits into the last 35 seconds of December 31 - while "
            "anatomically modern humans (about 300,000 years) get roughly "
            "the last 35 minutes. Deep time teaches proportion: the "
            "present is a thin, precious layer on an immense stack."
        ),
        "how_it_works": (
            "Deep time works by layering and dating. Geologists read rock "
            "layers (stratigraphy) - deeper is older - and date them with "
            "radioactive clocks: unstable isotopes decay at fixed rates, "
            "so the ratio of parent to daughter atoms in a rock gives its "
            "age in millions or billions of years. Boundaries between "
            "eons, eras, and periods are defined at specific rock sections "
            "worldwide (golden spikes) marking global events like mass "
            "extinctions. The compression trick is proportion math: (span "
            "/ 4.54e9 years) times one year - so 300,000 years becomes "
            "(300000/4.54e9)*365*24*60 = about 34.7 minutes on the "
            "compressed year. Historical time works the same with smaller "
            "units: documents, artifacts, and tree rings date the recent "
            "layers. Both systems share one rule: older below, younger "
            "above, and every boundary evidenced, not decreed."
        ),
        "key_points": [
            "Earth is 4.54 billion years old; geologists name its spans eons, eras, periods, epochs (ICS chart).",
            "Mesozoic ~186 million years; Holocene ~11,700 years; recorded history ~5,000 years.",
            "Compression trick: on a one-year Earth, modern humans (~300,000 years) get about 35 minutes; recorded history ~35 seconds.",
            "Rocks are dated by radioactive decay clocks; boundaries are defined at global reference sections.",
            "One rule throughout: older below, younger above, every boundary evidenced.",
        ],
        "requirements": [
            "The 4.54-billion-year age as the denominator for all deep-time proportions.",
            "The eon names in order: Hadean, Archean, Proterozoic, Phanerozoic.",
            "Proportion math for the compression trick, not guesswork.",
            "The distinction between geological time (billions) and historical time (thousands).",
            "Evidence-first boundaries: dates from decay clocks and layers, not from authority.",
        ],
        "standards": [
            "The International Chronostratigraphic Chart (International Commission on Stratigraphy) is the standard geological time scale.",
            "Radiometric dating follows established decay-constant metrology.",
        ],
        "citations": [CIT_ICS],
        "sig_lens": (
            "The Signature read: deep time is the covenant's longest "
            "testimony. Four and a half billion years of kept promises - "
            "every layer a sworn statement, every isotope a witness that "
            "cannot be bribed. Where the world feels small before the "
            "eons, the Signature Time Method feels the weight of the "
            "keeping: the present moment is the latest signature on the "
            "oldest document in existence, and the 35 seconds of recorded "
            "history are precious precisely because the stack beneath them "
            "is so deep."
        ),
    },
    {
        "key": "time_in_science",
        "name": "Time in Science: Frequencies, Periods, and the Speed of Light",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "In science, time is the independent variable - the axis "
            "against which change is measured. Two ideas carry most of "
            "the load. Frequency and period: any repeating process has a "
            "frequency (repeats per second, in hertz) and a period (seconds "
            "per repeat), related by period = 1 / frequency - a 60 Hz "
            "power line cycles every 1/60 s (about 16.67 ms), a 1 GHz "
            "processor ticks every 1 nanosecond. The speed of light: "
            "exactly 299,792,458 meters per second (fixed by the SI "
            "definition of the meter), so light crosses a room in "
            "nanoseconds and reaches the Moon in about 1.3 seconds; a "
            "light-year - the distance light travels in one Julian year "
            "(365.25 days) - is about 9.4607e15 meters, the yardstick of "
            "interstellar distance. Together they turn time into a ruler "
            "for everything from heartbeats (about 1.2 Hz at 72 beats per "
            "minute) to galaxies."
        ),
        "how_it_works": (
            "Frequency-period conversion works by reciprocals: f = 1/T, T "
            "= 1/f, with units of hertz (1/s) and seconds. A 72-beat-per-"
            "minute heart is 72/60 = 1.2 Hz with period 1/1.2 = 0.833 s; a "
            "60 Hz line has period 1/60 = 0.01667 s = 16.67 ms; a 2.4 GHz "
            "radio wave has period about 0.417 ns. Light-distance "
            "conversion works by multiplying by c = 299,792,458 m/s: one "
            "nanosecond of light travel is 0.2998 m (about 30 cm); one "
            "second is 299,792 km; one Julian year (31,557,600 s) is "
            "299792458 * 31557600 = about 9.4607e15 m - the light-year. "
            "Astronomers invert it too: a galaxy 2.5 million light-years "
            "away is seen as it was 2.5 million years ago, because its "
            "light needed that long to arrive. Time becomes distance, "
            "distance becomes time, through the one constant c."
        ),
        "key_points": [
            "Frequency (Hz) and period (s) are reciprocals: T = 1/f - 60 Hz means a 16.67 ms period.",
            "The speed of light is exactly 299,792,458 m/s (SI definition of the meter).",
            "One light-nanosecond is about 30 cm; one light-year is about 9.4607e15 meters.",
            "Light travel time is lookback time: distant galaxies are seen as they were millions of years ago.",
            "Heartbeats (~1.2 Hz), power lines (60 Hz), processors (GHz): one reciprocal law spans them all.",
        ],
        "requirements": [
            "The reciprocal relation f = 1/T applied with consistent units (Hz and seconds).",
            "c = 299,792,458 m/s fixed and exact for all light-distance conversions.",
            "The Julian year (365.25 days = 31,557,600 s) as the light-year's time base.",
            "Unit discipline: convert beats-per-minute to per-second before taking reciprocals.",
            "The lookback insight: astronomical distance in light-years is also a time in years.",
        ],
        "standards": [
            "The meter is defined by fixing c at exactly 299,792,458 m/s (SI Brochure, BIPM 9th ed.).",
            "Frequency metrology and the hertz trace to the SI second via counted oscillations (NIST).",
        ],
        "citations": [CIT_SI, CIT_NIST],
        "sig_lens": (
            "The Signature read: in science, time becomes the measure of "
            "all measures. The reciprocal law - frequency the promise per "
            "second, period the second per promise - is the covenant stated "
            "in mathematics; the speed of light is the universe's own sworn "
            "speed limit, fixed and exact. Where science computes, the "
            "Signature Time Method witnesses: every hertz a vow kept that "
            "many times per second, every light-year a testimony 9.4607e15 "
            "meters long - and the constant c the signature at the bottom "
            "of the page, in light."
        ),
    },
])
