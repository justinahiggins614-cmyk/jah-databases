(function(){'use strict';
/* JAH Biomedical Device Design Database generator — jahdb-biomedical-device-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BDD-";
var FIELDS=["physiological sensing", "signal processing", "electrical safety", "imaging interfaces", "therapeutic devices", "regulatory strategy"];
var TOPICS=[
    {t: "The Device Design Process", b: "Needs finding \u2192 specs \u2192 concept \u2192 prototype \u2192 verification \u2192 validation \u2192 regulatory: the disciplined path from idea to clinic."},
    {t: "ECG: Reading the Heart", b: "Electrodes, instrumentation amplifiers, and filtering extract millivolt cardiac signals from a noisy, moving body."},
    {t: "Pulse Oximetry", b: "Two-wavelength photoplethysmography computes oxygen saturation: Beer-Lambert law worn on a fingertip."},
    {t: "Blood Pressure Measurement", b: "Oscillometric cuffs and arterial lines each trade convenience against accuracy \u2014 the physics of each method."},
    {t: "Electrical Safety (IEC 60601)", b: "Patient leakage under 10 \u00b5A, defibrillation-proof isolation, creepage distances: the numbers that keep devices from shocking patients."},
    {t: "Defibrillators", b: "Capacitor-charged biphasic shocks reset fibrillating hearts: energy, waveform, and impedance compensation."},
    {t: "Infusion Pumps", b: "Peristaltic and syringe mechanisms meter drugs at mL/hour precision: occlusion alarms and drug libraries prevent overdoses."},
    {t: "Neurostimulators", b: "Deep-brain, spinal-cord, and vagus stimulators: charge-balanced waveforms and hermetic packaging for decades inside the body."},
    {t: "Point-of-Care Diagnostics", b: "Lateral-flow, microfluidic, and electrochemical sensors bring the lab to the bedside \u2014 accuracy under real-world conditions."},
    {t: "Wearables and Remote Monitoring", b: "Continuous ECG, glucose, and activity tracking: signal quality, battery life, and clinical actionability decide value."},
    {t: "Human Factors Engineering", b: "Use-error analysis, simulated-use testing, and IEC 62366: designing for stressed clinicians in chaotic rooms."},
    {t: "Regulatory Strategy", b: "510(k) substantial equivalence vs PMA vs De Novo: choosing the pathway shapes the entire development plan and budget."}
];
var PRINCIPLES=[
    {n: "Safety is designed, not added", e: "", s: "IEC 60601 isolation, leakage currents, and single-fault analysis shape the circuit from the first sketch."},
    {n: "Physiology sets the specs", e: "", s: "Electrode impedance, motion artifact, and the body's own signals define what the electronics must achieve."},
    {n: "Usability is clinical efficacy", e: "", s: "A device clinicians misuse is a failed device: human-factors validation is part of the design, not decoration."}
];
var USES=["Designing patient monitors", "Developing wearable sensors", "Planning regulatory submissions", "Testing electrical safety"];
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
    id:id, t:tp.t, g:field, name:"Biomedical Device Design"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Biomedical Device Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-biomedical-device-design-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-biomedical-device-design-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("biomedical-device-design",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
