(function(){'use strict';
/* JAH The Physics in Action Database generator — jahdb-db-physics-in-action-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PHIA-";
var FIELDS=["Motion & Forces","Energy & Matter","Waves & Modern"];
var TOPICS={
 "Motion & Forces": [
  "Inertia: The Body at Rest - Motion & Forces",
  "F=ma: Force Makes Acceleration - Motion & Forces",
  "Action-Reaction: Every Push Pushes Back - Motion & Forces",
  "Friction: Grip and Slip - Motion & Forces",
  "Gravity: The Constant Pull - Motion & Forces",
  "Momentum: Mass in Motion - Motion & Forces",
  "Circular Motion: Always Falling Inward - Motion & Forces",
  "Torque: The Twist That Turns - Motion & Forces",
  "Pressure: Force Over Area - Motion & Forces",
  "Buoyancy: Why Things Float - Motion & Forces",
  "Terminal Velocity: Falling's Speed Limit - Motion & Forces",
  "Springs: Hooke's Law - Motion & Forces"
 ],
 "Energy & Matter": [
  "Kinetic Energy: Motion's Currency - Energy & Matter",
  "Potential Energy: Stored Possibility - Energy & Matter",
  "Work: Force Through Distance - Energy & Matter",
  "Power: How Fast You Work - Energy & Matter",
  "Heat vs Temperature - Energy & Matter",
  "The Three Ways Heat Travels - Energy & Matter",
  "States of Matter: Energy Decides - Energy & Matter",
  "Density: Heavy for Its Size - Energy & Matter",
  "Electric Charge: Opposites Attract - Energy & Matter",
  "Circuits: Current Needs a Loop - Energy & Matter",
  "Magnetism: Invisible Grip - Energy & Matter",
  "Static Electricity: Shocks and Cling - Energy & Matter"
 ],
 "Waves & Modern": [
  "Light: Wave and Particle - Waves & Modern",
  "Sound: Pressure Waves - Waves & Modern",
  "Reflection and Refraction - Waves & Modern",
  "The Doppler Effect - Waves & Modern",
  "Resonance: Pushing at the Right Time - Waves & Modern",
  "Interference: Waves Adding Up - Waves & Modern",
  "Relativity: Time Is Flexible - Waves & Modern",
  "Quantum Weirdness: The Small Rules - Waves & Modern",
  "Entropy: Things Fall Apart - Waves & Modern",
  "Nuclear Energy: E=mc\u00b2 at Work - Waves & Modern"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Physics Action Study — "+safe+"\n"
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
    name:topic+' — physics lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A physics lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"physics-action-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-physics-in-action-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-physics-in-action',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
