(function(){'use strict';
/* JAH The Biodiversity Recovery Database generator — jahdb-db-biodiversity-recovery-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBRD-";
var FIELDS=["Species Returns","Ecosystem Returns","The Methods"];
var TOPICS={
 "Species Returns": [
  "The Wolf's Return \u2014 Species Returns",
  "The Wolf's Return \u2014 Deep Dive \u2014 Species Returns",
  "The Whale's Recovery \u2014 Species Returns",
  "The Whale's Recovery \u2014 Deep Dive \u2014 Species Returns",
  "The Condor's Second Flight \u2014 Species Returns",
  "The Condor's Second Flight \u2014 Deep Dive \u2014 Species Returns",
  "The Beaver's Engineering \u2014 Species Returns",
  "The Beaver's Engineering \u2014 Deep Dive \u2014 Species Returns",
  "The Eagle's Return \u2014 Species Returns",
  "The Eagle's Return \u2014 Deep Dive \u2014 Species Returns",
  "The Insect Recovery \u2014 Species Returns",
  "The Insect Recovery \u2014 Deep Dive \u2014 Species Returns"
 ],
 "Ecosystem Returns": [
  "The Forest's Return \u2014 Ecosystem Returns",
  "The Forest's Return \u2014 Deep Dive \u2014 Ecosystem Returns",
  "The Wetland's Comeback \u2014 Ecosystem Returns",
  "The Wetland's Comeback \u2014 Deep Dive \u2014 Ecosystem Returns",
  "The River's Revival \u2014 Ecosystem Returns",
  "The River's Revival \u2014 Deep Dive \u2014 Ecosystem Returns",
  "The Reef's Resilience \u2014 Ecosystem Returns",
  "The Reef's Resilience \u2014 Deep Dive \u2014 Ecosystem Returns",
  "The Prairie's Return \u2014 Ecosystem Returns",
  "The Prairie's Return \u2014 Deep Dive \u2014 Ecosystem Returns"
 ],
 "The Methods": [
  "The Corridor Method \u2014 The Methods",
  "The Corridor Method \u2014 Deep Dive \u2014 The Methods",
  "The Reintroduction Method \u2014 The Methods",
  "The Reintroduction Method \u2014 Deep Dive \u2014 The Methods",
  "The Seed Bank Method \u2014 The Methods",
  "The Seed Bank Method \u2014 Deep Dive \u2014 The Methods",
  "The Guardian Method \u2014 The Methods",
  "The Guardian Method \u2014 Deep Dive \u2014 The Methods",
  "The Law Method \u2014 The Methods",
  "The Law Method \u2014 Deep Dive \u2014 The Methods",
  "The Recovery Chronicler's Method \u2014 The Methods",
  "The Recovery Chronicler's Method \u2014 Deep Dive \u2014 The Methods"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Biodiversity Recovery Study — "+safe+"\n"
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
    name:topic+' — biodiversity recovery record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A biodiversity recovery record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-biodiversity-recovery-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-biodiversity-recovery',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
