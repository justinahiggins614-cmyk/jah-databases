(function(){'use strict';
/* JAH The Mesopotamian Mythology Signature Database generator — jahdb-mesopotamian-mythology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEMY-S-";
var FIELDS=["Gods of Mesopotamia", "Epics & Kings", "Creation & Cosmos"];
var TOPICS={
 "Gods of Mesopotamia": [
  "Anu — God of the Sky (Signature Edition) \u2014 Gods of Mesopotamia",
  "The Signature Method for Enlil — Lord of the Air \u2014 Gods of Mesopotamia",
  "Enki — God of Wisdom and Water (Signature Edition) \u2014 Gods of Mesopotamia",
  "The Signature Method for Inanna — Queen of Heaven \u2014 Gods of Mesopotamia",
  "Marduk — King of the Gods (Signature Edition) \u2014 Gods of Mesopotamia",
  "The Signature Method for Tiamat — The Chaos Dragon \u2014 Gods of Mesopotamia",
  "Nergal — God of Plague and the Underworld (Signature Edition) \u2014 Gods of Mesopotamia",
  "The Signature Method for Ereshkigal — Queen of the Dead \u2014 Gods of Mesopotamia",
  "Utu-Shamash — God of the Sun and Justice (Signature Edition) \u2014 Gods of Mesopotamia",
  "The Signature Method for Nanna-Sin — God of the Moon \u2014 Gods of Mesopotamia",
  "The Signature Method for Dumuzi — The Dying Shepherd \u2014 Gods of Mesopotamia",
  "Ninhursag — Mother of the Gods (Signature Edition) \u2014 Gods of Mesopotamia",
  "Ninurta — The Warrior God (Signature Edition) \u2014 Gods of Mesopotamia"
 ],
 "Epics & Kings": [
  "Gilgamesh — King of Uruk (Signature Edition) \u2014 Epics & Kings",
  "The Signature Method for Enkidu — The Wild Man \u2014 Epics & Kings",
  "The Epic of Gilgamesh (Signature Edition) \u2014 Epics & Kings",
  "The Signature Method for Utnapishtim — The Flood Survivor \u2014 Epics & Kings",
  "The Descent of Inanna (Signature Edition) \u2014 Epics & Kings",
  "The Signature Method for Sargon — The First Emperor \u2014 Epics & Kings",
  "Hammurabi — The Lawgiver (Signature Edition) \u2014 Epics & Kings",
  "The Signature Method for The Flood — Atrahasis \u2014 Epics & Kings",
  "Ashurbanipal — The Scholar King (Signature Edition) \u2014 Epics & Kings",
  "The Signature Method for Adapa — The Wise Mortal \u2014 Epics & Kings",
  "Etana — The Shepherd King (Signature Edition) \u2014 Epics & Kings",
  "The Signature Method for Lugalbanda — Hero of the Mountain Cave \u2014 Epics & Kings",
  "The Lament for Ur (Signature Edition) \u2014 Epics & Kings",
  "The Signature Method for Gudea — The Builder King \u2014 Epics & Kings"
 ],
 "Creation & Cosmos": [
  "The Signature Method for The Enuma Elish \u2014 Creation & Cosmos",
  "The Eridu Genesis (Signature Edition) \u2014 Creation & Cosmos",
  "The Signature Method for The Huluppu Tree \u2014 Creation & Cosmos",
  "The Seven Sages — Apkallu (Signature Edition) \u2014 Creation & Cosmos",
  "The Signature Method for The Underworld — Kur \u2014 Creation & Cosmos",
  "The Ziggurat — Stairway to Heaven (Signature Edition) \u2014 Creation & Cosmos",
  "The Signature Method for The Anzu Bird \u2014 Creation & Cosmos"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mesopotamian Mythology Signature — "+safe+"\n"
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
var gen={version:'jahdb-mesopotamian-mythology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mesopotamian-mythology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
