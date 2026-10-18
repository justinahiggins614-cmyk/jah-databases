(function(){'use strict';
/* JAH The Unsolved Nuclear Engineering Database generator — jahdb-unsolved-nuclear-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USNE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Reactor Pressure Vessel Embrittlement Problem - Reactor Engineering",
  "The Departure From Nucleate Boiling Problem - Reactor Engineering",
  "The Two Phase Flow Modeling Problem - Reactor Engineering",
  "The Stress Corrosion Cracking Problem - Nuclear Materials",
  "The CRUD Induced Power Shift Problem - Reactor Engineering",
  "The Small Modular Reactor Economics Problem - Reactor Engineering",
  "The Load Following With Nuclear Problem - Reactor Engineering",
  "The Nuclear Cogeneration Problem - Reactor Engineering",
  "The Decommissioning Cost Estimation Problem - Reactor Engineering",
  "The High Assay Low Enriched Uranium Supply Problem - Reactor Engineering",
  "The Accident Tolerant Fuel Qualification Problem - Nuclear Materials"
 ],
 "Compounded": [
  "The Severe Accident Source Term Problem - Reactor Engineering",
  "The Hydrogen Risk Mitigation Problem - Reactor Engineering",
  "The Molten Corium Coolability Problem - Reactor Engineering",
  "The Containment Filtered Venting Problem - Reactor Engineering",
  "The Probabilistic Risk Assessment Completeness Problem - Reactor Engineering",
  "The Human Reliability Analysis Quantification Problem - Reactor Engineering",
  "The Digital Instrumentation and Control Assurance Problem - Reactor Engineering",
  "The Molten Salt Reactor Corrosion Problem - Nuclear Materials",
  "The TRISO Fuel Performance Problem - Nuclear Materials",
  "The Fast Reactor Cladding Compatibility Problem - Nuclear Materials",
  "The Fusion Tritium Breeding Problem - Fusion Energy",
  "The Fusion First Wall Materials Problem - Fusion Energy"
 ],
 "Advanced": [
  "The Tokamak Disruption Prediction Problem - Fusion Energy",
  "The Stellarator Optimization Problem - Fusion Energy",
  "The Inertial Confinement Ignition Gain Problem - Fusion Energy",
  "The Nuclear Waste Transmutation Problem - Reactor Engineering",
  "The Deep Geological Repository Problem - Reactor Engineering",
  "The Microreactor Autonomous Control Problem - Reactor Engineering",
  "The Space Reactor Heat Rejection Problem - Reactor Engineering",
  "The Multiphysics Reactor Coupling Problem - Reactor Engineering",
  "The Neutron Transport Exact Solution Problem - Reactor Engineering",
  "The Spent Fuel Dry Cask Storage Problem - Reactor Engineering",
  "The Unified Nuclear Energy System Problem - Fusion Energy"
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
var gen={version:'jahdb-unsolved-nuclear-engineering-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-nuclear-engineering',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
