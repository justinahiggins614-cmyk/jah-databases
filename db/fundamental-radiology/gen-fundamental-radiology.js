(function(){'use strict';
/* JAH Fundamentals of Radiology Database generator — jahdb-fundamental-radiology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RAD-";
var FIELDS=["X-ray physics", "CT", "MRI", "ultrasound", "nuclear medicine", "interpretation"];
var TOPICS=[
    {t: "How X-rays Are Made", b: "Bremsstrahlung and characteristic radiation from electron-bombarded anodes: kilovoltage sets penetration, milliamperage sets quantity."},
    {t: "X-ray Image Formation", b: "Dense bone attenuates more than soft tissue: the shadow image is a 2-D projection of 3-D attenuation differences."},
    {t: "Contrast and Scatter", b: "Grids reject scatter, kVp trades contrast for penetration: image quality is controlled physics, not luck."},
    {t: "Computed Tomography", b: "Rotating X-ray source plus reconstruction algorithms (filtered back-projection, iterative) slice the body into cross-sections."},
    {t: "CT Numbers: Hounsfield Units", b: "Water = 0, air = \u22121000, bone = +1000+: calibrated density numbers make CT quantitative."},
    {t: "MRI: Spins in a Magnet", b: "Aligning hydrogen spins in a strong magnet, tipping them with RF, and listening to their re-emission builds images from chemistry."},
    {t: "T1 vs T2 Weighting", b: "T1 shows anatomy (fat bright), T2 shows pathology (fluid bright): sequence choice is diagnostic strategy."},
    {t: "Ultrasound: Sound as Sight", b: "Piezoelectric pulses echo off tissue boundaries; Doppler shifts reveal blood flow direction and speed \u2014 no radiation involved."},
    {t: "Nuclear Medicine", b: "Tracer radioisotopes (Tc-99m, FDG) image function, not just form: PET shows metabolism, the hallmark of cancer and brain activity."},
    {t: "Contrast Agents", b: "Iodine (CT), gadolinium (MRI), microbubbles (ultrasound) amplify differences \u2014 each with allergy and kidney considerations."},
    {t: "Reading Images Systematically", b: "Checklists (ABCDE, search patterns) defeat satisfaction-of-search: methodical viewing finds what casual glances miss."},
    {t: "Radiation Safety", b: "Justification, optimization, dose limits: ALARA governs every order, and shielding, distance, and time govern every room."}
];
var PRINCIPLES=[
    {n: "Attenuation", e: "I = I\u2080\u00b7e^(\u2212\u03bcx)", s: "X-ray intensity falls exponentially with tissue thickness and density \u2014 the contrast mechanism."},
    {n: "Larmor frequency", e: "\u03c9 = \u03b3\u00b7B\u2080", s: "Hydrogen nuclei precess at a frequency set by magnetic field strength \u2014 MRI's tuning dial."},
    {n: "ALARA", e: "dose as low as reasonably achievable", s: "Every exposure must be justified and minimized \u2014 the ethical law of radiology."}
];
var USES=["Interpreting chest X-rays", "Protocoling CT scans", "Reading brain MRIs", "Performing obstetric ultrasounds"];
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
    id:id, t:tp.t, g:field, name:"Radiology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Radiology demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-radiology-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-fundamental-radiology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-radiology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
