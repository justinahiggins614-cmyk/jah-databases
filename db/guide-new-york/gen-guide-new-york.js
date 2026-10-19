(function(){'use strict';
/* JAH New York City Travel Guide Database generator — "jahdb-guide-new-york-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GNYC-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["New York City: Orientation and First Impressions", "Best Time to Visit New York City", "Getting to New York City", "Getting Around New York City", "Where to Stay in New York City", "Money, Costs, and Budgeting for New York City", "Language Essentials for New York City", "Safety and Health in New York City", "Customs and Etiquette in New York City", "What to Pack for New York City", "Your First Day in New York City: A Walking Route", "Tourist Information and Emergency Numbers for New York City"], "Compounded": ["New York City: Statue of Liberty", "New York City: Empire State Building", "New York City: Central Park", "New York City: Times Square", "New York City: The Metropolitan Museum", "New York City: MoMA", "New York City Neighborhood Deep-Dive: Midtown East", "New York City Neighborhood Deep-Dive: Greenwich Village", "New York City Neighborhood Deep-Dive: Williamsburg", "Eating in New York City: Dishes You Must Try", "Markets and Shopping in New York City", "Parks, Water, and Green Escapes in New York City"], "Advanced": ["Hidden Gems of New York City", "New York City in Three Days: The Essential Itinerary", "New York City in Five Days: The Deep Itinerary", "Day Trip from New York City: The Hamptons", "Day Trip from New York City: Hudson Valley", "Photography and Viewpoints in New York City", "Nightlife and Evenings in New York City", "Festivals and Events Calendar for New York City", "New York City with Kids", "Living Like a Local: The Extended Stay in New York City"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-new-york demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-new-york-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-new-york",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
