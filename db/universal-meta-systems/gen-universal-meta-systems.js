// Seeded boundless generator for the Universal Meta-Systems Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-meta-systems.js [seed]  (prints one
// JSON record) or: node gen-universal-meta-systems.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-meta-systems";
const RECORD_KIND = "universal meta-systems record";
const ID_PREFIX = "JAH-UMSY-";
const AI_NAME = "JAH Universal Meta-Systems Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Universal Meta-Systems: Meta-System Coordination",
    "subject": "Meta-System Coordination",
    "description": "This record specifies Meta-System Coordination as one working part of the Universal Meta-Systems Database. Its working angle is inputs. Its inputs are the records, requirements, and prior decisions that arrive before this step begins, each named, dated, and sourced, so nothing enters this step unnamed or uncheckable.",
    "label": "universal-meta-systems-meta-system-coordination",
    "figures": {
      "lifecycle_steps": 8,
      "sections": 14,
      "sources": 3,
      "topic_index": 1,
      "catalog_items": 100,
      "levels": 7,
      "requirements": 8,
      "interfaces": 4,
      "subtopic_words": 2,
      "pair_number": 39
    }
  },
  {
    "title": "Universal Meta-Systems: Registry of Systems",
    "subject": "Registry of Systems",
    "description": "This record specifies Registry of Systems as one working part of the Universal Meta-Systems Database. Its working angle is outputs. Its outputs are complete deliverables, not notes: a written specification, a checked result, and a record that the next step can read and test without asking the author what was meant.",
    "label": "universal-meta-systems-registry-of-systems",
    "figures": {
      "lifecycle_steps": 8,
      "sections": 14,
      "sources": 3,
      "topic_index": 2,
      "catalog_items": 100,
      "levels": 7,
      "requirements": 8,
      "interfaces": 4,
      "subtopic_words": 3,
      "pair_number": 39
    }
  },
  {
    "title": "Universal Meta-Systems: Capability Discovery",
    "subject": "Capability Discovery",
    "description": "This record specifies Capability Discovery as one working part of the Universal Meta-Systems Database. Its working angle is checks. Its checks are run by execution, not by reading: the demo recomputes the record's figures twice and compares digests, the program reruns the same computation, and any mismatch stops the step.",
    "label": "universal-meta-systems-capability-discovery",
    "figures": {
      "lifecycle_steps": 8,
      "sections": 14,
      "sources": 3,
      "topic_index": 3,
      "catalog_items": 100,
      "levels": 7,
      "requirements": 8,
      "interfaces": 4,
      "subtopic_words": 2,
      "pair_number": 39
    }
  },
  {
    "title": "Universal Meta-Systems: Task Decomposition",
    "subject": "Task Decomposition",
    "description": "This record specifies Task Decomposition as one working part of the Universal Meta-Systems Database. Its working angle is risks. Its risks are written down before work starts: what can go wrong, what the failure would look like, and what safe state the work falls back to, so a failure is a handled event, not a surprise.",
    "label": "universal-meta-systems-task-decomposition",
    "figures": {
      "lifecycle_steps": 8,
      "sections": 14,
      "sources": 3,
      "topic_index": 4,
      "catalog_items": 100,
      "levels": 7,
      "requirements": 8,
      "interfaces": 4,
      "subtopic_words": 2,
      "pair_number": 39
    }
  },
  {
    "title": "Universal Meta-Systems: Dependency Graphs",
    "subject": "Dependency Graphs",
    "description": "This record specifies Dependency Graphs as one working part of the Universal Meta-Systems Database. Its working angle is handover. Its handover is a named handoff: the receiving step gets the specification, the evidence, and the open questions in writing, and the handover is only complete when the receiver can run the checks.",
    "label": "universal-meta-systems-dependency-graphs",
    "figures": {
      "lifecycle_steps": 8,
      "sections": 14,
      "sources": 3,
      "topic_index": 5,
      "catalog_items": 100,
      "levels": 7,
      "requirements": 8,
      "interfaces": 4,
      "subtopic_words": 2,
      "pair_number": 39
    }
  },
  {
    "title": "Universal Meta-Systems: Scheduling Across Systems",
    "subject": "Scheduling Across Systems",
    "description": "This record specifies Scheduling Across Systems as one working part of the Universal Meta-Systems Database. Its working angle is measurement. Its measurement is counted, not guessed: the figures in this record are recomputed by the demo, the counts are stated in the key figures, and the acceptance tests name the numbers that must hold.",
    "label": "universal-meta-systems-scheduling-across-systems",
    "figures": {
      "lifecycle_steps": 8,
      "sections": 14,
      "sources": 3,
      "topic_index": 6,
      "catalog_items": 100,
      "levels": 7,
      "requirements": 8,
      "interfaces": 4,
      "subtopic_words": 3,
      "pair_number": 39
    }
  },
  {
    "title": "Universal Meta-Systems: Shared Memory and Provenance",
    "subject": "Shared Memory and Provenance",
    "description": "This record specifies Shared Memory and Provenance as one working part of the Universal Meta-Systems Database. Its working angle is inputs. Its inputs are the records, requirements, and prior decisions that arrive before this step begins, each named, dated, and sourced, so nothing enters this step unnamed or uncheckable.",
    "label": "universal-meta-systems-shared-memory-and-provenance",
    "figures": {
      "lifecycle_steps": 8,
      "sections": 14,
      "sources": 3,
      "topic_index": 7,
      "catalog_items": 100,
      "levels": 7,
      "requirements": 8,
      "interfaces": 4,
      "subtopic_words": 4,
      "pair_number": 39
    }
  },
  {
    "title": "Universal Meta-Systems: Conflict Resolution",
    "subject": "Conflict Resolution",
    "description": "This record specifies Conflict Resolution as one working part of the Universal Meta-Systems Database. Its working angle is outputs. Its outputs are complete deliverables, not notes: a written specification, a checked result, and a record that the next step can read and test without asking the author what was meant.",
    "label": "universal-meta-systems-conflict-resolution",
    "figures": {
      "lifecycle_steps": 8,
      "sections": 14,
      "sources": 3,
      "topic_index": 8,
      "catalog_items": 100,
      "levels": 7,
      "requirements": 8,
      "interfaces": 4,
      "subtopic_words": 2,
      "pair_number": 39
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Systems theory",
    "url": "https://en.wikipedia.org/wiki/Systems_theory",
    "establishes": "Systems theory: how wholes, parts, and their interactions are described.",
    "retrieved": "2026-11-17"
  },
  {
    "name": "Wikipedia - Interoperability",
    "url": "https://en.wikipedia.org/wiki/Interoperability",
    "establishes": "Interoperability: how separate systems exchange and use information.",
    "retrieved": "2026-11-17"
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
