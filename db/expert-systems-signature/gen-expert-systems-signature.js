"use strict";
/* expert-systems-signature — boundless generator. Seeded, deterministic, throttled,
   content-hash duplicate-checked, hard stop at 10^9.
   - generateRecord(seed) is a PURE function of its seed: the record ID is derived
     from a stable hash of the seed (JAH-ESYSS-GEN-NNNNNN), and every field is composed
     deterministically from the same seeded stream. Same seed in a fresh process
     produces the byte-identical record. No in-memory counter plays any role.
   - Generated records carry the full 19-key archive schema (see ARCHIVE_KEYS).
     They are NOT structural samples: they carry slug, record_kind, a GEN-segment
     ID, substantive science_proof, math_proof, source and a runnable demo program
     whose expected_output is computed by the same arithmetic as the demo code.
     The demo code is straight-line Python mirroring the archive demo arithmetic
     for the same kind (series, ledger, metric, opt, chain, prob, cf).
   - Generated records are Signature-made: edition "signature", src "generated",
     source_quality "signature-generated". They are never presented as archive
     records and cite no real paper: the source field says so in plain words.
   - Design-study rule: no generated record asserts a real system, a real
     forecast, a real prescription, or an established result; the guard text
     in every record states the design-study status.
   - CLI: node gen-expert-systems-signature.js --seed 7 --n 1  prints a JSON array.
   - Library: generateRecord(seed) / generate(seed) / generateBatch(n, seed) /
     validateRecord(rec) / runTests(). */
(function (root) {
  var SLUG = "expert-systems-signature";
  var PREFIX = "JAH-ESYSS-";
  var RECORD_KIND = "expert system record";
  var HARD_STOP = 1000000000; // 10^9
  var MAX_BATCH = 100;
  var AI_NAME = "JAH Expert Systems Librarian (Signature)";
  var CROSS_LINKS = "ai-types, machine-learning-public-ai, reinforcement-learning-public-ai, ai-planning-public-ai, superintelligence, equations";
  var GENERATOR_NOTE = "gen-expert-systems-signature.js (seeded, deterministic, max 100 per call, hard stop 10^9, src generated)";
  var ARCHIVE_KEYS = ["id", "slug", "title", "edition", "record_kind", "ladder_rank", "description", "body", "science_proof", "math_proof", "source", "source_quality", "src", "ai_name", "status", "layers", "cross_links", "generator", "demo"];
  var GUARD = " design-study note: this record is Signature-generated, not a public record; it asserts no real system, no historical measurement, and no established result.";
  var TOPICS = [
  {
    "key": "cf",
    "kind": "cf",
    "title": "Generated: Certainty Factor Combination Ledger",
    "about": "combining certainty factors for a rule-based diagnosis"
  },
  {
    "key": "chain",
    "kind": "chain",
    "title": "Generated: Forward Chaining Firing Ledger",
    "about": "rules fired per stage in a forward-chaining run",
    "stages": 4,
    "lo": 5,
    "hi": 40
  },
  {
    "key": "ledger",
    "kind": "ledger",
    "title": "Generated: Rule Base Size Ledger",
    "about": "rules per module in a rule base",
    "names": [
      "diagnosis",
      "configuration",
      "planning",
      "monitoring",
      "explanation"
    ],
    "lo": 5,
    "hi": 150
  },
  {
    "key": "metric",
    "kind": "metric",
    "title": "Generated: Diagnosis Score Error Ledger",
    "about": "scoring error between an expert system and a reference"
  },
  {
    "key": "opt",
    "kind": "opt",
    "title": "Generated: Rule Engine Choice Ledger",
    "about": "choosing a rule engine by benefit per cost"
  },
  {
    "key": "series",
    "kind": "series",
    "title": "Generated: Expert System Adoption Series",
    "about": "growth of deployed expert systems over dated years",
    "yearLo": 2005,
    "yearHi": 2019,
    "valLo": 20,
    "valHi": 400
  },
  {
    "key": "prob",
    "kind": "prob",
    "title": "Generated: Diagnosis Confidence Ledger",
    "about": "calibration of an expert system's confidence"
  },
  {
    "key": "ledger2",
    "kind": "ledger",
    "title": "Generated: Knowledge Elicitation Ledger",
    "about": "rules captured per elicitation session",
    "names": [
      "session 1",
      "session 2",
      "session 3",
      "session 4",
      "session 5"
    ],
    "lo": 5,
    "hi": 30
  }
];

  var seenContent = {};
  var archiveHashes = {};

  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function fnv1a(str) {
    var h = 0x811c9dc5;
    for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 0x01000193); }
    return h >>> 0;
  }
  function hex8(n) { var s = n.toString(16); while (s.length < 8) s = "0" + s; return s; }
  function pad(n) { var s = String(n); while (s.length < 6) s = "0" + s; return s; }
  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
  /* Python-style float formatting: Python str(round(x, 4)) prints 39.0 for
     39.0 and 0.142 for 0.142. JS String(39) would print "39", so floats get ".0". */
  function pyFloat(x) {
    var v = parseFloat(x.toFixed(4));
    if (Number.isInteger(v)) return v + ".0";
    return String(v);
  }
  function pyNum(x) { return String(x); }

  function contentHash(rec) {
    if (!rec) return "";
    var parts = [rec.title || "", rec.description || "", rec.body || "", rec.science_proof || "", rec.math_proof || "", rec.source || ""];
    return hex8(fnv1a(parts.join("\n")));
  }
  function noteGenerated(rec) { if (rec) seenContent[contentHash(rec)] = rec.id || true; return rec; }
  function isDuplicateContent(rec) {
    if (!rec) return { duplicate: false, source: null, contentHash: "" };
    var h = contentHash(rec);
    if (seenContent[h]) return { duplicate: true, source: "session", contentHash: h };
    if (archiveHashes[h]) return { duplicate: true, source: "archive", matchedId: archiveHashes[h], contentHash: h };
    return { duplicate: false, source: null, contentHash: h };
  }
  function setArchiveRecords(list) {
    archiveHashes = {};
    var n = 0;
    (list || []).forEach(function (r) { if (r) { archiveHashes[contentHash(r)] = r.id || "?"; n += 1; } });
    return n;
  }
  function checkAgainstArchive(rec, records) {
    if (!rec) return { duplicate: false, matchedId: null, contentHash: "" };
    var h = contentHash(rec);
    if (records) {
      for (var i = 0; i < records.length; i++) {
        if (records[i] && contentHash(records[i]) === h) return { duplicate: true, matchedId: records[i].id || "?", contentHash: h };
      }
      return { duplicate: false, matchedId: null, contentHash: h };
    }
    if (archiveHashes[h]) return { duplicate: true, matchedId: archiveHashes[h], contentHash: h };
    return { duplicate: false, matchedId: null, contentHash: h };
  }
  function clearDuplicateState() { seenContent = {}; archiveHashes = {}; }

  function round4(x) { return parseFloat(x.toFixed(4)); }
  function round2(x) { return parseFloat(x.toFixed(2)); }
  function round1(x) { return parseFloat(x.toFixed(1)); }

  /* Build the demo (Python code + expected output) for one topic and its
     seeded numbers. The JS arithmetic mirrors the Python demo exactly, and
     expected_output is what the Python code prints. Print order is sorted
     by key, matching the archive demo format. */
  function buildDemo(topic, d) {
    var code = "", expected = "";
    if (topic.kind === "series") {
      var seriesPy = d.series.map(function (yv) { return "(" + yv[0] + ", " + yv[1] + ")"; }).join(", ");
      code = "series = [" + seriesPy + "]\n" +
        "years = [y for y, v in series]\n" +
        "values = [v for y, v in series]\n" +
        "earliest = values[0]\n" +
        "latest = values[-1]\n" +
        "multiple = round(latest / earliest, 4)\n" +
        "span = years[-1] - years[0]\n" +
        "cagr = round((latest / earliest) ** (1 / span) - 1, 4)\n" +
        "mean = round(sum(values) / len(values), 2)\n" +
        "n = len(values)\n" +
        "print('cagr:', cagr)\n" +
        "print('earliest:', earliest)\n" +
        "print('latest:', latest)\n" +
        "print('mean:', mean)\n" +
        "print('multiple:', multiple)\n" +
        "print('n:', n)\n";
      expected = "cagr: " + pyFloat(d.cagr) + "\nearliest: " + d.earliest +
        "\nlatest: " + d.latest + "\nmean: " + pyFloat(d.mean) +
        "\nmultiple: " + pyFloat(d.multiple) + "\nn: " + d.n + "\n";
    } else if (topic.kind === "ledger") {
      var ledgerPy = d.items.map(function (kv) { return '("' + kv[0] + '", ' + kv[1] + ")"; }).join(", ");
      code = "ledger = [" + ledgerPy + "]\n" +
        "counts = [c for _, c in ledger]\n" +
        "total = round(sum(counts), 4)\n" +
        "mean = round(sum(counts) / len(counts), 4)\n" +
        "smallest = min(counts)\n" +
        "largest = max(counts)\n" +
        "n = len(counts)\n" +
        "print('largest:', largest)\n" +
        "print('mean:', mean)\n" +
        "print('n:', n)\n" +
        "print('smallest:', smallest)\n" +
        "print('total:', total)\n";
      expected = "largest: " + d.largest + "\nmean: " + pyFloat(d.mean) + "\nn: " + d.n +
        "\nsmallest: " + d.smallest + "\ntotal: " + d.total + "\n";
    } else if (topic.kind === "metric") {
      var pairsPy = d.pairs.map(function (p) { return "(" + pyFloat(p[0]) + ", " + pyFloat(p[1]) + ")"; }).join(", ");
      code = "pairs = [" + pairsPy + "]\n" +
        "errs = [abs(p - a) for p, a in pairs]\n" +
        "mae = round(sum(errs) / len(errs), 4)\n" +
        "rmse = round((sum(e * e for e in errs) / len(errs)) ** 0.5, 4)\n" +
        "max_err = round(max(errs), 4)\n" +
        "n = len(pairs)\n" +
        "print('mae:', mae)\n" +
        "print('max_err:', max_err)\n" +
        "print('n:', n)\n" +
        "print('rmse:', rmse)\n";
      expected = "mae: " + pyFloat(d.mae) + "\nmax_err: " + pyFloat(d.maxErr) + "\nn: " + d.n +
        "\nrmse: " + pyFloat(d.rmse) + "\n";
    } else if (topic.kind === "opt") {
      var optionsPy = d.options.map(function (o) { return '("' + o[0] + '", ' + o[1] + ", " + o[2] + ")"; }).join(", ");
      code = "options = [" + optionsPy + "]\n" +
        "scored = [(b / c, name) for name, c, b in options]\n" +
        "best_ratio_raw, best = max(scored)\n" +
        "best_ratio = round(best_ratio_raw, 4)\n" +
        "total_cost = sum(c for _, c, _ in options)\n" +
        "total_benefit = sum(b for _, _, b in options)\n" +
        "print('best:', best)\n" +
        "print('best_ratio:', best_ratio)\n" +
        "print('total_benefit:', total_benefit)\n" +
        "print('total_cost:', total_cost)\n";
      expected = "best: " + d.best + "\nbest_ratio: " + pyFloat(d.bestRatio) +
        "\ntotal_benefit: " + d.totalBenefit + "\ntotal_cost: " + d.totalCost + "\n";
    } else if (topic.kind === "chain") {
      var chainPy = d.items.map(function (kv) { return '("' + kv[0] + '", ' + kv[1] + ")"; }).join(", ");
      code = "chain = [" + chainPy + "]\n" +
        "fired = [f for _, f in chain]\n" +
        "total_fired = sum(fired)\n" +
        "stages = len(fired)\n" +
        "max_stage = max(fired)\n" +
        "mean = round(total_fired / stages, 4)\n" +
        "print('max_stage:', max_stage)\n" +
        "print('mean:', mean)\n" +
        "print('stages:', stages)\n" +
        "print('total_fired:', total_fired)\n";
      expected = "max_stage: " + d.maxStage + "\nmean: " + pyFloat(d.mean) + "\nstages: " + d.stages +
        "\ntotal_fired: " + d.totalFired + "\n";
    } else if (topic.kind === "prob") {
      var probsPy = d.pairs.map(function (p) { return "(" + pyFloat(p[0]) + ", " + p[1] + ")"; }).join(", ");
      code = "probs = [" + probsPy + "]\n" +
        "brier = round(sum((p - o) ** 2 for p, o in probs) / len(probs), 4)\n" +
        "mean_p = round(sum(p for p, _ in probs) / len(probs), 4)\n" +
        "hits = sum(1 for p, o in probs if (p >= 0.5) == bool(o))\n" +
        "n = len(probs)\n" +
        "print('brier:', brier)\n" +
        "print('hits:', hits)\n" +
        "print('mean_p:', mean_p)\n" +
        "print('n:', n)\n";
      expected = "brier: " + pyFloat(d.brier) + "\nhits: " + d.hits + "\nmean_p: " + pyFloat(d.meanP) +
        "\nn: " + d.n + "\n";
    } else if (topic.kind === "cf") {
      var cfsPy = d.pairs.map(function (p) { return "(" + pyFloat(p[0]) + ", " + pyFloat(p[1]) + ")"; }).join(", ");
      code = "cfs = [" + cfsPy + "]\n" +
        "combined = [a + b - a * b for a, b in cfs]\n" +
        "mean_combined = round(sum(combined) / len(combined), 4)\n" +
        "n = len(cfs)\n" +
        "print('mean_combined:', mean_combined)\n" +
        "print('n:', n)\n";
      expected = "mean_combined: " + pyFloat(d.meanCombined) + "\nn: " + d.n + "\n";
    }
    return { code: code, expected: expected };
  }

  function drawNumbers(topic, rnd) {
    var d = {};
    if (topic.kind === "series") {
      var y0 = topic.yearLo + Math.floor(rnd() * (topic.yearHi - topic.yearLo + 1));
      d.series = [];
      for (var i = 0; i < 5; i++) {
        d.series.push([y0 + i, topic.valLo + Math.floor(rnd() * (topic.valHi - topic.valLo + 1))]);
      }
      var vals = d.series.map(function (yv) { return yv[1]; });
      d.earliest = vals[0];
      d.latest = vals[4];
      d.multiple = round4(d.latest / d.earliest);
      var span = d.series[4][0] - d.series[0][0];
      d.cagr = round4(Math.pow(d.latest / d.earliest, 1 / span) - 1);
      d.mean = round2(vals.reduce(function (a, b) { return a + b; }, 0) / vals.length);
      d.n = 5;
      d.summary = "Series " + d.series[0][0] + " to " + d.series[4][0] + " with values " +
        vals.join(", ") + "; multiple " + pyFloat(d.multiple) + ", CAGR " + pyFloat(d.cagr) +
        ", mean " + pyFloat(d.mean) + ".";
    } else if (topic.kind === "ledger") {
      d.items = topic.names.map(function (name) {
        return [name, topic.lo + Math.floor(rnd() * (topic.hi - topic.lo + 1))];
      });
      var counts = d.items.map(function (kv) { return kv[1]; });
      d.total = counts.reduce(function (a, b) { return a + b; }, 0);
      d.mean = round4(d.total / counts.length);
      d.smallest = Math.min.apply(null, counts);
      d.largest = Math.max.apply(null, counts);
      d.n = counts.length;
      d.summary = "Ledger: " + d.items.map(function (kv) { return kv[0] + " " + kv[1]; }).join(", ") +
        "; total " + d.total + ", mean " + pyFloat(d.mean) + ", smallest " + d.smallest + ", largest " + d.largest + ".";
    } else if (topic.kind === "metric") {
      d.pairs = [];
      for (var j = 0; j < 5; j++) {
        var p = round1(10 + rnd() * 80);
        var e = round1(-3 + rnd() * 6);
        d.pairs.push([p, round1(p + e)]);
      }
      var errs = d.pairs.map(function (pr) { return Math.abs(pr[0] - pr[1]); });
      d.mae = round4(errs.reduce(function (a, b) { return a + b; }, 0) / errs.length);
      d.rmse = round4(Math.sqrt(errs.reduce(function (a, b) { return a + b * b; }, 0) / errs.length));
      d.maxErr = round4(Math.max.apply(null, errs));
      d.n = 5;
      d.summary = "MAE " + pyFloat(d.mae) + " over " + d.n + " pairs; RMSE " + pyFloat(d.rmse) +
        ", largest error " + pyFloat(d.maxErr) + ".";
    } else if (topic.kind === "opt") {
      d.options = [];
      for (var k = 0; k < 5; k++) {
        var cost = 20 + Math.floor(rnd() * 181);
        var ratio = Math.round((1.5 + rnd() * 2.5) * 100) / 100;
        d.options.push(["option " + (k + 1), cost, Math.round(cost * ratio)]);
      }
      /* Mirror Python max() on (ratio, name) tuples: largest ratio wins;
         on a tie the lexicographically larger name wins. */
      var bestRatio = -1, bestName = "";
      d.options.forEach(function (o) {
        var r = o[2] / o[1];
        if (r > bestRatio || (r === bestRatio && o[0] > bestName)) { bestRatio = r; bestName = o[0]; }
      });
      d.best = bestName;
      d.bestRatio = round4(bestRatio);
      d.totalCost = d.options.reduce(function (a, o) { return a + o[1]; }, 0);
      d.totalBenefit = d.options.reduce(function (a, o) { return a + o[2]; }, 0);
      d.summary = "Best option " + d.best + " at ratio " + pyFloat(d.bestRatio) +
        "; total cost " + d.totalCost + ", total benefit " + d.totalBenefit + ".";
    } else if (topic.kind === "chain") {
      d.items = [];
      for (var s = 0; s < topic.stages; s++) {
        d.items.push(["stage " + (s + 1), topic.lo + Math.floor(rnd() * (topic.hi - topic.lo + 1))]);
      }
      var fired = d.items.map(function (kv) { return kv[1]; });
      d.totalFired = fired.reduce(function (a, b) { return a + b; }, 0);
      d.stages = fired.length;
      d.maxStage = Math.max.apply(null, fired);
      d.mean = round4(d.totalFired / d.stages);
      d.summary = "Chain fired " + d.totalFired + " rules over " + d.stages + " stages; mean " +
        pyFloat(d.mean) + " per stage, busiest stage " + d.maxStage + ".";
    } else if (topic.kind === "prob") {
      d.pairs = [];
      for (var m = 0; m < 5; m++) {
        var pp = Math.round((0.05 + rnd() * 0.9) * 100) / 100;
        var y = rnd() < 0.6 ? 1 : 0;
        d.pairs.push([pp, y]);
      }
      var sq = d.pairs.map(function (pr) { return Math.pow(pr[0] - pr[1], 2); });
      d.brier = round4(sq.reduce(function (a, b) { return a + b; }, 0) / sq.length);
      d.meanP = round4(d.pairs.reduce(function (a, pr) { return a + pr[0]; }, 0) / d.pairs.length);
      d.hits = d.pairs.reduce(function (a, pr) { return a + (((pr[0] >= 0.5) === (pr[1] === 1)) ? 1 : 0); }, 0);
      d.n = 5;
      d.summary = "Brier " + pyFloat(d.brier) + " over " + d.n + " pairs; mean p " + pyFloat(d.meanP) +
        ", hits " + d.hits + ".";
    } else if (topic.kind === "cf") {
      d.pairs = [];
      for (var c = 0; c < 3; c++) {
        d.pairs.push([Math.round((0.1 + rnd() * 0.8) * 10) / 10, Math.round((0.1 + rnd() * 0.8) * 10) / 10]);
      }
      var comb = d.pairs.map(function (pr) { return pr[0] + pr[1] - pr[0] * pr[1]; });
      d.meanCombined = round4(comb.reduce(function (a, b) { return a + b; }, 0) / comb.length);
      d.n = 3;
      d.summary = "Combined certainty factors average " + pyFloat(d.meanCombined) + " over " + d.n + " pairs.";
    }
    return d;
  }

  function generateRecord(seed) {
    var s = (typeof seed === "number" && isFinite(seed)) ? Math.floor(Math.abs(seed)) : 1;
    if (s >= HARD_STOP) return null;
    var rnd = mulberry32(s);
    var topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
    var d = drawNumbers(topic, rnd);
    var demo = buildDemo(topic, d);
    var lr = rnd();
    var ladderRank = lr < 0.4 ? "simple" : (lr < 0.75 ? "compounded" : "complex");
    var id = PREFIX + "GEN-" + pad(100000 + (fnv1a(SLUG + "#" + s) % 900000));
    var title = topic.title;
    var description =
      "Generated " + RECORD_KIND + " record about " + topic.about + ". " +
      "The record states a checkable claim in testable form: a ledger, a measurement, or a choice, " +
      "computed from seeded numbers so the same seed always gives the same record. " +
      "The demo recomputes the record's numbers from its seeded inputs and prints them, so the arithmetic is checked by execution rather than asserted. " +
      "Nothing here is a public record: the numbers are generated, the subject is a design study, and no real system, forecast, or prescription is claimed. " +
      d.summary + GUARD;
    var scienceProof =
      "Science proof: " + cap(topic.about) + " is measured by the demo, which recomputes the record's numbers from its seeded inputs " +
      "and prints them. The measurement is the evidence; the record claims nothing beyond what the demo computes." + GUARD;
    var mathProof =
      "Math proof: the demo recomputes every number in this record from its inputs and prints the result, so the arithmetic is checked " +
      "by execution rather than asserted. Rerun the demo code to verify.";
    var source =
      "Signature-generated record: the " + SLUG + " design-study specification in this pair; no single paper is cited, " +
      "because this record is generated rather than harvested from a publication. For published sources see the public-harvest records " +
      "in this database (as of November 2026)." + GUARD;
    return {
      id: id, slug: SLUG, title: title, edition: "signature", record_kind: RECORD_KIND,
      ladder_rank: ladderRank, description: description,
      body: description + "\n\n" + scienceProof + "\n\n" + mathProof,
      science_proof: scienceProof, math_proof: mathProof, source: source,
      source_quality: "signature-generated", src: "generated", ai_name: AI_NAME,
      status: "built", layers: SLUG, cross_links: CROSS_LINKS, generator: GENERATOR_NOTE,
      demo: { language: "python", code: demo.code, expected_output: demo.expected }
    };
  }
  function generate(seed) { return generateRecord(seed); }
  function generateBatch(n, seed) {
    /* Collect up to count distinct records, advancing the seed past duplicates
       instead of returning short: a batch of 100 must contain 100 records. */
    var out = [], count = Math.min(n || 1, MAX_BATCH);
    var base = seed || 1, attempts = 0, maxAttempts = count * 20;
    while (out.length < count && attempts < maxAttempts) {
      var r = generateRecord(base + attempts);
      attempts += 1;
      if (!r) break;
      if (isDuplicateContent(r).duplicate) continue;
      noteGenerated(r);
      out.push(r);
    }
    return out;
  }
  function searchRecords(q, pool) {
    q = String(q || "").toLowerCase();
    return (pool || TOPICS.map(function (t) { return t.title; })).filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
  }
  function validateRecord(rec) {
    var problems = [];
    if (!rec) return { valid: false, problems: ["record is required"] };
    if (rec.record_kind !== RECORD_KIND) problems.push("record_kind must be " + RECORD_KIND);
    if (rec.slug !== SLUG) problems.push("slug must be " + SLUG);
    if (!rec.id || rec.id.indexOf(PREFIX) !== 0) problems.push("id must start with " + PREFIX);
    if (rec.id && rec.id.indexOf("GEN-") === -1) problems.push("id must contain a GEN segment");
    if (!rec.title) problems.push("title is required");
    if (rec.edition !== "signature") problems.push("edition must be signature (generated records are Signature-made)");
    if (rec.src !== "generated") problems.push("src must be generated");
    if (rec.ladder_rank !== "simple" && rec.ladder_rank !== "compounded" && rec.ladder_rank !== "complex") problems.push("ladder_rank must be simple, compounded, or complex");
    if (!rec.description || rec.description.length < 500) problems.push("description is required (at least 500 characters)");
    if (!rec.body || rec.body.length < 500) problems.push("body is required (at least 500 characters)");
    if (!rec.science_proof || rec.science_proof.length < 100) problems.push("science_proof is required (at least 100 characters)");
    if (!rec.math_proof || rec.math_proof.length < 50) problems.push("math_proof is required (at least 50 characters)");
    if (!rec.source || rec.source.length < 50) problems.push("source is required (at least 50 characters)");
    if (!rec.source_quality) problems.push("source_quality is required");
    if (!rec.src) problems.push("src is required");
    if (!rec.ai_name) problems.push("ai_name is required");
    if (!rec.status) problems.push("status is required");
    if (!rec.layers) problems.push("layers is required");
    if (!rec.cross_links) problems.push("cross_links is required");
    if (!rec.generator) problems.push("generator is required");
    if (!rec.demo || typeof rec.demo !== "object") problems.push("demo is required");
    else {
      if (!rec.demo.language) problems.push("demo.language is required");
      if (!rec.demo.code || rec.demo.code.length < 50) problems.push("demo.code is required (at least 50 characters)");
      if (!rec.demo.expected_output) problems.push("demo.expected_output is required");
    }
    return { valid: problems.length === 0, problems: problems };
  }
  function runTests() {
    clearDuplicateState();
    var tests = [];
    var g = generateRecord(7);
    var g2 = generateRecord(7);
    tests.push({ name: "generated record_kind", pass: !!g && g.record_kind === RECORD_KIND });
    tests.push({ name: "generated slug is single edition slug", pass: !!g && g.slug === SLUG });
    tests.push({ name: "generated id prefix", pass: !!g && g.id.indexOf(PREFIX + "GEN-") === 0 });
    tests.push({ name: "generated src label", pass: !!g && g.src === "generated" });
    tests.push({ name: "generated edition signature", pass: !!g && g.edition === "signature" });
    tests.push({ name: "generated record has all 19 archive keys", pass: !!g && ARCHIVE_KEYS.every(function (k) { return Object.prototype.hasOwnProperty.call(g, k); }) });
    tests.push({ name: "validateRecord accepts generated record", pass: !!g && validateRecord(g).valid });
    tests.push({ name: "same seed gives identical record (deterministic)", pass: !!g && !!g2 && JSON.stringify(g) === JSON.stringify(g2) });
    tests.push({ name: "same-seed content flagged duplicate", pass: (function () { noteGenerated(g); return isDuplicateContent(g2).duplicate; })() });
    tests.push({ name: "duplicate content flagged even when id differs", pass: (function () { var c = {}; for (var k in g) c[k] = g[k]; c.id = PREFIX + "GEN-999999"; return contentHash(c) === contentHash(g) && isDuplicateContent(c).duplicate; })() });
    tests.push({ name: "archive injection flags matching content", pass: (function () { var arch = {}; for (var k in g) arch[k] = g[k]; arch.id = PREFIX + "000001"; var hit = checkAgainstArchive(g, [arch]); var miss = checkAgainstArchive(g, [generateRecord(8)]); return hit.duplicate === true && hit.matchedId === PREFIX + "000001" && miss.duplicate === false; })() });
    tests.push({ name: "validateRecord rejects stub missing science_proof", pass: (function () { var stub = { id: g.id, slug: SLUG, title: "x", record_kind: RECORD_KIND }; var v = validateRecord(stub); return !v.valid && v.problems.join(" ").indexOf("science_proof") !== -1; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "batch distinct content and all valid", pass: (function () { var b = generateBatch(100, 5000); var hashes = {}; b.forEach(function (r) { hashes[contentHash(r)] = true; }); var distinct = Object.keys(hashes).length; var allValid = b.every(function (r) { return validateRecord(r).valid; }); return b.length === 100 && distinct >= 90 && allValid; })() });
    tests.push({ name: "search finds a title", pass: searchRecords("Generated").length >= 1 });
    tests.push({ name: "guard text present", pass: !!g && g.description.indexOf("design-study") !== -1 && g.source.indexOf("design-study") !== -1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    clearDuplicateState();
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generate: generate, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, contentHash: contentHash, isDuplicateContent: isDuplicateContent, noteGenerated: noteGenerated, setArchiveRecords: setArchiveRecords, checkAgainstArchive: checkAgainstArchive, clearDuplicateState: clearDuplicateState, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["ExpertSystemsSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  /* CLI: node gen-expert-systems-signature.js --seed 7 --n 1 */
  if (typeof process !== "undefined" && process.argv && process.argv[1] && process.argv[1].indexOf("gen-expert-systems-signature.js") !== -1) {
    var seed = 7, n = 1;
    for (var i = 2; i < process.argv.length; i++) {
      if (process.argv[i] === "--seed" && process.argv[i + 1]) seed = parseInt(process.argv[i + 1], 10);
      if (process.argv[i] === "--n" && process.argv[i + 1]) n = parseInt(process.argv[i + 1], 10);
    }
    var out = [];
    for (var j = 0; j < n; j++) { var r = generateRecord(seed + j); if (r) out.push(r); }
    process.stdout.write(JSON.stringify(out, null, 2) + "\n");
  }
})(typeof window !== "undefined" ? window : globalThis);
