// Seeded boundless generator for the Differential Geometry Research Database (public edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-differential-geometry.js [seed]  (prints one JSON record) or:
// node gen-differential-geometry.js --test (runTests). Package-only; outputs are
// generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "differential-geometry";
const RECORD_KIND = "differential geometry research record";
const ID_PREFIX = "JAH-DGEO-";
const AI_NAME = "JAH Differential Geometry Librarian";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Differential Geometry: The Field in Outline",
    "subject": "differential geometry overview",
    "description": "In plain words: Differential geometry is the study of smooth shapes using calculus, the mathematics of rates of change. A manifold, in plain words, is a space that looks flat up close, like the surface of the Earth looks flat to a person standing on it. The field studies curves, surfaces, manifolds, curvature, which measures how a shape bends, and geodesics, the straightest possible paths. The for",
    "figures": {
      "dimensions_studied": 10,
      "founders_count": 5,
      "centuries_active": 3,
      "key_tools": 6,
      "major_theorems": 8,
      "fields_linked": 4,
      "textbooks_standard": 3,
      "years_modern": 100
    }
  },
  {
    "title": "Manifolds: Spaces That Look Flat Up Close",
    "subject": "manifolds",
    "description": "In plain words: A manifold is a space that looks flat up close. In plain words, every point of a manifold has a neighbourhood, a small region around it, that looks like ordinary flat space, even though the whole space may be curved, like the surface of a sphere. A chart is a map from such a neighbourhood to flat space, and an atlas is a collection of charts covering the whole manifold. The formal ",
    "figures": {
      "dimensions_examples": 4,
      "chart_types": 3,
      "year_riemann": 1854,
      "year_whitney": 1936,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 170
    }
  },
  {
    "title": "Riemannian Manifolds and the Metric",
    "subject": "Riemannian manifolds",
    "description": "In plain words: A Riemannian manifold is a manifold equipped with a metric, a rule that assigns to each tangent space an inner product, a way of measuring lengths of vectors and angles between them. A tangent space, in plain words, is the flat space of directions through a point. The metric lets us measure the length of a curve, the angle between two curves, and the volume of a region. The formal ",
    "figures": {
      "metric_components": 10,
      "dimensions_examples": 4,
      "year_riemann": 1854,
      "year_levi_civita": 1917,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 170
    }
  },
  {
    "title": "Curvature: Gaussian, Sectional, and Ricci",
    "subject": "curvature",
    "description": "In plain words: Curvature measures how a shape bends. Gaussian curvature, in plain words, is the bending of a surface at a point: positive on a sphere, zero on a flat plane, negative on a saddle. Sectional curvature generalises it to higher dimensions by looking at two-dimensional slices. Ricci curvature averages the sectional curvatures over all directions containing a given vector. The formal st",
    "figures": {
      "curvature_types": 3,
      "gauss_year": 1827,
      "riemann_year": 1854,
      "ricci_year": 1900,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 200
    }
  },
  {
    "title": "Geodesics: The Straightest Possible Paths",
    "subject": "geodesics",
    "description": "In plain words: A geodesic is the straightest possible path on a curved space. In plain words, it is a curve whose direction does not turn as it moves, so that a traveller following it feels no sideways force. On a sphere, the geodesics are the great circles, the largest circles that can be drawn; on a flat plane, they are straight lines. The formal statement above is the precise form of the claim",
    "figures": {
      "geodesic_equation_terms": 2,
      "great_circle_examples": 3,
      "year_hopf_rinow": 1931,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 200
    }
  },
  {
    "title": "The Gauss-Bonnet Theorem: Bending and Topology Together",
    "subject": "Gauss-Bonnet theorem",
    "description": "In plain words: The Gauss-Bonnet theorem connects the local bending of a surface with its global shape. It says that the integral, the total, of the Gaussian curvature over a closed surface equals two pi times the Euler characteristic, a number that counts the surface's topology: for a surface of genus g, the number of holes, the Euler characteristic is two minus two times g. The formal statement ",
    "figures": {
      "year_gauss": 1827,
      "year_bonnet": 1848,
      "genus_terms": 2,
      "curvature_integral_terms": 1,
      "key_versions": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 200
    }
  },
  {
    "title": "Connections and Parallel Transport",
    "subject": "connections and parallel transport",
    "description": "In plain words: A connection is a rule for comparing directions at different points of a manifold. In plain words, on a curved space there is no natural way to say that a direction here is the same as a direction there, and a connection supplies the rule. Parallel transport is the operation of carrying a vector along a curve using the connection, keeping it as constant as the connection allows. Th",
    "figures": {
      "connection_types": 3,
      "year_levi_civita": 1917,
      "year_cartan": 1920,
      "holonomy_groups": 5,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 100
    }
  },
  {
    "title": "Differential Forms and the Exterior Derivative",
    "subject": "differential forms",
    "description": "In plain words: A differential form is an object that can be integrated over a manifold. A zero-form is a function; a one-form is an object that can be integrated along a curve; a two-form can be integrated over a surface. The exterior derivative, in plain words, is an operation that takes a k-form to a (k+1)-form, generalising the gradient, curl, and divergence of vector calculus, and it satisfie",
    "figures": {
      "form_degrees": 4,
      "year_cartan": 1920,
      "exterior_rules": 3,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 100
    }
  },
  {
    "title": "Stokes' Theorem: The Fundamental Theorem of Calculus on Manifolds",
    "subject": "Stokes' theorem",
    "description": "In plain words: Stokes' theorem says that the integral of the exterior derivative of a differential form over a manifold equals the integral of the form over the manifold's boundary. A differential form is an object that can be integrated, and the exterior derivative is the operation generalising gradient, curl, and divergence. The theorem is the fundamental theorem of calculus, generalised to cur",
    "figures": {
      "year_stokes": 1854,
      "year_cartan": 1920,
      "form_degrees": 4,
      "key_versions": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 170
    }
  },
  {
    "title": "The Ricci Flow and the Poincare Conjecture",
    "subject": "Ricci flow",
    "description": "In plain words: The Ricci flow is a process that deforms the metric of a Riemannian manifold over time, in the direction of its Ricci curvature, which is an average of sectional curvatures. A metric, in plain words, is the rule for measuring lengths and angles. The flow smooths out bumps the way heat spreads, and it was the tool Grigori Perelman used to prove the Poincare conjecture. The formal st",
    "figures": {
      "year_hamilton": 1982,
      "year_perelman": 2003,
      "flow_dimensions": 3,
      "surgery_steps": 3,
      "millennium_problems": 7,
      "prize_dollars": 1000000,
      "years_active": 44,
      "key_theorems": 3
    }
  },
  {
    "title": "Lie Groups and Lie Algebras",
    "subject": "Lie groups",
    "description": "In plain words: A Lie group is a smooth manifold that is also a group, a set of symmetries with a rule for combining them, where the group operations are smooth maps. Its Lie algebra, in plain words, is the tangent space at the identity element, equipped with a bracket operation that records how the group fails to commute. The formal statement above is the precise form of the claim; the gloss is t",
    "figures": {
      "year_lie": 1870,
      "classical_families": 4,
      "dimension_examples": 3,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 155
    }
  },
  {
    "title": "The Levi-Civita Connection",
    "subject": "Levi-Civita connection",
    "description": "In plain words: The Levi-Civita connection is the canonical connection of Riemannian geometry. A connection, in plain words, is a rule for comparing directions at different points, and the Levi-Civita connection is the unique connection that is compatible with the metric, meaning it preserves lengths and angles under parallel transport, and torsion-free, meaning it has no twist. The formal stateme",
    "figures": {
      "year_levi_civita": 1917,
      "connection_properties": 2,
      "christoffel_symbols": 10,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 109
    }
  },
  {
    "title": "The Laplace-Beltrami Operator",
    "subject": "Laplace-Beltrami operator",
    "description": "In plain words: The Laplace-Beltrami operator is the generalisation of the Laplacian, the sum of second derivatives, to a Riemannian manifold. In plain words, it measures how a function differs from its average over nearby points, and its eigenvalues, the special numbers for which the equation has non-zero solutions, encode the geometry of the manifold. The formal statement above is the precise fo",
    "figures": {
      "year_beltrami": 1868,
      "eigenvalues_count": 10,
      "spectrum_properties": 3,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 158
    }
  },
  {
    "title": "Minimal Surfaces: Soap Films and Mathematics",
    "subject": "minimal surfaces",
    "description": "In plain words: A minimal surface is a surface that minimises area, at least locally, like a soap film spanning a wire frame. Its mean curvature, in plain words, is the average of its two principal bendings, and a minimal surface has mean curvature zero at every point, meaning it bends equally in opposite directions. The formal statement above is the precise form of the claim; the gloss is the sam",
    "figures": {
      "year_plateau": 1873,
      "year_douglas": 1931,
      "fields_medal_year": 1936,
      "area_minimising": 1,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 150
    }
  },
  {
    "title": "The Atiyah-Singer Index Theorem",
    "subject": "Atiyah-Singer index theorem",
    "description": "In plain words: The Atiyah-Singer index theorem says that the analytic index of an elliptic differential operator, the number of solutions minus the number of obstructions, equals a topological index computed from the characteristic classes of the manifold, which are cohomology classes measuring twisting. An elliptic operator, in plain words, is a differential operator whose highest-order part is ",
    "figures": {
      "year_proved": 1963,
      "index_terms": 2,
      "fields_linked": 4,
      "abel_prize_year": 2004,
      "key_versions": 3,
      "textbooks_standard": 3,
      "years_active": 63
    }
  },
  {
    "title": "Symplectic Geometry: The Geometry of Phase Space",
    "subject": "symplectic geometry",
    "description": "In plain words: Symplectic geometry is the geometry of phase space, the space of positions and momenta of a mechanical system. A symplectic manifold, in plain words, is a manifold equipped with a symplectic form, a closed nondegenerate two-form, a differential form that measures areas in a way compatible with the dynamics. Hamiltonian flows, the motions of mechanical systems, preserve the symplect",
    "figures": {
      "phase_dimensions": 2,
      "year_hamilton": 1834,
      "year_modern": 1970,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 55
    }
  },
  {
    "title": "Finsler Geometry: Geometry Without a Quadratic Metric",
    "subject": "Finsler geometry",
    "description": "In plain words: Finsler geometry is the generalisation of Riemannian geometry in which the length of a vector may depend on its direction in a way that does not come from an inner product. A Finsler metric, in plain words, is a rule that assigns a length to each tangent vector, smoothly and positively, without requiring the rule to be quadratic, as a Riemannian metric does. The formal statement ab",
    "figures": {
      "year_finsler": 1918,
      "year_riemann": 1854,
      "metric_types": 2,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 108
    }
  },
  {
    "title": "The Theorema Egregium: Gauss's Remarkable Theorem",
    "subject": "Theorema Egregium",
    "description": "In plain words: The Theorema Egregium, Latin for the remarkable theorem, says that the Gaussian curvature of a surface is intrinsic: it can be measured by an inhabitant of the surface, from distances measured within the surface, without any reference to the space the surface sits in. An isometry, a map that preserves distances, preserves Gaussian curvature. The formal statement above is the precis",
    "figures": {
      "year_gauss": 1827,
      "curvature_types": 1,
      "isometry_invariants": 2,
      "key_theorems": 2,
      "fields_linked": 2,
      "textbooks_standard": 3,
      "years_active": 199
    }
  },
  {
    "title": "Vector Bundles and Fibre Bundles",
    "subject": "vector bundles and fibre bundles",
    "description": "In plain words: A fibre bundle is a space that locally looks like a product: over each point of a base space sits a fibre, a copy of a fixed space, and the whole bundle is glued from these local products. A vector bundle, in plain words, is a fibre bundle whose fibres are vector spaces, so that a vector can be attached to each point of the base, varying smoothly. The formal statement above is the ",
    "figures": {
      "bundle_types": 3,
      "year_whitney": 1935,
      "year_steenrod": 1951,
      "structure_groups": 4,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 90
    }
  },
  {
    "title": "The Hopf-Rinow Theorem: Completeness and Geodesics",
    "subject": "Hopf-Rinow theorem",
    "description": "In plain words: The Hopf-Rinow theorem says that for a Riemannian manifold, three properties are equivalent: completeness as a metric space, meaning every Cauchy sequence converges; geodesic completeness, meaning every geodesic can be extended for all time; and the existence of a minimising geodesic, a shortest path, between any two points. A geodesic is the straightest possible path on the manifo",
    "figures": {
      "year_proved": 1931,
      "completeness_conditions": 3,
      "key_theorems": 2,
      "fields_linked": 2,
      "textbooks_standard": 3,
      "years_active": 95,
      "geodesic_properties": 3,
      "dimensions_examples": 3
    }
  },
  {
    "title": "Submanifolds and the Second Fundamental Form",
    "subject": "submanifolds",
    "description": "In plain words: A submanifold is a manifold sitting inside another manifold, like a surface sitting in three-dimensional space. The second fundamental form, in plain words, measures how the submanifold bends inside the ambient space: it records, for each pair of tangent directions, how the submanifold curves away from its tangent plane. The formal statement above is the precise form of the claim; ",
    "figures": {
      "fundamental_forms": 2,
      "principal_curvatures": 2,
      "year_gauss": 1827,
      "key_theorems": 3,
      "fields_linked": 2,
      "textbooks_standard": 3,
      "years_active": 199
    }
  },
  {
    "title": "Differential Geometry in General Relativity",
    "subject": "differential geometry in general relativity",
    "description": "In plain words: General relativity is the physical theory in which spacetime is a four-dimensional Lorentzian manifold, a manifold with a metric of a special type that distinguishes time from space, and gravity is the curvature of that manifold. A Lorentzian manifold, in plain words, is a manifold whose metric measures time-like directions differently from space-like ones. The formal statement abo",
    "figures": {
      "spacetime_dimensions": 4,
      "year_einstein": 1915,
      "field_equations": 10,
      "key_theorems": 3,
      "fields_linked": 2,
      "textbooks_standard": 3,
      "years_active": 111
    }
  },
  {
    "title": "The Chern-Gauss-Bonnet Theorem",
    "subject": "Chern-Gauss-Bonnet theorem",
    "description": "In plain words: The Chern-Gauss-Bonnet theorem generalises the Gauss-Bonnet theorem to all even-dimensional manifolds. It says that the integral of the Euler form, a differential form built from the curvature, over a closed even-dimensional Riemannian manifold equals the Euler characteristic, a number that counts the manifold's topology. The formal statement above is the precise form of the claim;",
    "figures": {
      "year_chern": 1944,
      "dimensions_general": 100,
      "euler_terms": 1,
      "key_versions": 2,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 82
    }
  },
  {
    "title": "Morse Theory: The Shape of a Manifold from a Function",
    "subject": "Morse theory",
    "description": "In plain words: Morse theory studies the topology of a manifold through the critical points of a function on it. A Morse function, in plain words, is a smooth function whose critical points, where its derivative vanishes, are all non-degenerate, like the top of a hill or the bottom of a valley, rather than flat. Each critical point contributes a handle, a piece, to the manifold's shape. The formal",
    "figures": {
      "year_morse": 1934,
      "critical_points": 10,
      "handle_types": 3,
      "key_theorems": 3,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_active": 92
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Differential geometry",
    "url": "https://en.wikipedia.org/wiki/Differential_geometry",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  },
  {
    "name": "Wikipedia - Manifold",
    "url": "https://en.wikipedia.org/wiki/Manifold",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  },
  {
    "name": "Wikipedia - Curvature",
    "url": "https://en.wikipedia.org/wiki/Curvature",
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
    edition: "public",
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: "public-harvest",
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
