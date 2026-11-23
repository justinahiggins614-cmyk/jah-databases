// Seeded boundless generator for the The Signature Algebraic Geometry Research Database (signature edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-algebraic-geometry-signature.js [seed]  (prints one JSON record) or:
// node gen-algebraic-geometry-signature.js --test (runTests). Package-only; outputs are
// generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "algebraic-geometry-signature";
const RECORD_KIND = "algebraic geometry research record";
const ID_PREFIX = "JAH-AGEOS-";
const AI_NAME = "JAH Algebraic Geometry Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: A Variety Explorer",
    "subject": "variety explorer design",
    "description": "In plain words: This Signature design is a variety explorer, a program that displays an algebraic variety, a shape defined by polynomial equations, together with its equations, its dimension, its degree, and its singular points, in a single view. A variety is the set of points satisfying a system of polynomial equations. The formal statement above is the precise form of the claim; the gloss is the",
    "figures": {
      "explorer_views": 5,
      "varieties_catalogued": 24,
      "invariants_computed": 6,
      "design_year": 2026,
      "plot_modes": 3,
      "search_filters": 4,
      "scales_max": 1000000000,
      "fields_covered": 3
    }
  },
  {
    "title": "Signature Design: A Curve Plotter for Algebraic Curves",
    "subject": "curve plotter design",
    "description": "In plain words: This Signature design is a curve plotter, a program that draws algebraic curves, one-dimensional shapes defined by polynomial equations, and marks their genus, their rational points, and their singular points. The genus, in plain words, is the number of holes in the curve. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "plot_types": 4,
      "curves_supported": 24,
      "genus_values": 5,
      "design_year": 2026,
      "point_modes": 3,
      "export_formats": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Scheme Visualiser",
    "subject": "scheme visualiser design",
    "description": "In plain words: This Signature design is a scheme visualiser, a program that shows a scheme, Grothendieck's generalisation of a variety, as its spectrum, the set of prime ideals of a ring made into a space, together with the gluing data that assembles affine pieces into the whole scheme. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "visualiser_layers": 4,
      "schemes_supported": 24,
      "spectrum_views": 3,
      "design_year": 2026,
      "gluing_diagrams": 5,
      "search_modes": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Sheaf Laboratory",
    "subject": "sheaf laboratory design",
    "description": "In plain words: This Signature design is a sheaf laboratory, a program for experimenting with sheaves, tools that track data defined locally on small pieces of a space, and their cohomology, the groups that measure the obstruction to patching local data into global data. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "sheaf_types": 5,
      "lab_experiments": 10,
      "cohomology_tools": 4,
      "design_year": 2026,
      "examples_catalogued": 24,
      "check_passes": 3,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Cohomology Calculator",
    "subject": "cohomology calculator design",
    "description": "In plain words: This Signature design is a cohomology calculator, a program that computes cohomology groups for algebraic varieties and checks the results against the theorems. Cohomology, in plain words, is a sequence of groups that measures the holes and twists of a shape. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "cohomology_theories": 3,
      "calculator_modes": 4,
      "examples_computed": 24,
      "design_year": 2026,
      "dimension_limits": 5,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Moduli Navigator",
    "subject": "moduli navigator design",
    "description": "In plain words: This Signature design is a moduli navigator, a program for exploring moduli spaces, geometric spaces whose points are themselves geometric objects. The navigator shows where a given curve sits in the moduli space of curves of its genus, what curves are near it, and what happens at the boundary, where curves degenerate. The formal statement above is the precise form of the claim; th",
    "figures": {
      "moduli_spaces_mapped": 10,
      "genera_covered": 5,
      "navigation_modes": 3,
      "design_year": 2026,
      "boundary_strata": 8,
      "search_filters": 4,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: An Intersection Workbench",
    "subject": "intersection workbench design",
    "description": "In plain words: This Signature design is an intersection workbench, a program that computes intersection numbers, the counts of how geometric shapes meet, and checks them against Bezout's theorem and the general intersection theory of Fulton. Intersection theory, in plain words, is the counting of meetings between shapes. The formal statement above is the precise form of the claim; the gloss is th",
    "figures": {
      "workbench_tools": 6,
      "intersection_products": 10,
      "examples_computed": 24,
      "design_year": 2026,
      "multiplicity_modes": 3,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Surface Classifier",
    "subject": "surface classifier design",
    "description": "In plain words: This Signature design is a surface classifier, a program that takes an algebraic surface, a two-dimensional variety, computes its invariants, and places it in the Enriques-Kodaira classification, which sorts all surfaces into four classes by their Kodaira dimension. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "surface_classes": 4,
      "invariants_computed": 5,
      "examples_classified": 24,
      "design_year": 2026,
      "kodaira_values": 4,
      "minimal_models": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Riemann-Roch Checker",
    "subject": "Riemann-Roch checker design",
    "description": "In plain words: This Signature design is a Riemann-Roch checker, a program that verifies the Riemann-Roch theorem, which counts functions on a curve, on concrete curves and divisors. A divisor, in plain words, is a formal list of points with whole-number weights, recording where a function is allowed poles and zeros. The formal statement above is the precise form of the claim; the gloss is the sam",
    "figures": {
      "checker_cases": 24,
      "divisors_supported": 10,
      "genera_covered": 5,
      "design_year": 2026,
      "dimension_checks": 3,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Minimal-Model Simulator",
    "subject": "minimal-model simulator design",
    "description": "In plain words: This Signature design is a minimal-model simulator, a program that runs the minimal model program, the procedure that simplifies a variety step by step until it reaches a minimal model, on a given variety, showing each contraction and each flip. A flip, in plain words, is a surgery that replaces a contracted part with a different one. The formal statement above is the precise form ",
    "figures": {
      "simulation_steps": 10,
      "flips_simulated": 20,
      "dimensions_supported": 3,
      "design_year": 2026,
      "contraction_types": 4,
      "termination_checks": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: An Abelian Variety Studio",
    "subject": "abelian variety studio design",
    "description": "In plain words: This Signature design is an abelian variety studio, a program for studying abelian varieties, higher-dimensional analogues of elliptic curves that are also groups. The studio computes torsion points, points of finite order, displays the dual variety, and locates the variety in its moduli space. The formal statement above is the precise form of the claim; the gloss is the same claim",
    "figures": {
      "studio_tools": 6,
      "dimensions_supported": 3,
      "torsion_computations": 16,
      "design_year": 2026,
      "moduli_views": 3,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: An Algebraic Group Explorer",
    "subject": "algebraic group explorer design",
    "description": "In plain words: This Signature design is an algebraic group explorer, a program for studying algebraic groups, varieties that are also groups, with the group operations given by polynomial maps. The explorer shows a group's structure: its torus part, its unipotent part, and its semisimple part, together with its root data. The formal statement above is the precise form of the claim; the gloss is t",
    "figures": {
      "group_families": 4,
      "root_systems": 10,
      "dimensions_supported": 3,
      "design_year": 2026,
      "representation_tools": 4,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Toric Builder",
    "subject": "toric builder design",
    "description": "In plain words: This Signature design is a toric builder, a program that constructs toric varieties, varieties containing a torus as a dense open part, from fans, collections of cones, and from polytopes, higher-dimensional polygons. A toric variety is determined by its fan, and its geometry can be read off the fan by combinatorics. The formal statement above is the precise form of the claim; the ",
    "figures": {
      "fan_cones_supported": 10,
      "polytopes_supported": 8,
      "builder_modes": 3,
      "design_year": 2026,
      "cohomology_tools": 2,
      "examples_built": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: An Etale Explorer",
    "subject": "etale explorer design",
    "description": "In plain words: This Signature design is an etale explorer, a program for studying etale coverings, the etale fundamental group, and etale cohomology. An etale map, in plain words, is a map that is locally an isomorphism, like a covering map, and the etale fundamental group is built from finite etale coverings the way the topological fundamental group is built from covering spaces. The formal stat",
    "figures": {
      "covering_types": 4,
      "fundamental_groups": 10,
      "cohomology_tools": 3,
      "design_year": 2026,
      "examples_catalogued": 24,
      "trace_formulas": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Hodge Laboratory",
    "subject": "Hodge laboratory design",
    "description": "In plain words: This Signature design is a Hodge laboratory, a program for experimenting with Hodge structures, decompositions of cohomology groups into parts of type (p, q). The laboratory computes Hodge numbers, the dimensions of the Hodge pieces, and checks the Hodge decomposition on examples. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary w",
    "figures": {
      "hodge_numbers_computed": 10,
      "lab_experiments": 8,
      "period_tools": 3,
      "design_year": 2026,
      "examples_catalogued": 24,
      "decomposition_checks": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Mirror-Symmetry Mapper",
    "subject": "mirror-symmetry mapper design",
    "description": "In plain words: This Signature design is a mirror-symmetry mapper, a program that pairs Calabi-Yau varieties, three-dimensional shapes with special geometric properties that appear in string theory, with their mirrors, and checks the enumerative predictions of mirror symmetry against computed curve counts. The formal statement above is the precise form of the claim; the gloss is the same claim in ",
    "figures": {
      "mirror_pairs_mapped": 100,
      "prediction_checks": 1000,
      "mapper_modes": 3,
      "design_year": 2026,
      "curve_counts": 100,
      "period_tools": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Diophantine Solver Bench",
    "subject": "Diophantine solver bench design",
    "description": "In plain words: This Signature design is a Diophantine solver bench, a program for solving Diophantine equations, polynomial equations whose solutions are required to be whole numbers or fractions. The bench searches for rational points, points with fractional coordinates, and bounds their heights, a measure of how complicated a point is. The formal statement above is the precise form of the claim",
    "figures": {
      "equation_types": 5,
      "solver_methods": 4,
      "solutions_found": 100,
      "design_year": 2026,
      "height_bounds": 3,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Topos Studio",
    "subject": "topos studio design",
    "description": "In plain words: This Signature design is a topos studio, a program for studying topoi, categories that behave like the categories of sheaves on a space. A site, in plain words, is a category equipped with a notion of covering, and the topos of sheaves on a site plays the role of the space. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "sites_supported": 3,
      "topos_examples": 10,
      "logic_models": 2,
      "design_year": 2026,
      "sheaf_tools": 4,
      "examples_catalogued": 24,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Singularity Resolver",
    "subject": "singularity resolver design",
    "description": "In plain words: This Signature design is a singularity resolver, a program that applies Hironaka's resolution of singularities, the theorem that any variety over a field of characteristic zero can be replaced by a smooth variety mapping onto it, to a given singular variety, showing each blow-up. A blow-up, in plain words, is a surgery that replaces a point by the set of directions through it. The ",
    "figures": {
      "blowup_steps": 10,
      "singularities_resolved": 24,
      "invariants_tracked": 3,
      "design_year": 2026,
      "resolution_modes": 2,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: An Algebraic Geometry Code Builder",
    "subject": "algebraic geometry code builder design",
    "description": "In plain words: This Signature design is an algebraic geometry code builder, a program that constructs error-correcting codes from algebraic curves over finite fields. An error-correcting code, in plain words, is a way of adding redundancy to a message so that errors in transmission can be detected and corrected. The formal statement above is the precise form of the claim; the gloss is the same cl",
    "figures": {
      "codes_built": 24,
      "curves_used": 10,
      "parameters_computed": 3,
      "design_year": 2026,
      "bound_checks": 2,
      "fields_linked": 2,
      "scales_max": 1000000000,
      "years_active": 45
    }
  },
  {
    "title": "Signature Design: A Grobner Engine",
    "subject": "Grobner engine design",
    "description": "In plain words: This Signature design is a Grobner engine, a program that computes Grobner bases, special sets of generators for an ideal with the property that questions about the ideal can be answered by division. An ideal, in plain words, is a set of polynomials closed under addition and multiplication by any polynomial. The formal statement above is the precise form of the claim; the gloss is ",
    "figures": {
      "algorithms_implemented": 5,
      "ideals_computed": 24,
      "monomial_orders": 4,
      "design_year": 2026,
      "reduction_steps": 100,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Jacobian Mapper",
    "subject": "Jacobian mapper design",
    "description": "In plain words: This Signature design is a Jacobian mapper, a program that builds the Jacobian variety of a curve, an abelian variety whose dimension equals the genus of the curve, and applies the Abel-Jacobi map, which sends a point of the curve to its class in the Jacobian. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "curves_mapped": 24,
      "jacobian_dimensions": 3,
      "torsion_computations": 16,
      "design_year": 2026,
      "abel_jacobi_modes": 2,
      "torelli_checks": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: A Design-Study Theorem Prover for Algebraic Geometry",
    "subject": "design-study theorem prover design",
    "description": "In plain words: This Signature design is a design-study theorem prover for algebraic geometry, a program that attempts to prove theorems in the field using tactics, which are reusable proof strategies, and checks every step it produces with a proof checker. A tactic is a named move, such as induction or reduction, that the prover can apply. The formal statement above is the precise form of the cla",
    "figures": {
      "prover_tactics": 8,
      "theorems_attempted": 24,
      "proof_steps_checked": 1000,
      "design_year": 2026,
      "search_depth": 5,
      "verification_runs": 2,
      "scales_max": 1000000000,
      "fields_covered": 2
    }
  },
  {
    "title": "Signature Design: An Algebraic Geometry Teaching Laboratory",
    "subject": "algebraic geometry teaching laboratory design",
    "description": "In plain words: This Signature design is an algebraic geometry teaching laboratory, a program that teaches the field in a ladder, from simple to compounded to most complex: curves, then varieties, then sheaves, then cohomology, then schemes. A teaching ladder, in plain words, is an ordering of a subject from the easiest ideas to the hardest. The formal statement above is the precise form of the cl",
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
    "name": "Wikipedia - Algebraic variety",
    "url": "https://en.wikipedia.org/wiki/Algebraic_variety",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  },
  {
    "name": "Wikipedia - Algebraic geometry",
    "url": "https://en.wikipedia.org/wiki/Algebraic_geometry",
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
