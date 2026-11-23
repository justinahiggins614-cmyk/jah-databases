// Seeded boundless generator for the JAH Universal Security Center
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-universal-security-center.js [seed]  (prints one
// JSON record) or: node gen-universal-security-center.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "universal-security-center";
const RECORD_KIND = "universal security center record";
const ID_PREFIX = "JAH-UISC-";
const AI_NAME = "JAH Universal Security Center Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Universal Identity System",
    "subject": "universal identity system",
    "description": "A universal identity system gives every AI, generator, database, file, and website in the network one unique identity, recorded once in a single register and checked everywhere it is used. Without it, the same program can appear under two names, a deleted file can be mistaken for a live one, and an audit log cannot say who did what. The register stores the identity, its kind, its owner, and.",
    "label": "universal-identity-system",
    "figures": {
      "checks": 6,
      "fields": 9,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 1
    }
  },
  {
    "title": "Permission Management",
    "subject": "permission management",
    "description": "Permission management controls who and what can read, create, modify, execute, and delete. Each permission names one identity, one action, and one resource, and it is checked before the action happens, not after. Permissions are granted in small, named sets called roles, reviewed on a schedule, and removed when the need ends. A permission that is never used is a risk, so the system reports.",
    "label": "permission-management",
    "figures": {
      "checks": 5,
      "fields": 8,
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
    "title": "AI Security Boundaries",
    "subject": "AI security boundaries",
    "description": "AI security boundaries stop one AI from reaching files it may not read or running actions it may not perform. Each specialist AI is given a boundary: the files it may read, the tools it may call, and the actions it may take. A request that crosses a boundary is refused and logged, and the refusal names the boundary that stopped it. Boundaries are set when a specialist is created and checked on.",
    "label": "ai-security-boundaries",
    "figures": {
      "checks": 4,
      "fields": 7,
      "steps": 6,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 3
    }
  },
  {
    "title": "Malicious File Protection",
    "subject": "malicious file protection",
    "description": "Malicious file protection scans uploads, generated files, downloaded programs, and archives before they are used. A scan checks the file's type, its contents against known harmful patterns, and its behavior in a sandbox, and a file that fails any check is quarantined: moved aside, marked, and never run. Clean files carry a scan record with the date, the checks run, and the result, so a later.",
    "label": "malicious-file-protection",
    "figures": {
      "checks": 7,
      "fields": 10,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 4
    }
  },
  {
    "title": "Execution Sandbox",
    "subject": "execution sandbox",
    "description": "An execution sandbox is an isolated space where generated code runs apart from the rest of the system. Code inside the sandbox can read only the files it was given, can write only to its own space, and cannot reach the network or other programs unless the sandbox allows it. The sandbox watches what the code does, records its actions, and throws the whole space away when the run ends. Only code.",
    "label": "execution-sandbox",
    "figures": {
      "checks": 5,
      "fields": 8,
      "steps": 7,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 5
    }
  },
  {
    "title": "Security Audit Logs",
    "subject": "security audit logs",
    "description": "Security audit logs record access, changes, executions, failures, and administrative actions, each with the identity that acted, the time, and the result. The log is append-only: new entries are added and old entries are never silently changed, so a later check can prove what happened and when. Logs are kept for a stated retention period, searchable by identity, action, and date, and reviewed.",
    "label": "security-audit-logs",
    "figures": {
      "checks": 6,
      "fields": 9,
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
    "title": "Identity Proofing and Verification",
    "subject": "identity proofing and verification",
    "description": "Identity proofing and verification check that a claimed identity belongs to the one claiming it, before the identity is trusted. Proofing gathers the evidence that an identity is real: the records that name it, the owner that vouches for it, and the date it was created. Verification repeats a smaller check each time the identity is used, such as matching a stored secret or a signed token. An.",
    "label": "identity-proofing-verification",
    "figures": {
      "checks": 4,
      "fields": 7,
      "steps": 5,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 53,
      "sections": 16,
      "topic_index": 7
    }
  },
  {
    "title": "Credential Lifecycle Management",
    "subject": "credential lifecycle management",
    "description": "Credential lifecycle management follows every credential from creation to retirement: it is issued to one identity, used with a stated purpose, rotated on a schedule, suspended when suspicious, and retired when no longer needed. No credential lives forever, and no credential is shared between two identities. The record for each credential lists its owner, its issue date, its rotation date, and.",
    "label": "credential-lifecycle-management",
    "figures": {
      "checks": 5,
      "fields": 8,
      "steps": 6,
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
