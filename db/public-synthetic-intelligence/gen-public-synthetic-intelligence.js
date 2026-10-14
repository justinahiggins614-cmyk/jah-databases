(function(){'use strict';
/* JAH Public Synthetic Intelligence Database generator — jahdb-public-synthetic-intelligence-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SI-";
var FIELDS=["approaches", "concepts", "history", "research-areas", "systems"];
var TOPICS={
 "concepts": [
  "Synthetic Intelligence",
  "Synthetic Cognition",
  "Synthetic Phenomenology",
  "Machine Consciousness",
  "Whole Brain Emulation",
  "Mind Uploading",
  "Neuromorphic Computing",
  "Synthetic Theory of Mind",
  "Embodied Synthetic Intelligence",
  "Enactive Intelligence",
  "Synthetic Curiosity and Intrinsic Motivation",
  "Artificial General Intelligence as Synthetic Intellect"
 ],
 "approaches": [
  "SOAR Cognitive Architecture",
  "ACT-R Cognitive Architecture",
  "OpenCog and Hyperon",
  "NARS — Non-Axiomatic Reasoning System",
  "Predictive Processing and the Free Energy Principle",
  "Active Inference",
  "Integrated Information Theory",
  "Global Workspace Theory",
  "Neuroevolution — NEAT and HyperNEAT",
  "Reservoir Computing and Liquid State Machines",
  "World Models",
  "Agent-Based Synthetic Intelligence"
 ],
 "history": [
  "The Turing Test (1950)",
  "The Dartmouth Conference (1956)",
  "Perceptrons and the First AI Winter",
  "The Chinese Room (1980)",
  "The Hard Problem of Consciousness (1995)",
  "The Cog Robot (MIT, 1990s)",
  "Kismet the Sociable Robot (2000)",
  "The Blue Brain Project (2005)",
  "The Human Brain Project (2013)",
  "DARPA SyNAPSE (2008)",
  "The Lovelace Test (2001)",
  "Carbon Copies and the 2045 Initiative (2011–2012)"
 ],
 "systems": [
  "IBM TrueNorth",
  "Intel Loihi",
  "SpiNNaker",
  "iCub Humanoid Robot",
  "DishBrain — Cortical Labs (2022)",
  "Xenobots (2020)",
  "Organoid Intelligence — Johns Hopkins (2023)",
  "Boids (1986)",
  "Tierra (1991)",
  "Avida",
  "Neuralink Brain-Computer Interface",
  "Kernel (Bryan Johnson)"
 ],
 "research-areas": [
  "Connectomics",
  "Brain-Computer Interfaces",
  "Synthetic Emotion and Affective Computing",
  "Swarm Intelligence",
  "Artificial Life",
  "Synthetic Developmental Robotics",
  "Wetware Computing and Living Computers",
  "Digital Twin Brains",
  "Synthetic Neurogenesis",
  "Machine Phenomenology Research",
  "The BRAIN Initiative (2013)",
  "Synthetic Immune Systems"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# SI Explorer — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — synthetic intelligence study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A synthetic intelligence study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'si-explorer',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-synthetic-intelligence-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-synthetic-intelligence',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
