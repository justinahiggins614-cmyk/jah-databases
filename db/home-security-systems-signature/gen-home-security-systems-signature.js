(function(){'use strict';
/* JAH The Home Security Systems Signature Database generator — jahdb-home-cleaning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HSECS-";
var FIELDS=["Security Foundations", "Doors, Locks & Entry", "Alarms & Sensors", "Cameras & Monitoring", "Smart Security", "Habits & Deterrence"];
var TOPICS={
 "Security Foundations": [
  "Layered Security: The Core Concept (Signature Edition) - Security Foundations",
  "Think Like a Burglar: The 60-Second Rule (Signature Edition) - Security Foundations",
  "Lighting as Security (Signature Edition) - Security Foundations",
  "Landscaping for Security (Signature Edition) - Security Foundations",
  "The Security Audit Walkthrough (Signature Edition) - Security Foundations",
  "Mail, Packages, and Porch Piracy (Signature Edition) - Security Foundations",
  "The Annual Security Review (Signature Edition) - Security Foundations"
 ],
 "Doors, Locks & Entry": [
  "Doors: Your First Line of Defense (Signature Edition) - Doors, Locks & Entry",
  "Deadbolts and Lock Grades (Signature Edition) - Doors, Locks & Entry",
  "Sliding Doors and Windows (Signature Edition) - Doors, Locks & Entry",
  "Garage Security (Signature Edition) - Doors, Locks & Entry",
  "Keys, Codes, and Access Control (Signature Edition) - Doors, Locks & Entry"
 ],
 "Alarms & Sensors": [
  "Alarm Systems: Monitored vs Self-Monitored (Signature Edition) - Alarms & Sensors",
  "Door and Window Sensors (Signature Edition) - Alarms & Sensors",
  "Motion Detectors Indoors (Signature Edition) - Alarms & Sensors",
  "Safes: What Goes In and Where (Signature Edition) - Alarms & Sensors",
  "Firearms Storage and Home Safety (Signature Edition) - Alarms & Sensors"
 ],
 "Cameras & Monitoring": [
  "Security Cameras: Placement and Practice (Signature Edition) - Cameras & Monitoring",
  "Video Doorbells (Signature Edition) - Cameras & Monitoring",
  "Security Cameras: Legal Considerations (Signature Edition) - Cameras & Monitoring"
 ],
 "Smart Security": [
  "Smart Locks: Benefits and Risks (Signature Edition) - Smart Security",
  "Home Automation for Security (Signature Edition) - Smart Security",
  "Security System Integration Platforms (Signature Edition) - Smart Security",
  "Safe Rooms: Design and Supplies (Signature Edition) - Smart Security",
  "Integrating Security With Smart Home (Signature Edition) - Smart Security"
 ],
 "Habits & Deterrence": [
  "Vacation Security: The Empty House (Signature Edition) - Habits & Deterrence",
  "Neighborhood Watch Participation (Signature Edition) - Habits & Deterrence",
  "What To Do During a Break-In (Signature Edition) - Habits & Deterrence",
  "Perimeter Security: Fences and Gates (Signature Edition) - Habits & Deterrence",
  "Security for Renters (Signature Edition) - Habits & Deterrence",
  "Elderly Home Security Adaptations (Signature Edition) - Habits & Deterrence",
  "Home Security on a Budget (Signature Edition) - Habits & Deterrence",
  "After a Break-In: Recovery (Signature Edition) - Habits & Deterrence",
  "Building a Security-Minded Household (Signature Edition) - Habits & Deterrence"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# JAH Home Security Guide Study — "+safe+"\n"
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
    name:topic+' — home security guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A home security guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"home-security-systems-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-home-security-systems-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-security-systems-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
