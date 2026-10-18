(function(){'use strict';
/* JAH The Space Manufacturing Network Database generator — jahdb-db-space-manufacturing-network-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CSMN-";
var FIELDS=["The Nodes","The Chains","The Logistics"];
var TOPICS={
 "The Nodes": [
  "The Orbital Foundry \u2014 The Nodes",
  "The Orbital Foundry \u2014 Deep Dive \u2014 The Nodes",
  "The Asteroid Refinery \u2014 The Nodes",
  "The Asteroid Refinery \u2014 Deep Dive \u2014 The Nodes",
  "The Lunar Factory Complex \u2014 The Nodes",
  "The Lunar Factory Complex \u2014 Deep Dive \u2014 The Nodes",
  "The Construction Yard \u2014 The Nodes",
  "The Construction Yard \u2014 Deep Dive \u2014 The Nodes",
  "The Orbital Pharma Lab \u2014 The Nodes",
  "The Orbital Pharma Lab \u2014 Deep Dive \u2014 The Nodes",
  "The Network Architect's Method \u2014 The Nodes",
  "The Network Architect's Method \u2014 Deep Dive \u2014 The Nodes"
 ],
 "The Chains": [
  "The Supply Chain \u2014 The Chains",
  "The Supply Chain \u2014 Deep Dive \u2014 The Chains",
  "The Propellant Depot Network \u2014 The Chains",
  "The Propellant Depot Network \u2014 Deep Dive \u2014 The Chains",
  "The Tug Fleet \u2014 The Chains",
  "The Tug Fleet \u2014 Deep Dive \u2014 The Chains",
  "The Standards Regime \u2014 The Chains",
  "The Standards Regime \u2014 Deep Dive \u2014 The Chains",
  "The Debris Recycling \u2014 The Chains",
  "The Debris Recycling \u2014 Deep Dive \u2014 The Chains"
 ],
 "The Logistics": [
  "The Orbital Workforce \u2014 The Logistics",
  "The Orbital Workforce \u2014 Deep Dive \u2014 The Logistics",
  "The Space Insurance Market \u2014 The Logistics",
  "The Space Insurance Market \u2014 Deep Dive \u2014 The Logistics",
  "The Orbital Customs \u2014 The Logistics",
  "The Orbital Customs \u2014 Deep Dive \u2014 The Logistics",
  "The Network Data Layer \u2014 The Logistics",
  "The Network Data Layer \u2014 Deep Dive \u2014 The Logistics",
  "The Circular Network \u2014 The Logistics",
  "The Circular Network \u2014 Deep Dive \u2014 The Logistics",
  "The Industrial Finance \u2014 The Logistics",
  "The Industrial Finance \u2014 Deep Dive \u2014 The Logistics"
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
var gen={version:'jahdb-db-space-manufacturing-network-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-space-manufacturing-network',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
