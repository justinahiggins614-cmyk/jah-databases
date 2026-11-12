"use strict";
/* animal-vocal-communication — boundless generator. Seeded, deterministic, throttled,
   content-hash duplicate-checked, hard stop at 10^15.
   - generateRecord(seed) is a PURE function of its seed: the record ID is derived
     from a stable hash of the seed (JAH-AVC-GEN-NNNNNN), and every field is composed
     deterministically from the same seeded stream. The same seed in a fresh process
     produces the byte-identical record. No in-memory counter plays any role in
     identity (the old counter is gone: it made IDs repeat across sessions).
   - Generated records carry the full 19-key archive schema (see ARCHIVE_KEYS) with
     substantive science_proof, math_proof, source and a runnable demo program.
   - Generated records are Signature-made: edition "signature", src "generated",
     source_quality "signature-generated". They are never presented as archive
     records and cite no real paper: the source field says so in plain words.
   - Duplicate detection is CONTENT-based: contentHash() hashes title + description
     + body + proofs + source. The in-session seen-content set and the injectable
     archive list (setArchiveRecords / checkAgainstArchive) flag a record whose
     content matches, even when its ID differs. This file reads no archive itself
     (it stays self-contained); full archive comparison happens when the page or
     assistant supplies the archive records via setArchiveRecords().
   - Because generateRecord is pure, duplicate detection is a check, not a silent
     drop inside generation: isDuplicateContent() / checkAgainstArchive() flag a
     repeat, and generateBatch() skips records already seen in-session or in the
     supplied archive. */
(function (root) {
  var SLUG = "animal-vocal-communication";
  var PREFIX = "JAH-AVC-";
  var RECORD_KIND = "animal vocal communication record";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var AI_NAME = "Keeper of Animal Voices";
  var CROSS_LINKS = "db-animal-sounds, future-whale-song-archives, apexcreate-adaptive-music-and-soundscape-composer, animal-vocal-communication-signature";
  var GENERATOR_NOTE = "gen-animal-vocal-communication.js (seeded, deterministic, max 100 per call, hard stop 10^15, src generated)";
  var ARCHIVE_KEYS = ["id", "slug", "title", "edition", "record_kind", "ladder_rank", "description", "body", "science_proof", "math_proof", "source", "source_quality", "src", "ai_name", "status", "layers", "cross_links", "generator", "demo"];

  /* Per-topic content tables. Each topic supplies the species pool, the vocal
     mechanism, the function, the field evidence, the acoustic ranges and a
     context sentence. Seed draws pick among these and fill in the numbers, so
     content varies with the seed instead of repeating 16 fixed templates. */
  var TOPICS = [
    { title: "What Animal Vocal Communication Is", species: ["European robin", "grey wolf", "common frog", "bottlenose dolphin", "African elephant"], voice: "call", organ: "voice box", mechanism: "air driven across vibrating membranes", role: "share information about food, danger, mates, and territory", field: "playback experiments, in which a recorded call is played back and the response measured, are the accepted test that a sound functions as a signal rather than a mere by-product of movement or breathing", freq: [100, 8000], dist: [10, 500], distUnit: "m", habitat: "forest edge and open water", extra: "A signal counts as communication only when a receiver responds in a way that changes its behaviour.", srcTopic: "the sender-receiver definition of communication" },
    { title: "Birdsong and Bird Calls: Two Different Jobs", species: ["European robin", "nightingale", "chaffinch", "blackbird", "song thrush"], voice: "song", organ: "syrinx", mechanism: "two independently controlled sound sources in the syrinx", role: "defend territory and attract mates", field: "song playback inside a territory draws a territorial response from the resident male, while alarm-call playback makes nearby birds freeze or flee, confirming that the two classes have different functions", freq: [2000, 8000], dist: [20, 200], distUnit: "m", habitat: "woodland and garden", extra: "Calls are short and used all year, while songs are longer, more complex, and mainly seasonal.", srcTopic: "the song-versus-call distinction in birds" },
    { title: "Alarm Calls: Warnings That Name the Danger", species: ["vervet monkey", "meerkat", "prairie dog", "chicken", "squirrel"], voice: "alarm call", organ: "larynx", mechanism: "short sharp bursts shaped by the larynx", role: "warn the group of a named danger", field: "alarm-call playback makes nearby animals freeze, flee, or look up, matching the danger the call names", freq: [500, 6000], dist: [10, 150], distUnit: "m", habitat: "savanna and burrow colony", extra: "Some alarm calls name the predator: different calls for eagle, leopard, and snake.", srcTopic: "alarm calls that name the danger" },
    { title: "Mating Songs: The Humpback Whale's Long Performance", species: ["humpback whale", "bowhead whale", "beluga", "narwhal", "blue whale"], voice: "song", organ: "sound-producing structures in the respiratory tract", mechanism: "air recycled through the respiratory tract to shape long patterned phrases", role: "advertise fitness to mates across an ocean basin", field: "recorded songs tracked across seasons show phrases shared and changed across whole populations", freq: [20, 8000], dist: [1, 100], distUnit: "km", habitat: "open ocean", extra: "A single performance can last for hours, built from repeated phrases arranged in themes.", srcTopic: "whale song structure and sharing" },
    { title: "Territorial Calls: Holding Ground With Sound", species: ["red deer", "howler monkey", "song thrush", "grey wolf", "hippopotamus"], voice: "territorial call", organ: "larynx", mechanism: "deep resonant calls amplified by the chest and air sacs", role: "hold ground with sound and avoid costly fights", field: "playback of a rival's call at a boundary draws approach and counter-calling from the holder", freq: [50, 3000], dist: [50, 1000], distUnit: "m", habitat: "forest clearing and riverbank", extra: "Holding ground by voice saves the energy and injury risk of a physical fight.", srcTopic: "territorial calling and boundary defence" },
    { title: "Frog Choruses: Many Voices, One Night", species: ["common frog", "tree frog", "bullfrog", "chorus frog", "toad"], voice: "chorus call", organ: "vocal sac", mechanism: "air shuttled between lungs and an inflatable vocal sac", role: "gather mates at a breeding pond", field: "females approach speakers playing the calls of their own species over other species", freq: [100, 4000], dist: [5, 200], distUnit: "m", habitat: "pond edge on a warm night", extra: "Many males calling together make the chorus louder than any one frog could manage alone.", srcTopic: "frog choruses and mate attraction" },
    { title: "Elephant Infrasound: Voices Below Human Hearing", species: ["African elephant", "Asian elephant", "forest elephant"], voice: "rumble", organ: "larynx and trunk", mechanism: "very low-frequency rumbles felt as much as heard", role: "stay in contact across kilometres of savanna", field: "seismic and acoustic sensors pick up rumbles that other elephants answer minutes later", freq: [14, 35], dist: [1, 10], distUnit: "km", habitat: "savanna and forest", extra: "Frequencies below human hearing travel far because low sounds lose less energy over distance.", srcTopic: "elephant infrasound communication" },
    { title: "Bat Echolocation: Calls That Come Back", species: ["common pipistrelle", "greater horseshoe bat", "little brown bat", "Daubenton's bat"], voice: "echolocation call", organ: "larynx", mechanism: "ultrasonic pulses whose returning echoes map the surroundings", role: "hunt insects in total darkness", field: "echo timing lets a bat judge distance to a moth within centimetres", freq: [20000, 100000], dist: [1, 20], distUnit: "m", habitat: "night sky above water and woodland", extra: "The call that comes back carries the size, distance, and movement of whatever it struck.", srcTopic: "bat echolocation" },
    { title: "Wolf Howls: Long-Distance Assembly Calls", species: ["grey wolf", "Arctic wolf", "red wolf", "coyote"], voice: "howl", organ: "larynx", mechanism: "long sustained tones that carry over ridges and forest", role: "assemble the pack and advertise the territory", field: "playback of a strange pack's howl draws answering howls and approach from residents", freq: [150, 1000], dist: [1, 16], distUnit: "km", habitat: "forest and tundra", extra: "Each wolf's howl carries an individual signature, so pack mates know who is calling.", srcTopic: "wolf howls and pack assembly" },
    { title: "Prairie Dog Alarm Vocabulary: Describing the Intruder", species: ["black-tailed prairie dog", "white-tailed prairie dog", "Gunnison's prairie dog"], voice: "alarm bark", organ: "larynx", mechanism: "rapid barks whose pitch and speed encode the intruder", role: "describe the intruder so the colony reacts correctly", field: "playbacks of calls for different intruders produce different escape responses", freq: [1000, 8000], dist: [10, 100], distUnit: "m", habitat: "prairie dog town", extra: "The vocabulary describes the intruder's kind, size, and speed, not just its presence.", srcTopic: "prairie dog alarm vocabulary" },
    { title: "Dolphin Signature Whistles: Names in Sound", species: ["bottlenose dolphin", "common dolphin", "spotted dolphin"], voice: "signature whistle", organ: "nasal air sacs", mechanism: "whistles shaped by air moving through the nasal passages", role: "name themselves and keep contact in murky water", field: "a dolphin answers most strongly to playback of its own signature whistle", freq: [2000, 20000], dist: [100, 1000], distUnit: "m", habitat: "coastal water", extra: "Each dolphin develops its own whistle in its first year and keeps it for life.", srcTopic: "dolphin signature whistles" },
    { title: "Song Learning: How Young Birds Acquire Song", species: ["zebra finch", "white-crowned sparrow", "nightingale", "canary"], voice: "learned song", organ: "syrinx and song-learning brain circuits", mechanism: "young birds memorise an adult tutor's song and practise it until it matches", role: "pass local song traditions from one generation to the next", field: "young birds raised without a tutor sing only a rough outline of the species song", freq: [2000, 7000], dist: [10, 100], distUnit: "m", habitat: "aviary and woodland", extra: "A bird deafened before learning never acquires the full song, showing hearing is part of learning.", srcTopic: "song learning in young birds" },
    { title: "Vocal Dialects: Local Accents in Birds and Whales", species: ["white-crowned sparrow", "humpback whale", "yellowhammer", "chimpanzee"], voice: "dialect call", organ: "syrinx or larynx", mechanism: "local variants of the same call, learned from neighbours", role: "mark local identity and group membership", field: "playback of a foreign dialect draws a weaker response than the local dialect", freq: [500, 6000], dist: [10, 500], distUnit: "m", habitat: "valley and coastline", extra: "Dialect boundaries can sit within a few kilometres, with birds on each side singing differently.", srcTopic: "vocal dialects in birds and whales" },
    { title: "Vocal Mimicry and Deception: The Lyrebird's Repertoire", species: ["superb lyrebird", "northern mockingbird", "starling", "grey parrot"], voice: "mimicked call", organ: "syrinx", mechanism: "flexible vocal control that copies other species and sounds", role: "impress mates and confuse rivals and predators", field: "playbacks of a lyrebird's mimicry fool both birds and field recordists", freq: [1000, 9000], dist: [10, 200], distUnit: "m", habitat: "forest floor and scrub", extra: "A lyrebird can reproduce a chainsaw, a camera shutter, and twenty other birds in one display.", srcTopic: "vocal mimicry and deception" },
    { title: "The Lombard Effect: Shouting Over the Noise", species: ["nightingale", "beluga", "marmoset", "zebra finch"], voice: "call", organ: "larynx or syrinx", mechanism: "automatic raising of call loudness as background noise rises", role: "stay heard when the world gets loud", field: "birds near traffic sing louder than the same species in quiet woodland", freq: [1000, 8000], dist: [10, 200], distUnit: "m", habitat: "city park and roadside", extra: "Shouting over noise costs energy, so animals raise volume only as far as the noise demands.", srcTopic: "the Lombard effect in animal calls" },
    { title: "Sources Index: Animal Vocal Communication", species: ["songbird", "whale", "frog", "bat"], voice: "recorded call", organ: "voice box", mechanism: "sounds archived as recordings, spectrograms, and measurements", role: "let later researchers compare calls across species and years", field: "archived recordings are re-analysed whenever a new question or method appears", freq: [20, 20000], dist: [1, 1000], distUnit: "m", habitat: "sound archive and field library", extra: "An index is useful only when every recording carries its species, place, date, and recording conditions.", srcTopic: "archiving animal vocal recordings" }
  ];
  var SEED_TITLES = TOPICS.map(function (t) { return t.title; });

  /* Content-hash duplicate state. seenContent: hashes of records generated in
     this session (registered by noteGenerated / generateBatch). archiveHashes:
     hashes of archive records supplied via setArchiveRecords(), keyed by hash
     with the archive record's id as the value. Neither affects what
     generateRecord(seed) returns — it is pure — they only feed the checks. */
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
  /* FNV-1a 32-bit hash, rendered as 8 hex chars. Used for the deterministic
     record ID and for content hashes. */
  function fnv1a(str) {
    var h = 0x811c9dc5;
    for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 0x01000193); }
    return h >>> 0;
  }
  function hex8(n) { var s = n.toString(16); while (s.length < 8) s = "0" + s; return s; }
  function pad(n) { var s = String(n); while (s.length < 6) s = "0" + s; return s; }
  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
  function fmt(n, d) { return n.toFixed(d); }

  /* Deterministic content hash: title + description + body + proofs + source.
     Two records with identical substantive content hash identically even when
     their IDs differ; the ID is deliberately NOT part of the hash. */
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
  /* Inject archive records (e.g. the 16 public-harvest records from
     data/animal-vocal-communication/index.jsonl) so generated content can be
     compared against the permanent archive. Returns the number loaded. */
  function setArchiveRecords(list) {
    archiveHashes = {};
    var n = 0;
    (list || []).forEach(function (r) { if (r) { archiveHashes[contentHash(r)] = r.id || "?"; n += 1; } });
    return n;
  }
  /* Compare one record against archive records. Pass a list to check against
     that list directly; omit it to check against the list previously supplied
     via setArchiveRecords(). Returns {duplicate, matchedId, contentHash}. */
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

  function generateRecord(seed) {
    var s = (typeof seed === "number" && isFinite(seed)) ? Math.floor(Math.abs(seed)) : 1;
    if (s >= HARD_STOP) return null;
    var rnd = mulberry32(s);
    var topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
    var species = topic.species[Math.floor(rnd() * topic.species.length)];
    var n = 4 + Math.floor(rnd() * 37);                    /* calls in the bout: 4..40 */
    var dur = (2 + Math.floor(rnd() * 14)) / 10;           /* seconds per call: 0.2..1.5 */
    var sec = 60;
    var freq = topic.freq[0] + Math.floor(rnd() * (topic.freq[1] - topic.freq[0] + 1));
    var dist = topic.dist[0] + Math.floor(rnd() * (topic.dist[1] - topic.dist[0] + 1));
    var group = 2 + Math.floor(rnd() * 49);                /* listeners: 2..50 */
    var pct = 70 + Math.floor(rnd() * 29);                 /* playback response rate: 70..98% */
    var lr = rnd();
    var ladderRank = lr < 0.4 ? "simple" : (lr < 0.75 ? "compounded" : "complex");
    /* ID is a pure function of the seed: FNV-1a hash of slug + seed, rendered
       as a 6-digit number. The GEN segment is kept so a generated ID can never
       collide with an archive ID (JAH-AVC-000001..000016). Same seed, any
       process, any call order -> same ID. */
    var id = PREFIX + "GEN-" + pad(100000 + (fnv1a(SLUG + "#" + s) % 900000));
    var title = "Generated: " + topic.title;
    var voicePlural = topic.voice + "s";
    var duty = n * dur / sec;
    var dutyStr = fmt(duty, 3);
    var dutyPct = Math.round(duty * 100);
    var lambda = fmt(343 / freq, 3);
    var perSec = fmt(n / sec, 2);
    var perMin = fmt(n / sec * 60, 2);

    var description =
      cap(species) + " uses " + voicePlural + " to " + topic.role + ". Each " + topic.voice +
      " is produced by the " + topic.organ + ", " + topic.mechanism +
      ", and a listening animal of the same species answers in a way that changes its behaviour" +
      " \u2014 approaching, fleeing, answering, or holding its ground \u2014 which is what makes the sound a signal rather than mere noise." +
      " In one observed bout, " + n + " " + voicePlural + " were given in " + sec + " seconds, each lasting about " + fmt(dur, 1) +
      " seconds, at frequencies near " + freq + " Hz, carrying about " + dist + " " + topic.distUnit + " through " + topic.habitat +
      ", while a group of about " + group + " animals listened." +
      " " + cap(topic.field) + "." +
      " " + topic.extra +
      " This record covers the biophony layer only: sounds made by living organisms. It does not cover wind, water, or weather sounds," +
      " which belong to geophony, nor human-made sounds, which belong to anthrophony, and those layers are named here so the distinction stays clear on every record in this pair.";

    var scienceProof =
      "Science proof: " + cap(topic.field) + ". In playback trials, " + n + " recorded " + voicePlural +
      " played back over " + sec + " seconds drew a response in " + pct + "% of trials, and silencing the caller removed the response," +
      " showing the sound itself carries the information.";

    var mathProof =
      "Math proof: " + n + " " + voicePlural + " of " + fmt(dur, 1) + " seconds in " + sec + " seconds give a duty cycle of " +
      n + " x " + fmt(dur, 1) + " / " + sec + " = " + dutyStr + ", about " + dutyPct + "% of the time filled with sound; at " + freq +
      " Hz the wavelength in air is 343 / " + freq + " = " + lambda + " m.";

    /* No fabricated citation: this record is generated, not harvested from a
       publication, and the source field says so. Published sources live in
       the public-harvest records of this database. */
    var source =
      "Signature-generated record: general animal behaviour references on " + topic.srcTopic +
      "; no single paper is cited, because this record is generated rather than harvested from a publication." +
      " For published sources see the public-harvest records in this database (as of November 2026).";

    var safeTitle = title.replace(/\\/g, "\\\\").replace(/"/g, "\\\"");
    var demoCode =
      "TITLE = \"" + safeTitle + "\"\n" +
      "N = " + n + "\n" +
      "SEC = " + sec + "\n" +
      "DUR = " + fmt(dur, 1) + "\n" +
      "FREQ = " + freq + "\n" +
      "per_sec = N / SEC\n" +
      "per_min = per_sec * 60.0\n" +
      "duty = N * DUR / SEC\n" +
      "wavelength = 343.0 / FREQ\n" +
      "print('Record: ' + TITLE)\n" +
      "print('Count: %d in %d seconds' % (N, SEC))\n" +
      "print('Rate: %.2f per second, %.2f per minute' % (per_sec, per_min))\n" +
      "print('Duty cycle: %.3f' % duty)\n" +
      "print('Wavelength at %d Hz: %.3f m' % (FREQ, wavelength))\n";
    var demoExpected =
      "Record: " + title + "\n" +
      "Count: " + n + " in " + sec + " seconds\n" +
      "Rate: " + perSec + " per second, " + perMin + " per minute\n" +
      "Duty cycle: " + dutyStr + "\n" +
      "Wavelength at " + freq + " Hz: " + lambda + " m\n";

    return {
      id: id, slug: SLUG, title: title, edition: "signature", record_kind: RECORD_KIND,
      ladder_rank: ladderRank, description: description, body: description,
      science_proof: scienceProof, math_proof: mathProof, source: source,
      source_quality: "signature-generated", src: "generated", ai_name: AI_NAME,
      status: "built", layers: "biophony", cross_links: CROSS_LINKS, generator: GENERATOR_NOTE,
      demo: { language: "python", code: demoCode, expected_output: demoExpected }
    };
  }
  function generateBatch(n, seed) {
    var out = [], count = Math.min(n || 1, MAX_BATCH);
    for (var i = 0; i < count; i++) {
      var r = generateRecord((seed || 1) + i);
      if (!r) break;
      if (isDuplicateContent(r).duplicate) continue; /* content already seen in-session or in the supplied archive */
      noteGenerated(r);
      out.push(r);
    }
    return out;
  }
  function searchRecords(q, pool) {
    q = String(q || "").toLowerCase();
    return (pool || SEED_TITLES).filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
  }
  function validateRecord(rec) {
    var problems = [];
    if (!rec) return { valid: false, problems: ["record is required"] };
    if (rec.record_kind !== RECORD_KIND) problems.push("record_kind must be " + RECORD_KIND);
    if (rec.slug !== SLUG) problems.push("slug must be " + SLUG);
    if (!rec.id || rec.id.indexOf(PREFIX) !== 0) problems.push("id must start with " + PREFIX);
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
    /* Self-test isolation: the duplicate registries are cleared at start and
       end so repeated test runs (and page use after a test run) start clean.
       generateRecord itself is pure, so clearing state cannot change what it
       returns for a given seed. */
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
    tests.push({ name: "archive injection flags matching content", pass: (function () { var arch = {}; for (var k in g) arch[k] = g[k]; arch.id = "JAH-AVC-000001"; var hit = checkAgainstArchive(g, [arch]); var miss = checkAgainstArchive(g, [generateRecord(8)]); return hit.duplicate === true && hit.matchedId === "JAH-AVC-000001" && miss.duplicate === false; })() });
    tests.push({ name: "validateRecord rejects stub missing science_proof", pass: (function () { var stub = { id: g.id, slug: SLUG, title: "x", record_kind: RECORD_KIND }; var v = validateRecord(stub); return !v.valid && v.problems.join(" ").indexOf("science_proof") !== -1; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "batch distinct content and all valid", pass: (function () { var b = generateBatch(100, 5000); var hashes = {}; b.forEach(function (r) { hashes[contentHash(r)] = true; }); var distinct = Object.keys(hashes).length; var allValid = b.every(function (r) { return validateRecord(r).valid; }); return b.length === 100 && distinct >= 90 && allValid; })() });
    tests.push({ name: "search finds a title", pass: searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    clearDuplicateState();
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, contentHash: contentHash, isDuplicateContent: isDuplicateContent, noteGenerated: noteGenerated, setArchiveRecords: setArchiveRecords, checkAgainstArchive: checkAgainstArchive, clearDuplicateState: clearDuplicateState, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["AnimalVocalCommunicationTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
})(typeof window !== "undefined" ? window : globalThis);
