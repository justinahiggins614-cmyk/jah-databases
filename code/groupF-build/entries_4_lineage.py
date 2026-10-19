#!/usr/bin/env python3
"""Authored records for the Data Lineage Registry databases (group F, part 1).
Public = real, fact-checked data-lineage knowledge (OpenLineage, column lineage,
impact analysis). Signature = expanded Signature treatment.
Property of Justin Addam Higgins (JAH)."""

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
dict(
name="What Data Lineage Is",
group="Lineage Basics", ladder_rank=1, ladder_tier="foundations",
description="""Data lineage is the record of where data came from and how it changed along the way: this dashboard number came from that warehouse table, which was loaded from that source feed, which was extracted from that operational database - with every transformation documented at each step. Lineage answers the two questions every data team asks in a crisis: upstream, what feeds this (so we can find the broken source)? Downstream, what does this feed (so we can warn the affected)? Without lineage, a broken source means hours of archaeology through pipeline code; with lineage, it means one graph query. Lineage also answers the questions auditors and regulators ask: prove this report's numbers trace to approved sources through documented transformations. The lineage registry is the system of record for these traces - capturing them automatically from pipelines, storing them as graphs, and serving them to everyone who needs to understand data's journey.""",
how_it_works="""Lineage is captured at the points where data moves or changes: extract jobs, transformation steps, load jobs, queries, and API calls. Each capture records the inputs, the outputs, the transformation (code reference, SQL text, or job ID), the actor, and the timestamp - in the OpenLineage event format. The registry assembles captures into a graph: nodes for datasets and jobs, edges for reads and writes. Upstream queries walk the graph backward from any dataset to its sources; downstream queries walk forward to its consumers. Column-level lineage refines this to field granularity. The graph stays current because capture is automatic - pipelines emit lineage events as they run - not because someone updates documentation.""",
key_points=[
 "Lineage records data's journey: sources, transformations, destinations, step by step.",
 "Upstream traces find broken sources; downstream traces find affected consumers.",
 "Auditors use lineage to prove reports trace to approved sources.",
 "Capture is automatic from running pipelines, not manual documentation.",
 "The registry stores lineage as graphs and serves upstream/downstream queries."],
requirements=[
 "Lineage capture at every data movement and transformation point.",
 "Standard event format (OpenLineage) for captures.",
 "Graph storage with upstream/downstream traversal.",
 "Automatic emission from pipelines as they run."],
standards=[
 "OpenLineage specification.",
 "W3C PROV-O for provenance modeling."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013."],
sig_lens="""The Signature reading: lineage is the registry's memory of every journey data has taken - each step witnessed, each transformation recorded. The Signature registry forgets no journey and can retrace any number to its source.""",
demo_data={"nodes":["extract","clean","report"],"edges":[["extract","clean"],["clean","report"]],
 "formula":{"inputs":{"qty":3,"price":20},"expr":"qty*price","expected":60}},
),
dict(
name="Why Lineage Matters: Trust, Debugging, Compliance",
group="Lineage Basics", ladder_rank=2, ladder_tier="foundations",
description="""Lineage earns its keep in three arenas. Trust: when an executive asks why the numbers changed, lineage shows the exact upstream change - the source redefined a field Tuesday - turning an argument into an explanation. Analysts trust data they can trace; lineage is the trace. Debugging: when a pipeline fails or produces wrong numbers, upstream traversal finds the broken or changed source in minutes instead of hours of code archaeology, and downstream traversal lists everything to re-run or warn. Compliance: regulations from financial reporting to data protection require proving where data came from, what transformed it, and who touched it - lineage is the evidence. There is a fourth arena emerging: AI governance, where models must document their training data's lineage to be deployable. Organizations that invest in lineage find it pays across all four; organizations that do not pay in incidents, audit findings, and untrusted data.""",
how_it_works="""The registry serves each arena through the same graph with different queries. Trust queries render the journey of a number as a human-readable path with transformation descriptions at each step - the explanation view. Debugging queries traverse upstream from a failure to candidate causes (recently changed sources, failed jobs) and downstream to affected consumers for notification. Compliance queries export the full trace with timestamps, actors, and transformation references as auditable evidence packages. AI governance queries trace model training datasets to their sources with consent and licensing metadata attached. Each arena's interface is tuned to its users, but all read the same captured lineage - one truth, many views.""",
key_points=[
 "Trust: lineage turns number disputes into traceable explanations.",
 "Debugging: upstream finds causes, downstream finds affected consumers.",
 "Compliance: lineage is the evidence regulators require.",
 "AI governance: models must document training-data lineage.",
 "One captured graph serves all arenas through different queries."],
requirements=[
 "Explanation views rendering data journeys for non-engineers.",
 "Upstream/downstream traversal for debugging with change recency.",
 "Evidence-package export for compliance.",
 "Training-data lineage with consent metadata for AI governance."],
standards=[
 "OpenLineage specification.",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: lineage serves trust, debugging, compliance, and AI governance from one sworn record of journeys. The Signature registry's single truth wears four faces, each honest.""",
demo_data={"nodes":["source","stage","mart"],"edges":[["source","stage"],["stage","mart"]],
 "formula":{"inputs":{"rows":1000,"bad":25},"expr":"rows-bad","expected":975}},
),
dict(
name="Source Nodes",
group="Lineage Basics", ladder_rank=3, ladder_tier="foundations",
description="""Source nodes are where lineage begins: the operational databases, files, feeds, APIs, and partner drops that originate data. Each source node in the registry carries its identity (system, dataset, access path), its owner, its trust profile (from profiling and history), its change cadence, and its contract reference if it has one. Source nodes are classified by kind - system of entry, system of record, reference feed, external partner - because the kind determines how the registry treats changes from it. The registry watches source nodes for the events that matter downstream: schema changes, delivery delays, quality collapses, and deprecations. A source node going dark is the most common root cause of downstream incidents, so source health is a first-class lineage concern, not someone else's monitoring problem. New sources join the graph through onboarding that records their metadata before their first byte flows.""",
how_it_works="""Source onboarding registers the node with identity, owner, kind, cadence, contract, and trust baseline. Change detection watches each source: schema drift detectors compare incoming schemas to the registered one, freshness monitors track delivery against cadence, quality profilers score each delivery. Detected changes publish lineage events marked as source changes, which downstream impact analysis consumes immediately. Health dashboards show every source's current status; unhealthy sources trigger the same incident process as pipeline failures. Source retirement follows deprecation: announced, drained, archived - with the node retained in the graph so historical traces still resolve.""",
key_points=[
 "Source nodes carry identity, owner, trust profile, cadence, and contract reference.",
 "Classification by kind (entry, record, reference, partner) governs change treatment.",
 "The registry watches sources for schema, delivery, quality, and deprecation events.",
 "Source outages are the top downstream-incident cause; source health is lineage's business.",
 "Retired sources stay in the graph so historical traces resolve."],
requirements=[
 "Source onboarding capturing full node metadata before first data flows.",
 "Change detection: schema drift, freshness, quality per source.",
 "Source health dashboards with incident integration.",
 "Deprecation workflow for source retirement."],
standards=[
 "OpenLineage (source dataset facets).",
 "DAMA-DMBOK data integration guidance."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: source nodes are the headwaters of every data river - named, owned, watched. The Signature registry knows every headwater and raises the alarm the moment one runs dry or turns strange.""",
demo_data={"nodes":["crm_db","orders_api"],"edges":[["crm_db","orders_api"]],
 "formula":{"inputs":{"a":10,"b":4},"expr":"a+b","expected":14}},
),
dict(
name="Transformation Steps",
group="Lineage Basics", ladder_rank=4, ladder_tier="foundations",
description="""Transformation steps are where data changes: the cleaning job that standardizes addresses, the aggregation that rolls transactions to daily totals, the join that enriches orders with customer data, the model that scores fraud. Each step in the lineage graph records its inputs, outputs, the transformation logic (code reference, SQL text, or model version), its owner, and its run history. Steps are the most valuable nodes for debugging - when numbers are wrong, the faulty step is usually a recent change away - so the registry versions step definitions and links each run to the exact code version that executed. Steps also carry their contracts: what the step promises about its outputs, so downstream consumers know what to expect. The discipline that makes step lineage work is granularity: one logical transformation per step, named clearly, instead of monolithic jobs that do twelve things opaquely.""",
how_it_works="""Pipelines declare their steps with inputs, outputs, logic references, and owners; the orchestrator emits lineage events per step run with the code version, parameters, and timing. The registry versions step definitions - logic changes create new versions, and runs link to their version. Step contracts declare output promises (schema, quality bars) which validators check per run. Debugging queries find recently changed steps upstream of a failure; impact queries find downstream consumers of a step about to change. Monolithic jobs are refactored into named steps over time, each gaining its own lineage, contract, and run history.""",
key_points=[
 "Steps record inputs, outputs, logic reference, owner, and run history.",
 "Step definitions are versioned; runs link to the exact code version.",
 "Steps carry output contracts validated per run.",
 "One logical transformation per step - monoliths get refactored.",
 "Recently changed steps upstream are the first debugging suspects."],
requirements=[
 "Step declarations with inputs, outputs, logic, owners.",
 "Per-run lineage events with code versions and parameters.",
 "Step output contracts with per-run validation.",
 "Refactoring of monolithic jobs into named steps."],
standards=[
 "OpenLineage (job and run facets).",
 "W3C PROV-O for activity modeling."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013."],
sig_lens="""The Signature reading: transformation steps are the waystations where data is remade - each with its name, its method, its sworn output. The Signature registry versions every waystation's method and can replay any run.""",
demo_data={"nodes":["raw","deduped","golden"],"edges":[["raw","deduped"],["deduped","golden"]],
 "formula":{"inputs":{"gross":1000,"refunds":150},"expr":"gross-refunds","expected":850}},
),
dict(
name="Sink Nodes and Records",
group="Lineage Basics", ladder_rank=5, ladder_tier="foundations",
description="""Sink nodes are where lineage ends: the dashboards executives read, the warehouse tables analysts query, the features models train on, the files sent to partners, the archives kept for compliance. Each sink records what it contains, who consumes it, its refresh cadence, its retention, and - critically - its upstream lineage, because a sink without lineage is a number without a story. Sinks are where lineage proves its consumer value: the dashboard's about panel shows its data journey, the model's documentation lists its training lineage, the partner file's manifest cites its sources. Sink monitoring closes the loop: freshness checks verify the sink actually refreshed, quality checks verify its contents, and consumer feedback (this number looks wrong) routes upstream through the lineage graph to the responsible step. When a sink is retired, its lineage is archived with it - the numbers it once showed must remain explainable.""",
how_it_works="""Sink registration captures contents, consumers, cadence, retention, and the upstream graph that feeds it. About-panels and documentation render the lineage automatically from the registry - no manual documentation to rot. Freshness and quality monitors watch each sink against its promises; consumer feedback buttons file lineage-routed investigations. Retirement archives the sink's data (per retention) and its lineage together, keeping historical numbers explainable. Sink dependency declarations feed the contract registry's consumer side and the impact analyzer's downstream walks.""",
key_points=[
 "Sinks: dashboards, tables, features, partner files, archives - lineage's endpoints.",
 "Every sink shows its data journey; numbers without stories are not trusted.",
 "Sink monitoring verifies refresh and contents against promises.",
 "Consumer feedback routes upstream through lineage to responsible steps.",
 "Retired sinks archive data and lineage together for lasting explainability."],
requirements=[
 "Sink registration with contents, consumers, cadence, retention.",
 "Automatic lineage rendering in about-panels and documentation.",
 "Freshness and quality monitoring per sink.",
 "Joint archival of data and lineage on retirement."],
standards=[
 "OpenLineage (output dataset facets).",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: sink nodes are where journeys end and stories get told - every dashboard, every model, every file able to show its road. The Signature registry lets no number stand without its story.""",
demo_data={"nodes":["mart","dashboard"],"edges":[["mart","dashboard"]],
 "formula":{"inputs":{"clicks":5000,"impressions":100000},"expr":"clicks/impressions","expected":0.05}},
),
dict(
name="Derivation Formulas",
group="Lineage Basics", ladder_rank=6, ladder_tier="foundations",
description="""Derivation formulas are the exact mathematics of transformation: revenue = quantity * unit_price, churn_rate = churned / total_customers, risk_score = 0.3*debt_ratio + 0.7*late_payments. Recording formulas in lineage turns opaque steps into checkable ones - anyone can verify the number by recomputing it. Formulas are captured at the precision the business needs: the expression, the input fields with their lineage, the constants and their sources (where did 0.3 come from?), the rounding and null-handling rules, and the effective dates (the formula changed in Q3). Formula changes are lineage events: when the churn definition changes, every downstream number's meaning changes, and consumers must be told. The registry versions formulas like code, because they are code - business logic wearing a spreadsheet's clothes.""",
how_it_works="""Transformation steps declare their derivation formulas with expressions, input lineage, constant provenance, rounding rules, null handling, and effective dates. The registry versions formulas and links runs to their formula version. Formula-change events propagate to downstream consumers with before/after semantics - the numbers will move and here is why. Verification tooling recomputes sample outputs from inputs using the recorded formula, flagging steps whose outputs do not match their declared math. Formula libraries collect the organization's standard calculations (how we compute churn, everywhere) so the same concept is never computed three different ways.""",
key_points=[
 "Formulas record the exact math: expressions, inputs, constants, rounding, null handling.",
 "Constants carry provenance - where did 0.3 come from?",
 "Formula changes are lineage events; downstream meanings change with them.",
 "Verification recomputes outputs from inputs to check declared math.",
 "Standard formula libraries prevent the same concept computed three ways."],
requirements=[
 "Formula declarations with full precision per transformation step.",
 "Versioning of formulas with effective dates.",
 "Change propagation to downstream consumers with semantics notes.",
 "Verification by recomputation on samples."],
standards=[
 "OpenLineage (transformation facets).",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: derivation formulas are the sworn mathematics of change - every calculation written plainly, every constant sourced, every change announced. The Signature registry lets any number be recomputed and checked by any skeptic.""",
demo_data={"nodes":["inputs","metric"],"edges":[["inputs","metric"]],
 "formula":{"inputs":{"qty":7,"price":15},"expr":"qty*price","expected":105}},
),
dict(
name="Column-Level Lineage",
group="Lineage Basics", ladder_rank=7, ladder_tier="foundations",
description="""Table-level lineage says the revenue report comes from the orders table; column-level lineage says the report's revenue column comes from orders.amount multiplied by the exchange rate from fx.rates, excluding refunded rows per orders.status. Column lineage is where debugging actually happens - nobody debugs a table, they debug a column - and where compliance actually bites: regulators ask which source columns feed a reported figure, and privacy teams ask which source columns flow into a shared dataset. Capturing it requires parsing transformation logic: SQL analyzers extract column mappings from queries, code instrumenters trace dataframe columns, and manual annotations cover the opaque steps. The registry stores column lineage as edges between qualified column identifiers, with the transformation expression on each edge. The investment is significant but so is the payoff: impact analysis becomes surgical (this source column change affects exactly these 14 downstream columns), and privacy tracing becomes possible.""",
how_it_works="""SQL parsers and dataframe instrumenters extract column-level mappings from transformation code automatically; steps that resist parsing get manual column annotations. The registry stores column edges with expressions, linking source columns through steps to sink columns. Queries answer: where did this column come from (full upstream column path), what does this column feed (downstream column fan-out), and what changed (which downstream columns does this source change touch). Privacy tracing walks column lineage from sensitive sources to find every downstream column needing protection. Coverage metrics track what share of steps have column lineage; opaque steps are refactoring targets.""",
key_points=[
 "Column lineage traces fields, not just tables - where debugging and compliance live.",
 "Captured by SQL parsing, dataframe instrumentation, and manual annotation.",
 "Edges carry transformation expressions between qualified column identifiers.",
 "Impact analysis becomes surgical: exact downstream columns per source change.",
 "Privacy tracing finds every downstream column a sensitive source touches."],
requirements=[
 "Column extraction from SQL and dataframe code.",
 "Manual annotation workflows for opaque steps.",
 "Column-edge storage with expressions.",
 "Coverage metrics driving opaque-step refactoring."],
standards=[
 "OpenLineage (column lineage facets).",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: column lineage is the registry tracing every field's ancestry to its birth - not just which table, which column, by what math. The Signature registry follows fields the way genealogists follow names: exactly.""",
demo_data={"nodes":["orders.amount","fx.rate","report.revenue"],"edges":[["orders.amount","report.revenue"],["fx.rate","report.revenue"]],
 "formula":{"inputs":{"amount":200,"rate":1.1},"expr":"amount*rate","expected":220.0}},
),
dict(
name="Table-Level Lineage",
group="Lineage Basics", ladder_rank=8, ladder_tier="foundations",
description="""Table-level lineage maps dataset to dataset: which tables feed which, through which jobs. It is coarser than column lineage but cheaper to capture and sufficient for many purposes: dependency mapping, coarse impact analysis, data estate discovery, and the first view in every debugging session. Table lineage answers the estate questions - what exists, what depends on what, what is orphaned - that column lineage is too fine to show. Capture is straightforward: every job declares or emits its input and output datasets, and the registry links them. The discipline is completeness: every job must emit lineage, including the ad-hoc queries analysts run and the scripts data scientists execute - the undocumented job is the one that breaks the trace. Table lineage is the foundation column lineage refines; organizations build table coverage first, then deepen to columns where the value justifies it.""",
how_it_works="""Jobs emit input/output dataset identifiers with each run; orchestrators and query engines emit automatically, ad-hoc tools get lineage plugins or manual declaration requirements. The registry links datasets through jobs into the table graph. Estate queries render the full dependency map; orphan detection finds datasets with no downstream consumers (candidates for retirement) and no upstream lineage (candidates for investigation). Impact analysis at table granularity runs fast and covers the estate, with column lineage consulted for precision where available. Completeness monitoring flags jobs that ran without emitting lineage, and repeat offenders get their execution blocked until instrumented.""",
key_points=[
 "Table lineage maps dataset dependencies - the estate view.",
 "Sufficient for dependency mapping, coarse impact, discovery, orphan detection.",
 "Every job must emit lineage, including ad-hoc queries and scripts.",
 "Table coverage comes first; column lineage deepens where valuable.",
 "Completeness monitoring blocks uninstrumented jobs."],
requirements=[
 "Input/output emission from every job and query engine.",
 "Lineage plugins or declarations for ad-hoc tools.",
 "Orphan detection for retirement and investigation candidates.",
 "Completeness monitoring with execution blocking for offenders."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: table lineage is the registry's map of the realm - every dataset, every dependency, no terra incognita. The Signature mapmaker permits no uncharted jobs and marks orphans for honest reckoning.""",
demo_data={"nodes":["staging","warehouse","marts"],"edges":[["staging","warehouse"],["warehouse","marts"]],
 "formula":{"inputs":{"in_rows":5000,"filtered":300},"expr":"in_rows-filtered","expected":4700}},
),
dict(
name="The OpenLineage Standard",
group="Lineage Basics", ladder_rank=9, ladder_tier="foundations",
description="""OpenLineage is the open standard for lineage metadata, a Linux Foundation project that lets every tool emit lineage in one common format. Its model is simple: jobs (the processes) have runs (executions), runs read input datasets and write output datasets, and facets attach typed metadata to each - schema facets, ownership facets, SQL facets, quality facets. Because the format is standard, a lineage graph can span tools that never heard of each other: Airflow emits runs, dbt emits column lineage, Spark emits dataset reads, and the registry assembles them into one graph. The standard's facet system keeps it extensible: vendors and teams add custom facets without breaking the core. Adopting OpenLineage means lineage capture becomes a commodity - instrument once per platform, and every pipeline on that platform emits lineage forever. The alternative is N custom integrations for N tools, each rotting at its own pace.""",
how_it_works="""Platforms integrate OpenLineage once: orchestrators emit job/run events, query engines emit dataset events, transformation tools emit column facets. Events flow to the registry's OpenLineage endpoint, which validates and assembles them into the graph. Custom facets carry organization-specific metadata (cost center, data classification) through the standard envelope. The registry also emits OpenLineage for its own operations, so meta-lineage (how the registry built the graph) is itself traceable. Version compatibility follows the spec's guarantees; the registry supports the current and previous spec versions during transitions.""",
key_points=[
 "OpenLineage: jobs, runs, input/output datasets, typed facets - one format for all tools.",
 "Cross-tool graphs: Airflow, dbt, Spark lineage assembles into one graph.",
 "Facets keep the standard extensible without breaking the core.",
 "Instrument once per platform; every pipeline emits lineage forever.",
 "The registry validates, assembles, and serves OpenLineage natively."],
requirements=[
 "OpenLineage integration per platform (orchestrator, engine, transform tool).",
 "Registry endpoint validating and assembling events.",
 "Custom facets for organization metadata.",
 "Spec version support with transition handling."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Marquez. OpenLineage: open standard for lineage metadata."],
sig_lens="""The Signature reading: OpenLineage is the common script of journeys - every tool writing its travels in one tongue the registry reads. The Signature registry is fluent in the script and keeps every traveler's tale.""",
demo_data={"nodes":["job_a","job_b"],"edges":[["job_a","job_b"]],
 "formula":{"inputs":{"events":1200,"errors":12},"expr":"events-errors","expected":1188}},
),
dict(
name="Lineage Capture Methods",
group="Lineage Basics", ladder_rank=10, ladder_tier="foundations",
description="""Lineage is captured four ways, and a complete registry uses all four. Instrumentation: platforms emit lineage automatically - orchestrators report job runs, query engines report tables read and written, Spark listeners report dataframe lineage. Parsing: SQL analyzers extract table and column mappings from query text, covering the vast estate of hand-written SQL. Inference: the registry correlates - this table's schema matches that query's output, this job always runs after that one - to propose lineage where direct evidence is missing, marked as inferred with confidence. Declaration: humans annotate what machines cannot see - the spreadsheet uploaded by hand, the partner file with no pipeline, the whiteboard SQL. Each method has a trust tier: instrumented beats parsed beats inferred beats declared-and-unverified, and the registry records the capture method on every edge so consumers know how much to trust the trace.""",
how_it_works="""The registry runs all four capture paths: platform instrumentation via OpenLineage integrations, SQL parsing over query logs and code repositories, inference jobs correlating schemas and schedules, and declaration UIs for manual annotation. Every edge carries its capture method and confidence; inferred edges below the confidence bar queue for human confirmation. Coverage dashboards show per-method capture rates per estate area; gaps become instrumentation projects. Declared edges get periodic re-verification prompts - the human who declared it confirms it is still true. Method trust tiers feed the lineage confidence scores shown on every trace.""",
key_points=[
 "Four methods: instrumentation, parsing, inference, declaration.",
 "Trust tiers: instrumented > parsed > inferred > declared-unverified.",
 "Every edge records its capture method and confidence.",
 "Inferred edges below the bar queue for human confirmation.",
 "Coverage dashboards turn gaps into instrumentation projects."],
requirements=[
 "Platform instrumentation via OpenLineage.",
 "SQL parsing over query logs and repositories.",
 "Inference with confidence thresholds and confirmation queues.",
 "Declaration UIs with re-verification prompts."],
standards=[
 "OpenLineage specification.",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: four ways of witnessing - the machine's own testimony, the parsed word, the reasoned inference, the human's sworn word - each labeled with its weight. The Signature registry trusts each as far as its nature warrants.""",
demo_data={"nodes":["etl","api","file_drop"],"edges":[["etl","api"],["file_drop","api"]],
 "formula":{"inputs":{"ok":98,"total":100},"expr":"ok/total","expected":0.98}},
),
dict(
name="Batch Lineage",
group="Lineage Basics", ladder_rank=11, ladder_tier="foundations",
description="""Batch lineage traces the scheduled world: nightly ETLs, hourly aggregations, weekly reports. Each batch run is a lineage event with its inputs (the source snapshots), outputs (the written partitions), parameters (the date window), and status. Batch lineage's superpower is reproducibility: given the run's inputs and code version, the outputs can be recomputed - which is exactly what backfills do. The registry links runs in sequence, so the lineage of Tuesday's report includes Monday's run that fed it, forming the run chain auditors love. Late and failed batches are lineage events too: a failed run explains the missing partition downstream, and the retry's lineage shows the recovery. Partition-level lineage refines batch traces: which input partitions fed which output partitions, so a corrupted source partition's blast radius is exactly known.""",
how_it_works="""Orchestrators emit per-run lineage events: job, run ID, inputs with partition identifiers, outputs with partitions, parameters, code version, status, timing. The registry chains runs by dependency, building the run-level graph alongside the dataset-level graph. Partition lineage maps input partitions to output partitions within each run. Failed runs emit failure events with error details; retries link to the failed run they replace. Backfill runs are marked as such with their recomputation scope. As-of queries can select the run chain effective on a date, reproducing exactly what the data looked like then.""",
key_points=[
 "Batch runs are lineage events: inputs, outputs, parameters, code version, status.",
 "Run chains link batches in sequence - the auditor's favorite view.",
 "Failed runs and retries are lineage events explaining gaps and recoveries.",
 "Partition lineage gives exact blast radius for corrupted source partitions.",
 "Reproducibility: inputs plus code version can recompute any output."],
requirements=[
 "Per-run lineage emission from orchestrators.",
 "Partition-level input/output mapping.",
 "Failure and retry events with error details.",
 "Run-chain as-of queries."],
standards=[
 "OpenLineage (run facets)."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: batch lineage is the registry's chronicle of scheduled labors - each run recorded with its materials, its methods, its outcome. The Signature chronicle makes every night's work reproducible and every failure explainable.""",
demo_data={"nodes":["nightly_extract","daily_agg"],"edges":[["nightly_extract","daily_agg"]],
 "formula":{"inputs":{"txns":86400,"dupes":36},"expr":"txns-dupes","expected":86364}},
),
dict(
name="Streaming Lineage",
group="Lineage Basics", ladder_rank=12, ladder_tier="foundations",
description="""Streaming lineage traces the continuous world: events flowing through topics, windows aggregating them, sinks serving them. Unlike batch lineage's discrete runs, streaming lineage deals in flows - the lineage of a continuously updated aggregate is the topology plus the window definitions plus the watermark policy. The registry captures the streaming topology (sources, processors, sinks, and their connections), the windowing (tumbling, sliding, session - with sizes and lateness handling), and the state (what the processor remembers between events). Event-time semantics matter: a late event reprocessed changes history, and the lineage must show the correction. Streaming lineage's hardest problem is the unbounded past - the graph cannot store every event - so the registry stores topology, window specs, and checkpoints, plus sampled event traces for debugging. When a streaming number looks wrong, the lineage shows the topology, the current watermarks, and the recent checkpoint - usually enough to find the stuck partition or the poisoned key.""",
how_it_works="""Stream processors emit topology lineage on deployment and checkpoint lineage on state commits: topology version, window specs, watermark positions, partition assignments. Sampled event traces capture full per-event lineage for a fraction of events, retained briefly for debugging. Late-event reprocessing emits correction events linked to the original processing. Watermark monitoring feeds the freshness side of lineage - a stuck watermark explains stale aggregates. Topology changes version like batch code; the registry keeps topology history so past behavior is explainable. Debugging queries show topology, watermarks, checkpoints, and recent samples together.""",
key_points=[
 "Streaming lineage captures topology, windows, watermarks, and state - not discrete runs.",
 "Event-time semantics: late events and corrections are lineage events.",
 "The registry stores topology plus checkpoints plus sampled traces, not every event.",
 "Watermark positions explain stale aggregates.",
 "Topology versions like code; history keeps past behavior explainable."],
requirements=[
 "Topology lineage on deployment with window and watermark specs.",
 "Checkpoint lineage on state commits.",
 "Sampled event traces for debugging.",
 "Watermark monitoring integrated with lineage views."],
standards=[
 "OpenLineage (streaming facets)."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Akidau T et al. Streaming Systems. O'Reilly, 2018."],
sig_lens="""The Signature reading: streaming lineage is the registry charting rivers, not ponds - the channels, the weirs of windows, the watermarks of time. The Signature chart shows the river's course and can say, for any moment, how far the waters had come.""",
demo_data={"nodes":["events","windowed","sink"],"edges":[["events","windowed"],["windowed","sink"]],
 "formula":{"inputs":{"late":5,"ontime":995},"expr":"ontime/(ontime+late)","expected":0.995}},
),
]
