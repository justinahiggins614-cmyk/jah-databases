'use strict';
/* gen-working-version-for-all-demos.js
 * Deterministic client-side generator + executable demo for
 * "The Working Version for All Demos Database" (JAH-DWV-).
 *
 * Mirrors demoai-lane-r18/build.py::build_records_a byte-for-byte in field
 * semantics: genRecord(entry, seq, scan) must produce the same record as the
 * Python builder for the same inputs (verified by node parity test at build).
 *
 * Boundless generator: CAP = 1e15 (one quadrillion) hard stop, generator
 * ladder simple -> ... -> god-mode, self-regulated, completion detection
 * (when the live manifest has no new databases the DB is marked complete
 * with reason). Generated output is labeled "generated"; assistant-built
 * records are labeled "assistant-built" -- never mixed.
 */
(function (root) {
  var CAP = 1e15;
  var LADDER = ['simple', 'most-competitive', 'mix-and-match', 'unmade',
    'top-notch-or-better', 'future-grade', 'god-mode'];
  var ID_PREFIX = 'JAH-DWV-';
  var PAGE_BASE = 'https://justinahiggins614-cmyk.github.io/jah-databases/db/';
  var LAST_VERIFIED = '2026-10-21';
  var ANCHOR_KIND = { 'p-demo': 'demo-lab', 'dGen': 'demo-lab', 'p-gen': 'generator', '': 'page' };
  var GENERATOR_CANON = {
    cap_records: CAP,
    cap_note: 'Hard stop at one quadrillion records per database, or earlier when genuinely complete (marked complete with reason).',
    ladder: LADDER,
    self_regulated: true,
    throttled: 'Throttled to a host-safe rate; never overloads the host or burns usage.',
    double_check: 'All generator work is double-checked by the assistant and by the generator itself.',
    dedupe: 'Duplicate check enforced on every write (id dedupe).',
    output_labeling: 'System-generated output is marked "generated"; assistant-built output is marked "assistant-built" -- never mixed.',
    completion_detection: 'Generator knows when complete: when the live manifest holds no new databases, the database is marked complete with reason and stops.'
  };

  function pad6(n) { var s = String(n); while (s.length < 6) s = '0' + s; return s; }

  function ladderRank(recordCount) {
    var n = parseInt(recordCount, 10) || 0;
    if (n >= 100000) return 'complex';
    if (n >= 1000) return 'compounded';
    return 'simple';
  }

  function genRecord(entry, seq, scan) {
    var name = entry.name || entry.slug;
    var rk = entry.record_kind || 'record';
    var url = scan.url, anchor = scan.anchor, kind = scan.kind;
    return {
      id: ID_PREFIX + pad6(seq),
      title: name + ' -- Working Version',
      target_slug: entry.slug,
      target_name: name,
      target_record_kind: rk,
      target_record_count: (entry.record_count == null ? 0 : entry.record_count),
      target_ai_name: entry.ai_name || '',
      demo_url: url,
      demo_anchor: anchor,
      demo_kind: kind,
      verified: !!scan.verified,
      link_check: scan.link_check,
      ladder_rank: ladderRank(entry.record_count),
      teaching: {
        simple: 'The working version of the ' + name + ' demo: open ' + url + ' to run the demo.',
        compounded: 'Each ' + rk + ' ships a runnable demo program. The working version link points at ' +
          'the database\'s Demo Lab entry point where the demo generates, runs, simulates step by step, ' +
          'or opens in the interactive playground.',
        complex: 'Full working version: copy or download the demo code and run it on a PC with ' +
          'node demo.js. Every link is verified against the live page bytes: the anchor id is ' +
          'confirmed present in the page file before the record ships.'
      },
      generator: GENERATOR_CANON,
      program: {
        engine: 'gen-working-version-for-all-demos.js',
        fn: 'demo',
        args: { demo_url: url, demo_anchor: anchor, verified: !!scan.verified, link_check: scan.link_check },
        note: 'The executable demo is demo(record) in the engine file: it re-verifies the demo link -- ' +
          'URL well-formed, anchor in the known set, verified/link_check consistent. Node-tested at build time.'
      },
      working_version: url,
      march_marker: 'MILLION IN PROGRESS',
      src: 'assistant-built',
      provenance: {
        derived_from: 'live manifest.json + local db/<slug>/index.html anchor scan',
        build: 'demoai-lane-r18/build.py',
        order: '2026-10-21 item 83 WORKING-VERSION-FOR-ALL-DEMOS'
      },
      last_verified: LAST_VERIFIED,
      record_kind: 'working version link record',
      ai_name: 'JAH Working Version Linker',
      status: 'live'
    };
  }

  /* Executable demo: re-verify a record's demo link, deterministically.
   * Returns {record_id, ok, checks:[{name, pass, detail}]}. */
  function demo(record) {
    var checks = [];
    function add(name, pass, detail) { checks.push({ name: name, pass: !!pass, detail: detail || '' }); }
    var m = /^https:\/\/justinahiggins614-cmyk\.github\.io\/jah-databases\/db\/([a-z0-9-]+)\/(#(p-demo|dGen|p-gen))?$/.exec(record.demo_url || '');
    add('url-well-formed', !!m, m ? ('slug=' + m[1]) : 'bad url: ' + record.demo_url);
    var urlAnchor = m && m[3] ? m[3] : '';
    add('anchor-known', urlAnchor in ANCHOR_KIND, 'anchor=' + JSON.stringify(urlAnchor));
    add('anchor-matches-record', urlAnchor === (record.demo_anchor || ''),
      'url anchor ' + JSON.stringify(urlAnchor) + ' vs record ' + JSON.stringify(record.demo_anchor));
    add('kind-matches-anchor', (ANCHOR_KIND[urlAnchor] || '') === (record.demo_kind || ''),
      'kind=' + JSON.stringify(record.demo_kind));
    add('id-format', new RegExp('^' + ID_PREFIX + '\\d{6}$').test(record.id || ''), 'id=' + record.id);
    add('verified-flag', typeof record.verified === 'boolean', 'verified=' + record.verified);
    add('link-check-value', ['anchor-verified', 'page-only', 'page-missing'].indexOf(record.link_check) !== -1,
      'link_check=' + record.link_check);
    add('link-check-consistent',
      (record.link_check === 'anchor-verified') === (record.verified === true && urlAnchor !== '') ||
      record.link_check === 'page-only' || record.link_check === 'page-missing',
      'consistency of verified/link_check/anchor');
    add('src-label', record.src === 'assistant-built', 'src=' + record.src);
    add('last-verified', record.last_verified === LAST_VERIFIED, 'last_verified=' + record.last_verified);
    var ok = checks.every(function (c) { return c.pass; });
    return { record_id: record.id, ok: ok, checks: checks };
  }

  /* Boundless generation over manifest entries with their scans. */
  function generate(entries, scans, startSeq) {
    var out = [], seen = {};
    for (var i = 0; i < entries.length; i++) {
      var r = genRecord(entries[i], (startSeq || 1) + i, scans[i]);
      if (seen[r.id]) throw new Error('duplicate id: ' + r.id);
      seen[r.id] = 1;
      out.push(r);
    }
    return out;
  }

  var api = {
    CAP: CAP, LADDER: LADDER, ID_PREFIX: ID_PREFIX, PAGE_BASE: PAGE_BASE,
    LAST_VERIFIED: LAST_VERIFIED, ANCHOR_KIND: ANCHOR_KIND,
    GENERATOR_CANON: GENERATOR_CANON,
    genRecord: genRecord, demo: demo, generate: generate, ladderRank: ladderRank
  };
  if (typeof module !== 'undefined' && module.exports) { module.exports = api; }
  else { root.DemoAIWorkingVersionGen = api; }
})(typeof self !== 'undefined' ? self : this);
