(function(){'use strict';
/* JAH The Home Safety Signature Database generator — jahdb-home-safety-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HSFS-";
var FIELDS=["Safety Foundations","Fire Prevention","Electrical & Gas","Child & Pet Proofing","Fall & Injury Prevention","Emergency Planning & Security"];
var TOPICS={
 "Safety Foundations": [
  "The Home Safety Walk-Through (Signature Edition) - Safety Foundations",
  "Smoke Alarms: Placement, Testing, Replacement (Signature Edition) - Safety Foundations",
  "Carbon Monoxide: The Silent Killer (Signature Edition) - Safety Foundations",
  "Fire Extinguishers: Types and Use (Signature Edition) - Safety Foundations",
  "Poison Prevention and the Poison Helpline (Signature Edition) - Safety Foundations",
  "Water Safety at Home (Signature Edition) - Safety Foundations"
 ],
 "Fire Prevention": [
  "Stovetop Fire Safety (Signature Edition) - Fire Prevention",
  "Heating Equipment Safety (Signature Edition) - Fire Prevention",
  "Candles, Smoking, and Open Flames (Signature Edition) - Fire Prevention",
  "Dryer and Laundry Fire Prevention (Signature Edition) - Fire Prevention",
  "Holiday and Decoration Fire Safety (Signature Edition) - Fire Prevention",
  "Grill and Outdoor Fire Safety (Signature Edition) - Fire Prevention"
 ],
 "Electrical & Gas": [
  "Outlets, Cords, and Power Strips (Signature Edition) - Electrical & Gas",
  "GFCI and AFCI Protection (Signature Edition) - Electrical & Gas",
  "Natural Gas Safety and Leak Response (Signature Edition) - Electrical & Gas",
  "Lightning and Surge Protection (Signature Edition) - Electrical & Gas",
  "Portable Generator Placement (Signature Edition) - Electrical & Gas"
 ],
 "Child & Pet Proofing": [
  "Baby Proofing Room by Room (Signature Edition) - Child & Pet Proofing",
  "Choking Hazards and Small Objects (Signature Edition) - Child & Pet Proofing",
  "Window and Balcony Safety for Kids (Signature Edition) - Child & Pet Proofing",
  "Pet Proofing the Home (Signature Edition) - Child & Pet Proofing",
  "Stairs, Doors, and Pinch Points (Signature Edition) - Child & Pet Proofing"
 ],
 "Fall & Injury Prevention": [
  "Preventing Falls: The Big Three Fixes (Signature Edition) - Fall & Injury Prevention",
  "Bathroom Grab Bars and Non-Slip Surfaces (Signature Edition) - Fall & Injury Prevention",
  "Ladder Safety at Home (Signature Edition) - Fall & Injury Prevention",
  "Sharp Objects and Tool Storage (Signature Edition) - Fall & Injury Prevention",
  "Safe Lifting and Moving Heavy Objects (Signature Edition) - Fall & Injury Prevention",
  "Winter Home Hazards: Ice, Heating, and Pipes (Signature Edition) - Fall & Injury Prevention"
 ],
 "Emergency Planning & Security": [
  "The Family Emergency Plan (Signature Edition) - Emergency Planning & Security",
  "Emergency Kits: Home, Car, and Go-Bag (Signature Edition) - Emergency Planning & Security",
  "Home Security Basics: Doors, Windows, Lighting (Signature Edition) - Emergency Planning & Security",
  "Security Systems and Cameras: What Matters (Signature Edition) - Emergency Planning & Security",
  "What To Do in a Home Invasion (Signature Edition) - Emergency Planning & Security",
  "Neighborhood Watch and Community Safety (Signature Edition) - Emergency Planning & Security"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Home Safety Study — "+safe+"\n"
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
    name:topic+' — home safety guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A home safety guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"home-safety-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-home-safety-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-safety-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
