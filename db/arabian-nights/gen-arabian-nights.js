(function(){'use strict';
/* JAH The Arabian Nights Database generator — jahdb-arabian-nights-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ARNI-";
var FIELDS=["Tales of Scheherazade", "Voyages & Adventures", "Magic & Marvels"];
var TOPICS={
 "Tales of Scheherazade": [
  "Scheherazade — The Storyteller \u2014 Tales of Scheherazade",
  "King Shahryar — The Converted King \u2014 Tales of Scheherazade",
  "Dunyazad — The Sister \u2014 Tales of Scheherazade",
  "The Frame Tale — The 1001 Nights \u2014 Tales of Scheherazade",
  "The Merchant and the Genie \u2014 Tales of Scheherazade",
  "The Fisherman and the Genie \u2014 Tales of Scheherazade",
  "The Porter and the Three Ladies \u2014 Tales of Scheherazade",
  "The Three Apples \u2014 Tales of Scheherazade",
  "The Hunchback's Tale \u2014 Tales of Scheherazade",
  "Nur al-Din and Shams al-Din \u2014 Tales of Scheherazade",
  "The Two Viziers — The Envier \u2014 Tales of Scheherazade",
  "The Tale of the Bull and the Ass \u2014 Tales of Scheherazade",
  "The Craft and Malice of Women \u2014 Tales of Scheherazade",
  "The History of the Kings — The Frame's End \u2014 Tales of Scheherazade",
  "Galland — The Translator \u2014 Tales of Scheherazade",
  "Why the Nights Matter \u2014 Tales of Scheherazade",
  "The Barber's Six Brothers \u2014 Tales of Scheherazade"
 ],
 "Voyages & Adventures": [
  "Sinbad the Sailor — The Voyages \u2014 Voyages & Adventures",
  "Sinbad the Porter — The Listener \u2014 Voyages & Adventures",
  "Ali Baba and the Forty Thieves \u2014 Voyages & Adventures",
  "The City of Brass \u2014 Voyages & Adventures",
  "Judar and His Brothers \u2014 Voyages & Adventures",
  "Ma'ruf the Cobbler \u2014 Voyages & Adventures",
  "The Nights' Afterlife — Influence \u2014 Voyages & Adventures",
  "Hasan of Basra — The Voyage \u2014 Voyages & Adventures"
 ],
 "Magic & Marvels": [
  "Aladdin and the Wonderful Lamp \u2014 Magic & Marvels",
  "The Ebony Horse \u2014 Magic & Marvels",
  "The Ensorcelled Prince \u2014 Magic & Marvels",
  "The Sleeper Awakened \u2014 Magic & Marvels",
  "The Mock Caliph \u2014 Magic & Marvels",
  "The Magic Horse — The Prince's Flight \u2014 Magic & Marvels",
  "The Queen of the Serpents \u2014 Magic & Marvels",
  "Prince Ahmad and Peri Banu \u2014 Magic & Marvels",
  "The Talking Bird \u2014 Magic & Marvels"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Arabian Nights — "+safe+"\n"
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
    name:topic+' — tale record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tale record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-arabian-nights-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('arabian-nights',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
