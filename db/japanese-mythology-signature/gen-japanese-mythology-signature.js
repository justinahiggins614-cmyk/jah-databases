(function(){'use strict';
/* JAH The Japanese Mythology Signature Database generator — jahdb-japanese-mythology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-JPMY-S-";
var FIELDS=["Kami of Heaven & Earth", "Heroes & Legends", "Yokai & the Spirit World"];
var TOPICS={
 "Kami of Heaven & Earth": [
  "Amaterasu — The Sun Goddess (Signature Edition) \u2014 Kami of Heaven & Earth",
  "The Signature Method for Susanoo — The Storm God \u2014 Kami of Heaven & Earth",
  "Tsukuyomi — The Moon God (Signature Edition) \u2014 Kami of Heaven & Earth",
  "The Signature Method for Izanagi and Izanami — The First Pair \u2014 Kami of Heaven & Earth",
  "The Rock-Cave — Amaterasu's Withdrawal (Signature Edition) \u2014 Kami of Heaven & Earth",
  "The Signature Method for Yamata no Orochi — The Eight-Headed Serpent \u2014 Kami of Heaven & Earth",
  "Inari — The Rice God (Signature Edition) \u2014 Kami of Heaven & Earth",
  "The Signature Method for Hachiman — God of War \u2014 Kami of Heaven & Earth",
  "Raijin and Fujin — Thunder and Wind (Signature Edition) \u2014 Kami of Heaven & Earth",
  "The Signature Method for The Kojiki — Records of Ancient Matters \u2014 Kami of Heaven & Earth",
  "Jomon and the First Myths (Signature Edition) \u2014 Kami of Heaven & Earth",
  "Ame no Uzume — The Dancing Goddess (Signature Edition) \u2014 Kami of Heaven & Earth",
  "The Signature Method for The Nihon Shoki — Chronicles of Japan \u2014 Kami of Heaven & Earth"
 ],
 "Heroes & Legends": [
  "The Signature Method for Momotaro — The Peach Boy \u2014 Heroes & Legends",
  "Urashima Taro — The Fisherman's Time (Signature Edition) \u2014 Heroes & Legends",
  "The Signature Method for Kintaro — The Golden Boy \u2014 Heroes & Legends",
  "The Tale of the Bamboo Cutter (Signature Edition) \u2014 Heroes & Legends",
  "The Signature Method for Yamato Takeru — The Brave of Yamato \u2014 Heroes & Legends",
  "The Forty-Seven Ronin (Signature Edition) \u2014 Heroes & Legends",
  "The Signature Method for Benkei — The Warrior Monk \u2014 Heroes & Legends",
  "Yoshitsune — The Tragic Hero (Signature Edition) \u2014 Heroes & Legends",
  "The Signature Method for The Heike — Tale of the Fallen \u2014 Heroes & Legends",
  "The Yatagarasu — The Sun Crow (Signature Edition) \u2014 Heroes & Legends"
 ],
 "Yokai & the Spirit World": [
  "Kitsune — The Fox Spirits (Signature Edition) \u2014 Yokai & the Spirit World",
  "The Signature Method for Tanuki — The Badger Tricksters \u2014 Yokai & the Spirit World",
  "Tengu — The Mountain Goblins (Signature Edition) \u2014 Yokai & the Spirit World",
  "The Signature Method for Oni — The Demons \u2014 Yokai & the Spirit World",
  "Yurei — The Ghosts (Signature Edition) \u2014 Yokai & the Spirit World",
  "The Signature Method for Kappa — The River Imps \u2014 Yokai & the Spirit World",
  "Yuki-onna — The Snow Woman (Signature Edition) \u2014 Yokai & the Spirit World",
  "The Signature Method for The Hyakki Yagyo — Night Parade \u2014 Yokai & the Spirit World",
  "Jorogumo — The Binding Bride (Signature Edition) \u2014 Yokai & the Spirit World",
  "The Signature Method for The Dragon Kings — Rulers of the Sea \u2014 Yokai & the Spirit World",
  "The Signature Method for The Kodama — Tree Spirits \u2014 Yokai & the Spirit World"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Japanese Mythology Signature — "+safe+"\n"
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
var gen={version:'jahdb-japanese-mythology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('japanese-mythology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
