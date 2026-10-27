'use strict';
// Boundless generator for tape-releases-signature — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["tape-deck-confessions", "side-a-side-b", "the-workshop-tapes", "chrome-and-rust", "ninety-minutes-to-midnight", "the-ferry-tape", "dust-on-the-heads", "songs-for-a-long-drive", "the-attic-sessions", "rewind-repeat", "kitchen-radio", "a-walkman-winter", "the-copy-shop", "mixtape-for-a-stranger", "static-bloom", "the-last-cassette"];
var RECORD_KIND = 'tape release record';
var SLUG = 'tape-releases-signature';
var PREFIX = 'JAH-TAPES-';
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
    title: 'Generated tape release record entry: ' + topic,
    body: 'Generated tape release record entry for ' + topic + '. General reference '
      + 'information only, drawn from this database\'s own schema. No song '
      + 'words, audio, artwork, or verbatim articles are reproduced.'};
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
