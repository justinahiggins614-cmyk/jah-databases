(function(){'use strict';
/* JAH Signature Venice Travel Guide Database generator — "jahdb-guide-venice-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GVENS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Venice: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Venice (Signature Edition)", "Getting to Venice (Signature Edition)", "Getting Around Venice (Signature Edition)", "Where to Stay in Venice (Signature Edition)", "Money, Costs, and Budgeting for Venice (Signature Edition)", "Language Essentials for Venice (Signature Edition)", "Safety and Health in Venice (Signature Edition)", "Customs and Etiquette in Venice (Signature Edition)", "What to Pack for Venice (Signature Edition)", "Your First Day in Venice: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Venice (Signature Edition)"], "Compounded": ["Venice: St. Mark’s Basilica (Signature Edition)", "Venice: Doge’s Palace (Signature Edition)", "Venice: Rialto Bridge (Signature Edition)", "Venice: The Grand Canal (Signature Edition)", "Venice: Peggy Guggenheim Collection (Signature Edition)", "Venice: Gallerie dell’Accademia (Signature Edition)", "Venice Neighborhood Deep-Dive: San Marco (Signature Edition)", "Venice Neighborhood Deep-Dive: Cannaregio (Signature Edition)", "Venice Neighborhood Deep-Dive: Dorsoduro (Signature Edition)", "Eating in Venice: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Venice (Signature Edition)", "Parks, Water, and Green Escapes in Venice (Signature Edition)"], "Advanced": ["Hidden Gems of Venice (Signature Edition)", "Venice in Three Days: The Essential Itinerary (Signature Edition)", "Venice in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Venice: The lagoon islands (Signature Edition)", "Day Trip from Venice: Padua (Signature Edition)", "Photography and Viewpoints in Venice (Signature Edition)", "Nightlife and Evenings in Venice (Signature Edition)", "Festivals and Events Calendar for Venice (Signature Edition)", "Venice with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Venice (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-venice-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original travel guide record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original travel guide record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-guide-venice-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-venice-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
