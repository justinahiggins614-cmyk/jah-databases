(function(){'use strict';
/* JAH Fundamentals of Organic Chemistry Database generator — jahdb-fundamental-organic-chemistry-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OC-";
var FIELDS=["bonding and structure", "stereochemistry", "reaction mechanisms", "spectroscopy", "synthesis", "carbonyl chemistry"];
var TOPICS=[
    {t: "Why Carbon Is Special", b: "Four bonds, catenation, and similar bond strengths let carbon build chains, rings, and 3-D frameworks no other element matches."},
    {t: "Hybridization and Geometry", b: "sp\u00b3 tetrahedral, sp\u00b2 trigonal planar, sp linear: orbital mixing predicts molecular shape, and shape predicts reactivity."},
    {t: "Functional Groups", b: "Alcohols, ketones, acids, amines: each group is a reactivity unit \u2014 recognizing them is reading the language of molecules."},
    {t: "Stereochemistry", b: "Chirality (handedness) makes mirror-image molecules behave differently in bodies: thalidomide is the tragic proof that shape matters."},
    {t: "Conformational Analysis", b: "Rotations about single bonds favor staggered over eclipsed (ethane's 12 kJ/mol barrier) \u2014 molecules spend most time in low-energy shapes."},
    {t: "Acids, Bases, and pKa", b: "pKa tables predict proton transfers: the stronger acid and stronger base always react to make their weaker conjugates."},
    {t: "Substitution: SN1 vs SN2", b: "Backside attack (SN2, inversion) vs carbocation intermediates (SN1, racemization): substrate, nucleophile, and solvent decide."},
    {t: "Elimination: E1 vs E2", b: "Anti-periplanar geometry favors the more substituted alkene (Zaitsev) \u2014 bases pull protons, leaving groups leave."},
    {t: "Electrophilic Addition", b: "\u03c0 bonds attack electrophiles first: Markovnikov's rule puts the proton where the most stable carbocation forms."},
    {t: "Spectroscopy: Reading Molecules", b: "IR shows functional groups, NMR maps carbon-hydrogen frameworks, mass spec weighs fragments \u2014 structure from spectra."},
    {t: "Carbonyl Chemistry", b: "The polarized C=O bond invites nucleophiles: aldehydes/ketones add, acids/esters substitute \u2014 the heart of synthesis."},
    {t: "Retrosynthesis", b: "Design syntheses backward: break target bonds into available starting materials, then run the plan forward."}
];
var PRINCIPLES=[
    {n: "Tetrahedral carbon", e: "bond angle 109.5\u00b0", s: "sp\u00b3 carbon arranges four bonds tetrahedrally \u2014 the geometry behind all organic shape."},
    {n: "Rate = k[A][B]", e: "mechanism from kinetics", s: "Reaction orders reveal the molecularity of the slow step \u2014 mechanisms are inferred, not seen."},
    {n: "Curtin-Hammett", e: "product ratio from \u0394\u0394G\u2021", s: "When conformers interconvert fast, transition-state energies \u2014 not ground states \u2014 decide products."}
];
var USES=["Designing drug syntheses", "Developing new polymers", "Analyzing unknown compounds", "Planning multi-step preparations"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Organic Chemistry"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Organic Chemistry demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-organic-chemistry-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-fundamental-organic-chemistry-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-organic-chemistry",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
