(function(){'use strict';
/* JAH The 2020s Database generator — jahdb-decades-2020s-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D2020-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 2020s at a Glance: The Decade We're Living - Foundations",
  "2020: The WHO Declares the Pandemic - Foundations",
  "2020: George Floyd and the Reckoning - Foundations",
  "2020: Biden Wins the Pandemic Election - Foundations",
  "2021: The Capitol Riot - Foundations",
  "2021: The Fall of Kabul - Foundations",
  "2022: Russia Invades Ukraine - Foundations",
  "2022: The James Webb Telescope's First Images - Foundations",
  "2022: ChatGPT Launches \u2014 AI Goes Mainstream - Foundations",
  "2022: Queen Elizabeth II Dies - Foundations"
 ],
 "Compounded": [
  "2020: The First COVID Vaccines - Compounded",
  "2021: The Ever Given Blocks Suez - Compounded",
  "2021: Perseverance Lands on Mars - Compounded",
  "2022: Artemis I Circles the Moon - Compounded",
  "2022: DART Shifts Dimorphos - Compounded",
  "2022: Fusion Ignition at NIF - Compounded",
  "2023: The Israel-Hamas War Begins - Compounded",
  "2023: The Titan Submersible - Compounded",
  "2024: Trump Wins Again - Compounded",
  "2024: The Paris Olympics - Compounded",
  "2021: The Billionaire Space Race - Compounded"
 ],
 "Advanced": [
  "2023: Threads Launches - Advanced",
  "2024: The Vision Pro - Advanced",
  "2024: The Great North American Eclipse - Advanced",
  "2025: The LA Fires - Advanced",
  "2023: The Ozempic Era - Advanced",
  "2022: Musk Buys Twitter - Advanced",
  "2023: The SVB Collapse - Advanced",
  "2024: The Bitcoin ETF - Advanced",
  "2023: India's Moon Landing \u2014 Chandrayaan-3 - Advanced",
  "2024: The First Commercial Spacewalk - Advanced",
  "2021: Beeple's $69 Million JPEG - Advanced",
  "2022: Dobbs Overturns Roe - Advanced",
  "2026: The 2020s at Halftime - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 2020S — "+safe+"\n"
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
    name:topic+' — 2020s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 2020s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-2020s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-2020s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-2020s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
