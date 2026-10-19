(function(){'use strict';
/* JAH Prosthetics Engineering Database generator — jahdb-prosthetics-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic synthesis record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PE-";
var FIELDS=["socket design", "knee mechanisms", "feet and ankles", "upper-limb systems", "materials", "neural interfaces"];
var TOPICS=[
    {t: "Levels of Amputation", b: "Transtibial, transfemoral, transradial, transhumeral: each level sets the biomechanical problem the device must solve."},
    {t: "Socket Biomechanics", b: "Total-surface-bearing vs patellar-tendon-bearing: distributing load over pressure-tolerant tissue without choking circulation."},
    {t: "Suspension", b: "Suction, pin-lock, and vacuum systems hold the limb on: pistoning wastes energy and wounds skin \u2014 suspension is efficiency."},
    {t: "Prosthetic Knees", b: "Single-axis, polycentric, hydraulic, microprocessor (C-Leg, Genium): stance stability plus swing control, escalating in intelligence."},
    {t: "Feet and Ankles", b: "SACH, energy-storing carbon (Flex-Foot), powered ankles (BiOM): returning push-off energy step after step."},
    {t: "Gait Analysis", b: "Force plates and motion capture quantify symmetry, speed, and metabolic cost \u2014 the scoreboard for every design change."},
    {t: "Upper-Limb Prostheses", b: "Body-powered hooks vs myoelectric hands: grip patterns, weight, and control intuitiveness traded per patient's life."},
    {t: "Myoelectric Control", b: "EMG electrodes read residual muscle signals; pattern recognition now decodes multiple grasps from the same muscles."},
    {t: "Osseointegration", b: "Bone-anchored implants skip the socket entirely: direct skeletal attachment with infection management at the skin portal."},
    {t: "Pediatric Prosthetics", b: "Growing children need adjustable, rugged, affordable limbs replaced as they grow \u2014 a different engineering economy."},
    {t: "Sports Prostheses", b: "Running blades (J-shaped carbon) and activity limbs: specialized tools that return amputees to competition."},
    {t: "Neural Interfaces", b: "Targeted muscle reinnervation and implanted electrodes are closing the loop toward thought-controlled limbs."}
];
var PRINCIPLES=[
    {n: "The socket is the device", e: "", s: "No component matters if the socket hurts: pressure distribution over load-tolerant tissue decides success."},
    {n: "Energy return is efficiency", e: "", s: "Feet and knees that store and return gait energy cut the amputee's metabolic cost \u2014 the performance metric that matters."},
    {n: "Reliability is dignity", e: "", s: "A knee that buckles destroys trust: prosthetic mechanisms are designed for fail-safe, then for performance."}
];
var USES=["Fitting transtibial sockets", "Selecting microprocessor knees", "Designing myoelectric hands", "Analyzing amputee gait"];
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
    id:id, t:tp.t, g:field, name:"Prosthetics Engineering"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Prosthetics Synthesis demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-prosthetics-engineering-1.0")\nprint("OK: '+id+' generated synthesis record")\n',note:'Generator sample demo.'},
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
var gen={version:"jahdb-prosthetics-engineering-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("prosthetics-engineering",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
