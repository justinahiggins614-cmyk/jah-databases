(function(){'use strict';
/* JAH The Future Education System Database generator — jahdb-db-future-education-system-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CFES-";
var FIELDS=["The Campus","The Curriculum","The Method"];
var TOPICS={
 "The Campus": [
  "The Forest School \u2014 The Campus",
  "The Forest School \u2014 Deep Dive \u2014 The Campus",
  "The Orbital Academy \u2014 The Campus",
  "The Orbital Academy \u2014 Deep Dive \u2014 The Campus",
  "The Ocean Semester \u2014 The Campus",
  "The Ocean Semester \u2014 Deep Dive \u2014 The Campus",
  "The Monastery School \u2014 The Campus",
  "The Monastery School \u2014 Deep Dive \u2014 The Campus",
  "The City as School \u2014 The Campus",
  "The City as School \u2014 Deep Dive \u2014 The Campus",
  "The Desert Academy \u2014 The Campus",
  "The Desert Academy \u2014 Deep Dive \u2014 The Campus",
  "The Arctic Field School \u2014 The Campus",
  "The Arctic Field School \u2014 Deep Dive \u2014 The Campus"
 ],
 "The Curriculum": [
  "The Healer's College \u2014 The Curriculum",
  "The Healer's College \u2014 Deep Dive \u2014 The Curriculum",
  "The Builder's Academy \u2014 The Curriculum",
  "The Builder's Academy \u2014 Deep Dive \u2014 The Curriculum",
  "The Sailor's School \u2014 The Curriculum",
  "The Sailor's School \u2014 Deep Dive \u2014 The Curriculum",
  "The Storykeeper's School \u2014 The Curriculum",
  "The Storykeeper's School \u2014 Deep Dive \u2014 The Curriculum"
 ],
 "The Method": [
  "The Apprenticeship Guild \u2014 The Method",
  "The Apprenticeship Guild \u2014 Deep Dive \u2014 The Method",
  "The Socratic Lyceum \u2014 The Method",
  "The Socratic Lyceum \u2014 Deep Dive \u2014 The Method",
  "The Maker Institute \u2014 The Method",
  "The Maker Institute \u2014 Deep Dive \u2014 The Method",
  "The Digital Commons School \u2014 The Method",
  "The Digital Commons School \u2014 Deep Dive \u2014 The Method",
  "The Farm School \u2014 The Method",
  "The Farm School \u2014 Deep Dive \u2014 The Method",
  "The School-Founder's Method \u2014 The Method",
  "The School-Founder's Method \u2014 Deep Dive \u2014 The Method"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Education Study — "+safe+"\n"
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
    name:topic+' — education system record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A education system record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-future-education-system-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-future-education-system',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
