(function(){'use strict';
/* JAH The Moving Guide Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MOVG-";
var FIELDS=["Moving Foundations", "Planning & Timeline", "Packing Systems", "Moving Day", "Unpacking & Settling", "Special Moves"];
var TOPICS={
 "Moving Foundations": [
  "DIY vs Hiring Movers: The Real Math - Moving Foundations",
  "Declutter Before You Pack - Moving Foundations",
  "Kids and Moving: Easing the Transition - Moving Foundations"
 ],
 "Planning & Timeline": [
  "The 8-Week Moving Timeline - Planning & Timeline",
  "Choosing a Reputable Mover - Planning & Timeline",
  "The Moving Budget: Every Cost - Planning & Timeline",
  "Address Changes and Notifications - Planning & Timeline",
  "Negotiating With Movers on Price - Planning & Timeline",
  "Moving During Peak Season - Planning & Timeline"
 ],
 "Packing Systems": [
  "Packing Supplies: What You Actually Need - Packing Systems",
  "The Room-by-Room Packing Order - Packing Systems",
  "Packing Fragiles and Valuables - Packing Systems",
  "Packing the Kitchen - Packing Systems",
  "Disassembling and Protecting Furniture - Packing Systems"
 ],
 "Moving Day": [
  "The First-Night Survival Kit - Moving Day",
  "Moving Day Command Center - Moving Day",
  "Loading the Truck Like a Pro - Moving Day",
  "Deep Cleaning the Old Place - Moving Day",
  "Filing Damage Claims - Moving Day",
  "The Ultimate Moving-Day Timeline - Moving Day"
 ],
 "Unpacking & Settling": [
  "Unpacking: The Priority System - Unpacking & Settling",
  "Setting Up Utilities and Services - Unpacking & Settling",
  "The New Home Safety Check - Unpacking & Settling",
  "Updating Documents After a Move - Unpacking & Settling",
  "The Post-Move 30-Day Checklist - Unpacking & Settling",
  "Settling In: Making It Home - Unpacking & Settling"
 ],
 "Special Moves": [
  "Moving With Pets - Special Moves",
  "Moving Plants Safely - Special Moves",
  "Storage Units: Smart Use - Special Moves",
  "Long-Distance Moving Logistics - Special Moves",
  "International Moving Essentials - Special Moves",
  "Moving a Home Office or Business - Special Moves",
  "Moving Elderly Parents - Special Moves",
  "Temporary Housing Between Homes - Special Moves"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Moving Guide Study — "+safe+"\n"
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
    name:topic+' — moving guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A moving guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"moving-guide-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-moving-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('moving-guide',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
