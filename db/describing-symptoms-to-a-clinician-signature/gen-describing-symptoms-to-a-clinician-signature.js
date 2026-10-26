'use strict';
// Boundless generator for describing-symptoms-to-a-clinician-signature — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var AREAS = ["shoulder-pain", "foot-pain", "foot-numbness-and-tingling", "hearing-loss", "taste-changes", "swallowing-difficulty", "balance-problems", "knee-joint-pain", "hand-and-wrist-joint-pain", "chest-pain", "arm-and-leg-numbness", "stiffness-and-soreness", "lower-back-ache", "neck-and-upper-back-ache", "muscle-soreness-after-activity", "general-everyday-aches"];
var RECORD_KIND = 'symptom description record';
var SLUG = 'describing-symptoms-to-a-clinician-signature';
var PREFIX = 'JAH-DESCS-';
function seeded(seed) {
  var s = 0;
  for (var i = 0; i < seed.length; i++) { s = (s * 31 + seed.charCodeAt(i)) >>> 0; }
  s ^= (s << 13) >>> 0; s ^= s >>> 17; s ^= (s << 5) >>> 0; s >>>= 0;
  for (var w = 0; w < 8; w++) { s = (s * 1664525 + 1013904223) >>> 0; }
  return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; };
}
function genOne(seed) {
  var rnd = seeded(String(seed));
  var area = AREAS[Math.floor(rnd() * AREAS.length)];
  return {id: PREFIX + 'GEN-' + String(seed).padStart(6, '0'), slug: SLUG,
    record_kind: RECORD_KIND, topic_area: area, src: 'generated',
    title: 'Generated symptom description record: ' + area,
    body: 'Generated Signature symptom-description entry for ' + area + '. Signature-original teaching design, general education only, never a diagnosis and never a prescription. See a clinician for new, worsening, or unexplained symptoms.'};
}
function main() {
  var n = 3;
  for (var i = 2; i < process.argv.length; i++) {
    if (process.argv[i] === '--n' && process.argv[i + 1]) n = parseInt(process.argv[i + 1], 10);
  }
  if (!isFinite(n) || n < 0 || n > 1e15) { console.error('bad --n'); process.exit(1); }
  for (var k = 1; k <= n; k++) console.log(JSON.stringify(genOne(k)));
}
if (require.main === module) main();
module.exports = {genOne: genOne};
