(function(){'use strict';
/* JAH The Space Manufacturing Network Signature Database generator — jahdb-db-space-manufacturing-network-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CSMNS-";
var FIELDS=["The Nodes","The Chains","The Logistics"];
var TOPICS={
 "The Nodes": [
  "The Orbital Foundry (Signature Edition) \u2014 The Nodes",
  "The Signature Method for The Orbital Foundry \u2014 The Nodes",
  "The Asteroid Refinery (Signature Edition) \u2014 The Nodes",
  "The Signature Method for The Asteroid Refinery \u2014 The Nodes",
  "The Lunar Factory Complex (Signature Edition) \u2014 The Nodes",
  "The Signature Method for The Lunar Factory Complex \u2014 The Nodes",
  "The Construction Yard (Signature Edition) \u2014 The Nodes",
  "The Signature Method for The Construction Yard \u2014 The Nodes",
  "The Orbital Pharma Lab (Signature Edition) \u2014 The Nodes",
  "The Signature Method for The Orbital Pharma Lab \u2014 The Nodes",
  "The Network Architect's Method (Signature Edition) \u2014 The Nodes",
  "The Signature Method for The Network Architect's Method \u2014 The Nodes"
 ],
 "The Chains": [
  "The Supply Chain (Signature Edition) \u2014 The Chains",
  "The Signature Method for The Supply Chain \u2014 The Chains",
  "The Propellant Depot Network (Signature Edition) \u2014 The Chains",
  "The Signature Method for The Propellant Depot Network \u2014 The Chains",
  "The Tug Fleet (Signature Edition) \u2014 The Chains",
  "The Signature Method for The Tug Fleet \u2014 The Chains",
  "The Standards Regime (Signature Edition) \u2014 The Chains",
  "The Signature Method for The Standards Regime \u2014 The Chains",
  "The Debris Recycling (Signature Edition) \u2014 The Chains",
  "The Signature Method for The Debris Recycling \u2014 The Chains"
 ],
 "The Logistics": [
  "The Orbital Workforce (Signature Edition) \u2014 The Logistics",
  "The Signature Method for The Orbital Workforce \u2014 The Logistics",
  "The Space Insurance Market (Signature Edition) \u2014 The Logistics",
  "The Signature Method for The Space Insurance Market \u2014 The Logistics",
  "The Orbital Customs (Signature Edition) \u2014 The Logistics",
  "The Signature Method for The Orbital Customs \u2014 The Logistics",
  "The Network Data Layer (Signature Edition) \u2014 The Logistics",
  "The Signature Method for The Network Data Layer \u2014 The Logistics",
  "The Circular Network (Signature Edition) \u2014 The Logistics",
  "The Signature Method for The Circular Network \u2014 The Logistics",
  "The Industrial Finance (Signature Edition) \u2014 The Logistics",
  "The Signature Method for The Industrial Finance \u2014 The Logistics"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Space Manufacturing Study — "+safe+"\n"
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
    name:topic+' — space manufacturing record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A space manufacturing record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-space-manufacturing-network-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-space-manufacturing-network-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
