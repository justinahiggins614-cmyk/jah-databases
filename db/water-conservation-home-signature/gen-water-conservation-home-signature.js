(function(){'use strict';
/* JAH Water Conservation at Home Database generator — jahdb-water-conservation-home-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WATECHS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Water Audit (Signature Edition)", "Leak Detection (Signature Edition)", "Toilet Efficiency (Signature Edition)", "Showerheads (Signature Edition)", "Faucet Aerators (Signature Edition)", "Dishwashers (Signature Edition)", "Laundry (Signature Edition)", "Outdoor Audit (Signature Edition)", "Smart Irrigation (Signature Edition)", "Native Landscaping (Signature Edition)", "Rain Barrels (Signature Edition)"], "Compounded": ["Greywater (Signature Edition)", "Teaching Conservation (Signature Edition)", "The Annual Water Review (Signature Edition)", "Water Softeners (Signature Edition)", "Water Pressure (Signature Edition)", "Swimming Pools (Signature Edition)", "Water Features (Signature Edition)", "Xeriscaping (Signature Edition)", "Lawn Alternatives (Signature Edition)", "Drip vs Spray (Signature Edition)", "Irrigation Scheduling (Signature Edition)", "Rain Gardens (Signature Edition)"], "Advanced": ["Permeable Paving (Signature Edition)", "Water-Efficient Appliances (Signature Edition)", "Hot Water Efficiency (Signature Edition)", "Water Bills Explained (Signature Edition)", "Drought Response (Signature Edition)", "Well Water (Signature Edition)", "Water Quality (Signature Edition)", "Stormwater (Signature Edition)", "Community Water (Signature Edition)", "Teaching Water Wisdom (Signature Edition)", "Emergency Water (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — conservation guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — conservation guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A conservation guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"water-conservation-home-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-water-conservation-home-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("water-conservation-home-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
