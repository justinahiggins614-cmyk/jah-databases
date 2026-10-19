(function(){'use strict';
/* JAH Signature Hong Kong Travel Guide Database generator — "jahdb-guide-hong-kong-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GHKGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Hong Kong: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Hong Kong (Signature Edition)", "Getting to Hong Kong (Signature Edition)", "Getting Around Hong Kong (Signature Edition)", "Where to Stay in Hong Kong (Signature Edition)", "Money, Costs, and Budgeting for Hong Kong (Signature Edition)", "Language Essentials for Hong Kong (Signature Edition)", "Safety and Health in Hong Kong (Signature Edition)", "Customs and Etiquette in Hong Kong (Signature Edition)", "What to Pack for Hong Kong (Signature Edition)", "Your First Day in Hong Kong: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Hong Kong (Signature Edition)"], "Compounded": ["Hong Kong: Victoria Peak (Signature Edition)", "Hong Kong: Star Ferry (Signature Edition)", "Hong Kong: Tian Tan Buddha (Signature Edition)", "Hong Kong: Temple Street (Signature Edition)", "Hong Kong: Hong Kong Palace Museum (Signature Edition)", "Hong Kong: M+ (Signature Edition)", "Hong Kong Neighborhood Deep-Dive: Central (Signature Edition)", "Hong Kong Neighborhood Deep-Dive: Tsim Sha Tsui (Signature Edition)", "Hong Kong Neighborhood Deep-Dive: Mong Kok (Signature Edition)", "Eating in Hong Kong: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Hong Kong (Signature Edition)", "Parks, Water, and Green Escapes in Hong Kong (Signature Edition)"], "Advanced": ["Hidden Gems of Hong Kong (Signature Edition)", "Hong Kong in Three Days: The Essential Itinerary (Signature Edition)", "Hong Kong in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Hong Kong: Macau (Signature Edition)", "Day Trip from Hong Kong: Lantau (Signature Edition)", "Photography and Viewpoints in Hong Kong (Signature Edition)", "Nightlife and Evenings in Hong Kong (Signature Edition)", "Festivals and Events Calendar for Hong Kong (Signature Edition)", "Hong Kong with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Hong Kong (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-hong-kong-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-hong-kong-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-hong-kong-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
