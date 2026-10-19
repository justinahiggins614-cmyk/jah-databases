(function(){'use strict';
/* JAH Argentina Travel Guide Database generator — "jahdb-guide-argentina-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GARG-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Argentina: Orientation and First Impressions", "Best Time to Visit Argentina", "Getting to Argentina", "Getting Around Argentina", "Where to Stay in Argentina", "Money, Costs, and Budgeting for Argentina", "Language Essentials for Argentina", "Safety and Health in Argentina", "Customs and Etiquette in Argentina", "What to Pack for Argentina", "Your First Day in Argentina: A Walking Route", "Tourist Information and Emergency Numbers for Argentina"], "Compounded": ["Argentina: Buenos Aires", "Argentina: Patagonia", "Argentina: Iguaçu Falls", "Argentina: Perito Moreno", "Argentina: The MALBA", "Argentina: The Evita Museum", "Argentina Neighborhood Deep-Dive: Buenos Aires (Palermo)", "Argentina Neighborhood Deep-Dive: El Chaltén", "Argentina Neighborhood Deep-Dive: Mendoza", "Eating in Argentina: Dishes You Must Try", "Markets and Shopping in Argentina", "Parks, Water, and Green Escapes in Argentina"], "Advanced": ["Hidden Gems of Argentina", "Argentina in Three Days: The Essential Itinerary", "Argentina in Five Days: The Deep Itinerary", "Day Trip from Argentina: Tigre from Buenos Aires", "Day Trip from Argentina: La Plata from Buenos Aires", "Photography and Viewpoints in Argentina", "Nightlife and Evenings in Argentina", "Festivals and Events Calendar for Argentina", "Argentina with Kids", "Living Like a Local: The Extended Stay in Argentina"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-argentina demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — travel guide record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A travel guide record study. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest-sample",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-guide-argentina-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-argentina",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
