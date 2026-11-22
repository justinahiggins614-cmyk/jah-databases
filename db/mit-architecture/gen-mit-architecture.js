/* Generator for mit-architecture — MIT OpenCourseWare suite, GEN_VERSION 1.0.
   Deterministic IDs: genId(seed) = <id_prefix>GEN- + hash(slug|version|seed)[0:12].
   Identical input -> identical id and identical content. GEN- namespace never
   collides with shipped numeric record ids. Registered with the shared JAHDB
   registry and exposed as window.MitArchitectureTools. */
(function (global) {
  'use strict';
  var SLUG = 'mit-architecture';
  var KIND = 'mit architecture record';
  var ID_PREFIX = 'JAH-MIT4-';
  var GEN_VERSION = '1.0';
  var HARD_STOP = 1000000000000000;
  var MAX_BATCH = 100;
  var SEED_TITLES = ["4.001 Where Is and What Is Architecture and Design?", "4.02A Design Studio: How to Design Intensive", "4.021 Design Studio: How to Design", "4.022 Architecture Design Foundations", "4.023 Architecture Design Studio I", "4.024 Architecture Design Studio II", "4.031 Design Studio: Objects and Interaction", "4.032 Design Studio: Information Design and Visualization", "4.033 Design Studio: Information and Visualization", "4.041 Design Studio: Advanced Product Design", "4.302 Foundations in Art, Design, and Spatial Practices", "4.401 Environmental Technologies in Buildings", "4.440J Building Structural Systems I", "4.500 Introduction to Design Computing", "4.501 Creative Design Prototyping", "4.502 Advanced Visualization: Architecture in Motion Graphics"];

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
    return ID_PREFIX + 'GEN-' + sha12(SLUG + '|' + GEN_VERSION + '|' + String(seed)).toUpperCase();
  }

  function generate(seed) {
    seed = (seed === undefined || seed === null || seed === '') ? 'default' : String(seed);
    var title = SEED_TITLES[Math.abs(sha12(seed).charCodeAt(0)) % SEED_TITLES.length];
    return {
      id: genId(seed),
      slug: SLUG,
      record_kind: KIND,
      src: 'generated',
      seed: seed,
      generator_version: GEN_VERSION,
      title: 'Generated: ' + title + ' (seed ' + seed + ')',
      description: 'A boundlessly generated ' + KIND + ' in the family of ' + title +
        ', produced by the seeded generator for this database.',
      demo_output: 'generated record ' + genId(seed)
    };
  }

  function generateBatch(n, seedBase) {
    var out = [];
    var count = Math.min(n || 1, MAX_BATCH);
    var base = (seedBase === undefined || seedBase === null || seedBase === '') ? 'batch' : String(seedBase);
    for (var i = 0; i < count; i++) { out.push(generate(base + '-' + i)); }
    return out;
  }

  function searchRecords(q, pool) {
    q = String(q || '').toLowerCase();
    return (pool || SEED_TITLES).filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
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
    t('generated id uses GEN- namespace', a.id.indexOf('GEN-') !== -1);
    t('generated id prefix', a.id.indexOf(ID_PREFIX + 'GEN-') === 0);
    t('validate accepts own output', validate(a));
    t('validate rejects wrong kind', !validate({ slug: SLUG, record_kind: 'other', src: 'generated', seed: 'alpha', id: a.id }));
    t('validate rejects wrong id', !validate({ slug: SLUG, record_kind: KIND, src: 'generated', seed: 'alpha', id: 'JAH-X-000001' }));
    t('batch throttle', generateBatch(500, 't').length === MAX_BATCH);
    t('search finds a title', searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1);
    var passed = results.filter(function (r) { return r.pass; }).length;
    return { total: results.length, passed: passed, tests: results };
  }

  var api = { slug: SLUG, kind: KIND, version: GEN_VERSION, hardStop: HARD_STOP,
    generate: generate, generateRecord: generate, generateBatch: generateBatch,
    searchRecords: searchRecords, validate: validate, validateRecord: validate,
    runTests: runTests, genId: genId };
  global.JAHDB = global.JAHDB || {};
  global.JAHDB.generators = global.JAHDB.generators || {};
  global.JAHDB.generators[SLUG] = api;
  if (typeof global.JAHDB.registerGenerator === 'function') { global.JAHDB.registerGenerator(SLUG, api); }
  if (typeof global.JAHDB.getGenerator !== 'function') {
    global.JAHDB.getGenerator = function (slug) { return global.JAHDB.generators[slug] || null; };
  }
  global['MitArchitectureTools'] = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
