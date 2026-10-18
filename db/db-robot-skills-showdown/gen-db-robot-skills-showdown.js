(function(){'use strict';
/* JAH The Robot Skills Showdown Database generator — jahdb-db-robot-skills-showdown-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RBSS-";
var FIELDS=["Walking Robots","Working Robots","Flying & Specialty"];
var TOPICS={
 "Walking Robots": [
  "Humanoid vs Quadruped: Legged Robots - Walking Robots",
  "Atlas vs Spot: Boston Dynamics Duel - Walking Robots",
  "Biped vs Wheeled: Indoor Robots - Walking Robots",
  "Exoskeleton vs Prosthetic: Wearable Robots - Walking Robots",
  "Snake Robot vs Crawler: Confined Spaces - Walking Robots",
  "Jumping Robot vs Flying: Getting Up - Walking Robots",
  "Ball Bot vs Biped: Balance - Walking Robots",
  "Soft Robot vs Rigid: Bodies - Walking Robots",
  "Swarm vs Single: Many vs One - Walking Robots",
  "Climbing Robot vs Drone: Walls - Walking Robots",
  "Running Robot vs Cheetah Bot: Speed - Walking Robots"
 ],
 "Working Robots": [
  "Industrial Arm vs Collaborative Arm: Factory - Working Robots",
  "Gripper: Suction vs Fingers - Working Robots",
  "Welding Robot vs Human Welder - Working Robots",
  "Ag Robot vs Tractor: Farming - Working Robots",
  "Surgical Robot vs Steady Hand - Working Robots",
  "Warehouse Robot vs Forklift - Working Robots",
  "Painting Robot vs Painter - Working Robots",
  "3D Printer vs CNC: Making - Working Robots",
  "Barista Robot vs Barista - Working Robots",
  "Delivery Robot vs Courier - Working Robots"
 ],
 "Flying & Specialty": [
  "Drone vs Helicopter: Inspection - Flying & Specialty",
  "Fixed-Wing vs Quadcopter: Drones - Flying & Specialty",
  "Underwater ROV vs Diver - Flying & Specialty",
  "Space Rover vs Astronaut - Flying & Specialty",
  "Firefighting Drone vs Fire Truck - Flying & Specialty",
  "Pollination Drone vs Bee - Flying & Specialty",
  "Window Washer Robot vs Human - Flying & Specialty",
  "Lawn Robot vs Mower - Flying & Specialty",
  "Security Robot vs Guard - Flying & Specialty",
  "Companion Robot vs Pet - Flying & Specialty",
  "Bartender Robot vs Bartender - Flying & Specialty",
  "Dishwasher Robot vs Human: Kitchen - Flying & Specialty",
  "Exosuit vs Forklift: Lifting - Flying & Specialty"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Robot Skills Study — "+safe+"\n"
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
    name:topic+' — robot comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A robot comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"robot-skills-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-robot-skills-showdown-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-robot-skills-showdown',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
