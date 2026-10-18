(function(){'use strict';
/* JAH The Weather Explorer Game generator — jahdb-db-weather-explorer-game-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WEGS-";
var FIELDS=["Sky Reading","Systems","Forecasting"];
var TOPICS={
 "Sky Reading": [
  "Look Up: The First Instrument (Signature Edition) - Sky Reading",
  "Cloud Families (Signature Edition) - Sky Reading",
  "Cirrus: Mare's Tails (Signature Edition) - Sky Reading",
  "Cumulus: Fair-Weather Puffs (Signature Edition) - Sky Reading",
  "Stratus: The Gray Blanket (Signature Edition) - Sky Reading",
  "Cumulonimbus: The Storm King (Signature Edition) - Sky Reading",
  "Reading Wind (Signature Edition) - Sky Reading",
  "Humidity: Feeling the Air (Signature Edition) - Sky Reading",
  "Pressure: The Invisible Ocean (Signature Edition) - Sky Reading",
  "Fog: Cloud on the Ground (Signature Edition) - Sky Reading",
  "Rainbows: Light's Signature (Signature Edition) - Sky Reading",
  "Halos and Sun Dogs (Signature Edition) - Sky Reading"
 ],
 "Systems": [
  "Highs and Lows (Signature Edition) - Systems",
  "Cold Fronts: The Clash (Signature Edition) - Systems",
  "Warm Fronts: The Slow Soak (Signature Edition) - Systems",
  "Thunderstorms: Anatomy (Signature Edition) - Systems",
  "Tornadoes: Nature's Fiercest (Signature Edition) - Systems",
  "Hurricanes: Ocean Giants (Signature Edition) - Systems",
  "Blizzards and Winter Storms (Signature Edition) - Systems",
  "The Jet Stream (Signature Edition) - Systems",
  "El Ni\u00f1o and La Ni\u00f1a (Signature Edition) - Systems",
  "Monsoons (Signature Edition) - Systems",
  "Heat Waves: The Silent Killer (Signature Edition) - Systems"
 ],
 "Forecasting": [
  "Reading Weather Maps (Signature Edition) - Forecasting",
  "Your Backyard Station (Signature Edition) - Forecasting",
  "Short-Term Forecasting (Signature Edition) - Forecasting",
  "Understanding Forecast Models (Signature Edition) - Forecasting",
  "Forecast Uncertainty (Signature Edition) - Forecasting",
  "Severe Weather Safety (Signature Edition) - Forecasting",
  "Climate vs Weather (Signature Edition) - Forecasting",
  "Keeping a Weather Diary (Signature Edition) - Forecasting",
  "Storm Spotting (Signature Edition) - Forecasting",
  "The Water Cycle (Signature Edition) - Forecasting",
  "Becoming the Local Forecaster (Signature Edition) - Forecasting"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Weather Explorer Study — "+safe+"\n"
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
    name:topic+' — weather lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A weather lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"weather-explorer-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-weather-explorer-game-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-weather-explorer-game-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
