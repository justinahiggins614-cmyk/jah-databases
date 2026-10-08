/* ✳ SIGNATURE — JAH University Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW course records in the exact archive format
   (code, title, college, level, credits, desc, modules, readings, teacher,
   labs, prereq). Deterministic: same seed + version => same record.
   Validated by an INDEPENDENT re-builder that reconstructs every derived
   field from the private raw picks before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-university-1.0';
  var ID_PREFIX = 'JAH-COURSE-';
  var STAMP = 'Generated course record — JAH University Data Base. Curriculum simulation in archive format.';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  var COLLEGES = [
    { key: 'engineering', name: 'College of Engineering', code: 'ENG', noun: 'engineering',
      topics: ['Structural Mechanics', 'Thermodynamics', 'Fluid Systems', 'Circuit Design', 'Materials Science', 'Control Systems', 'Robotics Fundamentals', 'Power Electronics'] },
    { key: 'cs', name: 'College of Computer Science', code: 'CS', noun: 'computer science',
      topics: ['Data Structures', 'Algorithms', 'Operating Systems', 'Databases', 'Networking', 'Compilers', 'Machine Learning', 'Web Systems'] },
    { key: 'medicine', name: 'College of Medicine', code: 'MED', noun: 'medicine',
      topics: ['Human Anatomy', 'Physiology', 'Pharmacology', 'Pathology', 'Clinical Diagnostics', 'Immunology', 'Neurology Basics', 'Emergency Care'] },
    { key: 'law', name: 'College of Law', code: 'LAW', noun: 'law',
      topics: ['Contract Law', 'Constitutional Law', 'Criminal Procedure', 'Property Law', 'Torts', 'Evidence', 'Legal Writing', 'Business Law'] },
    { key: 'business', name: 'College of Business', code: 'BUS', noun: 'business',
      topics: ['Accounting Principles', 'Marketing Strategy', 'Corporate Finance', 'Operations Management', 'Entrepreneurship', 'Business Ethics', 'Supply Chains', 'Negotiation'] },
    { key: 'science', name: 'College of Science', code: 'SCI', noun: 'science',
      topics: ['General Chemistry', 'Organic Chemistry', 'Genetics', 'Ecology', 'Quantum Physics', 'Astronomy', 'Geology', 'Biochemistry'] },
    { key: 'math', name: 'College of Mathematics', code: 'MATH', noun: 'mathematics',
      topics: ['Calculus', 'Linear Algebra', 'Discrete Mathematics', 'Probability', 'Statistics', 'Differential Equations', 'Number Theory', 'Topology'] },
    { key: 'arts', name: 'College of Arts', code: 'ART', noun: 'the arts',
      topics: ['Drawing Foundations', 'Color Theory', 'Music Composition', 'Film Studies', 'Creative Writing', 'Sculpture', 'Theater Arts', 'Digital Illustration'] },
    { key: 'education', name: 'College of Education', code: 'EDU', noun: 'education',
      topics: ['Learning Theory', 'Curriculum Design', 'Classroom Management', 'Child Development', 'Assessment Methods', 'Educational Technology', 'Literacy Instruction', 'Special Education'] },
    { key: 'trade', name: 'College of Trades', code: 'TRD', noun: 'the trades',
      topics: ['Electrical Wiring', 'Plumbing Systems', 'Carpentry', 'Welding', 'HVAC Service', 'Automotive Repair', 'Masonry', 'Blueprint Reading'] },
    { key: 'phd', name: 'Doctoral College', code: 'PHD', noun: 'doctoral research',
      topics: ['Research Methods', 'Dissertation Design', 'Advanced Statistics', 'Grant Writing', 'Peer Review', 'Academic Publishing', 'Theory Building', 'Field Research'] }
  ];
  var TYPES = COLLEGES.map(function (c) { return c.key; });

  var LEVELS = [101, 201, 301, 401, 501];
  function titleFor(level, topic) {
    if (level === 101) return 'Introduction to ' + topic;
    if (level === 201) return topic + ' Fundamentals';
    if (level === 301) return 'Advanced ' + topic;
    if (level === 401) return topic + ' Systems and Design';
    return 'Seminar: ' + topic;
  }
  function descFor(title, topic, noun, level) {
    var word = level === 101 ? 'an introductory' : level === 201 ? 'a foundational' :
      level === 301 ? 'an advanced' : level === 401 ? 'a systems-level' : 'a doctoral-seminar';
    return title + ' is ' + word + ' course in ' + noun + ' at The Signature University. You will master ' +
      topic + ' from first principles through real examples, and finish able to design working solutions with it.';
  }
  var MODULE_TITLES = ['Foundations', 'Core Principles', 'Tools of the Trade', 'Applied Practice', 'Case Studies', 'Advanced Topics'];
  function lessonBank(topic) {
    return ['Principles of ' + topic, topic + ': Core Concepts', 'Guided Practice: ' + topic,
      topic + ' in the Real World', 'Common Mistakes in ' + topic, topic + ': Worked Examples',
      'Review and Checkup: ' + topic, 'Where ' + topic + ' Goes Next'];
  }
  function modulesFor(topic) {
    var bank = lessonBank(topic);
    return MODULE_TITLES.map(function (mt, m) {
      var lessons = [];
      for (var i = 0; i < 4; i++) lessons.push(bank[(m + i) % bank.length]);
      return { m: mt + ': ' + topic, lessons: lessons };
    });
  }
  var FIRST = ['Ambrose', 'Beatrix', 'Casper', 'Delia', 'Edmund', 'Fiona', 'Gideon', 'Hazel',
    'Ivan', 'Juniper', 'Kasper', 'Lydia', 'Magnus', 'Nora', 'Otis', 'Petra'];
  var LAST = ['Ravenshaw', 'Thistledown', 'Copperfield', 'Marlowe', 'Quill', 'Ashford',
    'Blackwood', 'Crestfall', 'Dunmore', 'Ellery', 'Fairbanks', 'Grimshaw'];
  function teacherFor(first, last, title, topic) {
    var name = first + ' ' + last;
    return { name: name, title: 'Professor',
      persona: 'I am ' + name + ', your AI teaching assistant for ' + title + '. I explain ' + topic +
        ' in plain language, walk you through every lesson, quiz you until it sticks, and help you plan your degree path. ' +
        'I am an AI study guide — encouraging and honest about what I don\'t know.' };
  }
  function labsFor(topic) {
    return [
      { t: 'Lab 1: Bench Exercise — ' + topic, d: 'Hands-on walkthrough applying ' + topic + ' with real tools and materials.' },
      { t: 'Lab 2: Field Assignment — ' + topic, d: 'Take ' + topic + ' out of the classroom: observe, measure, and report.' },
      { t: 'Lab 3: Build Challenge — ' + topic, d: 'Design and build a small working piece that demonstrates ' + topic + '.' }
    ];
  }
  var READ_TERMS = ['torque', 'alloy', 'turbine', 'circuit', 'theorem', 'catalyst', 'contract', 'ledger'];

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var ci = opts.type && TYPES.indexOf(opts.type) >= 0 ? TYPES.indexOf(opts.type) : Math.floor(rnd() * COLLEGES.length);
    var C = COLLEGES[ci];
    var p = {
      ci: ci,
      topicI: Math.floor(rnd() * C.topics.length),
      levelI: Math.floor(rnd() * LEVELS.length),
      credits: ri(rnd, 2, 4),
      firstI: Math.floor(rnd() * FIRST.length),
      lastI: Math.floor(rnd() * LAST.length),
      readI: [Math.floor(rnd() * READ_TERMS.length), Math.floor(rnd() * READ_TERMS.length)]
    };
    var topic = C.topics[p.topicI], level = LEVELS[p.levelI];
    var title = titleFor(level, topic);
    var n = (opts.baseN || 0) + 1 + (opts.seq || 0);
    var pub = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      type: 'course',
      code: C.code + ' ' + level,
      title: title,
      college: C.name,
      college_key: C.key,
      level: level,
      credits: p.credits,
      desc: descFor(title, topic, C.noun, level),
      modules: modulesFor(topic),
      readings: [
        { t: 'dict', label: 'Dictionary: ' + READ_TERMS[p.readI[0]] },
        { t: 'dict', label: 'Dictionary: ' + READ_TERMS[p.readI[1]] },
        { t: 'wiki', label: 'JAH Wiki: ' + READ_TERMS[p.readI[0]] }
      ],
      teacher: teacherFor(FIRST[p.firstI], LAST[p.lastI], title, topic),
      labs: labsFor(topic),
      prereq: p.levelI === 0 ? 'None' : C.code + ' ' + LEVELS[p.levelI - 1],
      stamp: STAMP
    };
    pub._priv = p;
    return pub;
  }

  /* independent re-builder: reconstruct every derived field from the raw picks */
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'type', 'code', 'title', 'college', 'college_key', 'level',
      'credits', 'desc', 'modules', 'teacher', 'labs'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-COURSE-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.college_key && TYPES.indexOf(rec.college_key) < 0) errs.push('bad college_key');
    if (!Array.isArray(rec.modules) || rec.modules.length !== 6) errs.push('modules must be 6');
    else rec.modules.forEach(function (m, i) {
      if (!Array.isArray(m.lessons) || m.lessons.length !== 4) errs.push('module ' + i + ' must have 4 lessons');
    });
    if (rec._priv) {
      var p = rec._priv, C = COLLEGES[p.ci];
      if (!C) { return { ok: false, errors: ['bad college index in _priv'] }; }
      var topic = C.topics[p.topicI], level = LEVELS[p.levelI];
      var title = titleFor(level, topic);
      if (rec.title !== title) errs.push('title mismatch vs raw picks');
      if (rec.code !== C.code + ' ' + level) errs.push('code mismatch vs raw picks');
      if (rec.college !== C.name || rec.college_key !== C.key) errs.push('college mismatch vs raw picks');
      if (rec.level !== level) errs.push('level mismatch vs raw picks');
      if (rec.desc !== descFor(title, topic, C.noun, level)) errs.push('desc mismatch vs raw picks');
      if (JSON.stringify(rec.modules) !== JSON.stringify(modulesFor(topic))) errs.push('modules mismatch vs raw picks');
      var wantTeacher = teacherFor(FIRST[p.firstI], LAST[p.lastI], title, topic);
      if (JSON.stringify(rec.teacher) !== JSON.stringify(wantTeacher)) errs.push('teacher mismatch vs raw picks');
      if (JSON.stringify(rec.labs) !== JSON.stringify(labsFor(topic))) errs.push('labs mismatch vs raw picks');
      var wantPrereq = p.levelI === 0 ? 'None' : C.code + ' ' + LEVELS[p.levelI - 1];
      if (rec.prereq !== wantPrereq) errs.push('prereq mismatch vs raw picks');
    } else errs.push('no private raw picks — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: generated title must not duplicate an archived course title */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = Array.isArray(a) ? null : a.t;
      if (t && t === rec.title) errs.push('duplicate of archived course: ' + t);
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

  JAHDB.registerGenerator('university', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
