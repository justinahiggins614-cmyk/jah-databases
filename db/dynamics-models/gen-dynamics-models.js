(function(){'use strict';
/* JAH Dynamics Models Database generator — jahdb-dynamics-models-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DM-";
var FIELDS=["rigid-body-dynamics","state-space-models","lagrangian-formulations","linearized-models","parameter-sets","contact-dynamics"];
var TOPICS={
 "rigid-body-dynamics": [
  "Differential-drive rover \u2014 Rigid-body dynamics",
  "Quadrotor \u2014 Rigid-body dynamics",
  "6-DOF articulated arm \u2014 Rigid-body dynamics",
  "Cart-pole \u2014 Rigid-body dynamics",
  "Biped single-support \u2014 Rigid-body dynamics",
  "Autonomous underwater vehicle \u2014 Rigid-body dynamics",
  "Car-like vehicle (bicycle model) \u2014 Rigid-body dynamics",
  "SCARA arm \u2014 Rigid-body dynamics",
  "Satellite with reaction wheels \u2014 Rigid-body dynamics",
  "Soft continuum segment \u2014 Rigid-body dynamics"
 ],
 "state-space-models": [
  "Differential-drive rover \u2014 State-space models",
  "Quadrotor \u2014 State-space models",
  "6-DOF articulated arm \u2014 State-space models",
  "Cart-pole \u2014 State-space models",
  "Biped single-support \u2014 State-space models",
  "Autonomous underwater vehicle \u2014 State-space models",
  "Car-like vehicle (bicycle model) \u2014 State-space models",
  "SCARA arm \u2014 State-space models",
  "Satellite with reaction wheels \u2014 State-space models",
  "Soft continuum segment \u2014 State-space models"
 ],
 "lagrangian-formulations": [
  "Differential-drive rover \u2014 Lagrangian formulations",
  "Quadrotor \u2014 Lagrangian formulations",
  "6-DOF articulated arm \u2014 Lagrangian formulations",
  "Cart-pole \u2014 Lagrangian formulations",
  "Biped single-support \u2014 Lagrangian formulations",
  "Autonomous underwater vehicle \u2014 Lagrangian formulations",
  "Car-like vehicle (bicycle model) \u2014 Lagrangian formulations",
  "SCARA arm \u2014 Lagrangian formulations",
  "Satellite with reaction wheels \u2014 Lagrangian formulations",
  "Soft continuum segment \u2014 Lagrangian formulations"
 ],
 "linearized-models": [
  "Differential-drive rover \u2014 Linearized models",
  "Quadrotor \u2014 Linearized models",
  "6-DOF articulated arm \u2014 Linearized models",
  "Cart-pole \u2014 Linearized models",
  "Biped single-support \u2014 Linearized models",
  "Autonomous underwater vehicle \u2014 Linearized models",
  "Car-like vehicle (bicycle model) \u2014 Linearized models",
  "SCARA arm \u2014 Linearized models",
  "Satellite with reaction wheels \u2014 Linearized models",
  "Soft continuum segment \u2014 Linearized models"
 ],
 "parameter-sets": [
  "Differential-drive rover \u2014 Parameter sets",
  "Quadrotor \u2014 Parameter sets",
  "6-DOF articulated arm \u2014 Parameter sets",
  "Cart-pole \u2014 Parameter sets",
  "Biped single-support \u2014 Parameter sets",
  "Autonomous underwater vehicle \u2014 Parameter sets",
  "Car-like vehicle (bicycle model) \u2014 Parameter sets",
  "SCARA arm \u2014 Parameter sets",
  "Satellite with reaction wheels \u2014 Parameter sets",
  "Soft continuum segment \u2014 Parameter sets"
 ],
 "contact-dynamics": [
  "Differential-drive rover \u2014 Contact dynamics",
  "Quadrotor \u2014 Contact dynamics",
  "6-DOF articulated arm \u2014 Contact dynamics",
  "Cart-pole \u2014 Contact dynamics",
  "Biped single-support \u2014 Contact dynamics",
  "Autonomous underwater vehicle \u2014 Contact dynamics",
  "Car-like vehicle (bicycle model) \u2014 Contact dynamics",
  "SCARA arm \u2014 Contact dynamics",
  "Satellite with reaction wheels \u2014 Contact dynamics",
  "Soft continuum segment \u2014 Contact dynamics"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Dynamics Model — "+safe+"\n"
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
    name:topic+' — dynamics model record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A dynamics model record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"dynamics-simulator",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-dynamics-models-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('dynamics-models',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
