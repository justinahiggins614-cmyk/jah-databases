'use strict';
// Boundless generator — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["billie-jean-michael-jackson-track-release-record", "hey-jude-the-beatles-track-release-record", "bohemian-rhapsody-queen-track-release-record", "like-a-rolling-stone-bob-dylan-track-release-record", "i-will-always-love-you-whitney-houston-track-release-record", "smells-like-teen-spirit-nirvana-track-release-record", "imagine-john-lennon-track-release-record", "yesterday-the-beatles-track-release-record", "beat-it-michael-jackson-track-release-record", "with-or-without-you-u2-track-release-record", "dancing-in-the-dark-bruce-springsteen-track-release-record", "rolling-in-the-deep-adele-track-release-record", "someone-like-you-adele-track-release-record", "come-as-you-are-nirvana-track-release-record", "lithium-nirvana-track-release-record", "in-bloom-nirvana-track-release-record"];
var RECORD_KIND = 'track release record';
var SLUG = 'track-releases';
var PREFIX = 'JAH-TRKR-';
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
    title: 'Generated track release record entry: ' + topic,
    body: 'Generated track release record entry for ' + topic + '. '
      + 'Titles, dates, and factual credits only; no lyrics, audio, artwork, or verbatim articles are reproduced.'};
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
