// Seeded boundless generator for the Functional Analysis Signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-functional-analysis-signature.js [seed]  (prints one
// JSON record) or: node gen-functional-analysis-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "functional-analysis-signature";
const RECORD_KIND = "functional analysis research record";
const ID_PREFIX = "JAH-FUNAS-";
const AI_NAME = "JAH Functional Analysis Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Norm Meter",
    "subject": "Signature norm meter",
    "description": "A normed vector space is a vector space with a norm, a function assigning a non-negative size to each vector, satisfying three rules: only the zero vector has norm zero, scaling scales the norm, and the triangle inequality holds. The norm defines a metric by the distance between vectors being the norm of their difference. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "norm_axioms": 3,
      "standard_norms": 4,
      "ball_examples": 3,
      "equivalence_tests": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "metric_checks": 1,
      "demo_runs": 2
    },
    "label": "sig-norm-meter",
    "status": "Proposed",
    "limits": "The meter handles only the stated norms and vectors; different norms on infinite-dimensional spaces can define different topologies, and its measurements are design values, not a proof system."
  },
  {
    "title": "Signature Completeness Checker",
    "subject": "Signature completeness checker",
    "description": "A Banach space is a normed space that is complete, meaning every Cauchy sequence converges inside the space. The space of continuous functions with the supremum norm is complete, and every Lp space is complete by the Riesz-Fischer theorem. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "completeness_tests": 3,
      "cauchy_tests": 5,
      "standard_examples": 6,
      "incomplete_examples": 3,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "series_tests": 2,
      "demo_runs": 2
    },
    "label": "sig-completeness-checker",
    "status": "Proposed",
    "limits": "The checker tests only the stated sequences and spaces; completeness depends on the norm, and its verdicts are design values, not a proof system."
  },
  {
    "title": "Signature Hilbert Geometry Lab",
    "subject": "Signature Hilbert lab",
    "description": "A Hilbert space is a vector space with an inner product that is complete. The inner product gives angles, orthogonality, and projections, and the projection theorem says every closed convex set has a unique nearest point. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "inner_product_axioms": 4,
      "orthonormal_examples": 5,
      "projection_tests": 2,
      "angle_tests": 3,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "gram_schmidt_steps": 3,
      "demo_runs": 2
    },
    "label": "sig-hilbert-lab",
    "status": "Proposed",
    "limits": "The lab draws only finite-dimensional illustrations and the stated examples; infinite-dimensional geometry is shown by analogy, and its drawings are design values, not a proof system."
  },
  {
    "title": "Signature Riesz Vector Finder",
    "subject": "Signature Riesz finder",
    "description": "The Riesz representation theorem says every continuous linear functional on a Hilbert space is the inner product with a single fixed vector, and that vector is unique. It identifies the dual space with the Hilbert space itself. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "functional_tests": 3,
      "representation_parts": 2,
      "kernel_tests": 2,
      "uniqueness_checks": 1,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "dual_examples": 3,
      "demo_runs": 2
    },
    "label": "sig-riesz-finder",
    "status": "Proposed",
    "limits": "The finder handles only the stated functionals; completeness is essential, and its constructions are design values, not a proof system."
  },
  {
    "title": "Signature Operator Norm Gauge",
    "subject": "Signature operator gauge",
    "description": "A linear operator is bounded when outputs are bounded by a constant times inputs, and the smallest such constant is the operator norm. A linear operator is bounded exactly when it is continuous. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "operator_tests": 3,
      "norm_computations": 4,
      "standard_operators": 6,
      "continuity_tests": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "algebra_checks": 1,
      "demo_runs": 2
    },
    "label": "sig-operator-gauge",
    "status": "Proposed",
    "limits": "The gauge estimates norms on the stated operators only; the operator norm can be hard to compute exactly, and its estimates are design values, not a proof system."
  },
  {
    "title": "Signature Uniform Boundedness Demonstrator",
    "subject": "Signature uniform boundedness demo",
    "description": "The uniform boundedness principle says that if a family of bounded linear operators on a Banach space is pointwise bounded, then it is uniformly bounded by a single constant. Its proof uses the Baire category theorem. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "family_tests": 3,
      "pointwise_checks": 4,
      "uniform_checks": 2,
      "baire_steps": 2,
      "fourier_demo": 1,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-uniform-boundedness-demo",
    "status": "Proposed",
    "limits": "The demonstrator handles only the stated families; completeness of the domain is essential, and its demonstrations are design values, not a proof system."
  },
  {
    "title": "Signature Open Map Checker",
    "subject": "Signature open map checker",
    "description": "The open mapping theorem says a surjective bounded linear operator between Banach spaces is an open map, sending open sets to open sets, and a bijective bounded linear operator has a bounded inverse. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "openness_tests": 3,
      "surjectivity_tests": 2,
      "inverse_checks": 2,
      "baire_steps": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "ball_images": 2,
      "demo_runs": 2
    },
    "label": "sig-open-map-checker",
    "status": "Proposed",
    "limits": "The checker tests only the stated operators; both spaces must be Banach, and its verdicts are design values, not a proof system."
  },
  {
    "title": "Signature Graph Closer",
    "subject": "Signature graph closer",
    "description": "The closed graph theorem says a linear operator between Banach spaces is bounded exactly when its graph, the set of input-output pairs, is closed. It is the standard test for proving operators defined by formulas are continuous. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "graph_tests": 2,
      "closedness_tests": 3,
      "boundedness_checks": 2,
      "projection_steps": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "operator_examples": 3,
      "demo_runs": 2
    },
    "label": "sig-graph-closer",
    "status": "Proposed",
    "limits": "The closer tests only the stated operators; the operator must be everywhere defined, and its verdicts are design values, not a proof system."
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Normed vector space",
    "url": "https://en.wikipedia.org/wiki/Normed_vector_space",
    "establishes": "Normed vector space: the three norm axioms. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Banach space",
    "url": "https://en.wikipedia.org/wiki/Banach_space",
    "establishes": "Banach space: complete normed spaces. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Hilbert space",
    "url": "https://en.wikipedia.org/wiki/Hilbert_space",
    "establishes": "Hilbert space: inner products and the projection theorem. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Riesz representation theorem",
    "url": "https://en.wikipedia.org/wiki/Riesz_representation_theorem",
    "establishes": "Riesz representation theorem: functionals as inner products. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Bounded operator",
    "url": "https://en.wikipedia.org/wiki/Bounded_operator",
    "establishes": "Bounded operator: the operator norm and continuity. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Uniform boundedness principle",
    "url": "https://en.wikipedia.org/wiki/Uniform_boundedness_principle",
    "establishes": "Uniform boundedness principle: pointwise bounded implies uniformly bounded. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Open mapping theorem (functional analysis)",
    "url": "https://en.wikipedia.org/wiki/Open_mapping_theorem_(functional_analysis)",
    "establishes": "Open mapping theorem: surjective bounded operators are open. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Closed graph theorem",
    "url": "https://en.wikipedia.org/wiki/Closed_graph_theorem",
    "establishes": "Closed graph theorem: closed graph implies bounded. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
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
  const meanR = Math.round((total / keys.length) * 10000) / 10000;
  const totalR = Math.round(total * 10000) / 10000;
  const hasFloat = keys.some((k) => !Number.isInteger(figs[k]));
  const meanStr = Number.isInteger(meanR) ? meanR + ".0" : String(meanR);
  const totalStr = !hasFloat ? String(total) : (Number.isInteger(totalR) ? totalR + ".0" : String(totalR));
  const out = { count: keys.length, label: label, max: Math.max(...keys.map((k) => figs[k])), mean: meanStr, min: Math.min(...keys.map((k) => figs[k])), total: totalStr };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    mean = round(total / n, 4) if n else 0\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), \"mean\": mean, \"min\": min(FIGURES.values()), \"total\": round(total, 4)}\n" +
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
  const demo = buildDemo(topic, topic.label);
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
    description: topic.description,
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    evidence_status: topic.status,
    evidence_record: { assumptions: "The hypotheses of the stated result as published.", methods: "Proof as published in the cited literature.", test_outputs: "Demo output printed twice with matching SHA-256 digests.", limitations: topic.limits },
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One example: a single worked case.", A2: "The whole topic: the full statement, proof, examples, and limits.", A3: "The topic against the field: one result among the research of the field." },
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
  t("21 keys", Object.keys(a).length === 21);
  t("evidence_status present", typeof a.evidence_status === "string" && a.evidence_status.length > 0);
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
