(function(){'use strict';
/* JAH River Cruises Database generator — jahdb-river-cruises-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RVCRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a River Cruise?",
  "River Cruise vs Ocean Cruise",
  "The Danube: Europe’s Classic River",
  "The Rhine: Castles and Wine",
  "The Seine: Paris to Normandy",
  "The Douro: Portugal’s Wine River",
  "The Mekong: Southeast Asia by River",
  "The Nile: Egypt’s Ancient Waterway",
  "What’s Included on a River Cruise",
  "River Cruise Cabin Types",
  "When to Book a River Cruise"
 ],
 "Compounded": [
  "The Rhône and Saône: Burgundy and Provence",
  "The Main and Moselle",
  "The Volga: Russia’s Waterways",
  "The Yangtze: China’s Great River",
  "The Amazon by Riverboat",
  "The Mississippi: America’s River",
  "Christmas Market River Cruises",
  "Wine-Themed River Cruises",
  "Bike-and-Barge Cruises",
  "River Cruise Excursions, Explained",
  "Dining on River Cruises",
  "River Cruise Lines Compared"
 ],
 "Advanced": [
  "Advanced: The Grand European Tour",
  "Advanced: Back-to-Back River Cruises",
  "Advanced: Chartering a River Barge",
  "Advanced: Hotel Barges in France",
  "Advanced: River Cruise Loyalty Programs",
  "Advanced: The River Cruise Year",
  "Advanced: Expedition River Cruising",
  "Advanced: Teaching River Cruise Planning",
  "Advanced: The River Cruise Photo Journal",
  "Advanced: Accessibility on River Cruises",
  "The River Cruises Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete river cruise record entries with real measurement math.";
function demoProgram(topic,field){
  return "'use strict';\n// "+topic+" \u2014 sample demo.\n// Field: "+field+"\nconst a = 12;\nconst b = 4;\nconst r = a / b;\nconsole.log('sample ratio = ' + r.toFixed(2));\nif (!isFinite(r)) throw new Error('bad');\nconsole.log('DEMO_OK');\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — river cruise record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A river cruise record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'node',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-river-cruises-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('river-cruises-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
