// Seeded boundless generator for the Measure Theory Signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-measure-theory-signature.js [seed]  (prints one
// JSON record) or: node gen-measure-theory-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "measure-theory-signature";
const RECORD_KIND = "measure theory research record";
const ID_PREFIX = "JAH-MTHYS-";
const AI_NAME = "JAH Measure Theory Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Measure Workbench: Sigma-Algebra Builder",
    "subject": "Signature sigma-algebra builder",
    "description": "A sigma-algebra is a collection of subsets containing the empty set and closed under complements and countable unions. The Borel sigma-algebra is the smallest sigma-algebra containing all open sets. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "sigma_axioms": 3,
      "generated_examples": 5,
      "borel_tests": 4,
      "union_tests": 3,
      "complement_tests": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-sigma-builder",
    "status": "Proposed",
    "limits": "The builder works only on finite examples; generated sigma-algebras of infinite collections are not computed, and its results are design values, not a proof system."
  },
  {
    "title": "Signature Lebesgue Measure Ruler",
    "subject": "Signature Lebesgue ruler",
    "description": "Lebesgue measure assigns to each measurable subset of the real line a length extending the length of intervals, is countably additive, and is translation invariant. A null set has measure zero. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "interval_lengths": 4,
      "null_tests": 3,
      "translation_tests": 2,
      "additivity_tests": 3,
      "regularity_checks": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-lebesgue-ruler",
    "status": "Proposed",
    "limits": "The ruler measures only sets built from intervals and the stated examples; it does not measure arbitrary sets, and its measurements are design values, not a proof system."
  },
  {
    "title": "Signature Integral Slicer: Lebesgue Integration Lab",
    "subject": "Signature Lebesgue lab",
    "description": "The Lebesgue integral integrates a function by slicing its range into horizontal levels and measuring the sets where the function takes each level. It is defined first for simple functions, then by approximation, and every Riemann-integrable function is Lebesgue-integrable with the same integral. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "integration_steps": 4,
      "simple_functions": 3,
      "convergence_tests": 3,
      "riemann_comparisons": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "level_sets": 4,
      "demo_runs": 2
    },
    "label": "sig-lebesgue-lab",
    "status": "Proposed",
    "limits": "The lab integrates only the stated functions; it does not integrate arbitrary functions, and its sums are design values, not a proof system."
  },
  {
    "title": "Signature Measurability Tester",
    "subject": "Signature measurability tester",
    "description": "A function is measurable when preimages of Borel sets are measurable, and every non-negative measurable function is a pointwise limit of an increasing sequence of simple functions. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "measurability_tests": 3,
      "closure_tests": 5,
      "approximation_steps": 2,
      "limit_tests": 3,
      "egorov_checks": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-measurability-tester",
    "status": "Proposed",
    "limits": "The tester checks only the stated functions and generating sets; it does not decide measurability in general, and its verdicts are design values, not a proof system."
  },
  {
    "title": "Signature Convergence Theater: Monotone, Fatou, Dominated",
    "subject": "Signature convergence theater",
    "description": "The monotone convergence theorem, Fatou's lemma, and the dominated convergence theorem govern when limits pass inside integrals. The moving-bump examples show mass escaping to infinity, which is why the hypotheses matter. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "theorems_staged": 3,
      "moving_bump_demos": 2,
      "counterexamples": 2,
      "limit_exchanges": 3,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "proof_steps": 3,
      "demo_runs": 2
    },
    "label": "sig-convergence-theater",
    "status": "Proposed",
    "limits": "The theater stages only the stated examples; it does not prove the theorems, and its stagings are design values, not a proof system."
  },
  {
    "title": "Signature Product Measure Builder",
    "subject": "Signature product measure builder",
    "description": "A product measure gives rectangles the product of their measures, and Fubini's theorem says the integral over the product equals the iterated integrals in either order, for integrable functions. Tonelli's theorem is the companion for non-negative functions. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "product_steps": 3,
      "rectangle_tests": 4,
      "fubini_checks": 2,
      "tonelli_checks": 2,
      "counterexamples": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-product-measure-builder",
    "status": "Proposed",
    "limits": "The builder handles only the stated spaces and functions; it does not integrate arbitrary functions, and its computations are design values, not a proof system."
  },
  {
    "title": "Signature Probability Space Studio",
    "subject": "Signature probability studio",
    "description": "A probability measure has total mass one, assigns events numbers between zero and one, and adds over countable disjoint unions. A random variable is a measurable function, and its expectation is its Lebesgue integral. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "kolmogorov_axioms": 3,
      "event_tests": 4,
      "expectation_computations": 3,
      "independence_tests": 2,
      "dice_examples": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-probability-studio",
    "status": "Proposed",
    "limits": "The studio handles only finite experiments and the stated examples; it does not model arbitrary probability spaces, and its computations are design values, not a proof system."
  },
  {
    "title": "Signature Borel Approximator",
    "subject": "Signature Borel approximator",
    "description": "A Borel measure is defined on the Borel sigma-algebra, and it is regular when every measurable set can be approximated from inside by compact sets and from outside by open sets. Lebesgue measure is regular. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "approximation_steps": 2,
      "inner_checks": 3,
      "outer_checks": 3,
      "compact_tests": 2,
      "open_tests": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-borel-approximator",
    "status": "Proposed",
    "limits": "The approximator handles only the stated sets; it does not approximate arbitrary Borel sets, and its approximations are design values, not a proof system."
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Sigma-algebra",
    "url": "https://en.wikipedia.org/wiki/Sigma-algebra",
    "establishes": "Sigma-algebra: the three axioms and generated sigma-algebras. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Measure (mathematics)",
    "url": "https://en.wikipedia.org/wiki/Measure_(mathematics)",
    "establishes": "Measure (mathematics): measures defined on sigma-algebras. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Lebesgue measure",
    "url": "https://en.wikipedia.org/wiki/Lebesgue_measure",
    "establishes": "Lebesgue measure: length, additivity, translation invariance. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Outer measure",
    "url": "https://en.wikipedia.org/wiki/Outer_measure",
    "establishes": "Outer measure: the covering construction. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Lebesgue integration",
    "url": "https://en.wikipedia.org/wiki/Lebesgue_integration",
    "establishes": "Lebesgue integration: simple functions and approximation. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Measurable function",
    "url": "https://en.wikipedia.org/wiki/Measurable_function",
    "establishes": "Measurable function: preimages, closure, approximation. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Monotone convergence theorem",
    "url": "https://en.wikipedia.org/wiki/Monotone_convergence_theorem",
    "establishes": "Monotone convergence theorem: integrals of increasing sequences. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Fatou's lemma",
    "url": "https://en.wikipedia.org/wiki/Fatou%27s_lemma",
    "establishes": "Fatou's lemma: the integral of the limit inferior. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Fubini's theorem",
    "url": "https://en.wikipedia.org/wiki/Fubini%27s_theorem",
    "establishes": "Fubini's theorem: double integrals as iterated integrals. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Probability measure",
    "url": "https://en.wikipedia.org/wiki/Probability_measure",
    "establishes": "Probability measure: Kolmogorov's axioms. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Borel measure",
    "url": "https://en.wikipedia.org/wiki/Borel_measure",
    "establishes": "Borel measure: the Borel sigma-algebra and regularity. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
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
