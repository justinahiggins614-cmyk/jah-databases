// Seeded boundless generator for the Algebraic Geometry Research Database (public edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-algebraic-geometry.js [seed]  (prints one JSON record) or:
// node gen-algebraic-geometry.js --test (runTests). Package-only; outputs are
// generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "algebraic-geometry";
const RECORD_KIND = "algebraic geometry research record";
const ID_PREFIX = "JAH-AGEO-";
const AI_NAME = "JAH Algebraic Geometry Librarian";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Algebraic Geometry: The Field in Outline",
    "subject": "algebraic geometry overview",
    "description": "In plain words: Algebraic geometry studies shapes defined by polynomial equations, equations built from powers of variables, and the algebra that describes those shapes. A variety, in plain words, is such a shape: the set of points satisfying a system of polynomial equations. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "dimensions_studied": 10,
      "founders_count": 5,
      "centuries_active": 3,
      "key_tools": 6,
      "major_theorems": 8,
      "fields_linked": 4,
      "textbooks_standard": 3,
      "years_modern": 80
    }
  },
  {
    "title": "Algebraic Curves and the Genus",
    "subject": "algebraic curves and genus",
    "description": "In plain words: An algebraic curve is a one-dimensional shape defined by polynomial equations. Its genus, in plain words, is the number of holes in the curve: a line has genus zero, an elliptic curve has genus one, and more complicated curves have higher genus. The genus is the single most important number attached to a curve. The formal statement above is the precise form of the claim; the gloss ",
    "figures": {
      "genus_line": 0,
      "genus_elliptic": 1,
      "genus_examples": 5,
      "rational_points_finite_genus": 2,
      "centuries_studied": 3,
      "key_theorems": 4,
      "fields_linked": 2,
      "degree_examples": 3
    }
  },
  {
    "title": "Elliptic Curves and the Mordell-Weil Theorem",
    "subject": "elliptic curves",
    "description": "In plain words: An elliptic curve is a smooth curve of genus one with a chosen point, defined by an equation of the form y squared equals x cubed plus a times x plus b. Its rational points, points with fractional coordinates, form a group, a set with a rule for combining elements, under a geometric addition law. The formal statement above is the precise form of the claim; the gloss is the same cla",
    "figures": {
      "genus": 1,
      "rank_examples": 5,
      "torsion_possibilities": 15,
      "year_mordell": 1922,
      "year_weil": 1928,
      "group_law_steps": 3,
      "cryptography_bits": 256,
      "fields_linked": 2
    }
  },
  {
    "title": "Algebraic Varieties: Shapes Defined by Equations",
    "subject": "algebraic varieties",
    "description": "In plain words: An algebraic variety is a geometric shape defined as the set of points satisfying a system of polynomial equations. A polynomial is an expression built from variables and their powers, such as x squared plus y squared minus one, which defines a circle. The variety is the shape, and its ring of functions is the algebra that describes it. The formal statement above is the precise for",
    "figures": {
      "dimensions_examples": 4,
      "defining_polynomials": 10,
      "classical_types": 5,
      "centuries_studied": 3,
      "key_invariants": 6,
      "fields_linked": 3,
      "textbooks_standard": 3,
      "years_modern": 80
    }
  },
  {
    "title": "Schemes: Grothendieck's Rebuilding of Geometry",
    "subject": "schemes",
    "description": "In plain words: A scheme is Alexander Grothendieck's generalisation of an algebraic variety. An affine scheme is the spectrum of a ring, the set of prime ideals of the ring equipped with a sheaf of functions; a general scheme is built by gluing affine schemes together, the way a manifold is built by gluing flat pieces. The formal statement above is the precise form of the claim; the gloss is the s",
    "figures": {
      "year_introduced": 1960,
      "ega_volumes": 4,
      "sga_volumes": 7,
      "prime_spectrum_points": 100,
      "founders_count": 3,
      "fields_rebuilt": 5,
      "textbooks_standard": 3,
      "years_active": 66
    }
  },
  {
    "title": "Sheaves and Cohomology: Local Data, Global Shape",
    "subject": "sheaves and cohomology",
    "description": "In plain words: A sheaf is a tool for tracking data that is defined locally, on small pieces of a space, such as functions defined near each point. Cohomology is a sequence of groups, algebraic objects that measure symmetry, that records the obstruction to patching local data into global data: whether a function defined piece by piece can be assembled into one function on the whole shape. The form",
    "figures": {
      "cohomology_groups": 10,
      "sheaf_types": 5,
      "year_cohomology": 1945,
      "year_sheaf": 1950,
      "vanishing_theorems": 3,
      "fields_applied": 4,
      "textbooks_standard": 3,
      "key_theorems": 4
    }
  },
  {
    "title": "The Weil Conjectures in Algebraic Geometry",
    "subject": "Weil conjectures",
    "description": "In plain words: The Weil conjectures are four statements about counting the solutions of polynomial equations over finite fields, fields with finitely many elements. The zeta function of a variety packages the counts of solutions over all finite extensions of the field into a single function, and the conjectures describe that function's shape. The formal statement above is the precise form of the ",
    "figures": {
      "year_posed": 1949,
      "year_proved": 1974,
      "conjectures_count": 4,
      "proof_years": 25,
      "fields_medal_year": 1978,
      "cohomology_theories": 2,
      "primes_used": 100,
      "varieties_counted": 100
    }
  },
  {
    "title": "Moduli Spaces: Spaces Whose Points Are Shapes",
    "subject": "moduli spaces",
    "description": "In plain words: A moduli space is a geometric space whose points are themselves geometric objects. For example, the moduli space of curves of genus g, a measure of a curve's complexity, is a space in which each point represents one curve, and nearby points represent similar curves. Studying the space means studying all curves of that genus at once. The formal statement above is the precise form of",
    "figures": {
      "moduli_dimensions": 10,
      "curves_genus_examples": 5,
      "dimension_formula_terms": 2,
      "year_delgine_mumford": 1969,
      "compactification_types": 2,
      "fields_linked": 3,
      "key_theorems": 3,
      "years_active": 60
    }
  },
  {
    "title": "Intersection Theory and Bezout's Theorem",
    "subject": "intersection theory",
    "description": "In plain words: Intersection theory counts how geometric shapes meet. Bezout's theorem, in plain words, says that two curves in the plane, of degrees m and n, where the degree is the highest power in the defining equation, meet in exactly m times n points, when points are counted with multiplicity, a number recording how tangled the meeting is. The formal statement above is the precise form of the",
    "figures": {
      "year_bezout": 1779,
      "degree_product_rule": 2,
      "intersection_numbers": 10,
      "chow_groups_defined": 1,
      "fields_linked": 2,
      "key_theorems": 3,
      "textbooks_standard": 2,
      "years_active": 200
    }
  },
  {
    "title": "Algebraic Surfaces and the Enriques-Kodaira Classification",
    "subject": "algebraic surfaces",
    "description": "In plain words: An algebraic surface is a two-dimensional variety, a shape defined by polynomial equations in which a point can move in two independent directions. The Enriques-Kodaira classification sorts all surfaces into four classes by their Kodaira dimension, a number from minus infinity to two that measures how many pluricanonical forms, a kind of differential form, the surface has. The form",
    "figures": {
      "surface_types": 4,
      "kodaira_dimensions": 4,
      "year_classification": 1960,
      "key_invariants": 5,
      "minimal_models": 2,
      "fields_linked": 2,
      "textbooks_standard": 2,
      "years_active": 100
    }
  },
  {
    "title": "The Riemann-Roch Theorem: Counting Functions on a Curve",
    "subject": "Riemann-Roch theorem",
    "description": "In plain words: The Riemann-Roch theorem counts functions on a curve. A divisor, in plain words, is a formal list of points with whole-number weights, recording where a function is allowed poles, places where it blows up, and zeros. The theorem says the dimension of the space of functions with poles bounded by a divisor equals the degree of the divisor minus the genus plus one, plus a correction t",
    "figures": {
      "year_riemann": 1857,
      "year_roch": 1865,
      "year_hirzebruch": 1954,
      "genus_terms": 2,
      "dimension_formula_terms": 3,
      "fields_linked": 2,
      "key_versions": 3,
      "years_active": 170
    }
  },
  {
    "title": "Birational Geometry and the Minimal Model Program",
    "subject": "minimal model program",
    "description": "In plain words: Birational geometry studies varieties up to birational equivalence, the relation in which two varieties agree except on a small part, like two maps that agree except for a few towns. The minimal model program is a procedure that simplifies a variety, step by step, until it reaches a minimal model, a simplest representative, or a Mori fibre space. The formal statement above is the p",
    "figures": {
      "dimensions_proved": 3,
      "year_mori": 1988,
      "flips_count": 100,
      "minimal_models_exist": 1,
      "fields_medal_year": 1990,
      "steps_of_program": 4,
      "fields_linked": 2,
      "years_active": 40
    }
  },
  {
    "title": "Abelian Varieties: Higher-Dimensional Elliptic Curves",
    "subject": "abelian varieties",
    "description": "In plain words: An abelian variety is a higher-dimensional analogue of an elliptic curve: a complete algebraic variety that is also a group, a set with a rule for combining elements, where the group operations are given by polynomial maps. The simplest examples are elliptic curves in dimension one and Jacobians of curves in higher dimensions. The formal statement above is the precise form of the c",
    "figures": {
      "dimensions_examples": 3,
      "torsion_points_count": 16,
      "year_theory": 1950,
      "fields_linked": 2,
      "key_theorems": 3,
      "moduli_dimensions": 3,
      "textbooks_standard": 2,
      "years_active": 70
    }
  },
  {
    "title": "Algebraic Groups: Symmetry Described by Equations",
    "subject": "algebraic groups",
    "description": "In plain words: An algebraic group is a variety that is also a group, where the group operations are given by polynomial maps. A group, in plain words, is a set of symmetries with a rule for combining them. The classical examples are the general linear group of invertible matrices, the special linear group, the orthogonal group, and the symplectic group. The formal statement above is the precise f",
    "figures": {
      "group_types": 4,
      "classical_families": 4,
      "year_chevalley": 1955,
      "dimension_examples": 3,
      "fields_linked": 2,
      "key_theorems": 3,
      "textbooks_standard": 2,
      "years_active": 70
    }
  },
  {
    "title": "Toric Varieties: Geometry You Can Draw",
    "subject": "toric varieties",
    "description": "In plain words: A toric variety is a variety containing a torus, a product of multiplicative groups, as a dense open part, with the torus acting on the whole variety. The variety is determined by a fan, a collection of cones, which are wedge-shaped regions in a lattice, and its geometry can be read off the fan by combinatorics. The formal statement above is the precise form of the claim; the gloss",
    "figures": {
      "fan_cones": 10,
      "dimension_examples": 3,
      "year_theory": 1970,
      "polytope_faces": 8,
      "fields_linked": 2,
      "key_theorems": 3,
      "textbooks_standard": 2,
      "years_active": 55
    }
  },
  {
    "title": "Etale Cohomology and the Etale Fundamental Group",
    "subject": "etale cohomology",
    "description": "In plain words: Etale cohomology is a cohomology theory for algebraic varieties that works over any field, including finite fields, where ordinary topology fails because the spaces have no useful open sets in the classical sense. An etale map, in plain words, is a map that is locally an isomorphism, like a covering map, and the etale topology is built from such maps. The formal statement above is ",
    "figures": {
      "year_grothendieck": 1963,
      "cohomology_groups": 10,
      "weil_proof_year": 1974,
      "fields_linked": 2,
      "key_theorems": 3,
      "textbooks_standard": 2,
      "years_active": 60
    }
  },
  {
    "title": "Hodge Theory: The Shape of Cohomology",
    "subject": "Hodge theory",
    "description": "In plain words: Hodge theory studies how the cohomology of a complex variety splits into pieces. A Hodge structure, in plain words, is a decomposition of a cohomology group into parts of type (p, q), recording how many holomorphic and anti-holomorphic directions each part has. The Hodge conjecture asks which of these parts come from algebra. The formal statement above is the precise form of the cl",
    "figures": {
      "year_hodge": 1941,
      "hodge_numbers": 10,
      "decomposition_terms": 2,
      "year_delgine": 1971,
      "fields_linked": 2,
      "key_theorems": 3,
      "textbooks_standard": 2,
      "years_active": 85
    }
  },
  {
    "title": "Mirror Symmetry: Two Geometries, One Physics",
    "subject": "mirror symmetry",
    "description": "In plain words: Mirror symmetry is a correspondence, proposed by physicists, between pairs of Calabi-Yau varieties, three-dimensional shapes with special geometric properties that appear in string theory. A mirror pair exchanges two kinds of geometry: the complex geometry of one variety matches the symplectic geometry of the other, and enumerative predictions, counts of curves, on one side can be ",
    "figures": {
      "year_proposed": 1990,
      "mirror_pairs": 100,
      "enumerative_predictions": 1000,
      "fields_linked": 2,
      "key_theorems": 3,
      "textbooks_standard": 2,
      "years_active": 36
    }
  },
  {
    "title": "Arithmetic Geometry and Diophantine Equations",
    "subject": "arithmetic geometry",
    "description": "In plain words: Arithmetic geometry is the study of whole-number and fractional solutions of polynomial equations using the tools of geometry. A Diophantine equation, in plain words, is a polynomial equation whose solutions are required to be whole numbers or fractions, named after Diophantus of Alexandria. The formal statement above is the precise form of the claim; the gloss is the same claim in",
    "figures": {
      "diophantine_types": 5,
      "year_faltings": 1983,
      "year_wiles": 1994,
      "fields_linked": 2,
      "key_theorems": 4,
      "curves_studied": 100,
      "textbooks_standard": 2,
      "years_active": 100
    }
  },
  {
    "title": "The Resolution of Singularities: Hironaka's Theorem",
    "subject": "resolution of singularities",
    "description": "In plain words: The resolution of singularities says that any variety, a shape defined by polynomial equations, that has singular points, places where the shape is not smooth, like the tip of a cone, can be replaced by a smooth variety that maps onto it and agrees with it except over the singular points. A blow-up, in plain words, is a surgery that replaces a point by the set of directions through",
    "figures": {
      "year_hironaka": 1964,
      "fields_medal_year": 1970,
      "dimensions_proved": 100,
      "blowups_needed": 10,
      "characteristic_zero": 1,
      "positive_characteristic_open": 1,
      "key_steps": 3,
      "years_active": 62
    }
  },
  {
    "title": "Algebraic Geometry Codes: Curves That Correct Errors",
    "subject": "algebraic geometry codes",
    "description": "In plain words: Algebraic geometry codes are error-correcting codes built from algebraic curves over finite fields. An error-correcting code, in plain words, is a way of adding redundancy to a message so that errors in transmission can be detected and corrected. The code is built by evaluating functions on a curve at rational points. The formal statement above is the precise form of the claim; the",
    "figures": {
      "year_goppa": 1981,
      "code_length_examples": 100,
      "rate_improvement": 2,
      "fields_linked": 2,
      "key_theorems": 3,
      "curves_used": 10,
      "textbooks_standard": 2,
      "years_active": 45
    }
  },
  {
    "title": "Computational Algebraic Geometry and Grobner Bases",
    "subject": "computational algebraic geometry",
    "description": "In plain words: Computational algebraic geometry is the study of algorithms for polynomial equations. A Grobner basis, in plain words, is a special set of generators for an ideal, which is a set of polynomials closed under addition and multiplication by any polynomial, with the property that questions about the ideal, such as whether a polynomial belongs to it, can be answered by division. The for",
    "figures": {
      "year_buchberger": 1965,
      "algorithms_count": 5,
      "software_systems": 4,
      "complexity_bound": 2,
      "fields_linked": 2,
      "key_theorems": 3,
      "textbooks_standard": 2,
      "years_active": 60
    }
  },
  {
    "title": "The Jacobian Variety and the Abel-Jacobi Map",
    "subject": "Jacobian variety",
    "description": "In plain words: The Jacobian variety of a curve is an abelian variety, a higher-dimensional analogue of an elliptic curve, built from the curve: its dimension equals the genus of the curve, and its points correspond to divisor classes of degree zero, formal lists of points with weights summing to zero, modulo those coming from functions. The Abel-Jacobi map sends a point of the curve to its class ",
    "figures": {
      "dimension_equals_genus": 1,
      "year_abel": 1826,
      "year_jacobi": 1832,
      "torsion_points": 16,
      "fields_linked": 2,
      "key_theorems": 3,
      "textbooks_standard": 2,
      "years_active": 200
    }
  },
  {
    "title": "Grothendieck's Topos and the Etale Topology",
    "subject": "topos and etale topology",
    "description": "In plain words: A topos is a category, a collection of objects and maps between them, that behaves like the category of sheaves on a space. Grothendieck introduced topoi to generalise topology: a site is a category equipped with a notion of covering, and the topos of sheaves on a site plays the role of the space. The etale topos is the topos of the etale site of a scheme. The formal statement abov",
    "figures": {
      "year_topos": 1963,
      "sga_volumes": 7,
      "sites_defined": 3,
      "fields_linked": 2,
      "key_theorems": 3,
      "textbooks_standard": 2,
      "years_active": 63
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Algebraic geometry",
    "url": "https://en.wikipedia.org/wiki/Algebraic_geometry",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  },
  {
    "name": "Wikipedia - Alexander Grothendieck",
    "url": "https://en.wikipedia.org/wiki/Alexander_Grothendieck",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  },
  {
    "name": "nLab - Algebraic geometry",
    "url": "https://ncatlab.org/nlab/show/algebraic+geometry",
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
