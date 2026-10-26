'use strict';
// Boundless generator for everyday-headaches — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var AREAS = ["tension", "dehydration", "screen-strain", "sleep-related", "stress", "posture", "hunger", "caffeine", "sinus", "heat", "noise", "eye-strain", "weekend", "exercise", "cold-stimulus", "menstrual"];
var RECORD_KIND = "ways to help record";
var SLUG = "everyday-headaches";
var PREFIX = "JAH-EHD-";
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
    record_kind: RECORD_KIND, topic: area, src: 'generated',
    title: 'Generated entry: ' + area,
    body: 'Generated entry for ' + area + '. General information only, '
      + 'never a diagnosis and never a prescription. See a clinician for new, worsening, '
      + 'or unexplained symptoms. Follow package directions for any over-the-counter product.'};
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
