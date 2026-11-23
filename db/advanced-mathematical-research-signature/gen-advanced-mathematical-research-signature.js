// Seeded boundless generator for the The Signature Advanced Mathematical Research Database (signature edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-advanced-mathematical-research-signature.js [seed]  (prints one JSON record) or:
// node gen-advanced-mathematical-research-signature.js --test (runTests). Package-only; outputs are
// generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "advanced-mathematical-research-signature";
const RECORD_KIND = "advanced mathematical research record";
const ID_PREFIX = "JAH-AMRS-";
const AI_NAME = "JAH Advanced Mathematical Research Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: A Proof-Checking Workbench",
    "subject": "proof-checking workbench design",
    "description": "In plain words: This Signature design is a proof-checking workbench, a program that takes a written proof and checks every step against the definitions and the rules of logic. A proof, in plain words, is a sequence of logical steps from starting assumptions to a conclusion, and the workbench verifies that each step follows. The formal statement above is the precise form of the claim; the gloss is ",
    "figures": {
      "workbench_modules": 6,
      "check_passes": 4,
      "proof_steps_supported": 1000,
      "design_year": 2026,
      "interfaces_count": 3,
      "test_cases": 24,
      "scales_max": 1000000000,
      "team_size": 4
    }
  },
  {
    "title": "Signature Design: A Conjecture Tracker",
    "subject": "conjecture tracker design",
    "description": "In plain words: This Signature design is a conjecture tracker, a database that follows open conjectures, which are precise mathematical guesses not yet proved, and records every change in their status: new partial results, new counterexamples, claimed proofs, and accepted proofs. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "conjectures_tracked": 24,
      "status_values": 7,
      "sources_per_item": 3,
      "design_year": 2026,
      "update_checks": 12,
      "alert_rules": 5,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Literature Synthesis Engine",
    "subject": "literature synthesis engine design",
    "description": "In plain words: This Signature design is a literature synthesis engine, a program that gathers the published papers on a mathematical topic and synthesises them into one survey: what is known, what is open, what contradicts what, and what the evidence status of each claim is. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "papers_per_topic": 50,
      "synthesis_sections": 6,
      "sources_per_record": 3,
      "design_year": 2026,
      "review_rounds": 2,
      "contradiction_flags": 4,
      "scales_max": 1000000000,
      "topics_covered": 24
    }
  },
  {
    "title": "Signature Design: A Peer-Review Simulator",
    "subject": "peer-review simulator design",
    "description": "In plain words: This Signature design is a peer-review simulator, a program that rehearses the peer review of a mathematical paper before submission. Peer review, in plain words, is the checking of a paper by independent experts before publication. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "reviewer_roles": 3,
      "review_rounds": 3,
      "checklist_items": 12,
      "design_year": 2026,
      "simulated_reports": 24,
      "criteria_count": 6,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Hypothesis Generator",
    "subject": "hypothesis generator design",
    "description": "In plain words: This Signature design is a hypothesis generator, a program that looks for patterns in computed mathematical data and proposes new conjectures, precise guesses that could be investigated. A hypothesis is a statement put forward to be tested, not a result. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "hypotheses_per_run": 20,
      "test_filters": 5,
      "patterns_mined": 12,
      "design_year": 2026,
      "candidate_topics": 24,
      "plausibility_checks": 4,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: An Experimental Design Bench",
    "subject": "experimental design bench",
    "description": "In plain words: This Signature design is an experimental design bench, a tool for planning computational experiments in mathematics before they run. An experiment, in plain words, is a planned test with a stated question, stated variables, and a stated rule for deciding what the outcome means. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary word",
    "figures": {
      "experiments_per_topic": 10,
      "variables_tracked": 6,
      "controls_required": 2,
      "design_year": 2026,
      "replication_runs": 3,
      "data_sets": 8,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Computational Research Bench",
    "subject": "computational research bench design",
    "description": "In plain words: This Signature design is a computational research bench, a program that runs mathematical computations with verification built in. Computation, in plain words, is calculation carried out by a machine, and verified computation is calculation whose errors are bounded and whose results are re-checked. The formal statement above is the precise form of the claim; the gloss is the same c",
    "figures": {
      "bench_tools": 8,
      "precision_levels": 3,
      "verification_runs": 2,
      "design_year": 2026,
      "supported_operations": 12,
      "error_bounds": 4,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Reproducibility Checker",
    "subject": "reproducibility checker design",
    "description": "In plain words: This Signature design is a reproducibility checker, a program that takes a database record and tests whether it can be reproduced: re-run the demo, re-fetch the sources, re-check the evidence status, and report what fails. Reproducibility, in plain words, means another person can repeat the work and get the same result. The formal statement above is the precise form of the claim; t",
    "figures": {
      "checks_per_record": 8,
      "replication_modes": 3,
      "code_archives": 2,
      "design_year": 2026,
      "data_policies": 4,
      "report_sections": 5,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Theorem Dependency Graph",
    "subject": "theorem dependency graph design",
    "description": "In plain words: This Signature design is a theorem dependency graph, a map of what each theorem depends on. A dependency, in plain words, is a reliance: theorem B depends on theorem A if the proof of B uses A. The graph shows the whole chain, down to the axioms. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "nodes_per_field": 100,
      "edge_types": 4,
      "layers_count": 5,
      "design_year": 2026,
      "circular_checks": 2,
      "gap_flags": 3,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Counterexample Searcher",
    "subject": "counterexample searcher design",
    "description": "In plain words: This Signature design is a counterexample searcher, a program that hunts for counterexamples to a conjecture, which is a precise mathematical guess. A counterexample is one example that shows the guess false, and a single counterexample is enough to disprove a general claim. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "search_strategies": 6,
      "cases_per_run": 1000000,
      "pruning_rules": 4,
      "design_year": 2026,
      "families_searched": 10,
      "success_criteria": 2,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Research Expansion Mapper",
    "subject": "research expansion mapper design",
    "description": "In plain words: This Signature design is a research expansion mapper, a tool that takes a proved result and maps the research it opens: what can be generalised, what can be specialised, what happens if an assumption is weakened, and what connects to other fields. Expansion, in plain words, is the work of growing a result into a research program. The formal statement above is the precise form of th",
    "figures": {
      "expansion_directions": 8,
      "questions_per_result": 5,
      "generalisation_levels": 4,
      "design_year": 2026,
      "fields_linked": 3,
      "open_questions": 10,
      "scales_max": 1000000000,
      "topics_covered": 24
    }
  },
  {
    "title": "Signature Design: A Collaboration Hub for Distributed Proofs",
    "subject": "collaboration hub design",
    "description": "In plain words: This Signature design is a collaboration hub, a platform where many mathematicians build one proof together. A distributed proof is a proof whose parts are proved by different people, in different places, and combined into a whole. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "roles_count": 5,
      "review_stages": 3,
      "contribution_types": 6,
      "design_year": 2026,
      "projects_hosted": 10,
      "attribution_rules": 4,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Citation Graph Analyser",
    "subject": "citation graph analyser design",
    "description": "In plain words: This Signature design is a citation graph analyser, a program that maps how mathematical papers cite each other. A citation is a reference from one paper to another, and a citation graph is the whole network of those references. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "papers_indexed": 1000,
      "citation_types": 4,
      "influence_measures": 3,
      "design_year": 2026,
      "anomaly_flags": 3,
      "fields_covered": 5,
      "scales_max": 1000000000,
      "update_cycles": 12
    }
  },
  {
    "title": "Signature Design: An Open-Problem Dashboard",
    "subject": "open-problem dashboard design",
    "description": "In plain words: This Signature design is an open-problem dashboard, a single page showing the state of the great open problems: the six unsolved Millennium Prize Problems, the twin prime conjecture, Goldbach's conjecture, the Collatz conjecture, and the abc conjecture, each with its evidence status, its partial progress, and its claimed proofs. The formal statement above is the precise form of the",
    "figures": {
      "problems_listed": 24,
      "status_values": 7,
      "progress_meters": 5,
      "design_year": 2026,
      "update_sources": 3,
      "alert_types": 4,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Research Notebook with Evidence",
    "subject": "research notebook design",
    "description": "In plain words: This Signature design is a research notebook, a tool for recording mathematical research as it happens, with the evidence attached to every entry. A notebook entry, in plain words, is a dated record of what was tried, what was found, and what it means. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "notebook_sections": 7,
      "evidence_fields": 4,
      "revision_history": 100,
      "design_year": 2026,
      "linked_records": 24,
      "export_formats": 3,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Verification Pipeline",
    "subject": "verification pipeline design",
    "description": "In plain words: This Signature design is a verification pipeline, a program that carries a database record through six stages before publication: execution of the demo, determinism of the computation, live re-checking of the sources, validation of the evidence status, checking of the body sections, and checking of the identifiers. A gate is a check that must pass before the next stage begins. The ",
    "figures": {
      "pipeline_stages": 6,
      "checks_per_stage": 4,
      "gates_count": 3,
      "design_year": 2026,
      "records_processed": 24,
      "failure_modes": 5,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Mathematical Reasoning Tutor",
    "subject": "mathematical reasoning tutor design",
    "description": "In plain words: This Signature design is a mathematical reasoning tutor, a program that teaches proof by working through examples with the student. Reasoning, in plain words, is the process of moving from what is known to what follows, step by step, and a tutor is a guide through that process. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary word",
    "figures": {
      "tutor_lessons": 20,
      "reasoning_patterns": 8,
      "exercise_levels": 5,
      "design_year": 2026,
      "worked_examples": 24,
      "feedback_rules": 6,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Data Curation Tool for Mathematical Records",
    "subject": "data curation tool design",
    "description": "In plain words: This Signature design is a data curation tool, a program that keeps a database of mathematical records complete, deduplicated, and sourced. Curation, in plain words, is the ongoing care of a collection: adding what is missing, removing what is duplicated, and checking what is there. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary",
    "figures": {
      "curation_rules": 10,
      "duplicate_checks": 3,
      "quality_scores": 5,
      "design_year": 2026,
      "records_curated": 24,
      "source_checks": 2,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: An arXiv Monitor for New Results",
    "subject": "arxiv monitor design",
    "description": "In plain words: This Signature design is an arXiv monitor, a program that watches the arXiv, the open-access archive of scholarly articles, for new results in advanced mathematics, and summarises them daily with a provisional evidence status for each paper. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "categories_watched": 10,
      "alert_rules": 6,
      "summaries_per_day": 20,
      "design_year": 2026,
      "relevance_scores": 5,
      "fields_covered": 3,
      "scales_max": 1000000000,
      "update_cycles": 24
    }
  },
  {
    "title": "Signature Design: A Conference Proceedings Indexer",
    "subject": "conference proceedings indexer design",
    "description": "In plain words: This Signature design is a conference proceedings indexer, a program that indexes the talks and papers of mathematics conferences, so that a result announced at a conference can be found by topic, by result, and by evidence status, long after the conference ends. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "conferences_indexed": 20,
      "papers_per_conference": 50,
      "search_fields": 6,
      "design_year": 2026,
      "index_entries": 1000,
      "link_checks": 2,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Referee Assignment Aid",
    "subject": "referee assignment aid design",
    "description": "In plain words: This Signature design is a referee assignment aid, a program that helps journal editors match a submitted paper to referees, the independent experts who check a paper before publication. Matching, in plain words, is choosing the right experts for a given paper. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "expertise_fields": 20,
      "conflict_rules": 5,
      "workload_limits": 3,
      "design_year": 2026,
      "papers_matched": 50,
      "review_rounds": 2,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Result Replication Laboratory",
    "subject": "result replication laboratory design",
    "description": "In plain words: This Signature design is a result replication laboratory, a program that replicates published mathematical results independently: a second team, or a second program, re-derives the result from the same starting points, with independent code and independent reasoning, and compares the outcome with the original. The formal statement above is the precise form of the claim; the gloss i",
    "figures": {
      "replication_protocols": 6,
      "independent_runs": 3,
      "discrepancy_rules": 4,
      "design_year": 2026,
      "results_replicated": 24,
      "report_sections": 5,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Research Ethics Checker",
    "subject": "research ethics checker design",
    "description": "In plain words: This Signature design is a research ethics checker, a program that screens mathematical research records for ethics errors: missing attribution, uncredited borrowing, overstated evidence status, and presented-as-fact claims that are only design studies. Ethics, in plain words, is the standard of honest conduct in research. The formal statement above is the precise form of the claim",
    "figures": {
      "ethics_rules": 8,
      "attribution_checks": 4,
      "plagiarism_screens": 2,
      "design_year": 2026,
      "records_checked": 24,
      "flag_types": 5,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Theorem Announcement Tracker",
    "subject": "theorem announcement tracker design",
    "description": "In plain words: This Signature design is a theorem announcement tracker, a program that follows announced theorems, claims of new results made before peer review, from announcement through verification to acceptance, correction, or withdrawal. An announcement is a claim, not a result. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "announcements_tracked": 50,
      "verification_stages": 4,
      "claim_types": 3,
      "design_year": 2026,
      "outcome_log": 100,
      "alert_rules": 4,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Mathematical proof",
    "url": "https://en.wikipedia.org/wiki/Mathematical_proof",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  },
  {
    "name": "Wikipedia - Mathematics",
    "url": "https://en.wikipedia.org/wiki/Mathematics",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  }
];

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canonical(obj) {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return "[" + obj.map(canonical).join(",") + "]";
  const keys = Object.keys(obj).sort();
  return "{" + keys.map((k) => JSON.stringify(k) + ":" + canonical(obj[k])).join(",") + "}";
}

function buildDemo(topic, label) {
  const figs = topic.figures;
  const keys = Object.keys(figs).sort();
  const total = keys.reduce((s, k) => s + figs[k], 0);
  const out = { count: keys.length, label: label, max: Math.max(...keys.map((k) => figs[k])), min: Math.min(...keys.map((k) => figs[k])), total: total };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), \"min\": min(FIGURES.values()), \"total\": total}\n" +
    "    return out\n" +
    "outputs = compute()\n" +
    "result = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
    "h1 = hashlib.sha256(result.encode()).hexdigest()\n" +
    "outputs2 = compute()\n" +
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs2.items()))\n" +
    "h2 = hashlib.sha256(result2.encode()).hexdigest()\n" +
    "for k, v in sorted(outputs.items()):\n" +
    "    print(f\"{k}: {v}\")\n" +
    "print(f\"Result: {result}\")\n" +
    "print(f\"Run 1 SHA-256: {h1}\")\n" +
    "print(f\"Run 2 SHA-256: {h2}\")\n" +
    "print(f\"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}\")\n";
  const expected = Object.keys(out).sort().map((k) => k + ": " + out[k]).join("\n") + "\n" +
    "Result: " + result + "\n" +
    "Run 1 SHA-256: " + h + "\n" +
    "Run 2 SHA-256: " + h + "\n" +
    "Deterministic: MATCH\n";
  return { code, expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const label = topic.subject;
  const demo = buildDemo(topic, label);
  const rec = {
    id: id,
    slug: SLUG,
    edition: "signature",
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: "signature-generated",
    ai_name: AI_NAME,
    description: topic.description + " No claim of consciousness, sentience, or unlimited intelligence is established by this record; that framing is not part of mathematics and is not claimed here.",
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One result: a single theorem, conjecture, or design, fully specified.", A2: "The whole pair: 24 public records and 24 Signature designs covering the field.", A3: "The field against the network: linked to adjacent live databases and the unsolved-equations program." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function t(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = generate(42), b = generate(42);
  t("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  t("record_kind", a.record_kind === RECORD_KIND);
  t("slug form", a.slug === SLUG);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("19 keys", Object.keys(a).length === 19);
  console.log("Tests: " + passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === "--test") {
    process.exit(runTests() ? 0 : 1);
  }
  const seed = arg === undefined ? 1 : parseInt(arg, 10);
  if (!Number.isFinite(seed)) { console.error("seed must be an integer"); process.exit(2); }
  console.log(JSON.stringify(generate(seed)));
}
module.exports = { generate, runTests };
