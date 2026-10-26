// gen-stop-hpv-signature.js -- boundless generator for the Stop HPV Signature Database.
// Usage: node gen-stop-hpv-signature.js --n 5
// Deterministic seeded LCG; throttled; duplicate-checked; hard cap 10^15 records
// or stop when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records. Generated records are labelled generated.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["HPV Vaccination: Who, When, and How Many Doses", "Vaccination Catch-Up: Starting or Finishing Later", "Screening With Pap and HPV Tests: What Happens and How Often", "Screening After Vaccination: Why It Is Still Needed", "Safer Sex: Reducing HPV Transmission Risk", "Smoking Cessation: Why Quitting Helps Against Persistent HPV", "HPV Education: Knowing What HPV Is and Is Not", "Partner Communication: Talking Honestly About HPV", "Cryotherapy: Clinician Freezing Treatment for Warts", "Clinician-Prescribed Topical Treatments for Warts", "Excision Procedures: Surgical Removal by a Clinician", "Electrocautery: Heat-Based Clinician Removal", "Laser Removal: Clinician Laser Treatment for Warts", "What to Expect During and After a Wart-Removal Visit", "Aftercare at Home After Clinician Wart Treatment", "Recurrence and Follow-Up Monitoring After Wart Removal"];
const VARIANTS = ["checklist variation", "tracker variation", "questions variation", "calendar variation", "log variation"];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
  }
  return 5;
}
let seed = 20261026;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}
const seen = new Set();
function makeRecord(k) {
  const topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
  const variant = VARIANTS[Math.floor(rnd() * VARIANTS.length)];
  const key = topic + "#" + variant;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-SHSG-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "stop-hpv-signature",
    title: "Generated " + topic + " (" + variant + ")",
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "hpv prevention and removal record",
    feasibility_tier: "buildable-now",
    note: "Deterministic generated variation (" + key + ") over the 16 seed records. Labelled generated; not an assistant-built record. Educational only; see a clinician for personal advice."
  };
}
function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  const space = TOPICS.length * VARIANTS.length;
  let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 20 && seen.size < space) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  console.error("emitted " + emitted + " of " + n + "; variation space " + space);
}
main();
