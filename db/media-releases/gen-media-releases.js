'use strict';
// Boundless generator — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["the-media-releases-suite-framework-media-release-record", "brothers-in-arms-by-dire-straits-media-release-record", "thriller-by-michael-jackson-media-release-record", "billie-jean-by-michael-jackson-media-release-record", "bohemian-rhapsody-by-queen-media-release-record", "abbey-road-by-the-beatles-media-release-record", "the-dark-side-of-the-moon-by-pink-floyd-media-release-record", "born-in-the-u-s-a-by-bruce-springsteen-media-release-record", "jagged-little-pill-by-alanis-morissette-media-release-record", "i-will-always-love-you-by-whitney-houston-media-release-reco", "hey-jude-by-the-beatles-media-release-record", "purple-rain-the-film-media-release-record", "purple-rain-the-album-media-release-record", "tv-airtimes-how-this-suite-records-them-media-release-record", "nevermind-by-nirvana-media-release-record", "imagine-by-john-lennon-media-release-record"];
var RECORD_KIND = 'media release record';
var SLUG = 'media-releases';
var PREFIX = 'JAH-MREL-';
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
    title: 'Generated media release record entry: ' + topic,
    body: 'Generated media release record entry for ' + topic + '. '
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
