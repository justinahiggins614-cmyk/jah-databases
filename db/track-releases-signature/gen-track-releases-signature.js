'use strict';
// Boundless generator — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["lantern-on-the-water-marina-vale-track-release-record", "the-copper-road-song-the-copper-lanterns-track-release-recor", "kite-season-juno-park-track-release-record", "choir-of-the-tide-the-saltwater-choir-track-release-record", "maple-street-waltz-sable-rivers-track-release-record", "aldergrove-station-kite-and-anchor-track-release-record", "glasshouse-rain-petra-lind-track-release-record", "the-mapmaker-s-song-wren-halden-track-release-record", "emberfield-fair-the-emberfield-band-track-release-record", "the-unsent-letter-ana-corso-track-release-record", "first-frost-song-falk-neruda-track-release-record", "starling-radio-the-starlings-track-release-record", "bridge-chapel-bell-cora-venn-track-release-record", "afternoon-hour-milo-thatch-track-release-record", "meridian-night-ines-marlowe-track-release-record", "the-thousandth-door-the-doorwrights-track-release-record"];
var RECORD_KIND = 'track release record';
var SLUG = 'track-releases-signature';
var PREFIX = 'JAH-TRKRS-';
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
