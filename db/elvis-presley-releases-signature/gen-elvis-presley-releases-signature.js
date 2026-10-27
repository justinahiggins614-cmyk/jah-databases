'use strict';
// Boundless generator for elvis-presley-releases-signature — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["the-memphis-call", "danny", "a-southern-christmas", "danny-is-back", "his-hand-in-song", "something-for-everyone", "pot-luck-supper", "danny-for-everyone", "how-great-the-morning", "from-danny-in-memphis", "danny-country-i-m-ten-thousand-years-old", "love-letters-from-danny", "danny-now", "raised-on-rhythm-for-old-times-sake", "promised-river", "moody-sky"];
var RECORD_KIND = 'elvis release record';
var SLUG = 'elvis-presley-releases-signature';
var PREFIX = 'JAH-ELVPS-';
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
    title: 'Generated elvis release record entry: ' + topic,
    body: 'Generated elvis release record entry for ' + topic + '. Free forever; no payments, no upsells.'};
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
