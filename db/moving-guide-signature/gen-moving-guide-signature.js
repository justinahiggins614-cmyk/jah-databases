(function(){'use strict';
/* JAH The Moving Guide Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MOVGS-";
var FIELDS=["Moving Foundations", "Planning & Timeline", "Packing Systems", "Moving Day", "Unpacking & Settling", "Special Moves"];
var TOPICS={
 "Moving Foundations": [
  "DIY vs Hiring Movers: The Real Math (Signature Edition) - Moving Foundations",
  "Declutter Before You Pack (Signature Edition) - Moving Foundations",
  "Kids and Moving: Easing the Transition (Signature Edition) - Moving Foundations"
 ],
 "Planning & Timeline": [
  "The 8-Week Moving Timeline (Signature Edition) - Planning & Timeline",
  "Choosing a Reputable Mover (Signature Edition) - Planning & Timeline",
  "The Moving Budget: Every Cost (Signature Edition) - Planning & Timeline",
  "Address Changes and Notifications (Signature Edition) - Planning & Timeline",
  "Negotiating With Movers on Price (Signature Edition) - Planning & Timeline",
  "Moving During Peak Season (Signature Edition) - Planning & Timeline"
 ],
 "Packing Systems": [
  "Packing Supplies: What You Actually Need (Signature Edition) - Packing Systems",
  "The Room-by-Room Packing Order (Signature Edition) - Packing Systems",
  "Packing Fragiles and Valuables (Signature Edition) - Packing Systems",
  "Packing the Kitchen (Signature Edition) - Packing Systems",
  "Disassembling and Protecting Furniture (Signature Edition) - Packing Systems"
 ],
 "Moving Day": [
  "The First-Night Survival Kit (Signature Edition) - Moving Day",
  "Moving Day Command Center (Signature Edition) - Moving Day",
  "Loading the Truck Like a Pro (Signature Edition) - Moving Day",
  "Deep Cleaning the Old Place (Signature Edition) - Moving Day",
  "Filing Damage Claims (Signature Edition) - Moving Day",
  "The Ultimate Moving-Day Timeline (Signature Edition) - Moving Day"
 ],
 "Unpacking & Settling": [
  "Unpacking: The Priority System (Signature Edition) - Unpacking & Settling",
  "Setting Up Utilities and Services (Signature Edition) - Unpacking & Settling",
  "The New Home Safety Check (Signature Edition) - Unpacking & Settling",
  "Updating Documents After a Move (Signature Edition) - Unpacking & Settling",
  "The Post-Move 30-Day Checklist (Signature Edition) - Unpacking & Settling",
  "Settling In: Making It Home (Signature Edition) - Unpacking & Settling"
 ],
 "Special Moves": [
  "Moving With Pets (Signature Edition) - Special Moves",
  "Moving Plants Safely (Signature Edition) - Special Moves",
  "Storage Units: Smart Use (Signature Edition) - Special Moves",
  "Long-Distance Moving Logistics (Signature Edition) - Special Moves",
  "International Moving Essentials (Signature Edition) - Special Moves",
  "Moving a Home Office or Business (Signature Edition) - Special Moves",
  "Moving Elderly Parents (Signature Edition) - Special Moves",
  "Temporary Housing Between Homes (Signature Edition) - Special Moves"
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
var gen={version:'jahdb-moving-guide-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('moving-guide-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
