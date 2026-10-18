(function(){'use strict';
/* JAH The Feudal Japan Database generator — jahdb-feudal-japan-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FEUDJ-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Feudal Japan Was",
  "The Shogun and the Emperor",
  "Daimyo and Domains",
  "Samurai: The Warrior Class",
  "Bushido: The Warrior Code",
  "Peasants, Artisans, Merchants",
  "The Heian Court (Precursor)",
  "Kamakura: First Shogunate",
  "Daily Life in Feudal Japan",
  "A Feudal Japan Timeline Overview",
  "Sources: How We Know Feudal Japan"
 ],
 "Compounded": [
  "The Gempei War",
  "The Mongol Invasions",
  "Ashikaga and Muromachi Culture",
  "The Onin War and Sengoku Chaos",
  "Oda Nobunaga",
  "Toyotomi Hideyoshi",
  "Tokugawa Ieyasu and Sekigahara",
  "The Edo Peace",
  "Samurai Armor and Weapons",
  "Castles of Japan",
  "Tea Ceremony and Zen Arts",
  "The Merchant Class and Early Capitalism"
 ],
 "Advanced": [
  "The 47 Ronin",
  "Sakoku: The Closed Country",
  "The Meiji Restoration's End of Feudalism",
  "Women in Feudal Japan",
  "Ninja: Fact and Legend",
  "Kabuki and Ukiyo-e",
  "The Sankin-Kotai System",
  "Feudal Japan's Legacy",
  "Bushido in Modern Japan",
  "Kendo and Iaido: Martial Arts Today",
  "The Ainu and Ryukyu: Japan's Margins"
 ]
};
var DEMOKIND="era math";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Feudal era calculator — "+safe+"\n"
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
    name:topic+' — feudal japan record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A feudal japan record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
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
var gen={version:'jahdb-feudal-japan-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('feudal-japan',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
