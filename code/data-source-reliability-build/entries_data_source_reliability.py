#!/usr/bin/env python3
"""Entries for the Data Source Reliability databases (JAH Databases
governance track, group F, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); ID prefixes JAH-DSR- (public) and
JAH-DSRS- (signature) verified free: zero exact or substring hits in
manifest id_prefix values and zero hits in all shard record IDs of
jah-databases-data-1. All 68 record titles checked against the whole
system (exact dedupe index + live shard title corpus of 1,143,457 titles)
BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  data-source-reliability           - The Data Source Reliability Database
      (public-harvest: real, fact-checked reliability knowledge - source
      history, correction rates, independent corroboration, known
      limitations, reputation scores, provenance, freshness, citation
      practice, agreement analysis, bias assessment, retraction handling,
      survey/sensor/derived/expert/archival reliability, composite indexes,
      decay, adversarial detection, confidence calibration, weighted
      consensus, audit trails, monitoring, baselines, dispute resolution,
      certification, dashboards)
  data-source-reliability-signature - The Data Source Reliability Signature
      Database (the Signature Reliability Doctrine; src signature, titles
      suffixed " (Signature Edition)", never presented as authentic public
      record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_data_source_reliability.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - the Signature Reliability Doctrine: every "
            "source weighed, every claim corroborated, every correction logged "
            "in the open; reputation earned in public and spent carefully. "
            "Clearly labeled Signature-made, never presented as an authentic "
            "public record. Property of Justin Addam Higgins (JAH).")

ENTRIES = [
# ---------------- Foundations (1-10) ----------------
{
 "name": "Source Reliability Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "demo_key": "r_facts",
 "demo_data": {"dimensions": 5, "source_types": 8, "score_scale": 100, "review_cadence_days": 180,
               "checks": [["dimensions", "==", 5], ["score_scale", "==", 100]]},
 "description": ("The source reliability overview defines the five dimensions on which every "
   "source is scored: history (how long it has published and how it behaved), correction rate "
   "(how often it fixes itself), corroboration (whether independent sources agree), "
   "limitations (what it cannot know), and reputation (what the record says about it). "
   "Reliability is not a feeling about a source - it is a measured property, scored zero to "
   "one hundred, reviewed every one hundred eighty days. A source that scores well on four "
   "dimensions but hides its limitations is not reliable; it is merely persuasive. This "
   "database treats every source the same way: weighed in public, with the scale visible."),
 "how_it_works": ("Each source gets one reliability record carrying the five dimension scores, "
   "the evidence behind each score, and the composite. History is measured in years of "
   "continuous publication and in behavior during known stress events. Correction rate is "
   "corrections per thousand records published. Corroboration counts independent sources "
   "confirming the same facts. Limitations are listed explicitly - every source has them. "
   "Reputation aggregates peer assessments and the source's own correction transparency. The "
   "composite is the weighted mean, and the weights themselves are published so the score can "
   "be audited. Scores are recomputed on the one-hundred-eighty-day cadence and whenever a "
   "major correction or retraction lands."),
 "key_points": [
   "Five scored dimensions: history, correction rate, corroboration, limitations, reputation.",
   "Scores run zero to one hundred; the weighting formula is published and auditable.",
   "One-hundred-eighty-day review cadence plus event-driven rescoring.",
   "A source hiding its limitations is persuasive, not reliable.",
   "Every score carries its evidence - no black-box ratings.",
   "Eight source types covered: surveys, sensors, archives, experts, derived, machine, primary, secondary.",
 ],
 "requirements": [
   "Every source scored on all five dimensions before being cited as reliable.",
   "Evidence recorded per dimension score.",
   "Weighting formula published with the scores.",
   "Rescoring on schedule and on major corrections.",
 ],
 "standards": [
   "Scores are point-in-time: each carries its computation date.",
   "Dimension definitions fixed across sources for comparability.",
   "Corrections improve the correction-rate dimension - honesty is rewarded.",
   "No source exempt from the limitations dimension.",
 ],
 "citations": [
   "Ioannidis, J. P. A. Why most published research findings are false. PLoS Medicine 2(8): e124, 2005 (reliability of published findings).",
   "W3C PROV Overview: An Overview of the PROV Family of Documents. W3C, 2013 (provenance modeling).",
 ],
 "sig_lens": ("The Signature Reliability Doctrine opens with a scale, not a gavel: every source "
   "is weighed, none is worshipped. The Signature edition insists the scale itself be "
   "inspectable - a secret formula is just another unweighed claim."),
},
{
 "name": "Source History Record",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "demo_key": "r_history",
 "demo_data": {"years": 24, "stress_events": 6, "passed": 5, "corrections": 41, "records": 12000,
               "checks": [["years", ">=", 10]]},
 "description": ("The source history record is the biography of a source: twenty-four years of "
   "continuous publication, six major stress events weathered, five handled well, forty-one "
   "corrections across twelve thousand records. History matters because reliability is "
   "demonstrated, not declared - a source that corrected itself publicly through past crises "
   "has earned a presumption that a newcomer has not. The record lists founding date, "
   "ownership changes, methodology changes, past crises and how they were handled, and the "
   "full correction log. A source with no history is not unreliable by default, but it is "
   "unproven, and the record says so plainly."),
 "how_it_works": ("The record opens with the source's founding date and a timeline of material "
   "changes: ownership transfers, methodology revisions, scope expansions. Each of the six "
   "stress events - elections, disasters, market shocks, pandemics in the example - gets an "
   "entry: what happened, what the source published, what it got wrong, and how fast it "
   "corrected. The correction log lists all forty-one corrections with dates and severity. "
   "The history score derives from longevity (twenty-four years), crisis performance (five of "
   "six handled well), and correction transparency (every correction logged, none silent). "
   "Ownership changes reset portions of the score, because a source under new ownership is "
   "partly a new source."),
 "key_points": [
   "Biography of a source: 24 years, 6 stress events, 5 handled well.",
   "41 corrections across 12,000 records - all logged, none silent.",
   "Reliability is demonstrated, not declared.",
   "Ownership changes partly reset the history score.",
   "No history means unproven, not unreliable - stated plainly.",
   "Methodology changes dated - the source of 2010 may differ from the source of 2026.",
 ],
 "requirements": [
   "Founding date and ownership timeline documented.",
   "Stress-event entries with published-vs-correct accounting.",
   "Complete correction log with dates and severity.",
   "Methodology changes dated and described.",
 ],
 "standards": [
   "History claimed only with evidence - dates, events, corrections.",
   "Silent corrections count against the score, not for it.",
   "Crisis performance judged by correction speed and honesty, not by being right first.",
   "Records updated when ownership or methodology changes.",
 ],
 "citations": [
   "Committee on Publication Ethics (COPE): Retraction Guidelines (correction transparency practice).",
 ],
 "sig_lens": ("The Signature edition reads a source's history the way a banker reads a credit "
   "file: length of account, behavior under stress, honesty about mistakes. The Signature "
   "doctrine holds that the forty-one logged corrections are the strongest line in the "
   "record - a source that shows its scars can be trusted with sharp tools."),
},
{
 "name": "Correction Rate Metric",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "demo_key": "r_rate",
 "demo_data": {"corrections": 41, "records": 12000, "major": 3, "minor": 38, "band": "healthy"},
 "description": ("The correction rate metric states how often a source fixes itself: forty-one "
   "corrections across twelve thousand records is 3.42 per thousand - three major, thirty-eight "
   "minor - squarely in the healthy band. Counterintuitively, a zero correction rate is a "
   "warning sign, not a badge: no source is perfect, so zero corrections means corrections are "
   "being hidden. The metric distinguishes major corrections (wrong conclusions, wrong numbers "
   "that change meaning) from minor ones (typos, clarifications), because a source with three "
   "major corrections per thousand is a different animal from one with forty minor ones."),
 "how_it_works": ("The rate is corrections divided by records published, expressed per thousand "
   "for readability: 41/12000 x 1000 = 3.42. Major and minor corrections are tracked "
   "separately - the example shows 3 major and 38 minor. Bands are set per source type: "
   "breaking-news sources correct more than reference works, and the band accounts for that. "
   "The trend matters more than the snapshot: a rising major-correction rate triggers review, "
   "while a steady minor rate with fast correction times signals a healthy operation. "
   "Correction speed is measured too - median hours from error to published correction - "
   "because a correction issued in two hours and one issued in two months are different "
   "behaviors with the same rate."),
 "key_points": [
   "41 corrections / 12,000 records = 3.42 per thousand (3 major, 38 minor).",
   "Zero correction rate is a warning sign - perfection means hidden corrections.",
   "Major vs minor tracked separately - they mean different things.",
   "Bands set per source type; trends matter more than snapshots.",
   "Correction speed measured: median hours from error to published fix.",
   "Rising major-correction rate triggers review.",
 ],
 "requirements": [
   "Correction counts with major/minor severity classification.",
   "Denominator (records published) recorded for the same period.",
   "Correction timestamps for speed measurement.",
   "Bands documented per source type.",
 ],
 "standards": [
   "Corrections counted from the public log - unlogged fixes do not count as corrections.",
   "Severity classification rules written and applied consistently.",
   "Rates recomputed on the review cadence.",
   "Comparisons only within source type - never across types.",
 ],
 "citations": [
   "Committee on Publication Ethics (COPE): Retraction Guidelines.",
   "Ioannidis, J. P. A. Why most published research findings are false. PLoS Medicine, 2005.",
 ],
 "sig_lens": ("The Signature Reliability Doctrine celebrates the correction: the Signature "
   "edition scores a source higher for its forty-one public corrections than for a claimed "
   "zero, because the doctrine measures integrity by the repair log, not by the shine. A "
   "source that never errs in public is either divine or dishonest, and the doctrine does "
   "not believe in divine sources."),
},
{
 "name": "Independent Corroboration Count",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "demo_key": "r_quorum",
 "demo_data": {"claim": "Q3 manufacturing output rose 2.1%", "independent": 4, "required": 3, "total_citing": 11, "shared_lineage": 2},
 "description": ("The independent corroboration count answers 'who else says so': four genuinely "
   "independent sources confirm the claim, against a requirement of three, out of eleven "
   "total citations - two of which share lineage and do not count. Corroboration only works "
   "when the sources are actually independent: eleven outlets repeating one wire report is "
   "one source wearing eleven hats. The record traces each citation to its origin, discards "
   "the ones that trace back to the same root, and counts what remains. Four independent "
   "confirmations of a quantitative claim is strong; one is a rumor with a byline."),
 "how_it_works": ("For each significant claim, the record lists every citing source and traces "
   "its provenance: did it do original reporting, or did it cite another source? The example "
   "claim - Q3 manufacturing output rose 2.1% - drew eleven citations, but two traced to the "
   "same wire-service lineage and were excluded, leaving nine candidates, of which four were "
   "genuinely independent (separate data collection, separate analysis). The requirement is "
   "three independent confirmations for quantitative claims, two for qualitative ones. "
   "Corroboration strength also weighs agreement quality: four sources agreeing on 2.1% is "
   "stronger than four sources agreeing on 'rose somewhat.' Disagreements are recorded too - "
   "a credible source disputing the claim blocks corroboration until resolved."),
 "key_points": [
   "4 independent confirmations vs 3 required; 11 citations traced, 2 shared lineage excluded.",
   "Independence traced to origin - one wire report repeated eleven times is one source.",
   "Quantitative claims need 3 independent confirmations; qualitative need 2.",
   "Agreement quality weighed: '2.1%' beats 'rose somewhat.'",
   "Credible disputes block corroboration until resolved.",
   "One confirmation is a rumor with a byline.",
 ],
 "requirements": [
   "Citation tracing to origin for significant claims.",
   "Lineage analysis excluding shared-root citations.",
   "Corroboration thresholds documented per claim type.",
   "Disputes recorded and resolved before counting.",
 ],
 "standards": [
   "Independence defined as separate data collection or separate analysis.",
   "Press-release repetition never counts as corroboration.",
   "Thresholds published; exceptions documented with rationale.",
   "Corroboration recomputed when new evidence arrives.",
 ],
 "citations": [
   "Cochrane Handbook for Systematic Reviews of Interventions, Chapter 7 (assessing evidence independence).",
 ],
 "sig_lens": ("The Signature doctrine treats corroboration as witness law: one witness is a "
   "story, three independent witnesses are evidence, and eleven parrots are still one "
   "witness. The Signature edition requires the lineage traced - a witness who only heard it "
   "from the first witness does not count."),
},
{
 "name": "Known Limitations Register",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "demo_key": "r_facts",
 "demo_data": {"limitations": 7, "categories": ["coverage","method","timeliness","access","bias","granularity","lineage"],
               "reviewed": "2026-09-15",
               "checks": [["limitations", "==", 7]]},
 "description": ("The known limitations register is the list of what a source cannot do: seven "
   "documented limitations across coverage, method, timeliness, access, bias, granularity, and "
   "lineage - reviewed 2026-09-15. Every source has boundaries: the survey that cannot reach "
   "rural respondents, the sensor network with winter gaps, the archive missing a decade, the "
   "expert whose expertise stops at the border of their field. A source that lists its "
   "limitations can be used correctly; a source that hides them will be used wrongly. The "
   "register makes the boundaries explicit so users stay inside them."),
 "how_it_works": ("Each limitation is recorded with its category, a plain-language description, "
   "the affected use cases, and any available quantification - for example, 'rural coverage "
   "below 40% of target population' rather than 'limited rural coverage.' The seven categories "
   "ensure completeness: coverage (who/what is missing), method (how the data was gathered "
   "and its weaknesses), timeliness (how stale it can be), access (what is paywalled or "
   "restricted), bias (systematic skews), granularity (how fine the detail goes), and lineage "
   "(where the data came from before this source). New limitations are added when discovered - "
   "finding a limitation is a contribution, not an accusation. The register is reviewed with "
   "every reliability rescoring."),
 "key_points": [
   "7 limitations documented across 7 categories; reviewed 2026-09-15.",
   "Quantified where possible: 'rural coverage below 40%' beats 'limited coverage.'",
   "Categories: coverage, method, timeliness, access, bias, granularity, lineage.",
   "Limitations make correct use possible; hidden limits guarantee misuse.",
   "Discovering a limitation is a contribution, not an accusation.",
   "Reviewed with every rescoring.",
 ],
 "requirements": [
   "Limitation entries with category, description, affected uses, quantification.",
   "All seven categories considered for every source.",
   "Review date current.",
   "New limitations added on discovery.",
 ],
 "standards": [
   "Plain language - limitations must be understandable by non-specialists.",
   "No 'none known' without evidence of looking.",
   "Limitations referenced in every reliability summary of the source.",
   "Retired limitations kept in history with retirement reason.",
 ],
 "citations": [
   "W3C PROV Overview, 2013 (lineage as a limitation dimension).",
 ],
 "sig_lens": ("The Signature Reliability Doctrine holds that a source's limitations are part of "
   "its identity, not a defect in it: the Signature edition requires the register to be as "
   "prominent as the score. A scale that hides what it cannot weigh is a rigged scale."),
},
{
 "name": "Reputation Score Model",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "demo_key": "r_weighted",
 "demo_data": {"history": 82, "correction": 76, "corroboration": 88, "limitations": 90, "peer": 84,
               "weights": [0.25, 0.25, 0.2, 0.15, 0.15]},
 "description": ("The reputation score model combines the five dimension scores into one number: "
   "history 82, correction 76, corroboration 88, limitations 90, peer assessment 84 - weighted "
   "25/25/20/15/15 for a composite of 83.2. The weights encode a judgment: history and "
   "correction behavior matter most, because they are the hardest to fake. Limitations "
   "transparency is scored high when the register is complete - honesty about boundaries is "
   "reputation-positive. Peer assessment aggregates ratings from domain practitioners, "
   "outlier-trimmed so one enthusiastic or hostile rater cannot swing the score. The model is "
   "published in full: inputs, weights, and arithmetic, so anyone can recompute the score."),
 "how_it_works": ("The composite is the weighted mean: 82x0.25 + 76x0.25 + 88x0.20 + 90x0.15 + "
   "84x0.15 = 83.2. Each dimension score itself derives from measured evidence - the history "
   "score from longevity and crisis performance, the correction score from rate and speed, and "
   "so on. Peer assessment uses trimmed means of practitioner ratings with rater identity "
   "recorded (anonymous ratings are down-weighted). The model version is recorded with the "
   "score because weights evolve; a score of 82.6 under model v3 is not comparable to 82.6 "
   "under v2. Sensitivity analysis is published: which dimension moves the composite most, so "
   "gaming attempts are visible. Scores below 40 trigger enhanced scrutiny; below 25 the "
   "source is not cited for factual claims."),
 "key_points": [
   "Composite 83.2 from 82/76/88/90/84 weighted 25/25/20/15/15.",
   "History and correction behavior weighted highest - hardest to fake.",
   "Limitations transparency is reputation-positive.",
   "Peer ratings outlier-trimmed; anonymous ratings down-weighted.",
   "Model version recorded with every score; sensitivity analysis published.",
   "Below 40: enhanced scrutiny; below 25: not cited for facts.",
 ],
 "requirements": [
   "All five dimension scores with evidence.",
   "Model version and weights recorded.",
   "Peer ratings with rater identity and trimming rule.",
   "Sensitivity analysis available.",
 ],
 "standards": [
   "Weights sum to 1.0 and are published.",
   "Scores recomputed, never carried forward silently.",
   "Model changes versioned with migration notes.",
   "No single rater above 10% influence on peer dimension.",
 ],
 "citations": [
   "Ioannidis, J. P. A. Why most published research findings are false. PLoS Medicine, 2005.",
 ],
 "sig_lens": ("The Signature edition treats the reputation model as a public mint: it stamps "
   "the coin, but everyone may assay the metal. The Signature doctrine requires the weights "
   "published because a secret scoring formula is not a measurement - it is an opinion with "
   "arithmetic."),
},
{
 "name": "Primary vs Secondary Source Classification",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "demo_key": "r_facts",
 "demo_data": {"primary_pct": 62, "secondary_pct": 38, "rules": 6,
               "checks": [["rules", "==", 6]]},
 "description": ("The primary vs secondary classification sorts sources by closeness to the "
   "event: primary sources observed it directly - the sensor reading, the court transcript, "
   "the survey response - while secondary sources report on it - the article about the study, "
   "the summary of the data. In the example corpus, sixty-two percent of citations are "
   "primary, thirty-eight secondary. Primary is not automatically better: a sloppy primary "
   "source loses to a careful secondary analysis. But the classification matters because "
   "errors compound with distance - each retelling adds its own misunderstandings, and a "
   "claim three retellings from its origin is a game of telephone."),
 "how_it_works": ("Six classification rules decide primary vs secondary: direct observation or "
   "measurement (primary), contemporaneous record created by a participant (primary), later "
   "analysis of primary material (secondary), reporting that cites other reporting "
   "(secondary), compiled data with documented methodology (primary for the compilation, "
   "secondary for the underlying), and machine-generated summaries (secondary, always). "
   "Mixed sources are split: the dataset is primary, the accompanying editorial is secondary. "
   "The classification is recorded per citation, and reliability scoring weights primary "
   "evidence more heavily for factual claims while valuing secondary sources for analysis and "
   "context. Tertiary sources - encyclopedias, textbooks - are classified secondary and used "
   "for orientation, never as the sole support for a contested claim."),
 "key_points": [
   "Primary observed directly; secondary reports on it; 62%/38% in the example corpus.",
   "Primary is not automatically better - sloppy primary loses to careful secondary.",
   "Errors compound with distance: three retellings is a game of telephone.",
   "Six classification rules; mixed sources split by component.",
   "Machine-generated summaries are always secondary.",
   "Tertiary sources orient, never solely support contested claims.",
 ],
 "requirements": [
   "Classification recorded per citation with the rule applied.",
   "Mixed sources split by component.",
   "Distance-from-origin counted for chains of reporting.",
   "Tertiary use flagged where it occurs.",
 ],
 "standards": [
   "Contested factual claims need primary support or multiple independent secondaries.",
   "Classification rules applied consistently across the corpus.",
   "Reclassification when new provenance information arrives.",
   "Machine summaries never cited as primary.",
 ],
 "citations": [
   "Cochrane Handbook for Systematic Reviews of Interventions (primary evidence hierarchy).",
   "ISO 15489-1:2016 Records management (records as primary evidence).",
 ],
 "sig_lens": ("The Signature doctrine measures distance from the event the way a surveyor "
   "measures distance from the benchmark: every retelling is a measurement with its own "
   "error, and errors accumulate. The Signature edition requires the chain counted - a claim "
   "should know how far it has traveled."),
},
{
 "name": "Provenance Capture Standard",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "demo_key": "r_provenance",
 "demo_data": {"links": 5, "verified": 5, "gaps": 0, "model": "W3C PROV",
               "checks": [["verified", "==", 5], ["gaps", "==", 0]]},
 "description": ("The provenance capture standard requires every record to carry its chain of "
   "custody: who created it, who transformed it, and who published it - five links in the "
   "example chain, all five verified, zero gaps. Provenance answers 'where did this come "
   "from' with names and dates, not vibes. A record with a gap in its chain - data that "
   "appeared from nowhere - is treated as unprovenanced and scored accordingly. The standard "
   "follows the W3C PROV model: entities (the data), activities (what was done), and agents "
   "(who did it), linked so the whole history can be walked."),
 "how_it_works": ("Each record stores its provenance as a PROV chain: the original entity with "
   "its creator agent and creation activity, then each derivation - cleaning, aggregation, "
   "analysis - as an activity linking input entities to output entities with the responsible "
   "agent and the software version used. The example chain has five links: sensor capture, "
   "transmission, cleaning, aggregation, publication - each verified against the agent's own "
   "records. Verification means checking each link with its claimed agent, not just reading "
   "the chain's own assertions. Gaps - links that cannot be verified - are flagged and reduce "
   "the provenance score proportionally. Chains are immutable once published: corrections add "
   "new links, they never rewrite old ones."),
 "key_points": [
   "Chain of custody: creator, transformers, publisher - 5 links, 5 verified, 0 gaps.",
   "W3C PROV model: entities, activities, agents.",
   "Gaps flagged; unprovenanced records scored accordingly.",
   "Verification checks each link with its claimed agent.",
   "Chains immutable: corrections add links, never rewrite.",
   "Software versions recorded for every transformation.",
 ],
 "requirements": [
   "PROV chain stored with every record.",
   "Each link verifiable with its agent.",
   "Gaps flagged explicitly, never silently passed.",
   "Immutability enforced on published chains.",
 ],
 "standards": [
   "W3C PROV-DM for the data model.",
   "Timestamps in UTC with source timezone noted.",
   "Agent identity resolved, not just named.",
   "Derivation software versioned and recorded.",
 ],
 "citations": [
   "W3C PROV Overview: An Overview of the PROV Family of Documents. W3C, 2013.",
   "W3C PROV-DM: The PROV Data Model. W3C, 2013.",
 ],
 "sig_lens": ("The Signature edition treats provenance as the chain on a historical artifact: "
   "each owner recorded, each transfer witnessed. The Signature doctrine holds that an "
   "unbroken chain is what turns data into evidence - without it, even true numbers are "
   "just rumors with decimals."),
},
{
 "name": "Freshness Metric",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "demo_key": "r_fresh",
 "demo_data": {"age_days": 45, "half_life_days": 90, "domain": "economic indicators"},
 "description": ("The freshness metric scores how much a record's age has eroded its value: "
   "forty-five days old against a ninety-day half-life in economic indicators scores 0.707 - "
   "about seventy-one percent of full freshness. Freshness is domain-relative: yesterday's "
   "weather report is stale, but a ten-year-old geological survey is fresh. The metric uses "
   "exponential decay with a per-domain half-life - the time after which a record is worth "
   "half its original value for decision-making. A record past four half-lives (six percent "
   "freshness) is archival: useful for history, not for current decisions."),
 "how_it_works": ("Freshness = 0.5^(age/half-life): the example computes 0.5^(45/90) = 0.707. "
   "Half-lives are set per domain by expert judgment and reviewed annually: economic "
   "indicators ninety days, technology product data one hundred eighty days, demographic "
   "data two years, geological data twenty years. The metric drives refresh scheduling - "
   "records below 0.5 freshness are flagged for update - and it gates use: automated systems "
   "refuse to decide on records below the domain's freshness floor. Publication date is "
   "distinguished from observation date: a report published today about last year's survey "
   "has the survey's age, not today's. Estimated dates are flagged, because freshness "
   "computed from a guessed date is itself a guess."),
 "key_points": [
   "Freshness = 0.5^(age/half-life); example: 45 days / 90-day half-life = 0.707.",
   "Half-lives per domain: economic 90d, tech 180d, demographic 2y, geological 20y.",
   "Below 0.5: flagged for refresh; below floor: automated systems refuse to decide.",
   "Observation date rules, not publication date.",
   "Past four half-lives (6%): archival - history, not current decisions.",
   "Estimated dates flagged - freshness from a guess is a guess.",
 ],
 "requirements": [
   "Half-life documented per domain with review date.",
   "Observation dates recorded separately from publication dates.",
   "Freshness computed and stored with each record.",
   "Refresh flags acted on within the domain's SLA.",
 ],
 "standards": [
   "Exponential decay model applied uniformly within a domain.",
   "Half-lives reviewed annually by domain experts.",
   "Freshness floors published per domain for automated use.",
   "Stale-data use logged and justified.",
 ],
 "citations": [
   "American Statistical Association statement on p-values (2016) - on the decay of evidentiary value, by analogy.",
 ],
 "sig_lens": ("The Signature doctrine treats freshness as the ripeness of fruit: the metric "
   "does not moralize about age, it measures it. The Signature edition requires the "
   "half-life stated openly - a source that pretends its ten-year-old numbers are fresh is "
   "selling last season's harvest as today's."),
},
{
 "name": "Citation Practice Standard",
 "group": "Foundations", "ladder_rank": 10, "ladder_tier": "foundations",
 "demo_key": "r_facts",
 "demo_data": {"required_elements": 6, "style": "author-date", "link_check_days": 30,
               "checks": [["required_elements", "==", 6]]},
 "description": ("The citation practice standard defines what a proper citation contains: six "
   "required elements - author, date, title, publisher, locator, and access date for online "
   "sources - in author-date style, with links rechecked every thirty days. Citations are "
   "the load-bearing walls of reliability: a claim without a checkable citation is an "
   "assertion, and an assertion with a dead link is an assertion with a rumor of support. "
   "The standard requires citations to be specific enough that a stranger can find the exact "
   "passage - page, section, or timestamp - because 'see the report' is not a citation."),
 "how_it_works": ("Every citation carries the six elements: who wrote it, when, what it is "
   "called, who published it, where to find it (DOI, URL, or archive reference), and when it "
   "was accessed for online sources. Online citations get link-checked every thirty days; "
   "dead links trigger archival lookup, and if no archive exists, the citation is flagged "
   "degraded. Quotations are verified against the source - misquotation is treated as a "
   "reliability incident. Secondary citations ('cited in') are marked as such and never "
   "presented as direct consultation. The standard also covers data citations: datasets get "
   "versioned DOIs, and the exact version used is recorded, because datasets change."),
 "key_points": [
   "Six required elements: author, date, title, publisher, locator, access date.",
   "Specific enough for a stranger to find the exact passage.",
   "Links rechecked every 30 days; dead links trigger archival lookup.",
   "Misquotation treated as a reliability incident.",
   "'Cited in' marked as such - never presented as direct consultation.",
   "Datasets cited by versioned DOI with the exact version recorded.",
 ],
 "requirements": [
   "All six elements present for every citation.",
   "Link-check cadence documented and executed.",
   "Quotation verification for direct quotes.",
   "Dataset versions pinned.",
 ],
 "standards": [
   "Author-date style for consistency.",
   "Archival copies preferred for volatile online sources.",
   "Degraded citations flagged, not silently kept.",
   "Citation audits sample records quarterly.",
 ],
 "citations": [
   "ISO 690:2021 Information and documentation - Guidelines for bibliographic references.",
 ],
 "sig_lens": ("The Signature edition treats a citation as a sworn address: 'you will find the "
   "evidence at this place, on this date, in these words.' The Signature doctrine requires "
   "the address to be real - a citation that cannot be followed is not a citation, it is a "
   "bluff."),
},
# ---------------- Compounded (11-21) ----------------
{
 "name": "Cross-Source Agreement Analysis",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "demo_key": "r_agree",
 "demo_data": {"sources": 6, "agree": 5, "values": [2.1, 2.0, 2.2, 2.1, 1.9, 3.4], "outlier": 3.4},
 "description": ("The cross-source agreement analysis measures how tightly independent sources "
   "cluster: six sources, five agreeing, values 2.1, 2.0, 2.2, 2.1, 1.9 - and one outlier at "
   "3.4. Agreement is quantified, not vibed: the spread of reported values, the count within "
   "tolerance, and the treatment of outliers. Five sources within 0.3 points is strong "
   "agreement; the 3.4 is investigated, not averaged away, because an outlier is either a "
   "better measurement or a worse one, and the analysis must determine which. The record "
   "states the agreement metric, the tolerance, and the outlier disposition."),
 "how_it_works": ("The analysis collects the reported values from all independent sources on "
   "the same fact, computes the median (2.1 in the example) and the median absolute deviation, "
   "and counts sources within the tolerance band (five of six within 0.3). The outlier at 3.4 "
   "is investigated: its methodology reviewed, its provenance checked, its history consulted. "
   "If the outlier's method is sound and newer, the consensus shifts; if it is flawed, it is "
   "excluded with rationale. The agreement score is the in-tolerance fraction weighted by "
   "source reliability: 5/6 = 0.833, adjusted by the sources' individual scores. Persistent "
   "disagreement across reliable sources is itself a finding - it means the fact is contested, "
   "and the record says so instead of manufacturing consensus."),
 "key_points": [
   "6 sources, 5 within tolerance (2.1, 2.0, 2.2, 2.1, 1.9); outlier 3.4 investigated.",
   "Agreement quantified: median, median absolute deviation, in-tolerance fraction.",
   "Outliers investigated, never averaged away.",
   "Score 0.833 weighted by individual source reliability.",
   "Persistent disagreement among reliable sources is a finding: the fact is contested.",
   "Consensus never manufactured - disagreement is recorded.",
 ],
 "requirements": [
   "Value collection from all independent sources on the fact.",
   "Tolerance band documented per fact type.",
   "Outlier investigation with disposition rationale.",
   "Agreement score with weighting method.",
 ],
 "standards": [
   "Medians preferred over means - robust to outliers.",
   "Tolerance bands set before seeing the values.",
   "Exclusions require written rationale.",
   "Contested facts labeled contested.",
 ],
 "citations": [
   "Cochrane Handbook for Systematic Reviews of Interventions (heterogeneity assessment).",
 ],
 "sig_lens": ("The Signature doctrine treats agreement as a chorus: the analysis listens for "
   "harmony, but it also listens for the one voice singing a different note - because "
   "sometimes that voice is wrong, and sometimes it is the only one that is right. The "
   "Signature edition requires the outlier's song to be heard fully before it is judged."),
},
{
 "name": "Correction Lag Measurement",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "demo_key": "r_lag",
 "demo_data": {"lags_h": [2, 5, 1, 48, 3, 12, 7, 96, 4, 9], "threshold_h": 24},
 "description": ("The correction lag measurement tracks how fast a source fixes its errors: ten "
   "corrections with lags of 2, 5, 1, 48, 3, 12, 7, 96, 4, and 9 hours - median 6 hours, two "
   "beyond the twenty-four-hour threshold. Speed matters because an uncorrected error keeps "
   "misleading everyone who reads it in the meantime; a correction issued in two hours "
   "limits the damage, while one issued in ninety-six hours means four days of readers got "
   "the wrong facts. The record reports the median lag, the ninetieth percentile, and the "
   "fraction beyond threshold, because the tail - the slowest corrections - is where the "
   "damage concentrates."),
 "how_it_works": ("Lag is measured from the later of publication time or the time the error "
   "became knowable, to the publication time of the correction. The example's ten lags sort "
   "to 1, 2, 3, 4, 5, 7, 9, 12, 48, 96 - median 6 hours, ninetieth percentile 96 hours, two "
   "of ten (twenty percent) beyond the twenty-four-hour threshold. Major corrections are "
   "tracked separately from minor: a typo fixed in a week is fine, a wrong conclusion fixed "
   "in a week is not. The lag distribution feeds the correction dimension of the reputation "
   "score, and sources with chronic slow major corrections get their correction score capped "
   "regardless of rate. Improvement is credited: a source that halves its median lag year "
   "over year is improving, and the record shows the trend."),
 "key_points": [
   "10 lags: median 6h, p90 96h, 20% beyond the 24h threshold.",
   "Lag measured from error-knowable to correction-published.",
   "Major and minor corrections tracked separately.",
   "The tail (slowest corrections) is where damage concentrates.",
   "Chronic slow major corrections cap the correction score.",
   "Improvement trends credited year over year.",
 ],
 "requirements": [
   "Lag timestamps for every correction.",
   "Major/minor severity classification.",
   "Threshold documented per source type.",
   "Trend reported alongside the snapshot.",
 ],
 "standards": [
   "Median and ninetieth percentile reported, not just the mean.",
   "Thresholds published before measurement.",
   "Knowable-time defined consistently (not publication time when earlier knowledge existed).",
   "Slow corrections investigated, not just counted.",
 ],
 "citations": [
   "Committee on Publication Ethics (COPE): Retraction Guidelines.",
 ],
 "sig_lens": ("The Signature Reliability Doctrine measures a source's character by its repair "
   "speed: the Signature edition honors the two-hour correction and interrogates the "
   "ninety-six-hour one. The doctrine holds that everyone errs, but the honorable correct "
   "quickly - delay in admitting error is itself a kind of error."),
},
{
 "name": "Source Bias Assessment",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "demo_key": "r_bias",
 "demo_data": {"dimensions": ["selection","framing","omission","sourcing"], "scores": [0.2, 0.35, 0.15, 0.1], "verdict": "low-moderate"},
 "description": ("The source bias assessment names the systematic skews in a source: selection "
   "0.2, framing 0.35, omission 0.15, sourcing 0.1 - verdict low-moderate. Bias is not "
   "accusation; it is measurement. Every source selects (what to cover), frames (how to "
   "present), omits (what to leave out), and sources (whom to ask) - the question is never "
   "'is it biased' but 'how, and how much.' A source with measured, disclosed bias can be "
   "used correctly by compensating readers; a source that denies bias cannot be compensated "
   "for, because the skew is unknown. The assessment scores four bias dimensions on a "
   "zero-to-one scale with evidence for each."),
 "how_it_works": ("Each dimension is scored from evidence: selection bias from coverage "
   "analysis (what share of the topic space gets covered), framing bias from language "
   "analysis of headlines and ledes, omission bias from comparing covered vs notable events, "
   "and sourcing bias from the diversity of cited voices. The example scores 0.2, 0.35, 0.15, "
   "0.1 - framing the highest, a common pattern. Scores are relative within source type: a "
   "0.35 framing score means 'more framed than peers,' judged against a peer baseline, not "
   "against perfection. The verdict bands are low (under 0.25 mean), low-moderate (0.25-0.4), "
   "moderate, and high. High-bias sources are not banned - they are labeled, and their claims "
   "require stronger corroboration."),
 "key_points": [
   "Four dimensions scored 0-1: selection 0.2, framing 0.35, omission 0.15, sourcing 0.1.",
   "Verdict low-moderate; scores relative to peer baselines.",
   "Bias is measured, not accused; disclosed bias can be compensated for.",
   "Denied bias cannot be compensated for - the skew is unknown.",
   "High-bias sources labeled, not banned; their claims need stronger corroboration.",
   "Evidence cited per dimension score.",
 ],
 "requirements": [
   "Evidence per dimension score.",
   "Peer baseline documented for relative scoring.",
   "Verdict band with thresholds published.",
   "Reassessment on the review cadence.",
 ],
 "standards": [
   "Scoring rubrics written before assessment.",
   "Multiple assessors for contested sources; disagreements recorded.",
   "Bias labels travel with the source's citations.",
   "Assessments distinguish systematic skew from occasional error.",
 ],
 "citations": [
   "Fowler, F. J. Survey Research Methods. Sage (selection and nonresponse bias).",
 ],
 "sig_lens": ("The Signature edition treats bias assessment as cartography of the lens: the "
   "doctrine does not demand an unbiased source - it demands a mapped one. A lens with known "
   "curvature can still take true photographs, once the photographer corrects for the bend."),
},
{
 "name": "Retraction Handling Procedure",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "demo_key": "r_facts",
 "demo_data": {"retractions_ytd": 2, "avg_days_to_retract": 34, "downstream_notified": True, "policy": "COPE",
               "checks": [["retractions_ytd", "==", 2]]},
 "description": ("The retraction handling procedure governs the most serious correction a source "
   "can issue: two retractions year-to-date, average thirty-four days to retract, downstream "
   "users notified, following COPE policy. A retraction says 'this should never have been "
   "published' - the findings are invalid, the data was flawed, the conclusions do not stand. "
   "Handling it well means retracting visibly (the original stays up, marked RETRACTED, never "
   "quietly deleted), retracting completely (every downstream citation notified), and "
   "retracting honestly (the notice states what was wrong and why). The procedure turns the "
   "worst moment in a source's life into evidence of its integrity."),
 "how_it_works": ("When grounds for retraction are confirmed, the procedure requires: a "
   "retraction notice stating specifically what was wrong and why, linked bidirectionally "
   "with the original; the original retained and watermarked RETRACTED, never deleted; "
   "notification to all known downstream citers within seven days; and a root-cause entry in "
   "the reliability record. The example shows two retractions averaging thirty-four days "
   "from concern to notice - measured, not hidden. COPE guidelines govern the wording: "
   "retractions distinguish honest error from misconduct, and the notice says which. Sources "
   "that retract promptly and completely gain correction-score credit; sources that stealth-"
   "delete lose history-score points permanently."),
 "key_points": [
   "2 retractions YTD, 34 days average to retract, downstream notified, COPE policy.",
   "Original retained and marked RETRACTED - never quietly deleted.",
   "Downstream citers notified within 7 days.",
   "Notice states what was wrong and why; honest error distinguished from misconduct.",
   "Prompt complete retraction earns credit; stealth deletion loses points permanently.",
   "Root cause recorded in the reliability record.",
 ],
 "requirements": [
   "Written retraction procedure following COPE guidelines.",
   "Bidirectional linking between notice and original.",
   "Downstream notification list maintained and executed.",
   "Root-cause entries for every retraction.",
 ],
 "standards": [
   "Retraction notices specific about the flaw - no vague 'concerns.'",
   "Deletion of the original prohibited.",
   "Timelines measured from first concern to published notice.",
   "Misconduct findings referred per institutional policy.",
 ],
 "citations": [
   "Committee on Publication Ethics (COPE): Retraction Guidelines.",
 ],
 "sig_lens": ("The Signature Reliability Doctrine holds that how a source handles its worst "
   "day defines it: the Signature edition awards its highest correction marks to the source "
   "that retracts loudly, completely, and fast. The doctrine's hardest rule - the original "
   "must stand, marked, forever - exists because memory is the price of trust."),
},
{
 "name": "Sample vs Census Data Reliability",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "demo_key": "r_sample",
 "demo_data": {"census_n": 1000000, "sample_n": 1067, "margin": 3.0, "confidence": 95},
 "description": ("The sample vs census record compares full enumeration with sampled "
   "measurement: a census of one million against a sample of one thousand sixty-seven with a "
   "plus-or-minus three-point margin at ninety-five percent confidence. A census has no "
   "sampling error but has every other error - nonresponse, misreporting, processing "
   "mistakes - and costs enormously. A well-drawn sample of 1,067 estimates a population "
   "proportion within three points, nineteen times out of twenty, at a fraction of the cost. "
   "The record states when sampling suffices, how the sample was drawn, and what the margin "
   "means - because 'plus or minus three' is routinely misread as 'exactly.'"),
 "how_it_works": ("The record documents the sampling frame (who could be selected), the "
   "selection method (random, stratified, cluster - with the design effect), the achieved "
   "sample size (1,067), and the margin of error at the stated confidence level: "
   "1.96*sqrt(0.25/1067) = 3.0 points at 95% for a proportion near 50%. Nonresponse is "
   "reported with the response rate and any weighting adjustments, because a 20% response "
   "rate means the sample represents respondents, not the population, until proven otherwise. "
   "Census data gets its own error accounting: coverage error (who was missed), measurement "
   "error, and processing error. The verdict rule: prefer the census for small-area detail, "
   "prefer the sample for timely estimates, and never treat either as exact."),
 "key_points": [
   "Census 1,000,000 vs sample 1,067 at +/-3 points, 95% confidence.",
   "Census has no sampling error but every other error - and enormous cost.",
   "Sampling frame, method, design effect, and nonresponse all documented.",
   "'Plus or minus three' misread as 'exactly' is the classic error.",
   "20% response rate represents respondents, not the population.",
   "Census for small-area detail; sample for timely estimates; neither is exact.",
 ],
 "requirements": [
   "Sampling frame and selection method documented.",
   "Margin of error with confidence level stated.",
   "Response rate and weighting adjustments reported.",
   "Census error accounting (coverage, measurement, processing).",
 ],
 "standards": [
   "Margins computed, not asserted - formula and inputs recorded.",
   "Non-probability samples labeled as such with their limits.",
   "Design effects applied for clustered/stratified designs.",
   "Comparisons account for both sources' error profiles.",
 ],
 "citations": [
   "Fowler, F. J. Survey Research Methods. Sage Publications.",
   "American Association for Public Opinion Research (AAPOR) disclosure standards.",
 ],
 "sig_lens": ("The Signature edition treats sampling as honest estimation: the Signature "
   "doctrine requires the margin stated alongside the number, always - a naked estimate "
   "without its uncertainty is a claim wearing a disguise. The doctrine prefers the humble "
   "sample with known error to the proud census with hidden error."),
},
{
 "name": "Sensor Data Reliability",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "demo_key": "r_drift",
 "demo_data": {"sensors": 120, "drift_per_year": 0.8, "calibration_days": 180, "failed": 3, "unit": "degC"},
 "description": ("The sensor data reliability record covers instrument-measured data: one "
   "hundred twenty sensors, drift of 0.8 degrees Celsius per year, calibrated every one "
   "hundred eighty days, three failed this cycle. Sensors do not lie, but they do drift, "
   "freeze, foul, and die - and they do it silently, reporting plausible-looking wrong "
   "numbers. The record tracks calibration schedules, drift rates, failure modes, and "
   "redundancy: with three sensors per location, one failure is detectable by disagreement. "
   "The reliability question for sensor data is never 'is it precise' but 'is it still "
   "calibrated.'"),
 "how_it_works": ("Each sensor carries a calibration certificate with date and next due date; "
   "the example's one-hundred-eighty-day cycle bounds drift to about 0.4 degrees (0.8/year "
   "x 0.5 year). Drift is measured at each calibration against a reference standard, and "
   "sensors drifting beyond tolerance are adjusted or retired. Three failures this cycle out "
   "of one hundred twenty is a 2.5% failure rate - tracked as a reliability input. "
   "Redundancy design: triple sensors with median voting, so a single failed sensor is "
   "outvoted rather than trusted. Data gaps from failures are flagged in the record, never "
   "interpolated silently - interpolated values are marked as estimates. Environmental "
   "exposure (icing, fouling, heat) is logged per deployment because it predicts drift."),
 "key_points": [
   "120 sensors; drift 0.8 degC/year; calibrated every 180 days; 3 failed (2.5%).",
   "Sensors drift, freeze, foul, and die - silently reporting plausible wrong numbers.",
   "Calibration bounds drift: ~0.4 degC between 180-day calibrations.",
   "Triple redundancy with median voting - one failure outvoted, not trusted.",
   "Gaps flagged, never silently interpolated.",
   "The question is 'still calibrated,' not 'precise.'",
 ],
 "requirements": [
   "Calibration certificates with dates for every sensor.",
   "Drift measurements against reference standards.",
   "Failure log with rates.",
   "Redundancy design documented.",
 ],
 "standards": [
   "Calibration intervals set from measured drift, not from habit.",
   "Reference standards themselves calibrated (traceability chain).",
   "Interpolated values marked as estimates.",
   "Failed sensors quarantined from the data feed immediately.",
 ],
 "citations": [
   "ISO/IEC 17025:2017 General requirements for the competence of testing and calibration laboratories.",
 ],
 "sig_lens": ("The Signature doctrine treats a sensor as a witness that cannot speak: its "
   "testimony is only as good as its last calibration. The Signature edition requires the "
   "certificate with the reading - a number without a calibration date is an anonymous "
   "testimony, and anonymous testimony is weighed accordingly."),
},
{
 "name": "Survey Data Reliability",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "demo_key": "r_ci",
 "demo_data": {"n": 1067, "p": 0.52, "z": 1.96, "response_rate": 0.23, "mode": "phone+online", "expect_moe": 3.0},
 "description": ("The survey data reliability record evaluates polled opinion and behavior: "
   "one thousand sixty-seven respondents, fifty-two percent saying yes, margin plus-or-minus "
   "three points at ninety-five percent confidence - but a twenty-three percent response "
   "rate, collected by phone and online. The margin of error is the best-understood and "
   "least-important number here: it quantifies sampling error, while the twenty-three "
   "percent response rate threatens everything, because the seventy-seven percent who did "
   "not answer may differ systematically from those who did. The record weighs the "
   "quantified error against the unquantified ones."),
 "how_it_works": ("The margin is computed as 1.96*sqrt(0.52*0.48/1067) = 3.0 points - the "
   "nineteen-in-twenty interval for sampling error alone. Then the record turns to the "
   "harder questions: the 23% response rate means nonresponse bias dominates sampling error, "
   "so weighting adjustments (by age, sex, region, education) are documented with their "
   "targets and effects. Mode effects are considered: phone and online respondents answer "
   "differently, and the mixed mode is analyzed for mode skew. Question wording is recorded "
   "verbatim - 'do you support' vs 'do you oppose' move numbers - and the full questionnaire "
   "is archived. The reliability verdict: the 52% estimate is usable with its margin, but "
   "only after the nonresponse analysis, never from the margin alone."),
 "key_points": [
   "n=1067, 52% yes, +/-3.0 at 95% - but 23% response rate dominates the error.",
   "Margin quantifies sampling error only; nonresponse is the bigger threat.",
   "Weighting adjustments documented with targets and effects.",
   "Mode effects analyzed: phone vs online respondents differ.",
   "Question wording archived verbatim - wording moves numbers.",
   "Verdict needs the nonresponse analysis, never the margin alone.",
 ],
 "requirements": [
   "Full questionnaire archived verbatim.",
   "Response rate and weighting scheme documented.",
   "Mode breakdown reported.",
   "Margin with confidence level and formula.",
 ],
 "standards": [
   "AAPOR disclosure standards followed.",
   "Weighting targets from a stated population frame.",
   "Likely-voter or eligibility screens described, not hidden.",
   "Comparisons across surveys account for method differences.",
 ],
 "citations": [
   "Fowler, F. J. Survey Research Methods. Sage Publications.",
   "American Association for Public Opinion Research (AAPOR) Code of Professional Ethics and Practices.",
 ],
 "sig_lens": ("The Signature edition treats a survey as an election where most voters stayed "
   "home: the doctrine requires the nonresponse counted as carefully as the responses. A "
   "pollster who reports the margin but hides the response rate is reporting the precision "
   "of the count while hiding the emptiness of the room."),
},
{
 "name": "Derived Data Reliability",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "demo_key": "r_propagate",
 "demo_data": {"inputs": [2.0, 1.5, 3.0], "labels": ["sales", "returns", "adjustments"], "result": 0.5},
 "description": ("The derived data reliability record tracks numbers computed from other "
   "numbers: sales 2.0 plus-or-minus 2.0%, returns 1.5 plus-or-minus 1.5%, adjustments 3.0 "
   "plus-or-minus 3.0% combine into a result whose uncertainty is larger than any input's. "
   "Errors propagate - they do not cancel - and every transformation adds its own: rounding, "
   "model assumptions, join mismatches. The record requires the full derivation chain with "
   "each input's uncertainty, so the output's uncertainty is computed, not wished away. A "
   "derived figure quoted without its propagated error is a precision costume over an "
   "uncertain body."),
 "how_it_works": ("The record lists every input with its value and uncertainty, the "
   "transformation applied, and the propagated output uncertainty. For the example "
   "(2.0 +/- 0.04, 1.5 +/- 0.0225, 3.0 +/- 0.09 combined as sales - returns + adjustments... "
   "simplified here), independent errors combine in quadrature: sqrt(0.04^2 + 0.0225^2 + "
   "0.09^2) = 0.101 on a result near 3.5 - about 2.9%. Each transformation step is a link in "
   "the provenance chain with its software version. Model-based derivations additionally "
   "record their assumptions, because a derived number is only as reliable as the model "
   "that derived it. Joins across datasets record their match rates - a 92% match rate means "
   "8% of the derivation rests on unmatched records."),
 "key_points": [
   "Errors propagate in quadrature - they do not cancel.",
   "Every input's uncertainty recorded; output uncertainty computed.",
   "Transformation steps linked in the provenance chain with software versions.",
   "Model assumptions recorded - derivations inherit model reliability.",
   "Join match rates recorded: 92% matched means 8% rests on unmatched records.",
   "Derived figures quoted with propagated error, never naked.",
 ],
 "requirements": [
   "Input values with uncertainties documented.",
   "Transformation formula and code version recorded.",
   "Propagated uncertainty computed and reported.",
   "Model assumptions listed for model-based derivations.",
 ],
 "standards": [
   "Quadrature combination for independent errors; documented handling for correlated ones.",
   "Rounding only at the final step - never mid-chain.",
   "Derivation code under version control and review.",
   "Sensitivity analysis for the largest uncertainty contributors.",
 ],
 "citations": [
   "Joint Committee for Guides in Metrology (JCGM) 100:2008: Guide to the Expression of Uncertainty in Measurement (error propagation).",
 ],
 "sig_lens": ("The Signature doctrine treats derived data as a family tree: every ancestor "
   "named, every marriage of datasets recorded, the inherited uncertainties acknowledged. "
   "The Signature edition forbids the orphan number - a figure that cannot name its parents "
   "cannot be trusted with decisions."),
},
{
 "name": "Expert Opinion Reliability",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "demo_key": "r_calibrate",
 "demo_data": {"forecasts": 40, "claimed_90": 34, "actual_90": 28, "brier": 0.18},
 "description": ("The expert opinion reliability record scores human judgment: forty "
   "forecasts, thirty-four claimed at ninety percent confidence, twenty-eight actually "
   "correct - the expert is overconfident, and the Brier score of 0.18 quantifies it. "
   "Expertise is real but miscalibrated: most experts are systematically overconfident, "
   "right less often than their confidence claims. The record tracks calibration - the "
   "match between stated confidence and actual hit rate - separately from resolution (did "
   "they discriminate right from wrong cases). A well-calibrated expert who says 'sixty "
   "percent' and is right sixty percent of the time beats a brilliant-but-overconfident one."),
 "how_it_works": ("Each forecast is recorded with the expert's stated probability, the "
   "outcome, and the resolution date. Calibration is measured in bins: of the forecasts "
   "stated at 90%, what fraction came true? The example shows 28/34 = 82% - overconfident "
   "by eight points. The Brier score (mean squared error of probabilistic forecasts, 0.18 "
   "here - lower is better) summarizes accuracy and calibration jointly. Experts are "
   "tracked individually, not as a profession: the record names the expert, because "
   "'experts say' is not a source. Domain boundaries are enforced - the economist's "
   "calibration on markets does not transfer to epidemiology. Overconfident experts get "
   "their stated probabilities shrunk toward the base rate before use."),
 "key_points": [
   "40 forecasts: claimed 90% on 34, actually right on 28 (82%) - overconfident.",
   "Brier score 0.18 summarizes accuracy and calibration.",
   "Calibration (confidence vs hit rate) tracked separately from resolution.",
   "Experts tracked individually - 'experts say' is not a source.",
   "Domain boundaries enforced: calibration does not transfer across fields.",
   "Overconfident probabilities shrunk toward base rates before use.",
 ],
 "requirements": [
   "Forecast log with stated probabilities and outcomes.",
   "Calibration bins computed per expert.",
   "Brier scores maintained.",
   "Domain of expertise defined and bounded.",
 ],
 "standards": [
   "Probabilities required - verbal hedges ('likely') converted to numbers or rejected.",
   "Outcomes judged against pre-registered resolution criteria.",
   "Track records published, not just claimed.",
   "No expert cited outside their calibrated domain for factual claims.",
 ],
 "citations": [
   "Tetlock, P. E. Expert Political Judgment. Princeton University Press, 2005 (expert calibration).",
 ],
 "sig_lens": ("The Signature edition treats expert calibration as a marksmanship record: the "
   "doctrine does not ask whether the expert is brilliant, it asks where the bullets "
   "landed. The Signature rule is strict - an uncalibrated expert is an unmeasured "
   "instrument, and unmeasured instruments do not certify facts."),
},
{
 "name": "Archival Record Reliability",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "demo_key": "r_facts",
 "demo_data": {"completeness": 0.87, "gaps": ["1974-1979", "2003-Q2"], "integrity_checks": 1240, "failures": 0,
               "checks": [["failures", "==", 0]]},
 "description": ("The archival record reliability record evaluates historical holdings: "
   "eighty-seven percent complete, with known gaps for 1974-1979 and 2003-Q2, one thousand "
   "two hundred forty integrity checks run, zero failures. Archives are the memory of "
   "institutions, and memory has holes: fires, moves, format rot, and the quiet discarding "
   "of what seemed unimportant. The record quantifies completeness, documents the gaps with "
   "their causes where known, and verifies integrity - checksums proving the bits are the "
   "bits that were stored. An archive that knows its gaps can be used correctly; one that "
   "claims completeness it does not have manufactures false certainty about the past."),
 "how_it_works": ("Completeness is measured against the accession register: what should be "
   "here versus what is here - 87% in the example. Each gap is documented: the 1974-1979 gap "
   "from a basement flood, the 2003-Q2 gap from a failed migration, with the cause recorded "
   "where known and marked unknown where not. Integrity is verified by checksums computed "
   "at ingest and rechecked on schedule: 1,240 checks, zero failures means the holdings are "
   "bit-stable. Format obsolescence is tracked: records in formats with no working reader "
   "are flagged for migration, because a perfectly preserved file nobody can open is "
   "practically lost. Access restrictions are recorded so researchers know what exists but "
   "cannot be seen - dark holdings counted in completeness but flagged in availability."),
 "key_points": [
   "87% complete; gaps 1974-1979 (flood) and 2003-Q2 (failed migration).",
   "1,240 integrity checks, 0 failures - holdings bit-stable.",
   "Gaps documented with causes; unknown causes marked unknown.",
   "Format obsolescence tracked - unopenable files are practically lost.",
   "Dark holdings counted in completeness, flagged in availability.",
   "Claimed completeness without evidence manufactures false certainty.",
 ],
 "requirements": [
   "Completeness measured against the accession register.",
   "Gap documentation with causes.",
   "Integrity check schedule with results.",
   "Format obsolescence watch list.",
 ],
 "standards": [
   "ISO 15489 records management principles.",
   "Checksums at ingest and on schedule.",
   "Migration before formats die, not after.",
   "Deaccession logged with authority and reason.",
 ],
 "citations": [
   "ISO 15489-1:2016 Information and documentation - Records management.",
 ],
 "sig_lens": ("The Signature edition treats an archive as a sworn memory: the Signature "
   "doctrine requires it to confess what it has forgotten. The gaps are part of the "
   "record - a memory that admits its holes can be trusted with what remains; one that "
   "pretends at wholeness cannot."),
},
{
 "name": "Composite Reliability Index",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "demo_key": "r_composite",
 "demo_data": {"metrics": {"history": 82, "correction": 76, "corroboration": 88, "limitations": 90, "freshness": 71, "agreement": 83},
               "weights": [0.2, 0.2, 0.2, 0.15, 0.15, 0.1]},
 "description": ("The composite reliability index rolls six measured metrics into one "
   "decision-ready number: history 82, correction 76, corroboration 88, limitations 90, "
   "freshness 71, agreement 83 - weighted to 81.7. The index exists for one purpose: letting "
   "a system decide, automatically and accountably, how much to trust a source in a specific "
   "use. It is not a grade on the source's soul; it is a working number with published "
   "inputs, published weights, and a versioned formula. When the index moves, the record "
   "says which metric moved it and why - a number that changes without explanation is not "
   "an index, it is a mood."),
 "how_it_works": ("The index is the weighted mean of its six metrics: 82x0.2 + 76x0.2 + "
   "88x0.2 + 90x0.15 + 71x0.15 + 83x0.1 = 81.65, reported as 81.7. Each metric is itself a "
   "measured value from this database's records - not an impression. The index is computed "
   "per use context: freshness weighs more for news, history more for reference works; the "
   "context profile is recorded with the score. Thresholds drive action: above 80 the source "
   "is citable for facts, 60-80 citable with corroboration, 40-60 background only, below 40 "
   "not cited. Every published index value links to its inputs, so any decision made on the "
   "index is auditable to the underlying measurements."),
 "key_points": [
   "Six metrics weighted to 81.7 - a working number, not a grade on a soul.",
   "Inputs, weights, and formula all published and versioned.",
   "Computed per use context: freshness weighs more for news, history for reference.",
   "Thresholds: 80+ citable, 60-80 with corroboration, 40-60 background, <40 not cited.",
   "Every value links to its inputs - decisions auditable to measurements.",
   "When the index moves, the record says which metric moved it and why.",
 ],
 "requirements": [
   "All six metrics measured, not estimated.",
   "Context profile recorded with each computation.",
   "Formula version recorded.",
   "Input linkage maintained for audit.",
 ],
 "standards": [
   "Weights sum to 1.0; changes versioned.",
   "Thresholds published before use.",
   "No manual overrides without logged rationale.",
   "Index recomputed on the review cadence and on metric changes.",
 ],
 "citations": [
   "Joint Committee for Guides in Metrology (JCGM) 100:2008 (combining uncertainties).",
 ],
 "sig_lens": ("The Signature edition treats the composite index as a navigational fix: six "
   "bearings, one position, every bearing checkable. The Signature doctrine forbids the "
   "single-number verdict without the six numbers behind it - a fix without bearings is a "
   "guess with confidence."),
},
# ---------------- Advanced (22-34) ----------------
{
 "name": "Reliability Decay Over Time",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "demo_key": "r_decay",
 "demo_data": {"initial": 88, "lambda_per_year": 0.12, "years": 3},
 "description": ("The reliability decay record models how a source's score erodes without "
   "maintenance: starting at 88, decaying at twelve percent per year, reaching 61.4 after "
   "three years of neglect. Reliability is not a permanent achievement; it is a maintained "
   "condition. Staff turns over, methodology drifts, incentives shift, and the world the "
   "source measures changes underneath it. The decay model quantifies the cost of neglect so "
   "rescoring has a schedule driven by math, not by embarrassment after a failure. A source "
   "that was excellent three years ago and untouched since is not excellent now - it is "
   "unexamined."),
 "how_it_works": ("The model applies exponential decay to the composite score: "
   "score(t) = initial x e^(-lambda x t). With lambda 0.12/year, three years gives "
   "88 x e^(-0.36) = 61.4 - a full band drop from neglect alone. Lambda is set per source "
   "type from historical rescoring data: fast-moving domains (technology, markets) decay "
   "faster than slow ones (geology, classical reference). The decay curve schedules "
   "rescoring: when the modeled score crosses a threshold band, review is due. Actual "
   "rescoring resets the clock - maintenance defeats decay. The record also tracks whether "
   "real rescoring matches the model: systematic over- or under-prediction recalibrates "
   "lambda. Neglect is thus visible in advance, as a date on a calendar, not discovered "
   "after the damage."),
 "key_points": [
   "88 decaying at 12%/year reaches 61.4 after 3 years - a full band drop.",
   "Reliability is a maintained condition, not a permanent achievement.",
   "Lambda set per source type from historical rescoring data.",
   "Decay curve schedules rescoring: threshold crossings put review on the calendar.",
   "Maintenance resets the clock; model checked against actual rescorings.",
   "Neglect visible in advance as a date, not discovered after damage.",
 ],
 "requirements": [
   "Lambda documented per source type with its evidence.",
   "Decay-computed review dates scheduled.",
   "Rescoring results compared against model predictions.",
   "Recalibration when systematic error appears.",
 ],
 "standards": [
   "Decay applied to the composite, with dimension-level decay where measured.",
   "No source exempt from decay modeling.",
   "Review dates from decay are commitments, not suggestions.",
   "Model versions recorded with scores.",
 ],
 "citations": [
   "Ioannidis, J. P. A. Why most published research findings are false. PLoS Medicine, 2005 (on the decay of findings' reliability).",
 ],
 "sig_lens": ("The Signature Reliability Doctrine treats decay as rust: it never sleeps, and "
   "it attacks the unmaintained first. The Signature edition requires the rust measured and "
   "the repainting scheduled - a source left to the weather is not a source, it is a ruin "
   "with a good reputation."),
},
{
 "name": "Adversarial Source Detection",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "demo_key": "r_detect",
 "demo_data": {"flagged": 60, "true_pos": 45, "false_pos": 15, "missed": 5, "total_bad": 50},
 "description": ("The adversarial source detection record covers sources that mislead on "
   "purpose: sixty flagged, forty-five truly adversarial, fifteen false positives, five "
   "missed out of fifty genuinely bad - precision seventy-five percent, recall ninety "
   "percent. Adversarial sources include fabricators, coordinated inauthentic operations, "
   "and sources captured by interested parties. Detection looks for tells: impossible "
   "precision in data, provenance gaps at suspicious points, coordination signals across "
   "supposedly independent sources, and incentives wildly misaligned with honesty. The "
   "record is careful: false accusation destroys a good source's reputation, so flags "
   "require evidence and review before publication."),
 "how_it_works": ("Detection combines statistical tells (Benford-style digit analysis on "
   "reported numbers, impossible consistency), provenance tells (gaps, circular sourcing), "
   "behavioral tells (publishing speed inconsistent with genuine collection), and incentive "
   "analysis. The example confusion matrix: 60 flagged, 45 true positives, 15 false "
   "positives (precision 75%), 5 missed of 50 truly bad (recall 90%). Flags go through "
   "human review before any public label - the fifteen false positives in the example were "
   "cleared on review, which is the system working. Confirmed adversarial sources are "
   "labeled, their past citations flagged for re-verification, and their reliability score "
   "floored. The detector itself is evaluated on the matrix quarterly; a detector whose "
   "precision falls is worse than no detector, because false accusations are their own "
   "reliability incident."),
 "key_points": [
   "60 flagged: 45 true, 15 false positives (precision 75%); 5 missed of 50 bad (recall 90%).",
   "Tells: statistical, provenance, behavioral, incentive.",
   "Flags require human review before any public label.",
   "Confirmed adversarial: labeled, past citations re-verified, score floored.",
   "False accusation is its own reliability incident.",
   "Detector evaluated quarterly on its confusion matrix.",
 ],
 "requirements": [
   "Documented tell catalog with evidence standards.",
   "Human review gate before labeling.",
   "Re-verification procedure for past citations.",
   "Detector performance tracked quarterly.",
 ],
 "standards": [
   "Evidence standard for 'adversarial' higher than for 'unreliable.'",
   "False positives cleared publicly, not silently.",
   "Incentive analysis part of every assessment.",
   "No automated public labeling.",
 ],
 "citations": [
   "NIST Special Publication 800-53, control SI-4 (monitoring for malicious activity) - detection practice reference.",
 ],
 "sig_lens": ("The Signature doctrine treats adversarial detection as counterintelligence: "
   "necessary, dangerous, and bound by rules of evidence stricter than the accusation is "
   "tempting. The Signature edition requires the reviewer to prove the charge or drop it - "
   "a false charge against an honest source is the same crime it claims to fight."),
},
{
 "name": "Anonymous Source Policy",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "demo_key": "r_facts",
 "demo_data": {"allowed": True, "conditions": 4, "editor_approval": True, "corroboration_required": 2,
               "checks": [["conditions", "==", 4], ["corroboration_required", "==", 2]]},
 "description": ("The anonymous source policy governs information from sources that cannot be "
   "named: allowed, under four conditions, with editor approval, requiring two independent "
   "corroborations. Anonymous sourcing is sometimes necessary - whistleblowers face real "
   "retaliation - and always risky: the reader cannot evaluate what they cannot see. The "
   "policy balances this with four conditions: the information must be otherwise "
   "unobtainable, the source's position to know must be verified by the editor, the "
   "motivation must be assessed, and the claim must be corroborated by two independent "
   "sources. Anonymity protects the source; the conditions protect the reader."),
 "how_it_works": ("When a source requests anonymity, the editor verifies their identity and "
   "position to know directly - anonymous to the reader never means anonymous to the "
   "editor. The four conditions are checked and documented: unobtainability (could this be "
   "gotten on the record?), position (does this person actually know?), motivation (why are "
   "they talking, and what do they gain?), and corroboration (two independent sources "
   "confirm). The published piece describes the source as specifically as safety allows "
   "- 'a senior official involved in the negotiations' - and states why anonymity was "
   "granted. Single-anonymous-source publication is prohibited for factual claims; it is "
   "permitted only for clearly labeled opinion or with explicit editor-in-chief exception, "
   "logged. The policy is reviewed annually because the threat landscape for sources "
   "changes."),
 "key_points": [
   "Allowed under 4 conditions, with editor approval, 2 independent corroborations required.",
   "Anonymous to the reader never means anonymous to the editor.",
   "Conditions: unobtainable otherwise, verified position, assessed motivation, corroborated.",
   "Source described as specifically as safety allows; reason for anonymity stated.",
   "Single anonymous source never suffices for factual claims.",
   "Policy reviewed annually as the threat landscape changes.",
 ],
 "requirements": [
   "Editor verification of identity and position.",
   "Four-condition checklist documented per use.",
   "Corroboration count met before publication.",
   "Anonymity rationale published with the piece.",
 ],
 "standards": [
   "No anonymous sourcing without editor approval.",
   "Motivation assessment part of the record.",
   "Exceptions logged with approver identity.",
   "Source safety reviewed before and after publication.",
 ],
 "citations": [
   "Society of Professional Journalists Code of Ethics (anonymous source guidance).",
 ],
 "sig_lens": ("The Signature edition treats anonymous sourcing as a masked witness: the court "
   "may hear them, but only after the judge has seen the face behind the mask and the jury "
   "is told exactly why the mask stays on. The Signature doctrine holds that the mask "
   "protects the witness - the four conditions protect everyone else."),
},
{
 "name": "Statistical Confidence Calibration",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "demo_key": "r_ci",
 "demo_data": {"n": 2400, "p": 0.48, "z": 1.96, "response_rate": 0.31, "mode": "online panel", "expect_moe": 2.0},
 "description": ("The statistical confidence calibration record ensures uncertainty numbers "
   "mean what they claim: n=2,400, p=0.48, margin plus-or-minus two points at ninety-five "
   "percent confidence - calibrated, with a thirty-one percent response rate on an online "
   "panel. Calibration means the stated ninety-five percent intervals actually contain the "
   "truth about ninety-five percent of the time. Many published intervals fail this: they "
   "quantify sampling error while ignoring the nonresponse, coverage, and measurement "
   "errors that dominate. The record calibrates the full uncertainty - or labels the "
   "interval as sampling-error-only so nobody mistakes it for total uncertainty."),
 "how_it_works": ("The margin is computed: 1.96*sqrt(0.48*0.52/2400) = 2.0 points. Then "
   "calibration checks begin: is the sample probabilistic (can every population member be "
   "selected)? An online panel with 31% response is not, so the interval is labeled "
   "model-based and the weighting model's assumptions are stated. Historical calibration "
   "is checked where available: past intervals from this source, did 95% contain the "
   "eventual truth? Systematic misses widen future intervals or downgrade the confidence "
   "claim. The record distinguishes three interval types: design-based (probabilistic "
   "sample, full error accounting), model-based (stated assumptions), and nominal "
   "(sampling error only - the common, misleading kind). Only design-based intervals are "
   "cited without qualification."),
 "key_points": [
   "n=2400, p=0.48: margin +/-2.0 at 95% - then calibration asks what the margin omits.",
   "Calibration: do stated 95% intervals contain truth 95% of the time?",
   "Online panel, 31% response: interval labeled model-based, assumptions stated.",
   "Three interval types: design-based, model-based, nominal (sampling-error-only).",
   "Historical calibration checked; systematic misses widen future intervals.",
   "Only design-based intervals cited without qualification.",
 ],
 "requirements": [
   "Interval type labeled for every published margin.",
   "Assumptions stated for model-based intervals.",
   "Historical calibration tracked where possible.",
   "Full error accounting or explicit nominal labeling.",
 ],
 "standards": [
   "Nominal intervals never presented as total uncertainty.",
   "Confidence claims downgraded when calibration fails.",
   "Weighting models documented with their targets.",
   "Calibration reviewed on the reliability cadence.",
 ],
 "citations": [
   "American Statistical Association statement on p-values and statistical significance, 2016.",
   "Fowler, F. J. Survey Research Methods. Sage Publications.",
 ],
 "sig_lens": ("The Signature doctrine treats an uncalibrated confidence interval as a "
   "miscalibrated scale: the numbers look precise while the truth slips through. The "
   "Signature edition requires every interval to carry its type like a warning label - "
   "precision without calibration is the most expensive kind of wrong."),
},
{
 "name": "Reliability-Weighted Consensus",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "demo_key": "r_vote",
 "demo_data": {"sources": ["A", "B", "C", "D"], "scores": [88, 76, 92, 54], "values": [2.1, 2.3, 2.0, 3.1]},
 "description": ("The reliability-weighted consensus record combines disagreeing sources "
   "fairly: sources A, B, C, D with reliability scores 88, 76, 92, 54 reporting 2.1, 2.3, "
   "2.0, 3.1 - the weighted consensus is 2.29, not the simple mean of 2.38. Equal weighting "
   "lets the least reliable source pull the answer; reliability weighting lets the evidence "
   "pull it. Source D's 3.1, from the 54-scored source, moves the consensus only slightly, "
   "which is correct: extraordinary claims from weak sources should whisper, not shout. The "
   "record publishes the weights, the computation, and the sensitivity - how much the "
   "consensus would move if any source were excluded."),
 "how_it_works": ("Weights are the reliability scores normalized: total 310, weights "
   "0.284/0.245/0.297/0.174. Consensus = 2.1x0.284 + 2.3x0.245 + 2.0x0.297 + 3.1x0.174 = 2.29. The simple mean would be 2.38 - the weak source's outlier inflating the answer. "
   "Sensitivity is reported: excluding D moves consensus to 2.12; excluding C (the strongest) moves it to 2.42. When sources disagree beyond what their scores explain - "
   "two highly reliable sources far apart - the record flags model failure instead of "
   "averaging: the disagreement is the finding. Weights are the current reliability scores, "
   "so consensus updates as scores update. The method is published so any consumer can "
   "recompute or substitute their own weights."),
 "key_points": [
   "Weighted consensus 2.29 vs simple mean 2.38 - the weak source's outlier properly muted.",
   "Weights are current reliability scores, normalized; published and recomputable.",
   "Sensitivity reported: excluding D gives 2.12; excluding C gives 2.42.",
   "Extraordinary claims from weak sources whisper, not shout.",
   "Unexplained disagreement between strong sources flags model failure, not averaged.",
   "Consensus updates as reliability scores update.",
 ],
 "requirements": [
   "Current reliability scores for all contributing sources.",
   "Weighting formula and computation published.",
   "Sensitivity analysis included.",
   "Model-failure flagging rule defined.",
 ],
 "standards": [
   "Weights from measured scores, never from impression.",
   "Consensus labeled with its method and date.",
   "Disagreement beyond model expectations investigated.",
   "Consumers may substitute weights; method supports it.",
 ],
 "citations": [
   "Cochrane Handbook for Systematic Reviews of Interventions (weighting in meta-analysis).",
 ],
 "sig_lens": ("The Signature edition treats weighted consensus as a council where votes are "
   "weighed by earned trust: the long-reliable speak loudly, the unproven speak softly. "
   "The Signature doctrine insists the weighing be public - a council with secret vote "
   "weights is a cabal, not a consensus."),
},
{
 "name": "Source Reliability Audit Trail",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "demo_key": "r_facts",
 "demo_data": {"events": 184, "score_changes": 12, "reviews": 6, "immutable": True,
               "checks": [["events", "==", 184], ["immutable", "==", True]]},
 "description": ("The source reliability audit trail is the immutable log of everything that "
   "happened to a source's reliability record: one hundred eighty-four events, twelve "
   "score changes, six reviews - append-only, tamper-evident. Every score change links to "
   "the evidence that caused it; every review links to its findings; nothing is ever "
   "edited or deleted. When someone asks 'why did this source's score drop in March,' the "
   "trail answers with dates, evidence, and the analyst's name. A reliability system "
   "without an audit trail asks for trust while refusing to show its work."),
 "how_it_works": ("Each event is appended with a timestamp, actor, event type, and content "
   "hash chained to the previous event - tampering with any event breaks the chain and is "
   "detectable. Event types include: score computed, evidence added, correction logged, "
   "review opened/closed, threshold crossed, label applied, dispute filed/resolved. The "
   "example's 184 events include 12 score changes, each linked to its triggering evidence, "
   "and 6 reviews with findings. The trail is readable by auditors and by the source "
   "itself - sources may dispute entries, and disputes are appended as events, never "
   "resolved by editing history. Retention is permanent: the trail is the institutional "
   "memory of why each source is trusted as it is."),
 "key_points": [
   "184 events, 12 score changes, 6 reviews - append-only and tamper-evident.",
   "Every score change links to its triggering evidence.",
   "Hash-chained: tampering breaks the chain detectably.",
   "Sources may dispute entries; disputes appended, history never edited.",
   "Permanent retention - the institutional memory of trust.",
   "A system without a trail asks for trust while refusing to show its work.",
 ],
 "requirements": [
   "Append-only event log with hash chaining.",
   "Evidence linkage for every score change.",
   "Dispute events supported.",
   "Auditor and source read access.",
 ],
 "standards": [
   "No edit or delete operations exist on the trail.",
   "Timestamps from synchronized clocks.",
   "Actor identity recorded per event.",
   "Chain verification runnable by any auditor.",
 ],
 "citations": [
   "ISO 15489-1:2016 (records as evidence of activity).",
 ],
 "sig_lens": ("The Signature doctrine treats the audit trail as the reliability system's own "
   "reliability record: the system that judges sources must itself be judgable. The "
   "Signature edition requires the chain unbreakable - a judge who edits the court record "
   "is not a judge."),
},
{
 "name": "Automated Reliability Monitoring",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "demo_key": "r_monitor",
 "demo_data": {"sources": 340, "checks_per_day": 8160, "alerts_week": 23, "true_alerts": 19, "mttr_h": 7.5},
 "description": ("The automated reliability monitoring record watches sources continuously: "
   "three hundred forty sources, eight thousand one hundred sixty checks per day, twenty-three "
   "alerts last week, nineteen true - precision eighty-three percent - with a seven-and-a-half-"
   "hour mean time to resolve. Monitoring watches for the signals humans miss at scale: "
   "correction-rate spikes, publication gaps, link rot in citations, sudden tone shifts, "
   "provenance chain breaks, and freshness decay crossing thresholds. Automation handles the "
   "watching; humans handle the judging - every alert resolves to a human decision, because "
   "an algorithm that unilaterally downgrades sources is an unaccountable judge."),
 "how_it_works": ("Each source gets a monitoring profile: which signals are watched, their "
   "thresholds, and the alert routing. The 8,160 daily checks divide across sources by risk "
   "tier - high-impact sources checked hourly, background sources daily. Last week's 23 "
   "alerts broke down as 19 true positives (a correction spike, three publication gaps, "
   "link rot clusters) and 4 false positives tuned out afterward - precision 83%, tracked "
   "as a tuning metric. Mean time to resolve of 7.5 hours measures alert-to-human-decision. "
   "Alert fatigue is managed: thresholds auto-tune within guardrails, and noisy signals are "
   "demoted to weekly digests rather than pages. Monitoring covers the monitors too - a "
   "silent check pipeline pages louder than any source alert."),
 "key_points": [
   "340 sources, 8,160 checks/day, 23 alerts/week, 19 true (precision 83%).",
   "Signals: correction spikes, publication gaps, link rot, tone shifts, chain breaks, decay.",
   "MTTR 7.5 hours, alert to human decision.",
   "Automation watches; humans judge - no unilateral algorithmic downgrades.",
   "Thresholds auto-tune within guardrails; noisy signals demoted to digests.",
   "The monitoring pipeline itself is monitored - silence pages loudest.",
 ],
 "requirements": [
   "Monitoring profiles per source with signals and thresholds.",
   "Risk-tiered check cadences.",
   "Alert precision tracked and tuned.",
   "Human decision gate on every alert.",
 ],
 "standards": [
   "No fully automated score changes from monitoring alone.",
   "Alert fatigue metrics reviewed monthly.",
   "Pipeline liveness monitored independently.",
   "Tuning changes logged with rationale.",
 ],
 "citations": [
   "NIST Special Publication 800-53, control SI-4 (information system monitoring).",
 ],
 "sig_lens": ("The Signature edition treats automated monitoring as the night watch: tireless, "
   "literal-minded, and never promoted to judge. The Signature doctrine requires the watch "
   "to wake a human for every judgment call - a watchman who sentences in the night is not "
   "a watchman, whatever his precision."),
},
{
 "name": "Machine-Generated Content Reliability",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "demo_key": "r_facts",
 "demo_data": {"hallucination_rate": 0.08, "citation_fabrication": 0.03, "human_review": True,
               "label": "machine-generated",
               "checks": [["human_review", "==", True]]},
 "description": ("The machine-generated content reliability record scores AI-produced "
   "material: hallucination rate eight percent, citation fabrication three percent, human "
   "review required, labeled machine-generated. Machine-generated content is fluent, fast, "
   "and sometimes false with complete confidence - it fabricates citations that look real, "
   "states uncertain things certainly, and has no notion of truth. The record treats it as "
   "a source type with measured properties: the hallucination rate from red-team evaluation, "
   "the citation fabrication rate from verification sampling, and the mandatory human review "
   "gate before any factual use. Labeling is non-negotiable: machine-generated content "
   "presented as human work is deception, whatever its accuracy."),
 "how_it_works": ("The hallucination rate (8% in the example) comes from red-team "
   "evaluation: adversarial prompts testing factuality across domains, scored by human "
   "judges. Citation fabrication (3%) is measured by sampling generated citations and "
   "verifying each exists and says what is claimed. Human review is mandatory before "
   "factual use - the reviewer checks claims against sources, not against the model's "
   "confidence. The label 'machine-generated' travels with the content through every "
   "downstream use; stripping the label is a policy violation. Reliability scoring treats "
   "machine output as secondary evidence at best: it may suggest, never certify. Model "
   "version is recorded because rates differ by model and by prompt engineering - the score "
   "belongs to a specific model version, not to 'AI' in general."),
 "key_points": [
   "Hallucination rate 8%, citation fabrication 3% - measured, not assumed.",
   "Human review mandatory before any factual use.",
   "Label 'machine-generated' travels with content; stripping it is a violation.",
   "Machine output suggests, never certifies - secondary evidence at best.",
   "Scores belong to specific model versions, not to 'AI' generally.",
   "Presented as human work, it is deception whatever its accuracy.",
 ],
 "requirements": [
   "Red-team hallucination measurement per model version.",
   "Citation verification sampling.",
   "Human review gate enforced.",
   "Labeling preserved through downstream use.",
 ],
 "standards": [
   "No unlabeled machine-generated content in the corpus.",
   "Reviewers check against sources, not model confidence.",
   "Rates re-measured on model updates.",
   "Fabricated citations treated as integrity incidents.",
 ],
 "citations": [
   "NIST AI 100-1: Artificial Intelligence Risk Management Framework (2023).",
 ],
 "sig_lens": ("The Signature doctrine treats machine-generated content as a brilliant, "
   "compulsive storyteller: useful for drafts, dangerous for facts. The Signature edition "
   "requires the label the way medicine requires the label - the substance may help or harm, "
   "but the patient has a right to know what they are taking."),
},
{
 "name": "Domain Reliability Baselines",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "demo_key": "r_facts",
 "demo_data": {"domains": 12, "median_score": 74, "top_quartile": 86,
               "checks": [["domains", "==", 12]]},
 "description": ("The domain reliability baselines record sets the normal for each field: "
   "twelve domains baselined, median source score seventy-four, top quartile eighty-six. "
   "Reliability is relative to domain: a breaking-news source scoring 74 is excellent "
   "against a domain median of 61, while a reference work scoring 74 against a domain "
   "median of 88 is mediocre. Baselines prevent the two classic errors - demanding "
   "reference-work reliability from daily news, and accepting news-level reliability from "
   "reference works. Each domain's baseline includes the median, quartiles, and the "
   "characteristic error profile of the field."),
 "how_it_works": ("Baselines are computed from all scored sources in each domain: the "
   "median, quartiles, and the distribution shape. The twelve domains cover news, "
   "academic publishing, government statistics, market data, reference works, surveys, "
   "sensor networks, archival holdings, expert commentary, machine-generated content, "
   "corporate disclosure, and nonprofit research. Each baseline documents the domain's "
   "characteristic errors - news is fast and correctable, academic is slow and durable, "
   "corporate disclosure is complete but framed. Individual sources are reported with "
   "their percentile within domain, not just their raw score: '74th percentile in news' "
   "means more than 'score 74.' Baselines are recomputed annually; domain drift - a whole "
   "field getting better or worse - is itself a finding worth reporting."),
 "key_points": [
   "12 domains baselined; median 74, top quartile 86.",
   "74 is excellent in news (median 61), mediocre in reference (median 88).",
   "Prevents demanding reference reliability from news and vice versa.",
   "Each domain documents its characteristic error profile.",
   "Sources reported by domain percentile, not just raw score.",
   "Domain drift recomputed annually - a field improving or declining is a finding.",
 ],
 "requirements": [
   "Baseline distributions per domain with quartiles.",
   "Characteristic error profiles documented.",
   "Percentile reporting for individual sources.",
   "Annual recomputation.",
 ],
 "standards": [
   "Cross-domain score comparisons prohibited without baseline context.",
   "Domain definitions stable year over year for trend validity.",
   "New domains baselined before sources are scored against them.",
   "Drift reported, not silently absorbed.",
 ],
 "citations": [
   "Cochrane Handbook for Systematic Reviews of Interventions (domain-specific evidence standards).",
 ],
 "sig_lens": ("The Signature edition treats baselines as the local sea level: a height means "
   "nothing without knowing what it is measured from. The Signature doctrine requires every "
   "score to name its ocean - a number floating without a baseline is not a measurement, it "
   "is a wish."),
},
{
 "name": "Reliability Dispute Resolution",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "demo_key": "r_facts",
 "demo_data": {"disputes_ytd": 9, "resolved": 7, "upheld": 4, "overturned": 3, "median_days": 21,
               "checks": [["resolved", "==", 7]]},
 "description": ("The reliability dispute resolution record governs challenges to scores: nine "
   "disputes year-to-date, seven resolved, four upheld, three overturned, median twenty-one "
   "days to decision. Sources will dispute their scores - sometimes rightly, because the "
   "evidence was incomplete, and sometimes wrongly, because nobody enjoys a low grade. The "
   "procedure gives them a fair hearing: a written dispute stating the specific error "
   "alleged, independent re-examination of the evidence, and a published decision with "
   "reasons. Three overturned scores prove the process is real - a dispute system that never "
   "overturns is a suggestion box."),
 "how_it_works": ("A dispute opens with a written filing: which score, which dimension, what "
   "evidence was missed or misread. An analyst uninvolved in the original scoring "
   "re-examines the evidence and any new material; the original analyst may respond but "
   "does not decide. The decision - uphold, overturn, or partially adjust - is published "
   "with reasons, and the audit trail records the whole proceeding. The example shows 9 "
   "disputes, 7 resolved, 4 upheld and 3 overturned, median 21 days - a working system, not "
   "a rubber stamp. Frivolous disputes (no new evidence, no specific allegation) are "
   "dismissed quickly with reasons. Retaliation against disputing sources is prohibited and "
   "itself a reviewable offense - the right to dispute must be safe to exercise."),
 "key_points": [
   "9 disputes YTD, 7 resolved: 4 upheld, 3 overturned, median 21 days.",
   "Written filing: which score, which dimension, what evidence was missed.",
   "Independent re-examiner; original analyst responds but does not decide.",
   "Decisions published with reasons; 3 overturns prove the process is real.",
   "Frivolous disputes dismissed quickly with reasons.",
   "Retaliation against disputants prohibited and reviewable.",
 ],
 "requirements": [
   "Written dispute procedure with filing requirements.",
   "Independent re-examination.",
   "Published decisions with reasons.",
   "Anti-retaliation protection.",
 ],
 "standards": [
   "Decisions on evidence, not on relationships.",
   "Timelines published and met.",
   "Overturns analyzed for systemic scoring errors.",
   "Dispute records retained permanently.",
 ],
 "citations": [
   "ISO 10002:2018 Quality management - Customer satisfaction - Guidelines for complaints handling (dispute process reference).",
 ],
 "sig_lens": ("The Signature doctrine treats dispute resolution as the court of appeals for "
   "trust: the Signature edition requires the court to actually overturn sometimes, "
   "because a court that never reverses is not reviewing - it is decorating. The three "
   "overturned scores are the proof the system would rather be right than be consistent."),
},
{
 "name": "Reliability Certification",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "demo_key": "r_facts",
 "demo_data": {"certified": 28, "levels": ["bronze", "silver", "gold"], "gold": 6, "valid_years": 2,
               "checks": [["gold", "==", 6]]},
 "description": ("The reliability certification record awards public marks of trust: "
   "twenty-eight sources certified across bronze, silver, and gold levels - six at gold, "
   "valid two years. Certification is the system's positive statement: not just 'this "
   "source scores 82' but 'this source meets the published standard for gold.' Levels are "
   "earned by meeting cumulative criteria - gold requires two years above 85, zero major "
   "uncorrected errors, complete limitation registers, and a clean audit trail. "
   "Certification expires: two years, then re-earned, because trust maintained is trust "
   "demonstrated again."),
 "how_it_works": ("Bronze requires a complete reliability record and scores above 60 on all "
   "dimensions. Silver adds two years of history, correction rates in the healthy band, and "
   "independent corroboration practices. Gold - six sources in the example - requires scores "
   "above 85 sustained two years, zero major uncorrected errors, complete limitation "
   "registers, published methodology, and a clean audit trail. Assessment is by independent "
   "auditors, not self-attestation. Certificates carry expiry dates (two years) and are "
   "revocable: a major integrity failure suspends certification pending investigation. "
   "Certified sources are listed publicly with their level, criteria met, and expiry - the "
   "list is the point, letting users choose certified sources without doing the analysis "
   "themselves."),
 "key_points": [
   "28 certified: bronze/silver/gold tiers; 6 at gold; valid 2 years.",
   "Gold: 2 years above 85, zero major uncorrected errors, clean audit trail.",
   "Independent auditors, never self-attestation.",
   "Certificates expirable and revocable - trust re-earned, not permanent.",
   "Public list with level, criteria, and expiry - users choose without re-analyzing.",
   "Major integrity failure suspends pending investigation.",
 ],
 "requirements": [
   "Published criteria per level.",
   "Independent assessment.",
   "Expiry dates and revocation procedure.",
   "Public certification list.",
 ],
 "standards": [
   "Criteria measurable - no subjective 'excellence' clauses.",
   "Assessors independent of the source and of the certifier's commercial interests.",
   "Re-assessment from scratch at expiry, not renewal by default.",
   "Revocations published with reasons.",
 ],
 "citations": [
   "ISO/IEC 17065:2012 Conformity assessment - Requirements for bodies certifying products, processes and services (certification practice).",
 ],
 "sig_lens": ("The Signature edition treats certification as a knighthood with a term limit: "
   "the honor is real, the sword is real, but every two years the knight must prove worthy "
   "again. The Signature doctrine holds that permanent titles breed complacency - even "
   "gold must be re-earned."),
},
{
 "name": "Reliability Dashboard Exemplar",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "demo_key": "r_dashboard",
 "demo_data": {"sources": 340, "panels": 8, "refresh_min": 15, "alerts": 3},
 "description": ("The reliability dashboard exemplar shows what good looks like: three "
   "hundred forty sources, eight panels, fifteen-minute refresh, three active alerts. The "
   "panels are: score distribution, dimension heatmap, correction-rate trends, freshness "
   "aging, corroboration network, dispute queue, certification status, and the alert feed. "
   "Each panel answers one question a reliability manager asks daily. The exemplar is "
   "prescriptive: it shows the layout, the queries behind each panel, and the thresholds "
   "that color them - so every deployment starts from a working design instead of a blank "
   "screen and good intentions."),
 "how_it_works": ("The eight panels query the reliability records on a fifteen-minute "
   "refresh: the distribution histogram shows score bands across all 340 sources; the "
   "heatmap shows dimension scores per source type, revealing systemic weaknesses (a cold "
   "column means a dimension nobody measures well); correction trends show rates over time "
   "with threshold lines; freshness aging lists records below 0.5 freshness; the "
   "corroboration network graphs which sources confirm which claims; the dispute queue "
   "shows open disputes by age; certification status shows levels and upcoming expiries; "
   "the alert feed shows the three active alerts with owners. Thresholds are the same "
   "published numbers used in scoring - the dashboard displays the system, it does not "
   "redefine it. Drill-down goes from any panel to the underlying records and their audit "
   "trails."),
 "key_points": [
   "340 sources, 8 panels, 15-minute refresh, 3 active alerts.",
   "Panels: distribution, heatmap, correction trends, freshness, corroboration, disputes, certification, alerts.",
   "Heatmap reveals systemic weaknesses - a cold column is a dimension nobody measures.",
   "Thresholds are the published scoring numbers - display, not redefinition.",
   "Drill-down from any panel to records and audit trails.",
   "Exemplar is prescriptive: layout, queries, thresholds included.",
 ],
 "requirements": [
   "All eight panels implemented with documented queries.",
   "Refresh cadence met and monitored.",
   "Thresholds matching the published scoring standards.",
   "Drill-down to underlying records.",
 ],
 "standards": [
   "Dashboard numbers reproducible from the records.",
   "No vanity metrics - every panel answers a manager's real question.",
   "Alert ownership visible on the alert feed.",
   "Exemplar updated when scoring standards change.",
 ],
 "citations": [
   "NIST Special Publication 800-53, control SI-4 (monitoring displays).",
 ],
 "sig_lens": ("The Signature edition treats the dashboard as the watchtower: the doctrine "
   "requires the watchman to see the whole territory at a glance and any single sheep on "
   "demand. The exemplar exists because a territory watched through eight clear windows is "
   "governed; watched through none, it is merely hoped about."),
},
{
 "name": "Reliability Self-Audit and Mastery Record",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "demo_key": "r_mastery",
 "demo_data": {"records": 34, "complete": 34, "dimensions_audited": 5, "stale_scores": 0, "coverage": 1.0},
 "description": ("The reliability self-audit and mastery record proves the system judges "
   "itself: thirty-four reliability archetypes catalogued, thirty-four complete, all five "
   "dimensions audited, zero stale scores, coverage one hundred percent. This is the record "
   "that closes the loop - the reliability database submitting to its own reliability "
   "scoring. It verifies that every source record has its five dimensions scored, its "
   "evidence linked, its review date current, and its audit trail intact. A reliability "
   "system that exempts itself from reliability judgment is a priesthood, not a science."),
 "how_it_works": ("The self-audit applies the database's own standards to its own records: "
   "dimension completeness (all five scored for every source), evidence linkage (every "
   "score traceable to its measurements), review currency (no score older than its "
   "cadence - zero stale in the example), audit trail integrity (hash chains verified), "
   "and dispute responsiveness (open disputes within SLA). The example scores 34 of 34 "
   "complete with coverage 1.0. Gaps become findings with owners and dates, scored like "
   "any reliability finding. The audit runs quarterly and its report is public within the "
   "system, because the users of reliability scores deserve to know the scorer is sound. "
   "This record is also the mastery checkpoint: a reader who understands all thirty-four "
   "records - from the five dimensions through source-type analysis to advanced governance "
   "- understands source reliability end to end."),
 "key_points": [
   "34 archetypes, 34 complete, 5 dimensions audited, 0 stale scores - coverage 1.0.",
   "Self-audit applies the database's own standards to its own records.",
   "Gaps become findings with owners and dates.",
   "Runs quarterly; report public within the system.",
   "A system exempting itself from judgment is a priesthood, not a science.",
   "Mastery checkpoint: all 34 records teach source reliability end to end.",
 ],
 "requirements": [
   "Self-audit executed quarterly with published report.",
   "All five audit dimensions checked.",
   "Findings tracked to closure.",
   "Mastery path documented from record 1 to record 34.",
 ],
 "standards": [
   "Coverage target 1.0 - every source record complete.",
   "Zero stale scores tolerated.",
   "Audit performed by reviewers outside daily operations.",
   "Year-over-year trend reported.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems (audit practice).",
 ],
 "sig_lens": ("The Signature Reliability Doctrine ends where it began: with the scale turned "
   "on itself. The Signature self-audit weighs the weigher, and the mastery record is the "
   "proof that the whole teaching holds together - every source weighed, every claim "
   "corroborated, every correction logged, including the system's own."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks) == list(range(1, 35)), "ladder ranks must be 1..34 in order"
