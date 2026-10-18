(function(){'use strict';
/* JAH The Norse Mythology Signature Database generator — jahdb-norse-mythology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NRMY-S-";
var FIELDS=["The Aesir & Vanir", "Heroes & Sagas", "Cosmos & Ragnarok"];
var TOPICS={
 "The Aesir & Vanir": [
  "Odin — The All-Father (Signature Edition) \u2014 The Aesir & Vanir",
  "The Signature Method for Thor — Wielder of Mjollnir \u2014 The Aesir & Vanir",
  "Loki — The Trickster (Signature Edition) \u2014 The Aesir & Vanir",
  "The Signature Method for Freyja — Goddess of Love and War \u2014 The Aesir & Vanir",
  "Baldr — The Shining God (Signature Edition) \u2014 The Aesir & Vanir",
  "The Signature Method for Tyr — The One-Handed God \u2014 The Aesir & Vanir",
  "Heimdall — The Watchman (Signature Edition) \u2014 The Aesir & Vanir",
  "The Signature Method for Frigg — Queen of the Aesir \u2014 The Aesir & Vanir",
  "Freyr — God of Plenty (Signature Edition) \u2014 The Aesir & Vanir",
  "The Signature Method for The Norns — Weavers of Fate \u2014 The Aesir & Vanir",
  "The Signature Method for Gungnir — Odin's Spear \u2014 The Aesir & Vanir"
 ],
 "Heroes & Sagas": [
  "Sigurd — Slayer of Fafnir (Signature Edition) \u2014 Heroes & Sagas",
  "The Signature Method for Brynhild — The Valkyrie \u2014 Heroes & Sagas",
  "Ragnar Lodbrok — The Saga King (Signature Edition) \u2014 Heroes & Sagas",
  "The Signature Method for Egil Skallagrimsson — The Poet Warrior \u2014 Heroes & Sagas",
  "Grettir — The Strong Outlaw (Signature Edition) \u2014 Heroes & Sagas",
  "The Signature Method for The Volsungs — The Cursed Line \u2014 Heroes & Sagas",
  "Beowulf — The Geatish Hero (Signature Edition) \u2014 Heroes & Sagas",
  "The Signature Method for Sleipnir — The Eight-Legged Horse \u2014 Heroes & Sagas",
  "The Signature Method for Skidbladnir — The Best of Ships \u2014 Heroes & Sagas"
 ],
 "Cosmos & Ragnarok": [
  "The Signature Method for Yggdrasil — The World Tree \u2014 Cosmos & Ragnarok",
  "The Nine Worlds (Signature Edition) \u2014 Cosmos & Ragnarok",
  "The Signature Method for Ragnarok — The Doom of the Gods \u2014 Cosmos & Ragnarok",
  "Fenrir — The Bound Wolf (Signature Edition) \u2014 Cosmos & Ragnarok",
  "The Signature Method for Jormungandr — The World Serpent \u2014 Cosmos & Ragnarok",
  "Valhalla — Hall of the Slain (Signature Edition) \u2014 Cosmos & Ragnarok",
  "The Signature Method for The Valkyries — Choosers of the Slain \u2014 Cosmos & Ragnarok",
  "Hel — Ruler of the Dead (Signature Edition) \u2014 Cosmos & Ragnarok",
  "The Mead of Poetry (Signature Edition) \u2014 Cosmos & Ragnarok",
  "Mimir — The Rememberer (Signature Edition) \u2014 Cosmos & Ragnarok",
  "The Signature Method for The Dwarfs — Smiths of the Deep \u2014 Cosmos & Ragnarok",
  "Bifrost — The Rainbow Bridge (Signature Edition) \u2014 Cosmos & Ragnarok",
  "The Death of Baldr — The Beginning of the End (Signature Edition) \u2014 Cosmos & Ragnarok",
  "The Signature Method for The Volva — Prophetess of the Doom \u2014 Cosmos & Ragnarok"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Norse Mythology Signature — "+safe+"\n"
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
var gen={version:'jahdb-norse-mythology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('norse-mythology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
