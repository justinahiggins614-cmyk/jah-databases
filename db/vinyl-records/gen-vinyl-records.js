'use strict';
// Boundless generator for vinyl-records — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["abbey-road", "the-dark-side-of-the-moon", "thriller", "rumours", "led-zeppelin-iv", "sgt-pepper-s-lonely-hearts-club-band", "the-wall", "a-night-at-the-opera", "nevermind", "kind-of-blue", "exile-on-main-st", "the-rise-and-fall-of-ziggy-stardust-and-the-spiders-from-mars", "highway-61-revisited", "pet-sounds", "purple-rain", "back-in-black"];
var RECORD_KIND = 'vinyl record record';
var SLUG = 'vinyl-records';
var PREFIX = 'JAH-VNYL-';
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
    title: 'Generated vinyl record record entry: ' + topic,
    body: 'Generated vinyl record record entry for ' + topic + '. General reference '
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
