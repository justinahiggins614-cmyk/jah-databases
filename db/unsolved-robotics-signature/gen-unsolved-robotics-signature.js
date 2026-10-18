(function(){'use strict';
/* JAH The Unsolved Robotics Signature Database generator — jahdb-unsolved-robotics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USROS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Moravec's Paradox: Why Robots Can't Do Easy Things (Signature Edition) - Foundations",
  "Robotic Grasping: The Pick-Up Problem (Signature Edition) - Manipulation",
  "SLAM: Mapping the Unknown (Signature Edition) - Navigation",
  "Humanoid Walking: The Biped Problem (Signature Edition) - Locomotion",
  "Robot Safety: Working Beside Humans (Signature Edition) - Interaction",
  "Soft Robotics: The Squishy Machine (Signature Edition) - Design",
  "Swarm Robotics: The Collective Machine (Signature Edition) - Systems",
  "Robot Learning: The Data Problem (Signature Edition) - AI",
  "Tactile Sensing: The Sense of Touch (Signature Edition) - Sensing",
  "Autonomous Driving: The Last 1% (Signature Edition) - Navigation",
  "Drone Autonomy: Flying Without Pilots (Signature Edition) - Navigation"
 ],
 "Compounded": [
  "Exoskeletons: The Wearable Robot (Signature Edition) - Interaction",
  "Surgical Robots: The Autonomous Surgeon (Signature Edition) - Applications",
  "Agricultural Robots: Farming's Future (Signature Edition) - Applications",
  "Construction Robots: Building the Future (Signature Edition) - Applications",
  "Underwater Robots: Exploring the Deep (Signature Edition) - Applications",
  "Space Robots: Working Off-World (Signature Edition) - Applications",
  "Human-Robot Teaming (Signature Edition) - Interaction",
  "Robot Ethics: The Responsible Machine (Signature Edition) - Interaction",
  "Explainable Robots (Signature Edition) - AI",
  "Long-Term Autonomy: Robots That Persist (Signature Edition) - Systems",
  "Dexterous Manipulation: The Human Hand (Signature Edition) - Manipulation",
  "Field Robotics: The Unstructured World (Signature Edition) - Systems"
 ],
 "Advanced": [
  "Robot Consciousness: The Inner Life (Signature Edition) - Theory",
  "General-Purpose Robots (Signature Edition) - Systems",
  "Robot Economics: The Automation Question (Signature Edition) - Systems",
  "Evolutionary Robotics: Evolving Machines (Signature Edition) - AI",
  "Developmental Robotics: Growing Up Machine (Signature Edition) - AI",
  "Robot Language: Talking to Machines (Signature Edition) - Interaction",
  "Trust in Robots (Signature Edition) - Interaction",
  "Creative Robots (Signature Edition) - Theory",
  "Robot Rights: The Personhood Question (Signature Edition) - Theory",
  "The Future of Robotics: A Century Ahead (Signature Edition) - Theory",
  "The Robotics Singularity (Signature Edition) - Theory"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Robotics Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-robotics-solution-explorer",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-robotics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-robotics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
