(function(){'use strict';
/* JAH The Artificial Photosynthesis Future Technology Database — Signature Edition generator — jahdb-futuretech-75-artificial-photosynthesis-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT75-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Artificial Photosynthesis — Priestley Finds Photosynthesis (Signature Edition)", "Artificial Photosynthesis — the Photovoltaic Effect (Signature Edition)", "Artificial Photosynthesis — the Calvin Cycle (Signature Edition)", "Artificial Photosynthesis — Ciamician's Solar Dream (Signature Edition)", "Artificial Photosynthesis — Water Split by Light (Signature Edition)", "Artificial Photosynthesis — Photocatalysis Grows (Signature Edition)", "Artificial Photosynthesis — Grätzel Cells (Signature Edition)", "Artificial Photosynthesis — the Artificial Leaf (Signature Edition)", "Artificial Photosynthesis — the Bionic Leaf (Signature Edition)", "Artificial Photosynthesis — the Solar Fuel Sprint (Signature Edition)", "Artificial Photosynthesis — Photocatalytic Panels (Signature Edition)"], "Compounded": ["Artificial Photosynthesis — CO2 Becomes Fuel (Signature Edition)", "Artificial Photosynthesis — Solar Fuel Demos (Signature Edition)", "Artificial Photosynthesis — Perovskite Photocatalysts (Signature Edition)", "Artificial Photosynthesis — Pilots Scale (Signature Edition)", "Artificial Photosynthesis — Efficiency Records (Signature Edition)", "Artificial Photosynthesis — Commercial Pilots (Signature Edition)", "Artificial Photosynthesis — Solar Fuel Costs Fall (Signature Edition)", "Artificial Photosynthesis — The Efficient Artificial Leaf (Signature Edition)", "Artificial Photosynthesis — The Solar Hydrogen Economy (Signature Edition)", "Artificial Photosynthesis — CO2 to Fuel at Scale (Signature Edition)", "Artificial Photosynthesis — Artificial Forests (Signature Edition)", "Artificial Photosynthesis — Fuel from Air (Signature Edition)"], "Advanced": ["Artificial Photosynthesis — The Personal Fuel Maker (Signature Edition)", "Artificial Photosynthesis — Desert Fuel Farms (Signature Edition)", "Artificial Photosynthesis — The Carbon-Negative Economy (Signature Edition)", "Artificial Photosynthesis — Synthetic Hydrocarbons (Signature Edition)", "Artificial Photosynthesis — Solar Fuel for Aviation (Signature Edition)", "Artificial Photosynthesis — Global Solar Fuel Trade (Signature Edition)", "Artificial Photosynthesis — Photosynthesis 2.0 (Signature Edition)", "Artificial Photosynthesis — The Green Refinery (Signature Edition)", "Artificial Photosynthesis — Atmospheric Fuel (Signature Edition)", "Artificial Photosynthesis — The Photosynthetic Civilization (Signature Edition)", "Artificial Photosynthesis — Everyday Solar Fuel - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Artificial Photosynthesis study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-75-artificial-photosynthesis-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-75-artificial-photosynthesis-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
