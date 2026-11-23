// Seeded boundless generator for the Post-Quantum Computing Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-post-quantum-computing.js [seed]  (prints one
// JSON record) or: node gen-post-quantum-computing.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "post-quantum-computing";
const RECORD_KIND = "future post-quantum computing record";
const ID_PREFIX = "JAH-PQCM-";
const AI_NAME = "JAH Post-Quantum Computing Researcher";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Post-Quantum Computing Is",
    "subject": "post-quantum computing identity",
    "description": "Post-quantum computing is the study of computers and codes after quantum computers arrive: a quantum computer is a computer that uses quantum physics, the physics of very small things, to calculate in ways ordinary computers cannot, and post-quantum cryptography is the family of codes designed to stay safe even against such a machine. Ordinary computers protect messages with codes like RSA.",
    "label": "post-quantum-computing-identity",
    "figures": {
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "standardized_algorithms": 4,
      "shor_year": 1994,
      "ladder_ranks": 24
    }
  },
  {
    "title": "Shor's Algorithm and the Quantum Threat",
    "subject": "shor's algorithm and the quantum threat",
    "description": "Shor's algorithm is a quantum method for factoring large numbers and for solving discrete logarithms, which are the two hard problems behind RSA (Rivest-Shamir-Adleman) and elliptic-curve cryptography, the codes that protect most internet traffic today. Published by Peter Shor in 1994, the method runs in polynomial time on a quantum computer, which means its run time grows slowly as the.",
    "label": "shors-algorithm-threat",
    "figures": {
      "shor_year": 1994,
      "hard_problems": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24
    }
  },
  {
    "title": "Lattice-Based Cryptography",
    "subject": "lattice-based cryptography",
    "description": "Lattice-based cryptography is the family of post-quantum codes built on lattices, which are regular grids of points in many dimensions. The hard puzzle is to find a short path or a nearby point in a grid with hundreds of dimensions, which stays hard for ordinary and quantum computers alike. The best-known methods are ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism), the NIST (National.",
    "label": "lattice-based-cryptography",
    "figures": {
      "lattice_dimensions": 512,
      "security_bits": 128,
      "ml_kem_public_key_bytes": 1184,
      "ml_kem_ciphertext_bytes": 1088,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 16
    }
  },
  {
    "title": "Code-Based Cryptography",
    "subject": "code-based cryptography",
    "description": "Code-based cryptography is the oldest post-quantum family, built on error-correcting codes, which are methods for sending messages with extra bits so that errors can be found and fixed. The classic method is the McEliece cryptosystem, published in 1978: the public key is a scrambled error-correcting code, the private key is the unscrambling, and decoding a scrambled message without the private.",
    "label": "code-based-cryptography",
    "figures": {
      "mceliece_year": 1978,
      "decades_studied": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24
    }
  },
  {
    "title": "Hash-Based Signatures",
    "subject": "hash-based signatures",
    "description": "Hash-based signatures are signatures built only from hash functions, which are one-way fingerprints of data: a hash function turns any message into a short fixed-size fingerprint, and it is practically impossible to work backwards from the fingerprint to the message. The classic idea is the Lamport one-time signature, and the modern standardized method is SLH-DSA (Stateless Hash-Based Digital.",
    "label": "hash-based-signatures",
    "figures": {
      "sphincs_public_key_bytes": 32,
      "sphincs_signature_bytes": 7856,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24
    }
  },
  {
    "title": "Multivariate Cryptography",
    "subject": "multivariate cryptography",
    "description": "Multivariate cryptography is the family of post-quantum codes built on systems of equations in many variables: the public key is a set of quadratic equations, which are equations with squared terms, that are easy to evaluate but hard to solve backwards without the private key, which hides a trapdoor, a secret structure that makes solving easy for the owner. Multivariate signatures can be very.",
    "label": "multivariate-cryptography",
    "figures": {
      "variables": 64,
      "equations": 48,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24
    }
  },
  {
    "title": "Isogeny-Based Cryptography",
    "subject": "isogeny-based cryptography",
    "description": "Isogeny-based cryptography is the family of post-quantum codes built on isogenies, which are maps between elliptic curves, the smooth curve shapes used in today's elliptic-curve codes. The hard puzzle is to find the secret map between two curves when only the start and end curves are known. Isogeny codes once promised the smallest keys of any post-quantum family, small enough for the tiniest.",
    "label": "isogeny-based-cryptography",
    "figures": {
      "sike_break_year": 2022,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "families": 5
    }
  },
  {
    "title": "The NIST Standardization Process",
    "subject": "NIST standardization process",
    "description": "The NIST (National Institute of Standards and Technology) standardization process is the open competition, begun in 2016, that chose the first post-quantum cryptography standards. Teams from around the world submitted candidate algorithms, the public studied and attacked them for years across three rounds, and NIST (National Institute of Standards and Technology) announced the first four.",
    "label": "nist-standardization-process",
    "figures": {
      "process_start_year": 2016,
      "announcement_year": 2022,
      "rounds": 3,
      "first_standards": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "sections": 16
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Post-quantum cryptography",
    "url": "https://en.wikipedia.org/wiki/Post-quantum_cryptography",
    "establishes": "Post-quantum cryptography: cryptography designed to stay safe against a future quantum computer.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Post-quantum_cryptography"
  },
  {
    "name": "Wikipedia - Quantum computing",
    "url": "https://en.wikipedia.org/wiki/Quantum_computing",
    "establishes": "Quantum computing: how computers using quantum physics calculate, and why they threaten today's codes.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Quantum_computing"
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
  const label = topic.label;
  const demo = buildDemo(topic, label);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: EDITION === "public" ? "public-harvest" : "signature-generated",
    ai_name: AI_NAME,
    description: topic.description + " " + "No claim of consciousness, sentience, or unlimited intelligence is established by this system; singularity and self-aware framing here is a Signature design claim only, never established fact.",
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One record: a single entry, fully specified and checkable.", A2: "The whole type: every part of the type, specified and tested together.", A3: "The type against the network: the type feeding websites, generators, and the generator database." },
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
