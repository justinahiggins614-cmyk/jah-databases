#!/usr/bin/env python3
"""Authored records for the Data Observability databases (group F, part 1).
Public = real, fact-checked data-observability knowledge (freshness, drift,
anomalies, pipeline health). Signature = expanded Signature treatment.
Property of Justin Addam Higgins (JAH)."""

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
dict(
name="What Data Observability Is",
group="Observability Basics", ladder_rank=1, ladder_tier="foundations",
description="""Data observability is the discipline of knowing your data is healthy without manually checking it: automated monitoring of freshness, distribution, volume, schema, and lineage that detects problems and alerts before consumers are hurt. It is the data equivalent of application observability - where SRE teams monitor latency and errors, data teams monitor staleness and drift. The need is the same: systems too large and fast for human inspection, failures that are silent (the pipeline ran fine but the data is wrong), and consumers who discover problems last. Observability answers five questions continuously: is the data fresh (freshness), does it still look like itself (distribution), is there the expected amount (volume), is the shape unchanged (schema), and is the journey intact (lineage)? When all five are green, data is observable; when any goes red, the system says so - loudly, with evidence, before the dashboard lies to an executive.""",
how_it_works="""Observability platforms deploy monitors per dataset: freshness trackers watching watermarks against SLAs, distribution profilers comparing current data to baselines, volume counters against expected ranges, schema validators against registered schemas, and lineage health checks on the pipeline graph. Monitors run on schedules or streaming windows, write their verdicts to a metrics store, and fire alerts through routing rules when thresholds breach. Dashboards show the five pillars per dataset with history; incident workflows attach the evidence. The platform is configured from contracts and SLAs where they exist, and from learned baselines where they do not - then tuned as false positives teach it what normal looks like.""",
key_points=[
 "Data observability: automated health monitoring for data, like SRE for applications.",
 "Five pillars: freshness, distribution, volume, schema, lineage.",
 "Detects silent failures - pipelines that run fine but produce wrong data.",
 "Alerts fire before consumers are hurt, with evidence attached.",
 "Configured from contracts where they exist, learned baselines where they do not."],
requirements=[
 "Monitors per dataset covering all five pillars.",
 "Alert routing with evidence attached.",
 "Dashboards with per-pillar history.",
 "Tuning workflows driven by false-positive feedback."],
standards=[
 "OpenLineage for lineage pillar.",
 "ISO 8000-8 for quality measurement."],
citations=[
 "Barr D. Data Observability (industry literature).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: observability is the registry's sleepless watch - five senses on every dataset, alarming before harm lands. The Signature watch never blinks and never cries wolf without evidence.""",
demo_data={"feeds":[
 {"name":"sales","last_hours_ago":1,"sla_hours":2,"null_rate":0.01},
 {"name":"clicks","last_hours_ago":5,"sla_hours":2,"null_rate":0.02}],
 "expect_stale":["clicks"]},
),
dict(
name="The Five Pillars of Observability",
group="Observability Basics", ladder_rank=2, ladder_tier="foundations",
description="""The five pillars give observability its structure, each watching a different failure mode. Freshness watches time: is the data as current as promised, measured by watermarks and delivery timestamps against SLAs? Distribution watches shape: do the values still follow their historical patterns, measured by statistical comparison to baselines? Volume watches quantity: are row counts in the expected range, catching the half-loaded table and the duplicated feed? Schema watches structure: are the fields, types, and nullability unchanged, catching the silent column rename? Lineage watches the journey: are the pipelines and sources healthy, catching the broken upstream before its damage lands? The pillars interact: a volume drop with fresh timestamps means a partial load; a distribution shift with schema change means a redefined field. Mature observability monitors all five because real incidents rarely respect pillar boundaries.""",
how_it_works="""Each dataset gets a pillar profile: freshness SLA and measurement, distribution baselines per key column, volume expectations (absolute ranges or seasonal models), registered schema, and lineage health checks. Monitors evaluate each pillar on schedule; pillar verdicts combine into dataset health with the worst pillar setting the tone. Cross-pillar correlation rules interpret combinations - the volume-drop-plus-fresh pattern pages differently than volume-drop-plus-stale. Pillar coverage is itself monitored: a dataset missing distribution baselines is flagged as under-observed. Reviews tune pillar thresholds per dataset from incident history.""",
key_points=[
 "Freshness: time - watermarks vs SLAs. Distribution: shape - current vs baseline.",
 "Volume: quantity - row counts vs expected ranges. Schema: structure - fields and types.",
 "Lineage: journey - pipeline and source health.",
 "Cross-pillar patterns diagnose better than single pillars.",
 "Pillar coverage is monitored; under-observed datasets are flagged."],
requirements=[
 "Pillar profiles per dataset with SLAs, baselines, ranges, schemas.",
 "Scheduled monitors per pillar with combined health verdicts.",
 "Cross-pillar correlation rules for diagnosis.",
 "Coverage monitoring with under-observation flagging."],
standards=[
 "ISO 8000-8 for quality measurement.",
 "OpenLineage for lineage pillar."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Barr D. Data Observability (industry literature)."],
sig_lens="""The Signature reading: the five pillars are the watch's five senses - time, shape, quantity, structure, journey - each vigilant, together wise. The Signature watch reads their combinations like an experienced physician reads symptoms.""",
demo_data={"feeds":[
 {"name":"orders","last_hours_ago":0.5,"sla_hours":1,"null_rate":0.005},
 {"name":"inventory","last_hours_ago":0.2,"sla_hours":1,"null_rate":0.001}],
 "expect_stale":[]},
),
dict(
name="Freshness Tracking",
group="Freshness and Volume", ladder_rank=3, ladder_tier="foundations",
description="""Freshness tracking answers the most-asked data question: how old is this data? The machinery is watermarks - markers of event-time progress - and delivery timestamps, compared continuously against the freshness SLA. For batch, freshness is the max event time in the latest partition versus now; for streaming, it is the watermark position versus now. Tracking must handle the subtleties: late-arriving data (the watermark says midnight but stragglers arrive at 2 AM), timezone correctness (freshness computed in the wrong zone lies), and partial freshness (the table refreshed but one source partition is missing). Freshness dashboards show each dataset's lag against its SLA as a live number, with history revealing chronic lateness patterns. When freshness breaches, the alert carries the diagnosis so far: which upstream is late, by how much, and whether it is getting worse - because a freshness alert without a cause is just anxiety.""",
how_it_works="""Producers emit watermarks or the platform infers them from max event timestamps per partition. The freshness monitor computes lag as now minus watermark, compares to the SLA, and publishes the live lag metric with history. Late-data handling defines the policy: stragglers update the watermark with a correction event, or they wait for the next window per the contract. Timezone discipline keeps all freshness math in UTC with display conversion. Partial-freshness detection compares per-source-partition watermarks, flagging the missing piece. Breach alerts include the upstream attribution - which source or step is the laggard - and the trend (improving or worsening).""",
key_points=[
 "Freshness = now minus watermark, tracked live against the SLA.",
 "Batch uses partition max event times; streaming uses watermark positions.",
 "Late data, timezones, and partial freshness need explicit policies.",
 "Breach alerts carry upstream attribution and trend, not just anxiety.",
 "Freshness history reveals chronic lateness patterns."],
requirements=[
 "Watermark emission or inference per dataset.",
 "Live lag computation with SLA comparison and history.",
 "Late-data, timezone, and partial-freshness policies.",
 "Breach alerts with upstream attribution and trend."],
standards=[
 "Open Data Contract Standard (freshness SLAs).",
 "ISO 8601 for timestamp handling."],
citations=[
 "Akidau T et al. Streaming Systems. O'Reilly, 2018.",
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol."],
sig_lens="""The Signature reading: freshness tracking is the watch's clock - every dataset's age read live against its sworn hours. The Signature clock names the laggard and says whether time is healing or worsening.""",
demo_data={"feeds":[
 {"name":"feed_a","last_hours_ago":3,"sla_hours":4,"null_rate":0.01},
 {"name":"feed_b","last_hours_ago":9,"sla_hours":4,"null_rate":0.03}],
 "expect_stale":["feed_b"]},
),
dict(
name="SLA Clocks and Watermarks",
group="Freshness and Volume", ladder_rank=4, ladder_tier="foundations",
description="""SLA clocks turn freshness promises into running measurements. Each dataset's clock starts from its SLA: data through midnight must land by 6 AM, so at 6:01 the clock shows breach. Watermarks are the clock's hands: the event-time marker asserting all data through time T has arrived. Low watermarks (conservative, waiting for stragglers) trade freshness for completeness; high watermarks (aggressive) trade completeness for freshness - the choice is contractual. Idle partitions need special handling: a watermark that never advances because no data arrived looks identical to a stuck pipeline, so heartbeats distinguish silence from death. Clock skew between producers' event times and the platform's processing time is monitored; when skew grows, watermarks lie. The registry keeps the clock definitions with the contracts they enforce, so every freshness verdict cites the SLA version it measured against.""",
how_it_works="""SLA clocks are configured from contract freshness terms with the promise, measurement method, and remedy. Watermark policies per dataset set the straggler wait and the lateness handling. Heartbeats from idle sources keep their watermarks honest. Skew monitors compare event-time vs processing-time drift; breaching skew quarantines the watermark as untrustworthy. Clock verdicts (on-time, at-risk, breached) publish with the SLA version cited. At-risk warnings fire before breach - at 80 percent of the SLA window - giving producers time to recover. Clock history feeds chronic-lateness analysis and SLA renegotiation.""",
key_points=[
 "SLA clocks measure live against the promised freshness terms.",
 "Watermark policies trade straggler-wait against freshness aggressively or conservatively.",
 "Heartbeats distinguish idle sources from stuck pipelines.",
 "Clock-skew monitoring keeps watermarks honest.",
 "At-risk warnings fire before breach; history feeds SLA renegotiation."],
requirements=[
 "SLA clocks configured from contract terms with cited versions.",
 "Watermark policies with straggler and lateness handling.",
 "Heartbeat requirements for idle sources.",
 "At-risk warnings and chronic-lateness analysis."],
standards=[
 "Open Data Contract Standard (freshness SLAs)."],
citations=[
 "Akidau T et al. Streaming Systems. O'Reilly, 2018.",
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol."],
sig_lens="""The Signature reading: SLA clocks are the watch's sworn timepieces - each dataset's promise made into a running clock, each watermark an honest hand. The Signature timepiece warns before it condemns and cites the promise it keeps.""",
demo_data={"feeds":[
 {"name":"sla_ok","last_hours_ago":1,"sla_hours":6,"null_rate":0.01},
 {"name":"sla_risk","last_hours_ago":5,"sla_hours":6,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Staleness Detection",
group="Freshness and Volume", ladder_rank=5, ladder_tier="foundations",
description="""Staleness detection catches data that stopped being current: the feed that silently stopped Tuesday, the dashboard still showing last week's numbers, the model training on month-old features. Detection compares each dataset's data age against its expected cadence with tolerance bands - a daily feed is stale after 36 hours, an hourly feed after 90 minutes - and escalates with age: warning at the band edge, paging when the data is a full cycle late, incident when consumers are making decisions on it. The subtle cases need care: seasonally idle datasets (the ski resort's bookings in summer) must not page; backfill windows must not mask real staleness; and timezone-shifted schedules must not false-alarm twice a year. Staleness detection also watches the watchers: a freshness monitor that stopped reporting is itself stale, and meta-monitoring catches it.""",
how_it_works="""Staleness rules per dataset define cadence, tolerance bands, and escalation with age. Seasonal calendars suppress expected-idle periods; backfill markers distinguish intentional replays from real delays. Escalation tiers fire warning, page, and incident at increasing lateness, each with the upstream attribution. Meta-monitoring watches the monitors: a freshness metric older than its own reporting interval triggers a monitor-health alert. Staleness incidents link to the freshness history and the upstream lineage, so responders see the full picture. Post-incident, the tolerance bands are reviewed - false alarms tighten or loosen the bands with recorded reasons.""",
key_points=[
 "Staleness = data age beyond cadence plus tolerance, escalating with age.",
 "Seasonal idleness, backfills, and timezone shifts need explicit handling.",
 "Escalation tiers: warning, page, incident - each with upstream attribution.",
 "Meta-monitoring catches stale monitors themselves.",
 "Tolerance bands are reviewed after every false alarm."],
requirements=[
 "Per-dataset staleness rules with cadence and tolerance bands.",
 "Seasonal calendars and backfill markers.",
 "Age-escalated alerting with upstream attribution.",
 "Meta-monitoring of monitor health."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016."],
sig_lens="""The Signature reading: staleness detection is the watch's nose for rot - sniffing out the feed that died Tuesday while the dashboard still smiles. The Signature nose knows seasons, forgives backfills, and never lets its own senses go unchecked.""",
demo_data={"feeds":[
 {"name":"daily_feed","last_hours_ago":30,"sla_hours":36,"null_rate":0.01},
 {"name":"dead_feed","last_hours_ago":100,"sla_hours":36,"null_rate":0.05}],
 "expect_stale":["dead_feed"]},
),
dict(
name="Volume Monitoring",
group="Freshness and Volume", ladder_rank=6, ladder_tier="foundations",
description="""Volume monitoring watches row counts: the table that usually gets a million rows got twelve thousand (partial load), or got three million (duplicated feed). Expectations come in three forms: absolute ranges (this table gets 900K-1.1M rows daily), relative change limits (no more than 20 percent day-over-day swing), and seasonal models (retail volumes spike in December - the model knows). The monitor compares each load's count against the expectation and breaches with the diagnosis: partial, duplicated, missing, or shifted. Volume anomalies are the most common early signal of pipeline bugs - the join that dropped its key, the filter that got too aggressive, the source that sent the day twice. Volume monitoring also watches the watchers' blind spot: a table with the right row count but all nulls passes volume and fails everything else, which is why volume is one pillar among five.""",
how_it_works="""Volume expectations per dataset are set from history: absolute bands, change limits, or seasonal models fit to past counts. Each load's count is compared; breaches classify as partial, duplicated, missing, or shifted with the evidence. Seasonal models account for known cycles (holidays, month-ends) with calendars. Change-point detection flags when the baseline itself shifts - the business doubled, and the old bands are obsolete - triggering re-baselining instead of eternal alerts. Volume verdicts combine with the other pillars: right count but wrong distribution means something subtler broke. Re-baselining is governed: proposed new bands need steward approval, not silent auto-adjustment.""",
key_points=[
 "Volume expectations: absolute bands, change limits, or seasonal models.",
 "Breaches classify as partial, duplicated, missing, or shifted.",
 "Volume anomalies are the most common early pipeline-bug signal.",
 "Change-point detection re-baselines when the business itself shifts.",
 "Right count with wrong distribution means subtler breakage - check all pillars."],
requirements=[
 "Volume expectations per dataset from historical analysis.",
 "Seasonal calendars for known cycles.",
 "Change-point detection with governed re-baselining.",
 "Cross-pillar combination of volume verdicts."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003."],
sig_lens="""The Signature reading: volume monitoring is the watch's counting hand - every load counted against expectation, every shortfall or surplus named. The Signature counter knows the seasons and re-learns the business when it outgrows old bands.""",
demo_data={"feeds":[
 {"name":"normal","last_hours_ago":1,"sla_hours":2,"null_rate":0.01},
 {"name":"partial","last_hours_ago":1,"sla_hours":2,"null_rate":0.4}],
 "expect_stale":[]},
),
dict(
name="Row-Count Anomalies",
group="Freshness and Volume", ladder_rank=7, ladder_tier="foundations",
description="""Row-count anomalies are volume monitoring's bread and butter: the specific patterns of wrong counts and what they mean. A sudden drop to near zero means the source went dark or the extract failed open. A drop to a fraction means a filter changed or a join lost its key. A doubling means the feed ran twice or a union duplicated. A gradual decline means upstream decay - customers churning, sensors dying. A step change that persists means the business changed - and the baseline must follow. The diagnostic discipline is to read the count in context: compare against the source's own counts (did the source shrink, or did we lose rows?), against sibling datasets (did all feeds from this source drop?), and against the calendar (is this a holiday?). Row-count anomaly playbooks encode these checks so the on-call does not reinvent them at 3 AM.""",
how_it_works="""Anomaly classifiers label each volume breach with a pattern: cliff, fraction, multiple, decay, step. Each pattern triggers its playbook: cliff checks source health; fraction checks recent filter/join changes; multiple checks for duplicate runs; decay checks upstream trends; step checks for business changes and proposes re-baselining. Context enrichment attaches source counts, sibling dataset counts, and calendar flags automatically. Playbook outcomes feed back: confirmed diagnoses tune the classifiers. Anomaly records persist with their diagnoses, building the estate's memory of what each pattern meant last time.""",
key_points=[
 "Patterns: cliff (source dark), fraction (lost join), multiple (duplicate run), decay, step.",
 "Read counts in context: source counts, sibling datasets, calendar.",
 "Playbooks encode the diagnostic checks for the on-call.",
 "Step changes that persist mean the business changed - re-baseline.",
 "Anomaly records build the estate's diagnostic memory."],
requirements=[
 "Pattern classifiers for volume breaches.",
 "Context enrichment: source, sibling, calendar data.",
 "Diagnostic playbooks per pattern.",
 "Anomaly records with diagnoses feeding classifier tuning."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: row-count anomalies are the watch reading footprints - cliff, fraction, multiple, decay, step - each with its meaning and its playbook. The Signature tracker remembers what each print meant last time.""",
demo_data={"feeds":[
 {"name":"steady","last_hours_ago":2,"sla_hours":4,"null_rate":0.02},
 {"name":"cliff","last_hours_ago":2,"sla_hours":4,"null_rate":0.02}],
 "expect_stale":[]},
),
dict(
name="Schema Drift Detection",
group="Distribution and Drift", ladder_rank=8, ladder_tier="foundations",
description="""Schema drift is change in the data's shape: a renamed column, a new field, a type change from integer to string, a nullability flip. Drift detection compares each delivery's observed schema against the registered schema and reports the diff: added, removed, renamed (inferred), retyped, nullability-changed. Not all drift is bad - the new optional field is expected evolution - but all drift is news, because every drift changes what consumers can assume. Detection must be smart about the forms drift takes: case changes, reordered columns, and whitespace differences are noise; semantic changes are signal. The registry classifies drift by compatibility impact and routes accordingly: compatible drift notifies, breaking drift pages and quarantines. Drift history per dataset shows whether a schema is stabilizing or churning - the churn rate is itself a health metric that contract negotiations use.""",
how_it_works="""Schema snapshots are taken per delivery and diffed against the registered schema with noise filtering (case, order, whitespace). Diffs classify each change: added-optional, added-required, removed, renamed-inferred, retyped, nullability-changed. Compatibility rules map changes to impact: breaking changes trigger quarantine and paging per the contract; compatible changes notify. Renames are inferred by similarity (old column vanished, similar new column appeared) and proposed for human confirmation. Drift metrics - changes per month, breaking rate - feed dataset health scores and contract reviews. Schema registries enforce the same checks at registration time for streaming.""",
key_points=[
 "Drift detection diffs observed vs registered schemas per delivery.",
 "Noise (case, order) is filtered; semantic changes are signal.",
 "Changes classify by compatibility impact: notify vs quarantine-and-page.",
 "Renames are inferred by similarity and confirmed by humans.",
 "Drift history shows schema stability; churn rate is a health metric."],
requirements=[
 "Per-delivery schema snapshots with noise-filtered diffing.",
 "Compatibility classification of detected changes.",
 "Rename inference with human confirmation.",
 "Drift metrics feeding health scores and contract reviews."],
standards=[
 "Confluent Schema Registry compatibility rules."],
citations=[
 "Apache Avro Specification (schema resolution).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: schema drift detection is the watch's eye for changing shapes - every added, removed, or retyped field noticed, classified, and routed. The Signature eye ignores noise, names real change, and never lets a breaking shape pass unchallenged.""",
demo_data={"feeds":[
 {"name":"stable","last_hours_ago":1,"sla_hours":2,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Distribution Shift Detection",
group="Distribution and Drift", ladder_rank=9, ladder_tier="foundations",
description="""Distribution shift is when the data's values change their pattern: the average order value drifts down, a category's share doubles, the null rate in a field triples. Shift detection compares current value distributions against baselines - the historical pattern - using statistical measures, and alerts when the difference exceeds thresholds. Shifts matter because models and rules assume the past resembles the future: a fraud model trained on last year's transaction patterns degrades as patterns shift, and a report's year-over-year comparison lies when the underlying population changed. Not all shifts are problems - genuine business change (expansion into a new market) shifts distributions legitimately - so shift alerts carry the diagnosis: which segments moved, by how much, and whether the shift looks like business change or data corruption. The response differs: business change updates baselines and retrains models; corruption triggers incident response.""",
how_it_works="""Baselines per key column are built from historical distributions (histograms for numerics, frequency tables for categoricals). Current windows are compared with statistical measures - Population Stability Index, Kolmogorov-Smirnov, chi-square - each with alert thresholds tuned per column. Segment drill-downs show which slices moved (which region, which product line). Shift classification distinguishes business change (broad, explainable, correlated with known events) from corruption (narrow, inexplicable, correlated with pipeline changes). Confirmed business change triggers re-baselining with approval; corruption triggers incident workflows. Model monitoring consumes shift signals to schedule retraining.""",
key_points=[
 "Shift detection compares current distributions to baselines statistically.",
 "Shifts break models and reports that assume the past resembles the future.",
 "Alerts diagnose: which segments moved, business change or corruption?",
 "Business change re-baselines with approval; corruption triggers incidents.",
 "Shift signals feed model retraining schedules."],
requirements=[
 "Distribution baselines per key column with statistical comparison.",
 "Tuned thresholds per column (PSI, KS, chi-square).",
 "Segment drill-downs for shift diagnosis.",
 "Re-baselining workflows with approval."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "Sculley D et al. Hidden technical debt in machine learning systems. NeurIPS, 2015."],
sig_lens="""The Signature reading: shift detection is the watch's sense for changing tides - measuring the waters against memory, naming which currents moved, judging whether the sea changed or the river was poisoned.""",
demo_data={"feeds":[
 {"name":"stable_dist","last_hours_ago":1,"sla_hours":2,"null_rate":0.02},
 {"name":"shifted","last_hours_ago":1,"sla_hours":2,"null_rate":0.15}],
 "expect_stale":[]},
),
dict(
name="Statistical Tests for Drift: KS and PSI",
group="Distribution and Drift", ladder_rank=10, ladder_tier="foundations",
description="""Two workhorse statistics quantify distribution shift. The Kolmogorov-Smirnov (KS) test measures the maximum gap between the cumulative distributions of baseline and current - a single number between 0 and 1 where 0 means identical and larger means more different, with well-known significance thresholds. PSI (Population Stability Index) bins both distributions into deciles and sums the per-bin shifts weighted by size - practitioners read PSI under 0.1 as stable, 0.1-0.25 as moderate shift worth watching, above 0.25 as significant shift needing action. KS is sensitive to any distributional difference and needs no binning; PSI is intuitive per-bin and standard in credit risk. Both need care: tiny samples produce noisy statistics, so tests require minimum sample sizes; and both flag statistically significant but practically irrelevant shifts, so thresholds are tuned per column with business judgment. The registry standardizes which test applies where and publishes the thresholds, so drift verdicts are consistent across the estate.""",
how_it_works="""Drift monitors compute KS and PSI per monitored column per window against the baseline, enforcing minimum sample sizes before testing. Thresholds per column map statistics to verdicts (stable, watch, action) with the business rationale recorded. Results publish with the underlying distributions attached so humans can see the shift, not just the number. Threshold tuning uses historical labeled shifts - known incidents vs known non-events - to set per-column bars. The statistics feed dashboards and model monitoring; sustained watch-level drift triggers review, action-level triggers response.""",
key_points=[
 "KS: max cumulative gap, 0-1, no binning needed, sensitive to any difference.",
 "PSI: binned shift index; <0.1 stable, 0.1-0.25 watch, >0.25 action (practitioner rule).",
 "Minimum sample sizes required; tiny samples make noisy statistics.",
 "Thresholds tuned per column with business judgment, not just significance.",
 "Standardized test selection keeps drift verdicts consistent estate-wide."],
requirements=[
 "KS and PSI computation per monitored column per window.",
 "Minimum sample size enforcement.",
 "Per-column thresholds with recorded business rationale.",
 "Historical tuning from labeled shift events."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "Massey F. The Kolmogorov-Smirnov test for goodness of fit. JASA, 1951.",
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003."],
sig_lens="""The Signature reading: KS and PSI are the watch's calibrated instruments - one measuring the widest gap, the other weighing every bin's drift. The Signature watch calibrates each instrument to its column and trusts no reading from too small a sample.""",
demo_data={"feeds":[
 {"name":"ks_ok","last_hours_ago":1,"sla_hours":2,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Missing-Value Reports",
group="Distribution and Drift", ladder_rank=11, ladder_tier="foundations",
description="""Missing-value reports track nulls and empties: which fields are missing how often, in which segments, trending which way. A missing-value report per dataset shows null rates per column with history, null patterns (which columns go missing together - the joint-null signature of a broken join), and segment breakdowns (nulls concentrated in one region's data). The reports distinguish the kinds of missing: never-populated (the field the source never sends), recently-missing (was populated, now null - investigate), and structurally-missing (not applicable for this record type - expected). Trends matter most: a null rate creeping from 1 to 5 percent over a month is upstream decay caught early; a jump to 40 percent overnight is an incident. Missing-value reports feed contracts (population-rate promises), survivorship (trust signals), and cleansing (re-verification triggers) - the null is data about the data.""",
how_it_works="""Profilers compute null/empty rates per column per delivery with segment breakdowns and joint-null analysis. Reports classify missingness: never, recent, structural - using history and record-type rules. Trend monitors alert on creeping increases and step jumps with different severities. Segment concentration flags point at the responsible source or region. Reports publish to dataset dashboards and feed the contract's population-rate promises and the registry's trust signals. Structural missingness is documented per record type so it never pages. Investigation workflows start from the report's drill-downs.""",
key_points=[
 "Reports show null rates per column with history, joint patterns, and segments.",
 "Missingness classifies as never, recent, or structural - each handled differently.",
 "Creeping null rates signal upstream decay; jumps signal incidents.",
 "Joint-null patterns reveal broken joins; segment concentration reveals bad sources.",
 "Reports feed contracts, trust signals, and cleansing triggers."],
requirements=[
 "Per-delivery null profiling with segments and joint analysis.",
 "Missingness classification with history.",
 "Trend alerting for creeps and jumps.",
 "Integration with contracts and trust signals."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: missing-value reports are the watch's census of absences - every null counted, patterned, and trended. The Signature census knows which absences are natural, which are decay, and which are emergencies.""",
demo_data={"feeds":[
 {"name":"complete","last_hours_ago":1,"sla_hours":2,"null_rate":0.02},
 {"name":"decaying","last_hours_ago":1,"sla_hours":2,"null_rate":0.18}],
 "expect_stale":[]},
),
dict(
name="Null-Rate Monitoring",
group="Distribution and Drift", ladder_rank=12, ladder_tier="foundations",
description="""Null-rate monitoring watches the single most telling quality metric continuously: the share of nulls per column, checked every delivery against expected bands. Bands come from history with business judgment - the middle-name field is 40 percent null and that is fine; the order-amount field must be 0 percent null and any null is a breach. Monitoring distinguishes absolute breaches (nulls where zero are allowed) from band breaches (null rate outside the expected range) and from trend breaches (rate moving consistently in the wrong direction). Correlated nulls get special attention: when five columns go null together, the cause is structural (a join failed, a source section went missing), not five independent problems. Null-rate alerts carry the classification and the likely scope, so responders start from the right hypothesis. The monitors also watch for the opposite failure: a field that should sometimes be null suddenly never is - the default-value bug that fills nulls with zeros.""",
how_it_works="""Null-rate expectations per column define absolute limits, bands, and trend rules. Each delivery's rates are checked; breaches classify as absolute, band, or trend with severity. Correlation analysis groups co-occurring null spikes into single incidents with structural hypotheses. Zero-null-violation fields page immediately; band breaches warn; trend breaches open investigations. Default-value detection flags fields whose null rate collapses to zero unexpectedly. All verdicts publish with history; the monitors' own health is meta-monitored.""",
key_points=[
 "Null rates checked per column per delivery against absolute limits, bands, trend rules.",
 "Correlated nulls indicate structural causes - one incident, not five.",
 "Zero-null fields page on any null; band breaches warn; trends investigate.",
 "Watch the opposite failure: nulls replaced by default values.",
 "Verdicts publish with history; monitors are meta-monitored."],
requirements=[
 "Per-column null expectations: limits, bands, trend rules.",
 "Correlation analysis grouping co-occurring spikes.",
 "Severity-tiered alerting with hypothesis attached.",
 "Default-value collapse detection."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: null-rate monitoring is the watch's vigil over emptiness - every column's nulls counted against sworn bands, correlated spikes read as single structural cries. The Signature vigil even watches for nulls murdered by default values.""",
demo_data={"feeds":[
 {"name":"ok_nulls","last_hours_ago":1,"sla_hours":2,"null_rate":0.03}],
 "expect_stale":[]},
),
]
