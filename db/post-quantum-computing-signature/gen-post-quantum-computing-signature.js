// Seeded boundless generator for the Post-Quantum Computing Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-post-quantum-computing-signature.js [seed]  (prints one
// JSON record) or: node gen-post-quantum-computing-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "post-quantum-computing-signature";
const RECORD_KIND = "future post-quantum computing record";
const ID_PREFIX = "JAH-PQCMS-";
const AI_NAME = "JAH Post-Quantum Computing Researcher (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: Quantum-Safe Library",
    "subject": "signature quantum-safe library",
    "description": "A Signature-made design-study for a quantum-safe library: a single shelf of defensive codes, each labeled with its maturity, its key sizes, and its migration notes, so a builder can choose without guessing. The design imagines the library as a workshop where ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism) handles key exchange, ML-DSA (Module-Lattice-Based Digital Signature Algorithm).",
    "label": "sig-quantum-safe-library",
    "figures": {
      "codes": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "shelves": 1
    }
  },
  {
    "title": "Signature Design: Lattice Workshop",
    "subject": "signature lattice workshop",
    "description": "A Signature-made design-study for a lattice workshop: a room where lattice codes are built, measured, and taught, with grids drawn on the walls and key sizes written beside each bench. The design imagines apprentices learning lattices by building small grids first, then the ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism) and ML-DSA (Module-Lattice-Based Digital Signature Algorithm).",
    "label": "sig-lattice-workshop",
    "figures": {
      "benches": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "grids": 3
    }
  },
  {
    "title": "Signature Design: Code-Based Vault",
    "subject": "signature code-based vault",
    "description": "A Signature-made design-study for a code-based vault: a strong room holding the oldest post-quantum family, the McEliece cryptosystem from 1978, with its large keys stored on labeled shelves and its decades of study recorded on the wall. The design imagines the vault as proof that old does not mean weak: the codes have survived decades of public attack, and the vault's job is to keep that.",
    "label": "sig-code-based-vault",
    "figures": {
      "shelves": 5,
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
    "title": "Signature Design: Hash Signature Tree",
    "subject": "signature hash signature tree",
    "description": "A Signature-made design-study for a hash signature tree: a tree whose leaves are one-time signature keys and whose branches combine them into a single SLH-DSA (Stateless Hash-Based Digital Signature Algorithm) key that can sign many messages. The design imagines the tree grown in a garden, pruned so no leaf is ever used twice, with the hash functions, which are one-way fingerprints of data, as.",
    "label": "sig-hash-signature-tree",
    "figures": {
      "leaves": 1024,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "trees": 1
    }
  },
  {
    "title": "Signature Design: Multivariate Atelier",
    "subject": "signature multivariate atelier",
    "description": "A Signature-made design-study for a multivariate atelier: a studio where many-variable equations are drawn, tested, and, when broken, kept as lessons on the wall. The design imagines the atelier as honest about its family's history: several proposals broken, each break recorded with its date and its lesson, so no visitor mistakes a broken proposal for a standard. This is a design-study,.",
    "label": "sig-multivariate-atelier",
    "figures": {
      "equations": 48,
      "lessons": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24
    }
  },
  {
    "title": "Signature Design: Isogeny Map Room",
    "subject": "signature isogeny map room",
    "description": "A Signature-made design-study for an isogeny map room: a room of maps between elliptic curves, the smooth curve shapes used in cryptography, with the secret paths marked only for their owners and the 2022 break of SIKE (Supersingular Isogeny Key Encapsulation) marked in red on the largest map. The design imagines the room as a place for research, not deployment: visitors trace paths, count.",
    "label": "sig-isogeny-map-room",
    "figures": {
      "maps": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "break_year": 2022
    }
  },
  {
    "title": "Signature Design: Standards Council Hall",
    "subject": "signature standards council hall",
    "description": "A Signature-made design-study for a standards council hall: a hall where the NIST (National Institute of Standards and Technology) process is replayed as a public ceremony, with three rounds, four first standards, and the dropped candidates honored for the attacks that found them weak. The design imagines the hall as a lesson in how defensive security is chosen: openly, slowly, and with.",
    "label": "sig-standards-council-hall",
    "figures": {
      "rounds": 3,
      "first_standards": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "process_start_year": 2016
    }
  },
  {
    "title": "Signature Design: Key Exchange Post Office",
    "subject": "signature key exchange post office",
    "description": "A Signature-made design-study for a key exchange post office: a post office where secret keys are locked in parcels called ciphertexts and sent to their receivers, using ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism) as the standard parcel service. The design imagines three parcel sizes, ML-KEM-512, ML-KEM-768, and ML-KEM-1024, each with its weight in bytes written on the counter,.",
    "label": "sig-key-exchange-post-office",
    "figures": {
      "parcel_sizes": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 47,
      "sections": 16,
      "ladder_ranks": 24,
      "counters": 1
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
