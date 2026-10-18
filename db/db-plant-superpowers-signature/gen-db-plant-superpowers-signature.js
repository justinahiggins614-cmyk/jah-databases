(function(){'use strict';
/* JAH The Plant Superpowers Database Signature Database generator — jahdb-db-plant-superpowers-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PLWS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Plants Are Not Passive",
  "The Venus Flytrap",
  "The Corpse Flower",
  "Mimosa: The Shy Plant",
  "The Strangler Fig",
  "Resurrection Plants",
  "The Sensitive Fern",
  "Carnivorous Plant Traps",
  "The Talking Trees",
  "Seed Superpowers",
  "The Plant Senses"
 ],
 "Compounded": [
  "The Pitcher Plant",
  "The Sundew",
  "The Bladderwort",
  "The Cobra Lily",
  "Plant Communication Networks",
  "The Exploding Cucumber",
  "The Sensitive Plant Lab",
  "Plant Defenses",
  "The Sensitive Tree",
  "The Walking Palm",
  "The Dragon's Blood Tree",
  "The Welwitschia"
 ],
 "Advanced": [
  "Advanced: Plant Intelligence Debate",
  "Advanced: The Green Pharmacy",
  "Advanced: Growing Carnivores",
  "Advanced: The Baobab",
  "Advanced: Your Plant Lab",
  "Advanced: The Corpse Flower Watch",
  "Advanced: Plant Hunting Ethics",
  "Advanced: The Greenhouse Carnivores",
  "Advanced: The Plant Red List",
  "Advanced: Your Botanical Garden",
  "The Plant Superpowers Encyclopedia"
 ]
};
var DEMOKIND="animals-lab-demo";
var SAMPLEDESC="Sample records are complete real plant entries with real measurement math.";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nature Lab Demo — "+safe+"\n"
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
    name:topic+' — plant superpower record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A plant superpower record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-plant-superpowers-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-plant-superpowers-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
