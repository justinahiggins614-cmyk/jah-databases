'use strict';
// Boundless generator for urgent-vs-routine-care-guide-signature — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var AREAS = ["emergency-care-now-framework", "urgent-same-day-care-framework", "routine-appointment-framework", "self-care-and-watch-framework", "how-the-care-settings-differ", "worked-examples:-red-flag-and-comfort-split", "when-in-doubt,-seek-urgent-care", "what-to-bring-to-each-setting", "after-hours-general-guidance", "follow-up-after-urgent-care", "follow-up-after-routine-care", "watching-and-waiting-safely", "children-and-adult-setting-notes", "cost-and-time-general-considerations", "common-setting-mistakes", "combining-settings-over-an-episode-and-preparing-questions"];
var RECORD_KIND = 'care setting guide record';
var SLUG = 'urgent-vs-routine-care-guide-signature';
var PREFIX = 'JAH-UVRS-';
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
    title: 'Generated care setting guide record: ' + area,
    body: 'Generated Signature care-setting guide entry for ' + area + '. Signature-original teaching design, general education only; it does not tell you which setting you need for your own symptoms. See a clinician.'};
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
