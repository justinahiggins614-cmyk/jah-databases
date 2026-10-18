(function(){'use strict';
/* JAH The Elderly Home Safety Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EHSA-";
var FIELDS=["Safety Foundations", "Fall Prevention", "Bathroom Safety", "Kitchen & Daily Living", "Medical & Emergency", "Aging in Place Planning"];
var TOPICS={
 "Safety Foundations": [
  "Why Falls Are the Top Threat - Safety Foundations",
  "The Home Safety Walkthrough - Safety Foundations",
  "Lighting: The First Fix - Safety Foundations",
  "Clear Pathways Throughout the Home - Safety Foundations",
  "Emergency Access and Communication - Safety Foundations",
  "Scam and Fraud Awareness for Seniors - Safety Foundations",
  "Fire Safety for Older Adults - Safety Foundations",
  "The Senior Home Safety Checklist - Safety Foundations",
  "Celebrating Safe Independence - Safety Foundations"
 ],
 "Fall Prevention": [
  "Stair Safety and Alternatives - Fall Prevention",
  "Living Room and General Fall-Proofing - Fall Prevention",
  "Footwear and Clothing Safety - Fall Prevention",
  "Exercise for Fall Prevention - Fall Prevention"
 ],
 "Bathroom Safety": [
  "Bathroom: The Highest-Risk Room - Bathroom Safety",
  "Grab Bars: Placement and Installation - Bathroom Safety",
  "Walk-In Tubs and Shower Conversions - Bathroom Safety",
  "Toilet Safety and Accessibility - Bathroom Safety"
 ],
 "Kitchen & Daily Living": [
  "Kitchen Safety Adaptations - Kitchen & Daily Living",
  "Bedroom Safety for Seniors - Kitchen & Daily Living",
  "Nutrition and Hydration for Strength - Kitchen & Daily Living"
 ],
 "Medical & Emergency": [
  "Medication Safety at Home - Medical & Emergency",
  "The Daily Check-In System - Medical & Emergency",
  "Vision and Hearing: The Sensory Foundation - Medical & Emergency",
  "Technology for Senior Safety - Medical & Emergency",
  "Dementia Home Safety - Medical & Emergency"
 ],
 "Aging in Place Planning": [
  "Home Modifications: The Big Picture - Aging in Place Planning",
  "Aging in Place vs Moving: The Decision - Aging in Place Planning",
  "Hiring In-Home Care - Aging in Place Planning",
  "End-of-Life Planning at Home - Aging in Place Planning",
  "Financial Safety for Seniors - Aging in Place Planning",
  "Coordinating Family Caregiving - Aging in Place Planning",
  "Veterans' Home Safety Benefits - Aging in Place Planning",
  "When 24-Hour Care Becomes Needed - Aging in Place Planning",
  "Leaving a Safety Legacy - Aging in Place Planning"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Elderly Home Safety Guide Study — "+safe+"\n"
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
    name:topic+' — elderly home safety record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A elderly home safety record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"elderly-home-safety-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-elderly-home-safety-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('elderly-home-safety',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
