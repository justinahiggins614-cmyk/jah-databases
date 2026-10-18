(function(){'use strict';
/* JAH The Physics in Action Signature Database generator — jahdb-db-physics-in-action-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PHIAS-";
var FIELDS=["Motion & Forces","Energy & Matter","Waves & Modern"];
var TOPICS={
 "Motion & Forces": [
  "Inertia: The Body at Rest (Signature Edition) - Motion & Forces",
  "F=ma: Force Makes Acceleration (Signature Edition) - Motion & Forces",
  "Action-Reaction: Every Push Pushes Back (Signature Edition) - Motion & Forces",
  "Friction: Grip and Slip (Signature Edition) - Motion & Forces",
  "Gravity: The Constant Pull (Signature Edition) - Motion & Forces",
  "Momentum: Mass in Motion (Signature Edition) - Motion & Forces",
  "Circular Motion: Always Falling Inward (Signature Edition) - Motion & Forces",
  "Torque: The Twist That Turns (Signature Edition) - Motion & Forces",
  "Pressure: Force Over Area (Signature Edition) - Motion & Forces",
  "Buoyancy: Why Things Float (Signature Edition) - Motion & Forces",
  "Terminal Velocity: Falling's Speed Limit (Signature Edition) - Motion & Forces",
  "Springs: Hooke's Law (Signature Edition) - Motion & Forces"
 ],
 "Energy & Matter": [
  "Kinetic Energy: Motion's Currency (Signature Edition) - Energy & Matter",
  "Potential Energy: Stored Possibility (Signature Edition) - Energy & Matter",
  "Work: Force Through Distance (Signature Edition) - Energy & Matter",
  "Power: How Fast You Work (Signature Edition) - Energy & Matter",
  "Heat vs Temperature (Signature Edition) - Energy & Matter",
  "The Three Ways Heat Travels (Signature Edition) - Energy & Matter",
  "States of Matter: Energy Decides (Signature Edition) - Energy & Matter",
  "Density: Heavy for Its Size (Signature Edition) - Energy & Matter",
  "Electric Charge: Opposites Attract (Signature Edition) - Energy & Matter",
  "Circuits: Current Needs a Loop (Signature Edition) - Energy & Matter",
  "Magnetism: Invisible Grip (Signature Edition) - Energy & Matter",
  "Static Electricity: Shocks and Cling (Signature Edition) - Energy & Matter"
 ],
 "Waves & Modern": [
  "Light: Wave and Particle (Signature Edition) - Waves & Modern",
  "Sound: Pressure Waves (Signature Edition) - Waves & Modern",
  "Reflection and Refraction (Signature Edition) - Waves & Modern",
  "The Doppler Effect (Signature Edition) - Waves & Modern",
  "Resonance: Pushing at the Right Time (Signature Edition) - Waves & Modern",
  "Interference: Waves Adding Up (Signature Edition) - Waves & Modern",
  "Relativity: Time Is Flexible (Signature Edition) - Waves & Modern",
  "Quantum Weirdness: The Small Rules (Signature Edition) - Waves & Modern",
  "Entropy: Things Fall Apart (Signature Edition) - Waves & Modern",
  "Nuclear Energy: E=mc\u00b2 at Work (Signature Edition) - Waves & Modern"
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
var gen={version:'jahdb-db-physics-in-action-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-physics-in-action-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
