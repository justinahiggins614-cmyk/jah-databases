/* Generator for mit-mechanical-engineering-signature — MIT OpenCourseWare suite, GEN_VERSION 1.0.
   Deterministic IDs: genId(seed) = <id_prefix>GEN- + hash(slug|version|seed)[0:12].
   Identical input -> identical id and identical content. GEN- namespace never
   collides with shipped numeric record ids. Registered with the shared JAHDB
   registry and exposed as window.MitMechanicalEngineeringToolsSignature. */
(function (global) {
  'use strict';
  var SLUG = 'mit-mechanical-engineering-signature';
  var KIND = 'mit mechanical engineering record';
  var ID_PREFIX = 'JAH-MIT2S-';
  var GEN_VERSION = '1.0';
  var HARD_STOP = 1000000000000000;
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Signature: 2.001 Mechanics and Materials I", "Signature: 2.002 Mechanics and Materials II", "Signature: 2.003 Dynamics and Control I", "Signature: 2.004 Dynamics and Control II", "Signature: 2.005 Thermal-Fluids Engineering I", "Signature: 2.006 Thermal-Fluids Engineering II", "Signature: 2.007 Design and Manufacturing I", "Signature: 2.008 Design and Manufacturing II", "Signature: 2.016 Hydrodynamics", "Signature: 2.017J Design of Electromechanical Robotic Systems", "Signature: 2.12 Introduction to Robotics", "Signature: 2.14 Analysis and Design of Feedback Control Systems", "Signature: 2.670 Mechanical Engineering Tools", "Signature: 2.671 Measurement and Instrumentation", "Signature: 2.71 Optics", "Signature: 2.72 Elements of Mechanical Design"];

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
  global['MitMechanicalEngineeringToolsSignature'] = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
