(function(){'use strict';
/* JAH The Smoke and CO Detectors Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMCDS-";
var FIELDS=["Detector Basics", "Placement & Coverage", "Installation", "Testing & Maintenance", "Alarms & Response", "Special Situations"];
var TOPICS={
 "Detector Basics": [
  "Why Detectors Save Lives (Signature Edition) - Detector Basics",
  "Smoke vs CO: Different Threats (Signature Edition) - Detector Basics",
  "Ionization vs Photoelectric Smoke Alarms (Signature Edition) - Detector Basics",
  "How CO Detectors Work (Signature Edition) - Detector Basics",
  "Power Sources: Battery, Hardwired, Sealed (Signature Edition) - Detector Basics",
  "Lifespan and Replacement Schedules (Signature Edition) - Detector Basics",
  "Alarm Sounds: What Each Means (Signature Edition) - Detector Basics",
  "Detectors and Home Insurance (Signature Edition) - Detector Basics",
  "Renters and Detector Rights (Signature Edition) - Detector Basics",
  "The Science of Early Warning (Signature Edition) - Detector Basics",
  "Common Detector Myths (Signature Edition) - Detector Basics"
 ],
 "Placement & Coverage": [
  "Bedroom Placement Rules (Signature Edition) - Placement & Coverage",
  "Kitchen and Nuisance Alarm Placement (Signature Edition) - Placement & Coverage",
  "Hallways, Stairs, and Basements (Signature Edition) - Placement & Coverage",
  "Garage and Attic Considerations (Signature Edition) - Placement & Coverage",
  "High Ceilings and Special Architecture (Signature Edition) - Placement & Coverage"
 ],
 "Installation": [
  "Installing Battery Detectors (Signature Edition) - Installation",
  "Installing Hardwired Detectors (Signature Edition) - Installation",
  "Interconnecting Wireless Alarms (Signature Edition) - Installation"
 ],
 "Testing & Maintenance": [
  "Monthly Testing Routine (Signature Edition) - Testing & Maintenance",
  "Cleaning Detectors Properly (Signature Edition) - Testing & Maintenance",
  "Battery Replacement Schedules (Signature Edition) - Testing & Maintenance",
  "When Detectors Chirp at 2 AM (Signature Edition) - Testing & Maintenance"
 ],
 "Alarms & Response": [
  "Responding to a Smoke Alarm (Signature Edition) - Alarms & Response",
  "Responding to a CO Alarm (Signature Edition) - Alarms & Response",
  "CO Sources in the Home (Signature Edition) - Alarms & Response",
  "Fire Escape Plans With Detectors (Signature Edition) - Alarms & Response"
 ],
 "Special Situations": [
  "Smart Detectors: Features Worth Having (Signature Edition) - Special Situations",
  "Detectors for Hearing-Impaired Household (Signature Edition) - Special Situations",
  "Detectors in Rentals and Apartments (Signature Edition) - Special Situations",
  "New Construction Detector Codes (Signature Edition) - Special Situations",
  "False Alarms: Causes and Fixes (Signature Edition) - Special Situations",
  "The Whole-Home Detector Map (Signature Edition) - Special Situations",
  "Teaching Kids About Alarms (Signature Edition) - Special Situations"
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
var gen={version:'jahdb-smoke-co-detectors-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('smoke-co-detectors-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
