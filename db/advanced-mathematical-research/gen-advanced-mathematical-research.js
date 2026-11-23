// Seeded boundless generator for the Advanced Mathematical Research Database (public edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-advanced-mathematical-research.js [seed]  (prints one JSON record) or:
// node gen-advanced-mathematical-research.js --test (runTests). Package-only; outputs are
// generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "advanced-mathematical-research";
const RECORD_KIND = "advanced mathematical research record";
const ID_PREFIX = "JAH-AMR-";
const AI_NAME = "JAH Advanced Mathematical Research Librarian";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Riemann Hypothesis: The Greatest Open Problem in Mathematics",
    "subject": "Riemann hypothesis",
    "description": "In plain words: The Riemann hypothesis is a statement about the zeta function, a function that encodes information about the prime numbers, which are the whole numbers greater than 1 that have no divisors except 1 and themselves. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "millennium_problems": 7,
      "prize_dollars": 1000000,
      "year_posed": 1859,
      "primes_below_100": 25,
      "zeros_checked_trillions": 10,
      "critical_zeros": 100,
      "years_open": 167,
      "related_problems": 6
    }
  },
  {
    "title": "Fermat's Last Theorem: Proved by Andrew Wiles",
    "subject": "Fermat's Last Theorem",
    "description": "In plain words: Fermat's Last Theorem says that the equation x to the power n plus y to the power n equals z to the power n has no solutions in positive whole numbers when n is greater than 2. A whole number is a counting number like 1, 2, or 3. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "year_stated": 1637,
      "year_proved": 1994,
      "years_open": 357,
      "exponent_min": 3,
      "proof_pages": 100,
      "prize_year": 2016,
      "abel_prize_year": 2016,
      "cases_checked": 2
    }
  },
  {
    "title": "The Poincare Conjecture: The Shape of Three-Dimensional Space",
    "subject": "Poincare conjecture",
    "description": "In plain words: The Poincare conjecture is a statement about the shape of three-dimensional space. A manifold is a space that looks flat up close, like the surface of the Earth looks flat to a person standing on it; a 3-manifold is the three-dimensional version, and the 3-sphere is the three-dimensional analogue of the surface of a ball. The formal statement above is the precise form of the claim;",
    "figures": {
      "year_posed": 1904,
      "year_proved": 2003,
      "dimensions": 3,
      "millennium_problems": 7,
      "prize_dollars": 1000000,
      "prize_declined": 1,
      "years_open": 99,
      "fields_medal_year": 2006
    }
  },
  {
    "title": "The Four Colour Theorem: The First Major Computer-Assisted Proof",
    "subject": "Four color theorem",
    "description": "In plain words: The four colour theorem says that any map drawn on a flat surface can be coloured with four colours so that no two regions sharing a border have the same colour. A planar map is a map that can be drawn on a flat page without lines crossing. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "colors_needed": 4,
      "year_posed": 1852,
      "year_proved": 1976,
      "cases_checked": 1936,
      "proof_pages": 100,
      "years_open": 124,
      "map_regions": 4,
      "rechecks": 3
    }
  },
  {
    "title": "The Classification of Finite Simple Groups: Thirty Thousand Pages",
    "subject": "classification of finite simple groups",
    "description": "In plain words: The classification of finite simple groups is a complete list of the building blocks of finite symmetry. A group, in plain words, is a set of symmetries with a rule for combining them; a simple group is one that cannot be broken into smaller symmetry groups, the way a prime number cannot be broken into smaller factors. The formal statement above is the precise form of the claim; th",
    "figures": {
      "groups_families": 18,
      "sporadic_groups": 26,
      "proof_pages": 30000,
      "year_completed": 2004,
      "largest_group_order_digits": 54,
      "authors_count": 100,
      "years_work": 50,
      "theorems_count": 1
    }
  },
  {
    "title": "The Langlands Program: A Grand Unification of Mathematics",
    "subject": "Langlands program",
    "description": "In plain words: The Langlands program is a web of conjectures connecting number theory, the study of whole numbers; representation theory, the study of symmetry through matrices; and harmonic analysis, the study of functions by their frequencies. A conjecture is a precise mathematical guess that has not yet been proved. The formal statement above is the precise form of the claim; the gloss is the ",
    "figures": {
      "year_proposed": 1967,
      "conjectures_count": 10,
      "fields_linked": 3,
      "abel_prize_year": 2018,
      "fundamental_lemma_year": 2008,
      "proof_pages_lemma": 300,
      "cases_proved": 5,
      "years_active": 59
    }
  },
  {
    "title": "Hilbert's Problems: Twenty-Three Questions That Shaped a Century",
    "subject": "Hilbert's problems",
    "description": "In plain words: Hilbert's problems are twenty-three questions David Hilbert posed at the International Congress of Mathematicians in Paris in 1900. A problem, in plain words, is a precise question with a definite answer, and Hilbert chose questions he believed would drive mathematics for a century. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary",
    "figures": {
      "problems_count": 23,
      "year_posed": 1900,
      "solved_count": 15,
      "open_count": 8,
      "congress_city_problems": 23,
      "years_active": 126,
      "fields_touched": 10,
      "followup_problems": 7
    }
  },
  {
    "title": "The Millennium Prize Problems: Seven Problems, One Solved",
    "subject": "Millennium Prize Problems",
    "description": "In plain words: The Millennium Prize Problems are seven problems chosen by the Clay Mathematics Institute in 2000, each carrying a prize of one million dollars for a correct, peer-reviewed solution. A prize problem is a question chosen because its solution would be a landmark in mathematics. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "problems_count": 7,
      "solved_count": 1,
      "open_count": 6,
      "prize_dollars": 1000000,
      "year_announced": 2000,
      "year_solved": 2003,
      "institutes": 1,
      "fields_covered": 5
    }
  },
  {
    "title": "The Birch and Swinnerton-Dyer Conjecture: Rational Points on Elliptic Curves",
    "subject": "Birch and Swinnerton-Dyer conjecture",
    "description": "In plain words: The Birch and Swinnerton-Dyer conjecture connects two ways of measuring an elliptic curve, a kind of equation whose solutions form a curve with a group structure. The rank is the number of independent rational points, points with fractional coordinates; the L-function is an analytic object built from the curve's behaviour at every prime. The formal statement above is the precise fo",
    "figures": {
      "year_posed": 1965,
      "millennium_problems": 7,
      "prize_dollars": 1000000,
      "rank_cases_proved": 2,
      "rank_0_proved": 1,
      "rank_1_proved": 1,
      "curves_tested": 1000,
      "years_open": 61
    }
  },
  {
    "title": "The Hodge Conjecture: Which Shapes Come from Algebra",
    "subject": "Hodge conjecture",
    "description": "In plain words: The Hodge conjecture is a statement about algebraic varieties, geometric shapes defined by polynomial equations. A Hodge class is a cohomology class, a way of measuring holes and twists in a shape, of a special type; an algebraic cycle is a sub-shape cut out by more polynomial equations. The conjecture says every Hodge class comes from algebra. The formal statement above is the pre",
    "figures": {
      "year_posed": 1950,
      "millennium_problems": 7,
      "prize_dollars": 1000000,
      "dimensions_proved": 2,
      "years_open": 76,
      "related_theorems": 3,
      "fields_linked": 2
    }
  },
  {
    "title": "Navier-Stokes Existence and Smoothness: Do the Equations Break Down",
    "subject": "Navier-Stokes existence and smoothness",
    "description": "In plain words: The Navier-Stokes problem asks whether the equations that describe the flow of a fluid, like water or air, always have smooth solutions that last forever, or whether a solution can blow up, becoming infinite in finite time. A smooth solution is one without kinks or infinities; blow-up would mean the equations stop making physical sense. The formal statement above is the precise for",
    "figures": {
      "year_posed": 2000,
      "millennium_problems": 7,
      "prize_dollars": 1000000,
      "dimensions": 3,
      "equations_count": 4,
      "years_open": 26,
      "partial_results": 10,
      "known_solutions": 2
    }
  },
  {
    "title": "P versus NP: The Central Question of Computer Science",
    "subject": "P versus NP problem",
    "description": "In plain words: P versus NP asks whether every problem whose solution can be checked quickly can also be solved quickly. P is the class of problems solvable in polynomial time, meaning the time grows manageably with the size of the input; NP is the class whose solutions can be checked in polynomial time. The question is whether the two classes are the same. The formal statement above is the precis",
    "figures": {
      "year_posed": 1971,
      "millennium_problems": 7,
      "prize_dollars": 1000000,
      "years_open": 55,
      "np_complete_problems": 3000,
      "barrier_results": 3,
      "fields_linked": 2
    }
  },
  {
    "title": "Mathematical Proof: What Counts as a Proof",
    "subject": "mathematical proof",
    "description": "In plain words: A mathematical proof is a finite sequence of logical steps, each following from earlier steps and from axioms, which are starting assumptions accepted without proof, that ends with the claimed statement. In plain words, a proof is an argument that leaves no gap: anyone who accepts the starting points must accept the conclusion. The formal statement above is the precise form of the ",
    "figures": {
      "proof_types": 5,
      "axioms_zfc": 9,
      "year_euclid": 300,
      "formal_systems": 4,
      "proof_assistants": 3,
      "centuries_of_practice": 23,
      "checkers": 2,
      "fields_applied": 10
    }
  },
  {
    "title": "The abc Conjecture: A Deep Claim About Addition and Multiplication",
    "subject": "abc conjecture",
    "description": "In plain words: The abc conjecture is a statement about the tension between addition and multiplication. Take three whole numbers with a plus b equals c, sharing no common prime factor. The conjecture says that c cannot be much larger than the product of the distinct prime factors of a, b, and c, except in finitely many cases. A prime factor is a prime number that divides the number. The formal st",
    "figures": {
      "year_posed": 1985,
      "claimed_proof_year": 2012,
      "proof_pages": 500,
      "years_open": 41,
      "implied_theorems": 10,
      "workshops_held": 3,
      "verification_status": 0,
      "related_conjectures": 4
    }
  },
  {
    "title": "The Twin Prime Conjecture: Primes in Pairs",
    "subject": "twin prime conjecture",
    "description": "In plain words: The twin prime conjecture says there are infinitely many pairs of primes that differ by two, such as 3 and 5, 5 and 7, 11 and 13. A prime is a whole number greater than 1 with no divisors except 1 and itself, and twin primes are two primes two apart. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "year_posed": 1849,
      "gap_bound_proved": 246,
      "original_gap": 70000000,
      "year_zhang": 2013,
      "pairs_below_100": 8,
      "years_open": 177,
      "primes_below_100": 25,
      "polymath_contributors": 50
    }
  },
  {
    "title": "Goldbach's Conjecture: Every Even Number Is a Sum of Two Primes",
    "subject": "Goldbach's conjecture",
    "description": "In plain words: Goldbach's conjecture says that every even whole number greater than 2 can be written as the sum of two prime numbers. A prime is a whole number greater than 1 with no divisors except 1 and itself. For example, 10 equals 3 plus 7, and 100 equals 3 plus 97. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "year_posed": 1742,
      "checked_up_to": 4000000000000000000,
      "years_open": 284,
      "weak_case_proved_year": 2013,
      "primes_below_100": 25,
      "even_numbers_tested": 100,
      "proof_pages_weak": 100,
      "related_problems": 3
    }
  },
  {
    "title": "The Collatz Conjecture: The Simplest Unsolved Problem",
    "subject": "Collatz conjecture",
    "description": "In plain words: The Collatz conjecture concerns a simple rule: start with any positive whole number; if it is even, halve it; if it is odd, multiply by three and add one; repeat. The conjecture says you always reach 1. For example, starting from 6: 6, 3, 10, 5, 16, 8, 4, 2, 1. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "year_posed": 1937,
      "checked_up_to_trillions": 2,
      "years_open": 89,
      "steps_max_recorded": 2000,
      "rule_steps": 2,
      "starting_numbers_tested": 100,
      "proofs_found": 0,
      "related_problems": 2
    }
  },
  {
    "title": "The Continuum Hypothesis: Independence from the Axioms",
    "subject": "continuum hypothesis",
    "description": "In plain words: The continuum hypothesis is a statement about sizes of infinity. Georg Cantor showed there are different sizes of infinity: the counting numbers form one size, and the real numbers, the points on a line, form a strictly larger one. The hypothesis says there is no size of infinity strictly between those two. The formal statement above is the precise form of the claim; the gloss is t",
    "figures": {
      "year_posed": 1878,
      "year_godel": 1940,
      "year_cohen": 1963,
      "axioms_zfc": 9,
      "cardinalities_between": 0,
      "years_open_question": 85,
      "hilbert_problem": 1,
      "models_built": 2
    }
  },
  {
    "title": "Godel's Incompleteness Theorems: The Limits of Formal Systems",
    "subject": "Godel's incompleteness theorems",
    "description": "In plain words: Godel's incompleteness theorems say that any consistent formal system strong enough to do arithmetic contains true statements that the system cannot prove, and that such a system cannot prove its own consistency. A formal system is a precise set of axioms and rules for deriving theorems. The formal statement above is the precise form of the claim; the gloss is the same claim in ord",
    "figures": {
      "year_proved": 1931,
      "theorems_count": 2,
      "axioms_zfc": 9,
      "self_reference_steps": 3,
      "years_since": 95,
      "systems_affected": 100,
      "proof_pages": 50,
      "fields_touched": 3
    }
  },
  {
    "title": "The Weil Conjectures: Counting Points, Finding Patterns",
    "subject": "Weil conjectures",
    "description": "In plain words: The Weil conjectures are four statements about counting solutions of polynomial equations over finite fields, fields with finitely many elements. The zeta function of a variety, a geometric shape defined by equations, packages the counts of solutions over all finite extensions of the field into one function. The formal statement above is the precise form of the claim; the gloss is ",
    "figures": {
      "year_posed": 1949,
      "year_proved": 1974,
      "conjectures_count": 4,
      "proof_years": 25,
      "fields_medal_year": 1978,
      "varieties_counted": 100,
      "primes_used": 100,
      "years_open": 25
    }
  },
  {
    "title": "The Mordell Conjecture: Faltings's Theorem on Rational Points",
    "subject": "Mordell conjecture (Faltings's theorem)",
    "description": "In plain words: The Mordell conjecture, now Faltings's theorem, says that a curve of genus at least two, a measure of how complicated the curve is, defined over the rational numbers, has only finitely many rational points, points whose coordinates are fractions. A rational point is a solution in fractions to the curve's equation. The formal statement above is the precise form of the claim; the glo",
    "figures": {
      "year_posed": 1922,
      "year_proved": 1983,
      "genus_min": 2,
      "fields_medal_year": 1986,
      "years_open": 61,
      "rational_points_max": 0,
      "proof_pages": 100,
      "curves_covered": 100
    }
  },
  {
    "title": "The Kepler Conjecture: The Densest Way to Stack Spheres",
    "subject": "Kepler conjecture",
    "description": "In plain words: The Kepler conjecture says that the densest way to pack equal spheres, like oranges in a crate, is the face-centred cubic packing, the arrangement greengrocers use, with density about 74 percent. Density, in plain words, is the fraction of space filled by the spheres. The formal statement above is the precise form of the claim; the gloss is the same claim in ordinary words.",
    "figures": {
      "year_posed": 1611,
      "year_proved": 1998,
      "density_percent": 74,
      "cases_checked": 5000,
      "proof_pages": 300,
      "years_open": 387,
      "formal_proof_year": 2014,
      "spheres_arranged": 3
    }
  },
  {
    "title": "Research Recognition: The Abel Prize and the Fields Medal",
    "subject": "Abel Prize and Fields Medal",
    "description": "In plain words: The Abel Prize and the Fields Medal are the two most prestigious recognitions in mathematics. The Fields Medal, awarded every four years to mathematicians under forty, began in 1936; the Abel Prize, awarded annually without an age limit, began in 2003. Both are awarded for published, peer-reviewed work judged by committees of experts. The formal statement above is the precise form ",
    "figures": {
      "abel_year": 2003,
      "fields_year": 1936,
      "fields_age_limit": 40,
      "abel_prize_money": 7500000,
      "fields_medals_per_congress": 4,
      "abel_laureates": 22,
      "fields_laureates": 60,
      "years_fields": 90
    }
  },
  {
    "title": "Reproducibility in Mathematical Research: Checking the Checkers",
    "subject": "reproducibility in mathematical research",
    "description": "In plain words: Reproducibility in mathematics means that a result can be checked again, by another researcher, from the same starting points, and the same conclusion reached. A proof is reproducible when its steps can be followed; a computation is reproducible when its code and data are available and give the same output. The formal statement above is the precise form of the claim; the gloss is t",
    "figures": {
      "replication_studies": 10,
      "formal_projects": 5,
      "proof_assistants": 3,
      "years_active": 20,
      "cases_rechecked": 100,
      "journals_requiring_code": 5,
      "open_data_policies": 10,
      "fields_covered": 5
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Riemann hypothesis",
    "url": "https://en.wikipedia.org/wiki/Riemann_hypothesis",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  },
  {
    "name": "Wikipedia - Millennium Prize Problems",
    "url": "https://en.wikipedia.org/wiki/Millennium_Prize_Problems",
    "establishes": "Fetched 2026-11-17; HTTP 200 on retrieval. Establishes the statements cited from it in this record."
  },
  {
    "name": "MathWorld - Riemann Hypothesis",
    "url": "https://mathworld.wolfram.com/RiemannHypothesis.html",
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
