(function(){'use strict';
/* JAH The Roman Mythology Database generator — jahdb-roman-mythology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ROMY-";
var FIELDS=["Gods of Rome", "Heroes & Founding", "Ritual & Cosmos"];
var TOPICS={
 "Gods of Rome": [
  "Jupiter — Optimus Maximus \u2014 Gods of Rome",
  "Mars — Father of Rome \u2014 Gods of Rome",
  "Venus — Ancestress of Rome \u2014 Gods of Rome",
  "Minerva — Goddess of Wisdom \u2014 Gods of Rome",
  "Juno — Queen of Heaven \u2014 Gods of Rome",
  "Apollo — God of the Golden Age \u2014 Gods of Rome",
  "Diana — Goddess of the Hunt \u2014 Gods of Rome",
  "Mercury — Messenger and Merchant \u2014 Gods of Rome",
  "Vesta — Hearth of Rome \u2014 Gods of Rome",
  "Ceres — Goddess of Grain \u2014 Gods of Rome",
  "Neptune — God of the Sea \u2014 Gods of Rome",
  "Vulcan — God of Fire \u2014 Gods of Rome",
  "Pluto and Proserpina \u2014 Gods of Rome",
  "Cupid and Psyche \u2014 Gods of Rome",
  "The Dioscuri — Castor and Pollux \u2014 Gods of Rome"
 ],
 "Heroes & Founding": [
  "Aeneas — The Pious Founder \u2014 Heroes & Founding",
  "Romulus — First King of Rome \u2014 Heroes & Founding",
  "Remus — The Slain Twin \u2014 Heroes & Founding",
  "The Rape of the Sabine Women \u2014 Heroes & Founding",
  "Horatius at the Bridge \u2014 Heroes & Founding",
  "Cincinnatus — The Citizen Soldier \u2014 Heroes & Founding",
  "Mucius Scaevola — The Burned Hand \u2014 Heroes & Founding",
  "The Founding — April 21, 753 BCE \u2014 Heroes & Founding",
  "The Aeneid — Virgil's Epic \u2014 Heroes & Founding",
  "Ovid — The Metamorphoses \u2014 Heroes & Founding",
  "Scipio Africanus — Conqueror of Hannibal \u2014 Heroes & Founding"
 ],
 "Ritual & Cosmos": [
  "The Sibylline Books \u2014 Ritual & Cosmos",
  "The Lares and Penates \u2014 Ritual & Cosmos",
  "Augury — Reading the Birds \u2014 Ritual & Cosmos",
  "The Saturnalia \u2014 Ritual & Cosmos",
  "Janus — God of Beginnings \u2014 Ritual & Cosmos",
  "The Vestals — Keepers of the Flame \u2014 Ritual & Cosmos",
  "The Lupercalia \u2014 Ritual & Cosmos",
  "The Triumph — Rome's Victory Parade \u2014 Ritual & Cosmos"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Roman Mythology — "+safe+"\n"
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
    name:topic+' — mythology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mythology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-roman-mythology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('roman-mythology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
