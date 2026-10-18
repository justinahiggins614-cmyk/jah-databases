(function(){'use strict';
/* JAH The Personal Trainers Database generator — jahdb-personal-trainers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PTRAIN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Personal Trainers Do",
  "Certification Paths: NASM, ACE, ACSM",
  "Anatomy for Trainers",
  "Client Assessment",
  "Program Design Basics",
  "Nutrition Coaching Basics",
  "Exercise Form and Cueing",
  "Safety and Liability",
  "The Consultation and Sale",
  "Training Special Populations Intro",
  "History of Fitness Training",
 ],
 "Compounded": [
  "Strength Programming",
  "HIIT Design",
  "Mobility and Corrective Exercise",
  "Weight Loss Coaching",
  "Muscle Gain Programming",
  "Online Training Business",
  "Group Training",
  "Senior Fitness",
  "Pre and Postnatal Training",
  "Sport-Specific Training",
  "Client Retention",
  "Tracking and Metrics",
 ],
 "Advanced": [
  "Advanced Periodization",
  "Business Mastery for Trainers",
  "Building a Training Brand",
  "Corporate Wellness Contracts",
  "Rehab Collaboration",
  "Competition Prep Coaching",
  "Gym Ownership",
  "The Trainer Career Ladder",
  "Continuing Education Strategy",
  "Future of Personal Training",
  "Fitness Franchise Ownership",
 ],
};
var DEMOKIND="fitness calculation";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fitness calculator — "+safe+"\n"
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
    name:topic+' — personal trainer profession record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A miners profession record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-personal-trainers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-trainers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
