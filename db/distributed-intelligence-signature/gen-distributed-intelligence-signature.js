// Seeded boundless generator for the Distributed Intelligence Database database
// (Signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-distributed-intelligence-signature.js [seed]
// (prints one JSON record) or: node gen-distributed-intelligence-signature.js
// --test (runTests). Package-only; outputs are generated, not stored files.
// All records are design-study: illustrative design values, never real fact.
"use strict";
const crypto = require("crypto");

const SLUG = "distributed-intelligence-signature";
const RECORD_KIND = "distributed intelligence record";
const ID_PREFIX = "JAH-DISTIS-";
const AI_NAME = "JAH Distributed Intelligence Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  { title: "Signature Distributed Intelligence Overview Design",
    subject: "Distributed intelligence overview (Signature design-study)",
    description: "Design-study: Distributed intelligence spreads thinking across many connected machines and agents that share work, share knowledge, and coordinate decisions. Instead of one central computer doin",
    figures: { agents: 512, sites: 16, messages_per_s: 100000, decisions_per_s: 5000, knowledge_records: 1000000, uptime_percent: 99, latency_ms: 50, tasks_per_day: 20000 } },
  { title: "Signature Distributed Fundamentals Design",
    subject: "Distributed systems fundamentals (Signature design-study)",
    description: "Design-study: A distributed system is a set of processes on different machines that communicate only by sending messages, with no shared memory and no single clock. Each machine's clock can drif",
    figures: { processes: 1024, messages_per_s: 100000, clock_skew_ms: 10, partitions_per_year: 4, timeouts_s: 5, retries: 3, ordering_guarantees: 2, protocols: 8 } },
  { title: "Signature Consensus Lab Design",
    subject: "Consensus protocols (Signature design-study)",
    description: "Design-study: Consensus is the problem of getting a group of machines to agree on one value or one order of events even when some machines fail. Raft and Paxos are the two best-known families of",
    figures: { nodes: 7, quorum: 4, elections_per_year: 12, entries_per_s: 2000, leader_failures: 6, commit_latency_ms: 20, log_entries: 1000000, terms: 48 } },
  { title: "Signature Distributed Database Design",
    subject: "Distributed databases (Signature design-study)",
    description: "Design-study: A distributed database stores copies, called replicas, of its data on several machines, so that a read can be served from the nearest copy and the loss of one machine loses no data",
    figures: { replicas: 3, records: 100000000, reads_per_s: 50000, writes_per_s: 10000, replication_lag_ms: 100, partitions: 256, consistency_levels: 3, backups_per_day: 2 } },
  { title: "Signature Federated Learning Studio Design",
    subject: "Federated learning (Signature design-study)",
    description: "Design-study: Federated learning trains one shared model across many participants, such as hospitals or phones, without any participant sending its raw data away. Each participant trains on its ",
    figures: { participants: 100, rounds: 50, model_mb: 400, updates_per_round: 100, accuracy_percent: 92, dropouts_per_round: 5, privacy_budget: 4, aggregation_s: 60 } },
  { title: "Signature Edge Node Design",
    subject: "Edge computing (Signature design-study)",
    description: "Design-study: Edge computing moves computation to the edge of the network, close to where data is produced, such as a sensor, a camera, or a machine on a factory floor. A decision that must happ",
    figures: { edge_nodes: 256, latency_ms: 10, bandwidth_mbps: 1000, models_per_node: 4, offline_hours: 72, sync_interval_min: 15, power_watts: 25, sites: 32 } },
  { title: "Signature Agent Council Design",
    subject: "Multi-agent coordination (Signature design-study)",
    description: "Design-study: Multi-agent coordination is the problem of many software agents, each with its own goals and knowledge, working together on shared tasks without a single boss. Agents negotiate, wh",
    figures: { agents: 512, tasks_per_day: 20000, negotiations_per_day: 1000, conflicts_per_day: 40, resolution_s: 30, shared_goals: 12, roles: 16, messages_per_s: 100000 } },
  { title: "Signature Message Bus Design",
    subject: "Publish-subscribe messaging (Signature design-study)",
    description: "Design-study: Publish-subscribe messaging lets senders, called publishers, send messages to named topics without knowing who will read them, while receivers, called subscribers, listen only to t",
    figures: { topics: 200, subscribers: 2048, messages_per_s: 100000, delivery_ms: 20, retention_h: 72, partitions_per_topic: 16, replay_days: 7, dead_letters_per_day: 10 } },
]

const SOURCES = [
  { name: "Wikipedia - Distributed computing", url: "https://en.wikipedia.org/wiki/Distributed_computing", establishes: "Public background for this subject." },
  { name: "Wikipedia - Multi-agent system", url: "https://en.wikipedia.org/wiki/Multi-agent_system", establishes: "Public background for this subject." },
]

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
  const label = "distributed-intelligence-signature-design";
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
    description: topic.description + " Design-study: all model values are illustrative design values, never presented as real fact. DARPA-grade means engineering targets modeled on public standards; it is never a claim of DARPA approval, certification, funding, or endorsement.",
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One distributed intelligence record: a single subject with its full specification, demo, and evidence ladder.", A2: "The whole distributed intelligence database: 24 public records and 24 Signature design-study records covering the subject.", A3: "The distributed intelligence database against the network: linked to its sibling edition and to the adjacent live databases." },
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
  t("slug single -signature form", a.slug === SLUG && (a.slug.match(/-signature/g) || []).length === 1);
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
