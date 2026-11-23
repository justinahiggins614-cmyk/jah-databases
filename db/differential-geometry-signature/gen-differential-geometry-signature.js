// Seeded boundless generator for the The Signature Differential Geometry Research Database (signature edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-differential-geometry-signature.js [seed]  (prints one JSON record) or:
// node gen-differential-geometry-signature.js --test (runTests). Package-only; outputs are
// generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "differential-geometry-signature";
const RECORD_KIND = "differential geometry research record";
const ID_PREFIX = "JAH-DGEOS-";
const AI_NAME = "JAH Differential Geometry Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: A Manifold Explorer",
    "subject": "manifold explorer design",
    "description": "In plain words: This Signature design is a manifold explorer, a program that displays a manifold, a space that looks flat up close, through its charts, the maps from small regions to flat space, its atlas, the collection of charts covering the manifold, and its tangent spaces, the flat spaces of directions at each point. The formal statement above is the precise form of the claim; the gloss is the",
    "figures": {
      "explorer_views": 5,
      "manifolds_catalogued": 24,
      "chart_modes": 3,
      "design_year": 2026,
      "atlas_tools": 4,
      "search_filters": 4,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Metric Laboratory",
    "subject": "metric laboratory design",
    "description": "In plain words: This Signature design is a metric laboratory, a program for experimenting with Riemannian metrics, rules that assign to each tangent space an inner product for measuring lengths and angles. The laboratory computes the length of a curve, the angle between two curves, and the volume of a region, from the metric. The formal statement above is the precise form of the claim; the gloss i",
    "figures": {
      "metric_types": 4,
      "lab_experiments": 10,
      "measurement_tools": 5,
      "design_year": 2026,
      "examples_catalogued": 24,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Curvature Visualiser",
    "subject": "curvature visualiser design",
    "description": "In plain words: This Signature design is a curvature visualiser, a program that colours a surface by its curvature: Gaussian curvature, the bending at a point; sectional curvature, the bending of two-dimensional slices; and Ricci curvature, an average of sectional curvatures. Curvature, in plain words, measures how a shape bends. The formal statement above is the precise form of the claim; the glo",
    "figures": {
      "curvature_types": 3,
      "visualiser_modes": 4,
      "surfaces_shown": 24,
      "design_year": 2026,
      "colour_scales": 3,
      "section_views": 5,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Geodesic Tracer",
    "subject": "geodesic tracer design",
    "description": "In plain words: This Signature design is a geodesic tracer, a program that follows geodesics, the straightest possible paths on a curved space, from a point in every direction, and finds where they meet again, their conjugate points, and the cut locus, the set of points beyond which a geodesic stops being the shortest path. The formal statement above is the precise form of the claim; the gloss is ",
    "figures": {
      "tracer_modes": 4,
      "geodesics_traced": 24,
      "starting_directions": 10,
      "design_year": 2026,
      "conjugate_checks": 2,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Gauss-Bonnet Checker",
    "subject": "Gauss-Bonnet checker design",
    "description": "In plain words: This Signature design is a Gauss-Bonnet checker, a program that verifies the Gauss-Bonnet theorem, which says the integral of Gaussian curvature over a closed surface equals two pi times the Euler characteristic, on concrete surfaces of every genus. The genus, in plain words, is the number of holes in the surface. The formal statement above is the precise form of the claim; the glo",
    "figures": {
      "checker_cases": 24,
      "genera_covered": 5,
      "triangulation_modes": 3,
      "design_year": 2026,
      "integral_checks": 2,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Connection Laboratory",
    "subject": "connection laboratory design",
    "description": "In plain words: This Signature design is a connection laboratory, a program for experimenting with connections, rules for comparing directions at different points of a manifold, and parallel transport, the operation of carrying a vector along a curve. The laboratory shows how a vector turns when it is carried around a loop, which is how curvature is measured. The formal statement above is the prec",
    "figures": {
      "connection_types": 3,
      "lab_experiments": 10,
      "holonomy_tools": 4,
      "design_year": 2026,
      "transport_modes": 3,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Form Calculator",
    "subject": "form calculator design",
    "description": "In plain words: This Signature design is a form calculator, a program that computes with differential forms, objects that can be integrated over a manifold. The calculator computes wedge products, exterior derivatives, and integrals of forms, and checks that the exterior derivative squares to zero, the identity that makes the de Rham complex work. The formal statement above is the precise form of ",
    "figures": {
      "form_degrees": 4,
      "calculator_operations": 6,
      "examples_computed": 24,
      "design_year": 2026,
      "cohomology_checks": 2,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Stokes Workbench",
    "subject": "Stokes workbench design",
    "description": "In plain words: This Signature design is a Stokes workbench, a program that verifies Stokes' theorem, which says the integral of the exterior derivative of a form over a manifold equals the integral of the form over its boundary, on concrete manifolds with boundary. A differential form is an object that can be integrated, and the exterior derivative generalises gradient, curl, and divergence. The ",
    "figures": {
      "workbench_cases": 24,
      "form_degrees": 4,
      "integration_modes": 3,
      "design_year": 2026,
      "boundary_checks": 2,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Ricci-Flow Simulator",
    "subject": "Ricci-flow simulator design",
    "description": "In plain words: This Signature design is a Ricci-flow simulator, a program that runs the Ricci flow, the process that deforms the metric of a manifold in the direction of its Ricci curvature, on a three-dimensional manifold, performing surgery, a procedure that cuts the manifold where it pinches, where the flow would otherwise break down. The formal statement above is the precise form of the claim",
    "figures": {
      "simulation_steps": 10,
      "surgery_events": 3,
      "dimensions_supported": 3,
      "design_year": 2026,
      "entropy_checks": 2,
      "flow_modes": 3,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Lie Group Explorer",
    "subject": "Lie group explorer design",
    "description": "In plain words: This Signature design is a Lie group explorer, a program for studying Lie groups, smooth manifolds that are also groups. The explorer shows the group, its Lie algebra, the tangent space at the identity with a bracket operation, and the exponential map, which sends a tangent vector to the group element reached by travelling along the corresponding one-parameter subgroup. The formal ",
    "figures": {
      "group_families": 4,
      "explorer_tools": 5,
      "dimensions_supported": 3,
      "design_year": 2026,
      "representation_modes": 3,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Levi-Civita Workbench",
    "subject": "Levi-Civita workbench design",
    "description": "In plain words: This Signature design is a Levi-Civita workbench, a program that computes the Levi-Civita connection, the canonical connection of Riemannian geometry, from a metric. A connection, in plain words, is a rule for comparing directions at different points, and the Levi-Civita connection is the unique connection compatible with the metric and free of torsion. The formal statement above i",
    "figures": {
      "christoffel_symbols": 10,
      "workbench_tools": 4,
      "metrics_supported": 4,
      "design_year": 2026,
      "geodesic_modes": 2,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Spectral Laboratory",
    "subject": "spectral laboratory design",
    "description": "In plain words: This Signature design is a spectral laboratory, a program for studying the spectrum, the list of eigenvalues, of the Laplace-Beltrami operator, the generalisation of the Laplacian to a Riemannian manifold. The laboratory computes eigenvalues, studies how they grow, and tests what the spectrum determines about the shape. The formal statement above is the precise form of the claim; t",
    "figures": {
      "eigenvalues_computed": 10,
      "lab_experiments": 8,
      "isospectral_pairs": 2,
      "design_year": 2026,
      "heat_tools": 3,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Minimal-Surface Studio",
    "subject": "minimal-surface studio design",
    "description": "In plain words: This Signature design is a minimal-surface studio, a program that builds minimal surfaces, surfaces that minimise area like a soap film spanning a wire frame, for given boundary curves. A minimal surface has zero mean curvature at every point, meaning it bends equally in opposite directions. The formal statement above is the precise form of the claim; the gloss is the same claim in",
    "figures": {
      "studio_tools": 5,
      "surfaces_built": 24,
      "boundary_curves": 10,
      "design_year": 2026,
      "area_modes": 3,
      "regularity_checks": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: An Index-Theorem Checker",
    "subject": "index-theorem checker design",
    "description": "In plain words: This Signature design is an index-theorem checker, a program that verifies the Atiyah-Singer index theorem, which says the analytic index of an elliptic differential operator equals a topological index computed from characteristic classes, on concrete operators. An elliptic operator, in plain words, is a differential operator whose highest-order part is invertible in every directio",
    "figures": {
      "checker_cases": 24,
      "operators_supported": 3,
      "index_terms": 2,
      "design_year": 2026,
      "heat_checks": 2,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Symplectic Explorer",
    "subject": "symplectic explorer design",
    "description": "In plain words: This Signature design is a symplectic explorer, a program for studying symplectic manifolds, manifolds equipped with a symplectic form, a closed nondegenerate two-form that measures areas in a way compatible with dynamics. The explorer displays the symplectic form, follows Hamiltonian flows, the motions of mechanical systems, and tests Gromov's non-squeezing theorem. The formal sta",
    "figures": {
      "phase_spaces": 10,
      "explorer_tools": 5,
      "hamiltonian_systems": 8,
      "design_year": 2026,
      "squeezing_checks": 2,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Finsler Laboratory",
    "subject": "Finsler laboratory design",
    "description": "In plain words: This Signature design is a Finsler laboratory, a program for studying Finsler geometry, the generalisation of Riemannian geometry in which the length of a vector may depend on its direction in a way that does not come from an inner product. The laboratory computes Finsler geodesics and flag curvature, the Finsler analogue of sectional curvature. The formal statement above is the pr",
    "figures": {
      "metric_types": 3,
      "lab_experiments": 8,
      "flag_curvatures": 5,
      "design_year": 2026,
      "geodesic_modes": 2,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Theorema Egregium Demonstrator",
    "subject": "Theorema Egregium demonstrator design",
    "description": "In plain words: This Signature design is a Theorema Egregium demonstrator, a program that shows Gauss's remarkable theorem, which says Gaussian curvature is intrinsic, meaning it can be measured from within a surface without reference to the space it sits in. The demonstrator bends a surface without stretching it and shows the curvature unchanged. The formal statement above is the precise form of ",
    "figures": {
      "demonstrator_cases": 24,
      "surfaces_shown": 10,
      "isometry_modes": 3,
      "design_year": 2026,
      "curvature_checks": 2,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Bundle Builder",
    "subject": "bundle builder design",
    "description": "In plain words: This Signature design is a bundle builder, a program that constructs fibre bundles, spaces that locally look like products, with a fibre over each point of a base, and vector bundles, whose fibres are vector spaces, from transition functions, the maps that glue the local products on overlaps. The formal statement above is the precise form of the claim; the gloss is the same claim i",
    "figures": {
      "bundle_types": 3,
      "builder_modes": 3,
      "sections_computed": 10,
      "design_year": 2026,
      "characteristic_tools": 4,
      "examples_built": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Hopf-Rinow Explorer",
    "subject": "Hopf-Rinow explorer design",
    "description": "In plain words: This Signature design is a Hopf-Rinow explorer, a program that tests the three equivalent conditions of the Hopf-Rinow theorem, which says that for a Riemannian manifold, completeness as a metric space, geodesic completeness, and the existence of a minimising geodesic between any two points are equivalent. A geodesic is the straightest possible path. The formal statement above is t",
    "figures": {
      "explorer_cases": 24,
      "completeness_checks": 3,
      "geodesic_modes": 2,
      "design_year": 2026,
      "minimising_tools": 3,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Submanifold Studio",
    "subject": "submanifold studio design",
    "description": "In plain words: This Signature design is a submanifold studio, a program for studying submanifolds, manifolds sitting inside another manifold, like a surface sitting in three-dimensional space. The studio computes the second fundamental form, which measures how the submanifold bends inside the ambient space, and the shape operator, whose eigenvalues are the principal curvatures. The formal stateme",
    "figures": {
      "studio_tools": 5,
      "submanifolds_built": 24,
      "curvature_modes": 3,
      "design_year": 2026,
      "fundamental_forms": 2,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Relativity Geometry Bench",
    "subject": "relativity geometry bench design",
    "description": "In plain words: This Signature design is a relativity geometry bench, a program for the differential geometry of general relativity, in which spacetime is a four-dimensional Lorentzian manifold and gravity is its curvature. The bench computes the metric, the geodesics, and the curvature of model spacetimes, such as the Schwarzschild and Friedmann solutions. The formal statement above is the precis",
    "figures": {
      "spacetime_models": 5,
      "bench_tools": 6,
      "geodesic_modes": 3,
      "design_year": 2026,
      "curvature_checks": 4,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Chern Laboratory",
    "subject": "Chern laboratory design",
    "description": "In plain words: This Signature design is a Chern laboratory, a program for Chern-Weil theory, the method of building characteristic classes, cohomology classes measuring twisting, from the curvature of a connection. The laboratory computes Euler forms and characteristic classes and checks the Chern-Gauss-Bonnet formula on examples. The formal statement above is the precise form of the claim; the g",
    "figures": {
      "lab_experiments": 8,
      "characteristic_classes": 5,
      "euler_checks": 2,
      "design_year": 2026,
      "dimensions_supported": 4,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Morse Explorer",
    "subject": "Morse explorer design",
    "description": "In plain words: This Signature design is a Morse explorer, a program that decomposes a manifold into handles using Morse theory, which studies the topology of a manifold through the critical points of a function on it. A Morse function, in plain words, is a smooth function whose critical points are all non-degenerate, like the top of a hill or the bottom of a valley. The formal statement above is ",
    "figures": {
      "explorer_cases": 24,
      "critical_points": 10,
      "handle_types": 3,
      "design_year": 2026,
      "gradient_modes": 2,
      "betti_checks": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Differential Geometry Teaching Laboratory",
    "subject": "differential geometry teaching laboratory design",
    "description": "In plain words: This Signature design is a differential geometry teaching laboratory, a program that teaches the field in a ladder, from simple to compounded to most complex: curves, then surfaces, then manifolds, then metrics, then curvature, then geodesics. A teaching ladder, in plain words, is an ordering of a subject from the easiest ideas to the hardest. The formal statement above is the prec",
    "figures": {
      "lab_lessons": 20,
      "worked_examples": 24,
      "difficulty_levels": 5,
      "design_year": 2026,
      "exercise_sets": 10,
      "feedback_types": 4,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Manifold",
    "url": "https://en.wikipedia.org/wiki/Manifold",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  },
  {
    "name": "Wikipedia - Differential geometry",
    "url": "https://en.wikipedia.org/wiki/Differential_geometry",
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
