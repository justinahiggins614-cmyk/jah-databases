'use strict';
// Boundless generator for beatles-releases-signature — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["harbour-lights-at-dawn", "four-lads-from-the-docks", "a-day-at-the-seaside", "winter-windows", "help-is-on-the-way", "leather-and-lace", "turn-the-dial", "the-sergeant-s-brass-band", "mystery-coach-tour", "the-plain-white-sleeve", "yellow-river-boat", "abbey-lane", "let-it-stand", "past-takes-volume-one", "past-takes-volume-two", "1962-1966-the-lantern-years"];
var RECORD_KIND = 'beatles release record';
var SLUG = 'beatles-releases-signature';
var PREFIX = 'JAH-BTLSS-';
function seeded(seed) {
  var s = 0;
  for (var i = 0; i < seed.length; i++) { s = (s * 31 + seed.charCodeAt(i)) >>> 0; }
  s ^= (s << 13) >>> 0; s ^= s >>> 17; s ^= (s << 5) >>> 0; s >>>= 0;
  for (var w = 0; w < 8; w++) { s = (s * 1664525 + 1013904223) >>> 0; }
  return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; };
}
function genOne(seed) {
  var rnd = seeded(String(seed));
  var topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
  return {id: PREFIX + 'GEN-' + String(seed).padStart(6, '0'), slug: SLUG,
    record_kind: RECORD_KIND, topic: topic, src: 'generated',
    title: 'Generated beatles release record entry: ' + topic,
    body: 'Generated beatles release record entry for ' + topic + '. Free forever; no payments, no upsells.'};
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
