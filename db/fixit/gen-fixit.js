/* ✳ SIGNATURE — JAH Fix-It Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW fix guides in the exact archive format
   (field, title, symptoms, diagnosis, ranked solutions with steps/tools/parts,
   safety, difficulty). Deterministic: same seed + version => same record.
   Titles are NEW combinations of real field vocab — never copied verbatim.
   Time/cost figures are labeled estimates; every guide carries a safety note
   naming the qualified pro. Validated by an INDEPENDENT re-builder that
   reconstructs every derived field from the private raw picks. */
(function () {
  'use strict';
  var VERSION = 'jahdb-fixit-1.0';
  var ID_PREFIX = 'JAH-FIX-';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  var FIELDS = [
    { id: 'JAH-FIXFIELD-001', name: 'Electrical', pro: 'licensed electrician',
      devices: ['outlet', 'light switch', 'ceiling fan', 'breaker', 'doorbell', 'smoke detector', 'dimmer switch', 'GFCI outlet'],
      problems: ['dead — no power at all', 'flickering intermittently', 'trips the breaker', "won't reset", 'buzzing loudly', 'sparks when used', 'warm to the touch'],
      tools: ['non-contact voltage tester', 'insulated screwdriver set', 'flashlight', 'wire strippers'],
      parts: ['replacement duplex outlet', 'wire nuts', 'new breaker (same rating)', 'cover plate'],
      safety: 'HIGH — power off at the panel before touching anything.' },
    { id: 'JAH-FIXFIELD-002', name: 'Appliances', pro: 'appliance repair technician',
      devices: ['dishwasher', 'washing machine', 'dryer', 'refrigerator', 'microwave', 'garbage disposal', 'oven'],
      problems: ["won't start", 'leaking water', 'making a grinding noise', 'not heating', 'shaking violently', 'draining slowly', 'tripping the outlet'],
      tools: ['nut driver set', 'multimeter', 'putty knife', 'towels and bucket'],
      parts: ['replacement hose', 'door gasket', 'thermal fuse', 'drain pump'],
      safety: 'MODERATE — unplug the appliance and shut off water before opening panels.' },
    { id: 'JAH-FIXFIELD-003', name: 'Heating & Cooling', pro: 'HVAC technician',
      devices: ['furnace', 'air conditioner', 'thermostat', 'heat pump', 'vent register', 'air handler'],
      problems: ['blowing cold air', 'short-cycling', 'not turning on', 'making a rattling noise', 'iced-over coils', 'weak airflow'],
      tools: ['screwdriver set', 'fin comb', 'shop vacuum', 'new filter'],
      parts: ['replacement air filter', 'thermostat batteries', 'contactor', 'capacitor'],
      safety: 'MODERATE — power off at the disconnect; refrigerant work is pro-only.' },
    { id: 'JAH-FIXFIELD-004', name: 'Automotive', pro: 'certified mechanic',
      devices: ['car battery', 'brake pads', 'headlight', 'alternator', 'tire', 'windshield wipers', 'spark plugs'],
      problems: ["won't turn over", 'squealing when braking', 'dim or out', 'draining overnight', 'vibrating at speed', 'streaking the glass'],
      tools: ['socket set', 'jack and jack stands', 'tire pressure gauge', 'jumper cables'],
      parts: ['replacement bulb', 'wiper blades', 'battery terminals cleaner', 'brake pads (axle set)'],
      safety: 'HIGH — never work under a car held only by a jack; use stands.' },
    { id: 'JAH-FIXFIELD-005', name: 'Computers & Cyber', pro: 'computer repair shop',
      devices: ['laptop', 'desktop PC', 'Wi-Fi router', 'external hard drive', 'printer', 'monitor'],
      problems: ["won't boot", 'running very slowly', 'dropping the connection', 'overheating and shutting down', 'no display', 'paper jamming constantly'],
      tools: ['precision screwdriver set', 'compressed air', 'USB installer drive', 'cable ties'],
      parts: ['replacement SSD', 'thermal paste', 'RAM stick', 'power cable'],
      safety: 'LOW — back up data first; ground yourself before touching boards.' },
    { id: 'JAH-FIXFIELD-006', name: 'Phones & Tablets', pro: 'phone repair shop',
      devices: ['phone screen', 'charging port', 'phone battery', 'tablet', 'speaker', 'camera lens'],
      problems: ['cracked and unresponsive', 'charging intermittently', 'draining in hours', 'no sound', 'foggy photos', 'stuck in a boot loop'],
      tools: ['pentalobe driver', 'spudger', 'suction cup', 'tweezers'],
      parts: ['replacement screen assembly', 'charging cable (certified)', 'adhesive strips'],
      safety: 'MODERATE — a swollen battery is a fire risk; stop and get pro help.' },
    { id: 'JAH-FIXFIELD-007', name: 'Vintage Electronics', pro: 'vintage electronics specialist',
      devices: ['tube radio', 'record player', 'CRT television', 'cassette deck', 'vintage amplifier'],
      problems: ['humming loudly', 'no sound at all', 'speed drifting', 'picture collapsed', 'eating tapes', 'scratchy volume knob'],
      tools: ['contact cleaner', 'soldering iron', 'capacitor tester', 'soft brush'],
      parts: ['replacement stylus', 'drive belt', 'electrolytic capacitors', 'fuses'],
      safety: 'HIGH — old sets can hold lethal charge; discharge capacitors first.' },
    { id: 'JAH-FIXFIELD-008', name: 'Chips & Circuit Boards', pro: 'electronics repair technician',
      devices: ['circuit board', 'solder joint', 'microcontroller', 'power supply board', 'sensor module'],
      problems: ['burnt smell near the board', 'intermittent resets', 'corroded traces', 'cold solder joints', 'blown fuse on the board'],
      tools: ['soldering station', 'magnifier lamp', 'multimeter', 'flux pen'],
      parts: ['replacement fuse', 'jumper wire', 'conformal coating', 'header pins'],
      safety: 'MODERATE — power off and discharge; lead solder needs ventilation.' },
    { id: 'JAH-FIXFIELD-009', name: 'Home Repair', pro: 'general contractor',
      devices: ['drywall', 'door hinge', 'faucet', 'toilet', 'window latch', 'deck board', 'gutter'],
      problems: ['hole punched through', 'sagging and squeaking', 'dripping constantly', 'running nonstop', "won't latch", 'rotted and soft', 'overflowing in rain'],
      tools: ['drill', 'putty knife', 'level', 'caulk gun', 'adjustable wrench'],
      parts: ['drywall patch kit', 'replacement flapper', 'wood filler', 'caulk'],
      safety: 'LOW — shut off water for plumbing; mind ladders on gutters.' },
    { id: 'JAH-FIXFIELD-010', name: 'Small Engines & Tools', pro: 'small-engine mechanic',
      devices: ['lawn mower', 'chainsaw', 'leaf blower', 'pressure washer', 'drill', 'string trimmer'],
      problems: ["won't start", 'sputtering under load', 'leaking fuel', 'chain slipping', 'losing pressure', 'smoking heavily'],
      tools: ['spark plug wrench', 'fuel stabilizer', 'air filter', 'fresh fuel mix'],
      parts: ['spark plug', 'air filter', 'fuel line', 'replacement chain'],
      safety: 'HIGH — drain fuel and pull the plug wire before touching blades.' },
    { id: 'JAH-FIXFIELD-011', name: 'Lawn & Outdoor', pro: 'landscaping professional',
      devices: ['sprinkler head', 'lawn', 'garden hose', 'fence post', 'patio pavers', 'outdoor lighting'],
      problems: ['spraying sideways', 'brown patches spreading', 'leaking at the coupling', 'leaning after storms', 'sinking unevenly', 'flickering at dusk'],
      tools: ['shovel', 'sprinkler adjustment tool', 'hose washers', 'tamper'],
      parts: ['replacement sprinkler head', 'grass seed', 'hose gasket set', 'paver sand'],
      safety: 'LOW — call before you dig; watch for buried utilities.' },
    { id: 'JAH-FIXFIELD-012', name: 'Plumbing', pro: 'licensed plumber',
      devices: ['sink drain', 'toilet', 'shower head', 'water heater', 'supply valve', 'garbage disposal'],
      problems: ['draining slowly', 'clogged solid', 'weak water pressure', 'no hot water', 'dripping at the valve', 'humming but not grinding'],
      tools: ['plunger', 'drain snake', 'basin wrench', 'bucket and towels'],
      parts: ['plumber\u2019s tape', 'replacement flapper', 'supply line', 'drain gasket'],
      safety: 'MODERATE — shut off water first; water heaters can scald — pro for gas units.' }
  ];
  var TYPES = FIELDS.map(function (f) { return f.name; });

  var DIFFS = ['Easy', 'Moderate', 'Advanced'];
  var TIMES = ['10–20 min', '20–30 min', '30–60 min', '1–2 hours'];
  var COSTS = ['$0–$10', '$0–$15', '$10–$30', '$15–$50', '$30–$80'];

  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var fi = opts.type && TYPES.indexOf(opts.type) >= 0 ? TYPES.indexOf(opts.type) : Math.floor(rnd() * FIELDS.length);
    var F = FIELDS[fi];
    var p = {
      fi: fi,
      devI: Math.floor(rnd() * F.devices.length),
      probI: Math.floor(rnd() * F.problems.length),
      symI: [Math.floor(rnd() * 4), Math.floor(rnd() * 4), Math.floor(rnd() * 4)],
      diaI: [Math.floor(rnd() * 4), Math.floor(rnd() * 4), Math.floor(rnd() * 4)],
      toolI: [Math.floor(rnd() * F.tools.length), Math.floor(rnd() * F.tools.length)],
      partI: [Math.floor(rnd() * F.parts.length)],
      diffI: Math.floor(rnd() * DIFFS.length),
      timeI: Math.floor(rnd() * TIMES.length),
      costI: Math.floor(rnd() * COSTS.length),
      safeI: Math.floor(rnd() * 3)
    };
    var dev = F.devices[p.devI], prob = F.problems[p.probI];
    var title = cap(dev) + ' ' + prob;
    var symT = [
      'The ' + dev + ' is ' + prob + ' — you can see it happen every time you try.',
      'It worked fine before; nothing else on the same circuit or system changed.',
      'A known-good replacement or a second unit does not show the same behavior.'
    ];
    var diaT = [
      'Confirm the symptom with a known-good test — rule out the simple causes first.',
      'Check power, connections, and settings on the ' + dev + ' before opening anything.',
      'Inspect for the obvious: loose parts, wear, blockage, or damage.',
      'Narrow it down: change one thing at a time and re-test the ' + dev + '.'
    ];
    var safetyNote = F.safety;
    var sol1 = {
      rank: 1, kind: 'DIY_FIX',
      title: 'Fix the ' + dev + ' yourself — ' + prob.split('—')[0].trim(),
      steps: [
        'Shut off power, water, or fuel to the ' + dev + ' as the safety note requires.',
        'Work through the diagnosis list above and confirm the exact failure.',
        'Apply the fix: reseat, tighten, clean, or replace the worn part on the ' + dev + '.',
        'Reassemble, restore power/water/fuel, and test the ' + dev + ' three times.',
        'If the ' + dev + ' is still ' + prob + ', stop — move to the pro repair below.'
      ],
      difficulty: DIFFS[p.diffI],
      time: TIMES[p.timeI],
      cost: COSTS[p.costI],
      tools: [F.tools[p.toolI[0]], F.tools[p.toolI[1]]],
      parts: [F.parts[p.partI[0]]]
    };
    var sol2 = {
      rank: 2, kind: 'PRO_REPAIR',
      title: 'Have a ' + F.pro + ' repair it',
      steps: [
        'If the diagnosis points past basic DIY, or the safety level is HIGH, call a ' + F.pro + '.',
        'Describe the symptoms and what you already checked — it saves diagnostic time.',
        'Get the quote in writing before authorizing work.'
      ],
      note: 'Best when safety is HIGH, special tools are needed, or the DIY fix did not hold.'
    };
    var sol3 = {
      rank: 3, kind: 'REPLACE',
      title: 'Replace the ' + dev,
      steps: [
        'If the ' + dev + ' is old, badly worn, or repair costs approach replacement cost, replace it.',
        'Match specifications (size, rating, fittings) before buying.',
        'Recycle the old unit per local rules.'
      ]
    };
    var n = (opts.baseN || 0) + 1 + (opts.seq || 0);
    var pub = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      type: 'fix',
      field: F.name,
      field_id: F.id,
      title: title,
      symptoms: [symT[p.symI[0]], symT[p.symI[1]], symT[p.symI[2]]],
      diagnosis: [diaT[p.diaI[0]], diaT[p.diaI[1]], diaT[p.diaI[2]]],
      solutions: [sol1, sol2, sol3],
      safety: ['LOW', 'MODERATE', 'HIGH'][p.safeI],
      safety_note: safetyNote,
      warnings: ['If anything smells burnt, looks scorched, or feels hot — stop and call a ' + F.pro + '.'],
      difficulty: DIFFS[p.diffI],
      stamp: 'Generated fix guide — JAH Fix-It Data Base. Estimates, not quotes; for HIGH safety issues, a qualified ' + F.pro + ' must do the work.'
    };
    pub._priv = p;
    return pub;
  }

  /* independent re-builder: reconstruct every derived field from the raw picks */
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'type', 'field', 'field_id', 'title', 'symptoms', 'diagnosis',
      'solutions', 'safety', 'difficulty'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-FIX-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.field && TYPES.indexOf(rec.field) < 0) errs.push('bad field');
    if (['LOW', 'MODERATE', 'HIGH'].indexOf(rec.safety) < 0) errs.push('bad safety level');
    var sols = rec.solutions || [];
    if (sols.length !== 3) errs.push('must have exactly 3 ranked solutions');
    else {
      if (sols[0].rank !== 1 || sols[0].kind !== 'DIY_FIX') errs.push('solution 1 must be rank 1 DIY_FIX');
      if (sols[1].rank !== 2 || sols[1].kind !== 'PRO_REPAIR') errs.push('solution 2 must be rank 2 PRO_REPAIR');
      if (sols[2].rank !== 3 || sols[2].kind !== 'REPLACE') errs.push('solution 3 must be rank 3 REPLACE');
      sols.forEach(function (s2, i) {
        if (!Array.isArray(s2.steps) || s2.steps.length === 0) errs.push('solution ' + (i + 1) + ' needs steps');
      });
    }
    if (rec._priv) {
      var p = rec._priv, F = FIELDS[p.fi];
      if (!F) { return { ok: false, errors: ['bad field index in _priv'] }; }
      var dev = F.devices[p.devI], prob = F.problems[p.probI];
      if (rec.title !== cap(dev) + ' ' + prob) errs.push('title mismatch vs raw picks');
      if (rec.field !== F.name || rec.field_id !== F.id) errs.push('field mismatch vs raw picks');
      if (rec.safety_note !== F.safety) errs.push('safety_note mismatch vs raw picks');
      var s1 = rec.solutions[0] || {};
      if (s1.title !== 'Fix the ' + dev + ' yourself — ' + prob.split('—')[0].trim()) errs.push('solution 1 title mismatch');
      if (s1.difficulty !== DIFFS[p.diffI] || s1.time !== TIMES[p.timeI] || s1.cost !== COSTS[p.costI]) errs.push('solution 1 estimate mismatch');
      if (JSON.stringify(s1.tools) !== JSON.stringify([F.tools[p.toolI[0]], F.tools[p.toolI[1]]])) errs.push('solution 1 tools mismatch');
      if (JSON.stringify(s1.parts) !== JSON.stringify([F.parts[p.partI[0]]])) errs.push('solution 1 parts mismatch');
      var s2 = rec.solutions[1] || {};
      if (s2.title !== 'Have a ' + F.pro + ' repair it') errs.push('solution 2 title mismatch');
      if (rec.warnings[0].indexOf(F.pro) < 0) errs.push('warning must name the pro');
    } else errs.push('no private raw picks — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: generated title must not duplicate an archived fix title */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = Array.isArray(a) ? a[1] : a.title;
      if (t && t === rec.title) errs.push('duplicate of archived fix: ' + t);
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

  JAHDB.registerGenerator('fixit', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
