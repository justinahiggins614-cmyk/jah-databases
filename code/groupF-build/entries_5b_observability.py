#!/usr/bin/env python3
"""Data Observability entries 13-24 (compounded)."""

APPEND = [
dict(
name="Anomaly Detection Basics",
group="Anomalies and Alerts", ladder_rank=13, ladder_tier="compounded",
description="""Anomaly detection finds the unusual without being told what to look for: the metric that deviates from its own history, the pattern that breaks its seasonality, the value that has never been seen before. The methods form a ladder of sophistication. Thresholds: alert when the metric crosses a fixed line - simple, explainable, blind to context. Statistical: alert when the metric leaves its historical bands (mean plus/minus N standard deviations, or quantile bands) - context-aware but fooled by shifting baselines. Seasonal decomposition: separate trend, seasonality, and residual, and alert on the residual - handles the retail December spike correctly. Machine learning: isolation forests, autoencoders, and forecasting models that learn normal deeply - powerful but opaque and hungry for tuning. The practice that matters most is not the method but the feedback loop: every alert's true/false verdict retunes the detector, because an anomaly detector that cannot learn becomes either silent or a boy who cried wolf.""",
how_it_works="""Detectors are configured per metric with the method suited to its behavior: thresholds for contractual limits, statistical bands for stable metrics, seasonal models for cyclical ones, ML for complex multivariate cases. Each detection carries the evidence: the metric's history chart with the anomalous point marked, the expected range, and the deviation magnitude. Alert verdicts (true positive, false positive) feed back into threshold tuning and model retraining. Cold-start metrics get conservative defaults until enough history accumulates. Detector health dashboards show precision per detector - the share of alerts that were real - and detectors below the bar are retuned or retired.""",
key_points=[
 "Methods ladder: thresholds, statistical bands, seasonal decomposition, ML.",
 "Thresholds are simple and explainable; ML is powerful but opaque.",
 "The feedback loop matters most: alert verdicts retune detectors.",
 "Cold-start metrics get conservative defaults until history accumulates.",
 "Detector precision is monitored; poor detectors are retuned or retired."],
requirements=[
 "Per-metric detector configuration matched to metric behavior.",
 "Evidence attached to every detection: history, expected range, deviation.",
 "Verdict feedback loops into tuning and retraining.",
 "Detector precision dashboards with retirement policies."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "Chandola V, Banerjee A, Kumar V. Anomaly detection: a survey. ACM Computing Surveys, 2009.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: anomaly detection is the watch's instinct for the wrong - learned from history, sharpened by every verdict. The Signature instinct distrusts its own first impressions until the evidence confirms them, and learns from every mistake.""",
demo_data={"feeds":[
 {"name":"metric_a","last_hours_ago":1,"sla_hours":2,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Threshold Alerts vs ML Alerts",
group="Anomalies and Alerts", ladder_rank=14, ladder_tier="compounded",
description="""Threshold alerts and ML alerts serve different masters. Threshold alerts fire when a metric crosses a line everyone agreed on: null rate above 5 percent, freshness beyond the SLA, error count above zero. They are explainable (the line was crossed), auditable (the line is in the contract), and cheap - the right choice for contractual limits and known-bad conditions. ML alerts fire when the metric deviates from learned normal: the isolation forest flags this combination of features as unlike history, the forecaster says this value is outside the prediction interval. They catch the unknown unknowns - the failure mode nobody wrote a threshold for - but they are opaque (why did it fire?), hungry (needing tuning and history), and prone to novel-but-fine alerts. Mature observability uses both: thresholds guard the known, ML explores the unknown, and every ML alert that proves real becomes a candidate for a threshold - the unknown, once understood, joins the known.""",
how_it_works="""Threshold alerts configure directly from contracts and known limits with the line, the severity, and the rationale recorded. ML alerts train on historical metrics with labeled incidents where available; their outputs include anomaly scores and contributing features for explainability. A promotion workflow converts validated ML discoveries into thresholds: when the same ML alert fires truly three times with the same signature, a threshold proposal goes to the owning team. Alert routing distinguishes the two: threshold breaches page per contract severity, ML alerts notify for investigation. Both feed the same incident workflow once confirmed.""",
key_points=[
 "Threshold alerts guard the known: contractual, explainable, auditable, cheap.",
 "ML alerts explore the unknown: catching failure modes nobody thresholded.",
 "Validated ML discoveries promote into thresholds - the unknown joins the known.",
 "ML alerts need anomaly scores and contributing features for explainability.",
 "Routing differs: thresholds page per contract, ML notifies for investigation."],
requirements=[
 "Threshold alerts configured from contracts with recorded rationale.",
 "ML detectors trained on history with explainability outputs.",
 "Promotion workflows from validated ML alerts to thresholds.",
 "Differentiated routing per alert kind."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "Chandola V, Banerjee A, Kumar V. Anomaly detection: a survey. ACM Computing Surveys, 2009.",
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016."],
sig_lens="""The Signature reading: thresholds are the watch's standing orders - clear lines, certain responses. ML is the watch's intuition - sensing what no order foresaw. The Signature watch honors both, and promotes proven intuitions into standing orders.""",
demo_data={"feeds":[
 {"name":"metric_b","last_hours_ago":2,"sla_hours":4,"null_rate":0.02}],
 "expect_stale":[]},
),
dict(
name="Alert Routing and On-Call",
group="Anomalies and Alerts", ladder_rank=15, ladder_tier="compounded",
description="""Alerts are useless if they reach the wrong person or reach the right person as noise. Routing sends each alert to the team that owns the failing dataset or pipeline, at the severity the contract demands, through the channel the situation needs: pages for contract breaches affecting consumers, tickets for warnings, chat messages for informational. On-call rotations ensure a human is always reachable, with escalation chains when the primary does not acknowledge - and acknowledgment means I am working on it, not I saw it. Routing rules encode the ownership map (dataset to team to rotation), severity mapping (breach class to page-or-ticket), and quiet hours policies (the non-critical warning waits for morning; the consumer-facing breach pages now). The routing table is itself governed: ownership changes update it, or alerts rot in departed teams' queues. Alert quality is measured end to end: time to acknowledge, time to resolve, and the false-positive rate per route.""",
how_it_works="""The ownership map links datasets and pipelines to teams and their on-call rotations. Routing rules map alert classes to severities and channels; escalation chains fire on unacknowledged pages. Quiet-hours policies defer non-critical alerts with morning digests. Ownership changes propagate to routing automatically from the registry's ownership metadata. Routing health metrics - acknowledge times, resolve times, false-positive rates per route - are reviewed with the owning teams. Misrouted alerts get rerouted with the rule fixed; the fix is the point, not the reroute.""",
key_points=[
 "Routing sends each alert to the owning team at the contracted severity.",
 "Pages for consumer-affecting breaches; tickets for warnings; chat for info.",
 "Escalation chains fire on unacknowledged pages; acknowledgment means working on it.",
 "Quiet-hours policies defer non-critical alerts to morning digests.",
 "Routing tables update with ownership changes; alert quality is measured end to end."],
requirements=[
 "Ownership maps from datasets to teams to rotations.",
 "Routing rules with severity mapping and escalation chains.",
 "Quiet-hours policies with digest delivery.",
 "End-to-end alert quality metrics per route."],
standards=[
 "Site Reliability Engineering alerting practices."],
citations=[
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: alert routing is the watch's chain of command - every alarm to its rightful officer, at the urgency the covenant demands, with escalation when the officer sleeps. The Signature chain is kept current and its performance is inspected.""",
demo_data={"feeds":[
 {"name":"metric_c","last_hours_ago":1,"sla_hours":3,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Alert Fatigue and Tuning",
group="Anomalies and Alerts", ladder_rank=16, ladder_tier="compounded",
description="""Alert fatigue is the slow death of observability: too many alerts, too many false, and the on-call stops reading them - so the real breach hides in the noise it created. The cures are systematic. Precision over recall: it is better to miss a subtle anomaly than to page falsely ten times, because the eleventh page - the real one - will be ignored. Deduplication and grouping: fifty alerts from one incident become one incident with fifty symptoms. Severity honesty: if it pages, it must need a human now; everything else is a ticket. Tuning cadence: weekly alert reviews where the team dispositions every alert - true, false, or unactionable - and tunes or deletes accordingly. And the nuclear option, used sparingly: alert budgets, capping pages per team per week, forcing prioritization of what truly deserves to wake someone. The metric that matters is alert precision trending up and page volume trending down while incident catch rate holds.""",
how_it_works="""Alert review rituals disposition every alert weekly: true (keep), false (tune the detector), unactionable (delete the alert or fix the underlying condition). Deduplication groups alerts by incident using correlation rules. Severity audits reclassify pages that did not need immediate humans. Tuning changes are versioned with before/after precision measurements. Alert budgets cap pages per team per week with override processes for genuine crises. Fatigue surveys - asking the on-call directly - catch what metrics miss. The tuning loop is itself monitored: teams that skip reviews get their alerting privileges reviewed.""",
key_points=[
 "Fatigue kills observability: false pages train the on-call to ignore real ones.",
 "Precision over recall: fewer, truer alerts beat noisy coverage.",
 "Deduplicate by incident; be honest about severity; review weekly.",
 "Alert budgets cap pages, forcing prioritization of what truly wakes humans.",
 "Measure precision up, page volume down, catch rate holding."],
requirements=[
 "Weekly alert disposition rituals with tune-or-delete outcomes.",
 "Deduplication and correlation grouping.",
 "Severity audits with reclassification.",
 "Alert budgets with override processes."],
standards=[
 "Site Reliability Engineering alerting practices."],
citations=[
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016.",
 "Chandola V, Banerjee A, Kumar V. Anomaly detection: a survey. ACM Computing Surveys, 2009."],
sig_lens="""The Signature reading: fatigue is the watch's greatest enemy - not the dark, but the crying wolf that deafens the garrison. The Signature watch speaks rarely and truly, groups its cries by battle, and audits its own voice weekly.""",
demo_data={"feeds":[
 {"name":"metric_d","last_hours_ago":1,"sla_hours":2,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Pipeline-Failure Records",
group="Pipeline Health", ladder_rank=17, ladder_tier="compounded",
description="""Pipeline-failure records are the incident reports of data engineering: every failed run documented with what failed, when, why, what it affected, and how it was fixed. A failure record captures the job, the run ID, the failure time and stage, the error (with logs linked), the blast radius (downstream datasets and consumers affected, from lineage), the response timeline (detected, acknowledged, fixed, verified), and the prevention item filed. Failure records serve three masters: the immediate incident (coordinating response), the post-mortem (learning), and the trend analysis (is this pipeline getting flakier? is this error pattern spreading?). The records live in the observability system linked to lineage, so any dataset's health view shows its pipeline's failure history. Blameless by policy: records name systems and causes, never scapegoats - the goal is prevention, and blame kills the honesty prevention needs.""",
how_it_works="""Orchestrators emit failure events with job, run, stage, error, and timing; the registry enriches them with blast radius from lineage and opens the failure record. Responders work the record: acknowledge, diagnose, fix, verify - each step timestamped. Post-mortems attach root cause and prevention items with owners. Trend analysis aggregates failures by pipeline, error pattern, and time - flakiness scores per pipeline, spreading patterns across the estate. Blameless policy is enforced in review: records are audited for blame language. Failure records feed reliability metrics: MTBF and MTTR per pipeline, feeding SLA negotiations and investment decisions.""",
key_points=[
 "Failure records: what, when, why, blast radius, response timeline, prevention.",
 "Serve incidents, post-mortems, and trend analysis from one record.",
 "Blast radius comes from lineage; response steps are timestamped.",
 "Blameless by policy: name systems and causes, never scapegoats.",
 "Trends reveal flaky pipelines and spreading error patterns."],
requirements=[
 "Failure event emission from orchestrators with error details.",
 "Blast-radius enrichment from lineage.",
 "Timestamped response workflows with post-mortems.",
 "Trend analysis with flakiness scoring per pipeline."],
standards=[
 "Site Reliability Engineering incident practices."],
citations=[
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016.",
 "OpenLineage. OpenLineage Specification. Linux Foundation."],
sig_lens="""The Signature reading: failure records are the watch's battle reports - every defeat documented honestly, every lesson filed, no blame cast. The Signature chronicler studies defeats to prevent their recurrence.""",
demo_data={"feeds":[
 {"name":"pipe_a","last_hours_ago":1,"sla_hours":2,"null_rate":0.02}],
 "expect_stale":[]},
),
dict(
name="Retry and Backfill Records",
group="Pipeline Health", ladder_rank=18, ladder_tier="compounded",
description="""Retries and backfills are how pipelines recover, and their records prove the recovery actually happened. A retry record shows the failed run, the retry attempt, what changed (code fix, config change, or just transient-flake retry), and the successful outcome - distinguishing the healthy transient retry from the pipeline that needed five retries and a code patch. A backfill record shows the recomputed range, the reason (source correction, logic bug, missed window), the code version used, and the verification that the backfilled data matches expectations. The discipline matters because silent retries hide flakiness and silent backfills rewrite history: every retry and backfill is a lineage event, visible in the affected datasets' histories, with the reason recorded. Backfill verification compares the recomputed data against quality expectations before it replaces the old - a backfill that introduces new errors is worse than the gap it filled.""",
how_it_works="""Orchestrators emit retry events linked to their failed runs with attempt numbers and change descriptions; backfill jobs emit scope, reason, code version, and verification results. The registry links retries to failures and backfills to the affected partitions as lineage events. Retry analysis flags pipelines with rising retry rates for flakiness investigation. Backfill verification runs quality checks on recomputed data before promotion; failures quarantine the backfill. Histories of affected datasets show the retry/backfill events inline, so consumers see that Tuesday's numbers were recomputed Wednesday and why.""",
key_points=[
 "Retry records distinguish transient flakes from pipelines needing fixes.",
 "Backfill records show range, reason, code version, and verification.",
 "Every retry and backfill is a visible lineage event, never silent.",
 "Backfills verify against quality expectations before replacing data.",
 "Rising retry rates flag flakiness for investigation."],
requirements=[
 "Retry event emission linked to failed runs.",
 "Backfill records with scope, reason, version, verification.",
 "Lineage visibility of retries and backfills in dataset histories.",
 "Retry-rate trend analysis with flakiness flagging."],
standards=[
 "OpenLineage (run facets)."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016."],
sig_lens="""The Signature reading: retries and backfills are the watch's record of recoveries - each second attempt documented, each rewritten history verified. The Signature record never lets a recovery happen in the dark.""",
demo_data={"feeds":[
 {"name":"pipe_b","last_hours_ago":2,"sla_hours":4,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Data Quality Scores",
group="Pipeline Health", ladder_rank=19, ladder_tier="compounded",
description="""Data quality scores compress the six quality dimensions into numbers decision-makers can use: this dataset scores 94 overall, with completeness at 98 and timeliness at 87. Scores are computed per dimension from the underlying metrics, then combined - usually weighted, with the weights reflecting business priorities (a fraud dataset weights accuracy over completeness). Scores serve the audiences that will not read metric tables: executives see portfolio scores, consumers see the datasets they depend on, producers see their own trend. The scoring methodology is published and versioned - a score nobody can explain is a number nobody trusts. Score changes trigger explanations: the score dropped 6 points because timeliness breached twice this week. And scores have consequences tied to contracts: sustained low scores breach quality promises, trigger improvement plans, or renegotiate the promises to honest levels.""",
how_it_works="""Scoring jobs compute dimension scores from metric values against targets, then combine with published weights into dataset scores, rolling up to domain and portfolio scores. Methodologies version with change logs; score histories show trends. Explanations attach to significant changes, naming the driving metrics. Scores publish to dashboards, catalogs (as dataset badges), and contract compliance views. Contract integration ties sustained low scores to promise-breach workflows. Weight reviews happen annually or when business priorities shift - the weights encode what the organization values.""",
key_points=[
 "Scores compress six quality dimensions into usable numbers per dataset.",
 "Weighted combination reflects business priorities; methodology published and versioned.",
 "Audiences: executives see portfolios, consumers see dependencies, producers see trends.",
 "Score changes carry explanations naming the driving metrics.",
 "Sustained low scores trigger contract consequences."],
requirements=[
 "Published, versioned scoring methodologies with weights.",
 "Dimension and combined scores with history.",
 "Change explanations on significant moves.",
 "Contract integration for sustained low scores."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: quality scores are the watch's report card - six subjects graded, weighted by what matters, every grade explainable. The Signature grader publishes the rubric and never grades in secret.""",
demo_data={"feeds":[
 {"name":"scored","last_hours_ago":1,"sla_hours":2,"null_rate":0.02}],
 "expect_stale":[]},
),
dict(
name="Quality Trend Dashboards",
group="Pipeline Health", ladder_rank=20, ladder_tier="compounded",
description="""Quality trend dashboards show where data health is heading, not just where it is: the null rate creeping up for six weeks, the freshness SLA breached three times this month, the distribution shift that started after the source migration. Trends beat snapshots because most data problems are slow - decay, drift, and rot announce themselves in trends long before they breach thresholds. Dashboards layer the views: metric time series with bands and breach markers, pillar health timelines per dataset, estate heatmaps showing problem areas, and annotations marking the events (deploys, migrations, incidents) that explain the moves. The review ritual matters more than the dashboard: weekly quality reviews where owners explain their trends and commit to actions. A dashboard nobody reviews is wallpaper; a reviewed one is the organization's early-warning system.""",
how_it_works="""Dashboards render metric time series, pillar timelines, estate heatmaps, and event annotations from the metrics store. Annotation feeds mark deploys, migrations, and incidents on the timelines automatically. Review workflows assign trend anomalies to owners with expected actions. Heatmaps aggregate to domain and portfolio levels for executive views. Dashboard usage is itself monitored - views nobody opens are redesigned or retired. Trend alerts fire on sustained directional moves before thresholds breach, giving the early warning that snapshots cannot.""",
key_points=[
 "Trends beat snapshots: decay announces itself in trends before breaching thresholds.",
 "Layers: metric series, pillar timelines, estate heatmaps, event annotations.",
 "Weekly quality reviews with owner explanations and committed actions.",
 "Trend alerts fire on sustained moves before threshold breaches.",
 "Dashboards nobody reviews are wallpaper - usage is monitored."],
requirements=[
 "Time-series dashboards with bands, breaches, and event annotations.",
 "Estate heatmaps aggregating to domain and portfolio.",
 "Review workflows assigning trends to owners.",
 "Trend alerts on sustained directional moves."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003."],
sig_lens="""The Signature reading: trend dashboards are the watch's far-sight - seeing the rot coming weeks before it breaches. The Signature far-seer marks every event on the timeline and holds weekly councils on what the trends portend.""",
demo_data={"feeds":[
 {"name":"trended","last_hours_ago":1,"sla_hours":2,"null_rate":0.04}],
 "expect_stale":[]},
),
dict(
name="Profiling Schedules",
group="Pipeline Health", ladder_rank=21, ladder_tier="compounded",
description="""Profiling schedules decide how often each dataset gets measured: the critical feed profiles every load, the stable dimension table profiles weekly, the archive profiles quarterly. Scheduling balances cost against risk: profiling is compute, and profiling everything every hour is wasteful - but the unprofiled dataset is where the next incident hides. Schedules derive from data tier and volatility: tier-1 data profiles per delivery, volatile data profiles often, stable reference data profiles rarely. Event-triggered profiling supplements schedules: a schema change, a volume anomaly, or a consumer complaint triggers an immediate profile. Profile results feed every downstream use - quality scores, trust signals, drift baselines, missing-value reports - so the schedule is really the heartbeat of the whole observability system. Missed profiles are themselves monitored: a dataset whose profiling stopped is flying blind, and the schedule monitor says so.""",
how_it_works="""Profiling policies per dataset define cadence from tier and volatility, plus event triggers (schema change, anomaly, complaint). The scheduler runs profilers and publishes results to the metrics store feeding scores, trust, baselines, and reports. Cost controls cap profiling spend per dataset with sampling for the largest tables. Schedule compliance is monitored: missed or late profiles alert like any other staleness. Policy reviews adjust cadences from incident history - the dataset that surprised everyone gets profiled more often.""",
key_points=[
 "Cadence from tier and volatility: critical per delivery, stable weekly, archives quarterly.",
 "Event triggers supplement schedules: schema changes, anomalies, complaints.",
 "Profiles feed scores, trust, baselines, reports - the observability heartbeat.",
 "Sampling caps cost on the largest tables.",
 "Missed profiles alert; policies adjust from incident history."],
requirements=[
 "Per-dataset profiling policies with cadence and triggers.",
 "Scheduler with cost controls and sampling.",
 "Schedule compliance monitoring.",
 "Policy reviews driven by incident history."],
standards=[
 "ISO 8000-8 for quality measurement.",
 "DAMA-DMBOK data quality guidance."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: profiling schedules are the watch's rounds - every dataset inspected on its appointed round, the critical hourly, the archives quarterly. The Signature watchman never skips a round and reports the missed ones.""",
demo_data={"feeds":[
 {"name":"profiled","last_hours_ago":1,"sla_hours":2,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Freshness for Streaming Data",
group="Pipeline Health", ladder_rank=22, ladder_tier="compounded",
description="""Streaming freshness is measured in watermarks, not batch completions: how far behind reality is the stream's event-time progress? The monitor tracks watermark lag per partition - the slowest partition sets the stream's freshness - and pages when lag exceeds the SLA. Streaming brings its own failure modes: a single poisoned key can stall one partition's watermark while the rest flow (the hot-partition stall), idle partitions need heartbeats to advance, and late data policies decide whether stragglers update history or are dropped. Freshness SLAs for streams are tighter and mean more: a 5-minute SLA on a fraud stream is a business promise, not a technical nicety. The observability platform treats streaming freshness as a first-class pillar with its own dashboards, because batch freshness tooling cannot see watermark stalls.""",
how_it_works="""Stream processors expose watermark positions per partition; the monitor computes lag against now and the SLA. Hot-partition detection flags single partitions lagging while others flow. Heartbeat requirements keep idle partitions honest. Late-data policies (update vs drop) are declared per stream and visible in freshness views. Breach alerts carry the stalled partitions and the suspected cause (poisoned key, downstream backpressure, source outage). Watermark history feeds capacity planning - chronic lag means under-provisioned processing.""",
key_points=[
 "Streaming freshness = watermark lag per partition; slowest sets the pace.",
 "Hot-partition stalls: one poisoned key can stall a single partition.",
 "Idle partitions need heartbeats; late-data policies are declared.",
 "Stream SLAs are business promises with first-class dashboards.",
 "Chronic watermark lag signals under-provisioned processing."],
requirements=[
 "Per-partition watermark exposure and lag monitoring.",
 "Hot-partition and idle-partition detection.",
 "Declared late-data policies per stream.",
 "Watermark history for capacity planning."],
standards=[
 "Open Data Contract Standard (freshness SLAs)."],
citations=[
 "Akidau T et al. Streaming Systems. O'Reilly, 2018.",
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol."],
sig_lens="""The Signature reading: streaming freshness is the watch timing rivers - every partition's progress against the sworn minutes. The Signature timer finds the single stuck eddy and names the poison in it.""",
demo_data={"feeds":[
 {"name":"stream_a","last_hours_ago":0.1,"sla_hours":0.5,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Observability Metadata",
group="Pipeline Health", ladder_rank=23, ladder_tier="compounded",
description="""Observability metadata describes the monitoring itself: which monitors watch which datasets, with what thresholds, owned by whom, alerting where, with what history of tuning. This metadata is what makes observability governable: coverage reports show which datasets lack monitors, ownership records route alerts, threshold histories explain why a line sits where it does, and tuning logs show the feedback loop working. Without it, monitoring becomes folklore - nobody knows why this alert exists or who owns that dashboard. The registry stores observability metadata alongside the datasets: monitor definitions versioned like code, threshold changes with reasons, ownership with rotations, and coverage as a first-class metric. Metadata reviews are part of data reviews: when a dataset's contract changes, its monitoring metadata is reviewed in the same change.""",
how_it_works="""Monitor definitions are stored versioned with thresholds, owners, routes, and tuning history. Coverage analyzers compare the dataset inventory against monitor definitions, reporting gaps. Threshold changes require reasons and flow through the same review as contract changes. Ownership metadata syncs with team rotations. Coverage is a reported metric per domain with targets; gaps become instrumentation work. Metadata APIs let platforms generate monitors from contracts automatically, keeping metadata and promises in sync.""",
key_points=[
 "Observability metadata: monitors, thresholds, owners, routes, tuning history.",
 "Makes monitoring governable: coverage, ownership, rationale all recorded.",
 "Monitor definitions versioned like code; threshold changes need reasons.",
 "Coverage is a first-class metric with targets per domain.",
 "Metadata reviews ride along with contract changes."],
requirements=[
 "Versioned monitor definitions with tuning history.",
 "Coverage analysis against the dataset inventory.",
 "Threshold change governance with reasons.",
 "Contract-to-monitor generation keeping promises and monitoring in sync."],
standards=[
 "ISO 8000-8 for quality measurement."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016."],
sig_lens="""The Signature reading: observability metadata is the watch's own muster roll - every sentry posted, every order written, every tuning recorded. The Signature muster is inspected with the same rigor as the watch it describes.""",
demo_data={"feeds":[
 {"name":"meta_ok","last_hours_ago":1,"sla_hours":2,"null_rate":0.01}],
 "expect_stale":[]},
),
dict(
name="Incident Timelines",
group="Pipeline Health", ladder_rank=24, ladder_tier="compounded",
description="""Incident timelines reconstruct what happened during a data incident, minute by minute: the first freshness breach at 02:14, the source outage confirmed at 02:31, consumers notified at 02:35, the fix deployed at 03:02, verification green at 03:20. Timelines assemble automatically from the event record - monitor breaches, pipeline failures, human actions, communications - into one chronological account. They serve the incident (coordinating - what has been tried?), the post-mortem (learning - where did the time go?), and the audit (proving - what did you know when?). The timeline distinguishes detection latency (breach to page), response latency (page to action), and recovery latency (action to green) - the three numbers that incident reviews optimize. Timeline templates ensure consistency: every incident gets the same structure, so reviews compare apples to apples and the organization learns across incidents instead of within them.""",
how_it_works="""The incident system ingests monitor breaches, pipeline events, human actions, and communications into per-incident timelines automatically. Responders annotate with decisions and hypotheses. Latency metrics - detection, response, recovery - compute from the timeline and trend per team and incident class. Post-mortem templates structure the review around the timeline. Timeline archives persist with the incident record; cross-incident analysis finds systemic patterns (detection always slow on weekends). Timeline completeness is reviewed - gaps mean missing instrumentation, which becomes work.""",
key_points=[
 "Timelines assemble breaches, failures, actions, communications chronologically.",
 "Serve incidents, post-mortems, and audits from one account.",
 "Three latencies optimized: detection, response, recovery.",
 "Templates keep incidents comparable; organizations learn across them.",
 "Timeline gaps reveal missing instrumentation."],
requirements=[
 "Automatic timeline assembly from event records.",
 "Latency metrics per incident class with trends.",
 "Post-mortem templates structured on timelines.",
 "Cross-incident pattern analysis."],
standards=[
 "Site Reliability Engineering incident practices."],
citations=[
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: incident timelines are the watch's battle chronicle - every minute accounted, every latency measured, every lesson filed. The Signature chronicler's accounts let the army learn across battles, not just within them.""",
demo_data={"feeds":[
 {"name":"incident_ok","last_hours_ago":1,"sla_hours":2,"null_rate":0.01}],
 "expect_stale":[]},
),
]
