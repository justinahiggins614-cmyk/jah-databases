(function(){'use strict';
/* JAH The Unsolved Nuclear Engineering Signature Database generator — jahdb-unsolved-nuclear-engineering-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USNES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Reactor Pressure Vessel Embrittlement Problem (Signature Edition) - Reactor Engineering",
  "The Departure From Nucleate Boiling Problem (Signature Edition) - Reactor Engineering",
  "The Two Phase Flow Modeling Problem (Signature Edition) - Reactor Engineering",
  "The Stress Corrosion Cracking Problem (Signature Edition) - Nuclear Materials",
  "The CRUD Induced Power Shift Problem (Signature Edition) - Reactor Engineering",
  "The Small Modular Reactor Economics Problem (Signature Edition) - Reactor Engineering",
  "The Load Following With Nuclear Problem (Signature Edition) - Reactor Engineering",
  "The Nuclear Cogeneration Problem (Signature Edition) - Reactor Engineering",
  "The Decommissioning Cost Estimation Problem (Signature Edition) - Reactor Engineering",
  "The High Assay Low Enriched Uranium Supply Problem (Signature Edition) - Reactor Engineering",
  "The Accident Tolerant Fuel Qualification Problem (Signature Edition) - Nuclear Materials"
 ],
 "Compounded": [
  "The Severe Accident Source Term Problem (Signature Edition) - Reactor Engineering",
  "The Hydrogen Risk Mitigation Problem (Signature Edition) - Reactor Engineering",
  "The Molten Corium Coolability Problem (Signature Edition) - Reactor Engineering",
  "The Containment Filtered Venting Problem (Signature Edition) - Reactor Engineering",
  "The Probabilistic Risk Assessment Completeness Problem (Signature Edition) - Reactor Engineering",
  "The Human Reliability Analysis Quantification Problem (Signature Edition) - Reactor Engineering",
  "The Digital Instrumentation and Control Assurance Problem (Signature Edition) - Reactor Engineering",
  "The Molten Salt Reactor Corrosion Problem (Signature Edition) - Nuclear Materials",
  "The TRISO Fuel Performance Problem (Signature Edition) - Nuclear Materials",
  "The Fast Reactor Cladding Compatibility Problem (Signature Edition) - Nuclear Materials",
  "The Fusion Tritium Breeding Problem (Signature Edition) - Fusion Energy",
  "The Fusion First Wall Materials Problem (Signature Edition) - Fusion Energy"
 ],
 "Advanced": [
  "The Tokamak Disruption Prediction Problem (Signature Edition) - Fusion Energy",
  "The Stellarator Optimization Problem (Signature Edition) - Fusion Energy",
  "The Inertial Confinement Ignition Gain Problem (Signature Edition) - Fusion Energy",
  "The Nuclear Waste Transmutation Problem (Signature Edition) - Reactor Engineering",
  "The Deep Geological Repository Problem (Signature Edition) - Reactor Engineering",
  "The Microreactor Autonomous Control Problem (Signature Edition) - Reactor Engineering",
  "The Space Reactor Heat Rejection Problem (Signature Edition) - Reactor Engineering",
  "The Multiphysics Reactor Coupling Problem (Signature Edition) - Reactor Engineering",
  "The Neutron Transport Exact Solution Problem (Signature Edition) - Reactor Engineering",
  "The Spent Fuel Dry Cask Storage Problem (Signature Edition) - Reactor Engineering",
  "The Unified Nuclear Energy System Problem (Signature Edition) - Fusion Energy"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Nuclear Engineering Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-nuclear-engineering-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-nuclear-engineering-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-nuclear-engineering-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
