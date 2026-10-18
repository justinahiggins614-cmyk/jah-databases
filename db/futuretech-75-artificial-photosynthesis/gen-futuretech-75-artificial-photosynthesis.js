(function(){'use strict';
/* JAH The Artificial Photosynthesis Future Technology Database generator — jahdb-futuretech-75-artificial-photosynthesis-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT75-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1772: Priestley Finds Photosynthesis - Foundations",
  "1839: the Photovoltaic Effect - Foundations",
  "1950s: the Calvin Cycle - Foundations",
  "1912: Ciamician's Solar Dream - Foundations",
  "1972: Water Split by Light - Foundations",
  "1970s: Photocatalysis Grows - Foundations",
  "1991: Gr\u00e4tzel Cells - Foundations",
  "2011: the Artificial Leaf - Foundations",
  "2016: the Bionic Leaf - Foundations",
  "2018: the Solar Fuel Sprint - Foundations",
  "2019: Photocatalytic Panels - Foundations"
 ],
 "Compounded": [
  "2020: CO2 Becomes Fuel - Compounded",
  "2021: Solar Fuel Demos - Compounded",
  "2022: Perovskite Photocatalysts - Compounded",
  "2023: Pilots Scale - Compounded",
  "2024: Efficiency Records - Compounded",
  "2025: Commercial Pilots - Compounded",
  "2025: Solar Fuel Costs Fall - Compounded",
  "The Efficient Artificial Leaf - Compounded",
  "The Solar Hydrogen Economy - Compounded",
  "CO2 to Fuel at Scale - Compounded",
  "Artificial Forests - Compounded",
  "Fuel from Air - Compounded"
 ],
 "Advanced": [
  "The Personal Fuel Maker - Advanced",
  "Desert Fuel Farms - Advanced",
  "The Carbon-Negative Economy - Advanced",
  "Synthetic Hydrocarbons - Advanced",
  "Solar Fuel for Aviation - Advanced",
  "Global Solar Fuel Trade - Advanced",
  "Photosynthesis 2.0 - Advanced",
  "The Green Refinery - Advanced",
  "Atmospheric Fuel - Advanced",
  "The Photosynthetic Civilization - Advanced",
  "Everyday Solar Fuel - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — artificial photosynthesis record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A artificial photosynthesis record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-75-artificial-photosynthesis-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-75-artificial-photosynthesis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-75-artificial-photosynthesis',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
