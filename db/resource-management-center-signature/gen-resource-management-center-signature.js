// Seeded boundless generator for the resource-management-center-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-resource-management-center-signature.js [seed]  (prints one
// JSON record) or: node gen-resource-management-center-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
// Attribution: this system was proposed in another AI's review pasted
// 2026-11-18; source unconfirmed, NOT Manon's words.
"use strict";
const crypto = require("crypto");

const SLUG = "resource-management-center-signature";
const RECORD_KIND = "resource management center record";
const ID_PREFIX = "JAH-RMCS-";
const AI_NAME = "JAH Resource Management Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated-completion";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const DISCLAIMER = " Generated content is never presented as an authentic public record; Signature records are design studies, never established fact.";

const TOPICS = [{"title": "Resource Management Center: Overview and Mission", "subject": "Resource Management Center overview", "description": "Signature design study: The Resource Management Center is the network's steward of scarce things: processor time, memory, storage, network use, and the queues that hold waiting work. The center holds schedules, quotas, budgets, and execution histories as records; it is not itself a live scheduler running jobs. Its rule is plain: every job gets what it needs and no more, every limit is written down, and every overrun is recorded.", "figures": {"resources_tracked": 5, "queues": 4, "quotas_written": 24, "overruns_logged": 3}, "label": "resource-management-center-01"}, {"title": "Resource Management Center: Compute Scheduling", "subject": "Sharing processor time fairly", "description": "Signature design study: Compute scheduling decides which job uses the processor next, and for how long, so no single job can starve the rest. A CPU (Central Processing Unit) is the part of a computer that runs instructions; scheduling is the timetable that shares it. The center records the scheduling rule, the queue order, and the wait time each job actually saw.", "figures": {"jobs_scheduled": 120, "median_wait_seconds": 8, "starved_jobs": 0, "rules_written": 3}, "label": "resource-management-center-02"}, {"title": "Resource Management Center: Memory Management", "subject": "Sharing memory without running out", "description": "Signature design study: Memory management tracks how much working memory each job uses, sets a ceiling per job, and refuses or pauses a job that would exceed it. Memory here means RAM (Random Access Memory), the fast working space a program uses while it runs. The center records the ceiling, the peak use, and every job that hit its ceiling.", "figures": {"jobs_measured": 96, "ceiling_mb": 512, "peak_mb": 488, "ceiling_hits": 2}, "label": "resource-management-center-03"}, {"title": "Resource Management Center: Storage Quotas and Capacity", "subject": "How much disk each database may hold", "description": "Signature design study: A storage quota is the written limit on how much disk space one database or job may use, and capacity is the total space available to share. The center watches use against quota and warns before the limit is hit, because a full disk stops everything at once. Quotas are set from measured need, not from guesses, and the measurements are filed with the quota.", "figures": {"databases_measured": 24, "quota_gb": 2, "peak_use_gb": 1, "warnings_sent": 1}, "label": "resource-management-center-04"}, {"title": "Resource Management Center: Network Bandwidth Management", "subject": "Sharing the network pipe", "description": "Signature design study: Bandwidth management shares the network's carrying capacity between jobs, so one large download cannot choke the rest of the network. Bandwidth is measured in bits per second; the center records the share each job was given and the share it actually used. Jobs that need the network state their need in advance, and the center schedules them instead of letting them fight.", "figures": {"jobs_sharing": 12, "capacity_mbps": 100, "peak_use_mbps": 78, "choked_jobs": 0}, "label": "resource-management-center-05"}, {"title": "Resource Management Center: Work Queues and Job Scheduling", "subject": "Orderly lines for waiting work", "description": "Signature design study: A work queue is an orderly line of jobs waiting their turn, each with its place, its priority, and its stated needs. Job scheduling takes jobs from the queue in a stated order, starts them when resources are free, and records the start and finish of each. The center keeps the queue visible, so a job that waits too long is seen, not forgotten.", "figures": {"queues": 4, "jobs_queued": 240, "jobs_finished": 238, "jobs_waiting": 2}, "label": "resource-management-center-06"}, {"title": "Resource Management Center: Concurrency Limits", "subject": "How many things may run at once", "description": "Signature design study: A concurrency limit is the written maximum number of jobs that may run at the same time, set so the machine stays responsive. Running too many jobs at once slows all of them and can exhaust memory; the limit is chosen from measurement, not from hope. The center records the limit, the peak number running, and every time the limit was reached.", "figures": {"limit": 4, "peak_running": 4, "times_at_limit": 9, "overloads": 0}, "label": "resource-management-center-07"}, {"title": "Resource Management Center: Throttling and Rate Limits", "subject": "Slowing work down on purpose to protect the host", "description": "Signature design study: Throttling slows work down on purpose, and a rate limit is the written maximum rate, for example at most one hundred operations per call. Generators in this network throttle themselves so they never overload the host or burn through usage; the center records each throttle setting. A job that is throttled is not failing: it is waiting its turn, and the wait is logged.", "figures": {"rate_per_call": 100, "throttled_calls": 18, "waits_logged": 18, "host_overloads": 0}, "label": "resource-management-center-08"}];

const SOURCES = [{"name": "Kubernetes documentation \u2014 scheduling, resource requests and limits", "url": "https://kubernetes.io/docs/home/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "Prometheus documentation \u2014 monitoring and metering", "url": "https://prometheus.io/docs/introduction/overview/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "Internet Engineering Task Force (IETF) \u2014 RFC (Request for Comments) editor, network standards", "url": "https://www.rfc-editor.org/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "National Institute of Standards and Technology (NIST) \u2014 cloud and resource guidance", "url": "https://www.nist.gov/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}];

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
  const count = keys.length;
  const mean = (total / count).toFixed(1);
  const out = { count: count, label: label, max: Math.max(...keys.map((k) => figs[k])), mean: mean, min: Math.min(...keys.map((k) => figs[k])), total: total };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "from decimal import Decimal, ROUND_HALF_UP\n" +
    "total = sum(FIGURES.values())\n" +
    "count = len(FIGURES)\n" +
    "mean = str((Decimal(total) / Decimal(count)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))\n" +
    "mn = min(FIGURES.values())\n" +
    "mx = max(FIGURES.values())\n" +
    "print('count: %d' % count)\n" +
    "print('label: %s' % LABEL)\n" +
    "print('max: %d' % mx)\n" +
    "print('mean: %s' % mean)\n" +
    "print('min: %d' % mn)\n" +
    "print('total: %d' % total)\n" +
    "result = 'count=%d|label=%s|max=%d|mean=%s|min=%d|total=%d' % (count, LABEL, mx, mean, mn, total)\n" +
    "print('Result: %s' % result)\n" +
    "print('Run 1 SHA-256: %s' % hashlib.sha256(result.encode()).hexdigest())\n";
  const expected = Object.keys(out).sort().map((k) => k + ": " + out[k]).join("\n") + "\n" +
    "Result: " + result + "\n" +
    "Run 1 SHA-256: " + h + "\n";
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
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + " No claim of a proven breakthrough, of flight readiness, or of deployment readiness is established by this generated record." + DISCLAIMER,
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record on this topic.", A2: "The pair: generated records extend the 24 filed records.", A3: "The network: every database a knowledge source, every generator a tool." },
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
