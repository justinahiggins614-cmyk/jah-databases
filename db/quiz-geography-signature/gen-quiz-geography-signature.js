(function(){'use strict';
/* JAH The Geography Quiz Signature Database generator — jahdb-quiz-geography-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-QZGES-";
var FIELDS=["Climate and Earth","Countries and Capitals","Landforms and Mountains","Maps and Navigation","Places and Records","Rivers and Water"];
var TOPICS={
 "Climate and Earth": [
  "The Volcanoes and Earthquakes Quiz (Signature Edition) - Climate and Earth",
  "The Climate Zones and Weather Quiz (Signature Edition) - Climate and Earth",
  "The Polar Regions Quiz (Signature Edition) - Climate and Earth",
  "The Plate Tectonics Quiz (Signature Edition) - Climate and Earth"
 ],
 "Countries and Capitals": [
  "The World Capitals Quiz (Signature Edition) - Countries and Capitals",
  "The United States States and Capitals Quiz (Signature Edition) - Countries and Capitals",
  "The Europe Countries and Capitals Quiz (Signature Edition) - Countries and Capitals",
  "The Asia Countries and Capitals Quiz (Signature Edition) - Countries and Capitals",
  "The Africa Countries and Capitals Quiz (Signature Edition) - Countries and Capitals",
  "The South America Countries and Capitals Quiz (Signature Edition) - Countries and Capitals",
  "The Central Asia and Caucasus Quiz (Signature Edition) - Countries and Capitals",
  "The Middle East Geography Quiz (Signature Edition) - Countries and Capitals"
 ],
 "Landforms and Mountains": [
  "The Mountains and Mountain Ranges Quiz (Signature Edition) - Landforms and Mountains",
  "The Deserts and Rainforests Quiz (Signature Edition) - Landforms and Mountains",
  "The Islands and Archipelagos Quiz (Signature Edition) - Landforms and Mountains",
  "The Caves, Canyons, and Natural Wonders Quiz (Signature Edition) - Landforms and Mountains"
 ],
 "Maps and Navigation": [
  "The Continents and Oceans Quiz (Signature Edition) - Maps and Navigation",
  "The Maps and Compass Directions Quiz (Signature Edition) - Maps and Navigation",
  "The Latitude, Longitude, and Time Zones Quiz (Signature Edition) - Maps and Navigation",
  "The Map Projections and Scale Quiz (Signature Edition) - Maps and Navigation"
 ],
 "Places and Records": [
  "The Famous Landmarks Quiz (Signature Edition) - Places and Records",
  "The Country Borders and Enclaves Quiz (Signature Edition) - Places and Records",
  "The Highest, Deepest, Longest Quiz (Signature Edition) - Places and Records",
  "The Population and Biggest Cities Quiz (Signature Edition) - Places and Records",
  "The Island Nations Quiz (Signature Edition) - Places and Records",
  "The Unusual Borders and Geography Trivia Quiz (Signature Edition) - Places and Records",
  "The Grand Geography Challenge Quiz (Signature Edition) - Places and Records"
 ],
 "Rivers and Water": [
  "The Great Rivers of the World Quiz (Signature Edition) - Rivers and Water",
  "The Lakes and Inland Seas Quiz (Signature Edition) - Rivers and Water",
  "The Rivers of the Americas Quiz (Signature Edition) - Rivers and Water",
  "The Rivers of Africa and Asia Quiz (Signature Edition) - Rivers and Water",
  "The Ocean Currents and Tides Quiz (Signature Edition) - Rivers and Water",
  "The European Rivers Quiz (Signature Edition) - Rivers and Water",
  "The Waterfalls, Rapids, and Deltas Quiz (Signature Edition) - Rivers and Water"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Geography Quiz — "+safe+"\n"
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
    name:topic+' — quiz record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A quiz record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"geography-quiz-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-quiz-geography-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quiz-geography-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
