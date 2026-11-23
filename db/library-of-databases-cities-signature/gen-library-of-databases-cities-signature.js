/* Generator for library-of-databases-cities-signature — Cities Books from the Databases, GEN_VERSION 1.
   Deterministic IDs: genId(seed) = <own id_prefix>GEN- + sha12(slug|version|seed).
   The id always starts with this shelf's own prefix; no generic GEN- prefix.
   Identical input -> identical id and identical content. GEN- namespace never
   collides with shipped numeric record ids. Registered with the shared JAHDB registry.
   Generator ceiling: up to 1,000,000,000 scales per file, generated on demand
   by the file AI — not stored files. */
(function (global) {
  'use strict';
  var SLUG = 'library-of-databases-cities-signature';
  var KIND = 'book from the databases record';
  var ID_PREFIX = 'JAH-LDBCS-';
  var GEN_VERSION = '1';
  var HARD_STOP = 1000000000;
  var TOPICS = ["Abu Dhabi: The Signature Abu Dhabi City Method", "Accra: The Signature Accra City Method", "Addis Ababa: The Signature Addis Ababa City Method", "Amman: The Signature Amman City Method", "Amsterdam: The Signature Amsterdam City Method", "Athens: The Signature Athens City Method", "Atlanta: The Signature Atlanta City Method", "Auckland: The Signature Auckland City Method", "Baghdad: The Signature Baghdad City Method", "Bangkok: The Signature Bangkok City Method", "Barcelona: The Signature Barcelona City Method", "Beijing: The Signature Beijing City Method", "Beirut: The Signature Beirut City Method", "Berlin: The Signature Berlin City Method", "Bogota: The Signature Bogota City Method", "Boston: The Signature Boston City Method"];

  function sha12(str) {
    var h1 = 0x811c9dc5, h2 = 0x01000193;
    for (var i = 0; i < str.length; i++) {
      var c = str.charCodeAt(i);
      h1 ^= c; h1 = Math.imul(h1, 0x01000193) >>> 0;
      h2 ^= c; h2 = Math.imul(h2, 0x85ebca6b) >>> 0;
    }
    function hex(n) { return ('00000000' + n.toString(16)).slice(-8); }
    return (hex(h1) + hex(h2)).slice(0, 12);
  }

  function genId(seed) {
    return ID_PREFIX + 'GEN-' + sha12(SLUG + '|' + GEN_VERSION + String(seed)).toUpperCase();
  }

  function topicFor(seed) {
    var h = 0;
    for (var i = 0; i < String(seed).length; i++) { h = (Math.imul(h, 31) + String(seed).charCodeAt(i)) >>> 0; }
    return TOPICS[h % TOPICS.length];
  }

  function generate(seed) {
    seed = (seed === undefined || seed === null || seed === '') ? 'default' : String(seed);
    return {
      id: genId(seed),
      slug: SLUG,
      record_kind: KIND,
      src: 'generated',
      seed: seed,
      generator_version: GEN_VERSION,
      title: 'Generated cities book on ' + topicFor(seed),
      demo_output: 'generated record ' + genId(seed)
    };
  }

  function validate(record) {
    if (!record) return false;
    if (record.slug !== SLUG) return false;
    if (record.record_kind !== KIND) return false;
    if (record.src !== 'generated') return false;
    if (record.id !== genId(record.seed)) return false;
    return true;
  }

  function runTests() {
    var results = [];
    function t(name, pass) { results.push({ name: name, pass: !!pass }); }
    var a = generate('alpha'), b = generate('alpha');
    t('same seed -> same id', a.id === b.id);
    t('same seed -> same content', JSON.stringify(a) === JSON.stringify(b));
    var c = generate('beta');
    t('different seeds -> different ids', a.id !== c.id);
    t('generated id starts with own prefix', a.id.indexOf(ID_PREFIX) === 0);
    t('generated id uses GEN- namespace after own prefix', a.id.indexOf(ID_PREFIX + 'GEN-') === 0);
    t('hard stop is one billion', HARD_STOP === 1000000000);
    t('record_kind matches manifest', a.record_kind === KIND);
    t('validate accepts own output', validate(a));
    t('validate rejects wrong kind', !validate({ slug: SLUG, record_kind: 'other', src: 'generated', seed: 'alpha', id: a.id }));
    t('validate rejects wrong id', !validate({ slug: SLUG, record_kind: KIND, src: 'generated', seed: 'alpha', id: 'JAH-X-000001' }));
    return results;
  }

  var api = { slug: SLUG, kind: KIND, version: GEN_VERSION, hardStop: HARD_STOP,
    generate: generate, validate: validate, runTests: runTests, genId: genId };
  global.JAHDB = global.JAHDB || {};
  global.JAHDB.generators = global.JAHDB.generators || {};
  global.JAHDB.generators[SLUG] = api;
  if (typeof global.JAHDB.registerGenerator === 'function') { global.JAHDB.registerGenerator(SLUG, api); }
  if (typeof global.JAHDB.getGenerator !== 'function') {
    global.JAHDB.getGenerator = function (slug) { return global.JAHDB.generators[slug] || null; };
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
