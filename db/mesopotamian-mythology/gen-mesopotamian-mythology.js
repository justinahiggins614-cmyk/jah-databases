(function(){'use strict';
/* JAH The Mesopotamian Mythology Database generator — jahdb-mesopotamian-mythology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEMY-";
var FIELDS=["Gods of Mesopotamia", "Epics & Kings", "Creation & Cosmos"];
var TOPICS={
 "Gods of Mesopotamia": [
  "Anu — God of the Sky \u2014 Gods of Mesopotamia",
  "Enlil — Lord of the Air \u2014 Gods of Mesopotamia",
  "Enki — God of Wisdom and Water \u2014 Gods of Mesopotamia",
  "Inanna — Queen of Heaven \u2014 Gods of Mesopotamia",
  "Marduk — King of the Gods \u2014 Gods of Mesopotamia",
  "Tiamat — The Chaos Dragon \u2014 Gods of Mesopotamia",
  "Nergal — God of Plague and the Underworld \u2014 Gods of Mesopotamia",
  "Ereshkigal — Queen of the Dead \u2014 Gods of Mesopotamia",
  "Utu-Shamash — God of the Sun and Justice \u2014 Gods of Mesopotamia",
  "Nanna-Sin — God of the Moon \u2014 Gods of Mesopotamia",
  "Dumuzi — The Dying Shepherd \u2014 Gods of Mesopotamia",
  "Ninhursag — Mother of the Gods \u2014 Gods of Mesopotamia",
  "Ninurta — The Warrior God \u2014 Gods of Mesopotamia"
 ],
 "Epics & Kings": [
  "Gilgamesh — King of Uruk \u2014 Epics & Kings",
  "Enkidu — The Wild Man \u2014 Epics & Kings",
  "The Epic of Gilgamesh \u2014 Epics & Kings",
  "Utnapishtim — The Flood Survivor \u2014 Epics & Kings",
  "The Descent of Inanna \u2014 Epics & Kings",
  "Sargon — The First Emperor \u2014 Epics & Kings",
  "Hammurabi — The Lawgiver \u2014 Epics & Kings",
  "The Flood — Atrahasis \u2014 Epics & Kings",
  "Ashurbanipal — The Scholar King \u2014 Epics & Kings",
  "Adapa — The Wise Mortal \u2014 Epics & Kings",
  "Etana — The Shepherd King \u2014 Epics & Kings",
  "Lugalbanda — Hero of the Mountain Cave \u2014 Epics & Kings",
  "The Lament for Ur \u2014 Epics & Kings",
  "Gudea — The Builder King \u2014 Epics & Kings"
 ],
 "Creation & Cosmos": [
  "The Enuma Elish \u2014 Creation & Cosmos",
  "The Eridu Genesis \u2014 Creation & Cosmos",
  "The Huluppu Tree \u2014 Creation & Cosmos",
  "The Seven Sages — Apkallu \u2014 Creation & Cosmos",
  "The Underworld — Kur \u2014 Creation & Cosmos",
  "The Ziggurat — Stairway to Heaven \u2014 Creation & Cosmos",
  "The Anzu Bird \u2014 Creation & Cosmos"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mesopotamian Mythology — "+safe+"\n"
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
var gen={version:'jahdb-mesopotamian-mythology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mesopotamian-mythology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
