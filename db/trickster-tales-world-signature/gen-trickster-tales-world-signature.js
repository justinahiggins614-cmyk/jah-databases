(function(){'use strict';
/* JAH The World Trickster Tales Signature Database generator — jahdb-trickster-tales-world-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TRKT-S-";
var FIELDS=["Tricksters of the Americas", "Tricksters of Africa & Europe", "Tricksters of Asia & Oceania"];
var TOPICS={
 "Tricksters of the Americas": [
  "The Signature Method for Coyote — The Hungry One \u2014 Tricksters of the Americas",
  "Brer Rabbit — The Weak Victor (Signature Edition) \u2014 Tricksters of the Americas",
  "The Signature Method for Raven — The Northwest Trickster \u2014 Tricksters of the Americas",
  "Iktomi — The Lakota Spider (Signature Edition) \u2014 Tricksters of the Americas",
  "The Signature Method for Nanabozho — The Ojibwe Trickster \u2014 Tricksters of the Americas",
  "Saci — The Brazilian Trickster (Signature Edition) \u2014 Tricksters of the Americas",
  "Wakdjunkaga — The Winnebago Trickster (Signature Edition) \u2014 Tricksters of the Americas",
  "The Signature Method for Azeban — The Raccoon Trickster \u2014 Tricksters of the Americas",
  "Saynday — The Kiowa Trickster (Signature Edition) \u2014 Tricksters of the Americas",
  "The Signature Method for Kokopelli — The Flute Player \u2014 Tricksters of the Americas"
 ],
 "Tricksters of Africa & Europe": [
  "Anansi — The Spider (Signature Edition) \u2014 Tricksters of Africa & Europe",
  "The Monkey's Paw — The Cautionary Trick (Signature Edition) \u2014 Tricksters of Africa & Europe",
  "The Signature Method for Till Eulenspiegel — The Prankster \u2014 Tricksters of Africa & Europe",
  "Reynard — The Fox (Signature Edition) \u2014 Tricksters of Africa & Europe",
  "The Signature Method for Loki — The Norse Trickster \u2014 Tricksters of Africa & Europe",
  "Hermes — The Divine Trickster (Signature Edition) \u2014 Tricksters of Africa & Europe",
  "The Signature Method for Prometheus — The Fire Trickster \u2014 Tricksters of Africa & Europe",
  "Eshu — The Yoruba Trickster (Signature Edition) \u2014 Tricksters of Africa & Europe",
  "The Signature Method for The Jackal — African Trickster \u2014 Tricksters of Africa & Europe",
  "The Signature Method for Pedro de Urdemalas — The Spanish Trickster \u2014 Tricksters of Africa & Europe",
  "Juha — The Arab Wise Fool (Signature Edition) \u2014 Tricksters of Africa & Europe",
  "The Signature Method for The Schildbürger — Fools of Schilda \u2014 Tricksters of Africa & Europe",
  "The Wise Men of Gotham (Signature Edition) \u2014 Tricksters of Africa & Europe",
  "The Signature Method for The Brave Little Tailor \u2014 Tricksters of Africa & Europe"
 ],
 "Tricksters of Asia & Oceania": [
  "Maui — The Polynesian Trickster (Signature Edition) \u2014 Tricksters of Asia & Oceania",
  "The Signature Method for Sun Wukong — The Monkey King \u2014 Tricksters of Asia & Oceania",
  "The Trickster's Punishment (Signature Edition) \u2014 Tricksters of Asia & Oceania",
  "The Signature Method for Trickster Women — The Clever Ones \u2014 Tricksters of Asia & Oceania",
  "The Theft of Fire — Worldwide (Signature Edition) \u2014 Tricksters of Asia & Oceania",
  "The Signature Method for Why the Trickster Matters \u2014 Tricksters of Asia & Oceania",
  "Nasreddin Hodja — The Wise Fool (Signature Edition) \u2014 Tricksters of Asia & Oceania",
  "The Signature Method for Birbal — The Clever Minister \u2014 Tricksters of Asia & Oceania",
  "Tenali Raman — The Telugu Wit (Signature Edition) \u2014 Tricksters of Asia & Oceania",
  "The Signature Method for Sang Kancil — The Mouse Deer \u2014 Tricksters of Asia & Oceania"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# World Trickster Tales Signature — "+safe+"\n"
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
    name:topic+' — folklore record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A folklore record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-trickster-tales-world-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('trickster-tales-world-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
