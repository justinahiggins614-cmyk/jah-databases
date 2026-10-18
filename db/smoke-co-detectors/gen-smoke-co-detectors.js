(function(){'use strict';
/* JAH The Smoke and CO Detectors Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMCD-";
var FIELDS=["Detector Basics", "Placement & Coverage", "Installation", "Testing & Maintenance", "Alarms & Response", "Special Situations"];
var TOPICS={
 "Detector Basics": [
  "Why Detectors Save Lives - Detector Basics",
  "Smoke vs CO: Different Threats - Detector Basics",
  "Ionization vs Photoelectric Smoke Alarms - Detector Basics",
  "How CO Detectors Work - Detector Basics",
  "Power Sources: Battery, Hardwired, Sealed - Detector Basics",
  "Lifespan and Replacement Schedules - Detector Basics",
  "Alarm Sounds: What Each Means - Detector Basics",
  "Detectors and Home Insurance - Detector Basics",
  "Renters and Detector Rights - Detector Basics",
  "The Science of Early Warning - Detector Basics",
  "Common Detector Myths - Detector Basics"
 ],
 "Placement & Coverage": [
  "Bedroom Placement Rules - Placement & Coverage",
  "Kitchen and Nuisance Alarm Placement - Placement & Coverage",
  "Hallways, Stairs, and Basements - Placement & Coverage",
  "Garage and Attic Considerations - Placement & Coverage",
  "High Ceilings and Special Architecture - Placement & Coverage"
 ],
 "Installation": [
  "Installing Battery Detectors - Installation",
  "Installing Hardwired Detectors - Installation",
  "Interconnecting Wireless Alarms - Installation"
 ],
 "Testing & Maintenance": [
  "Monthly Testing Routine - Testing & Maintenance",
  "Cleaning Detectors Properly - Testing & Maintenance",
  "Battery Replacement Schedules - Testing & Maintenance",
  "When Detectors Chirp at 2 AM - Testing & Maintenance"
 ],
 "Alarms & Response": [
  "Responding to a Smoke Alarm - Alarms & Response",
  "Responding to a CO Alarm - Alarms & Response",
  "CO Sources in the Home - Alarms & Response",
  "Fire Escape Plans With Detectors - Alarms & Response"
 ],
 "Special Situations": [
  "Smart Detectors: Features Worth Having - Special Situations",
  "Detectors for Hearing-Impaired Household - Special Situations",
  "Detectors in Rentals and Apartments - Special Situations",
  "New Construction Detector Codes - Special Situations",
  "False Alarms: Causes and Fixes - Special Situations",
  "The Whole-Home Detector Map - Special Situations",
  "Teaching Kids About Alarms - Special Situations"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Smoke and CO Detector Guide Study — "+safe+"\n"
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
    name:topic+' — detector guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A detector guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"smoke-co-detectors-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-smoke-co-detectors-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('smoke-co-detectors',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
