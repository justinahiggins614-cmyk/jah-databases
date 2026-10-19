(function(){'use strict';
/* JAH Biosensor Development Database generator — jahdb-biosensor-development-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BD-";
var FIELDS=["biorecognition", "transducers", "electrochemical sensors", "optical sensors", "microfluidics", "validation"];
var TOPICS=[
    {t: "What Biosensors Are", b: "Biorecognition (enzyme, antibody, DNA) plus transducer (electrochemical, optical): biology's specificity with electronics' readability."},
    {t: "Glucose Sensors: The Model", b: "Enzyme electrodes in billions of test strips and CGMs: the most successful biosensor ever, and its design lessons."},
    {t: "Electrochemical Transducers", b: "Amperometric, potentiometric, impedimetric: measuring the electrons biology moves."},
    {t: "Optical Transducers", b: "SPR, fluorescence, colorimetric: light-based readouts from benchtop to phone-camera diagnostics."},
    {t: "Lateral-Flow Assays", b: "Pregnancy and COVID tests: capillary-driven, instrument-free biosensing at massive scale."},
    {t: "Microfluidic Integration", b: "Lab-on-chip: sample prep, reaction, and detection in microliters \u2014 the path to point-of-care."},
    {t: "Wearable Biosensors", b: "Sweat, interstitial fluid, tears: noninvasive monitoring's frontier, fighting biofouling and calibration drift."},
    {t: "Environmental Biosensors", b: "Detecting pollutants, pathogens, and toxins in water and air: sentinels for public health."},
    {t: "Aptamers and MIPs", b: "Synthetic recognition elements: stable, cheap alternatives to antibodies expanding what's sensable."},
    {t: "Signal Amplification", b: "Enzymatic, nanoparticle, and CRISPR-based amplification pushing detection to single molecules."},
    {t: "Validation and Regulation", b: "Analytical sensitivity/specificity, clinical trials, FDA 510(k)/PMA: the evidence ladder for diagnostics."},
    {t: "Manufacturing", b: "Screen printing, roll-to-roll, and QC at billion-unit scale: making sensors cheap enough to be disposable."}
];
var PRINCIPLES=[
    {n: "Selectivity is the product", e: "", s: "A sensor that responds to everything measures nothing: the biorecognition element defines value."},
    {n: "Matrix effects are real", e: "", s: "Blood, saliva, and wastewater foul sensors: validation in the real sample, not buffer, decides."},
    {n: "Calibration drifts", e: "", s: "Every sensor ages: built-in references and recalibration schedules are part of the design."}
];
var USES=["Designing glucose monitors", "Developing rapid diagnostics", "Building environmental sensors", "Validating assay performance"];
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
    id:id, t:tp.t, g:field, name:"Biosensor Development"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Biosensor Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-biosensor-development-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-biosensor-development-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("biosensor-development",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
