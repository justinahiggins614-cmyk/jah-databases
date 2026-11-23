// Seeded boundless generator for the High-Performance Computing Database database
// (Signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-high-performance-computing-signature.js [seed]
// (prints one JSON record) or: node gen-high-performance-computing-signature.js
// --test (runTests). Package-only; outputs are generated, not stored files.
// All records are design-study: illustrative design values, never real fact.
"use strict";
const crypto = require("crypto");

const SLUG = "high-performance-computing-signature";
const RECORD_KIND = "high performance computing record";
const ID_PREFIX = "JAH-HPCS-";
const AI_NAME = "JAH High Performance Computing Librarian (Signature)";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  { title: "Signature High-Performance Computing Overview Design",
    subject: "High-performance computing overview (Signature design-study)",
    description: "Design-study: A high-performance computing system joins hundreds or thousands of compute nodes, each holding many processor cores, with a fast interconnect network, parallel storage, and a sched",
    figures: { compute_nodes: 1024, cores_per_node: 64, total_cores: 65536, interconnect_gbps: 200, storage_petabytes: 10, jobs_per_day: 480, power_megawatts: 12, uptime_percent: 99 } },
  { title: "Signature Supercomputer Node Design",
    subject: "Supercomputer architecture (Signature design-study)",
    description: "Design-study: A supercomputer is a machine built from many identical compute nodes, each a small computer with its own processors and memory, wired together by a fast network called an interconn",
    figures: { nodes: 1024, cores_per_node: 64, memory_gb_per_node: 256, interconnect_gbps: 200, latency_microseconds: 2, racks: 32, nodes_per_rack: 32, switches: 64 } },
  { title: "Signature Parallel Model Design",
    subject: "Parallel computing models (Signature design-study)",
    description: "Design-study: Parallel computing splits one problem into pieces that run at the same time. In the shared-memory model, threads inside one node read and write the same memory. In the distributed-",
    figures: { models: 3, cores_per_node: 64, nodes: 1024, threads_per_core: 2, messages_per_step: 4096, steps: 1000, speedup_target: 512, efficiency_percent: 50 } },
  { title: "Signature MPI Library Design",
    subject: "Message Passing Interface standard (Signature design-study)",
    description: "Design-study: The Message Passing Interface, shortened to MPI, is the standard way for processes on different computers to exchange data by sending and receiving messages. Each process is called",
    figures: { mpi_version: 4, collectives: 12, point_to_point: 6, ranks: 4096, messages_per_rank: 256, max_message_mb: 64, implementations: 3, test_programs: 18 } },
  { title: "Signature OpenMP Runtime Design",
    subject: "OpenMP shared-memory parallelism (Signature design-study)",
    description: "Design-study: OpenMP is a set of compiler directives, which are short annotations added to ordinary code, that tell the compiler to split loops and regions across the threads of one node. Thread",
    figures: { threads: 64, cores_per_node: 64, directives: 24, loops_parallel: 40, reductions: 8, barriers: 12, schedules: 3, test_programs: 14 } },
  { title: "Signature Graphics Processing Unit Pod Design",
    subject: "Graphics processing unit acceleration (Signature design-study)",
    description: "Design-study: A graphics processing unit, shortened to GPU, is a chip built with thousands of small cores that all run the same operation on different data at once. That shape suits problems whe",
    figures: { gpus_per_node: 4, gpu_memory_gb: 80, gpu_bandwidth_gbps: 2000, nodes_with_gpu: 256, total_gpus: 1024, speedup_vs_cpu: 12, kernels: 30, power_watts_per_gpu: 400 } },
  { title: "Signature Interconnect Fabric Design",
    subject: "Cluster interconnects (Signature design-study)",
    description: "Design-study: The interconnect is the network that joins the nodes of a cluster. Its two numbers that matter most are bandwidth, how much data it moves per second, and latency, how long one smal",
    figures: { links_gbps: 200, latency_microseconds: 2, switches: 64, ports_per_switch: 64, bisection_tb_per_s: 25, redundant_paths: 2, cables: 8192, error_rate: 1 } },
  { title: "Signature Parallel Storage Tier Design",
    subject: "Parallel file systems (Signature design-study)",
    description: "Design-study: A parallel file system spreads one file across many storage servers so that many compute nodes can read and write different parts of it at the same time. Without it, a thousand nod",
    figures: { storage_petabytes: 10, write_gbps: 500, read_gbps: 600, metadata_ops_per_s: 100000, storage_servers: 48, disks: 960, replication: 2, snapshots_per_day: 4 } },
]

const SOURCES = [
  { name: "Wikipedia - High-performance computing", url: "https://en.wikipedia.org/wiki/High-performance_computing", establishes: "Public background for this subject." },
  { name: "Wikipedia - Supercomputer", url: "https://en.wikipedia.org/wiki/Supercomputer", establishes: "Public background for this subject." },
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
  const label = "high-performance-computing-signature-design";
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
    scales: { A1: "One high-performance computing (HPC) record: a single subject with its full specification, demo, and evidence ladder.", A2: "The whole high-performance computing (HPC) database: 24 public records and 24 Signature design-study records covering the subject.", A3: "The high-performance computing (HPC) database against the network: linked to its sibling edition and to the adjacent live databases." },
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
