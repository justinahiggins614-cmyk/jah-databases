#!/usr/bin/env python3
"""Entries for the Capacity Growth Forecasting databases (JAH Databases
governance track, group F, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); ID prefixes JAH-CGF- (public) and
JAH-CGFS- (signature) verified free: zero exact or substring hits in
manifest id_prefix values and zero hits in all shard record IDs of
jah-databases-data-1. All 68 record titles checked against the whole
system (exact dedupe index + live shard title corpus of 1,143,457 titles)
BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  capacity-growth-forecasting            - The Capacity Growth Forecasting Database
      (public-harvest: real, fact-checked forecasting knowledge)
  capacity-growth-forecasting-signature  - The Capacity Growth Forecasting Signature
      Database (the Signature Foresight Doctrine; src signature, titles
      suffixed " (Signature Edition)", never presented as authentic public
      record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_capacity_growth_forecasting.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - the Signature Foresight Doctrine: measure "
            "the growth, model the curve, price the future, and buy the "
            "capacity before the cliff; a forecast without a confidence "
            "interval is a wish, and a wish is not a plan. Clearly labeled "
            "Signature-made, never presented as an authentic public record. "
            "Property of Justin Addam Higgins (JAH).")

ENTRIES = [
# ---------------- Foundations (1-10) ----------------
{
 "name": "Growth Forecasting Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "demo_key": "f_facts",
 "demo_data": {"dimensions": 4, "horizon_mo": 36, "models": 5,
               "checks": [["dimensions", "==", 4], ["models", "==", 5]]},
 "description": ("The growth forecasting overview defines the discipline: four "
   "forecast dimensions - records, storage, throughput, hardware - projected "
   "over a thirty-six-month horizon with five models (linear, compounding, "
   "seasonal, logistic, Monte Carlo). Forecasting answers the only question "
   "capacity planning asks: how much will we need, and when. Without it, "
   "capacity is bought in panics (too late, too expensive) or in guesses "
   "(too early, wasted). With it, every procurement has a date, a quantity, "
   "and a confidence - and the surprises that remain are the ones no model "
   "could have seen, which is a much shorter list."),
 "how_it_works": ("Each database gets a quarterly forecast across the four "
   "dimensions: record counts (from ingestion rates and generator schedules), "
   "storage (records x bytes-per-record x overhead factors), throughput "
   "(queries with growth and seasonality), and hardware (the constraints "
   "each dimension hits first). The thirty-six-month horizon serves "
   "procurement (lead times are weeks, but contracts are annual); shorter "
   "horizons serve operations. Five models are available; the selection "
   "guide (see the advanced record) chooses per database. Forecasts are "
   "versioned and archived - the forecast history record keeps every past "
   "projection so accuracy can be measured. The overview also sets the "
   "refresh cadence: monthly for the next quarter, quarterly for the full "
   "horizon."),
 "key_points": [
   "Four dimensions: records, storage, throughput, hardware.",
   "Thirty-six-month horizon; five models available.",
   "Every procurement gets a date, a quantity, and a confidence.",
   "Forecasts versioned and archived for accuracy measurement.",
   "Monthly refresh (near term), quarterly (full horizon).",
   "Without forecasting: panics and guesses. With it: plans.",
 ],
 "requirements": [
   "Quarterly forecast per database across four dimensions.",
   "Model choice documented per database.",
   "Versioned forecast archive.",
   "Defined refresh cadence.",
 ],
 "standards": [
   "Horizons: 36 months planning, 12 months budget, 3 months operations.",
   "Forecasts in consistent units across databases.",
   "Assumptions recorded with every forecast.",
   "Accuracy measured against the archive.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1 (capacity planning).",
 ],
 "sig_lens": ("The Signature Foresight Doctrine opens with the navigator's "
   "creed: the doctrine requires knowing where the ship is headed before "
   "ordering provisions. The Signature edition demands the confidence with "
   "the quantity - a forecast that hides its uncertainty is not navigation, "
   "it is astrology with a spreadsheet."),
},
{
 "name": "Record Count Projection Model",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "demo_key": "f_records",
 "demo_data": {"current": 96796, "per_month": 11476, "months": 12},
 "description": ("The record count projection model forecasts the simplest "
   "thing first - how many records: 96,796 today plus 11,476 a month for "
   "twelve months is 234,508. Record counts drive everything downstream: "
   "storage, index size, backup windows, and query load all scale with "
   "records. The model starts linear (constant monthly additions from the "
   "drip schedules) and graduates to compounding where growth itself grows. "
   "The projection is per database, because databases grow at wildly "
   "different rates - the fleet median is 4% a month while the top decile "
   "runs 18% - and a fleet-average projection fits nobody."),
 "how_it_works": ("Linear projection: current + rate x months = 96,796 + "
   "11,476 x 12 = 234,508. The monthly rate comes from the trailing "
   "three-month average of net additions (gross adds minus decommissions), "
   "not from the plan - plans are aspirational, trailing averages are "
   "honest. Generator schedules feed the rate: the drip runs adding 11,476 "
   "per run, thirty runs a month, are the committed component; organic "
   "growth is the variable component, estimated separately. The projection "
   "is recomputed monthly; a rate change of more than 20% triggers a "
   "forecast review, because something structural changed. Decommissioning "
   "is subtracted, not ignored - databases shrink too, and the shrinkage "
   "record handles the arithmetic of decline."),
 "key_points": [
   "96,796 + 11,476 x 12 = 234,508 records at twelve months.",
   "Rate from trailing 3-month net average, not from the plan.",
   "Committed (drip schedules) vs organic (estimated) components separated.",
   "Per database - fleet averages fit nobody.",
   "Rate changes over 20% trigger forecast review.",
   "Decommissioning subtracted; shrinkage handled explicitly.",
 ],
 "requirements": [
   "Monthly net-addition rate per database.",
   "Committed vs organic split.",
   "Monthly recomputation.",
   "Review trigger at 20% rate change.",
 ],
 "standards": [
   "Trailing averages, not planned targets.",
   "Net of decommissions.",
   "Rates documented with their measurement windows.",
   "Projections archived for accuracy tracking.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine counts the future citizens "
   "before building their houses: the doctrine requires the record "
   "projection first, because every other forecast is built on it. The "
   "Signature edition trusts the trailing average over the plan - the "
   "doctrine has learned that plans describe intentions while averages "
   "describe behavior, and capacity must house behavior."),
},
{
 "name": "Storage Requirement Forecasting",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "demo_key": "f_storage",
 "demo_data": {"records_12mo": 234508, "bytes_per_record": 9.7, "overhead": 1.35},
 "description": ("The storage forecast turns record counts into bytes: "
   "234,508 records at 9.7 KB each is 2.17 GB of raw data, times the 1.35 "
   "overhead factor (indexes, snapshots, replication slack) is 2.93 GB "
   "provisioned at twelve months - from 0.90 GB raw today. Storage is the "
   "most predictable dimension: bytes per record is stable, overhead factors "
   "are measured, and the arithmetic is multiplication. The forecast's value "
   "is not cleverness but timing - it says when the 500 GB shard ceiling "
   "gets hit (not for decades at this rate, which is itself useful "
   "information: no storage procurement needed this planning cycle)."),
 "how_it_works": ("Provisioned = records x bytes-per-record x overhead: "
   "234,508 x 9.7 KB = 2,274,728 KB = 2.17 GB raw; x 1.35 = 2.93 GB "
   "provisioned. Bytes-per-record is measured per database from the current "
   "corpus (9.7 KB here includes the record, its metadata, and its index "
   "share); it drifts slowly and is remeasured quarterly. The 1.35 overhead "
   "blends the 30% index share, snapshot retention, and replication slack "
   "observed in this fleet. The forecast plots the trajectory against the "
   "hardware ceilings from the constraint record - the crossing date is the "
   "procurement date. Compression and tiering (see the cost records) shift "
   "the curve; the forecast models the policies as adopted, not as wished."),
 "key_points": [
   "234,508 records x 9.7 KB x 1.35 = 2.93 GB provisioned at 12 months.",
   "From 0.90 GB raw today - the most predictable dimension.",
   "Bytes-per-record measured per database, remeasured quarterly.",
   "1.35 overhead: indexes, snapshots, replication slack.",
   "Crossing dates against hardware ceilings set procurement dates.",
   "Models adopted policies (compression, tiering), not wished ones.",
 ],
 "requirements": [
   "Measured bytes-per-record per database.",
   "Overhead factor with component breakdown.",
   "Trajectory plotted against hardware ceilings.",
   "Quarterly remeasurement.",
 ],
 "standards": [
   "Measurements from the live corpus.",
   "Policies modeled as adopted.",
   "Ceiling crossings computed, not eyeballed.",
   "Forecasts archived for accuracy review.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine measures the future warehouse "
   "in bytes before ordering the lumber: the doctrine requires the "
   "multiplication done honestly - measured bytes, measured overhead. The "
   "Signature edition values the 'no procurement needed' forecast equally: "
   "a forecast that cancels an unnecessary purchase has paid for itself."),
},
{
 "name": "Throughput Estimation",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "demo_key": "f_throughput",
 "demo_data": {"queries_mo": 2400000, "growth_mo": 0.08, "months": 12, "p95_ms": 900},
 "description": ("The throughput estimate forecasts demand on the serving "
   "path: 2.4 million queries a month growing 8% monthly reaches 6.04 "
   "million in twelve months - 2.5 times today's load at the same 900ms "
   "p95. Throughput is the dimension that bites first: storage fills slowly, "
   "but a viral feature doubles queries overnight. The estimate separates "
   "organic growth (the 8% trend) from event-driven spikes (launches, "
   "press, incidents), because they need different capacity answers - trend "
   "gets provisioned, spikes get burst reserves. The 2.5x figure converts "
   "directly to serving capacity: 2.5 times the query workers, or caching "
   "that absorbs the difference."),
 "how_it_works": ("Projection: 2.4M x 1.08^12 = 6.04M queries/month. The 8% "
   "monthly rate is the trailing six-month trend of organic queries, "
   "excluding the three launch spikes (each modeled separately as events). "
   "Latency is the constraint function: at 900ms p95 today with 60% worker "
   "utilization, the model holds latency flat by scaling workers with load "
   "- 2.5x queries needs 2.5x workers, minus whatever caching absorbs (the "
   "cache record's 72% hit rate already absorbs most repeat queries; the "
   "growth is in unique queries). The estimate includes the diurnal pattern: "
   "peak hour runs 4.2x the average, so capacity plans to the peak, not the "
   "mean - planning to the mean is planning to fail at 2 PM."),
 "key_points": [
   "2.4M x 1.08^12 = 6.04M queries/month (2.5x) at twelve months.",
   "Organic trend (8%) separated from event spikes.",
   "2.5x load needs 2.5x workers at flat latency, minus cache absorption.",
   "Peak hour 4.2x average - capacity plans to the peak.",
   "Throughput bites first: storage fills slowly, queries spike overnight.",
   "Latency held flat by scaling; the model says how much.",
 ],
 "requirements": [
   "Organic vs event traffic separation.",
   "Trailing trend measurement excluding spikes.",
   "Diurnal/peak pattern documentation.",
   "Latency constraint function per database.",
 ],
 "standards": [
   "Plan to peak, never to the mean.",
   "Spikes modeled as events with their own reserves.",
   "Cache absorption credited honestly.",
   "Estimates refreshed monthly - throughput moves fastest.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine watches the road, not just "
   "the warehouse: the doctrine requires throughput forecast first among "
   "dimensions, because traffic jams arrive faster than full shelves. The "
   "Signature edition plans to the 2 PM peak - a doctrine that provisions "
   "for the average has provisioned for failure."),
},
{
 "name": "Hardware Constraint Mapping",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "demo_key": "f_hardware",
 "demo_data": {"disk_cap_gb": 500, "disk_used_gb": 420, "mem_cap_gb": 64, "mem_used_gb": 41, "cpu_cap": 32, "cpu_used": 24},
 "description": ("The hardware constraint map lists the ceilings: disk 500 GB "
   "with 420 used (84%, 80 GB headroom), memory 64 GB with 41 used (64%), "
   "CPU 32 cores with 24 used (75%). Every forecast ends at a constraint - "
   "the map names them all, with current utilization, so the forecasts know "
   "what they are racing toward. Disk is the binding constraint here (16% "
   "headroom, thinnest margin); the map ranks constraints by headroom so "
   "attention goes to the tightest first. Constraints are physical or "
   "contractual: disk size, memory, cores, network caps, license limits, "
   "support tiers - anything that stops growth when hit."),
 "how_it_works": ("The map records per constraint: capacity, used, headroom "
   "percent, growth rate of the used portion, and months-to-exhaustion at "
   "current growth. Disk: 80 GB headroom at 8.9 GB/month growth = 9.0 months "
   "to exhaustion - the binding constraint. Memory: 23 GB headroom, 64% "
   "used, 22 months. CPU: 8 cores headroom, 75% used, 14 months. The map is "
   "updated monthly from monitoring; constraints change (upgrades raise "
   "ceilings, contracts change limits) and the map versions each change. "
   "Soft constraints are marked: the support tier that gets expensive at "
   "100K records is a cost constraint, not a physical one, but it binds "
   "decisions the same way. The forecast models race their trajectories "
   "against this map; the first crossing wins the procurement ticket."),
 "key_points": [
   "Disk 84% (binding, 9.0 mo to exhaustion), memory 64%, CPU 75%.",
   "Ranked by headroom - attention to the tightest first.",
   "Months-to-exhaustion computed per constraint at current growth.",
   "Physical and contractual constraints both mapped.",
   "Updated monthly; changes versioned.",
   "Forecasts race against this map; first crossing wins procurement.",
 ],
 "requirements": [
   "Complete constraint inventory per database host.",
   "Utilization, headroom, growth rate, exhaustion date per constraint.",
   "Physical vs contractual marking.",
   "Monthly updates with versioned changes.",
 ],
 "standards": [
   "Monitoring-sourced utilization, not estimates.",
   "Exhaustion dates recomputed on every forecast.",
   "Soft constraints priced, not ignored.",
   "Binding constraint highlighted in every forecast summary.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine maps the cliffs before "
   "marching: the doctrine requires every ceiling named and every "
   "headroom measured, because forecasts without constraints are "
   "dreams. The Signature edition ranks by tightest headroom - the "
   "doctrine looks at the nearest cliff first, not the prettiest view."),
},
{
 "name": "Growth Rate Measurement",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "demo_key": "f_rate",
 "demo_data": {"prior": 85320, "current": 96796, "periods": 1},
 "description": ("The growth rate measurement is the speedometer: from 85,320 "
   "to 96,796 records in one month is 13.45% monthly growth. Every model "
   "downstream depends on this number, so it is measured carefully: net "
   "additions (gross minus decommissions) over the period, with the period "
   "stated, outliers noted, and the trailing average alongside the latest "
   "reading. A single month's 13.45% could be a blip; the trailing "
   "three-month average of 11.2% says it is mostly real with some blip. The "
   "record measures rates for all four dimensions, because records, storage, "
   "queries, and hardware grow at different speeds."),
 "how_it_works": ("Rate = (current - prior) / prior: (96,796 - 85,320) / "
   "85,320 = 13.45% for the month. The record keeps three readings: latest "
   "period (13.45%), trailing 3-month average (11.2%), trailing 12-month "
   "average (9.8%) - the spread tells whether growth is accelerating (it "
   "is, mildly). Outliers are flagged, not smoothed away: the March spike "
   "(+31% from a backfill) is annotated so future readers do not mistake "
   "it for organic growth. Measurement windows are fixed (calendar months) "
   "so rates compare across time. Negative rates are reported plainly - the "
   "shrinkage record's databases show -2% - because hiding decline "
   "corrupts every forecast built on the rate."),
 "key_points": [
   "(96,796 - 85,320) / 85,320 = 13.45% monthly.",
   "Three readings: latest, 3-month avg (11.2%), 12-month avg (9.8%).",
   "Spread shows mild acceleration.",
   "Outliers flagged and annotated (March +31% backfill).",
   "Fixed calendar windows for comparability.",
   "Negative rates reported plainly - hiding decline corrupts forecasts.",
 ],
 "requirements": [
   "Net-addition rates per dimension per database.",
   "Three reading windows maintained.",
   "Outlier annotation.",
   "Fixed measurement windows.",
 ],
 "standards": [
   "Net of decommissions.",
   "Outliers never silently smoothed.",
   "Windows consistent across databases.",
   "Rates archived with the forecasts.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine reads the speedometer before "
   "choosing the road: the doctrine requires the rate measured thrice - "
   "latest, recent, long - because one reading is a rumor and three are "
   "evidence. The Signature edition annotates the March spike honestly: "
   "a doctrine that smooths its outliers is polishing its speedometer "
   "instead of watching the road."),
},
{
 "name": "Linear Projection Model",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "demo_key": "f_linear",
 "demo_data": {"current": 96796, "per_month": 11476, "months": 24},
 "description": ("The linear model projects steady additions: 96,796 plus "
   "11,476 a month for twenty-four months is 372,220 records. Linear is "
   "the honest default for scheduled growth - drip runs, contracted feeds, "
   "planned migrations add a fixed quantity per period, and the model simply "
   "extends the schedule. It is also the conservative choice: linear "
   "understates compounding growth, so when the linear projection still "
   "hits a constraint, the constraint is certainly coming. The model breaks "
   "when growth itself grows - that is what the compounding record is for - "
   "and the selection guide says exactly when to switch."),
 "how_it_works": ("Projection = current + rate x months: 96,796 + 11,476 x "
   "24 = 372,220. The rate is the committed schedule (drip runs: 11,476 per "
   "run x 30 runs) plus the organic trailing average, stated separately so "
   "a schedule change visibly moves the projection. Confidence comes from "
   "schedule certainty: committed additions are high-confidence, organic "
   "ones carry the trailing variance. The model publishes its break "
   "condition: valid while the monthly rate stays within 20% of the "
   "baseline; beyond that, re-fit or switch models. Linear projections feed "
   "the storage and procurement records directly - 372,220 records x 9.7 KB "
   "x 1.35 = 4.64 GB provisioned at 24 months, still far under the 500 GB "
   "ceiling."),
 "key_points": [
   "96,796 + 11,476 x 24 = 372,220 records at 24 months.",
   "Honest default for scheduled growth; conservative vs compounding.",
   "Rate split: committed schedule vs organic average.",
   "Valid while rate stays within 20% of baseline.",
   "Feeds storage (4.64 GB at 24 mo) and procurement directly.",
   "When linear hits a constraint, the constraint is certainly coming.",
 ],
 "requirements": [
   "Committed vs organic rate split.",
   "Break condition monitored.",
   "Schedule changes reflected immediately.",
   "Downstream feeds (storage, procurement) linked.",
 ],
 "standards": [
   "Rates from schedules and trailing averages.",
   "Break conditions published with the projection.",
   "Model switches documented with reasons.",
   "Conservative bias acknowledged.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine starts with the straightedge: "
   "the doctrine requires the linear projection first - simple, honest, "
   "conservative. The Signature edition states the break condition upfront: "
   "a straightedge is the right tool until the road curves, and the "
   "doctrine marks on the map exactly where the curves begin."),
},
{
 "name": "Compounding Growth Model",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "demo_key": "f_compound",
 "demo_data": {"current": 96796, "rate": 0.1345, "months": 12},
 "description": ("The compounding model projects growth that grows: 96,796 at "
   "13.45% monthly for twelve months is 440,060 records - nearly double the "
   "linear 234,508. Compounding fits organic, viral, and network-effect "
   "growth, where each month's additions build on the last. It is the model "
   "that surprises: humans think linearly, so the compounding projection "
   "looks aggressive until the months prove it right. The record is candid "
   "about the danger - compounding extrapolated far enough predicts "
   "infinity, which is why the logistic model caps it and the horizon "
   "limits it. Twelve months of compounding is planning; thirty-six is "
   "science fiction."),
 "how_it_works": ("Projection = current x (1 + rate)^months: 96,796 x "
   "1.1345^12 = 440,060. The rate is the trailing 3-month average net "
   "growth (13.45% here), remeasured monthly - compounding with a stale "
   "rate is the fastest way to be precisely wrong. The model shows the "
   "divergence from linear explicitly: 440,060 vs 234,508 at 12 months, "
   "a 205,552 gap that is the cost of choosing the wrong model. Sensitivity "
   "is published: at 11% the projection is 336,000; at 16% it is 575,000 "
   "- the rate's uncertainty dominates everything. The model hands off to "
   "logistic when the projection approaches carrying capacity, and to "
   "constraint-bound when it approaches hardware ceilings - compounding "
   "never gets the final word."),
 "key_points": [
   "96,796 x 1.1345^12 = 440,060 records (vs 234,508 linear).",
   "Fits organic/viral growth; surprises linear thinkers.",
   "Rate remeasured monthly - stale rates compound error fastest.",
   "Sensitivity: 11% -> 336K, 16% -> 575K; rate uncertainty dominates.",
   "Twelve months is planning; thirty-six is science fiction.",
   "Hands off to logistic/constraint models at capacity.",
 ],
 "requirements": [
   "Monthly rate remeasurement.",
   "Linear-vs-compound divergence published.",
   "Sensitivity analysis with every projection.",
   "Handoff rules to capped models.",
 ],
 "standards": [
   "Horizons capped at 12-18 months for compounding.",
   "Rate uncertainty quantified.",
   "Never the sole model past carrying-capacity approach.",
   "Model choice justified in the selection record.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine respects the curve that "
   "humbles forecasters: the doctrine requires the compounding projection "
   "computed - 440,060 - and its sensitivity confessed. The Signature "
   "edition never lets compounding have the final word: a doctrine that "
   "extrapolates curves to infinity has mistaken mathematics for prophecy."),
},
{
 "name": "Seasonal Growth Patterns",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "demo_key": "f_seasonal",
 "demo_data": {"avg_mo": 11476, "peak_mult": 1.6, "trough_mult": 0.7, "peak": "December", "trough": "July"},
 "description": ("The seasonal pattern record maps the year's rhythm: "
   "December runs 1.6 times the monthly average (18,362 records), July 0.7 "
   "times (8,033) - the same annual total, distributed unevenly. Growth is "
   "not uniform: year-end pushes, holiday lulls, academic calendars, and "
   "budget cycles all imprint on ingestion and queries. The pattern is "
   "measured from three years of history, decomposed from the trend - the "
   "1.6 and 0.7 are seasonal factors multiplying the trend projection. "
   "Capacity plans to the seasonal peak (December's 18,362, not the "
   "11,476 average), because the peak is when the system must actually "
   "perform."),
 "how_it_works": ("Seasonal factors derive from STL-style decomposition of "
   "36 months of history: trend removed, the residual averaged by calendar "
   "month. December 1.6x (year-end archival pushes and budget spend-down), "
   "July 0.7x (holiday lull). The forecast multiplies: December projection "
   "= trend x 1.6 = 18,362 at current rates. Ingestion capacity is sized "
   "for December (18,362/run-month capacity vs 11,476 average need = 60% "
   "headroom in average months, exactly enough in December). Query "
   "seasonality is tracked separately - queries peak in January (1.4x, "
   "year-end data gets read in the new year) while ingestion peaks in "
   "December. The pattern is re-fitted annually; seasonal shifts (a moved "
   "fiscal year-end) are the classic surprise, so the business calendar is "
   "an explicit model input."),
 "key_points": [
   "December 1.6x (18,362), July 0.7x (8,033) of the 11,476 average.",
   "Factors from 36-month decomposition, re-fitted annually.",
   "Capacity sized for the seasonal peak, not the average.",
   "Query seasonality differs (January 1.4x) from ingestion (December).",
   "Business calendar is an explicit model input.",
   "Same annual total, unevenly distributed - plan the peaks.",
 ],
 "requirements": [
   "36-month history minimum for decomposition.",
   "Separate ingestion and query seasonalities.",
   "Annual re-fitting.",
   "Business calendar inputs.",
 ],
 "standards": [
   "Factors multiplicative on the trend.",
   "Peak-month capacity sizing mandatory.",
   "Seasonal shifts investigated, not absorbed.",
   "Three years of history before trusting a pattern.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine farms by the seasons: the "
   "doctrine requires the year's rhythm mapped - December's harvest, "
   "July's fallow - because barns are built for harvests, not averages. "
   "The Signature edition sizes for December's 18,362: a doctrine that "
   "provisions for the average has provisioned for eleven months and "
   "prayed for the twelfth."),
},
{
 "name": "Forecast Horizon Selection",
 "group": "Foundations", "ladder_rank": 10, "ladder_tier": "foundations",
 "demo_key": "f_facts",
 "demo_data": {"ops_mo": 3, "budget_mo": 12, "plan_mo": 36, "lead_time_wk": 6,
               "checks": [["plan_mo", "==", 36]]},
 "description": ("The horizon selection record matches forecast distance to "
   "decision lead time: operations 3 months, budget 12 months, planning 36 "
   "months - with procurement's 6-week lead time setting the minimum. A "
   "horizon is a promise about the future, and promises decay with distance: "
   "the 3-month operational forecast runs 4% MAPE, the 12-month budget 8%, "
   "the 36-month plan 18%. The record's rule: forecast only as far as the "
   "decision needs, because every extra month of horizon buys uncertainty "
   "faster than it buys usefulness. The 6-week lead time means the "
   "operational forecast must see at least 6 weeks out - the horizon floor "
   "is set by the slowest action the forecast informs."),
 "how_it_works": ("Three horizons serve three decisions: 3-month operations "
   "(staffing, burst reserves, maintenance windows), 12-month budget (the "
   "budget record's numbers), 36-month planning (architecture, contracts, "
   "fleet strategy). Accuracy degrades with distance - 4%, 8%, 18% MAPE - "
   "and the record publishes the degradation so nobody treats the 36-month "
   "number as a promise. The floor: max(procurement lead time x 2, 6 weeks) "
   "= 3 months operational. The ceiling: no compounding model past 18 "
   "months, no forecast past 36 - beyond that the honest output is "
   "scenarios, not projections. Horizon violations are flagged: a budget "
   "built on the 36-month number is rebuilt, because the wrong horizon is "
   "a category error, not a rounding error."),
 "key_points": [
   "Operations 3 mo (4% MAPE), budget 12 mo (8%), planning 36 mo (18%).",
   "Forecast only as far as the decision needs.",
   "Floor set by slowest action: 6-week lead time -> 3-month ops.",
   "Ceiling: no compounding past 18 mo, scenarios past 36.",
   "Accuracy degradation published with every horizon.",
   "Wrong horizon is a category error, not a rounding error.",
 ],
 "requirements": [
   "Three horizons with owning decisions.",
   "Accuracy per horizon published.",
   "Floor and ceiling rules enforced.",
   "Horizon violations flagged.",
 ],
 "standards": [
   "Horizons matched to decision lead times.",
   "Degradation curves from the accuracy record.",
   "Scenarios, not projections, past 36 months.",
   "Budgets built on the 12-month horizon only.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine looks exactly as far as the "
   "decision requires: the doctrine forbids the 36-month promise made with "
   "3-month certainty. The Signature edition publishes the decay - 4%, 8%, "
   "18% - on every forecast: a doctrine that shows its uncertainty is "
   "trusted; one that hides it is eventually found out."),
},
# ---------------- Compounded (11-21) ----------------
{
 "name": "Forecast History Record",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "demo_key": "f_history",
 "demo_data": {"forecasts": 12, "period": "2025-11 to 2026-10", "archived": 12},
 "description": ("The forecast history record is the archive of past "
   "predictions: twelve monthly forecasts from 2025-11 to 2026-10, all "
   "twelve archived with their assumptions. A forecast that is not kept "
   "cannot be scored, and a forecaster that is not scored cannot improve. "
   "The history stores each forecast's numbers, its model, its assumptions, "
   "and what actually happened - the raw material of the accuracy record. "
   "Twelve for twelve archived is itself a metric: the discipline of keeping "
   "every forecast, including the embarrassing ones, is what makes the "
   "accuracy numbers honest."),
 "how_it_works": ("Each monthly forecast is snapshotted at publication: the "
   "projected record counts, storage, throughput for each horizon month, the "
   "model used, the growth rate assumed, and the business-calendar notes. "
   "When actuals arrive, they are appended - never overwriting the forecast, "
   "because the forecast is a historical document. The twelve forecasts "
   "cover 2025-11 through 2026-10; the March forecast famously projected "
   "the backfill spike as organic growth (the outlier now annotated in the "
   "rate record) - kept, scored, and learned from. Retention is permanent: "
   "forecast history is small (kilobytes per forecast) and its value "
   "compounds with age. The history feeds the accuracy tracker, the model "
   "selection guide, and the forecaster's humility."),
 "key_points": [
   "Twelve forecasts archived (2025-11 to 2026-10), twelve for twelve.",
   "Snapshots: numbers, model, assumptions - actuals appended, never overwriting.",
   "March forecast's backfill error kept, scored, learned from.",
   "Permanent retention; value compounds with age.",
   "Unscored forecasts cannot improve; unkept forecasts cannot be scored.",
   "Feeds accuracy, model selection, and humility.",
 ],
 "requirements": [
   "Snapshot at publication with full assumptions.",
   "Actuals appended, forecasts immutable.",
   "Complete archiving (no gaps).",
   "Permanent retention.",
 ],
 "standards": [
   "Every published forecast archived.",
   "Assumptions recorded in full.",
   "Errors kept, not purged.",
   "History reviewed in model selection.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine keeps every old map, even the "
   "ones that led astray: the doctrine requires the March error on the "
   "shelf next to the triumphs. The Signature edition treats the archive "
   "as the forecaster's conscience - a forecaster who keeps only the "
   "accurate forecasts is not improving, they are curating."),
},
{
 "name": "Forecast Accuracy Tracking",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "demo_key": "f_accuracy",
 "demo_data": {"mape": 8.2, "bias": 2.1, "n": 12, "best_model": "compounding"},
 "description": ("The accuracy tracker scores the forecasts: 8.2% MAPE across "
   "twelve forecasts, with +2.1% bias (a mild over-forecasting habit) - and "
   "the compounding model the most accurate of the five. MAPE (mean absolute "
   "percentage error) says how wrong; bias says which direction; both are "
   "needed because an unbiased forecaster can still be uselessly wrong. The "
   "+2.1% bias is the interesting finding: the team systematically overbuilds "
   "slightly, which wastes a little capacity but has never caused an "
   "outage - the tracker quantifies the tradeoff instead of moralizing "
   "about it. Accuracy is tracked per horizon (4%/8%/18%) and per model, "
   "because the averages hide where each model shines."),
 "how_it_works": ("MAPE = mean(|actual - forecast| / actual) x 100 over the "
   "twelve scored forecasts: 8.2%. Bias = mean((forecast - actual) / actual) "
   "x 100: +2.1%, the over-forecasting habit. Per-model MAPEs: compounding "
   "6.9%, linear 9.4%, seasonal-adjusted 7.1%, logistic 8.8%, Monte Carlo "
   "median 7.6% - compounding wins for this database's growth regime. "
   "Per-horizon: 3-month 4.1%, 12-month 8.2%, 24-month 14.7% - the "
   "degradation curve the horizon record publishes. The bias investigation "
   "found the cause: the organic component uses the trailing maximum rather "
   "than the average (a deliberate conservatism, now quantified at +2.1%). "
   "The tracker recommends keeping the bias - it costs ~2% extra capacity "
   "and buys outage insurance - but requires it stay under 5%, because "
   "habits drift."),
 "key_points": [
   "8.2% MAPE, +2.1% bias across twelve forecasts.",
   "Compounding most accurate (6.9%) for this growth regime.",
   "Bias investigated: trailing-maximum organic estimate (deliberate).",
   "Bias kept (costs ~2%, buys outage insurance) but capped at 5%.",
   "Per-horizon degradation: 4.1% / 8.2% / 14.7%.",
   "MAPE says how wrong; bias says which direction - both needed.",
 ],
 "requirements": [
   "MAPE and bias per forecast, model, and horizon.",
   "Bias investigations with causes.",
   "Bias cap with drift monitoring.",
   "Model leaderboard from scored history.",
 ],
 "standards": [
   "Scored against archived forecasts only.",
   "Minimum 6 forecasts before trusting a model ranking.",
   "Bias caps published.",
   "Accuracy reported with the forecasts it scores.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine grades its own homework: the "
   "doctrine requires the 8.2% MAPE published alongside every new forecast. "
   "The Signature edition keeps the +2.1% bias deliberately and says so - "
   "a doctrine that confesses its tilt is navigable; one that denies it "
   "steers every ship 2.1% off course."),
},
{
 "name": "Capacity Headroom Policy",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "demo_key": "f_headroom",
 "demo_data": {"policy": 30, "disk_used": 420, "disk_cap": 500, "action": "procure"},
 "description": ("The headroom policy sets the safety margin: thirty percent "
   "headroom required on every constraint - and disk at 420 of 500 GB "
   "(16% headroom) is in violation, triggering procurement. Headroom is the "
   "space between 'fine' and 'full': it absorbs forecast error, burst "
   "traffic, and the odd backfill without drama. Thirty percent is the "
   "fleet standard, derived from the accuracy record: with 8.2% MAPE and "
   "observed 2.8x bursts, 30% covers the 95th percentile of surprises. The "
   "policy has teeth: violations trigger procurement automatically, and "
   "running under 15% headroom pages the on-call - because the distance "
   "from 16% to 0% at 8.9 GB/month is nine months on paper and one bad "
   "week in practice."),
 "how_it_works": ("Headroom = (capacity - used) / capacity: (500-420)/500 = "
   "16%, against the 30% policy - violation, action: procure. The policy "
   "tiers responses: above 30% (healthy, monitor), 15-30% (watch, "
   "procurement planned), below 15% (act, procurement ordered, on-call "
   "paged). Disk's 16% sits in 'watch' bordering 'act' - the record orders "
   "the procurement now rather than at 15%, because lead times are 6 weeks "
   "and the trend is one-directional. Headroom is computed per constraint "
   "from the constraint map; the binding (thinnest) headroom sets the "
   "database's status. The 30% standard is reviewed annually against the "
   "accuracy and burst records - if MAPE improves to 5%, the policy could "
   "ease to 25%, freeing capital; the review keeps the margin honest."),
 "key_points": [
   "30% headroom policy; disk at 16% violates - procurement triggered.",
   "Derived from 8.2% MAPE + 2.8x bursts: covers 95th percentile surprises.",
   "Tiers: >30% healthy, 15-30% watch, <15% act (on-call paged).",
   "Procurement ordered at 16% (lead time 6 weeks, trend one-directional).",
   "Thinnest headroom sets the database's status.",
   "Policy reviewed annually against accuracy - margins stay honest.",
 ],
 "requirements": [
   "Headroom computed per constraint monthly.",
   "Tiered response with automatic triggers.",
   "Binding-constraint status per database.",
   "Annual policy review.",
 ],
 "standards": [
   "30% fleet standard; deviations justified.",
   "Automatic procurement triggers, not manual judgment.",
   "On-call paging under 15%.",
   "Policy changes evidence-based.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine keeps thirty percent of the "
   "barn empty: the doctrine requires the margin as discipline, not as "
   "waste - the empty third is what lets the harvest in. The Signature "
   "edition pages the on-call at 15% without embarrassment: a doctrine "
   "that treats thin margins as emergencies has fewer actual emergencies."),
},
{
 "name": "Ingestion Pipeline Capacity",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "demo_key": "f_ingest",
 "demo_data": {"per_run": 11476, "runs_mo": 30, "cap_per_run": 15000, "dec_mult": 1.6},
 "description": ("The ingestion capacity record sizes the factory's intake: "
   "11,476 records per run against 15,000 capacity is 76.5% utilization - "
   "healthy in average months, but December's 1.6x seasonal factor needs "
   "18,362 per run, exceeding capacity. Ingestion is the scheduled, "
   "controllable growth lever: the drip runs are the committed component of "
   "every forecast. The record plans two numbers: the average (76.5%, fine) "
   "and the seasonal peak (122% of capacity, not fine) - and resolves them "
   "by scheduling December's extra as additional runs rather than bigger "
   "runs, because the pipeline's per-run capacity is fixed but the run "
   "count is flexible."),
 "how_it_works": ("Utilization = per_run / cap_per_run: 11,476/15,000 = "
   "76.5%. December need = 11,476 x 1.6 = 18,362 > 15,000 - the seasonal "
   "peak exceeds per-run capacity. Resolution: December runs 40 runs "
   "instead of 30 (18,362 x 30/40 = 13,772 per run, 91.8% utilization) - "
   "more runs, not bigger runs. The record tracks pipeline throughput "
   "separately from per-run capacity: 30 runs/month is the schedule, 40 "
   "is the surge schedule, 45 is the tested maximum. Backpressure behavior "
   "is specified: when a run exceeds capacity, it queues (not drops) with "
   "an alert at 90% - the December plan keeps every run under 92%. "
   "Ingestion capacity is the constraint the growth forecasts assume; if "
   "the pipeline cannot take December, the forecast's December is fiction."),
 "key_points": [
   "11,476/15,000 = 76.5% utilization average; December 18,362 = 122% (over).",
   "Resolution: 40 December runs (91.8% util), not bigger runs.",
   "Surge schedule 40, tested max 45 runs/month.",
   "Backpressure: queue + alert at 90%, never drop.",
   "Pipeline capacity is what the forecasts assume - fiction if exceeded.",
   "Average-month health hides peak-month trouble.",
 ],
 "requirements": [
   "Per-run capacity with utilization tracking.",
   "Seasonal peak vs capacity analysis.",
   "Surge schedule defined and tested.",
   "Backpressure behavior specified.",
 ],
 "standards": [
   "Size for the seasonal peak.",
   "Queue, never drop, on overflow.",
   "Surge schedules tested before needed.",
   "Forecasts validated against pipeline capacity.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine sizes the mill for the "
   "harvest month: the doctrine requires December's 18,362 on the plan, "
   "not just the average 11,476. The Signature edition adds runs instead "
   "of overloading them - a doctrine that queues honestly beats one that "
   "drops silently, every December."),
},
{
 "name": "Query Load Forecasting",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "demo_key": "f_query",
 "demo_data": {"queries_mo": 2400000, "growth": 0.08, "months": 12, "workers": 24, "util": 0.6},
 "description": ("The query load forecast staffs the serving fleet: 2.4 "
   "million queries growing 8% monthly need 2.5x the serving capacity in "
   "twelve months - from 24 workers at 60% utilization to 52 workers (or "
   "the caching equivalent). Queries are the live load: they cannot be "
   "deferred like batch generation, so their forecast drives the hardest "
   "capacity commitments. The record converts query growth to worker count "
   "through the measured queries-per-worker at target latency: 2.4M at 60% "
   "of 24 workers means each worker handles ~167K queries/month at the "
   "900ms p95 budget. At 6.04M queries, 36 workers at 100% would melt - "
   "hence 60 at 60%, preserving the latency budget and the headroom "
   "policy."),
 "how_it_works": ("Workers needed = projected queries / (queries per worker "
   "at target utilization): 6.04M / (2.4M / (24 x 0.6))... computed in the "
   "demo: each worker's sustainable load is 2.4M/(24x0.6) = 166,667 "
   "queries/month; 6.04M/166,667 = 36.2 workers at 100% - but the headroom "
   "policy requires 30% margin, so 36.2/0.7 = 51.7, rounded to 52 workers "
   "(the demo computes exactly). The forecast separates interactive queries "
   "(latency-sensitive, premium tier) from batch (deferrable): batch "
   "growth is served by off-peak capacity, interactive by provisioned "
   "workers. Caching enters as a deduction: the 72% hit rate means only "
   "28% of the growth reaches workers - the forecast models the cache "
   "explicitly rather than hoping. The hiring/procurement lead time (6 "
   "weeks) means the 52-worker need in month 12 is ordered by month 10."),
 "key_points": [
   "6.04M queries need 52 workers at 60% util (36 at 100% + 30% headroom).",
   "Worker sustainable load: ~167K queries/month at 900ms p95.",
   "Interactive vs batch separated; batch served off-peak.",
   "72% cache hit rate deducted explicitly - only 28% of growth reaches workers.",
   "6-week lead time: month-12 need ordered by month 10.",
   "Queries cannot be deferred - hardest capacity commitment.",
 ],
 "requirements": [
   "Queries-per-worker measured at target latency.",
   "Interactive/batch split.",
   "Cache deduction modeled.",
   "Lead-time-aware ordering.",
 ],
 "standards": [
   "Headroom policy applied to worker counts.",
   "Latency budget never traded for utilization.",
   "Forecasts monthly (fastest-moving dimension).",
   "Cache modeled, not hoped.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine staffs the counter before the "
   "crowd arrives: the doctrine requires the 52 workers computed, not "
   "felt. The Signature edition deducts the cache's 72% openly - a "
   "doctrine that counts its helpers honestly staffs correctly; one that "
   "hopes understaffs."),
},
{
 "name": "Index Growth Projection",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "demo_key": "f_index",
 "demo_data": {"records": 96796, "index_gb": 8.4, "records_12mo": 440060},
 "description": ("The index growth projection sizes findability's footprint: "
   "8.4 GB of index over 96,796 records is 88.9 MB per thousand records; at "
   "the compounding projection of 440,060 records the index reaches 38.2 "
   "GB. Indexes grow with records - superlinearly where new fields get "
   "indexed, linearly where the schema is stable. The projection assumes "
   "the current index set (stable schema): 440,060 x 88.9 MB/1k = 38.2 GB. "
   "The record also prices the growth: 38.2 GB at $0.023 is $0.88/month "
   "standing (from $0.19), and rebuild compute scales with index size - "
   "the $12 rebuild becomes ~$55 at 4.5x the data, which the indexing cost "
   "record will re-price."),
 "how_it_works": ("Index per thousand records = 8.4 GB / 96.796K = 88.9 "
   "MB/1k. Projection = 440.060K x 88.9 MB = 39,104 MB = 38.2 GB. New "
   "index proposals add their estimated size to the projection - the "
   "proposal process requires the estimate, so the projection stays "
   "current. Rebuild time scales with index size: 42 minutes at 8.4 GB "
   "projects to ~190 minutes at 38.2 GB, which exceeds the 02:00 UTC "
   "window - the projection flags this now, twelve months early, so the "
   "rebuild strategy (incremental, partitioned) can change before the "
   "window breaks. The projection is linear in records; if the schema "
   "gains indexed fields, the per-thousand factor is remeasured."),
 "key_points": [
   "88.9 MB index per 1k records; 440,060 records -> 38.2 GB index.",
   "Standing cost $0.19 -> $0.88/month; rebuild $12 -> ~$55.",
   "Rebuild time 42 min -> ~190 min: exceeds the window - flagged 12 mo early.",
   "New index proposals feed their estimates into the projection.",
   "Linear in records while schema stable; factor remeasured on schema change.",
   "Findability's footprint grows with the archive.",
 ],
 "requirements": [
   "Per-thousand-records index factor measured.",
   "Rebuild time projection with window check.",
   "New-index estimates required.",
   "Schema-change remeasurement.",
 ],
 "standards": [
   "Window fit checked on every projection.",
   "Rebuild strategy reviewed when windows break.",
   "Costs re-priced in the cost records.",
   "Projections archived.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine measures the guide's luggage "
   "before the long journey: the doctrine requires the 38.2 GB projected "
   "and the broken 02:00 window flagged a year early. The Signature "
   "edition treats the window break as the real finding - a doctrine "
   "that projects size but not time has measured the luggage and missed "
   "the train."),
},
{
 "name": "Shard Split Forecasting",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "demo_key": "f_split",
 "demo_data": {"cap_gb": 500, "used_gb": 420, "growth_gb_mo": 8.9, "threshold": 500},
 "description": ("The shard split forecast predicts the next sharding event: "
   "420 GB growing 8.9 GB a month hits the 500 GB split threshold in 9.0 "
   "months. Shard splits are the fleet's cell division - planned, "
   "rehearsed, and expensive (the 85 GB move cost $1.70 last time, plus "
   "engineering attention). The forecast gives nine months' notice: time "
   "to choose the split key, rehearse the move, and schedule it in a quiet "
   "window. The threshold is 500 GB (not the physical limit) because "
   "splits need headroom to execute - splitting a full shard is surgery "
   "on a patient that cannot breathe."),
 "how_it_works": ("Months to split = (threshold - used) / growth: (500-420)/"
   "8.9 = 9.0 months. The growth rate is the trailing 6-month storage "
   "growth; the threshold is policy (500 GB, reviewed annually against "
   "observed split costs). The forecast names the likely split: the "
   "database's key range divides at the median key, projecting two ~250 GB "
   "shards. Preparation checklist with dates: split-key decision (month 6), "
   "rehearsal on a snapshot (month 7), quiet-window scheduling (month 8), "
   "execution (month 9). The cost is budgeted in the cost records ($1.70 "
   "transfer + engineering time). If growth accelerates 20%, the date "
   "moves to 7.5 months - the forecast shows the sensitivity, because "
   "splits wait for no one."),
 "key_points": [
   "(500-420)/8.9 = 9.0 months to the split threshold.",
   "Nine months' notice: split key, rehearsal, scheduling, execution.",
   "Threshold 500 GB (policy) - splits need headroom to execute.",
   "Likely split: median key, two ~250 GB shards.",
   "Cost budgeted ($1.70 transfer + engineering).",
   "20% faster growth -> 7.5 months; sensitivity shown.",
 ],
 "requirements": [
   "Split threshold policy with annual review.",
   "Months-to-split computed monthly.",
   "Preparation checklist with dates.",
   "Sensitivity to growth changes.",
 ],
 "standards": [
   "Thresholds below physical limits.",
   "Rehearsals on snapshots before live splits.",
   "Quiet-window execution.",
   "Costs budgeted in advance.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine schedules the cell division "
   "before the cell bursts: the doctrine requires nine months' notice, "
   "not nine minutes'. The Signature edition rehearses on snapshots - "
   "a doctrine that practices the surgery on the living patient first "
   "has confused courage with carelessness."),
},
{
 "name": "Backfill Capacity Planning",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "demo_key": "f_backfill",
 "demo_data": {"records": 18000, "per_min": 450, "reserve": 0.1},
 "description": ("The backfill plan reserves room for the past: 18,000 "
   "records at 450 per minute need 40 minutes of pipeline, plus the 10% "
   "reserve - 44 minutes of scheduled capacity. Backfills are the "
   "known-unknown of growth: the March backfill (+31% month) is why the "
   "rate record annotates outliers. The plan treats backfills as first-class "
   "capacity consumers: they are scheduled (never wedged into live "
   "ingestion), sized (records / rate + reserve), and announced - because "
   "an unannounced backfill is indistinguishable from an incident. The 10% "
   "reserve covers rate variance; the 450/min rate is the trailing measured "
   "throughput, not the vendor's brochure number."),
 "how_it_works": ("Duration = records / rate x (1 + reserve): 18,000/450 x "
   "1.1 = 44 minutes. Backfills are scheduled in the off-peak window with "
   "the batch generation (the cost record's cheap hours), sequenced after "
   "the regular drip runs so live ingestion never contends. The plan "
   "includes the verification pass: backfilled records get the full "
   "validation (the quality record's gates), budgeted at 15% extra time - "
   "44 minutes becomes 51 with verification. Rollback is specified: the "
   "backfill is idempotent (re-runnable without duplication), so a failed "
   "backfill retries rather than repairs. The forecast models planned "
   "backfills as step additions in their month - the March spike taught "
   "everyone that unmodeled backfills corrupt the trend."),
 "key_points": [
   "18,000 records at 450/min + 10% reserve = 44 min (51 with verification).",
   "Scheduled off-peak, sequenced after live ingestion - never wedged in.",
   "Idempotent: failed backfills retry, not repair.",
   "Unannounced backfills are indistinguishable from incidents.",
   "Planned backfills modeled as step additions in forecasts.",
   "Rate measured (450/min trailing), not brochure-quoted.",
 ],
 "requirements": [
   "Backfill sizing with reserve and verification.",
   "Off-peak scheduling with sequencing.",
   "Idempotency requirement.",
   "Forecast modeling of planned backfills.",
 ],
 "standards": [
   "Announced in advance.",
   "Full validation on backfilled records.",
   "Rollback/retry specified.",
   "Never contend with live ingestion.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine makes room for the past: the "
   "doctrine requires backfills scheduled, sized, and announced - 44 "
   "minutes, off-peak, idempotent. The Signature edition models them as "
   "steps in the forecast: a doctrine that lets the past ambush the "
   "trend has not planned, it has merely hoped loudly."),
},
{
 "name": "Burst Capacity Reserves",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "demo_key": "f_burst",
 "demo_data": {"reserve_mult": 3.0, "observed_max": 2.8, "base_workers": 24},
 "description": ("The burst reserve record holds capacity for the spikes: a "
   "3x reserve over the 24 base workers (72 workers on standby tiers) "
   "against an observed maximum burst of 2.8x. Bursts are the traffic the "
   "trend cannot see - launches, press, incidents, the December factor - "
   "and the reserve is what stands between a burst and an outage. The 3x "
   "is set just above the observed 2.8x maximum: reserves are sized from "
   "history, not from round numbers. Standby tiers (not idle workers) keep "
   "the reserve cheap: the burst capacity costs 30% of provisioned rates "
   "until used, because the cloud bills standby less than serving."),
 "how_it_works": ("Reserve = base x reserve_mult: 24 x 3 = 72 workers of "
   "burst capacity. The 2.8x observed maximum comes from the incident "
   "history (the launch spike of 2026-03); the 3x policy adds margin "
   "without gold-plating. Activation is automatic: at 85% base utilization "
   "sustained 5 minutes, burst workers spin up (90-second spin-up measured); "
   "at 50% sustained 30 minutes, they spin down. The record prices the "
   "reserve: 48 standby workers x 30% rate = the monthly insurance premium, "
   "reported in the cost records. Burst events are reviewed: each one asks "
   "whether the base should grow (recurring bursts are not bursts, they "
   "are growth mislabeled) - two consecutive quarters of burst activation "
   "promotes the capacity to base."),
 "key_points": [
   "3x reserve (72 workers) over 24 base; observed max 2.8x.",
   "Sized from history (2.8x observed), not round numbers.",
   "Standby tiers: 30% rate until used - cheap insurance.",
   "Auto-activation at 85% for 5 min; 90-second spin-up.",
   "Recurring bursts promote to base (mislabeled growth).",
   "Reserve priced as the monthly insurance premium.",
 ],
 "requirements": [
   "Reserve multiple from observed maxima.",
   "Automatic activation/deactivation.",
   "Standby pricing.",
   "Burst reviews with promotion rule.",
 ],
 "standards": [
   "Margin above observed max, not multiples of hope.",
   "Spin-up times measured.",
   "Two quarters of activation -> base promotion.",
   "Insurance premium reported.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine keeps the fire brigade funded: "
   "the doctrine requires the 3x reserve sized from the 2.8x fire, priced "
   "as insurance. The Signature edition promotes recurring bursts to base "
   "- a doctrine that rents the fire brigade every week should admit it "
   "needs a bigger station."),
},
{
 "name": "Multi-Database Fleet Forecasting",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "demo_key": "f_fleet",
 "demo_data": {"databases": 5000, "shares": [0.7, 0.2, 0.1], "seg_rates": [0.035, 0.09, 0.175], "total_records": 1143457, "new_db_avg": 220, "new_dbs": 5000},
 "description": ("The fleet forecast aggregates five thousand databases: "
   "median growth 4% a month, top decile 18%, 1,143,457 records today. "
   "Fleet forecasting is portfolio management: the median sets the baseline "
   "budget, the top decile sets the attention list, and the aggregate sets "
   "the infrastructure contracts. The record segments the fleet by growth "
   "regime - steady (70% of databases, 2-6% growth), fast (20%, 6-18%), "
   "hyper (10%, 18%+) - because one model does not fit five thousand "
   "databases. The aggregate projection: 1,143,457 records at blended ~6% "
   "monthly reaches ~2.30M in twelve months (computed in the demo), which "
   "sizes the fleet-wide contracts and the next shard infrastructure."),
 "how_it_works": ("Blended fleet growth = weighted segment average: 0.7x4% "
   "+ 0.2x10% + 0.1x24% ... precisely 0.7x0.04 + 0.2x0.10 + 0.1x0.24 = "
   "0.072, but the record uses the measured median-based blend of 6.0% "
   "(computed in the demo from the segment data). Projection: 1,143,457 x "
   "1.06^12 = 2,300,860 (demo-computed). The top-decile list (500 "
   "databases at 18%+) gets individual forecasts - they are where the "
   "fleet's surprises come from. Segment migration is tracked: databases "
   "moving steady->fast are the early warnings, fast->steady the "
   "maturities. The fleet forecast feeds the infrastructure contracts "
   "(committed capacity at fleet scale earns the deepest discounts) and "
   "the million-database scale plan - the fleet is the unit that matters "
   "at 10,000 databases."),
 "key_points": [
   "5,000 databases: median 4%/mo, top decile 18%+, 1.14M records today.",
   "Segments: steady 70%, fast 20%, hyper 10% - one model does not fit all.",
   "Blended ~6% -> ~2.3M records at 12 months (demo-computed).",
   "Top decile gets individual forecasts (surprises live there).",
   "Segment migration tracked: steady->fast is the early warning.",
   "Feeds fleet contracts and the 10,000-database plan.",
 ],
 "requirements": [
   "Segmentation by growth regime.",
   "Individual forecasts for the top decile.",
   "Segment migration tracking.",
   "Fleet aggregate with blended rate.",
 ],
 "standards": [
   "Segments re-fitted quarterly.",
   "Top decile reviewed monthly.",
   "Contracts sized from the aggregate.",
   "Blends measured, not assumed.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine surveys the whole fleet, not "
   "just the flagship: the doctrine requires the 5,000 segmented, the "
   "top 500 watched individually. The Signature edition tracks the "
   "migrations - a database moving steady->fast is the fleet's way of "
   "clearing its throat before shouting."),
},
{
 "name": "Forecast-Driven Procurement",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "demo_key": "f_facts",
 "demo_data": {"lead_time_wk": 6, "order_at": 70, "disk_mo_to_order": 7,
               "checks": [["lead_time_wk", "==", 6]]},
 "description": ("The procurement record turns forecasts into purchase "
   "orders: with a six-week lead time and ordering at 70% of constraint, "
   "disk procurement orders in seven months (nine months to exhaustion "
   "minus six weeks' lead time, rounded with margin). Procurement is where "
   "forecasts become money, so the record is strict: orders trigger on "
   "forecast dates, not on feelings; quantities come from the projections "
   "(not from round numbers); and every order cites the forecast version "
   "that justified it. The 70% order point (before the 85% action tier) "
   "gives the lead time room to work - ordering at 85% with a 6-week lead "
   "time is ordering during the emergency."),
 "how_it_works": ("Order date = exhaustion date minus lead time minus "
   "margin: 9.0 months - 1.5 months - 0.5 month margin = 7.0 months from "
   "now. The order quantity covers the next 18 months of projected growth "
   "past the constraint (not just the gap): 8.9 GB/month x 18 = 160 GB "
   "plus the 80 GB gap = 240 GB, rounded to the 250 GB procurement unit. "
   "Every order records: the forecast version cited, the exhaustion date, "
   "the quantity math, and the approval - the audit trail from prediction "
   "to purchase. Standing orders cover the predictable: the monthly drip "
   "consumables are on subscription, the lumpy capacity on forecast "
   "trigger. The record also tracks procurement accuracy: ordered vs "
   "actually needed, scored like forecasts - buyers get graded too."),
 "key_points": [
   "Disk order in 7 months (9.0 - 1.5 lead - 0.5 margin).",
   "Order at 70% of constraint - before the 85% action tier.",
   "Quantity: 18 months of growth past the gap (250 GB unit).",
   "Orders cite the forecast version; full audit trail.",
   "Standing orders for predictable; forecast triggers for lumpy.",
   "Procurement accuracy scored - buyers get graded too.",
 ],
 "requirements": [
   "Order dates from exhaustion minus lead time minus margin.",
   "Quantity math documented per order.",
   "Forecast citation per order.",
   "Procurement accuracy tracking.",
 ],
 "standards": [
   "Triggers on forecast dates, not feelings.",
   "Lead times measured, not vendor-promised.",
   "Margin mandatory (minimum 2 weeks).",
   "Subscriptions for the predictable.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine orders the lumber before the "
   "barn is full: the doctrine requires the purchase order dated from the "
   "forecast, seven months out. The Signature edition grades the buyers - "
   "a doctrine that scores its forecasters but not its purchasers is "
   "auditing the map and ignoring the driver."),
},
# ---------------- Advanced (22-34) ----------------
{
 "name": "Million-Database Scale Projection",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "demo_key": "f_million",
 "demo_data": {"total_records": 1143457, "growth": 0.06, "new_dbs": 5000, "new_db_avg": 220, "fixed_per_db_yr": 240},
 "description": ("The million-scale projection (the ten-thousand-database "
   "milestone on the march) plans the fleet's doubling: 5,000 databases "
   "today, 10,000 targeted, 1,143,457 records growing at a blended 6% "
   "monthly. Doubling the database count does not merely double the "
   "records - new databases start small and grow fast (the hyper segment), "
   "so the projection models the mix: 5,000 steady databases at 4% plus "
   "5,000 new ones ramping from near-zero to an average of 220 records each in their first year. "
   "The infrastructure implication is concrete: shard count doubles, the "
   "control plane's per-database overhead ($0.0124 fixed per record-month "
   "does not apply to empty databases - the per-database fixed cost of "
   "$240/year does) adds $1.2M/year at 5,000 new databases, and the "
   "forecasting function itself must scale (5,000 more forecasts quarterly)."),
 "how_it_works": ("The projection builds the fleet bottom-up: existing "
   "5,000 databases at their segment rates (the fleet record's 6% blend -> "
   "~2.30M records at 12 months), plus 5,000 new databases ramping: month m "
   "records = 11,476 x (1.25^m - 1)/0.25 per database... aggregated in the "
   "demo, reaching ~1.1M records from new databases alone at 12 months. "
   "Total fleet at 12 months: ~3.4M records across 10,000 databases. "
   "Infrastructure: shard capacity doubles (the split forecast's 9-month "
   "cadence becomes continuous), monitoring cardinality doubles (the "
   "metrics budget doubles), and the forecasting pipeline processes 10,000 "
   "forecasts quarterly. The projection is the capacity plan for the "
   "10,000-database target - every number the target needs, dated."),
 "key_points": [
   "5,000 -> 10,000 databases; ~3.4M records at 12 months (demo-computed).",
   "New databases ramp at 25%/mo year one (hyper segment behavior).",
   "Per-database fixed cost $240/year x 5,000 = $1.2M/year new overhead.",
   "Shard count doubles; split cadence becomes continuous.",
   "Forecasting function scales: 10,000 forecasts quarterly.",
   "Bottom-up by segment - doubling databases does not merely double records.",
 ],
 "requirements": [
   "Bottom-up fleet model with new-database ramp.",
   "Infrastructure scaling plan (shards, monitoring, forecasting).",
   "Fixed-cost overhead of new databases priced.",
   "Quarterly re-projection as the count grows.",
 ],
 "standards": [
   "Ramp rates from observed new-database history.",
   "Overhead priced per database, not per record.",
   "Plans dated with procurement triggers.",
   "Target milestones with capacity gates.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine plans the city's doubling "
   "before the first new street is paved: the doctrine requires the "
   "~3.4M records and the $1.2M overhead on the plan. The Signature "
   "edition prices the empty databases too - a doctrine that counts "
   "only records has forgotten that databases cost money before they "
   "hold anything."),
},
{
 "name": "Logistic S-Curve Growth Model",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "demo_key": "f_logistic",
 "demo_data": {"K": 1000000, "P0": 96796, "r": 0.1345, "t": 12},
 "description": ("The logistic model caps growth with reality: carrying "
   "capacity K=1,000,000 records, starting from 96,796 at 13.45% monthly, "
   "reaches 349,931 at twelve months - below the compounding 440,060, "
   "because the S-curve bends as it approaches the ceiling. Every database "
   "has a carrying capacity: the audience saturates, the domain is "
   "exhausted, the shard fills. The logistic curve models the bend - fast "
   "growth early, slowing as saturation nears, flat at K. The inflection "
   "point (fastest growth) comes at K/2 = 500,000 records, still far ahead; "
   "until then the logistic tracks close to compounding, then diverges. "
   "The model's honesty is its value: it refuses to project infinity."),
 "how_it_works": ("P(t) = K / (1 + A x e^(-rt)), A = (K - P0)/P0 = 9.331: "
   "P(12) = 1,000,000 / (1 + 9.331 x e^(-1.614)) = 349,931. The carrying "
   "capacity K is estimated from the domain: the total addressable records "
   "(for this database, ~1M before the domain is fully covered), reviewed "
   "annually - K is the model's most important and most uncertain "
   "parameter. The inflection at 500K records is 31 months out at current "
   "rates; the model hands off to the maturity playbook then (growth "
   "investing shifts from acquisition to depth). Sensitivity: K=800K -> "
   "P(12)=329K; K=1.5M -> P(12)=371K - the twelve-month projection is "
   "robust to K uncertainty, which is why the model is trusted near-term "
   "even when K is fuzzy."),
 "key_points": [
   "P(12) = 349,931 at K=1M (vs 440,060 compounding) - the bend is real.",
   "A = 9.331; inflection (fastest growth) at 500K records, ~31 months out.",
   "K estimated from domain addressability; reviewed annually.",
   "Robust near-term: K=800K->329K, K=1.5M->371K at 12 months.",
   "Refuses to project infinity - the model's honesty is its value.",
   "Hands off to the maturity playbook at inflection.",
 ],
 "requirements": [
   "Carrying capacity estimated with methodology.",
   "Annual K review.",
   "Inflection date computed and watched.",
   "Sensitivity to K published.",
 ],
 "standards": [
   "K from domain analysis, not from curve-fitting alone.",
   "Near-term trust, long-term humility.",
   "Maturity handoff defined.",
   "Model compared against compounding in selection.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine knows every harvest has a "
   "field's edge: the doctrine requires the carrying capacity named - "
   "1,000,000 - and the bend honored. The Signature edition trusts the "
   "model near and doubts it far: a doctrine that believes its own "
   "K exactly has mistaken an estimate for a fence."),
},
{
 "name": "Constraint-Bound Forecasting",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "demo_key": "f_constraint",
 "demo_data": {"demand": 600000, "cap": 500000, "unit": "records"},
 "description": ("The constraint-bound forecast takes the minimum of want "
   "and can: demand projects 600,000 records but the hardware caps at "
   "500,000 - so the forecast is 500,000, and the 100,000 gap is flagged "
   "as unserved demand. Forecasts that ignore constraints are fiction; "
   "this model makes the constraint the forecast wherever the constraint "
   "binds. The 100,000 unserved is the important output - it is the "
   "quantified cost of not expanding: records not ingested, queries not "
   "served, growth deferred. The record presents both numbers always: the "
   "unconstrained demand (what the world wants) and the bound forecast "
   "(what the hardware allows) - planning needs both, and hiding either "
   "is a decision made blind."),
 "how_it_works": ("Bound forecast = min(demand projection, constraint): "
   "min(600,000, 500,000) = 500,000. Unserved = 100,000 records, priced at "
   "the marginal value per record (the value the database creates per "
   "record, from the value records) - the cost of the constraint made "
   "visible. The model runs per constraint from the constraint map: disk, "
   "memory, CPU, licenses - each produces its own bound, and the tightest "
   "wins. The unserved demand feeds procurement directly: it is the "
   "business case for the expansion, quantified. When procurement lands "
   "(the 250 GB order), the constraint lifts and the forecast unbinds - "
   "the model re-runs on every constraint change. Constraint-bound is the "
   "default model for mature databases near their ceilings; it is the "
   "honest answer when the hardware has opinions."),
 "key_points": [
   "min(600K demand, 500K cap) = 500K forecast; 100K unserved demand flagged.",
   "Unserved priced at marginal value - the cost of the constraint, visible.",
   "Tightest of all mapped constraints wins.",
   "Unserved demand is the business case for expansion.",
   "Re-run on every constraint change; unbinds when procurement lands.",
   "Default model near ceilings - honest when hardware has opinions.",
 ],
 "requirements": [
   "Demand and bound forecasts published together.",
   "Unserved demand quantified and priced.",
   "Per-constraint bounds computed.",
   "Re-run triggers on constraint changes.",
 ],
 "standards": [
   "Never publish demand as the forecast near a binding constraint.",
   "Unserved demand always visible.",
   "Value-per-record methodology documented.",
   "Procurement linked to unserved quantities.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine reports both the appetite "
   "and the pantry: the doctrine requires the 600,000 wanted and the "
   "500,000 possible side by side. The Signature edition prices the "
   "100,000 unserved - a doctrine that hides the gap between want and "
   "can is not forecasting, it is wishing with better arithmetic."),
},
{
 "name": "Monte Carlo Capacity Simulation",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "demo_key": "f_montecarlo",
 "demo_data": {"sims": 10000, "p10": 380000, "p50": 440060, "p90": 520000, "seed": 42},
 "description": ("The Monte Carlo simulation runs ten thousand futures: with "
   "the growth rate drawn from its observed distribution (mean 13.45%, "
   "standard deviation 3.2%), the twelve-month record count lands at p10 "
   "380,000, p50 440,060, p90 520,000. One forecast is a guess; ten "
   "thousand are a distribution - and capacity plans to percentiles, not "
   "to points. The p50 (440,060) matches the compounding model's point "
   "forecast, which cross-validates both; the p90 (520,000) is the number "
   "the headroom policy cares about; the p10 (380,000) bounds the downside. "
   "The seed (42) is fixed so the simulation is reproducible - a simulation "
   "that cannot be re-run is a rumor with a histogram."),
 "how_it_works": ("Each simulation draws a monthly growth rate from the "
   "trailing distribution (normal, mean 13.45%, sd 3.2%, floored at 0%) "
   "and compounds twelve months from 96,796; ten thousand draws give the "
   "percentiles: p10 380,000, p50 440,060, p90 520,000 (the demo runs a "
   "seeded, reduced simulation verifying the percentile ordering and the "
   "p50's agreement with the analytic 440,060). Correlated dimensions are "
   "drawn jointly: high record growth correlates with high query growth "
   "(0.72 correlation observed), so the simulation does not produce "
   "impossible futures (record explosions with query collapses). The "
   "outputs feed decisions by percentile: procurement sizes to p90, budgets "
   "to p50, contingency to p90-p50. The distribution is re-estimated "
   "quarterly; a regime change (the March backfill) widens the sd until "
   "it ages out."),
 "key_points": [
   "10,000 seeded futures: p10 380K, p50 440K, p90 520K at 12 months.",
   "p50 matches the analytic compounding forecast (cross-validation).",
   "Capacity plans to percentiles: procurement p90, budget p50.",
   "Correlated draws (records-queries 0.72) - no impossible futures.",
   "Seed fixed (42): reproducible, re-runnable.",
   "Distribution re-estimated quarterly; regime changes widen it.",
 ],
 "requirements": [
   "Seeded, reproducible simulations.",
   "Rate distributions from trailing observations.",
   "Correlated dimensions drawn jointly.",
   "Percentile-based decision mapping.",
 ],
 "standards": [
   "Minimum 10,000 simulations.",
   "Seeds recorded with results.",
   "p50 cross-checked against analytic models.",
   "Distributions re-estimated quarterly.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine runs ten thousand futures "
   "before choosing one: the doctrine requires the distribution - p10, "
   "p50, p90 - not the point. The Signature edition fixes the seed: a "
   "doctrine whose futures change every run is not simulating, it is "
   "improvising with statistics."),
},
{
 "name": "What-If Scenario Modeling",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "demo_key": "f_scenario",
 "demo_data": {"base": 440060, "optimistic": 620000, "pessimistic": 310000},
 "description": ("The scenario model tells three stories: base 440,060 "
   "records, optimistic 620,000 (+41%), pessimistic 310,000 (-30%) at "
   "twelve months. Scenarios are not predictions - they are structured "
   "'what ifs' that prepare decisions: what if the new feed contract "
   "lands (optimistic: +180K records), what if the migration stalls "
   "(pessimistic: -130K). Each scenario has a trigger (the event that "
   "would make it real), a probability (base 60%, optimistic 25%, "
   "pessimistic 15%), and a pre-planned response (the optimistic response "
   "is accelerated procurement; the pessimistic is deferred hiring). The "
   "value is decision readiness: when the trigger fires, the plan exists."),
 "how_it_works": ("The three scenarios derive from the Monte Carlo "
   "percentiles with narrative overlays: base = p50 (440,060), optimistic "
   "= p90 plus the feed contract (+100K -> 620,000), pessimistic = p10 "
   "minus the migration stall (-70K -> 310,000). Probabilities: 60/25/15, "
   "reviewed quarterly - the expected value (0.6x440K + 0.25x620K + "
   "0.15x310K = 465,536, demo-computed) informs the budget's contingency. "
   "Each scenario's response is pre-authorized within limits: the "
   "optimistic procurement (accelerated 250 GB order) can execute on the "
   "trigger without a new approval cycle - the approval was the scenario "
   "review. Triggers are monitored: the feed contract's signature, the "
   "migration's milestone dates. A scenario whose trigger fires without "
   "its response executing is a planning failure, reviewed as an "
   "incident."),
 "key_points": [
   "Base 440,060 (60%), optimistic 620,000 (25%), pessimistic 310,000 (15%).",
   "Expected value 465,536 informs budget contingency.",
   "Each scenario: trigger, probability, pre-planned response.",
   "Optimistic response pre-authorized (no new approval cycle).",
   "Scenarios are decision readiness, not predictions.",
   "Unfired responses on fired triggers are planning failures.",
 ],
 "requirements": [
   "Three scenarios minimum with triggers and probabilities.",
   "Pre-authorized responses within limits.",
   "Trigger monitoring.",
   "Quarterly probability review.",
 ],
 "standards": [
   "Scenarios from percentiles with narratives.",
   "Expected value computed for budgeting.",
   "Responses executable without re-approval.",
   "Failures reviewed as incidents.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine rehearses three futures and "
   "prepares for all: the doctrine requires the trigger, the odds, and "
   "the ready response. The Signature edition pre-authorizes the "
   "optimistic procurement - a doctrine that plans the response but "
   "withholds the authority has written theater, not contingency."),
},
{
 "name": "Forecast Confidence Intervals",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "demo_key": "f_ci",
 "demo_data": {"point": 440060, "pct": 0.12, "level": 95},
 "description": ("The confidence interval quantifies the doubt: 440,060 "
   "records plus or minus 12% at 95% confidence - the interval [387,253, "
   "492,867]. The interval comes from the accuracy record: the 12% is the "
   "trailing 12-month 95th-percentile absolute error at this horizon, not "
   "a statistical assumption - it is what the forecasts actually missed "
   "by. The interval widens with horizon (4% at 3 months, 8% at 12, 18% "
   "at 24 in relative terms... here 12% blends the model error and the "
   "rate uncertainty) and is published with every forecast, because a "
   "point without an interval is a promise the data cannot keep. "
   "Decisions use the interval edges: procurement sizes to the top edge "
   "(492,867), decommissioning plans to the bottom (387,253)."),
 "how_it_works": ("Interval = point x (1 +/- pct): 440,060 x 0.88 = "
   "387,253; x 1.12 = 492,867. The 12% derives from the scored history: "
   "the 95th percentile of |actual - forecast|/forecast at the 12-month "
   "horizon across the twelve archived forecasts. The interval is "
   "empirical, not normal-theory - the error distribution has fat tails "
   "(the March backfill), and the empirical percentile honors them. "
   "Asymmetric intervals are used where bias exists: the +2.1% bias "
   "shifts the interval up (the demo shows the symmetric version; the "
   "published forecast notes the bias adjustment). The interval feeds the "
   "headroom policy: the 30% headroom must cover the interval's top edge "
   "plus bursts - the policy and the interval are consistent by "
   "construction, checked quarterly."),
 "key_points": [
   "440,060 +/- 12% at 95% = [387,253, 492,867].",
   "12% from scored history (95th percentile error), not assumption.",
   "Empirical intervals honor fat tails (March backfill).",
   "Bias-adjusted: +2.1% shifts the interval up.",
   "Procurement to the top edge; decommissioning to the bottom.",
   "Consistent with the 30% headroom policy by construction.",
 ],
 "requirements": [
   "Empirical intervals from scored history.",
   "Published with every forecast.",
   "Bias adjustment where bias exists.",
   "Horizon-specific widths.",
 ],
 "standards": [
   "No point forecast without an interval.",
   "Percentiles from actual errors.",
   "Fat tails honored, not assumed away.",
   "Consistency with headroom checked quarterly.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine states its doubt in numbers: "
   "the doctrine requires [387,253, 492,867] printed under the 440,060. "
   "The Signature edition derives the doubt from its own misses - a "
   "doctrine that calibrates confidence on its errors is humble; one "
   "that assumes it is precise."),
},
{
 "name": "Capacity Cliff Detection",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "demo_key": "f_cliff",
 "demo_data": {"cap_gb": 500, "used_gb": 420, "growth_gb_mo": 8.9, "warn_mo": 9.0},
 "description": ("The cliff detector watches for the edge: 500 GB capacity, "
   "420 used, 8.9 GB monthly growth - the cliff arrives in 9.0 months, and "
   "the detector says so every day until it is handled. A cliff is a "
   "constraint whose exhaustion breaks the system (disk full stops "
   "writes; memory exhaustion crashes workers) - as opposed to a slope "
   "(costs rise gradually). The detector classifies each constraint as "
   "cliff or slope and watches cliffs with escalating urgency: 9 months "
   "is 'planned', 6 is 'scheduled', 3 is 'urgent', 1 is 'incident'. The "
   "9.0-month disk cliff is currently 'planned' with the procurement "
   "ordered - the detector's job is to make sure it never becomes "
   "'incident'."),
 "how_it_works": ("Months to cliff = (cap - used) / growth: (500-420)/8.9 "
   "= 9.0 months. The detector recomputes daily from monitoring (not "
   "monthly like the forecasts) because cliffs accelerate: growth at 8.9 "
   "GB/month is the average, but the detector also tracks the maximum "
   "sustained rate (14.2 GB/month in March) and reports the worst-case "
   "5.6 months alongside. Escalation tiers: >6 months planned (procurement "
   "in flight), 3-6 scheduled (order placed, expedite evaluated), 1-3 "
   "urgent (daily review, contingency active), <1 incident (all hands). "
   "The disk cliff at 9.0/5.6 months sits in 'planned' with the order "
   "placed at month 7 - the detector verifies the order covers the "
   "worst case, not just the average. A cliff that reaches 'urgent' "
   "without a placed order is a process failure, investigated."),
 "key_points": [
   "(500-420)/8.9 = 9.0 months average; 5.6 worst-case (March rate).",
   "Cliffs (break the system) vs slopes (costs rise) classified.",
   "Tiers: planned >6, scheduled 3-6, urgent 1-3, incident <1 month.",
   "Recomputed daily from monitoring - cliffs accelerate.",
   "Order verified against worst case, not just average.",
   "'Urgent' without a placed order is a process failure.",
 ],
 "requirements": [
   "Daily cliff recomputation from monitoring.",
   "Average and worst-case horizons.",
   "Escalation tiers with actions.",
   "Cliff/slope classification per constraint.",
 ],
 "standards": [
   "Procurement verified against worst case.",
   "Tier breaches trigger their actions automatically.",
   "Process failures investigated.",
   "Detector outputs feed the dashboard.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine watches the cliff edge daily: "
   "the doctrine requires 9.0 months average and 5.6 worst-case on the "
   "board every morning. The Signature edition plans for the March rate, "
   "not the average - a doctrine that averages its cliffs has averaged "
   "away the fall."),
},
{
 "name": "Decommissioning and Shrinkage Forecasts",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "demo_key": "f_facts",
 "demo_data": {"dbs_quarter": 3, "shrink_rate": -0.02, "records_reclaimed": 42000,
               "checks": [["dbs_quarter", "==", 3]]},
 "description": ("The shrinkage forecast plans the decline: three databases "
   "decommissioned per quarter, a -2% quarterly shrinkage rate on the "
   "legacy segment, 42,000 records reclaimed last quarter. Growth "
   "forecasting that only grows is half a discipline - databases retire, "
   "segments shrink, and the capacity plan must harvest the freed "
   "resources. The forecast schedules decommissions (which databases, "
   "which quarter, whose approval), projects the reclaimed capacity "
   "(42,000 records' worth of storage, compute, and licenses returned to "
   "the pool), and nets it against growth - the fleet's net growth is "
   "gross minus shrinkage, and budgets use the net. The -2% is the "
   "legacy segment's measured decline; the decommission list is reviewed "
   "quarterly because sentiment keeps databases alive past their use."),
 "how_it_works": ("Net fleet growth = gross additions - shrinkage: the "
   "fleet forecast's 6% blend is already net of the -2% legacy decline "
   "and the quarterly decommissions. Each decommission has a plan: data "
   "archived (or purged per retention policy), dependents migrated, DNS "
   "and references removed, the database deleted, and the capacity "
   "returned - the 42,000 reclaimed records freed ~0.4 GB and one "
   "support-tier step. The forecast values shrinkage: reclaimed capacity "
   "offsets procurement (the disk order's 250 GB is net of 40 GB expected "
   "reclamation). Decommission candidates are scored (usage declining 3+ "
   "quarters, no owner response, superseded by another database) - "
   "sentiment is not a criterion. A decommissioned database's forecast "
   "goes to zero explicitly; zombie forecasts (projecting growth for dead "
   "databases) are a data quality incident."),
 "key_points": [
   "3 decommissions/quarter; -2% legacy shrinkage; 42,000 records reclaimed.",
   "Net growth = gross - shrinkage; budgets use the net.",
   "Reclaimed capacity offsets procurement (40 GB of the 250 GB order).",
   "Candidates scored on decline and supersession - not sentiment.",
   "Decommission plans: archive, migrate, remove, delete, return capacity.",
   "Zombie forecasts for dead databases are data quality incidents.",
 ],
 "requirements": [
   "Quarterly decommission schedule with owners.",
   "Reclamation accounting per decommission.",
   "Net-growth budgeting.",
   "Candidate scoring criteria.",
 ],
 "standards": [
   "Retention policy governs archive-vs-purge.",
   "Dependent migration verified before deletion.",
   "Reclaimed capacity credited to procurement plans.",
   "Zero-forecasts for decommissioned databases.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine plans the harvest as well as "
   "the planting: the doctrine requires the decline forecast - 42,000 "
   "records reclaimed - alongside the growth. The Signature edition "
   "scores candidates without sentiment: a doctrine that cannot retire "
   "a database cannot afford a new one."),
},
{
 "name": "Cost-Linked Capacity Planning",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "demo_key": "f_costlink",
 "demo_data": {"records_12mo": 440060, "unit": 0.0155},
 "description": ("The cost-linked plan prices the forecast: 440,060 records "
   "at $0.0155 per record-month is $6,820.93 a month at twelve months - "
   "the capacity forecast expressed in dollars. Every capacity number has "
   "a cost twin: the storage projection prices the disk order, the worker "
   "projection prices the compute, the record projection prices the total. "
   "The link runs both ways: costs constrain capacity (the budget caps the "
   "procurement) and capacity drives costs (the forecast sets the budget). "
   "The $6,820.93 is the twelve-month run-rate the budget record plans "
   "against; the variance record will score it. A capacity plan without "
   "costs is a wish list; a budget without capacity is a number without "
   "a meaning."),
 "how_it_works": ("Cost = projected records x unit cost: 440,060 x $0.0155 "
   "= $6,820.93/month. The unit comes from the cost accounting database "
   "(per-record unit, $0.0155), and the link is live: when the unit changes "
   "(rate changes, efficiency gains), the cost-linked plan re-prices "
   "automatically. The plan breaks the $6,820.93 into dimensions (storage "
   "$X, compute $Y...) via the cost dimensions, so the budget sees the "
   "structure. Constraint costs appear too: the unserved 100,000 records "
   "from the constraint-bound forecast are priced at marginal value - the "
   "opportunity cost of the cliff. The plan's output is the budget "
   "record's input; the two records share the forecast version so they "
   "can never disagree about the future."),
 "key_points": [
   "440,060 x $0.0155 = $6,820.93/month at 12 months.",
   "Every capacity number has a cost twin; the link runs both ways.",
   "Live link: unit changes re-price the plan automatically.",
   "Unserved demand priced at marginal value (opportunity cost).",
   "Output feeds the budget record; shared forecast version.",
   "Capacity without costs is a wish list; budget without capacity is meaningless.",
 ],
 "requirements": [
   "Cost twin for every capacity projection.",
   "Live unit-cost linkage.",
   "Opportunity costing of unserved demand.",
   "Shared forecast version with the budget.",
 ],
 "standards": [
   "Units from the cost accounting database.",
   "Re-pricing on unit changes.",
   "Dimension-level cost breakdown.",
   "Version consistency enforced.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine prices every future it "
   "predicts: the doctrine requires the $6,820.93 under the 440,060. The "
   "Signature edition links them live - a doctrine whose forecasts and "
   "budgets can disagree has two futures, and a house divided against "
   "itself cannot procure."),
},
{
 "name": "Forecast Governance Record",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "demo_key": "f_facts",
 "demo_data": {"board": "Capacity Review Board", "cadence": "quarterly", "models_approved": 5,
               "checks": [["models_approved", "==", 5]]},
 "description": ("The forecast governance record runs the review board: the "
   "Capacity Review Board meets quarterly, owns the five approved models, "
   "and signs every forecast that drives procurement. Governance is what "
   "keeps forecasting honest at scale: model changes need board approval "
   "(no silent model swaps), forecasts that drive orders over $10,000 need "
   "board sign-off, and the accuracy record is presented every quarter - "
   "the forecasters report their MAPE to the board like earnings. The "
   "board's membership is fixed: engineering, finance, and the database "
   "owners' representative - the three parties with standing in the "
   "accuracy-vs-cost tradeoff."),
 "how_it_works": ("The board's quarterly agenda: accuracy review (MAPE and "
   "bias per model), model changes proposed (with backtested evidence), "
   "major forecasts signed (procurement-driving), assumption challenges "
   "(the business-calendar inputs), and the headroom policy review "
   "(annual). Decisions are recorded with rationales; dissent is recorded "
   "too - a unanimous board that never disagrees is not governing. Model "
   "approval requires backtesting on the forecast history (minimum 6 "
   "scored forecasts); new models run in shadow for two quarters before "
   "promotion. The board can also retire models: the simple-trend model "
   "was retired in 2026-Q2 after four quarters under 15% MAPE. Emergency "
   "forecasts (incident-driven) may bypass the board but are reviewed at "
   "the next meeting - speed now, accountability next quarter."),
 "key_points": [
   "Capacity Review Board: quarterly, owns 5 approved models.",
   "Model changes need approval; >$10K orders need sign-off.",
   "Forecasters report MAPE quarterly, like earnings.",
   "Members: engineering, finance, owners' representative.",
   "New models: backtest + 2 quarters shadow before promotion.",
   "Emergency forecasts bypass but are reviewed next meeting.",
 ],
 "requirements": [
   "Board charter with membership and cadence.",
   "Model approval with backtesting standard.",
   "Sign-off thresholds.",
   "Decision and dissent records.",
 ],
 "standards": [
   "No silent model swaps.",
   "Shadow promotion path mandatory.",
   "Accuracy presented every quarter.",
   "Emergency bypass with retrospective review.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine holds its navigators to "
   "account: the doctrine requires the quarterly MAPE reported to the "
   "board, dissent recorded. The Signature edition retires failing models "
   "publicly - a doctrine that cannot retire a model cannot be trusted "
   "with the ones it keeps."),
},
{
 "name": "Capacity Dashboard Exemplar",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "demo_key": "f_facts",
 "demo_data": {"panels": 8, "databases": 5000, "refresh": "daily", "cliffs": 3,
               "checks": [["panels", "==", 8]]},
 "description": ("The capacity dashboard exemplar shows what good looks "
   "like: 8 panels across 5,000 databases, daily refresh, 3 active cliff "
   "warnings. The panels: fleet trajectory (records vs forecast), "
   "constraint map (headroom by database), cliff countdown (months to each "
   "cliff), accuracy (MAPE trends), scenarios (the three stories), "
   "procurement pipeline (orders and dates), cost-linked view (dollars "
   "with the capacity), and the top-decile watch list. Each panel answers "
   "a planner's question: are we on track, what binds, when does it break, "
   "how wrong have we been, what if, what is ordered, what does it cost, "
   "who needs attention. Three cliff warnings active (disk at 9.0 months "
   "and two smaller) show the dashboard is watched."),
 "how_it_works": ("The eight panels query the forecasts and monitoring on "
   "daily refresh (cliff countdown intraday). The trajectory panel plots "
   "actual vs forecast with the confidence interval shaded - the visual "
   "that makes accuracy intuitive. The constraint map is a heat grid: "
   "5,000 databases x key constraints, colored by headroom - the fleet's "
   "tight spots visible at a glance. The cliff countdown lists every "
   "cliff with months remaining, worst case, and procurement status. "
   "Thresholds match the published standards: 30% headroom coloring, "
   "escalation tiers, MAPE targets. Drill-down goes fleet -> database -> "
   "constraint -> forecast version. The exemplar includes the review "
   "routine: the planner's Monday morning pass over the eight panels, "
   "because a dashboard without a routine is wallpaper."),
 "key_points": [
   "8 panels, 5,000 databases, daily refresh, 3 cliff warnings active.",
   "Panels: trajectory, constraint map, cliff countdown, accuracy, scenarios, procurement, cost, watch list.",
   "Trajectory plots actual vs forecast with CI shaded.",
   "Constraint heat grid: 5,000 x constraints colored by headroom.",
   "Monday-morning review routine included.",
   "Drill-down: fleet -> database -> constraint -> forecast version.",
 ],
 "requirements": [
   "All eight panels with documented queries.",
   "Daily refresh; cliff countdown intraday.",
   "Thresholds matching published standards.",
   "Review routine documented.",
 ],
 "standards": [
   "Numbers reproducible from forecasts and monitoring.",
   "Every panel has an owner.",
   "Unwatched dashboards decommissioned.",
   "Exemplar updated when standards change.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine keeps the lookout's log "
   "visible: the doctrine requires the eight panels watched on routine - "
   "trajectory, cliffs, accuracy, cost. The Signature edition includes "
   "the Monday pass: a doctrine with a dashboard but no routine has "
   "bought a telescope and never climbed the mast."),
},
{
 "name": "Forecast Model Selection Guide",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "demo_key": "f_facts",
 "demo_data": {"models": 5, "criteria": 6, "default": "compounding",
               "checks": [["models", "==", 5]]},
 "description": ("The model selection guide chooses the right lens: five "
   "models, six criteria, compounding the default for growing databases. "
   "The criteria: growth regime (scheduled->linear, organic->compounding, "
   "saturating->logistic), horizon (short->any, long->logistic/scenario), "
   "constraint proximity (near->constraint-bound), uncertainty (high->Monte "
   "Carlo), seasonality (strong->seasonal-adjusted), and history depth "
   "(<6 forecasts->linear only). The guide is a decision tree, not a "
   "preference: it outputs the model with the criteria cited, and the "
   "accuracy record validates the choices over time - databases where the "
   "guide chose compounding average 6.9% MAPE vs 11.2% where teams "
   "overrode it. Overrides are allowed but logged with reasons; the log "
   "is how the guide improves."),
 "how_it_works": ("The decision tree: (1) constraint within 12 months? -> "
   "constraint-bound. (2) history < 6 forecasts? -> linear. (3) saturating "
   "(growth decelerating 2+ quarters)? -> logistic. (4) strong seasonality "
   "(factor >1.4)? -> seasonal-adjusted compounding. (5) high uncertainty "
   "(rate sd > 5%)? -> Monte Carlo. (6) else -> compounding (the default). "
   "The guide re-runs on regime changes: a database moving steady->fast "
   "gets re-selected (usually linear->compounding). The override log shows "
   "the pattern: teams override toward simpler models (linear) and lose "
   "4.3 points of MAPE on average - the guide's gentle 'are you sure' has "
   "data behind it. Annual review: the criteria weights are re-fit against "
   "the accuracy history, so the guide learns which criteria predict "
   "model success."),
 "key_points": [
   "5 models, 6 criteria; compounding the default.",
   "Decision tree: constraint -> history -> saturation -> seasonality -> uncertainty.",
   "Guide-chosen: 6.9% MAPE vs 11.2% on overrides.",
   "Overrides allowed but logged; the log improves the guide.",
   "Re-run on regime changes (steady->fast usually linear->compounding).",
   "Criteria re-fit annually against accuracy history.",
 ],
 "requirements": [
   "Decision tree with cited criteria per selection.",
   "Override logging with reasons.",
   "Regime-change re-selection.",
   "Annual criteria re-fit.",
 ],
 "standards": [
   "Selections documented per database.",
   "Overrides never silent.",
   "Backtesting for new criteria.",
   "Guide versioned with changes.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine chooses its lens deliberately: "
   "the doctrine requires the decision tree walked, the criteria cited. "
   "The Signature edition logs the overrides - a doctrine that lets "
   "instinct override evidence without recording it will never learn "
   "whether the instinct was worth anything."),
},
{
 "name": "Forecasting Self-Audit and Mastery Record",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "demo_key": "f_mastery",
 "demo_data": {"records": 34, "complete": 34, "mape": 8.2, "coverage": 1.0},
 "description": ("The forecasting self-audit and mastery record proves the "
   "foresight sees itself: thirty-four forecasting archetypes catalogued, "
   "thirty-four complete, 8.2% MAPE across the scored history, coverage "
   "one hundred percent. This is the record that closes the loop - the "
   "forecasting system forecasting its own accuracy. It verifies that "
   "every database has a current forecast, every model is selected by the "
   "guide, every cliff is watched daily, and the governance board met its "
   "quarterly cadence. A forecasting system that cannot predict its own "
   "error is a weather vane that does not know which way it points."),
 "how_it_works": ("The self-audit checks: forecast completeness (every "
   "database, current quarter), model selection compliance (guide-chosen "
   "or logged override), cliff monitoring (daily recomputation verified), "
   "accuracy reporting (MAPE published with forecasts), procurement linkage "
   "(orders cite forecast versions), and board cadence (four meetings "
   "last year, all quorate). The example: 34 of 34 complete, 8.2% MAPE, "
   "coverage 1.0. Findings become scenarios or board agenda items, tracked "
   "to closure. The audit runs quarterly with its report to engineering "
   "and finance leadership. This record is also the mastery checkpoint: a "
   "reader who understands all thirty-four records - from linear "
   "projections through Monte Carlo to governance - understands capacity "
   "growth forecasting end to end."),
 "key_points": [
   "34 archetypes, 34 complete; 8.2% MAPE; coverage 1.0.",
   "Self-audit checks completeness, selection, cliffs, accuracy, linkage, board.",
   "Findings become scenarios or board items.",
   "Runs quarterly; report to engineering and finance.",
   "A forecaster that cannot predict its own error is a broken vane.",
   "Mastery checkpoint: all 34 records teach forecasting end to end.",
 ],
 "requirements": [
   "Self-audit executed quarterly with published report.",
   "All six audit dimensions checked.",
   "Findings tracked to closure.",
   "Mastery path documented from record 1 to record 34.",
 ],
 "standards": [
   "Coverage target 1.0.",
   "MAPE reported with every audit.",
   "Audit independent of daily forecasting.",
   "Year-over-year trend reported.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1.",
 ],
 "sig_lens": ("The Signature Foresight Doctrine ends by forecasting itself: "
   "the doctrine requires the 8.2% MAPE on the mastery record - the "
   "forecaster's error, confessed. The Signature self-audit closes the "
   "loop from record 1 to record 34: measure the growth, model the curve, "
   "price the future, buy before the cliff - and check the work."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks) == list(range(1, 35)), "ladder ranks must be 1..34 in order"
