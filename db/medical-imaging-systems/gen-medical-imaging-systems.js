(function(){'use strict';
/* JAH Medical Imaging Systems Database generator — jahdb-medical-imaging-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MIS-";
var FIELDS=["X-ray and fluoroscopy", "CT scanners", "MRI systems", "ultrasound machines", "nuclear medicine", "PACS and AI"];
var TOPICS=[
    {t: "X-ray Systems", b: "Tube, generator, detector: kVp/mAs technique charts, grids, and digital detectors (CsI, flat-panel) \u2014 the oldest modality, still first-line."},
    {t: "Fluoroscopy", b: "Real-time X-ray for interventions: pulsed fluoro, last-image-hold, and dose tracking keep procedures safe."},
    {t: "CT Architecture", b: "Rotating gantry, slip rings, multi-detector arrays: helical acquisition and iterative reconstruction in seconds."},
    {t: "CT Dose Management", b: "CTDI, DLP, tube-current modulation, and iterative reconstruction: engineering dose down while keeping diagnosis up."},
    {t: "MRI Magnets", b: "Superconducting 1.5T/3T magnets, gradients, and RF coils: the most complex machines in the hospital, imaging chemistry itself."},
    {t: "MRI Sequences", b: "T1, T2, FLAIR, diffusion, perfusion: each sequence asks tissue a different question \u2014 protocoling is diagnostic strategy."},
    {t: "Ultrasound Machines", b: "Transducer arrays, beamforming, and Doppler: real-time, portable, radiation-free \u2014 operator skill is the image quality."},
    {t: "PET/CT and SPECT", b: "Radiotracers (FDG) reveal metabolism; fused with CT anatomy: function plus form for cancer staging."},
    {t: "Image Reconstruction", b: "Filtered back-projection, iterative, and deep-learning reconstruction turn raw signals into pictures \u2014 algorithms are hardware now."},
    {t: "PACS and Workflow", b: "DICOM networks, hanging protocols, and voice recognition: the informatics plumbing of modern radiology departments."},
    {t: "AI in Imaging", b: "Detection, triage, and quantification algorithms: validated against ground truth, deployed as assistants, never oracles."},
    {t: "Choosing the Modality", b: "Speed, cost, contrast, radiation, availability: the decision tree from clinical question to the right machine."}
];
var PRINCIPLES=[
    {n: "Contrast comes from physics", e: "", s: "Every modality images a physical property (attenuation, proton density, echogenicity, tracer uptake) \u2014 know the property, know the image."},
    {n: "Dose is a design parameter", e: "", s: "Image quality, scan time, and radiation dose trade against each other: ALARA is engineered into protocols, not wished for."},
    {n: "Artifacts lie convincingly", e: "", s: "Beam hardening, motion, metal, and aliasing all mimic disease: recognizing artifacts is part of reading every image."}
];
var USES=["Specifying CT scanner purchases", "Optimizing MRI protocols", "Managing imaging dose", "Evaluating AI imaging tools"];
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
    id:id, t:tp.t, g:field, name:"Medical Imaging Systems"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Medical Imaging Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-medical-imaging-systems-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-medical-imaging-systems-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("medical-imaging-systems",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
