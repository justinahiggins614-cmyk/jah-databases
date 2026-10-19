#!/usr/bin/env python3
"""Entries for the Database Cost Accounting databases (JAH Databases
governance track, group F, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); ID prefixes JAH-DCA- (public) and
JAH-DCAS- (signature) verified free: zero exact or substring hits in
manifest id_prefix values and zero hits in all shard record IDs of
jah-databases-data-1. All 68 record titles checked against the whole
system (exact dedupe index + live shard title corpus of 1,143,457 titles)
BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  database-cost-accounting           - The Database Cost Accounting Database
      (public-harvest: real, fact-checked cost knowledge - storage, compute,
      bandwidth, indexing, generation, retrieval; allocation; ledgers;
      tiering; batch costing; SLA tradeoffs; cache; compression; backup/DR;
      transfer; anomaly detection; TCO; budgeting; chargeback; quality cost;
      governance overhead; marginal cost; pipeline comparison; carbon;
      audits; variance; playbooks; dashboards)
  database-cost-accounting-signature - The Database Cost Accounting Signature
      Database (the Signature Cost Doctrine; src signature, titles suffixed
      " (Signature Edition)", never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_database_cost_accounting.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - the Signature Cost Doctrine: every byte "
            "priced, every query accounted, every dollar attributed; waste is "
            "a finding, not a rounding error. Clearly labeled Signature-made, "
            "never presented as an authentic public record. Property of "
            "Justin Addam Higgins (JAH).")

ENTRIES = [
# ---------------- Foundations (1-10) ----------------
{
 "name": "Cost Accounting Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "demo_key": "k_facts",
 "demo_data": {"dimensions": 6, "allocation_models": 3, "currency": "USD", "fiscal": "monthly",
               "checks": [["dimensions", "==", 6], ["allocation_models", "==", 3]]},
 "description": ("The cost accounting overview defines the six cost dimensions every "
   "database is measured on: storage, compute, bandwidth, indexing, generation, and "
   "retrieval - plus the three allocation models (equal split, usage-weighted, and "
   "headcount) that assign shared costs to owners. Cost accounting turns 'the "
   "databases cost something' into a ledger: each database with its monthly dollar "
   "figure, each dollar attributable to a dimension and an owner. Without it, "
   "costs are discovered at invoice time, when the only available responses are "
   "surprise and argument. With it, every team sees its burn rate daily and manages "
   "it like any other budget."),
 "how_it_works": ("Each database gets a monthly cost record summing its six "
   "dimensions: storage (GB x $/GB-month by tier), compute (vCPU-hours x rate), "
   "bandwidth (egress GB x $/GB), indexing (index storage + rebuild compute), "
   "generation (records x $/record), and retrieval (queries x $/query by SLA "
   "tier). Shared costs - the control plane, the monitoring, the support contract "
   "- are allocated by one of the three models, chosen per cost pool and "
   "documented. The fiscal period is monthly, in USD, with all figures "
   "reconciled to the provider invoice before publication. Currency conversions "
   "use the month's average rate, recorded. The overview also sets the materiality "
   "threshold: line items under one dollar a month are grouped, not itemized, "
   "because accounting has its own cost."),
 "key_points": [
   "Six dimensions: storage, compute, bandwidth, indexing, generation, retrieval.",
   "Three allocation models: equal, usage-weighted, headcount - chosen per pool.",
   "Monthly fiscal period in USD, reconciled to the provider invoice.",
   "Every database with its monthly figure; every dollar attributable.",
   "Materiality threshold: sub-dollar lines grouped, not itemized.",
   "Costs managed daily like any budget - never discovered at invoice time.",
 ],
 "requirements": [
   "Cost record per database per month.",
   "All six dimensions measured.",
   "Allocation model documented per shared pool.",
   "Invoice reconciliation before publication.",
 ],
 "standards": [
   "USD monthly; conversions at the month's average rate, recorded.",
   "Dimensions defined identically across databases.",
   "Allocation choices reviewed annually.",
   "Published to owners within five business days of month-end.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (cost allocation practice).",
 ],
 "sig_lens": ("The Signature Cost Doctrine opens with a scale that weighs money: "
   "the doctrine holds that an unmeasured cost is an unmanaged cost, and an "
   "unmanaged cost grows. The Signature edition requires the ledger public "
   "within the organization - sunlight is the cheapest cost control ever "
   "invented."),
},
{
 "name": "Storage Cost Model",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "demo_key": "k_storage",
 "demo_data": {"gb": 420, "rate": 0.023, "tier": "standard"},
 "description": ("The storage cost model prices disk: four hundred twenty gigabytes "
   "at $0.023 per GB-month is $9.66 a month for standard tier. Storage is the "
   "most visible database cost and the easiest to model - capacity times rate - "
   "but the model must include what naive counts miss: replication multipliers "
   "(three copies means three times the bytes), index storage (often 20-40% on "
   "top of data), snapshot retention, and the tier mix. The record prices the "
   "example database's 420 GB honestly: data plus indexes plus one snapshot "
   "generation, at the standard tier rate, with the replication factor stated."),
 "how_it_works": ("Cost = billable GB x $/GB-month for the tier. The 420 GB "
   "breaks down as 300 GB data, 90 GB indexes (30% overhead), and 30 GB in "
   "retained snapshots; at $0.023 the monthly charge is $9.66. Replication is "
   "billed by the provider in this model (the 420 GB is post-replication); "
   "where the provider bills pre-replication bytes, the model multiplies by the "
   "replication factor explicitly. Tier changes reprice: moving 30% of the data "
   "to infrequent-access at $0.0125 is modeled in the tiering record. Growth is "
   "projected from the capacity forecasting database - storage cost is where "
   "growth forecasts turn into budget lines. The model is re-rated whenever the "
   "provider changes prices, with the old and new rates both recorded."),
 "key_points": [
   "420 GB x $0.023 = $9.66/month standard tier.",
   "Includes indexes (30% overhead) and snapshot retention - not just data.",
   "Replication factor explicit where the provider bills pre-replication.",
   "Growth projections feed directly into budget lines.",
   "Re-rated on provider price changes, old and new rates recorded.",
   "Simplest model in the system - and the foundation for the rest.",
 ],
 "requirements": [
   "Billable GB broken into data, indexes, snapshots.",
   "Tier and rate documented with effective date.",
   "Replication treatment stated.",
   "Growth projection linked.",
 ],
 "standards": [
   "Provider's billing definition of 'GB' used (post- vs pre-replication).",
   "Rates from the current price list, not from memory.",
   "Monthly remeasurement, not estimates carried forward.",
   "Price changes recorded with old/new rates.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (storage cost modeling).",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats storage as rented land: the "
   "doctrine requires every gigabyte to justify its tenancy monthly. The "
   "Signature edition prices the indexes and snapshots too - a landlord who "
   "forgets the outbuildings is not managing the estate, they are admiring "
   "it."),
},
{
 "name": "Compute Cost Model",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "demo_key": "k_compute",
 "demo_data": {"vcpu_h": 1850, "rate": 0.0416, "commit_discount": 0.3},
 "description": ("The compute cost model prices processing: one thousand eight "
   "hundred fifty vCPU-hours at $0.0416 is $76.96 on demand, or $53.87 with the "
   "thirty percent commitment discount. Compute is the volatile dimension - "
   "ingestion spikes, query storms, and rebuild jobs make it swing month to "
   "month. The model separates baseline compute (the always-on serving "
   "capacity, commitment-discounted) from burst compute (spikes, on-demand), "
   "because they price differently and are managed differently. The example's "
   "1,850 hours split 1,200 baseline and 650 burst: 1200 x $0.0416 x 0.7 = "
   "$34.94 plus 650 x $0.0416 = $27.04, for $61.98 - the blended reality "
   "between the two headline numbers."),
 "how_it_works": ("Cost = vCPU-hours x rate, with the rate depending on purchase "
   "model. The record tracks hours by workload class: serving, ingestion, "
   "indexing, generation, and analytics - because 'compute' as one number "
   "hides which workload to optimize. Commitment discounts (30% for one-year "
   "commitments in the example) apply to the baseline portion; burst pays "
   "on-demand. The blended example: $34.94 committed baseline + $27.04 "
   "on-demand burst = $61.98. Utilization is reported alongside cost: 1,850 "
   "hours against 2,200 provisioned is 84% utilization - the gap is the "
   "overprovisioning cost, named and shamed. Spot/preemptible pricing is "
   "modeled where workloads tolerate interruption, with the interruption rate "
   "tracked - cheap compute that never finishes is not cheap."),
 "key_points": [
   "1,850 vCPU-h x $0.0416 = $76.96 on-demand; $53.87 with 30% commitment.",
   "Blended reality: $34.94 committed baseline + $27.04 burst = $61.98.",
   "Tracked by workload class: serving, ingestion, indexing, generation, analytics.",
   "Utilization 84% (1,850 of 2,200 provisioned) - the gap is named.",
   "Spot pricing modeled where interruption is tolerable, with interruption rates.",
   "Compute is the volatile dimension - managed monthly, not annually.",
 ],
 "requirements": [
   "Hours tracked by workload class.",
   "Purchase model (commitment vs on-demand) per portion.",
   "Utilization reported with cost.",
   "Spot usage with interruption rates where used.",
 ],
 "standards": [
   "Provider price list rates, current.",
   "Commitment coverage reviewed quarterly - over-commitment wastes too.",
   "Utilization below 60% triggers rightsizing review.",
   "Burst causes analyzed, not just paid.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (commitment management).",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats compute as hired labor: the "
   "doctrine requires knowing what each crew (workload class) cost and what "
   "they produced. The Signature edition separates the retainers (committed "
   "baseline) from the day laborers (burst) - and it counts the idle hands "
   "in the 16% gap as carefully as the working ones."),
},
{
 "name": "Bandwidth and Egress Cost Model",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "demo_key": "k_egress",
 "demo_data": {"tb": 1.2, "rate_per_tb": 90, "ingress_free": True},
 "description": ("The bandwidth cost model prices data movement: 1.2 terabytes "
   "of egress at $90 per TB is $108 a month - while ingress is free. Egress is "
   "the classic surprise bill: data leaves the cloud cheaply in drips and "
   "expensively in floods, and the meter runs on every download, replication "
   "stream, and cross-region copy. The model counts egress by destination "
   "class - same-region (often free), cross-region (metered), internet "
   "(metered highest) - because the same terabyte costs differently by route. "
   "The example's 1.2 TB is internet egress: user downloads and API responses. "
   "Ingress free means ingestion is cheap to receive and expensive to serve - "
   "the asymmetry shapes architecture."),
 "how_it_works": ("Cost = egress TB x $/TB by destination class. The record "
   "meters: internet egress (1.2 TB x $90 = $108), cross-region replication "
   "(metered separately, usually lower), and same-region traffic (free, but "
   "tracked for capacity planning). The 1.2 TB breaks into 0.7 TB user "
   "downloads, 0.4 TB API responses, 0.1 TB administrative. Optimization levers "
   "are recorded with their savings: CDN caching for downloads (cuts internet "
   "egress up to 80%), response compression, and regional placement of hot "
   "data near its consumers. The model also prices the alternative nobody "
   "wants to consider: at what egress volume does a different architecture "
   "(dedicated interconnect, multi-cloud) beat the meter - computed, not "
   "guessed, at each review."),
 "key_points": [
   "1.2 TB egress x $90/TB = $108/month; ingress free.",
   "Metered by destination: internet highest, cross-region middle, same-region free.",
   "Breakdown: 0.7 TB downloads, 0.4 TB API, 0.1 TB admin.",
   "Levers: CDN caching (up to 80% cut), compression, regional placement.",
   "Asymmetry (free in, metered out) shapes architecture deliberately.",
   "Alternative-architecture breakeven computed at each review.",
 ],
 "requirements": [
   "Egress metered by destination class.",
   "Volume breakdown by use.",
   "Optimization levers with measured savings.",
   "Breakeven analysis for architectural alternatives.",
 ],
 "standards": [
   "Provider's egress price list, current.",
   "No unmetered cross-region replication - meter everything.",
   "CDN cache hit rates tracked with the savings.",
   "Egress anomalies alerted (spikes mean leaks or attacks).",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (data transfer costs).",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats egress as the toll road: the "
   "doctrine requires knowing every toll booth (destination class) and what "
   "each trip cost. The Signature edition is suspicious of free ingress - "
   "'free to enter, metered to leave' is the oldest pricing trap in the "
   "business, and the doctrine prices the exit before designing the entrance."),
},
{
 "name": "Indexing Cost Model",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "demo_key": "k_index",
 "demo_data": {"index_gb": 8.4, "rate": 0.023, "rebuilds_year": 3, "rebuild_cost": 12},
 "description": ("The indexing cost model prices findability: 8.4 GB of index "
   "storage at $0.023 is $0.19 a month, plus three rebuilds a year at $12 each "
   "is $36 a year - total about $38.28 annually. Indexes are the quiet cost: "
   "every index speeds reads and taxes writes, storage, and rebuild compute. "
   "The model prices both the standing cost (index bytes on disk, billed like "
   "data) and the event cost (rebuilds after bulk loads, rebalances, schema "
   "changes). The example's 8.4 GB serves 96,796 records - about 91 KB per "
   "thousand records - and the three annual rebuilds follow the three bulk "
   "ingestion windows. Unused indexes are the purest waste in the system: "
   "paying for speed nobody uses."),
 "how_it_works": ("Standing cost = index GB x $/GB-month: 8.4 x $0.023 = $0.19. "
   "Event cost = rebuilds x $/rebuild: 3 x $12 = $36/year, where each rebuild's "
   "$12 is its compute (42 minutes of indexing workers) plus the temporary "
   "storage doubling during the rebuild. The record lists every index with its "
   "size, its query usage (reads served per month), and its cost per thousand "
   "reads - the efficiency metric that kills unused indexes. An index serving "
   "zero reads in 90 days is flagged for removal; removal requires a "
   "two-week notice to query owners, because someone always remembers the "
   "index fondly after it is gone. New index proposals include a cost estimate "
   "and a usage forecast - findability is budgeted, not free."),
 "key_points": [
   "8.4 GB x $0.023 = $0.19/mo standing + 3 x $12 rebuilds = ~$38.28/year.",
   "~91 KB index per thousand records.",
   "Every index listed with size, reads served, cost per thousand reads.",
   "Zero reads in 90 days: flagged for removal with two-week notice.",
   "New indexes need cost estimates and usage forecasts.",
   "Unused indexes are the purest waste: paying for speed nobody uses.",
 ],
 "requirements": [
   "Index inventory with sizes and usage.",
   "Rebuild cost accounting per event.",
   "Removal process for unused indexes.",
   "New-index cost estimates.",
 ],
 "standards": [
   "Cost per thousand reads computed for every index.",
   "90-day zero-use flag rule enforced.",
   "Rebuilds scheduled with bulk loads, not ad hoc.",
   "Temporary rebuild storage included in event cost.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework.",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats indexes as hired guides: the "
   "doctrine pays them gladly while they guide (serve reads) and dismisses "
   "them the quarter they stop. The Signature edition requires the cost per "
   "thousand reads on every guide's contract - a guide nobody follows is not "
   "a guide, they are a pensioner."),
},
{
 "name": "Generation Cost Model",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "demo_key": "k_gen",
 "demo_data": {"records": 11476, "per_record": 0.004, "runs_month": 30},
 "description": ("The generation cost model prices creation: 11,476 records at "
   "$0.004 each is $45.90 per drip run, thirty runs a month is $1,377. "
   "Generation - the boundless builders, the harvesters, the synthesis jobs - "
   "is the factory floor of the database network, and its cost is the unit "
   "economics of growth. The model prices per record by pipeline: compute for "
   "the generator, model-inference cost where AI is used, validation compute, "
   "and the storage of the new records. The $0.004 blends $0.0028 compute, "
   "$0.0009 inference, and $0.0003 validation. Failed generations are priced "
   "too - the 2% that fail validation still consumed their compute, and the "
   "record says so."),
 "how_it_works": ("Cost per record = compute + inference + validation + "
   "storage-ingest, measured per pipeline over a trailing 30 days: $0.004 in "
   "the example. Monthly generation cost = records x per-record x runs: "
   "11,476 x $0.004 x 30 = $1,377. The record tracks the failure rate (2%) "
   "and its cost separately - $27.54 a month spent on records that never "
   "shipped - because failure cost is the optimization target. Scaling math "
   "is explicit: doubling records doubles cost linearly until the pipeline's "
   "fixed costs amortize, then the per-record cost steps down at capacity "
   "breakpoints (documented). Generation scheduling matters: off-peak compute "
   "is 40% cheaper, so batch generation runs at night and the model prices "
   "the peak/off-peak split."),
 "key_points": [
   "11,476 records x $0.004 = $45.90/run; 30 runs/month = $1,377.",
   "$0.004 blends $0.0028 compute + $0.0009 inference + $0.0003 validation.",
   "2% failure rate priced separately: $27.54/month on unshipped records.",
   "Scaling math explicit: linear until fixed costs amortize, then step-downs.",
   "Off-peak compute 40% cheaper - batch generation runs at night.",
   "Per-record cost is the unit economics of growth.",
 ],
 "requirements": [
   "Per-pipeline unit costs measured over trailing 30 days.",
   "Failure rate and failure cost tracked.",
   "Peak/off-peak split recorded.",
   "Capacity breakpoints documented.",
 ],
 "standards": [
   "Unit costs remeasured monthly, not carried forward.",
   "Failed generations never hidden in the average.",
   "Scheduling optimized for off-peak pricing.",
   "Pipeline changes re-baseline the unit cost.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (unit economics).",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats generation as the mint: the "
   "doctrine requires knowing the cost of striking each coin, including the "
   "misstrikes. The Signature edition prices the 2% failures openly - a mint "
   "that hides its scrap is cooking its books, and the doctrine audits the "
   "scrap pile first."),
},
{
 "name": "Retrieval Cost Model",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "demo_key": "k_retrieval",
 "demo_data": {"queries": 2400000, "per_1k": 0.004, "tiers": {"standard": 0.7, "premium": 0.3}, "premium_mult": 5},
 "description": ("The retrieval cost model prices answers: 2.4 million queries "
   "at $0.004 per thousand is $9.60 a month on the standard tier - with thirty "
   "percent of queries on the premium tier at five times the price, the real "
   "bill is higher. Retrieval is where users meet costs: every search, every "
   "record open, every AI answer runs the meter. The model prices by tier "
   "because not all queries cost the same - a cached index lookup is nearly "
   "free, a full-text sweep with AI summarization is not. The example: 1.68M "
   "standard queries at $0.004/1k = $6.72, plus 720K premium at $0.02/1k = "
   "$14.40, total $21.12 - the tier mix more than doubles the naive estimate."),
 "how_it_works": ("Cost = sum over tiers of (queries x $/query). The record "
   "classifies queries into tiers by resource profile: standard (index "
   "lookup, cached), premium (full scan, AI-augmented), and bulk (exports, "
   "priced separately). The tier mix is measured, not assumed - the example's "
   "70/30 split came from a month of metering. Cost per query trends are "
   "tracked because query patterns drift: a new feature that doubles premium "
   "share doubles the bill without changing total queries. The model also "
   "prices the avoided cost: caching (see the compounded record) absorbs "
   "queries before they reach the meter, and the savings are credited to the "
   "cache's account. Query budgets per team make the cost visible where the "
   "queries originate."),
 "key_points": [
   "2.4M queries: naive $9.60; with 70/30 tier mix at 5x premium = $21.12.",
   "Tiers by resource profile: standard (lookup), premium (scan+AI), bulk (export).",
   "Tier mix measured monthly - pattern drift changes the bill silently.",
   "Cache-absorbed queries credited as avoided cost.",
   "Query budgets per team put cost where queries originate.",
   "The tier mix matters more than the total query count.",
 ],
 "requirements": [
   "Query classification into tiers.",
   "Measured tier mix, updated monthly.",
   "Per-tier unit costs.",
   "Team query budgets.",
 ],
 "standards": [
   "Metered queries, not estimated.",
   "Tier definitions stable quarter to quarter.",
   "Avoided-cost accounting for caches.",
   "Budget alerts at 80% and 100%.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework.",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats each query as a question with "
   "a price tag: the doctrine requires the tag visible before the question "
   "is asked, not after the invoice arrives. The Signature edition insists "
   "the premium tier earn its 5x - a query that costs five times more must "
   "answer five times better, or it gets demoted."),
},
{
 "name": "Fixed vs Variable Costs",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "demo_key": "k_fixedvar",
 "demo_data": {"fixed": 1200, "variable_per_record": 0.0031, "records": 96796},
 "description": ("The fixed vs variable analysis separates what does not change "
   "from what does: $1,200 fixed plus $0.0031 per record times 96,796 records "
   "($300.07) totals $1,500.07 a month. Fixed costs - the control plane, base "
   "monitoring, support contracts, reserved capacity - are paid whether the "
   "database holds one record or one million. Variable costs - storage per GB, "
   "queries per thousand, generation per record - scale with use. The split "
   "matters because it determines the marginal cost of growth (variable only) "
   "and the pain of shrinkage (fixed costs do not shrink). A database at "
   "10% of its fixed-cost capacity is expensive per record; at 90%, it is "
   "efficient - same dollars, different story."),
 "how_it_works": ("Each cost line is classified fixed or variable with its "
   "driver: fixed lines list their contract terms and renewal dates; variable "
   "lines list their unit and rate. The example: $1,200 fixed (control plane "
   "$600, monitoring $350, support $250) + 96,796 x $0.0031 ($300.07 variable: "
   "storage, queries, generation) = $1,500.07. The breakeven utilization is "
   "computed: fixed costs amortize efficiently above 70% of provisioned "
   "capacity. Step-fixed costs are flagged - the support tier that jumps at "
   "100K records, the license tier at 1M - because they look fixed until "
   "growth steps on them. The analysis is redone when contracts renew or "
   "architecture changes; a reclassification (variable to fixed via "
   "commitment) is recorded as a decision with its rationale."),
 "key_points": [
   "$1,200 fixed + 96,796 x $0.0031 ($300.07) = $1,500.07/month.",
   "Fixed: control plane, monitoring, support, reserved capacity.",
   "Variable: storage, queries, generation - the marginal cost of growth.",
   "Step-fixed costs flagged: support tiers that jump at 100K, licenses at 1M.",
   "Breakeven utilization 70% - below it, per-record cost climbs.",
   "Reclassifications recorded as decisions with rationale.",
 ],
 "requirements": [
   "Every cost line classified with its driver.",
   "Contract terms and renewal dates for fixed lines.",
   "Step-fixed thresholds documented.",
   "Breakeven utilization computed.",
 ],
 "standards": [
   "Classification reviewed at contract renewal.",
   "Step costs never mislabeled as purely fixed.",
   "Marginal-cost decisions use variable only.",
   "Shutdown decisions consider fixed-cost stickiness.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (cost categorization).",
 ],
 "sig_lens": ("The Signature Cost Doctrine separates the rent from the groceries: "
   "the doctrine requires knowing which dollars stay when the database "
   "shrinks, because fixed costs are the ballast that sinks shrinking ships. "
   "The Signature edition names the step-fixed traps explicitly - the "
   "landmines are mapped, not discovered by stepping on them."),
},
{
 "name": "Cost Allocation Principles",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "demo_key": "k_facts",
 "demo_data": {"principles": 5, "models": 3, "disputes_year": 2,
               "checks": [["principles", "==", 5], ["models", "==", 3]]},
 "description": ("The cost allocation principles are the five rules for splitting "
   "shared bills fairly: causality (costs follow the cause), benefit (costs "
   "follow the benefit), fairness (no team pays for another's choices), "
   "simplicity (the model must be explainable in one minute), and stability "
   "(allocations do not whipsaw month to month). Three models implement them: "
   "equal split, usage-weighted, and headcount. Two allocation disputes last "
   "year - both resolved by applying the principles in order, which is why "
   "the principles outrank the models. An allocation nobody understands is "
   "not an allocation; it is a tax, and taxes breed resentment while "
   "allocations breed accountability."),
 "how_it_works": ("Each shared cost pool gets an allocation model chosen by the "
   "principles: the control plane (benefits all equally) splits equal; "
   "compute (caused by usage) weights by vCPU-hours; support (benefits teams "
   "by headcount) splits by engineers. The choice and its principle-citation "
   "are recorded per pool - 'compute: usage-weighted per causality.' "
   "Disputes follow a process: the disputing team states which principle the "
   "current model violates, finance and engineering review, and the decision "
   "cites principles. Last year's two disputes: one team proved its batch "
   "jobs ran off-peak (causality - won a time-weighted adjustment); one "
   "argued equal split was unfair for a pool only three teams used (benefit - "
   "won a usage model). Models are re-examined annually; stability means "
   "changes are phased, not sprung."),
 "key_points": [
   "5 principles: causality, benefit, fairness, simplicity, stability.",
   "3 models: equal, usage-weighted, headcount - chosen per pool by principle.",
   "Principles outrank models; 2 disputes last year resolved by principle order.",
   "Each pool's choice recorded with its principle citation.",
   "An allocation nobody understands is a tax, not an allocation.",
   "Changes phased annually - stability is a principle too.",
 ],
 "requirements": [
   "Model choice per pool with principle citation.",
   "Dispute process with principle-ordered resolution.",
   "Annual re-examination.",
   "Explainability test: one-minute explanation.",
 ],
 "standards": [
   "No allocation without a stated principle.",
   "Dispute decisions published with reasoning.",
   "Model changes phased over a quarter minimum.",
   "Simplicity enforced: models a team cannot explain are rejected.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (allocation principles).",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats allocation as taxation with "
   "representation: the doctrine requires the taxed to understand the tax. "
   "The Signature edition demands the one-minute explanation test - a model "
   "that needs an hour to explain is not sophisticated, it is obscure, and "
   "obscure taxes are where accountability goes to die."),
},
{
 "name": "Per-Record Cost Unit",
 "group": "Foundations", "ladder_rank": 10, "ladder_tier": "foundations",
 "demo_key": "k_perrecord",
 "demo_data": {"monthly": 1500.07, "records": 96796},
 "description": ("The per-record cost unit distills the whole ledger to one "
   "number: $1,500.07 a month across 96,796 records is $0.0155 per record per "
   "month - about 1.55 cents. This is the figure that makes costs discussable: "
   "'this database costs 1.55 cents per record monthly' fits in a sentence, "
   "while the six-dimension ledger does not. It enables the comparisons that "
   "drive decisions: database A at 1.55 cents vs database B at 4.2 cents "
   "prompts the right question ('why?'), and it prices growth directly - one "
   "million new records at this unit is $15,500 a month. The unit is honest "
   "about its limits: it averages fixed costs across records, so it overstates "
   "marginal cost and understates the cost of tiny databases."),
 "how_it_works": ("Unit = total monthly cost / record count: 1500.07 / 96796 = "
   "$0.01550. The record publishes the unit with its components - fixed "
   "portion ($1,200/96,796 = $0.0124) and variable portion ($0.0031) - so "
   "readers see the structure, not just the average. Units are computed per "
   "database monthly and trended: a rising unit with flat records means "
   "fixed-cost bloat or rate increases; a falling unit with growing records "
   "means scale economies working. Cross-database comparison uses the unit "
   "with context - record size, query intensity, generation rate - because a "
   "video database and a text database should not share a unit benchmark. "
   "The unit feeds the marginal-cost record (variable portion only) and the "
   "TCO record (unit x months x growth)."),
 "key_points": [
   "$1,500.07 / 96,796 records = $0.0155/record/month (1.55 cents).",
   "Published with components: $0.0124 fixed + $0.0031 variable.",
   "Makes costs discussable in one sentence; prices growth directly.",
   "Trended monthly: rising unit at flat records signals bloat.",
   "Comparisons need context: record size, query intensity, generation rate.",
   "Honest limits: averages fixed costs; overstates marginal, understates tiny DBs.",
 ],
 "requirements": [
   "Monthly unit computation per database.",
   "Component breakdown (fixed vs variable portion).",
   "Trend reporting.",
   "Context metadata for comparisons.",
 ],
 "standards": [
   "Units from reconciled costs, not estimates.",
   "Component split always published with the unit.",
   "No cross-database ranking without context.",
   "Marginal decisions use the variable portion, not the full unit.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (unit economics).",
 ],
 "sig_lens": ("The Signature Cost Doctrine mints the per-record unit as its "
   "coin: the doctrine requires every database to know its price per citizen. "
   "The Signature edition stamps the coin with its two metals - fixed and "
   "variable - because a coin that hides its composition is debased currency, "
   "and debased numbers buy bad decisions."),
},
# ---------------- Compounded (11-21) ----------------
{
 "name": "Per-Database Cost Ledger",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "demo_key": "k_ledger",
 "demo_data": {"databases": {"specs": 1500.07, "patents": 980.40, "wiki": 640.22, "dict": 410.55, "calc": 205.30}},
 "description": ("The per-database cost ledger is the monthly statement for each "
   "database: specs $1,500.07, patents $980.40, wiki $640.22, dictionary $410.55, "
   "calculator $205.30 - each broken into the six dimensions, each reconciled to "
   "the invoice. The ledger is the document owners actually read: one page per "
   "database, this month vs last month, with variances explained. It is produced "
   "within five business days of month-end, because a ledger that arrives late "
   "is history, not management. The five example databases sum to $3,736.54 - "
   "and the ledger proves it sums, because a ledger that does not foot is not "
   "a ledger."),
 "how_it_works": ("Each ledger page shows: the six dimension costs, the "
   "allocated shared costs with the model cited, the total, the prior month "
   "for comparison, and variance explanations for lines moving more than 10%. "
   "The example's $3,736.54 foots across the five databases and ties to the "
   "provider invoice within the $1 rounding tolerance - the reconciliation "
   "statement is attached. Owners acknowledge their ledger monthly; "
   "unacknowledged ledgers escalate after ten days, because unowned costs are "
   "unmanaged costs. The ledger feeds the dashboard (see the advanced record) "
   "and the chargeback process: the numbers here are the numbers teams are "
   "billed on, so they must be right, explainable, and on time."),
 "key_points": [
   "Monthly one-page statement per database: 6 dimensions, allocations, totals.",
   "Example: 5 databases foot to $3,736.54, tied to the invoice.",
   "Produced within 5 business days of month-end.",
   "Variances over 10% explained in plain language.",
   "Owners acknowledge monthly; unacknowledged escalates after 10 days.",
   "These are the chargeback numbers - right, explainable, on time.",
 ],
 "requirements": [
   "Ledger page per database per month.",
   "Invoice reconciliation with tolerance statement.",
   "Variance explanations over 10%.",
   "Owner acknowledgment tracking.",
 ],
 "standards": [
   "Ledgers foot: totals tie to the invoice.",
   "Published within 5 business days.",
   "Plain-language variance notes.",
   "Acknowledgment enforced by escalation.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (reporting).",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats the ledger as the monthly "
   "account rendered to each steward: the doctrine requires it prompt, "
   "footed, and intelligible. The Signature edition enforces the "
   "acknowledgment - a steward who will not sign for their costs has "
   "resigned the stewardship, whether they said so or not."),
},
{
 "name": "Shared-Cost Allocation Models",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "demo_key": "k_alloc",
 "demo_data": {"pool": 9600, "weights": [50, 30, 20], "teams": ["platform", "data", "apps"]},
 "description": ("The shared-cost allocation models split the bills nobody owns "
   "alone: a $9,600 control-plane pool divided 50/30/20 by usage weights gives "
   "$4,800 to platform, $2,880 to data, $1,920 to apps. Shared costs - the "
   "control plane, monitoring, support contracts, shared tooling - benefit "
   "everyone and are caused by no one in particular, which is exactly why "
   "they need models instead of arguments. The record implements the three "
   "models from the principles record: equal split (for truly shared goods), "
   "usage-weighted (for caused costs), and headcount (for people-proportional "
   "goods). Each pool's model is chosen by principle, documented, and "
   "re-examined annually."),
 "how_it_works": ("The example pool: $9,600 control plane, usage-weighted by "
   "vCPU-hours - platform 50%, data 30%, apps 20% - yielding $4,800/$2,880/"
   "$1,920, summing exactly to $9,600 (allocations must foot). Weights come "
   "from metering: the same vCPU-hour meters that price compute. Equal-split "
   "pools divide by team count with no metering needed; headcount pools use "
   "the HR system's engineer counts as of month-end. Model changes are phased "
   "over a quarter with advance notice - the team gaining $2,000 a month "
   "deserves time to plan. The allocation report shows each team's total with "
   "the pool-by-pool breakdown, so any team can recompute its bill. Disputes "
   "follow the principles-ordered process; the models serve the principles, "
   "never the reverse."),
 "key_points": [
   "$9,600 pool at 50/30/20 = $4,800/$2,880/$1,920 - allocations must foot.",
   "Weights from metering (vCPU-hours); equal split needs no metering.",
   "Each pool's model chosen by principle and documented.",
   "Model changes phased over a quarter with notice.",
   "Teams can recompute their bills from the report.",
   "Models serve principles, never the reverse.",
 ],
 "requirements": [
   "Pool inventory with chosen models.",
   "Metering sources for weighted models.",
   "Footing verification (allocations sum to pools).",
   "Change phasing with notice.",
 ],
 "standards": [
   "Allocations always foot to the pool total.",
   "Weights from current metering, not last year's.",
   "Reports recomputable by the billed teams.",
   "Annual model re-examination.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (shared cost allocation).",
 ],
 "sig_lens": ("The Signature Cost Doctrine splits shared bread by rule, not by "
   "grab: the doctrine requires the division visible and the rule stated "
   "before the meal. The Signature edition insists the portions foot to the "
   "loaf - bread that does not divide evenly was miscounted, and miscounted "
   "bread starts fights."),
},
{
 "name": "Storage Tiering Costs",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "demo_key": "k_tiering",
 "demo_data": {"gb": 420, "mix": [0.2, 0.5, 0.3], "rates": [0.023, 0.0125, 0.004]},
 "description": ("The storage tiering record prices data by temperature: 420 GB "
   "split 20% hot at $0.023, 50% warm at $0.0125, 30% cold at $0.004 costs "
   "$5.07 a month instead of $9.66 all-hot - a 47.5% saving. Not all bytes are "
   "equal: yesterday's records are read constantly, last year's rarely, the "
   "archive almost never - yet all-hot pricing treats them identically. The "
   "record sets the tiering policy: access recency defines the tier, lifecycle "
   "rules move data automatically, and retrieval fees for cold data are "
   "priced in (cold storage is cheap to keep and metered to read). The 47.5% "
   "saving is net of the lifecycle management cost - tiering that costs more "
   "to administer than it saves is theater."),
 "how_it_works": ("Cost = sum(tier GB x tier rate): 84 x $0.023 ($1.93) + 210 x "
   "$0.0125 ($2.63) + 126 x $0.004 ($0.50) = $5.07, vs $9.66 all-hot. Tier "
   "assignment is by measured access: hot = accessed in 30 days, warm = 31-90 "
   "days, cold = older, evaluated by the lifecycle policy monthly. Retrieval "
   "fees apply to cold reads ($0.01/GB in the example) - the record tracks "
   "cold retrievals to verify the tiering still pays: if cold data gets read "
   "often, it belongs in warm. Lifecycle transitions are automatic but "
   "audited - the monthly report shows GB moved per tier and the resulting "
   "savings. Mis-tiering is the failure mode: hot data in cold tier pays "
   "retrieval fees that erase the savings, so the policy errs toward warmer."),
 "key_points": [
   "420 GB tiered 20/50/30% = $5.07/mo vs $9.66 all-hot: 47.5% saved.",
   "Tiers by measured access recency; lifecycle rules move data automatically.",
   "Cold retrieval fees ($0.01/GB) priced in and monitored.",
   "Savings net of lifecycle management cost.",
   "Mis-tiering erases savings - policy errs toward warmer.",
   "Monthly audit: GB moved per tier and resulting savings.",
 ],
 "requirements": [
   "Tiering policy with access-recency definitions.",
   "Lifecycle automation with audit reports.",
   "Cold retrieval tracking.",
   "Net-savings computation.",
 ],
 "standards": [
   "Tiers assigned by measurement, not by guess.",
   "Retrieval fees included in tier economics.",
   "Err toward warmer on uncertainty.",
   "Policy reviewed when access patterns shift.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (storage optimization).",
 ],
 "sig_lens": ("The Signature Cost Doctrine stores data like a prudent householder "
   "stores goods: daily tools by the door (hot), seasonal goods in the attic "
   "(warm), heirlooms in the vault (cold) - each in its proper place at its "
   "proper price. The Signature edition audits the attic monthly, because "
   "goods migrate and attics fill, and a vault used as a pantry pays vault "
   "prices for pantry goods."),
},
{
 "name": "Index Rebuild Costs",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "demo_key": "k_rebuild",
 "demo_data": {"rebuilds": 3, "cost_each": 12, "minutes": 42, "window": "02:00 UTC"},
 "description": ("The index rebuild cost record prices the periodic reconstruction "
   "of indexes: three rebuilds a year at $12 each is $36, each taking 42 "
   "minutes in the 02:00 UTC window. Rebuilds follow bulk ingestion - the "
   "drip runs that add thousands of records fragment indexes, and periodic "
   "rebuilds restore their efficiency. The $12 per rebuild covers the indexing "
   "workers' compute plus the temporary storage doubling during the rebuild. "
   "The record schedules rebuilds with the ingestion calendar (never ad hoc), "
   "measures whether each rebuild actually improved query performance (it "
   "should, or the schedule is wrong), and prices the alternative: "
   "incremental maintenance vs full rebuilds."),
 "how_it_works": ("Each rebuild is a planned event: announced a week ahead, run "
   "in the 02:00 UTC low-traffic window, taking 42 minutes, costing $12 in "
   "compute and temp storage. The three annual rebuilds align with the three "
   "bulk ingestion windows - rebuilds without preceding bulk loads are "
   "questioned, because rebuilding a healthy index is pure cost. Effectiveness "
   "is measured: p95 query latency before and after, with the improvement "
   "recorded - the example shows 18% latency improvement per rebuild, "
   "justifying the $36. Incremental maintenance (online reorganization) is "
   "priced as the alternative: $4/month continuous vs $36/year periodic - the "
   "periodic wins while bulk loads stay bursty. Failed rebuilds are incidents: "
   "the $12 is still spent, the index is still fragmented, and the retry is "
   "scheduled, not improvised."),
 "key_points": [
   "3 rebuilds/year x $12 = $36; 42 minutes each in the 02:00 UTC window.",
   "Scheduled with bulk ingestion - never ad hoc.",
   "Effectiveness measured: 18% p95 latency improvement justifies the spend.",
   "Alternative priced: $4/mo incremental vs $36/yr periodic - periodic wins.",
   "Failed rebuilds are incidents: cost spent, fragmentation remains, retry scheduled.",
   "Rebuilds without preceding bulk loads are questioned.",
 ],
 "requirements": [
   "Rebuild schedule aligned to ingestion calendar.",
   "Per-rebuild cost accounting (compute + temp storage).",
   "Before/after latency measurement.",
   "Alternative (incremental) pricing.",
 ],
 "standards": [
   "Rebuilds announced a week ahead.",
   "Low-traffic windows only.",
   "Effectiveness threshold: rebuilds must earn their cost.",
   "Failures handled as incidents.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework.",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats index rebuilds as the seasonal "
   "overhaul: the doctrine schedules them with the harvest (bulk loads), "
   "measures their yield (latency improvement), and questions any overhaul "
   "without a harvest before it. The Signature edition requires the yield "
   "proven - maintenance that cannot show its improvement is ritual, not "
   "husbandry."),
},
{
 "name": "Generation Batch Costing",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "demo_key": "k_batch",
 "demo_data": {"records": 11476, "per_record": 0.004, "offpeak_discount": 0.4, "offpeak_share": 0.8},
 "description": ("The generation batch costing record prices the factory runs: "
    "11,476 records at $0.004 is $45.90 per run at peak pricing - but with 80% "
   "of generation scheduled off-peak at a 40% discount, the blended run costs "
   "$31.21, saving $14.69 per run or $440.68 monthly across 30 runs. Batch "
   "generation is schedulable work, which makes it the most optimizable cost "
   "in the system: unlike serving queries that must run now, records can be "
   "built at 3 AM when compute is cheap. The record prices each batch with "
   "its peak/off-peak split, tracks the savings as a KPI, and guards quality "
   "- off-peak generation gets the same validation as peak, because cheap "
   "records that fail validation are the most expensive kind."),
 "how_it_works": ( "Blended cost = records x per-record x (peak_share x 1.0 + "
   "offpeak_share x 0.6): 11,476 x $0.004 x (0.2 + 0.8 x 0.6) = $45.90 x 0.68 "
   "= $31.21, saving $14.69 per run, $440.68 across 30 runs. The scheduler holds "
   "non-urgent generation for the off-peak window (22:00-06:00), when the "
   "40% discount applies; urgent generation (user-requested, incident-driven) "
   "runs at peak and is labeled as such. The monthly savings KPI - $440.68 at "
   "30 runs - is reported to engineering leadership as proof the scheduling "
   "discipline pays. Quality gates are identical across windows: validation "
   "compute is never skimped off-peak. Batch sizing is optimized too: runs "
   "are sized to fill the off-peak window without spilling into peak, because "
   "spillover pays peak rates for the overrun."),
 "key_points": [
   "$45.90 peak run vs ~$31 blended with 80% off-peak at 40% discount.",
   "$440.68/month saved across 30 runs by scheduling discipline.",
   "Batch generation is the most optimizable cost - it can wait for 3 AM.",
   "Urgent generation labeled and priced at peak honestly.",
   "Identical validation off-peak - cheap failures are the most expensive.",
   "Batches sized to fill the window without peak spillover.",
 ],
 "requirements": [
   "Peak/off-peak split recorded per batch.",
   "Blended cost computed, savings KPI reported.",
   "Identical quality gates across windows.",
   "Batch sizing to window capacity.",
 ],
 "standards": [
   "Off-peak window defined with discount terms.",
   "Urgent overrides logged with reasons.",
   "Validation never reduced for cost.",
   "Spillover measured and minimized.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (workload scheduling).",
 ],
 "sig_lens": ("The Signature Cost Doctrine runs the factory on the night shift "
   "where the power is cheap: the doctrine requires the schedulable work "
   "scheduled cheaply, as a matter of discipline, not of cleverness. The "
   "Signature edition guards the night shift's quality jealously - the "
   "doctrine would rather pay peak prices than ship cheap defects."),
},
{
 "name": "Retrieval SLA Cost Tradeoffs",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "demo_key": "k_sla_trade",
 "demo_data": {"standard_cpm": 0.004, "premium_mult": 5, "premium_p95_ms": 120, "standard_p95_ms": 900, "mix": [0.7, 0.3]},
 "description": ("The retrieval SLA tradeoff record prices speed: standard "
   "queries at $0.004 per thousand with p95 900ms vs premium at 5x ($0.02) "
   "with p95 120ms - and the 70/30 mix that blends them. Every millisecond "
   "has a price, and the record makes the exchange rate explicit so teams "
   "choose deliberately instead of defaulting to premium 'to be safe.' The "
   "example fleet spends $21.12/month on retrieval; moving 10 points of mix "
   "from premium to standard (where the latency budget allows) saves $3.84 - "
   "18.2%. The record classifies queries by actual latency need: user-facing "
   "interactive gets premium, batch analytics gets standard, and the "
   "classification is reviewed when features change."),
 "how_it_works": ("Each query class gets an SLA tier assignment with its "
   "latency target and unit cost: premium 120ms p95 at $0.02/1k, standard "
   "900ms p95 at $0.004/1k. The 70/30 mix yields the $21.12 blended bill "
   "(computed in the retrieval record). The tradeoff analysis runs quarterly: "
   "for each premium-class query pattern, is the 120ms actually needed? "
   "Patterns that tolerate 900ms are demoted, with the savings tracked - the "
   "10-point shift saving $3.84/month is the example. Latency budgets come "
   "from product requirements, not engineering preference: the record cites "
   "the requirement per class. Premium spend without a cited latency need is "
   "flagged as waste, because 'fast' is not a requirement and 5x is not a "
   "rounding error."),
 "key_points": [
   "Standard: $0.004/1k, p95 900ms. Premium: 5x, p95 120ms. Mix 70/30 = $21.12.",
   "Shifting 10 points premium->standard saves $3.84 (18.2%).",
   "Tiers assigned by cited latency need, not engineering preference.",
   "'Fast' is not a requirement; 5x is not a rounding error.",
   "Quarterly tradeoff review demotes over-tiered patterns.",
   "Every millisecond has an exchange rate - choose deliberately.",
 ],
 "requirements": [
   "Latency requirements cited per query class.",
   "Tier assignments with unit costs.",
   "Quarterly tradeoff review.",
   "Savings tracked per demotion.",
 ],
 "standards": [
   "No premium tier without a written latency requirement.",
   "Mix measured monthly.",
   "Demotions reversible if latency suffers.",
   "Requirements re-validated when features change.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework.",
 ],
 "sig_lens": ("The Signature Cost Doctrine prices speed like a courier service: "
   "overnight, two-day, standard - each with its rate, chosen by need. The "
   "Signature edition forbids the 'everything overnight' default - a doctrine "
   "that pays courier rates for letters nobody is waiting for is not "
   "generous, it is innumerate."),
},
{
 "name": "Cache Cost-Benefit Analysis",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "demo_key": "k_cache",
 "demo_data": {"calls_day": 48000, "hit_rate": 0.72, "cost_per_1k": 1.5, "cache_cost_day": 8.4},
 "description": ("The cache cost-benefit record proves the cache earns its keep: "
   "48,000 calls a day at 72% hit rate absorbs 34,560 calls; at $1.50 per "
   "thousand that's $51.84 a day in avoided origin cost against $8.40 a day "
   "in cache cost - net $43.44 daily, $1,303 monthly. Caching is an "
   "investment with a measurable return, and the record measures it: avoided "
   "origin cost minus cache infrastructure cost (memory, invalidation "
   "compute, operational overhead). The 6.2x return justifies the cache; a "
   "cache returning less than 2x gets a redesign review. Hit rate is the "
   "lever: every point of hit rate is worth $0.72 a day here, so the "
   "invalidation tuning that lifted hit rate from 68% to 72% pays $2.88 "
   "daily."),
 "how_it_works": ("Avoided cost = calls x hit_rate / 1000 x $/1k: 48,000 x "
   "0.72 / 1000 x $1.50 = $51.84/day. Cache cost = $8.40/day (memory $5.20, "
   "invalidation compute $1.90, operational share $1.30). Net = $43.44/day, "
   "$1,303/month. The record tracks hit rate by content class, because "
   "aggregate hit rate hides the classes where caching fails - the 72% "
   "blends 91% on reference data with 41% on personalized data, and the "
   "latter is a candidate for cache removal (its invalidation cost exceeds "
   "its savings). Staleness cost is estimated too: the 0.3% of served-stale "
   "responses that caused user-visible issues are priced (support time, "
   "goodwill) and charged against the cache's return. The verdict rule: net "
   "positive and return above 2x, or redesign."),
 "key_points": [
   "$51.84/day avoided vs $8.40/day cache cost = $43.44 net daily ($1,303/mo).",
   "6.2x return; below 2x triggers redesign review.",
   "Hit rate by content class: 91% reference vs 41% personalized.",
   "Each hit-rate point worth $0.72/day here.",
   "Staleness incidents priced and charged against the return.",
   "Verdict: net positive and 2x+, or redesign.",
 ],
 "requirements": [
   "Avoided-cost computation with measured hit rates.",
   "Cache cost fully loaded (memory, compute, ops).",
   "Per-class hit rates.",
   "Staleness incident pricing.",
 ],
 "standards": [
   "Hit rates measured, not estimated.",
   "2x return threshold enforced.",
   "Personalized-content caching justified per class.",
   "Invalidation tuning tracked as a KPI.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework.",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats the cache as a warehouse that "
   "must pay its rent: the doctrine requires the $43.44 daily profit proven, "
   "not assumed. The Signature edition prices the stale goods too - a "
   "warehouse whose spoilage nobody counts is profitable only on paper."),
},
{
 "name": "Compression Savings Record",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "demo_key": "k_compress",
 "demo_data": {"raw_gb": 935, "ratio": 5.0, "rate": 0.023, "cpu_cost_mo": 3.2},
 "description": ("The compression savings record prices smaller bytes: 935 GB "
   "at 5:1 compression becomes 187 GB, saving 748 GB of storage - $17.20 a "
   "month at $0.023/GB - against $3.20 a month in compression CPU, net "
   "$14.00 monthly. Compression trades CPU for disk, and the record verifies "
   "the trade wins: net positive by 4.4x here. The ratio is measured per "
   "data class - text compresses 5:1, JSON 4:1, already-compressed media "
   "barely 1.05:1 (and is not recompressed, because compressing JPEGs burns "
   "CPU for nothing). Decompression latency is priced into the retrieval "
   "model: the 12ms added to p50 reads is acceptable for the archive tiers, "
   "not for the hot tier - so hot data stays uncompressed."),
 "how_it_works": ("Savings = (raw - compressed) GB x $/GB-month: (935 - 187) x $0.023 "
   "= 748 x $0.023 = $17.20/month (computed exactly in the demo). CPU cost = compression worker hours x "
   "rate: $3.20/month. Net = savings - CPU, must exceed 2x CPU to justify "
   "(here ~4.4x). Ratios are measured per class on samples before rollout; "
   "the policy compresses classes above 2:1, skips below. Decompression cost "
   "lands in retrieval latency: +12ms p50, acceptable for warm/cold tiers. "
   "The record also prices the alternative: thinner provisioning vs "
   "compression - compression wins while CPU stays cheap relative to disk, "
   "revisited if the price ratio inverts."),
 "key_points": [
   "935 GB at 5:1 -> 187 GB; ~$14/month net after $3.20 CPU cost.",
   "Ratios per class: text 5:1, JSON 4:1, media 1.05:1 (not recompressed).",
   "Net must exceed 2x CPU cost; here ~4.4x.",
   "+12ms decompression p50: fine for warm/cold, not hot tier.",
   "Hot data stays uncompressed - latency beats savings there.",
   "Revisited if the CPU/disk price ratio inverts.",
 ],
 "requirements": [
   "Measured ratios per data class.",
   "CPU cost accounting for compression.",
   "Net-savings computation with 2x threshold.",
   "Decompression latency impact assessed.",
 ],
 "standards": [
   "No recompression of already-compressed media.",
   "Hot tier exempt unless latency-neutral.",
   "Ratios remeasured when data mix changes.",
   "CPU/disk price ratio watched.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework.",
 ],
 "sig_lens": ("The Signature Cost Doctrine packs the warehouse tightly but never "
   "packs the storefront: the doctrine requires the compression proven "
   "profitable per class, with the decompression latency priced honestly. "
   "The Signature edition refuses to recompress the already-compressed - "
   "squeezing JPEGs is not thrift, it is theater with a CPU bill."),
},
{
 "name": "Backup and Disaster Recovery Costs",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "demo_key": "k_backup",
 "demo_data": {"gb": 802, "rate": 0.023, "version_factor": 1.2, "drill_cost": 150, "drills_year": 4},
 "description": ("The backup and disaster recovery cost record prices safety: "
   "802 GB at $0.023 with a 1.2 versioning factor is $22.14 a month in backup "
   "storage, plus four drills a year at $150 each ($600/year, $50/month) - "
   "total about $72.14 monthly for the ability to survive catastrophe. Backup "
   "is insurance: the premium is certain, the payout is hypothetical, and "
   "the record prices it like insurance - by the risk it covers. The 1.2 "
   "factor covers versioned retention (30 daily, 12 monthly versions with "
   "dedupe); the drills prove the restores actually work, because a backup "
   "that cannot restore is not insurance but a comforting lie with a monthly "
   "bill."),
 "how_it_works": ("Backup storage = GB x rate x version factor: 802 x $0.023 x "
   "1.2 = $22.14/month. The version factor is measured from actual retention "
   "consumption, not assumed - dedupe across versions keeps it at 1.2 rather "
   "than the naive 2.5. Drill cost = staff time + compute + verification: "
   "$150 per drill x 4/year = $600/year. The record also prices the RPO/RTO "
   "choice: synchronous cross-region replication would add $180/month for a "
   "15-minute better RPO - evaluated and declined, documented with the risk "
   "acceptance. Restore testing is the control that matters: each drill "
   "restores a sampled database and verifies checksums, because the industry "
   "is full of backups that never restored. Untested backup spend is flagged "
   "as waste regardless of amount."),
 "key_points": [
   "802 GB x $0.023 x 1.2 = $22.14/mo backup storage + $50/mo drills = ~$72.14/mo.",
   "Version factor 1.2 measured (dedupe), not the naive 2.5.",
   "RPO/RTO upgrades priced as options: +$180/mo for 15-min better RPO (declined, documented).",
   "Drills restore and verify checksums - untested backups are comforting lies.",
   "Untested backup spend flagged as waste at any amount.",
   "Insurance priced by the risk it covers.",
 ],
 "requirements": [
   "Measured version factor.",
   "Drill schedule with per-drill costing.",
   "RPO/RTO option pricing with decisions.",
   "Restore verification in every drill.",
 ],
 "standards": [
   "Drills quarterly minimum.",
   "Checksum verification on restores.",
   "Risk acceptances documented for declined upgrades.",
   "Backup spend without drill proof flagged.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1: Contingency Planning Guide.",
 ],
 "sig_lens": ("The Signature Cost Doctrine buys insurance with open eyes: the "
   "doctrine requires the premium priced, the coverage defined, and the "
   "claim tested - by drill, not by disaster. The Signature edition treats "
   "an untested backup as the most expensive kind: money spent for safety "
   "that is not there when needed."),
},
{
 "name": "Inter-Shard Transfer Costs",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "demo_key": "k_transfer",
 "demo_data": {"gb": 450, "rate": 0.02, "syncs_month": 30},
 "description": ("The inter-shard transfer cost record prices data movement "
   "between shards: 450 GB a month at $0.02 per GB is $9.00 - thirty daily "
   "syncs of 15 GB. Shards replicate, rebalance, and backfill, and every "
   "gigabyte crossing a region boundary is metered. The record meters by "
   "cause: replication (the steady 15 GB daily), rebalancing (bursty, after "
   "shard splits), and backfill (one-time, after incidents). At $9/month the "
   "cost is small, which is exactly why it is tracked - small unmeasured "
   "costs grow silently, and the transfer volume is the early warning for "
   "architectural drift (a shard that suddenly syncs 10x was probably "
   "mispartitioned)."),
 "how_it_works": ("Cost = GB x $/GB: 450 x $0.02 = $9.00/month. The 450 GB "
   "breaks into 450 GB replication... precisely: 30 syncs x 15 GB = 450 GB, "
   "all cross-region replication at $0.02. Rebalancing events are logged "
   "separately - last quarter's shard-16 creation moved 110 chunks (~85 GB) "
   "one time at $1.70, recorded as a capital event, not run-rate. The record "
   "watches the per-shard transfer ratio: shards syncing far above their "
   "size-proportional share are investigated for partition skew. Compression "
   "applies to transfers (the 5:1 ratio from the compression record), so the "
   "450 GB is post-compression - the raw movement was ~2.2 TB, and the "
   "savings are credited. Transfer anomalies (10x spikes) alert like cost "
   "anomalies, because they usually are."),
 "key_points": [
   "450 GB/month x $0.02 = $9.00; 30 daily syncs of 15 GB.",
   "Metered by cause: replication (steady), rebalancing (bursty), backfill (one-time).",
   "Shard-16 creation: 85 GB one-time at $1.70, a capital event.",
   "Per-shard ratios watched for partition skew.",
   "450 GB post-compression; raw ~2.2 TB with savings credited.",
   "Small unmeasured costs grow silently - tracked precisely because it is small.",
 ],
 "requirements": [
   "Transfer metering by cause.",
   "Capital vs run-rate classification.",
   "Per-shard ratio monitoring.",
   "Compression credit accounting.",
 ],
 "standards": [
   "All cross-region bytes metered.",
   "Rebalancing events logged with cause.",
   "Skew investigations triggered by ratio alerts.",
   "Spikes alerted as cost anomalies.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (data transfer).",
 ],
 "sig_lens": ("The Signature Cost Doctrine counts the wagons between "
   "warehouses: the doctrine requires every inter-shard byte metered by "
   "cause, because uncounted movement is how architectures drift. The "
   "Signature edition treats a 10x sync spike as a confession - the shard "
   "is saying its partitions are wrong, and the doctrine listens."),
},
{
 "name": "Cost Anomaly Detection",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "demo_key": "k_anomaly",
 "demo_data": {"alerts": 312, "true_pos": 289, "mttr_h": 3.2, "saved": 1840},
 "description": ("The cost anomaly detection record watches the meter for "
   "surprises: 312 alerts last year, 289 true positives (92.6% precision), "
   "3.2-hour mean time to resolve, $1,840 in runaway spend caught and "
   "stopped. Anomalies are the early warnings - a runaway query loop, a "
   "misconfigured retention, a compromised key burning egress - and the "
   "difference between a $50 anomaly and a $5,000 invoice is detection "
   "speed. The record tunes for precision over recall: 23 false positives "
   "is the cost of catching the 289 true ones, and the tuning keeps the "
   "false ones from training teams to ignore the alerts."),
 "how_it_works": ("Detection compares actual spend against forecasted spend "
   "per database per dimension, alerting beyond adaptive thresholds (3 "
   "standard deviations on stable series, wider on bursty ones). The 312 "
   "alerts broke into 289 true (runaway queries, retention misconfigs, "
   "egress spikes, a compromised test key) and 23 false (legitimate growth, "
   "one-time backfills) - precision 92.6%. MTTR of 3.2 hours measures "
   "alert-to-mitigation; the $1,840 saved is spend that would have continued "
   "without detection, estimated from the run-rate at detection time. Each "
   "true positive gets a root cause and a prevention: the runaway query got "
   "a query governor, the retention misconfig got a policy check. The "
   "detector's own cost is tracked - $120/month in compute - for an ROI of "
   "over 15x."),
 "key_points": [
   "312 alerts, 289 true (92.6% precision), MTTR 3.2h, $1,840 runaway spend stopped.",
   "Adaptive thresholds: 3 sigma on stable series, wider on bursty.",
   "True positives get root causes and preventions, not just fixes.",
   "Tuned for precision: 23 false positives is the price of 289 catches.",
   "Detector ROI over 15x ($1,840 saved vs $120/month cost).",
   "The difference between a $50 anomaly and a $5,000 invoice is detection speed.",
 ],
 "requirements": [
   "Forecasted-vs-actual comparison per database per dimension.",
   "Adaptive thresholds with documented tuning.",
   "Root-cause and prevention per true positive.",
   "Detector cost tracking with ROI.",
 ],
 "standards": [
   "Alerts owned with runbooks.",
   "Precision tracked; tuning for precision over recall.",
   "False positives analyzed, not just dismissed.",
   "Preventions verified effective.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (anomaly detection).",
 ],
 "sig_lens": ("The Signature Cost Doctrine posts a night watchman on the meter: "
   "the doctrine requires the watchman sharp-eyed (92.6% precision) and "
   "quick (3.2h MTTR), because money leaking at 3 AM does not wait for "
   "business hours. The Signature edition measures the watchman's own wage "
   "against his catches - 15x return - and finds him cheap at twice the "
   "price."),
},
# ---------------- Advanced (22-34) ----------------
{
 "name": "Total Cost of Ownership at Scale",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "demo_key": "k_tco",
 "demo_data": {"capex": 18000, "opex_mo": 1500.07, "years": 3, "growth": 0.15},
 "description": ("The total cost of ownership record prices the whole journey: "
   "$18,000 capital expense plus $1,500.07 monthly operating cost over three "
   "years is $72,002.52 at flat scale - and with 15% annual record growth, "
   "the variable portion compounds to a three-year TCO of about $76,400. TCO "
   "is the number that matters for build-vs-buy, for funding requests, and "
   "for the 'is this sustainable' question. It includes everything the "
   "monthly ledger includes, plus the capital nobody puts on the monthly "
   "page: initial engineering, migration, training, and the decommissioning "
   "cost everyone forgets until decommissioning day."),
 "how_it_works": ("TCO = capex + sum over months of (fixed + variable x "
   "growth^t). Flat: $18,000 + 36 x $1,500.07 = $72,002.52. With 15% annual "
   "growth on the variable $300.07: year 1 $3,600.84, year 2 $4,140.97, year "
   "3 $4,762.11 - variable total $12,503.92 vs flat $10,802.52, a $1,701.40 "
   "growth premium; fixed $1,200 x 36 = $43,200; TCO = $18,000 + $43,200 + "
   "$12,503.92 = $73,703.92 (computed exactly in the demo). Capex breaks "
   "into engineering $12,000, migration $4,000, training $1,500, and "
   "decommissioning reserve $500. The record is recomputed annually and on "
   "architectural changes; TCO comparisons (build vs buy, cloud A vs cloud B) "
   "use identical scopes and horizons, or they are not comparisons."),
 "key_points": [
   "$18k capex + $1,500.07/mo x 36 = $72,002.52 flat; ~$73,704 with 15% growth.",
   "Growth premium on variable costs: $1,701 over three years.",
   "Capex: engineering $12k, migration $4k, training $1.5k, decom reserve $500.",
   "Includes the decommissioning everyone forgets until decommissioning day.",
   "Recomputed annually and on architectural changes.",
   "Comparisons use identical scopes and horizons - or they are not comparisons.",
 ],
 "requirements": [
   "Capex breakdown with all four components.",
   "Monthly opex with fixed/variable split.",
   "Growth assumption documented with evidence.",
   "Annual recomputation.",
 ],
 "standards": [
   "Identical scope and horizon for comparisons.",
   "Decommissioning reserve mandatory.",
   "Growth rates from the forecasting database, not from optimism.",
   "TCO horizon minimum three years.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (TCO analysis).",
 ],
 "sig_lens": ("The Signature Cost Doctrine prices the whole voyage, not just "
   "the daily bread: the doctrine requires the TCO on the table before the "
   "ship sails. The Signature edition includes the decommissioning reserve "
   "- the doctrine holds that a voyage planned without its return is not a "
   "plan, it is an abandonment scheduled for later."),
},
{
 "name": "Forecasting-Driven Budgeting",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "demo_key": "k_budget",
 "demo_data": {"budget_mo": 5000, "actual_mo": 4612, "forecast_mo": 4780, "quarter": "2026-Q4"},
 "description": ("The forecasting-driven budgeting record sets spending from "
   "predicted need, not from last year plus hope: Q4 2026 budget $5,000 a "
   "month against actual $4,612 and forecast $4,780 - under budget by 7.76%, "
   "with the forecast within 3.6% of actual. Budgets derive from the capacity "
   "growth forecasts: projected records times unit costs, plus fixed costs, "
   "plus a contingency reserve (5% here). The forecast-actual-budget triangle "
   "is the control: budget says what was authorized, forecast says what was "
   "expected, actual says what happened. When forecast and actual diverge, "
   "the model is tuned; when budget and forecast diverge, the plan is "
   "questioned. A budget without a forecast is a wish with a signature."),
 "how_it_works": ("The quarterly budget builds from: fixed costs ($1,200 x 3 "
   "= $3,600/quarter per database, summed), variable forecast (projected "
   "records x unit costs from the forecasting database), and a 5% contingency "
   "for price changes and surprises. Q4 2026: budget $15,000/quarter "
   "($5,000/mo), forecast $14,340 ($4,780/mo), actual $13,836 ($4,612/mo). "
   "Variance analysis runs monthly: budget-vs-actual (-7.76%, favorable), "
   "forecast-vs-actual (+3.6%, the model slightly high). Favorable variances "
   "are investigated too - persistent underspend means the budget is padded "
   "or the forecast is wrong, both worth knowing. Contingency draw-downs are "
   "logged with reasons; an untouched contingency at quarter-end is returned, "
   "not spent, because contingency spent 'because it was there' is not "
   "contingency."),
 "key_points": [
   "Q4 2026: budget $5,000/mo, forecast $4,780, actual $4,612 (-7.76% vs budget).",
   "Budgets from growth forecasts x unit costs + fixed + 5% contingency.",
   "Triangle: budget (authorized), forecast (expected), actual (happened).",
   "Forecast-actual divergence tunes the model; budget-forecast divergence questions the plan.",
   "Favorable variances investigated too - padding and model error both matter.",
   "Untouched contingency returned, never spent because it was there.",
 ],
 "requirements": [
   "Budget build from forecasts with documented assumptions.",
   "Monthly variance analysis (budget and forecast).",
   "Contingency policy with draw-down logging.",
   "Quarterly forecast accuracy review.",
 ],
 "standards": [
   "Forecasts from the capacity forecasting database.",
   "Contingency 5% default, justified if different.",
   "No budget without a supporting forecast.",
   "Accuracy tracked: forecast-vs-actual reported every quarter.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (budgeting).",
 ],
 "sig_lens": ("The Signature Cost Doctrine budgets from the map (forecast), "
   "not from the rearview mirror: the doctrine requires the budget to say "
   "what the journey should cost given where we are going. The Signature "
   "edition returns unspent contingency as a matter of honor - a steward "
   "who spends the reserve to avoid returning it has confused stewardship "
   "with ownership."),
},
{
 "name": "Chargeback and Showback Models",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "demo_key": "k_chargeback",
 "demo_data": {"total": 4612, "shares": [0.6, 0.25, 0.15], "teams": ["platform", "data", "apps"], "model": "chargeback"},
 "description": ("The chargeback record bills teams for what they use: $4,612 "
   "a month split 60/25/15 by measured usage - platform $2,767.20, data "
   "$1,153.00, apps $691.80 - actually charged to their budgets. Chargeback "
   "moves real money (or real budget); showback shows the bill without "
   "moving money. The record implements chargeback for the mature cost "
   "centers and showback for new teams in their first two quarters - because "
   "billing a team that is still learning the system teaches resentment, "
   "not efficiency. The 60/25/15 split comes from metering (compute-hours, "
   "storage-GB, query counts weighted), not from negotiation."),
 "how_it_works": ("Each team's share = total x usage share: $4,612 x 0.6 = "
   "$2,767.20; x 0.25 = $1,153.00; x 0.15 = $691.80; footing to $4,612.00 "
   "exactly. Usage shares derive from the metering: 55% compute weight, 25% "
   "storage, 20% queries, blended per team. Chargeback posts to team budgets "
   "monthly with the ledger detail; teams may dispute within 15 days via the "
   "allocation dispute process. Showback teams get the same report marked "
   "'informational - no charge,' graduating to chargeback after two quarters "
   "or $1,000/month, whichever comes first. The behavioral effect is the "
   "point: teams that see their $2,767 optimize; teams that never see a bill "
   "treat the databases as free. The record measures the effect - chargeback "
   "teams reduced usage 12% year over year without output loss."),
 "key_points": [
   "$4,612 at 60/25/15 = $2,767.20/$1,153.00/$691.80, footing exactly.",
   "Shares from metering (55% compute, 25% storage, 20% queries), not negotiation.",
   "Chargeback moves budget; showback informs (new teams, 2 quarters).",
   "Disputes within 15 days via the allocation process.",
   "Behavioral effect measured: chargeback teams cut usage 12% YoY.",
   "Teams that never see a bill treat the databases as free.",
 ],
 "requirements": [
   "Metering-based share computation.",
   "Monthly charge postings with ledger detail.",
   "Showback graduation criteria.",
   "Dispute window and process.",
 ],
 "standards": [
   "Charges foot to the reconciled total.",
   "Shares remeasured quarterly.",
   "No charge without metered evidence.",
   "Behavioral effects tracked, not assumed.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (chargeback).",
 ],
 "sig_lens": ("The Signature Cost Doctrine bills by the meter, visibly: the "
   "doctrine holds that people manage what they pay for, and pay attention "
   "to what they see. The Signature edition graduates showback teams to "
   "chargeback on schedule - permanent showback is a permanent subsidy, and "
   "subsidies hide the very signals the doctrine exists to reveal."),
},
{
 "name": "Cost of Data Quality",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "demo_key": "k_quality",
 "demo_data": {"rework_h": 340, "rate": 85, "incidents": 7, "incident_cost": 12000},
 "description": ("The data quality cost record prices bad data: 340 rework "
   "hours at $85 is $28,900 a year in fixing, plus 7 quality incidents at "
   "$12,000 average impact is $84,000 - total $112,900 annually that good "
   "data would not have cost. Bad data is not free; it is merely unbilled - "
   "paid in rework, in wrong decisions, in incidents, in the slow erosion of "
   "trust that makes everyone re-verify everything. The record splits quality "
   "cost into prevention (validation, monitoring), appraisal (audits, "
   "sampling), internal failure (rework before release), and external failure "
   "(incidents after release) - because the cheapest place to catch an error "
   "is at entry, and the most expensive is in production."),
 "how_it_works": ("Prevention: $18,000/year in validation compute and rule "
   "maintenance. Appraisal: $9,500 in audits and sampling. Internal failure: "
   "340 rework hours x $85 = $28,900. External failure: 7 incidents x $12,000 "
   "= $84,000. Total cost of quality: $140,400, of which $112,900 is failure "
   "- the classic imbalance proving underinvestment in prevention. The "
   "record computes the prevention ROI: every $1 shifted from failure to "
   "prevention historically returns $4 in this fleet (the validation rule "
   "that caught the March incident class would have cost $2,000 to build "
   "vs the $36,000 incident it would have prevented). Quality investment "
   "decisions cite this record; 'we cannot afford validation' is answered "
   "with the $112,900 failure bill."),
 "key_points": [
   "Rework $28,900 + incidents $84,000 = $112,900/year in failure costs.",
   "Total quality cost $140,400; failure dominates - underinvestment in prevention.",
   "Prevention ROI 4:1 in this fleet ($2k rule vs $36k incident).",
   "Bad data is unbilled, not free - paid in rework, decisions, trust.",
   "'Cannot afford validation' answered with the $112,900 bill.",
   "Cheapest catch at entry; most expensive in production.",
 ],
 "requirements": [
   "Four-category quality cost accounting.",
   "Incident costing with impact methodology.",
   "Prevention ROI tracking.",
   "Rework hour logging.",
 ],
 "standards": [
   "Incident costs include decision impact, not just engineering time.",
   "Prevention investments require ROI estimates.",
   "Failure trend reported quarterly.",
   "Quality budget set from this record, not from hope.",
 ],
 "citations": [
   "English, L. Improving Data Warehouse and Business Information Quality. Wiley (cost of poor data quality).",
 ],
 "sig_lens": ("The Signature Cost Doctrine prices bad data like spoiled goods: "
   "the doctrine requires the spoilage counted - $112,900 - because "
   "unpriced rot spreads. The Signature edition invests the $2,000 in the "
   "validation rule gladly: the doctrine's arithmetic is simple, that "
   "prevention at 4:1 is not spending but harvesting."),
},
{
 "name": "Cost of Governance Overhead",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "demo_key": "k_govcost",
 "demo_data": {"audit_h": 120, "rate": 95, "tooling_mo": 800, "databases": 5000},
 "description": ("The governance overhead cost record prices the cost of "
   "control itself: 120 audit hours at $95 is $11,400 a year, plus $800 a "
   "month in governance tooling ($9,600/year) - $21,000 annually to govern "
   "5,000 databases, or $4.20 per database per year. Governance is not free, "
   "and pretending it is leads to the two failure modes: starving it (then "
   "wondering why nobody trusts the data) or gold-plating it (controls "
   "costing more than the risks they mitigate). The record prices each "
   "governance activity - audits, reviews, policy maintenance, tooling, "
   "training - and asks the ROI question per activity, because overhead that "
   "cannot justify itself is just overhead."),
 "how_it_works": ("The $21,000 breaks into: audits $11,400 (120h x $95), "
   "tooling $9,600 ($800/mo: policy engine, audit log storage, dashboard), "
   "policy maintenance $6,000 (60h), training $4,000 - total $31,000... "
   "recomputed exactly in the demo; the per-database figure follows. Each "
   "activity carries its justification: audits caught $48,000 in misallocated "
   "costs last year (4.2x return); the policy engine's automated checks "
   "replaced 200 manual review hours. Activities below 2x return go on the "
   "chopping block annually - governance must earn its keep like everything "
   "else. The record also prices governance risk inversely: the estimated "
   "cost of the incidents governance prevented, so the 'what if we cut it' "
   "question has a number attached."),
 "key_points": [
   "~$31,000/year governing 5,000 databases (~$6.20 per database/year).",
   "Priced per activity: audits, tooling, policy, training.",
   "Audits returned 4.2x ($48k caught misallocations).",
   "Activities below 2x return face the chopping block annually.",
   "Two failure modes: starved governance and gold-plated governance.",
   "Overhead that cannot justify itself is just overhead.",
 ],
 "requirements": [
   "Per-activity governance cost accounting.",
   "ROI per activity with evidence.",
   "Annual cull of sub-2x activities.",
   "Prevented-incident valuation.",
 ],
 "standards": [
   "Governance costs fully loaded (staff time at burdened rates).",
   "ROI evidence, not assertion.",
   "Per-database unit reported for scale planning.",
   "Risk acceptance documented where governance is declined.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework.",
 ],
 "sig_lens": ("The Signature Cost Doctrine weighs the watchman too: the "
   "doctrine requires governance to prove its $31,000 like any other "
   "spend. The Signature edition culls the sub-2x controls annually - a "
   "doctrine that exempts its own overhead from accounting is not "
   "discipline, it is priesthood with a budget."),
},
{
 "name": "Marginal Cost per Million Records",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "demo_key": "k_marginal",
 "demo_data": {"variable_per_record": 0.0031, "million": 1000000, "fixed_step": 250},
 "description": ("The marginal cost record prices the next million: $0.0031 "
   "variable per record times one million is $3,100 a month in true marginal "
   "cost, plus a $250 step-fixed support tier increase - $3,350 total. "
   "Marginal cost is the number for growth decisions: it answers 'what does "
   "one more million cost us' without the fixed-cost distortion of the "
   "average unit. The $0.0155 average unit would quote $15,500 for the "
   "million - nearly 5x the true marginal - which would kill worthwhile "
   "growth. The record keeps both numbers honest: average for efficiency "
   "comparisons, marginal for growth decisions, and never the twain confused."),
 "how_it_works": ("Marginal = variable unit x quantity + step-fixed triggers: "
   "$0.0031 x 1,000,000 = $3,100 + $250 (support tier step at the volume "
   "threshold) = $3,350/month. The step-fixed scan checks every threshold "
   "between current and target volume: license tiers, support tiers, "
   "commitment cliffs - the $250 is the only trigger in this range. Beyond "
   "one million, the record projects the step function: the next support "
   "tier at 5M records (+$1,200/mo), the license tier at 10M (+$8,000/mo) - "
   "so growth planning sees the stairs, not just the slope. The marginal "
   "is recomputed when variable rates change; a rate increase flows "
   "straight through. Growth proposals cite this record's number; proposals "
   "citing the average unit are returned for correction."),
 "key_points": [
   "$0.0031 x 1M = $3,100 + $250 step-fixed = $3,350/month marginal.",
   "Average unit ($15,500/M) would kill worthwhile growth - 5x the truth.",
   "Step-fixed scan: support +$250 here; +$1,200 at 5M; +$8,000 license at 10M.",
   "Average for efficiency comparisons; marginal for growth decisions.",
   "Growth proposals citing the average are returned for correction.",
   "Planning sees the stairs (steps), not just the slope.",
 ],
 "requirements": [
   "Variable unit maintained current.",
   "Step-fixed threshold inventory.",
   "Marginal computed per growth proposal.",
   "Average/marginal discipline enforced.",
 ],
 "standards": [
   "Marginal from variable costs only.",
   "All step thresholds in range identified.",
   "Proposals state which unit they use and why.",
   "Recomputed on rate changes.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (marginal economics).",
 ],
 "sig_lens": ("The Signature Cost Doctrine prices the next mile, not the whole "
   "journey: the doctrine requires growth decisions made on marginal truth "
   "($3,350), not average illusion ($15,500). The Signature edition returns "
   "proposals that cite the wrong number - a doctrine that lets averages "
   "veto growth is a doctrine taxing the future for the past's fixed costs."),
},
{
 "name": "Public vs Signature Pipeline Cost Comparison",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "demo_key": "k_compare",
 "demo_data": {"public_per_record": 0.021, "sig_per_record": 0.014, "records_mo": 344280},
 "description": ("The pipeline cost comparison prices the two ways of building: "
   "public-harvest pipeline at $0.021 per record vs Signature pipeline at "
   "$0.014 - the Signature path 33.3% cheaper at 344,280 records a month "
   "($7,229.88 vs $4,819.92, saving $2,409.96 monthly). The difference is "
   "structural: harvesting pays egress, parsing, deduplication against the "
   "unknown, and licensing; the Signature pipeline pays generation with "
   "known provenance and no licensing. The record compares fully-loaded "
   "unit costs - compute, inference, validation, storage-ingest, licensing, "
   "and failure rates - over trailing 90 days, because pipeline economics "
   "drift as models and prices change."),
 "how_it_works": ("Public unit: $0.021 = $0.008 egress+fetch, $0.006 parse, "
   "$0.004 dedupe, $0.002 licensing, $0.001 validation. Signature unit: "
   "$0.014 = $0.009 generation compute, $0.003 inference, $0.0015 validation, "
   "$0.0005 storage-ingest. Monthly at 344,280 records: $7,229.88 vs "
   "$4,819.92. The comparison includes quality-adjusted cost: public records "
   "need 8% rework ($0.0017 effective adder), Signature records 2% ($0.0003) "
   "- the quality gap widens the economic gap. The record is honest about "
   "reversals: where harvesting is cheaper (bulk public datasets with "
   "permissive licensing), it says so and routes work there. Pipeline choice "
   "is per-workload, reviewed quarterly - dogma is not a cost model."),
 "key_points": [
   "Public $0.021 vs Signature $0.014 per record - 33.3% cheaper Signature.",
   "$7,229.88 vs $4,819.92 monthly at 344,280 records ($2,409.96 saved).",
   "Quality-adjusted: public +$0.0017 rework vs Signature +$0.0003.",
   "Fully-loaded units over trailing 90 days.",
   "Honest about reversals: harvesting wins some workloads, routed there.",
   "Per-workload choice, quarterly review - dogma is not a cost model.",
 ],
 "requirements": [
   "Fully-loaded unit costs per pipeline.",
   "Quality-adjusted costing.",
   "Trailing-90-day measurement.",
   "Workload-level routing decisions.",
 ],
 "standards": [
   "Identical scope in comparisons.",
   "Licensing costs included where applicable.",
   "Reversals documented, not hidden.",
   "Quarterly re-comparison.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework.",
 ],
 "sig_lens": ("The Signature Cost Doctrine compares honestly, even when the "
   "comparison flatters: the doctrine requires the $2,409.96 proven and "
   "the reversals admitted. The Signature edition routes each workload to "
   "its cheapest honest path - a doctrine that favored its own pipeline "
   "against the numbers would be marketing, not accounting."),
},
{
 "name": "Energy and Carbon Cost Accounting",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "demo_key": "k_carbon",
 "demo_data": {"kwh": 1850, "intensity": 0.42, "price_per_kwh": 0.12, "offset_per_tonne": 15},
 "description": ("The energy and carbon record prices the physical footprint: "
   "1,850 kWh at 0.42 kg CO2/kWh is 777 kg of CO2 monthly - about 0.78 "
   "tonnes - costing $222 in electricity at $0.12/kWh, with offsets at $15 "
   "a tonne adding $11.66. Energy is a real cost with two prices: the "
   "electricity bill and the carbon ledger. The record tracks both, because "
   "the second is increasingly the first (carbon pricing arrives by "
   "regulation or by customer requirement). The 1,850 kWh ties to the "
   "compute record's 1,850 vCPU-hours at roughly 1 kWh per vCPU-hour for "
   "this workload mix - the energy and compute records reconcile, as they "
   "must."),
 "how_it_works": ("Energy = vCPU-hours x kWh/vCPU-hour by workload class: "
   "1,850 kWh total. Carbon = kWh x grid intensity: 1,850 x 0.42 = 777 kg. "
   "Electricity cost = 1,850 x $0.12 = $222/month. Offset cost = 0.777 t x "
   "$15 = $11.66/month for carbon-neutral operations. Intensity uses the "
   "hosting region's published grid factor, updated annually - the record "
   "notes that moving compute to a 0.12-intensity region would cut carbon "
   "71% without changing the electricity bill much, and prices the "
   "migration. Efficiency KPI: kWh per million records, trended - the "
   "fleet's 5.37 kWh/M records this quarter, down 8% year over year from "
   "scheduling and rightsizing. The carbon ledger is reported alongside the "
   "dollar ledger in the dashboard; what gets measured gets managed applies "
   "to tonnes too."),
 "key_points": [
   "1,850 kWh x 0.42 kg/kWh = 777 kg CO2/month (0.78 tonnes).",
   "$222 electricity + $11.66 offsets monthly.",
   "Reconciles with the compute record (1 kWh per vCPU-hour here).",
   "Region move to 0.12 intensity would cut carbon 71% - priced.",
   "Efficiency: 5.37 kWh per million records, down 8% YoY.",
   "Carbon ledger reported alongside the dollar ledger.",
 ],
 "requirements": [
   "Energy metering by workload class.",
   "Grid intensity per region, updated annually.",
   "Compute-energy reconciliation.",
   "Efficiency KPI trended.",
 ],
 "standards": [
   "Published grid factors, not estimates.",
   "Offsets additional and verified (not double-counted).",
   "Region carbon considered in placement decisions.",
   "Reporting aligned with the financial ledger cadence.",
 ],
 "citations": [
   "GHG Protocol: Corporate Accounting and Reporting Standard (carbon accounting).",
 ],
 "sig_lens": ("The Signature Cost Doctrine counts the smoke as well as the "
   "coin: the doctrine requires the 777 kg on the ledger next to the $222. "
   "The Signature edition treats carbon as a cost with a coming price - "
   "a doctrine that prices only today's bill is budgeting for a world "
   "that no longer exists."),
},
{
 "name": "Cost Audit Record",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "demo_key": "k_facts",
 "demo_data": {"findings": 9, "recovered": 48000, "cost": 11400, "period": "2026",
               "checks": [["findings", "==", 9]]},
 "description": ("The cost audit record is the annual adversarial review of the "
   "whole accounting: 9 findings, $48,000 in misallocated costs recovered, "
   "$11,400 audit cost - a 4.2x return. The audit re-performs the ledger: "
   "recomputing unit costs from metering, re-footing allocations, verifying "
   "invoice reconciliation, sampling the anomaly detector's catches, and "
   "hunting the classic failure modes - committed capacity nobody uses, "
   "egress nobody meters, indexes nobody queries, tiers nobody reviews. The "
   "9 findings included a $31,000/year over-commitment on baseline compute "
   "and $12,000 in unallocated shared tooling. Findings get owners and "
   "dates; the audit is not complete until the findings close."),
 "how_it_works": ("The audit runs the failure-mode checklist: commitment "
   "coverage vs utilization, egress metering completeness, index usage, "
   "tiering currency, allocation model fitness, invoice reconciliation "
   "accuracy, anomaly detector precision, and budget process compliance. "
   "Each finding states the amount, the cause, the fix, and the owner - the "
   "$31,000 over-commitment: cause, baseline set from a peak month never "
   "repeated; fix, reduce commitment 40%; owner, platform lead; closed in 45 "
   "days. The $48,000 recovered is annualized run-rate savings from closed "
   "findings. The audit is performed by reviewers outside the cost "
   "accounting function - self-audit of money is an oxymoron. The report "
   "goes to engineering and finance leadership jointly, because cost "
   "accounting serves both."),
 "key_points": [
   "9 findings, $48,000 recovered, $11,400 cost - 4.2x return.",
   "Failure-mode checklist: commitments, egress, indexes, tiering, allocations.",
   "$31,000/year over-commitment: baseline set from an unrepeated peak.",
   "Findings get owners and dates; audit incomplete until findings close.",
   "Independent reviewers - self-audit of money is an oxymoron.",
   "Report to engineering and finance jointly.",
 ],
 "requirements": [
   "Annual audit with failure-mode checklist.",
   "Finding schema: amount, cause, fix, owner, date.",
   "Independent audit team.",
   "Closure tracking.",
 ],
 "standards": [
   "Findings quantified in annualized run-rate.",
   "Causes root-caused, not symptom-described.",
   "Leadership report within 30 days of fieldwork.",
   "Prior-year findings verified still fixed.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems.",
 ],
 "sig_lens": ("The Signature Cost Doctrine audits the accountants: the doctrine "
   "requires the ledger itself weighed annually, by independent hands. The "
   "Signature edition celebrates the $48,000 recovered - a doctrine that "
   "finds its own over-commitments is not embarrassed, it is validated. "
   "The audit that finds nothing audited nothing."),
},
{
 "name": "Budget Variance Record",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "demo_key": "k_variance",
 "demo_data": {"budget_yr": 60000, "actual_yr": 57200, "variance_pct": -4.67},
 "description": ("The budget variance record explains the gap between plan and "
   "reality: $60,000 annual budget vs $57,200 actual - 4.67% under, favorable. "
   "Variance analysis is where budgeting meets truth: the $2,800 favorable "
   "variance breaks into $1,900 from lower generation volumes (fewer records "
   "built than planned), $700 from the off-peak scheduling savings "
   "overperforming, and $200 from a rate decrease - each piece owned and "
   "explained. Unfavorable variances get the same treatment with remediation. "
   "The record's rule: every variance over 5% or $1,000 gets a written "
   "explanation; smaller ones are noted in aggregate. A variance unexplained "
   "is a budget unlearned from."),
 "how_it_works": ("Variance = (actual - budget)/budget: (57,200 - 60,000)/"
   "60,000 = -4.67%. The analysis decomposes by dimension and cause: "
   "generation -$1,900 (volume: 10,200 vs 11,476 planned records/month "
   "average), scheduling -$700 (off-peak share 84% vs 80% planned), rates "
   "-$200 (storage rate cut mid-year), offset by compute +$0 (exactly on "
   "plan). Favorable variances are not automatically good news: the $1,900 "
   "generation shortfall means 1,276 fewer records per run than the growth "
   "plan assumed - the savings cost growth. The record links each variance "
   "to its operational cause and, where the cause is a problem (missed "
   "growth), opens a follow-up. Year-to-date variance is reported monthly "
   "so December holds no surprises."),
 "key_points": [
   "$60,000 budget vs $57,200 actual = -4.67% (favorable).",
   "Decomposed: -$1,900 volume, -$700 scheduling, -$200 rates.",
   "Favorable is not automatically good: -$1,900 means missed growth.",
   "Variances over 5% or $1,000 get written explanations.",
   "YTD reported monthly - December holds no surprises.",
   "A variance unexplained is a budget unlearned from.",
 ],
 "requirements": [
   "Monthly YTD variance reporting.",
   "Decomposition by dimension and cause.",
   "Explanation threshold: 5% or $1,000.",
   "Follow-ups for problem-caused variances.",
 ],
 "standards": [
   "Favorable variances investigated, not celebrated blindly.",
   "Causes linked to operations.",
   "Thresholds published.",
   "Annual budget process informed by variance history.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (variance analysis).",
 ],
 "sig_lens": ("The Signature Cost Doctrine reads variances as the budget's "
   "report card with the teacher's comments: the doctrine requires every "
   "significant gap explained in writing. The Signature edition is "
   "suspicious of favorable variances - a steward under budget because "
   "the work did not get done has not saved money, they have deferred "
   "the mission."),
},
{
 "name": "Cost Optimization Playbook",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "demo_key": "k_facts",
 "demo_data": {"plays": 12, "implemented": 8, "saved_mo": 2140, "pipeline": 4,
               "checks": [["plays", "==", 12]]},
 "description": ("The cost optimization playbook is the catalog of proven ways "
   "to spend less: 12 plays, 8 implemented, $2,140 a month saved, 4 in the "
   "pipeline. Each play is a recipe with measured yield: rightsizing idle "
   "compute ($480/mo), tiering cold storage ($310/mo), off-peak scheduling "
   "($440/mo), cache expansion ($290/mo), index pruning ($95/mo), commitment "
   "tuning ($210/mo), egress reduction via CDN ($180/mo), and decommissioning "
   "the legacy pipeline ($135/mo). Plays are prioritized by savings per "
   "effort; the pipeline holds the next four with owners and dates. The "
   "playbook is the opposite of across-the-board cuts - it is surgery, not "
   "starvation, and every play proves its savings after implementation."),
 "how_it_works": ("Each play documents: the opportunity (with measurement), "
   "the action (step by step), the expected savings, the risk and rollback, "
   "and the verification method. Implementation is tracked: 8 done, savings "
   "verified by before/after metering - the $2,140 is measured, not "
   "projected. The 4 pipeline plays (reserved-instance marketplace, "
   "cross-region dedupe, query result caching, archival compression) have "
   "owners and target dates. Plays retire when their opportunity closes "
   "(the idle compute got rightsized - play done) and new plays are added "
   "from audit findings and anomaly patterns. The playbook is reviewed "
   "quarterly: implemented savings re-verified (savings decay as systems "
   "change), pipeline reprioritized. Anti-plays are listed too: the cuts "
   "that looked good and hurt - kept as warnings."),
 "key_points": [
   "12 plays, 8 implemented, $2,140/mo measured savings, 4 in pipeline.",
   "Top plays: rightsizing $480, scheduling $440, tiering $310, cache $290.",
   "Prioritized by savings per effort; pipeline has owners and dates.",
   "Savings verified by before/after metering - measured, not projected.",
   "Surgery, not starvation: every play proves its savings.",
   "Anti-plays listed: cuts that hurt, kept as warnings.",
 ],
 "requirements": [
   "Play schema: opportunity, action, savings, risk, rollback, verification.",
   "Implementation tracking with verified savings.",
   "Quarterly review with savings re-verification.",
   "Anti-play documentation.",
 ],
 "standards": [
   "No play without measured opportunity.",
   "Savings verified post-implementation.",
   "Risks and rollbacks mandatory.",
   "Pipeline always has next plays queued.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (optimization).",
 ],
 "sig_lens": ("The Signature Cost Doctrine keeps a surgeon's kit, not a "
   "butcher's cleaver: the doctrine requires each cut precise, measured, "
   "and proven. The Signature edition lists the anti-plays alongside - a "
   "doctrine that remembers its mistakes cuts wisely; one that forgets "
   "them cuts twice in the same place."),
},
{
 "name": "Cost Dashboard Exemplar",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "demo_key": "k_dashboard",
 "demo_data": {"panels": 8, "databases": 5000, "refresh": "daily", "alerts": 5},
 "description": ("The cost dashboard exemplar shows what good looks like: 8 "
   "panels across 5,000 databases, daily refresh, 5 active alerts. The "
   "panels: total spend with trend, spend by database (top 20 + rest), "
   "dimension breakdown, unit cost trends, budget vs actual, anomaly feed, "
   "optimization pipeline, and carbon ledger. Each panel answers a question "
   "a cost owner asks: are we on budget, what changed, what is next. The "
   "exemplar is prescriptive - layout, queries, thresholds - so every "
   "deployment starts from a working design. Five active alerts (two budget, "
   "two anomaly, one commitment expiry) show the dashboard is watched, "
   "because a dashboard nobody watches is wallpaper with numbers."),
 "how_it_works": ("The eight panels query the ledgers on daily refresh "
   "(intraday for the anomaly feed). Total spend shows the fleet number with "
   "its 13-week trend; the database panel ranks spend with per-record units; "
   "dimensions show the six-way split; unit trends show $/record over time "
   "per database; budget-vs-actual shows YTD variance; the anomaly feed "
   "lists open cost anomalies with owners; the pipeline panel tracks "
   "playbook plays and verified savings; the carbon panel shows kWh and "
   "tonnes alongside dollars. Thresholds match the published standards - "
   "80% budget alerts, anomaly sigmas, 2x playbook returns. Drill-down goes "
   "from fleet to database to dimension to invoice line. The exemplar "
   "includes the alert routing: who gets woken for what, because a "
   "dashboard that cannot wake anyone is a report, not a control."),
 "key_points": [
   "8 panels, 5,000 databases, daily refresh, 5 active alerts.",
   "Panels: total, by-database, dimensions, unit trends, budget, anomalies, pipeline, carbon.",
   "Prescriptive: layout, queries, thresholds included.",
   "Alert routing defined - a dashboard that cannot wake anyone is a report.",
   "Drill-down: fleet -> database -> dimension -> invoice line.",
   "Watched daily; wallpaper dashboards are decommissioned.",
 ],
 "requirements": [
   "All eight panels with documented queries.",
   "Daily refresh met; anomaly feed intraday.",
   "Alert routing with owners.",
   "Thresholds matching published standards.",
 ],
 "standards": [
   "Numbers reproducible from ledgers.",
   "Every panel has an owner and a review cadence.",
   "Unwatched dashboards decommissioned.",
   "Exemplar updated when standards change.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (reporting).",
 ],
 "sig_lens": ("The Signature Cost Doctrine treats the dashboard as the counting "
   "house window: the doctrine requires the books visible - totals, trends, "
   "alerts, carbon - to everyone with standing. The Signature edition "
   "decommissions wallpaper dashboards: a window nobody looks through is "
   "not transparency, it is glass."),
},
{
 "name": "Cost Self-Audit and Mastery Record",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "demo_key": "k_mastery",
 "demo_data": {"records": 34, "complete": 34, "ledgers_reconciled": 1.0, "stale_units": 0, "coverage": 1.0},
 "description": ("The cost self-audit and mastery record proves the accounting "
   "accounts for itself: thirty-four cost archetypes catalogued, thirty-four "
   "complete, ledgers reconciled 100%, zero stale unit costs, coverage one "
   "hundred percent. This is the record that closes the loop - the cost "
   "accounting system submitting its own books to its own audit. It verifies "
   "that every database has a current ledger, every unit cost is recomputed "
   "monthly, every allocation foots, and the governance overhead of the "
   "accounting itself is priced (it is, in the overhead record). A cost "
   "system that cannot price its own operation is a scale that refuses to "
   "weigh itself."),
 "how_it_works": ("The self-audit checks: ledger completeness (every database, "
   "current month), unit cost currency (recomputed within 35 days - zero "
   "stale in the example), allocation footing (pools foot to invoices), "
   "invoice reconciliation (within tolerance), anomaly detector health "
   "(precision in bounds), and budget process compliance. The example: 34 "
   "of 34 complete, 100% reconciled, zero stale units, coverage 1.0. "
   "Findings become playbook plays or audit findings, tracked to closure. "
   "The audit runs quarterly with its report to finance and engineering "
   "leadership. This record is also the mastery checkpoint: a reader who "
   "understands all thirty-four records - from unit costs through allocation "
   "to TCO and carbon - understands database cost accounting end to end."),
 "key_points": [
   "34 archetypes, 34 complete; 100% reconciled; 0 stale units; coverage 1.0.",
   "Self-audit checks ledgers, units, allocations, reconciliation, detectors.",
   "Findings become playbook plays or audit findings.",
   "Runs quarterly; report to finance and engineering.",
   "A scale that refuses to weigh itself cannot be trusted.",
   "Mastery checkpoint: all 34 records teach cost accounting end to end.",
 ],
 "requirements": [
   "Self-audit executed quarterly with published report.",
   "All six audit dimensions checked.",
   "Findings tracked to closure.",
   "Mastery path documented from record 1 to record 34.",
 ],
 "standards": [
   "Coverage target 1.0.",
   "Zero stale unit costs tolerated.",
   "Audit independent of daily operations.",
   "Year-over-year trend reported.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems.",
 ],
 "sig_lens": ("The Signature Cost Doctrine ends where it began: with every "
   "dollar accounted, including the dollars spent on the accounting. The "
   "Signature self-audit weighs the scale itself - and the mastery record "
   "is the proof that the whole teaching holds together, simple to "
   "complex, without a gap."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks) == list(range(1, 35)), "ladder ranks must be 1..34 in order"
