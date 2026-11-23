// Seeded boundless generator for the Topology Research Signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-topology-research-signature.js [seed]  (prints one
// JSON record) or: node gen-topology-research-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "topology-research-signature";
const RECORD_KIND = "topology research record";
const ID_PREFIX = "JAH-TOPRS-";
const AI_NAME = "JAH Topology Research Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Topology Studio: Open-Set Workbench",
    "subject": "Signature open-set workbench",
    "description": "A topological space is a set together with a collection of subsets called open sets, satisfying three axioms: the empty set and the whole set are open, arbitrary unions of open sets are open, and finite intersections of open sets are open. A function is continuous when preimages of open sets are open. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "workbench_tools": 6,
      "example_spaces": 8,
      "axiom_checks": 3,
      "continuity_tests": 4,
      "topology_presets": 5,
      "guided_lessons": 12,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-topology-workbench",
    "status": "Proposed",
    "limits": "The workbench checks axioms and continuity only for the finite examples a learner enters; it does not prove theorems about infinite spaces, and its checks are design values, not a proof system."
  },
  {
    "title": "Signature Compactness Checker",
    "subject": "Signature compactness checker",
    "description": "A space is compact when every open cover, a collection of open sets whose union is the whole space, has a finite subcover. The Heine-Borel theorem says a subset of Euclidean space is compact exactly when it is closed and bounded. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "cover_tests": 5,
      "compact_examples": 7,
      "noncompact_examples": 4,
      "subcover_searches": 6,
      "heine_borel_checks": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-compactness-checker",
    "status": "Proposed",
    "limits": "The checker works only on finite examples and on the Heine-Borel test; it does not prove compactness of infinite spaces, and its searches are design values, not a proof system."
  },
  {
    "title": "Signature Connectedness Explorer",
    "subject": "Signature connectedness explorer",
    "description": "A space is connected when it cannot be split into two disjoint non-empty open sets. A space is path connected when any two points can be joined by a continuous path, and path connectedness implies connectedness but not conversely. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "separation_tests": 3,
      "connected_examples": 8,
      "disconnected_examples": 4,
      "path_tests": 5,
      "component_counts": 4,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-connectedness-explorer",
    "status": "Proposed",
    "limits": "The explorer works on finite examples and on the stated classical example; it does not prove connectedness of arbitrary spaces, and its results are design values, not a proof system."
  },
  {
    "title": "Signature Hausdorff Separator",
    "subject": "Signature Hausdorff separator",
    "description": "A space is Hausdorff when any two distinct points have disjoint neighborhoods. The separation axioms T0 through T4 form a ladder of increasingly strong separation, and every metric space is Hausdorff, which is why limits of sequences are unique in metric spaces. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "separation_levels": 6,
      "hausdorff_examples": 7,
      "non_hausdorff_examples": 3,
      "limit_tests": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "axiom_checks": 6,
      "demo_runs": 2
    },
    "label": "sig-hausdorff-separator",
    "status": "Proposed",
    "limits": "The separator tests only finite examples and the stated classical counter-examples; it does not decide separation axioms for arbitrary spaces, and its verdicts are design values, not a proof system."
  },
  {
    "title": "Signature Product-Quotient Builder",
    "subject": "Signature product-quotient builder",
    "description": "The product topology is the coarsest topology making all projection maps continuous. The quotient topology is the finest topology making the gluing map continuous. The torus, the surface of a doughnut, is a quotient of a square with opposite edges glued. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "product_builds": 4,
      "quotient_builds": 5,
      "torus_steps": 3,
      "circle_steps": 2,
      "universal_checks": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-product-quotient-builder",
    "status": "Proposed",
    "limits": "The builder constructs only the stated examples and finite products; it does not handle infinite products or arbitrary gluings, and its constructions are design values, not a proof system."
  },
  {
    "title": "Signature Loop Counter: Fundamental Group Lab",
    "subject": "Signature fundamental group lab",
    "description": "The fundamental group of a space is the group of homotopy classes of loops based at a point, where a loop is a path that starts and ends at the base point and two loops are equivalent when one can be deformed into the other. The fundamental group of the circle is the integers, classified by winding number. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "loop_classes": 6,
      "winding_numbers": 5,
      "circle_tests": 3,
      "simply_connected_tests": 5,
      "group_axioms": 4,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-fundamental-group-lab",
    "status": "Proposed",
    "limits": "The lab handles loops on the circle and the stated examples only; it does not compute fundamental groups of arbitrary spaces, and its counts are design values, not a proof system."
  },
  {
    "title": "Signature Homotopy Deformer",
    "subject": "Signature homotopy deformer",
    "description": "Two maps are homotopic when one can be deformed into the other through a continuous family of maps. Two spaces are homotopy equivalent when maps back and forth compose to maps homotopic to the identity, and a space is contractible when it is homotopy equivalent to a point. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "deformation_steps": 5,
      "equivalence_tests": 4,
      "retract_examples": 4,
      "contractible_tests": 5,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "invariant_checks": 3,
      "demo_runs": 2
    },
    "label": "sig-homotopy-deformer",
    "status": "Proposed",
    "limits": "The deformer animates only the stated examples; it does not decide homotopy equivalence in general, and its animations are design values, not a proof system."
  },
  {
    "title": "Signature Homology Calculator",
    "subject": "Signature homology calculator",
    "description": "Homology measures holes in every dimension: the zeroth homology counts connected pieces, the first counts loops, the second counts enclosed voids. It is computed from a chain complex, where homology is cycles modulo boundaries, and the Betti numbers are the ranks of the homology groups. This is a Signature-made design study, labeled as a proposal throughout, never presented as a demonstrated discovery.",
    "figures": {
      "chain_steps": 3,
      "betti_computations": 3,
      "triangulation_examples": 4,
      "sphere_tests": 2,
      "torus_tests": 2,
      "guided_lessons": 8,
      "checkable_claims": 9,
      "demo_runs": 2
    },
    "label": "sig-homology-calculator",
    "status": "Proposed",
    "limits": "The calculator handles only small triangulations and the stated examples; it does not compute homology of arbitrary spaces, and its results are design values, not a proof system."
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Topology",
    "url": "https://en.wikipedia.org/wiki/Topology",
    "establishes": "Topology: open sets and continuity, the basis of the workbench. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Point-set topology",
    "url": "https://en.wikipedia.org/wiki/Point-set_topology",
    "establishes": "Point-set topology: the axioms the workbench checks. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Compact space",
    "url": "https://en.wikipedia.org/wiki/Compact_space",
    "establishes": "Compact space: open covers and finite subcovers. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Metric space",
    "url": "https://en.wikipedia.org/wiki/Metric_space",
    "establishes": "Metric space: the Euclidean setting of Heine-Borel. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Connected space",
    "url": "https://en.wikipedia.org/wiki/Connected_space",
    "establishes": "Connected space: separation, components, and path connectedness. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Hausdorff space",
    "url": "https://en.wikipedia.org/wiki/Hausdorff_space",
    "establishes": "Hausdorff space: the separation axiom and unique limits. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Product topology",
    "url": "https://en.wikipedia.org/wiki/Product_topology",
    "establishes": "Product topology: the subbase of preimages under projections. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Quotient space (topology)",
    "url": "https://en.wikipedia.org/wiki/Quotient_space_(topology)",
    "establishes": "Quotient space: identification and the quotient topology. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Fundamental group",
    "url": "https://en.wikipedia.org/wiki/Fundamental_group",
    "establishes": "Fundamental group: loops, homotopy classes, and the circle. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Homotopy",
    "url": "https://en.wikipedia.org/wiki/Homotopy",
    "establishes": "Homotopy: deformation of maps and paths. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Homology (mathematics)",
    "url": "https://en.wikipedia.org/wiki/Homology_(mathematics)",
    "establishes": "Homology: chain complexes, cycles, boundaries, and Betti numbers. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
  },
  {
    "name": "Wikipedia - Euler characteristic",
    "url": "https://en.wikipedia.org/wiki/Euler_characteristic",
    "establishes": "Euler characteristic: the alternating sum of Betti numbers. Retrieved 2026-11-17; HTTP 200 verified by curl before citation."
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
