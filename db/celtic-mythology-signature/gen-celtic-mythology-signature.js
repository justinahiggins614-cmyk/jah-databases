(function(){'use strict';
/* JAH The Celtic Mythology Signature Database generator — jahdb-celtic-mythology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CEMY-S-";
var FIELDS=["Gods of the Celts", "Heroes & Cycles", "The Otherworld"];
var TOPICS={
 "Gods of the Celts": [
  "The Dagda — The Good God (Signature Edition) \u2014 Gods of the Celts",
  "The Signature Method for Lugh — The Many-Skilled \u2014 Gods of the Celts",
  "The Morrigan — Phantom Queen (Signature Edition) \u2014 Gods of the Celts",
  "The Signature Method for Brigid — Goddess of the Hearth \u2014 Gods of the Celts",
  "Manannan mac Lir — Lord of the Sea (Signature Edition) \u2014 Gods of the Celts",
  "The Signature Method for The Tuatha De Danaan — People of the Goddess Danu \u2014 Gods of the Celts",
  "The Fomorians — Powers of Chaos (Signature Edition) \u2014 Gods of the Celts",
  "Cernunnos — The Horned God (Signature Edition) \u2014 Gods of the Celts",
  "The Signature Method for Arawn — Lord of Annwn \u2014 Gods of the Celts",
  "Rhiannon — The Horse Goddess (Signature Edition) \u2014 Gods of the Celts",
  "The Signature Method for Goibniu — The Divine Smith \u2014 Gods of the Celts",
  "Danu — Mother of the Gods (Signature Edition) \u2014 Gods of the Celts"
 ],
 "Heroes & Cycles": [
  "The Signature Method for Cu Chulainn — The Hound of Ulster \u2014 Heroes & Cycles",
  "The Tain Bo Cuailnge — Cattle Raid of Cooley (Signature Edition) \u2014 Heroes & Cycles",
  "The Signature Method for Finn mac Cumhaill — Leader of the Fianna \u2014 Heroes & Cycles",
  "Oisin — The Poet in the Otherworld (Signature Edition) \u2014 Heroes & Cycles",
  "The Signature Method for Deirdre — The Sorrow of Ulster \u2014 Heroes & Cycles",
  "The Salmon of Knowledge (Signature Edition) \u2014 Heroes & Cycles",
  "The Signature Method for The Mabinogion — Tales of Wales \u2014 Heroes & Cycles",
  "Taliesin — The Radiant Bard (Signature Edition) \u2014 Heroes & Cycles",
  "The Signature Method for Conchobar — King of Ulster \u2014 Heroes & Cycles",
  "Medb — Queen of Connacht (Signature Edition) \u2014 Heroes & Cycles",
  "The Signature Method for Culhwch and Olwen \u2014 Heroes & Cycles",
  "The Voyage of Mael Duin (Signature Edition) \u2014 Heroes & Cycles"
 ],
 "The Otherworld": [
  "The Signature Method for Tir na nOg — Land of Youth \u2014 The Otherworld",
  "The Sidhe — Mounds of the Fair Folk (Signature Edition) \u2014 The Otherworld",
  "The Signature Method for Samhain — Night of the Thin Veil \u2014 The Otherworld",
  "Imbolc — Brigid's Spring (Signature Edition) \u2014 The Otherworld",
  "The Signature Method for Beltane — Fires of Summer \u2014 The Otherworld",
  "Lughnasadh — The Harvest Games (Signature Edition) \u2014 The Otherworld",
  "The Signature Method for The Cauldron of Annwn \u2014 The Otherworld",
  "The Signature Method for Avalon — The Apple Isle \u2014 The Otherworld",
  "The Banshee — Woman of the Mounds (Signature Edition) \u2014 The Otherworld",
  "The Signature Method for The Selkie — Seal Folk \u2014 The Otherworld"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Celtic Mythology Signature — "+safe+"\n"
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
var gen={version:'jahdb-celtic-mythology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('celtic-mythology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
