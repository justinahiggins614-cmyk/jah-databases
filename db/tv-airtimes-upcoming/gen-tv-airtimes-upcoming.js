'use strict';
// Boundless generator for tv-airtimes-upcoming — deterministic, seeded, throttled.
// Hard cap: 1e15 records (one quadrillion), or stop when genuinely complete.
// Generated records carry src "generated" and are never mixed with assistant-built records.
var TOPICS = ["st.-denis-medical", "the-fall-and-rise-of-reggie-dinkins", "bass-x-machina", "the-greatest", "alls-fair", "stick", "black-doves", "mistletoe-murders", "it-gets-worse", "the-good-daughter", "the-empress", "kids-choice-awards", "the-chosen", "he-said,-she-said", "yellowjackets", "blade-runner-2099"];
var RECORD_KIND = 'tv airtime upcoming record';
var SLUG = 'tv-airtimes-upcoming';
var PREFIX = 'JAH-TVAU-';
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
    title: 'Generated tv airtime upcoming record entry: ' + topic,
    body: 'Generated tv airtime upcoming record entry for ' + topic + '. Program titles, dates, and factual credits only; all descriptions original.'};
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
