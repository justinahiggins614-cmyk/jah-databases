(function(){'use strict';
/* JAH The Norse Mythology Database generator — jahdb-norse-mythology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NRMY-";
var FIELDS=["The Aesir & Vanir", "Heroes & Sagas", "Cosmos & Ragnarok"];
var TOPICS={
 "The Aesir & Vanir": [
  "Odin — The All-Father \u2014 The Aesir & Vanir",
  "Thor — Wielder of Mjollnir \u2014 The Aesir & Vanir",
  "Loki — The Trickster \u2014 The Aesir & Vanir",
  "Freyja — Goddess of Love and War \u2014 The Aesir & Vanir",
  "Baldr — The Shining God \u2014 The Aesir & Vanir",
  "Tyr — The One-Handed God \u2014 The Aesir & Vanir",
  "Heimdall — The Watchman \u2014 The Aesir & Vanir",
  "Frigg — Queen of the Aesir \u2014 The Aesir & Vanir",
  "Freyr — God of Plenty \u2014 The Aesir & Vanir",
  "The Norns — Weavers of Fate \u2014 The Aesir & Vanir",
  "Gungnir — Odin's Spear \u2014 The Aesir & Vanir"
 ],
 "Heroes & Sagas": [
  "Sigurd — Slayer of Fafnir \u2014 Heroes & Sagas",
  "Brynhild — The Valkyrie \u2014 Heroes & Sagas",
  "Ragnar Lodbrok — The Saga King \u2014 Heroes & Sagas",
  "Egil Skallagrimsson — The Poet Warrior \u2014 Heroes & Sagas",
  "Grettir — The Strong Outlaw \u2014 Heroes & Sagas",
  "The Volsungs — The Cursed Line \u2014 Heroes & Sagas",
  "Beowulf — The Geatish Hero \u2014 Heroes & Sagas",
  "Sleipnir — The Eight-Legged Horse \u2014 Heroes & Sagas",
  "Skidbladnir — The Best of Ships \u2014 Heroes & Sagas"
 ],
 "Cosmos & Ragnarok": [
  "Yggdrasil — The World Tree \u2014 Cosmos & Ragnarok",
  "The Nine Worlds \u2014 Cosmos & Ragnarok",
  "Ragnarok — The Doom of the Gods \u2014 Cosmos & Ragnarok",
  "Fenrir — The Bound Wolf \u2014 Cosmos & Ragnarok",
  "Jormungandr — The World Serpent \u2014 Cosmos & Ragnarok",
  "Valhalla — Hall of the Slain \u2014 Cosmos & Ragnarok",
  "The Valkyries — Choosers of the Slain \u2014 Cosmos & Ragnarok",
  "Hel — Ruler of the Dead \u2014 Cosmos & Ragnarok",
  "The Mead of Poetry \u2014 Cosmos & Ragnarok",
  "Mimir — The Rememberer \u2014 Cosmos & Ragnarok",
  "The Dwarfs — Smiths of the Deep \u2014 Cosmos & Ragnarok",
  "Bifrost — The Rainbow Bridge \u2014 Cosmos & Ragnarok",
  "The Death of Baldr — The Beginning of the End \u2014 Cosmos & Ragnarok",
  "The Volva — Prophetess of the Doom \u2014 Cosmos & Ragnarok"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Norse Mythology — "+safe+"\n"
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
var gen={version:'jahdb-norse-mythology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('norse-mythology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
