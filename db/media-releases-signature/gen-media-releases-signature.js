'use strict';
// Boundless generator — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["the-media-releases-suite-framework-signature-edition-media-r", "harbor-lights-by-marina-vale-media-release-record", "copper-lantern-road-by-the-copper-lanterns-media-release-rec", "lantern-on-the-water-by-marina-vale-media-release-record", "kite-season-by-juno-park-media-release-record", "maple-and-iron-by-sable-rivers-media-release-record", "the-winter-orchard-by-falk-neruda-media-release-record", "night-train-to-aldergrove-by-kite-and-anchor-media-release-r", "letters-never-sent-by-ana-corso-media-release-record", "choir-of-the-tide-by-the-saltwater-choir-media-release-recor", "the-mapmaker-s-song-by-wren-halden-media-release-record", "the-emberfield-picture-by-the-emberfield-band-media-release-", "stonebridge-chapel-by-cora-venn-media-release-record", "the-starling-broadcast-by-the-starlings-media-release-record", "velvet-meridian-by-ines-marlowe-media-release-record", "the-thousandth-door-by-the-doorwrights-media-release-record"];
var RECORD_KIND = 'media release record';
var SLUG = 'media-releases-signature';
var PREFIX = 'JAH-MRELS-';
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
