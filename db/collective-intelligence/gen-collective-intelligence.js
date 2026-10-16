(function(){'use strict';
/* JAH The Collective & Swarm Intelligence Database generator — jahdb-collective-intelligence-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COLI-";
var FIELDS=["intelligence-scale abilities"];
var TOPICS={
 "intelligence-scale abilities": [
  "Ant Colony Foraging Optimization \u2014 intelligence-scale abilities",
  "Ant Colony Foraging Optimization (Signature Edition) \u2014 intelligence-scale abilities",
  "Bacterial Quorum Sensing \u2014 intelligence-scale abilities",
  "Bacterial Quorum Sensing (Signature Edition) \u2014 intelligence-scale abilities",
  "Prediction Markets \u2014 intelligence-scale abilities",
  "Prediction Markets (Signature Edition) \u2014 intelligence-scale abilities",
  "Scientific Collaboration Networks \u2014 intelligence-scale abilities",
  "Scientific Collaboration Networks (Signature Edition) \u2014 intelligence-scale abilities",
  "Open-Source Software Coordination \u2014 intelligence-scale abilities",
  "Open-Source Software Coordination (Signature Edition) \u2014 intelligence-scale abilities",
  "Distributed Sensor Networks \u2014 intelligence-scale abilities",
  "Distributed Sensor Networks (Signature Edition) \u2014 intelligence-scale abilities",
  "Crowd Problem-Solving \u2014 intelligence-scale abilities",
  "Crowd Problem-Solving (Signature Edition) \u2014 intelligence-scale abilities",
  "Cultural Accumulation Across Generations \u2014 intelligence-scale abilities",
  "Cultural Accumulation Across Generations (Signature Edition) \u2014 intelligence-scale abilities",
  "Swarm Robotics Coordination \u2014 intelligence-scale abilities",
  "Swarm Robotics Coordination (Signature Edition) \u2014 intelligence-scale abilities",
  "Wisdom of Crowds Estimation \u2014 intelligence-scale abilities",
  "Wisdom of Crowds Estimation (Signature Edition) \u2014 intelligence-scale abilities"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Collective Intelligence — "+safe+"\n"
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
    name:topic+' — collective intelligence ability',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A collective intelligence ability of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-collective-intelligence-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('collective-intelligence',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
