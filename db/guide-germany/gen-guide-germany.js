(function(){'use strict';
/* JAH Germany Travel Guide Database generator — "jahdb-guide-germany-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GGER-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Germany: Orientation and First Impressions", "Best Time to Visit Germany", "Getting to Germany", "Getting Around Germany", "Where to Stay in Germany", "Money, Costs, and Budgeting for Germany", "Language Essentials for Germany", "Safety and Health in Germany", "Customs and Etiquette in Germany", "What to Pack for Germany", "Your First Day in Germany: A Walking Route", "Tourist Information and Emergency Numbers for Germany"], "Compounded": ["Germany: Neuschwanstein", "Germany: The Rhine Gorge", "Germany: Cologne Cathedral", "Germany: The Brandenburg Gate", "Germany: Pergamon Museum", "Germany: Deutsches Museum", "Germany Neighborhood Deep-Dive: Berlin", "Germany Neighborhood Deep-Dive: Munich", "Germany Neighborhood Deep-Dive: The Rhine Valley", "Eating in Germany: Dishes You Must Try", "Markets and Shopping in Germany", "Parks, Water, and Green Escapes in Germany"], "Advanced": ["Hidden Gems of Germany", "Germany in Three Days: The Essential Itinerary", "Germany in Five Days: The Deep Itinerary", "Day Trip from Germany: Potsdam from Berlin", "Day Trip from Germany: Neuschwanstein from Munich", "Photography and Viewpoints in Germany", "Nightlife and Evenings in Germany", "Festivals and Events Calendar for Germany", "Germany with Kids", "Living Like a Local: The Extended Stay in Germany"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-germany demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-germany-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-germany",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
