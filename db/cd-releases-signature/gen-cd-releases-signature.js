'use strict';
// Boundless generator — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["harbor-lights-marina-vale-cd-release-record", "copper-lantern-road-the-copper-lanterns-cd-release-record", "paper-kites-over-june-juno-park-cd-release-record", "the-saltwater-choir-the-saltwater-choir-cd-release-record", "maple-and-iron-sable-rivers-cd-release-record", "night-train-to-aldergrove-kite-and-anchor-cd-release-record", "glasshouse-summer-petra-lind-cd-release-record", "the-cartographer-s-daughter-wren-halden-cd-release-record", "emberfield-the-emberfield-band-cd-release-record", "letters-never-sent-ana-corso-cd-release-record", "the-winter-orchard-falk-neruda-cd-release-record", "radio-starling-the-starlings-cd-release-record", "stonebridge-hymnal-cora-venn-cd-release-record", "the-long-afternoon-milo-thatch-cd-release-record", "velvet-meridian-ines-marlowe-cd-release-record", "a-thousand-small-doors-the-doorwrights-cd-release-record"];
var RECORD_KIND = 'cd release record';
var SLUG = 'cd-releases-signature';
var PREFIX = 'JAH-CDRLS-';
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
    title: 'Generated cd release record entry: ' + topic,
    body: 'Generated cd release record entry for ' + topic + '. '
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
