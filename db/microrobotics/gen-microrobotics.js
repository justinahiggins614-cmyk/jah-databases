(function(){'use strict';
/* JAH The Microrobotics Database generator — jahdb-microrobotics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MRO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Microrobotics: Robots Smaller Than a Grain of Sand - Foundations",
  "The Micro-Scale Map: From Millibots to Nanobots - Foundations",
  "Scaling Laws at Small Sizes: Why Surface Beats Volume - Foundations",
  "MEMS: The Micro-Electro-Mechanical Body of the Microrobot - Foundations",
  "Microfabrication: Lithography, Etching, and Building Tiny Machines - Foundations",
  "Materials at the Micro-Scale: Silicon, Polymers, and Smart Films - Foundations"
 ],
 "Compounded": [
  "Electrostatic Actuation: Comb Drives and the Pull-In Limit - Compounded",
  "Piezoelectric Actuation: Bending Tiny Muscles with Voltage - Compounded",
  "Thermal Actuation: Heat as a Micro-Muscle - Compounded",
  "Magnetic Actuation: Steering Untethered Microrobots with Fields - Compounded",
  "Micro-Sensors: How Microrobots Feel the World - Compounded",
  "Powering Micro-Robots: Batteries, Capacitors, and the Energy Problem - Compounded",
  "Wireless Power and Communication: Feeding Robots Without Wires - Compounded",
  "Micro-Locomotion: Legs, Crawlers, and Swimming at Low Reynolds Number - Compounded",
  "Microfluidic Integration: Robots That Swim in Labs-on-Chips - Compounded",
  "Micro-Grippers and End Effectors: Hands for the Invisible - Compounded",
  "Micro-Assembly: Building Things One Micron at a Time - Compounded",
  "Control at the Micro-Scale: Steering Without Seeing Clearly - Compounded",
  "Swarm Microrobots: Many Tiny Robots, One Big Job - Compounded"
 ],
 "Advanced": [
  "Compliant Mechanisms: Hinges Made of Bending, Not Pins - Advanced",
  "Chemical Propulsion: Catalytic Motors and Janus Particles - Advanced",
  "Biohybrid Microrobots: Living Engines in Synthetic Bodies - Advanced",
  "Optical Control: Tweezers and Light-Driven Microrobots - Advanced",
  "Medical Microrobots: Drug Delivery Inside the Body - Advanced",
  "Microsurgery Tools: Operating at the Cellular Scale - Advanced",
  "Insect-Scale Flight: The Hardest Actuation Problem - Advanced",
  "Inspection Microrobots: Pipelines, Engines, and the Environment - Advanced",
  "Self-Assembly and Micro-Origami: Robots That Fold Themselves - Advanced",
  "Reliability at the Micro-Scale: Stiction, Wear, and Packaging - Advanced",
  "Testing and Characterization: Measuring the Invisible - Advanced",
  "Energy Scaling Limits: Why Small Robots Can't Carry Big Batteries - Advanced",
  "Economics and Roadmap: From Lab Curiosity to Micro-Robot Industry - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Microrobotics Study — "+safe+"\n"
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
    name:topic+' — microrobotics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A microrobotics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"microrobotics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-microrobotics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('microrobotics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
