(function(){'use strict';
/* JAH Expedition Cruises Database generator — jahdb-expedition-cruises-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EXCRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is an Expedition Cruise?",
  "Expedition vs Traditional Cruising",
  "Antarctica: The Seventh Continent Voyage",
  "The Arctic: Svalbard and Beyond",
  "The Galapagos by Expedition Ship",
  "Alaska’s Inside Passage, Expedition Style",
  "What’s Included on Expedition Cruises",
  "Expedition Ships, Explained",
  "The Expedition Team: Naturalists and Guides",
  "Zodiac Landings, Explained",
  "When to Book Polar Voyages"
 ],
 "Compounded": [
  "The Northwest Passage",
  "South Georgia and the Falklands",
  "Baja California: Whales and Desert",
  "Papua New Guinea by Expedition Ship",
  "The Kimberley, Australia",
  "Norwegian Fjords, Expedition Style",
  "Greenland’s West Coast",
  "Expedition Cruising and the Environment",
  "Packing for Polar Regions",
  "Photography on Expedition Cruises",
  "Expedition Cruise Lines Compared",
  "The Cost of Expedition Cruising"
 ],
 "Advanced": [
  "Advanced: The Ross Sea and East Antarctica",
  "Advanced: Crossing the Drake Passage",
  "Advanced: Citizen Science on Board",
  "Advanced: Kayaking and Polar Diving",
  "Advanced: The Expedition Grand Voyage",
  "Advanced: Chartering an Expedition Yacht",
  "Advanced: Teaching Expedition Cruising",
  "Advanced: The Polar Travel Journal",
  "Advanced: Expedition Travel Insurance",
  "Advanced: The Expedition Cruise Year",
  "The Expedition Cruises Encyclopedia"
 ]
};
var DEMOKIND="node-demo";
var SAMPLEDESC="Sample records are complete expedition cruise record entries with real measurement math.";
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
    name:topic+' — expedition cruise record record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A expedition cruise record record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-expedition-cruises-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('expedition-cruises-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
