// Seeded boundless generator for the JAH Universal Security Center
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-security-center-signature.js [seed]  (prints one
// JSON record) or: node gen-universal-security-center-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-security-center-signature";
const RECORD_KIND = "universal security center record";
const ID_PREFIX = "JAH-UISCS-";
const AI_NAME = "JAH Universal Security Center Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Identity Atrium — Signature Design",
    "subject": "identity atrium design",
    "description": "The Identity Atrium is a Signature-made design for the identity register, imagined as a hall with one door per identity. Each door carries the identity's name, kind, owner, and creation date, and a visitor may enter only through the door that matches the identity they claim. The design is a proposal: it shows how an identity register could be read at a glance, with retired identities shown as.",
    "label": "identity-atrium-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 1
    }
  },
  {
    "title": "The Permission Loom — Signature Design",
    "subject": "permission loom design",
    "description": "The Permission Loom is a Signature-made design for permission management, imagined as a loom where each thread is one permission and each cloth is one role. A role is woven from threads, and a permission is granted by adding a thread to the cloth. When a job ends, its cloth is unwoven, and the threads return to the store. The design shows how permissions could be seen as woven cloth: a wide.",
    "label": "permission-loom-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 2
    }
  },
  {
    "title": "The Boundary Gate — Signature Design",
    "subject": "boundary gate design",
    "description": "The Boundary Gate is a Signature-made design for AI security boundaries, imagined as a gatehouse where each specialist AI passes through a gate built for it alone. The gate lists the files the AI may read and the tools it may call, and anything beyond the list is refused at the gate and written in the gate book. The design shows how a boundary could be a place, not a paragraph: a gate that is.",
    "label": "boundary-gate-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 3
    }
  },
  {
    "title": "The File Sieve — Signature Design",
    "subject": "file sieve design",
    "description": "The File Sieve is a Signature-made design for malicious file protection, imagined as a sieve through which every file must pass before use. Clean files fall through to the shelf; files that fail a check stay in the sieve and are carried to quarantine. The sieve is shaken by three checks: type, contents, and behavior, and the design shows how a scan could be a single visible step instead of a.",
    "label": "file-sieve-design",
    "figures": {
      "checks": 4,
      "fields": 6,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 4
    }
  },
  {
    "title": "The Sandbox Garden — Signature Design",
    "subject": "sandbox garden design",
    "description": "The Sandbox Garden is a Signature-made design for the execution sandbox, imagined as a walled garden where generated code is planted and watched. The code may touch only the soil it was given, and the gardener watches what grows and writes it in the garden book. When the run ends, the garden bed is dug over and made fresh. The design shows how isolation could be a place with walls, a watcher,.",
    "label": "sandbox-garden-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 5
    }
  },
  {
    "title": "The Audit Ledger — Signature Design",
    "subject": "audit ledger design",
    "description": "The Audit Ledger is a Signature-made design for security audit logs, imagined as a great bound book where every action is written in ink by the hand that did it. Pages are never torn out and entries are never erased; a correction is a new entry that names the old one. The design shows how an audit log could be read as a book: open it at any date and see who did what, in order, with nothing.",
    "label": "audit-ledger-design",
    "figures": {
      "checks": 3,
      "fields": 6,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 6
    }
  },
  {
    "title": "The Proofing Porch — Signature Design",
    "subject": "proofing porch design",
    "description": "The Proofing Porch is a Signature-made design for identity proofing, imagined as a porch where a new identity is examined before it is let inside. The claimant lays out its evidence on the porch table: the records that name it, the owner that vouches for it, and the date it was created. If the evidence holds, the door opens; if not, the claimant waits on the porch. The design shows proofing as.",
    "label": "proofing-porch-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 7
    }
  },
  {
    "title": "The Credential Well — Signature Design",
    "subject": "credential well design",
    "description": "The Credential Well is a Signature-made design for credential lifecycle management, imagined as a well from which credentials are drawn fresh each morning and poured back each evening. A credential drawn too long ago is stale and is not used; a credential that is suspicious is dropped into the deep well and never drawn again. The design shows how a credential's life could be seen as water:.",
    "label": "credential-well-design",
    "figures": {
      "checks": 3,
      "fields": 5,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 8
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Computer security",
    "url": "https://en.wikipedia.org/wiki/Computer_security",
    "establishes": "Computer security: how systems protect data and programs from unwanted access and harm.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Computer_security"
  },
  {
    "name": "Wikipedia - Identity management",
    "url": "https://en.wikipedia.org/wiki/Identity_management",
    "establishes": "Identity management: how unique identities are created, kept, and checked.",
    "retrieved": "2026-11-18",
    "resource_id": "en.wikipedia.org/wiki/Identity_management"
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
