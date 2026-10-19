(function(){'use strict';
/* JAH Signature Warsaw Travel Guide Database generator — "jahdb-guide-warsaw-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GWARS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Warsaw: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Warsaw (Signature Edition)", "Getting to Warsaw (Signature Edition)", "Getting Around Warsaw (Signature Edition)", "Where to Stay in Warsaw (Signature Edition)", "Money, Costs, and Budgeting for Warsaw (Signature Edition)", "Language Essentials for Warsaw (Signature Edition)", "Safety and Health in Warsaw (Signature Edition)", "Customs and Etiquette in Warsaw (Signature Edition)", "What to Pack for Warsaw (Signature Edition)", "Your First Day in Warsaw: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Warsaw (Signature Edition)"], "Compounded": ["Warsaw: Old Town (Signature Edition)", "Warsaw: Łazienki Park (Signature Edition)", "Warsaw: Palace of Culture (Signature Edition)", "Warsaw: Royal Castle (Signature Edition)", "Warsaw: Warsaw Uprising Museum (Signature Edition)", "Warsaw: POLIN (Signature Edition)", "Warsaw Neighborhood Deep-Dive: Śródmieście (Signature Edition)", "Warsaw Neighborhood Deep-Dive: Praga (Signature Edition)", "Warsaw Neighborhood Deep-Dive: Wola (Signature Edition)", "Eating in Warsaw: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Warsaw (Signature Edition)", "Parks, Water, and Green Escapes in Warsaw (Signature Edition)"], "Advanced": ["Hidden Gems of Warsaw (Signature Edition)", "Warsaw in Three Days: The Essential Itinerary (Signature Edition)", "Warsaw in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Warsaw: Krakow (Signature Edition)", "Day Trip from Warsaw: Żelazowa Wola (Signature Edition)", "Photography and Viewpoints in Warsaw (Signature Edition)", "Nightlife and Evenings in Warsaw (Signature Edition)", "Festivals and Events Calendar for Warsaw (Signature Edition)", "Warsaw with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Warsaw (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-warsaw-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-warsaw-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-warsaw-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
