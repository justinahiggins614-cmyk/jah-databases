(function(){'use strict';
/* JAH The Civilization Milestones Signature Database generator — jahdb-db-civilization-milestones-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CCMDS-";
var FIELDS=["Crossed","Crossing Now","Ahead"];
var TOPICS={
 "Crossed": [
  "The Taming of Fire (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Taming of Fire \u2014 Crossed",
  "The Agricultural Revolution (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Agricultural Revolution \u2014 Crossed",
  "The Invention of Writing (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Invention of Writing \u2014 Crossed",
  "The Steam Revolution (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Steam Revolution \u2014 Crossed",
  "The Electric Age (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Electric Age \u2014 Crossed",
  "The Conquest of Air (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Conquest of Air \u2014 Crossed",
  "The Space Age (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Space Age \u2014 Crossed",
  "The Networked Mind (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Networked Mind \u2014 Crossed",
  "The Read Genome (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Read Genome \u2014 Crossed",
  "The Printing Press (Signature Edition) \u2014 Crossed",
  "The Signature Method for The Printing Press \u2014 Crossed"
 ],
 "Crossing Now": [
  "The Thinking Machines (Signature Edition) \u2014 Crossing Now",
  "The Signature Method for The Thinking Machines \u2014 Crossing Now",
  "The Clean Energy Transition (Signature Edition) \u2014 Crossing Now",
  "The Signature Method for The Clean Energy Transition \u2014 Crossing Now"
 ],
 "Ahead": [
  "The Mars Landing (Signature Edition) \u2014 Ahead",
  "The Signature Method for The Mars Landing \u2014 Ahead",
  "The Fusion Ignition (Signature Edition) \u2014 Ahead",
  "The Signature Method for The Fusion Ignition \u2014 Ahead",
  "The Longevity Escape (Signature Edition) \u2014 Ahead",
  "The Signature Method for The Longevity Escape \u2014 Ahead",
  "The Interstellar Probe (Signature Edition) \u2014 Ahead",
  "The Signature Method for The Interstellar Probe \u2014 Ahead",
  "The Milestone Keeper's Method (Signature Edition) \u2014 Ahead",
  "The Signature Method for The Milestone Keeper's Method \u2014 Ahead"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Civilization Milestone Study — "+safe+"\n"
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
    name:topic+' — civilization milestone record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A civilization milestone record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-civilization-milestones-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-civilization-milestones-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
