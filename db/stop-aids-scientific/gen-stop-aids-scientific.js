// Boundless generator for stop-aids-scientific (Stop AIDS Scientific Database).
// Seeded and deterministic. Throttled, duplicate-checked, self-regulating.
// Hard cap: 1e15 (one quadrillion) records, or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
const HARD_CAP = 1e15;
const SLUG = "stop-aids-scientific";
const ID_PREFIX = "JAH-SAIS-GEN-";
const RECORD_KIND = "hiv aids prevention record";
const EDITION = "scientific";
const TOPICS = ["Pre-Exposure Prophylaxis (PrEP)", "Post-Exposure Prophylaxis (PEP)", "Condoms", "Regular HIV Testing", "Treatment as Prevention and U=U", "Needle and Syringe Safety and Harm-Reduction Services", "Prevention of Mother-to-Child Transmission", "Partner Services and Notification", "Education and Stigma Reduction", "Safer-Sex Communication", "Voluntary Medical Male Circumcision", "Lubricant Safety with Condoms", "Testing Frequency Guidance", "Linkage to Care After a Positive Result", "PrEP Adherence Support", "Community Outreach Programs"];
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
  const variant = 1 + Math.floor(rnd() * 50);
  const key = topic + "#v" + variant;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: ID_PREFIX + String(k + 1).padStart(6, "0"),
    slug: SLUG,
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: EDITION,
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: RECORD_KIND,
    feasibility_tier: "research-stage",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record. Educational only; never a diagnosis, never a prescription."
  };
}
function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  const space = TOPICS.length * 50;
  let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 20 && seen.size < space) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  console.error("emitted " + emitted + " generated records for " + SLUG);
}
main();
