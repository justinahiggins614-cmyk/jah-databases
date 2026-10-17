(function(){'use strict';
/* JAH The Force and Motion Basics Database generator — jahdb-force-motion-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FMOB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Force - Foundations",
  "Push and Pull: The Two Faces of Force - Foundations",
  "Position, Distance, and Displacement - Foundations",
  "Speed: Measuring How Fast - Foundations",
  "Direction: Giving Motion an Address - Foundations",
  "Velocity: Speed with Direction - Foundations",
  "Acceleration: Changing Velocity - Foundations",
  "Mass: The Measure of Matter - Foundations",
  "Weight: Gravity Acting on Mass - Foundations",
  "The Newton: The Unit of Force - Foundations",
  "Reading Force: Spring Scales and Force Meters - Foundations",
  "Balanced and Unbalanced Forces - Foundations"
 ],
 "Compounded": [
  "Net Force: The Vector Sum - Compounded",
  "Free-Body Diagrams - Compounded",
  "Newton First Law: Inertia - Compounded",
  "Newton Second Law: Force Equals Mass Times Acceleration - Compounded",
  "Newton Third Law: Action and Reaction - Compounded",
  "Gravity: The Universal Attraction - Compounded",
  "Friction: The Grip Between Surfaces - Compounded",
  "Static and Kinetic Friction - Compounded",
  "Air Resistance and Drag - Compounded",
  "Momentum: Mass in Motion - Compounded",
  "The Lever: Force at a Distance - Compounded",
  "The Inclined Plane: Trading Distance for Force - Compounded"
 ],
 "Advanced": [
  "The Wheel and Axle - Advanced",
  "The Pulley: Redirecting Force - Advanced",
  "The Wedge and the Screw: Inclined Planes in Disguise - Advanced",
  "Mechanical Advantage: The Machine Multiplier - Advanced",
  "Work: Force Through Distance - Advanced",
  "Energy: The Capacity to Do Work - Advanced",
  "Power: Work Over Time - Advanced",
  "Torque and Rotational Equilibrium - Advanced",
  "Projectile Motion: Two Motions at Once - Advanced",
  "Conservation of Momentum in Collisions - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Force Motion Study — "+safe+"\n"
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
    name:topic+' — force and motion basics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A force and motion basics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"force-motion-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-force-motion-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('force-motion-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
