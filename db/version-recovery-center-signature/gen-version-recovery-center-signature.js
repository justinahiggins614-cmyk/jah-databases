// Seeded boundless generator for the version-recovery-center-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-version-recovery-center-signature.js [seed]  (prints one
// JSON record) or: node gen-version-recovery-center-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
// Attribution: this system was proposed in another AI's review pasted
// 2026-11-18; source unconfirmed, NOT Manon's words.
"use strict";
const crypto = require("crypto");

const SLUG = "version-recovery-center-signature";
const RECORD_KIND = "version and recovery center record";
const ID_PREFIX = "JAH-VRCS-";
const AI_NAME = "JAH Version and Recovery Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated-completion";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const DISCLAIMER = " Generated content is never presented as an authentic public record; Signature records are design studies, never established fact.";

const TOPICS = [{"title": "Version and Recovery Center: Overview and Mission", "subject": "Version and Recovery Center overview", "description": "Signature design study: The Version and Recovery Center is the network's memory and safety net: it keeps every version of every record and file, and it can bring back what was lost or broken. The center holds version records, snapshots, backups, and recovery reports as records; it is not itself a live backup service. Two promises sit at the front of the center: nothing is ever silently overwritten, and every recovery is rehearsed before it is needed.", "figures": {"versions_kept": 24, "snapshots": 12, "backups": 6, "rehearsals": 4}, "label": "version-recovery-center-01"}, {"title": "Version and Recovery Center: Version Control", "subject": "Keeping every change with its author and reason", "description": "Signature design study: Version control records every change as a version: what changed, who changed it, when, and why, so any earlier state can be found again. A version is a saved snapshot of a file at one moment; the history of versions is the story of how the file grew. The center records versions for databases and files alike, and never rewrites history to hide a mistake.", "figures": {"versions": 120, "authors": 3, "changes_logged": 120, "history_rewrites": 0}, "label": "version-recovery-center-02"}, {"title": "Version and Recovery Center: Snapshots and Checkpoints", "subject": "Frozen moments you can return to", "description": "Signature design study: A snapshot is a frozen copy of a whole database or file at one moment, taken so the work can return to exactly that moment later. A checkpoint is a snapshot taken at a known-good moment, for example right after a verified merge, so recovery starts from solid ground. Snapshots are labelled with the date, the contents, and the reason they were taken, and the label is part of the record.", "figures": {"snapshots_taken": 12, "checkpoints": 4, "labels_complete": 12, "restores_from_snapshot": 2}, "label": "version-recovery-center-03"}, {"title": "Version and Recovery Center: Backups, Full, Incremental, Differential", "subject": "Copies that survive the original being lost", "description": "Signature design study: A full backup copies everything; an incremental backup copies only what changed since the last backup; a differential backup copies what changed since the last full backup. The center records which kind each backup is, when it was taken, and what it covers, so a restore can be planned instead of guessed. A backup that has never been tested by restoring from it is treated as unproven, not as protection.", "figures": {"full_backups": 2, "incremental_backups": 10, "differential_backups": 4, "untested_backups": 0}, "label": "version-recovery-center-04"}, {"title": "Version and Recovery Center: Restore and Rollback", "subject": "Bringing back the earlier version", "description": "Signature design study: A restore brings back a saved copy; a rollback moves a live database back to an earlier version after a bad change. Every restore in the center is logged with what was restored, from which backup, by whom, and whether the result was verified afterwards. Rollback is a last resort with a written reason, because it also undoes the good changes made after the bad one.", "figures": {"restores_done": 3, "rollbacks_done": 1, "verified_after": 4, "unlogged_restores": 0}, "label": "version-recovery-center-05"}, {"title": "Version and Recovery Center: Disaster Recovery Planning", "subject": "A written plan for the worst day", "description": "Signature design study: A disaster recovery plan is a written plan for the worst day: what is lost, what is restored first, who decides, and how long each step takes. The plan names the order of recovery, because restoring the least important thing first wastes the time the important things need. The plan is rehearsed, timed, and rewritten after every rehearsal, because an unrehearsed plan is a guess.", "figures": {"plan_steps": 9, "rehearsals": 2, "rehearsal_minutes": 45, "plan_rewrites": 1}, "label": "version-recovery-center-06"}, {"title": "Version and Recovery Center: Change History and Audit Trail", "subject": "Who did what, when, in order", "description": "Signature design study: An audit trail is the ordered list of every change, read, and administrative action, kept so that any event can be traced back. The trail records the actor, the action, the target, and the time, and it cannot be edited after the fact without leaving a mark. Audit trails in this center cover changes, executions, failures, and administrative actions, as the review asked for.", "figures": {"events_logged": 1500, "edits_after_fact": 0, "actions_covered": 6, "gaps_found": 0}, "label": "version-recovery-center-07"}, {"title": "Version and Recovery Center: Branching and Merging", "subject": "Trying a change without breaking the main line", "description": "Signature design study: A branch is a separate line of work that leaves the main line untouched, so a change can be tried, tested, and only then merged back. Merging brings a branch back into the main line; a merge conflict is when both lines changed the same part, and a human decides the outcome. The center records every branch, its purpose, and its merge result, so no experiment is lost and no merge is a mystery.", "figures": {"branches": 8, "merges_done": 6, "conflicts": 2, "conflicts_resolved": 2}, "label": "version-recovery-center-08"}];

const SOURCES = [{"name": "Git documentation \u2014 version control concepts and commands", "url": "https://git-scm.com/doc", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "PostgreSQL documentation \u2014 backup and restore", "url": "https://www.postgresql.org/docs/current/backup.html", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "SQLite \u2014 backup API and file format", "url": "https://www.sqlite.org/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}, {"name": "National Institute of Standards and Technology (NIST) \u2014 data integrity and contingency planning", "url": "https://www.nist.gov/", "establishes": "Source for generated records in this edition.", "retrieved": "2026-11-18", "status": 200}];

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
