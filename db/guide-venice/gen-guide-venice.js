(function(){'use strict';
/* JAH Venice Travel Guide Database generator — "jahdb-guide-venice-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GVEN-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Venice: Orientation and First Impressions", "Best Time to Visit Venice", "Getting to Venice", "Getting Around Venice", "Where to Stay in Venice", "Money, Costs, and Budgeting for Venice", "Language Essentials for Venice", "Safety and Health in Venice", "Customs and Etiquette in Venice", "What to Pack for Venice", "Your First Day in Venice: A Walking Route", "Tourist Information and Emergency Numbers for Venice"], "Compounded": ["Venice: St. Mark’s Basilica", "Venice: Doge’s Palace", "Venice: Rialto Bridge", "Venice: The Grand Canal", "Venice: Peggy Guggenheim Collection", "Venice: Gallerie dell’Accademia", "Venice Neighborhood Deep-Dive: San Marco", "Venice Neighborhood Deep-Dive: Cannaregio", "Venice Neighborhood Deep-Dive: Dorsoduro", "Eating in Venice: Dishes You Must Try", "Markets and Shopping in Venice", "Parks, Water, and Green Escapes in Venice"], "Advanced": ["Hidden Gems of Venice", "Venice in Three Days: The Essential Itinerary", "Venice in Five Days: The Deep Itinerary", "Day Trip from Venice: The lagoon islands", "Day Trip from Venice: Padua", "Photography and Viewpoints in Venice", "Nightlife and Evenings in Venice", "Festivals and Events Calendar for Venice", "Venice with Kids", "Living Like a Local: The Extended Stay in Venice"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-venice demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-venice-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-venice",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
