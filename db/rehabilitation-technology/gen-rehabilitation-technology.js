(function(){'use strict';
/* JAH Rehabilitation Technology Database generator — jahdb-rehabilitation-technology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RT-";
var FIELDS=["exoskeletons", "functional electrical stimulation", "brain-computer interfaces", "prosthetic control", "gait training", "outcome measurement"];
var TOPICS=[
    {t: "Principles of Neurorehabilitation", b: "Use-dependent plasticity, learned non-use, and critical periods: the neuroscience every rehab device serves."},
    {t: "Robotic Gait Trainers", b: "Lokomat-style body-weight-supported treadmill training: high step counts early after stroke and spinal cord injury."},
    {t: "Exoskeletons", b: "Powered hip-knee-ankle systems for paraplegia and stroke: torque assistance, balance, and the path to community use."},
    {t: "Upper-Limb Robots", b: "End-effector and exoskeleton arms deliver the hundreds of repetitions hands need to relearn reach and grasp."},
    {t: "Functional Electrical Stimulation", b: "Stimulating paralyzed muscles to contract: foot-drop stimulators, grasp systems, and FES cycling."},
    {t: "Brain-Computer Interfaces", b: "Decoding motor intent from EEG or implants to drive stimulators, robots, or cursors \u2014 bypassing the broken pathway."},
    {t: "Constraint-Induced Therapy", b: "Forcing use of the affected limb (mitt on the good hand) reverses learned non-use \u2014 low-tech, high-evidence."},
    {t: "Virtual Reality Rehab", b: "Engaging environments multiply repetitions and motivation: VR turns tedious exercises into games patients actually do."},
    {t: "Assistive Technology", b: "Wheelchairs, communication devices, environmental controls: engineering independence when recovery plateaus."},
    {t: "Outcome Measurement", b: "Standardized scales (FIM, Berg, ARAT) quantify recovery: what gets measured gets rehabilitated."},
    {t: "Telerehabilitation", b: "Remote supervision and home devices extend therapy beyond clinic walls \u2014 access multiplied by connectivity."},
    {t: "Pediatric Rehab Tech", b: "Growing bodies and developing brains need adaptable, playful systems: early intervention shapes lifelong trajectories."}
];
var PRINCIPLES=[
    {n: "Neuroplasticity is the mechanism", e: "", s: "Repetition, intensity, and task-specificity drive rewiring: technology must deliver the dose the brain needs."},
    {n: "Assist as needed, no more", e: "", s: "Robots that do the work for patients teach dependence: adaptive assistance fades as ability returns."},
    {n: "Measure function, not motion", e: "", s: "Fugl-Meyer, 10-meter walk, and real-world use beat joint angles as the outcomes that matter."}
];
var USES=["Prescribing exoskeleton training", "Setting up FES programs", "Evaluating BCI candidates", "Measuring rehab outcomes"];
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
    id:id, t:tp.t, g:field, name:"Rehabilitation Technology"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Rehabilitation Technology Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-rehabilitation-technology-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-rehabilitation-technology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("rehabilitation-technology",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
