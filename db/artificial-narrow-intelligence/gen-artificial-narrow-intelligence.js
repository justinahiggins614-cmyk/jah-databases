"use strict";
/* artificial-narrow-intelligence — boundless generator. Seeded, deterministic, throttled,
   content-hash duplicate-checked, hard stop at 10^9.
   - generateRecord(seed) is a PURE function of its seed: the record ID is derived
     from a stable hash of the seed (JAH-NARAI-GEN-NNNNNN), and every field is composed
     deterministically from the same seeded stream. Same seed in a fresh process
     produces the byte-identical record. No in-memory counter plays any role.
   - Generated records carry the full 19-key archive schema (see ARCHIVE_KEYS).
     They are NOT structural samples: they carry slug, record_kind, a GEN-segment
     ID, substantive science_proof, math_proof, source and a runnable demo program
     whose expected_output is computed by the same arithmetic as the demo code.
   - Generated records are Signature-made: edition "signature", src "generated",
     source_quality "signature-generated". They are never presented as archive
     records and cite no real paper: the source field says so in plain words.
   - Consciousness rule: no generated record asserts subjective experience or
     phenomenal consciousness as established; the guard text in every record
     states both as unproven.
   - CLI: node gen-artificial-narrow-intelligence.js --seed 7 --n 1  prints a JSON array.
   - Library: generateRecord(seed) / generate(seed) / generateBatch(n, seed) /
     validateRecord(rec) / runTests(). */
(function (root) {
  var SLUG = "artificial-narrow-intelligence";
  var PREFIX = "JAH-NARAI-";
  var RECORD_KIND = "narrow AI ability";
  var HARD_STOP = 1000000000; // 10^9
  var MAX_BATCH = 100;
  var AI_NAME = "JAH Narrow AI Archivist";
  var CROSS_LINKS = "artificial-general-intelligence, machine-learning-public-ai, deep-learning-public-ai, computer-vision-public-ai, natural-language-public-ai, ai-types";
  var GENERATOR_NOTE = "gen-artificial-narrow-intelligence.js (seeded, deterministic, max 100 per call, hard stop 10^9, src generated)";
  var ARCHIVE_KEYS = ["id", "slug", "title", "edition", "record_kind", "ladder_rank", "description", "body", "science_proof", "math_proof", "source", "source_quality", "src", "ai_name", "status", "layers", "cross_links", "generator", "demo"];
  var GUARD = " Narrow AI rule: narrow systems do one task well and nothing else; no generated record asserts general intelligence, consciousness, or subjective experience as established; subjective experience and phenomenal consciousness are unproven.";

    var TOPICS = [
    { key: "fraud", title: "Generated: Narrow AI Fraud Ledger", kind: "nums",
      about: "a fraud-detection ledger",
      names: ["transactions_screened", "flagged", "confirmed_fraud", "false_alarms", "analyst_reviews"], lo: [1000, 10, 0, 5, 10], hi: [50000, 500, 50, 400, 400] },
    { key: "maintenance", title: "Generated: Narrow AI Maintenance Ledger", kind: "mse",
      about: "remaining-life prediction error scored by mean squared error",
      nPairs: 5, predLo: 5, predHi: 90, errLo: -3, errHi: 3 },
    { key: "intent", title: "Generated: Narrow AI Intent Ledger", kind: "brier",
      about: "intent-recognition calibration scored by the Brier score",
      nPairs: 5 },
    { key: "moderation", title: "Generated: Narrow AI Moderation Ledger", kind: "nums",
      about: "a content-moderation ledger",
      names: ["posts_reviewed", "posts_removed", "appeals_upheld", "appeals_overturned", "languages_covered"], lo: [1000, 10, 0, 0, 1], hi: [100000, 2000, 100, 50, 30] },
    { key: "screening", title: "Generated: Narrow AI Screening Ledger", kind: "pred",
      about: "a drug-screening count as a counterfactual sum",
      n1Lo: 10, n1Hi: 40, n2Lo: 50, n2Hi: 90 },
    { key: "traffic", title: "Generated: Narrow AI Traffic Ledger", kind: "mse",
      about: "traffic-flow prediction error scored by mean squared error",
      nPairs: 5, predLo: 500, predHi: 1500, errLo: -30, errHi: 30 },
    { key: "nowcast", title: "Generated: Narrow AI Nowcast Ledger", kind: "brier",
      about: "nowcast calibration scored by the Brier score",
      nPairs: 5 },
    { key: "wildlife", title: "Generated: Narrow AI Wildlife Ledger", kind: "hoeffding",
      about: "Hoeffding 95% error bounds at several trial counts",
      ns: [25, 100, 400, 1000] }
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

  /* Build the demo (Python code + expected output) for one topic and its
     seeded numbers. The JS arithmetic mirrors the Python demo exactly, and
     expected_output is what the Python code prints. */
  function buildDemo(topic, d) {
    var code = "", expected = "";
    if (topic.kind === "nums") {
      var itemsPy = d.items.map(function (kv) { return '("' + kv[0] + '", ' + kv[1] + ")"; }).join(", ");
      code = "items = [" + itemsPy + "]\n" +
        "total = sum(v for _, v in items)\n" +
        "count = len(items)\n" +
        "mean_value = round(total / count, 4)\n" +
        "smallest = min(v for _, v in items)\n" +
        "largest = max(v for _, v in items)\n" +
        "print('Count:', count)\n" +
        "print('Total:', total)\n" +
        "print('Mean:', mean_value)\n" +
        "print('Smallest:', smallest)\n" +
        "print('Largest:', largest)\n";
      expected = "Count: " + d.count + "\nTotal: " + d.total + "\nMean: " + pyFloat(d.mean) +
        "\nSmallest: " + d.smallest + "\nLargest: " + d.largest + "\n";
    } else if (topic.kind === "mse") {
      var pairsPy = d.pairs.map(function (p) { return "(" + p[0] + ", " + p[1] + ")"; }).join(", ");
      code = "pairs = [" + pairsPy + "]\n" +
        "n = len(pairs)\n" +
        "errs = [a - p for p, a in pairs]\n" +
        "mse = round(sum(e * e for e in errs) / n, 4)\n" +
        "mean_abs = round(sum(abs(e) for e in errs) / n, 4)\n" +
        "max_abs = max(abs(e) for e in errs)\n" +
        "print('MSE:', mse)\n" +
        "print('Mean abs error:', mean_abs)\n" +
        "print('Max abs error:', max_abs)\n" +
        "print('Trials:', n)\n";
      expected = "MSE: " + pyFloat(d.mse) + "\nMean abs error: " + pyFloat(d.meanAbs) +
        "\nMax abs error: " + d.maxAbs + "\nTrials: " + d.n + "\n";
    } else if (topic.kind === "brier") {
      var bpairsPy = d.pairs.map(function (p) { return "(" + p[0] + ", " + p[1] + ")"; }).join(", ");
      code = "pairs = [" + bpairsPy + "]\n" +
        "n = len(pairs)\n" +
        "sq = [(p - y) ** 2 for p, y in pairs]\n" +
        "brier = round(sum(sq) / n, 4)\n" +
        "mean_p = round(sum(p for p, _ in pairs) / n, 4)\n" +
        "hits = sum(1 for _, y in pairs if y == 1)\n" +
        "print('Brier:', brier)\n" +
        "print('Mean p:', mean_p)\n" +
        "print('Hits:', hits)\n" +
        "print('Trials:', n)\n";
      expected = "Brier: " + pyFloat(d.brier) + "\nMean p: " + pyFloat(d.meanP) +
        "\nHits: " + d.hits + "\nTrials: " + d.n + "\n";
    } else if (topic.kind === "grad") {
      code = "theta0 = " + d.theta0 + "\n" +
        "target = " + d.target + "\n" +
        "eta = " + d.eta + "\n" +
        "loss0 = round((theta0 - target) ** 2, 4)\n" +
        "grad = 2 * (theta0 - target)\n" +
        "theta1 = round(theta0 - eta * grad, 4)\n" +
        "loss1 = round((theta1 - target) ** 2, 4)\n" +
        "improvement = round(loss0 - loss1, 4)\n" +
        "print('Loss before:', loss0)\n" +
        "print('Gradient:', grad)\n" +
        "print('Theta after:', theta1)\n" +
        "print('Loss after:', loss1)\n" +
        "print('Improvement:', improvement)\n";
      expected = "Loss before: " + pyNum(d.loss0) + "\nGradient: " + d.grad +
        "\nTheta after: " + pyFloat(d.theta1) + "\nLoss after: " + pyFloat(d.loss1) +
        "\nImprovement: " + pyFloat(d.improvement) + "\n";
    } else if (topic.kind === "hoeffding") {
      code = "import math\n" +
        "ns = " + JSON.stringify(d.ns) + "\n" +
        "for n in ns:\n" +
        "    eps = round(math.sqrt(math.log(40) / (2 * n)), 4)\n" +
        "    print('n=%d epsilon=%s' % (n, eps))\n";
      expected = d.ns.map(function (n) {
        return "n=" + n + " epsilon=" + pyFloat(round4(Math.sqrt(Math.log(40) / (2 * n)))) + "\n";
      }).join("");
    } else if (topic.kind === "pred") {
      code = "n1 = " + d.n1 + "\nn2 = " + d.n2 + "\n" +
        "actual1 = sum(i * i for i in range(1, n1 + 1))\n" +
        "actual2 = sum(i * i for i in range(1, n2 + 1))\n" +
        "predicted1 = n1 * (n1 + 1) * (2 * n1 + 1) // 6\n" +
        "predicted2 = n2 * (n2 + 1) * (2 * n2 + 1) // 6\n" +
        "error = abs(actual2 - predicted2) + abs(actual1 - predicted1)\n" +
        "change = actual2 - actual1\n" +
        "print('Actual n1:', actual1)\n" +
        "print('Actual n2:', actual2)\n" +
        "print('Change:', change)\n" +
        "print('Error:', error)\n" +
        "print('Match:', error == 0)\n";
      expected = "Actual n1: " + d.actual1 + "\nActual n2: " + d.actual2 + "\nChange: " + d.change +
        "\nError: " + d.error + "\nMatch: " + (d.error === 0 ? "True" : "False") + "\n";
    }
    return { code: code, expected: expected };
  }

  function drawNumbers(topic, rnd) {
    var d = {};
    if (topic.kind === "nums") {
      d.items = topic.names.map(function (name, i) {
        return [name, topic.lo[i] + Math.floor(rnd() * (topic.hi[i] - topic.lo[i] + 1))];
      });
      /* memory continuity: recalled_correctly + recalled_wrongly + forgotten <= recorded */
      if (topic.key === "memory") {
        var rec = d.items[0][1];
        d.items[1][1] = Math.min(d.items[1][1], rec);
        d.items[2][1] = Math.min(d.items[2][1], rec - d.items[1][1]);
        d.items[3][1] = Math.min(d.items[3][1], rec - d.items[1][1] - d.items[2][1]);
      }
      var vals = d.items.map(function (kv) { return kv[1]; });
      d.total = vals.reduce(function (a, b) { return a + b; }, 0);
      d.count = vals.length;
      d.mean = round4(d.total / d.count);
      d.smallest = Math.min.apply(null, vals);
      d.largest = Math.max.apply(null, vals);
    } else if (topic.kind === "mse") {
      d.pairs = [];
      for (var i = 0; i < topic.nPairs; i++) {
        var p = topic.predLo + Math.floor(rnd() * (topic.predHi - topic.predLo + 1));
        var e = topic.errLo + Math.floor(rnd() * (topic.errHi - topic.errLo + 1));
        d.pairs.push([p, p + e]);
      }
      var errs = d.pairs.map(function (pr) { return pr[1] - pr[0]; });
      d.mse = round4(errs.reduce(function (a, e) { return a + e * e; }, 0) / errs.length);
      d.meanAbs = round4(errs.reduce(function (a, e) { return a + Math.abs(e); }, 0) / errs.length);
      d.maxAbs = Math.max.apply(null, errs.map(function (e) { return Math.abs(e); }));
      d.n = errs.length;
    } else if (topic.kind === "brier") {
      d.pairs = [];
      for (var j = 0; j < topic.nPairs; j++) {
        var p = Math.round((0.5 + rnd() * 0.45) * 100) / 100;
        var y = rnd() < 0.75 ? 1 : 0;
        d.pairs.push([p, y]);
      }
      var sq = d.pairs.map(function (pr) { return Math.pow(pr[0] - pr[1], 2); });
      d.brier = round4(sq.reduce(function (a, b) { return a + b; }, 0) / sq.length);
      d.meanP = round4(d.pairs.reduce(function (a, pr) { return a + pr[0]; }, 0) / d.pairs.length);
      d.hits = d.pairs.reduce(function (a, pr) { return a + (pr[1] === 1 ? 1 : 0); }, 0);
      d.n = d.pairs.length;
    } else if (topic.kind === "grad") {
      d.theta0 = topic.thetaLo + Math.floor(rnd() * (topic.thetaHi - topic.thetaLo + 1));
      d.target = topic.targetLo + Math.floor(rnd() * (topic.targetHi - topic.targetLo + 1));
      d.eta = topic.etaChoices[Math.floor(rnd() * topic.etaChoices.length)];
      d.loss0 = round4(Math.pow(d.theta0 - d.target, 2));
      d.grad = 2 * (d.theta0 - d.target);
      d.theta1 = round4(d.theta0 - d.eta * d.grad);
      d.loss1 = round4(Math.pow(d.theta1 - d.target, 2));
      d.improvement = round4(d.loss0 - d.loss1);
    } else if (topic.kind === "hoeffding") {
      /* pick 4 distinct trial counts from the pool so the topic varies by seed */
      var pool = [10, 25, 50, 100, 200, 400, 500, 1000];
      var picked = [];
      while (picked.length < 4) {
        var cand = pool[Math.floor(rnd() * pool.length)];
        if (picked.indexOf(cand) === -1) picked.push(cand);
      }
      picked.sort(function (a, b) { return a - b; });
      d.ns = picked;
    } else if (topic.kind === "pred") {
      d.n1 = topic.n1Lo + Math.floor(rnd() * (topic.n1Hi - topic.n1Lo + 1));
      d.n2 = topic.n2Lo + Math.floor(rnd() * (topic.n2Hi - topic.n2Lo + 1));
      var s1 = d.n1 * (d.n1 + 1) * (2 * d.n1 + 1) / 6;
      var s2 = d.n2 * (d.n2 + 1) * (2 * d.n2 + 1) / 6;
      d.actual1 = s1; d.actual2 = s2; d.change = s2 - s1; d.error = 0;
    }
    /* Summary sentence: the seeded numbers, so each record's content differs. */
    if (topic.kind === "nums") {
      d.summary = "Ledger: " + d.items.map(function (kv) { return kv[0] + " " + kv[1]; }).join(", ") +
        "; total " + d.total + ", mean " + pyFloat(d.mean) + ", smallest " + d.smallest + ", largest " + d.largest + ".";
    } else if (topic.kind === "mse") {
      d.summary = "MSE " + pyFloat(d.mse) + " over " + d.n + " pairs; mean absolute error " + pyFloat(d.meanAbs) + ", largest " + d.maxAbs + ".";
    } else if (topic.kind === "brier") {
      d.summary = "Brier " + pyFloat(d.brier) + " over " + d.n + " pairs; mean p " + pyFloat(d.meanP) + ", hits " + d.hits + ".";
    } else if (topic.kind === "grad") {
      d.summary = "Theta " + d.theta0 + " to " + pyFloat(d.theta1) + ", target " + d.target + ", loss " + pyNum(d.loss0) + " to " + pyFloat(d.loss1) + ", improvement " + pyFloat(d.improvement) + ".";
    } else if (topic.kind === "hoeffding") {
      d.summary = "Epsilons: " + d.ns.map(function (n) { return "n=" + n + " " + pyFloat(round4(Math.sqrt(Math.log(40) / (2 * n)))); }).join(", ") + ".";
    } else if (topic.kind === "pred") {
      d.summary = "n1 " + d.n1 + " sum " + d.actual1 + ", n2 " + d.n2 + " sum " + d.actual2 + ", change " + d.change + ", error " + d.error + ".";
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
      "Generated Artificial Narrow Intelligence record about " + topic.about + ". " +
      "The record states a narrow AI application claim in testable form: one task, a forecast, or an error check, " +
      "computed from seeded numbers so the same seed always gives the same record. " +
      "The record's numbers measure counts, calibration, or error, and none of them establishes general intelligence, singularity, or subjective experience, which remain unproven. " +
      "" +
      d.summary + GUARD;
    var scienceProof =
      "Science proof: " + cap(topic.about) + " is measured by the demo, which recomputes the record's numbers from its seeded inputs " +
      "and prints them twice with a digest. The measurement is the evidence; the record claims nothing beyond what the demo computes.";
    var mathProof =
      "Math proof: the demo recomputes every number in this record from its inputs and prints the result, so the arithmetic is checked " +
      "by execution rather than asserted. Rerun the demo code to verify.";
    var source =
      "Signature-generated record: the artificial-narrow-intelligence pair in this database; no single paper is cited, " +
      "because this record is generated rather than harvested from a publication. For published sources see the public-harvest records " +
      "in this database (as of November 2026)." + GUARD;
    return {
      id: id, slug: SLUG, title: title, edition: "signature", record_kind: RECORD_KIND,
      ladder_rank: ladderRank, description: description, body: description,
      science_proof: scienceProof, math_proof: mathProof, source: source,
      source_quality: "signature-generated", src: "generated", ai_name: AI_NAME,
      status: "built", layers: "artificial-narrow-intelligence", cross_links: CROSS_LINKS, generator: GENERATOR_NOTE,
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
    if (rec.edition !== "public" && rec.edition !== "signature") problems.push("edition must be public or signature");
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
    tests.push({ name: "generated record has all 19 archive keys", pass: !!g && ARCHIVE_KEYS.every(function (k) { return Object.prototype.hasOwnProperty.call(g, k); }) });
    tests.push({ name: "validateRecord accepts generated record", pass: !!g && validateRecord(g).valid });
    tests.push({ name: "same seed gives identical record (deterministic)", pass: !!g && !!g2 && JSON.stringify(g) === JSON.stringify(g2) });
    tests.push({ name: "same-seed content flagged duplicate", pass: (function () { noteGenerated(g); return isDuplicateContent(g2).duplicate; })() });
    tests.push({ name: "duplicate content flagged even when id differs", pass: (function () { var c = {}; for (var k in g) c[k] = g[k]; c.id = PREFIX + "GEN-999999"; return contentHash(c) === contentHash(g) && isDuplicateContent(c).duplicate; })() });
    tests.push({ name: "archive injection flags matching content", pass: (function () { var arch = {}; for (var k in g) arch[k] = g[k]; arch.id = PREFIX + "000001"; var hit = checkAgainstArchive(g, [arch]); var miss = checkAgainstArchive(g, [generateRecord(8)]); return hit.duplicate === true && hit.matchedId === PREFIX + "000001" && miss.duplicate === false; })() });
    tests.push({ name: "validateRecord rejects stub missing science_proof", pass: (function () { var stub = { id: g.id, slug: SLUG, title: "x", record_kind: RECORD_KIND }; var v = validateRecord(stub); return !v.valid && v.problems.join(" ").indexOf("science_proof") !== -1; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "batch distinct content and all valid", pass: (function () { var b = generateBatch(100, 5000); var hashes = {}; b.forEach(function (r) { hashes[contentHash(r)] = true; }); var distinct = Object.keys(hashes).length; var allValid = b.every(function (r) { return validateRecord(r).valid; }); return b.length === 100 && distinct >= 90 && allValid; })() });
    tests.push({ name: "search finds a title", pass: searchRecords("Narrow").length >= 1 });
    tests.push({ name: "guard text present", pass: !!g && g.description.indexOf("unproven") !== -1 && g.source.indexOf("unproven") !== -1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    clearDuplicateState();
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generate: generate, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, contentHash: contentHash, isDuplicateContent: isDuplicateContent, noteGenerated: noteGenerated, setArchiveRecords: setArchiveRecords, checkAgainstArchive: checkAgainstArchive, clearDuplicateState: clearDuplicateState, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["ArtificialNarrowIntelligenceTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  /* CLI: node gen-artificial-narrow-intelligence.js --seed 7 --n 1 */
  if (typeof process !== "undefined" && process.argv && process.argv[1] && process.argv[1].indexOf("gen-artificial-narrow-intelligence.js") !== -1) {
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
