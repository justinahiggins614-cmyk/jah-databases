(function(){'use strict';
/* JAH Emerging Technology Maturity Database generator — jahdb-emerging-technology-maturity-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMERTMS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Technology Readiness Levels (Signature Edition)", "The Hype Cycle (Signature Edition)", "Demos vs Deployments (Signature Edition)", "AI Maturity (Signature Edition)", "Quantum Computing (Signature Edition)", "Biotechnology Frontiers (Signature Edition)", "Energy Technologies (Signature Edition)", "Space Technologies (Signature Edition)", "Assessing Claims (Signature Edition)", "Timing Adoption (Signature Edition)", "Teaching Tech Assessment (Signature Edition)"], "Compounded": ["The Annual Tech Review (Signature Edition)", "Assessing AI Agents (Signature Edition)", "Robotics Maturity (Signature Edition)", "Brain Interfaces (Signature Edition)", "Synthetic Biology (Signature Edition)", "Advanced Materials (Signature Edition)", "6G and Beyond (Signature Edition)", "Edge Computing (Signature Edition)", "Digital Twins (Signature Edition)", "Web3 Assessment (Signature Edition)", "AR/VR Maturity (Signature Edition)", "Autonomous Vehicles (Signature Edition)"], "Advanced": ["Fusion Update (Signature Edition)", "Carbon Removal (Signature Edition)", "Alternative Proteins (Signature Edition)", "Smart Grids (Signature Edition)", "Personalized Medicine (Signature Edition)", "Aging Research (Signature Edition)", "Ocean Tech (Signature Edition)", "AgTech (Signature Edition)", "Construction Tech (Signature Edition)", "The Prediction Ledger (Signature Edition)", "Signals vs Noise (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — technology assessment guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — technology assessment guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology assessment guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"emerging-technology-maturity-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-emerging-technology-maturity-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("emerging-technology-maturity-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
