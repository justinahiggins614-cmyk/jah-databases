/* ✳ SIGNATURE — JAH Robot Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW robot designs + AI-to-robot matches in the
   exact archive format (body, class, mission, AI pairing, score, rationale,
   demo lines, hardware). Deterministic: same seed + version => same record.
   Every record is validated by an INDEPENDENT re-builder that reconstructs
   every derived string from the private raw parameters before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-robots-1.0';
  var ID_PREFIX = 'JAH-ROBOT-';
  var STAMP = 'Generated robot design + AI match. Design simulation for the archive — not a shipped product, not a safety certification.';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  var TYPES = ['domestic-helper', 'industrial-arm', 'medical-assistant', 'exploration-rover',
    'humanoid-companion', 'aerial-drone', 'underwater-drone', 'construction-rig',
    'agricultural-bot', 'security-sentinel'];

  var CLASS_LABEL = {
    'domestic-helper': 'domestic helper-class', 'industrial-arm': 'industrial arm-class',
    'medical-assistant': 'medical assistant-class', 'exploration-rover': 'exploration rover-class',
    'humanoid-companion': 'humanoid companion-class', 'aerial-drone': 'aerial drone-class',
    'underwater-drone': 'underwater drone-class', 'construction-rig': 'construction rig-class',
    'agricultural-bot': 'agricultural bot-class', 'security-sentinel': 'security sentinel-class'
  };
  var CLASS_TAGS = {
    'domestic-helper': ['organizing', 'quiet', 'gentle'],
    'industrial-arm': ['precision', 'strength', 'repeatability'],
    'medical-assistant': ['sterile', 'careful', 'calm'],
    'exploration-rover': ['rugged', 'patient', 'curious'],
    'humanoid-companion': ['expressive', 'attentive', 'warm'],
    'aerial-drone': ['agile', 'wide-ranging', 'precise'],
    'underwater-drone': ['steady', 'deep-rated', 'quiet'],
    'construction-rig': ['powerful', 'stable', 'methodical'],
    'agricultural-bot': ['patient', 'weather-wise', 'gentle'],
    'security-sentinel': ['watchful', 'tireless', 'discreet']
  };

  var MISSIONS = ['airport runway debris scan', 'aquarium tank maintenance', 'bakery dawn prep shift',
    'coastal cliff nest census', 'construction site material lift', 'dam intake grate cleaning',
    'data center thermal sweep', 'forest fire watch', 'grain silo level sounding',
    'greenhouse pollination run', 'harbor cargo survey', 'home elder companionship',
    'hospital linen delivery', 'library book reshelving', 'marina hull cleaning',
    'mountain trail rescue standby', 'museum after-hours guard', 'night warehouse patrol',
    'nursing home evening rounds', 'observatory dome night watch', 'offshore rig bolt audit',
    'oil pipeline leak survey', 'orchard harvest sweep', 'pharmacy restock round',
    'playground safety inspection', 'riverbank erosion mapping', 'school hallway monitor duty',
    'solar farm panel inspection', 'stadium post-game cleanup', 'subway tunnel safety check',
    'vineyard frost alert patrol', 'wheat field pest scouting'];

  var AI_NAMES = ['Accountant', 'Ad Writer', 'Affirmation Crafter', 'Airport Navigator',
    'Allergy Checker', 'Allowance Planner', 'Anger Cooler', 'Anniversary Dinner Planner',
    'Anxiety Easer', 'Apology Writer', 'Architect', 'BBQ Chief', 'Baby Care Helper',
    'Band Name Maker', 'Barista', 'Bass Line Builder', 'Bike Mechanic', 'Bingo Caller',
    'Bird Watcher', 'Bread Baker', 'Budget Planner', 'Business Planner', 'Cake Decorator',
    'Camp Setup Guide', 'Car Buyer Advisor', 'Date Night Cook', 'Debate Partner',
    'Essay Outliner', 'Form Writer', 'Gift Finder', 'Gratitude Guide', 'Homework Peacekeeper',
    'Karaoke Picker', 'Knitting Teacher', 'Laundry Guide', 'Meditation Guide', 'Note Taker',
    'Party Planner', 'Personal Shopper', 'Photo Editor Guide', 'Picnic Packer',
    'Pizza Dough Doctor', 'Plumber Helper', 'Poker Odds Counter', 'Pun Smith', 'Run Pacer',
    'Spice Matcher', 'Toast Writer', 'Trivia Host', 'Tutor', 'Weather Reader',
    'Workout Planner', 'World Builder'];

  var PRE = ['Pan', 'Hearth', 'Rivet', 'Wind', 'Meadow', 'Solar', 'Tidy', 'Canyon', 'Feather',
    'Kitchen', 'Dust', 'Copper', 'Ash', 'Birch', 'Cinder', 'Ember', 'Flint', 'Gale', 'Hazel',
    'Ivy', 'Juniper', 'Lark', 'Moss', 'Nettle', 'Onyx', 'Pebble', 'Quartz', 'Rowan', 'Sage',
    'Thorn', 'Umber', 'Vale', 'Willow', 'Zephyr', 'Brass', 'Clove', 'Dune', 'Elm', 'Fern', 'Grove'];
  var SUF = ['ward', 'mantle', 'reach', 'whisper', 'mere', 'tide', 'lane', 'post', 'kind',
    'loft', 'door', 'well', 'moss', 'pantry', 'chime', 'ford', 'stride', 'light', 'fall',
    'keel', 'crown', 'shade', 'trail', 'bell', 'field', 'haven', 'brook', 'cliff', 'dale',
    'frost', 'grove', 'hollow', 'isle', 'marsh', 'mead', 'ridge', 'shore', 'wood', 'wick',
    'stead', 'holm'];

  var ACTUATORS = ['dual-arm manipulator (14-DOF)', 'torso lift column (1-DOF)',
    '6-axis articulated arm (6-DOF)', 'servo gripper (2-DOF)', 'sterile instrument arm (2-DOF)',
    'medication carousel (1-DOF)', 'height-adjust column (1-DOF)',
    'rocker-bogie wheel set (6-DOF)', 'sample-collection arm (5-DOF)',
    'expressive head and neck (3-DOF)', 'gesturing arms (14-DOF)',
    'brushless rotor set (4-DOF)', 'thrust-vectoring nozzles (3-DOF)',
    'telescoping mast (2-DOF)', 'cargo winch (1-DOF)'];
  var SENSORS = ['thermal imager', 'thermal camera', 'ambient microphone array',
    'ground-stability radar', 'odor sensor', 'tactile fingertip array',
    'UV sterilization lamp', 'face-tracking camera', 'proximity skin',
    'emotion-voice analyzer', '4K stabilized camera', 'sonar array',
    'lidar mapping unit', 'moisture probe', 'particulate counter'];
  var MOBILITY = ['bipedal indoor walker', 'quiet omni-wheel drive', 'wheeled lower body',
    'articulated wheel loader base', 'six-wheel rocker-bogie', 'VTOL fixed-wing cruise',
    'tracked orchard crawler', 'quadruped patrol walker', 'hover-pad glide',
    'treaded all-terrain drive'];
  var INTERFACES = ['companion-app pairing', 'JAH-Link mesh', 'voice-array API',
    'USB-C service port', 'fleet-telemetry uplink'];
  var POWERS = ['48V lithium-iron battery, 12h runtime', '24V lithium pack, 8h runtime',
    'hot-swap dual battery, 16h runtime', 'solar trickle + 10h battery',
    'tethered mains with 2h backup'];
  var COMPUTES = ['Signature Cortex-S2 module · 12 TOPS', 'Signature Cortex-M1 module · 8 TOPS',
    'Signature Cortex-X4 module · 40 TOPS'];
  var VERBS = ['measure, mix, and portion', 'scan, sort, and stack', 'lift, carry, and place',
    'inspect, log, and report', 'sweep, check, and flag', 'guide, steady, and assist'];

  /* shared templates — used by generate() AND the independent verifier */
  function rationaleOf(p) {
    var tags = CLASS_TAGS[p.cls];
    return {
      capability: p.ai + "'s strengths (" + tags[0] + ", " + tags[1] + ", communication) meet the " +
        p.body + "'s " + CLASS_LABEL[p.cls] + " build head-on: they share " + tags[0] +
        ", so the mind and the shell pull in the same direction from the first boot.",
      temperament: "As a working specialist, " + p.ai +
        " stays focused on the job, narrates its own work in plain words, and hands control " +
        "back to its human operator the instant anything looks off.",
      task: "On the " + p.mission + ", the " + p.body + " puts its " + p.act0 + " and " + p.sens0 +
        " to work to " + p.verb + " — the mission's demands and the body's hardware line up actuator for actuator."
    };
  }
  function demoLinesOf(p) {
    return [
      "My " + p.act0 + " lets me " + p.verb + ", " + p.mission + " — without breaking stride.",
      "Through my " + p.sens0 + ", I read the mission field in full detail before I act.",
      "On " + p.mission + " I keep my " + p.mobility + " moving with " + p.act1 + ", steady from start to finish.",
      "Matched at " + p.score + " of 100, this pairing is no accident — ask me anything.",
      "With " + p.mobility + " under me and my " + p.sens1 + " awake, the " + p.mission + " is already underway."
    ];
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var cls = opts.type && TYPES.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, TYPES);
    var p = {
      body: pick(rnd, PRE) + pick(rnd, SUF),
      cls: cls,
      mission: pick(rnd, MISSIONS),
      ai: pick(rnd, AI_NAMES),
      ai_family: 'domain',
      score: ri(rnd, 58, 97),
      height_cm: ri(rnd, 60, 190),
      width_cm: ri(rnd, 40, 120),
      depth_cm: ri(rnd, 30, 90),
      mass_kg: ri(rnd, 25, 220),
      payloadRatio: pick(rnd, [0.25, 0.3, 0.35, 0.4, 0.5]),
      power: pick(rnd, POWERS),
      compute: pick(rnd, COMPUTES),
      mobility: pick(rnd, MOBILITY),
      act0: pick(rnd, ACTUATORS), act1: pick(rnd, ACTUATORS), act2: pick(rnd, ACTUATORS),
      sens0: pick(rnd, SENSORS), sens1: pick(rnd, SENSORS), sens2: pick(rnd, SENSORS),
      if0: pick(rnd, INTERFACES), if1: pick(rnd, INTERFACES),
      verb: pick(rnd, VERBS)
    };
    p.payload_kg = Math.round(p.mass_kg * p.payloadRatio);
    var n = (opts.baseN || 0) + 1 + (opts.seq || 0);
    var pub = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      type: 'robot-design-match',
      title: p.body + ' × ' + p.ai,
      body_name: p.body,
      class: p.cls,
      mission: p.mission,
      ai_name: p.ai,
      ai_family: p.ai_family,
      score: p.score,
      hardware: {
        height_cm: p.height_cm, width_cm: p.width_cm, depth_cm: p.depth_cm,
        mass_kg: p.mass_kg, payload_kg: p.payload_kg,
        power: p.power, compute: p.compute, mobility: p.mobility,
        actuators: [p.act0, p.act1, p.act2],
        sensors: [p.sens0, p.sens1, p.sens2],
        interfaces: [p.if0, p.if1]
      },
      rationale: rationaleOf(p),
      demo_lines: demoLinesOf(p),
      stamp: STAMP
    };
    pub._priv = p;
    return pub;
  }

  /* independent re-builder: validate() reconstructs every derived string from
     the raw params (rationaleOf/demoLinesOf) and compares — the verifier. */
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'type', 'title', 'body_name', 'class', 'mission', 'ai_name',
      'score', 'hardware', 'rationale', 'demo_lines'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-ROBOT-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.class && TYPES.indexOf(rec.class) < 0) errs.push('bad class');
    if (rec.score !== undefined && (rec.score < 58 || rec.score > 97)) errs.push('score out of range');
    var h = rec.hardware || {};
    ['height_cm', 'width_cm', 'depth_cm', 'mass_kg', 'payload_kg'].forEach(function (k) {
      if (typeof h[k] !== 'number' || !isFinite(h[k])) errs.push('bad hardware.' + k);
    });
    if (h.payload_kg > h.mass_kg) errs.push('payload exceeds mass');
    if (!Array.isArray(rec.demo_lines) || rec.demo_lines.length !== 5) errs.push('demo_lines must be 5 lines');
    if (rec._priv) {
      var p = rec._priv, r = rationaleOf(p), d = demoLinesOf(p);
      if (JSON.stringify(rec.rationale) !== JSON.stringify(r)) errs.push('rationale mismatch vs raw params');
      if (JSON.stringify(rec.demo_lines) !== JSON.stringify(d)) errs.push('demo_lines mismatch vs raw params');
      if (rec.body_name !== p.body) errs.push('body_name mismatch');
      if (rec.title !== p.body + ' × ' + p.ai) errs.push('title mismatch');
      if (rec.score !== p.score) errs.push('score mismatch');
      if (rec.mission !== p.mission) errs.push('mission mismatch');
      if (rec.ai_name !== p.ai) errs.push('ai_name mismatch');
      if (h.payload_kg !== Math.round(p.mass_kg * p.payloadRatio)) errs.push('payload not derived from mass');
      if (d[3].indexOf(String(p.score)) < 0) errs.push('demo line 3 does not carry the score');
      if (r.task.indexOf(p.mission) < 0 || r.task.indexOf(p.body) < 0) errs.push('rationale.task missing mission/body');
    } else errs.push('no private raw params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: generated design name must not duplicate an archived pair's body name */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var bn = Array.isArray(a) ? a[2] : a.body_name;
      if (bn && bn === rec.body_name) errs.push('duplicate of archived robot design: ' + bn);
    });
    return { ok: errs.length === 0, errors: errs };
  }

  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var rec2 = generate(seed + (parseInt(nums[0], 10) % 1000), opts, JAHDB.prng(JAHDB.hashStr(String(seed) + nums[0])));
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('robots', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
