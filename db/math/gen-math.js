/* ✳ SIGNATURE — JAH Math Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW math grid records in archive style —
   a deterministic 12x12 bit grid (the Signature math grid) encoded through
   the archive's encoding families (hex, base64, ASCII-art). Deterministic:
   same seed + version => same record. Every record is re-encoded by an
   INDEPENDENT verifier before it is accepted. */
(function () {
  'use strict';
  var VERSION = 'jahdb-math-1.0';
  var ID_PREFIX = 'JAH-MATH-';
  var GRID = 12, CELLS = 144;
  var STAMP = 'Official JAH Math Grid Archive — generated boundlessly, verified independently.';
  var CATS = ['Base systems', 'Mixes', 'Visual codes', 'Text encodings', 'Numeric formats',
              'Audio', 'Geometry', 'Cryptography', 'Compression'];
  var HEXC = '0123456789abcdef';
  var B64C = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  function bitsToHex(bits) {
    var s = '';
    for (var i = 0; i < CELLS; i += 4)
      s += HEXC[bits[i] * 8 + bits[i + 1] * 4 + bits[i + 2] * 2 + bits[i + 3]];
    return s;
  }
  function bitsToB64(bits) {
    var s = '';
    for (var i = 0; i < CELLS; i += 6) {
      var v = 0;
      for (var j = 0; j < 6; j++) v = v * 2 + bits[i + j];
      s += B64C[v];
    }
    return s;
  }
  function bitsToArt(bits) {
    var rows = [];
    for (var r = 0; r < GRID; r++) {
      var s = '';
      for (var c = 0; c < GRID; c++) s += bits[r * GRID + c] ? '█' : '·';
      rows.push(s);
    }
    return rows;
  }
  function popcount(bits) { var n = 0, i; for (i = 0; i < bits.length; i++) n += bits[i]; return n; }
  function sym180(bits) { for (var i = 0; i < CELLS; i++) if (bits[i] !== bits[CELLS - 1 - i]) return false; return true; }

  var PUB_KEYS = ['id', 'n', 'title', 'cat', 'grid', 'bitstring', 'encodings', 'popcount',
                  'symmetric180', 'note', 'stamp'];

  /* ============ GEOMETRIC ENTRIES (Geometry-One six-tool framework) ============
     Real classical content: theorems with proofs, constructions, formulas, and
     worked problems with computed solutions. Deterministic: same seed => same entry. */
  var GEO_ID_PREFIX = 'JAH-GEO-';
  var GEO_TOOLS = ['Line/Distance/Dimension','Triangle/Level/Pyramid','Square/Corner/Box',
                   'Plus/Cross/Crossroads','Circle/Dot/Ball','Curvature/Perspective/Fluidity'];
  var GEO_KINDS = ['geometry-theorem','geometry-construction','geometry-formula','geometry-problem'];
  var GEO_STAMP = 'Signature Math Database — generated geometric entry. Real classical mathematics on the Geometry-One six-tool framework.';
  var GEO_THEOREMS = [
    {t:'Triangle/Level/Pyramid', title:'Pythagorean Theorem',
     statement:'In a right triangle, a^2 + b^2 = c^2 where c is the hypotenuse.',
     proof:['Erect squares outward on all three sides of right triangle ABC (right angle at C).',
       'Drop the altitude from C to the hypotenuse, extending it through the square on c; it splits that square into two rectangles.',
       'Each rectangle equals one smaller square in area (same base, same height between parallels).',
       'Hence the square on c has area a^2 + b^2.'],
     source:"Euclid's Elements I.47"},
    {t:'Triangle/Level/Pyramid', title:'Triangle Angle Sum',
     statement:'The interior angles of any triangle sum to 180 degrees.',
     proof:['Through vertex A draw DE parallel to BC.',
       'Angle DAB = angle ABC and angle EAC = angle ACB (alternate interior angles).',
       'DAB + BAC + CAE = 180 degrees on straight line DE; substituting gives the sum.'],
     source:"Euclid's Elements I.32"},
    {t:'Circle/Dot/Ball', title:"Thales' Theorem",
     statement:'Any angle inscribed in a semicircle is a right angle.',
     proof:['AB diameter, center O, C on circle; OA = OB = OC so triangles OAC, OBC are isosceles.',
       'Let the base angles be x and y; the triangle angles x, y, x+y sum to 180 degrees.',
       'Thus x + y = 90 degrees = angle ACB.'],
     source:'Euclid III.31'},
    {t:'Circle/Dot/Ball', title:'Central Angle Theorem',
     statement:'A central angle is twice any inscribed angle subtending the same arc.',
     proof:['Extend OC to D; triangle OAC is isosceles, so exterior angle AOD = 2 x angle ACO.',
       'Likewise BOD = 2 x BCO; adding gives AOB = 2 x ACB.'],
     source:'Euclid III.20'},
    {t:'Line/Distance/Dimension', title:'Triangle Inequality',
     statement:'Any side of a triangle is shorter than the sum of the other two.',
     proof:['Extend BA to D with AD = AC; triangle ACD is isosceles.',
       'Angle BCD > angle BDC, so the side opposite (BA + AC) exceeds BC.'],
     source:'Euclid I.20'},
    {t:'Plus/Cross/Crossroads', title:'Vertical Angles Are Equal',
     statement:'Opposite angles formed by two intersecting lines are equal.',
     proof:['Adjacent angles form linear pairs summing to 180 degrees; subtracting the shared angle leaves the vertical pair equal.'],
     source:'Euclid I.15'},
    {t:'Square/Corner/Box', title:'Parallelogram Diagonals Bisect Each Other',
     statement:'The diagonals of a parallelogram bisect each other.',
     proof:['Triangles AOB and COD have AB = CD, with alternate interior angles equal: ASA-congruent.',
       'Hence AO = OC and BO = OD.'],
     source:'Euclid I.34'},
    {t:'Square/Corner/Box', title:'Polygon Interior Angle Sum',
     statement:'An n-gon\'s interior angles sum to (n-2) x 180 degrees.',
     proof:['Diagonals from one vertex split the n-gon into (n-2) triangles of 180 degrees each.'],
     source:'Standard'},
    {t:'Circle/Dot/Ball', title:'Intersecting Chords Theorem',
     statement:'If chords AB and CD meet at P: AP x PB = CP x PD.',
     proof:['Angles subtending arc CB are equal, so triangles PAC and PDB are similar (AA).',
       'Corresponding sides give PA/PD = PC/PB.'],
     source:'Euclid III.35'},
    {t:'Triangle/Level/Pyramid', title:'Midpoint (Midsegment) Theorem',
     statement:'Joining the midpoints of two sides gives a segment parallel to the third side and half its length.',
     proof:['AD/AB = AE/AC = 1/2 with common angle A: triangles ADE and ABC similar (SAS).',
       'Hence DE/BC = 1/2 and DE is parallel to BC.'],
     source:'Standard'}
  ];
  var GEO_CONSTRUCTIONS = [
    {t:'Line/Distance/Dimension', title:'Bisect a Line Segment',
     given:'Segment AB.', goal:'Its midpoint and perpendicular bisector.',
     steps:['Compass wider than half AB; arcs centered at A and B meet at P and Q.',
       'Line PQ crosses AB at the midpoint M.'],
     why:'P and Q are each equidistant from A and B: the perpendicular-bisector locus.'},
    {t:'Plus/Cross/Crossroads', title:'Bisect an Angle',
     given:'Angle with vertex O.', goal:'A ray dividing it into two equal angles.',
     steps:['Arc centered at O cuts the sides at A, B.',
       'Equal arcs centered at A, B meet at P; ray OP is the bisector.'],
     why:'Triangles OAP, OBP are SSS-congruent.'},
    {t:'Line/Distance/Dimension', title:'Perpendicular from an External Point',
     given:'Line l and point P off l.', goal:'The perpendicular from P to l.',
     steps:['Arc centered at P cuts l at A and B.',
       'Equal arcs from A, B meet at Q; line PQ is perpendicular to l.'],
     why:'P and Q lie on the perpendicular bisector of AB.'},
    {t:'Triangle/Level/Pyramid', title:'Equilateral Triangle on a Segment',
     given:'Segment AB.', goal:'Equilateral triangle ABC.',
     steps:['Circle centered at A through B; circle centered at B through A.',
       'They meet at C; join AC, BC.'],
     why:'AC = AB = BC as radii.',
     source:'Euclid I.1'},
    {t:'Circle/Dot/Ball', title:'Regular Hexagon Inscribed in a Circle',
     given:'Circle with center O.', goal:'A regular inscribed hexagon.',
     steps:['Mark A on the circle; step the radius around the circumference six times.',
       'Join consecutive marks.'],
     why:'Chord = radius subtends 60 degrees; six make 360.',
     source:'Euclid IV.15'},
    {t:'Line/Distance/Dimension', title:'Divide a Segment into n Equal Parts',
     given:'Segment AB and integer n.', goal:'n equal divisions.',
     steps:['Ray from A at an angle; step n equal marks along it.',
       'Join the last mark to B; parallels through the marks cut AB proportionally.'],
     why:'Intercept theorem (Thales).'},
    {t:'Circle/Dot/Ball', title:'Tangent from an External Point',
     given:'Circle (center O), external point P.', goal:'The two tangent segments.',
     steps:['Bisect OP at M; circle centered at M radius MO meets the given circle at T1, T2.',
       'Lines PT1, PT2 are tangent.'],
     why:'Angle OT1P stands in a semicircle: right angle (Thales).'},
    {t:'Triangle/Level/Pyramid', title:'Circumcircle of a Triangle',
     given:'Triangle ABC.', goal:'The circle through A, B, C.',
     steps:['Perpendicular bisectors of two sides meet at O.',
       'Circle centered at O through A passes through B and C.'],
     why:'O is equidistant from all three vertices.'}
  ];
  var GEO_FORMULAS = [
    {t:'Triangle/Level/Pyramid', title:"Heron's Formula", formula:'A = sqrt(s(s-a)(s-b)(s-c)), s = (a+b+c)/2',
     variables:{A:'area','a, b, c':'side lengths','s':'semiperimeter'}},
    {t:'Circle/Dot/Ball', title:'Area of a Circle', formula:'A = pi x r^2',
     variables:{A:'area','r':'radius'}},
    {t:'Circle/Dot/Ball', title:'Volume of a Sphere', formula:'V = (4/3) x pi x r^3',
     variables:{V:'volume','r':'radius'}},
    {t:'Circle/Dot/Ball', title:'Volume of a Cylinder', formula:'V = pi x r^2 x h',
     variables:{V:'volume','r':'radius','h':'height'}},
    {t:'Square/Corner/Box', title:'Volume of a Pyramid', formula:'V = (1/3) x B x h',
     variables:{V:'volume','B':'base area','h':'height'}},
    {t:'Square/Corner/Box', title:'Area of a Trapezoid', formula:'A = (a+b)/2 x h',
     variables:{A:'area','a, b':'parallel sides','h':'height'}},
    {t:'Line/Distance/Dimension', title:'Distance Between Two Points', formula:'d = sqrt((x2-x1)^2 + (y2-y1)^2)',
     variables:{d:'distance','(x1,y1), (x2,y2)':'the points'}},
    {t:'Triangle/Level/Pyramid', title:'Law of Cosines', formula:'c^2 = a^2 + b^2 - 2ab cos(C)',
     variables:{'a, b, c':'sides','C':'angle opposite side c'}},
    {t:'Triangle/Level/Pyramid', title:'Law of Sines', formula:'a/sin(A) = b/sin(B) = c/sin(C) = 2R',
     variables:{'a, b, c':'sides','A, B, C':'opposite angles','R':'circumradius'}},
    {t:'Circle/Dot/Ball', title:'Arc Length', formula:'L = r x theta',
     variables:{L:'arc length','r':'radius','theta':'central angle in radians'}},
    {t:'Curvature/Perspective/Fluidity', title:'Area of an Ellipse', formula:'A = pi x a x b',
     variables:{A:'area','a':'semi-major axis','b':'semi-minor axis'}},
    {t:'Square/Corner/Box', title:"Euler's Formula", formula:'V - E + F = 2',
     variables:{V:'vertices','E':'edges','F':'faces'}}
  ];
  function geoProblem(rnd) {
    var which = Math.floor(rnd() * 8);
    var a, b, c, s, A, r, h, d, l, w, x1, y1, x2, y2, C;
    function f2(x){ return Math.round(x*100)/100; }
    if (which === 0) {
      a = ri(rnd,3,24); b = ri(rnd,3,24); c = f2(Math.sqrt(a*a+b*b));
      return {title:'Hypotenuse from legs '+a+' and '+b, problem:'A right triangle has legs '+a+' and '+b+'. Find the hypotenuse.',
        given:{leg_a:a,leg_b:b}, steps:['c^2 = '+a+'^2 + '+b+'^2 = '+(a*a+b*b)+'.','c = sqrt('+(a*a+b*b)+') = '+c+'.'], answer:'c = '+c};
    } else if (which === 1) {
      a = ri(rnd,4,25); b = ri(rnd,4,25); c = ri(rnd,4,25);
      if (!(a+b>c&&a+c>b&&b+c>a)) { a=13;b=14;c=15; }
      s = (a+b+c)/2; A = f2(Math.sqrt(s*(s-a)*(s-b)*(s-c)));
      return {title:'Heron area: sides '+a+', '+b+', '+c, problem:'Find the area of the triangle with sides '+a+', '+b+', '+c+'.',
        given:{a:a,b:b,c:c}, steps:['s = ('+a+'+'+b+'+'+c+')/2 = '+s+'.','A = sqrt('+s+' x '+f2(s-a)+' x '+f2(s-b)+' x '+f2(s-c)+') = '+A+'.'], answer:'A = '+A};
    } else if (which === 2) {
      r = ri(rnd,1,20); A = f2(Math.PI*r*r);
      return {title:'Circle area, radius '+r, problem:'Find the area of the circle with radius '+r+'.',
        given:{radius:r}, steps:['A = pi x r^2 = 3.1416 x '+(r*r)+' = '+A+'.'], answer:'A = '+A};
    } else if (which === 3) {
      l = ri(rnd,2,25); w = ri(rnd,2,25); d = f2(Math.hypot(l,w));
      return {title:'Rectangle diagonal '+l+' by '+w, problem:'Find the diagonal of the '+l+' by '+w+' rectangle.',
        given:{length:l,width:w}, steps:['d = sqrt('+l+'^2 + '+w+'^2) = sqrt('+(l*l+w*w)+') = '+d+'.'], answer:'d = '+d};
    } else if (which === 4) {
      a = ri(rnd,2,20); b = ri(rnd,2,20); h = ri(rnd,2,15); A = f2((a+b)/2*h);
      return {title:'Trapezoid area: bases '+a+', '+b+'; height '+h, problem:'Find the area of the trapezoid with parallel sides '+a+' and '+b+' and height '+h+'.',
        given:{base_a:a,base_b:b,height:h}, steps:['A = (a+b)/2 x h = '+f2((a+b)/2)+' x '+h+' = '+A+'.'], answer:'A = '+A};
    } else if (which === 5) {
      r = ri(rnd,1,12); h = ri(rnd,1,20); A = f2(Math.PI*r*r*h);
      return {title:'Cylinder volume: r = '+r+', h = '+h, problem:'Find the volume of the cylinder with radius '+r+' and height '+h+'.',
        given:{radius:r,height:h}, steps:['V = pi x r^2 x h = 3.1416 x '+(r*r)+' x '+h+' = '+A+'.'], answer:'V = '+A};
    } else if (which === 6) {
      x1=ri(rnd,-10,10);y1=ri(rnd,-10,10);x2=ri(rnd,-10,10);y2=ri(rnd,-10,10); d=f2(Math.hypot(x2-x1,y2-y1));
      return {title:'Distance: ('+x1+','+y1+') to ('+x2+','+y2+')', problem:'Find the distance between ('+x1+','+y1+') and ('+x2+','+y2+').',
        given:{p1:[x1,y1],p2:[x2,y2]}, steps:['d = sqrt(('+x2+'-'+x1+')^2 + ('+y2+'-'+y1+')^2) = sqrt('+((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))+') = '+d+'.'], answer:'d = '+d};
    }
    a = ri(rnd,20,100); b = ri(rnd,20,100); if (a+b>=170){a=50;b=60;} C = 180-a-b;
    return {title:'Third angle: '+a+' deg and '+b+' deg', problem:'Two angles of a triangle are '+a+' degrees and '+b+' degrees. Find the third.',
      given:{angle_A:a,angle_B:b}, steps:['C = 180 - '+a+' - '+b+' = '+C+' degrees.'], answer:'C = '+C+' degrees'};
  }
  function generateGeo(seed, opts, rnd) {
    opts = opts || {};
    var kind = opts.type || 'geometry-problem';
    var n = (opts.baseN || 0) + 1;
    var id = GEO_ID_PREFIX + String(n).padStart(6, '0');
    var rec = {id:id, n:n, record_kind:'geometric-archive', stamp:GEO_STAMP, _seed:seed, _kind:kind};
    if (kind === 'geometry-theorem') {
      var T = pick(rnd, GEO_THEOREMS);
      rec.kind='theorem'; rec.sg1_tool=T.t; rec.tool_key=toolKey(T.t); rec.topic='Euclidean geometry';
      rec.title=T.title; rec.statement=T.statement; rec.proof=T.proof.slice();
      if (T.source) rec.source=T.source;
      rec.description=T.statement;
      rec._priv={kind:kind, ti:GEO_THEOREMS.indexOf(T)};
    } else if (kind === 'geometry-construction') {
      var Cc = pick(rnd, GEO_CONSTRUCTIONS);
      rec.kind='construction'; rec.sg1_tool=Cc.t; rec.tool_key=toolKey(Cc.t); rec.topic='Compass and straightedge';
      rec.title=Cc.title; rec.given=Cc.given; rec.goal=Cc.goal; rec.steps=Cc.steps.slice();
      if (Cc.why) rec.why_it_works=Cc.why;
      if (Cc.source) rec.source=Cc.source;
      rec.description=Cc.goal;
      rec._priv={kind:kind, ci:GEO_CONSTRUCTIONS.indexOf(Cc)};
    } else if (kind === 'geometry-formula') {
      var F = pick(rnd, GEO_FORMULAS);
      rec.kind='formula'; rec.sg1_tool=F.t; rec.tool_key=toolKey(F.t); rec.topic='Formula';
      rec.title=F.title; rec.formula=F.formula;
      rec.variables=JSON.parse(JSON.stringify(F.variables));
      rec.description=F.formula;
      rec._priv={kind:kind, fi:GEO_FORMULAS.indexOf(F)};
    } else {
      var P = geoProblem(rnd);
      rec.kind='problem'; rec.sg1_tool='Triangle/Level/Pyramid'; rec.tool_key='triangle'; rec.topic='Worked problem';
      rec.title=P.title; rec.problem=P.problem;
      rec.given=JSON.parse(JSON.stringify(P.given)); rec.solution_steps=P.steps.slice(); rec.answer=P.answer;
      rec.description=P.problem;
      rec._priv={kind:kind, seed:seed};
    }
    return rec;
  }
  var TOOL_BY_NAME={'Line/Distance/Dimension':'line','Triangle/Level/Pyramid':'triangle','Square/Corner/Box':'square','Plus/Cross/Crossroads':'plus','Circle/Dot/Ball':'circle','Curvature/Perspective/Fluidity':'curvature'};
  function toolKey(tool){ return TOOL_BY_NAME[tool]||'triangle'; }
  function validateGeo(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return {ok:false, errors:['not an object']};
    ['id','kind','sg1_tool','tool_key','topic','title','description'].forEach(function(k){
      if (rec[k]===undefined||rec[k]===null||rec[k]==='') errs.push('missing field: '+k);
    });
    if (rec.id && !/^JAH-GEO-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (GEO_TOOLS.indexOf(rec.sg1_tool)<0) errs.push('bad sg1_tool');
    if (rec.kind==='theorem' && (!Array.isArray(rec.proof)||!rec.proof.length)) errs.push('theorem needs proof steps');
    if (rec.kind==='construction' && (!Array.isArray(rec.steps)||!rec.steps.length)) errs.push('construction needs steps');
    if (rec.kind==='formula' && (!rec.formula||!rec.variables)) errs.push('formula needs formula+variables');
    if (rec.kind==='problem') {
      if (!rec.problem||!rec.given||!Array.isArray(rec.solution_steps)||!rec.solution_steps.length||!rec.answer)
        errs.push('problem needs problem+given+solution_steps+answer');
    }
    if (rec._priv) {
      var p=rec._priv;
      if (p.kind==='geometry-theorem') {
        var T=GEO_THEOREMS[p.ti];
        if (!T||rec.title!==T.title||rec.statement!==T.statement) errs.push('theorem does not match curated source');
      } else if (p.kind==='geometry-construction') {
        var Cc=GEO_CONSTRUCTIONS[p.ci];
        if (!Cc||rec.title!==Cc.title) errs.push('construction does not match curated source');
      } else if (p.kind==='geometry-formula') {
        var F=GEO_FORMULAS[p.fi];
        if (!F||rec.title!==F.title||rec.formula!==F.formula) errs.push('formula does not match curated source');
      }
    } else errs.push('no private params — cannot independently verify');
    return {ok:errs.length===0, errors:errs};
  }
  function driftCheckGeo(rec, archiveSample) {
    var errs = [];
    (archiveSample||[]).forEach(function(a){
      var t=a.title;
      if (t && String(t)===String(rec.title)) errs.push('duplicate of archived record: '+t);
    });
    return {ok:errs.length===0, errors:errs};
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    if (opts.type && GEO_KINDS.indexOf(opts.type) >= 0) return generateGeo(seed, opts, rnd);
    var cat = opts.type && CATS.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, CATS);
    var bits = [];
    for (var i = 0; i < CELLS; i++) bits.push(rnd() < 0.5 ? 0 : 1);
    var n = (opts.baseN || 0) + 1;
    var pc = popcount(bits), sym = sym180(bits);
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      title: cat + ' grid record — ' + pc + ' marks on the 12×12',
      cat: cat,
      grid: '12x12',
      bitstring: bits.join(''),
      encodings: { hex: bitsToHex(bits), base64: bitsToB64(bits), ascii_art: bitsToArt(bits) },
      popcount: pc,
      symmetric180: sym,
      note: 'Generated math grid record: a deterministic 12×12 bit grid encoded through the archive\'s ' + cat + ' family. Not a stored archive record.',
      stamp: STAMP,
      _bits: bits, _cat: cat, _seed: seed
    };
    var pub = {};
    PUB_KEYS.forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = rec;
    return pub;
  }

  /* independent re-encoder: rebuilds every derived field from the raw bits */
  function verify(priv) {
    var errs = [];
    var bits = priv._bits;
    if (!Array.isArray(bits) || bits.length !== CELLS) return ['bad bit grid'];
    for (var i = 0; i < CELLS; i++)
      if (bits[i] !== 0 && bits[i] !== 1) { errs.push('bit grid not binary'); break; }
    if (priv.bitstring !== bits.join('')) errs.push('bitstring mismatch');
    if (priv.encodings.hex !== bitsToHex(bits)) errs.push('hex re-encode mismatch');
    if (priv.encodings.base64 !== bitsToB64(bits)) errs.push('base64 re-encode mismatch');
    var art = bitsToArt(bits);
    if (priv.encodings.ascii_art.length !== art.length ||
        priv.encodings.ascii_art.some(function (r, k) { return r !== art[k]; }))
      errs.push('ascii-art re-encode mismatch');
    if (priv.popcount !== popcount(bits)) errs.push('popcount mismatch');
    if (priv.symmetric180 !== sym180(bits)) errs.push('symmetry mismatch');
    return errs;
  }

  function validate(rec) {
    if (rec && rec._kind && GEO_KINDS.indexOf(rec._kind) >= 0) return validateGeo(rec);
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'title', 'cat', 'grid', 'bitstring', 'encodings', 'popcount', 'symmetric180'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-MATH-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.cat && CATS.indexOf(rec.cat) < 0) errs.push('bad category');
    if (rec.bitstring && !/^[01]{144}$/.test(rec.bitstring)) errs.push('bitstring must be 144 binary chars');
    if (rec._priv) {
      var p = rec._priv;
      PUB_KEYS.forEach(function (k) {
        if (JSON.stringify(rec[k]) !== JSON.stringify(p[k])) errs.push('field diverged from verified copy: ' + k);
      });
      errs = errs.concat(verify(p));
    }
    else errs.push('no private bit grid — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    if (rec && rec._kind && GEO_KINDS.indexOf(rec._kind) >= 0) return driftCheckGeo(rec, archiveSample);
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var bs = a.bitstring || (a[2]);
      if (bs && String(bs) === String(rec.bitstring)) errs.push('duplicate of archived grid bitstring');
    });
    return { ok: errs.length === 0, errors: errs };
  }

  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var r2 = JAHDB.prng(JAHDB.hashStr(String(seed) + nums[0]));
        /* fold the theme number into the bit grid deterministically */
        var rec2 = generate(seed, opts, r2);
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('math', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: CATS.concat(GEO_KINDS)
  });
})();
