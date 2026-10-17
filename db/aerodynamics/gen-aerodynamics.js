(function(){'use strict';
/* JAH The Aerodynamics Database generator — jahdb-aerodynamics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AER-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Aerodynamics Is: The Study of Air in Motion - Foundations",
  "Air as a Fluid: Density, Pressure, and Viscosity - Foundations",
  "The Four Forces: Lift, Weight, Thrust, and Drag - Foundations",
  "Continuity and Bernoulli: Why Speed Changes Pressure - Foundations",
  "The Reynolds Number: When Smooth Flow Turns Turbulent - Foundations",
  "How Wings Make Lift: Airfoils, Angle of Attack, and Circulation - Foundations",
  "Drag, Decomposed: Friction, Pressure, and Induced Drag - Foundations",
  "The Boundary Layer: Where Air Meets the Wing - Foundations"
 ],
 "Compounded": [
  "Airfoil Geometry: Camber, Thickness, and the Mean Line - Compounded",
  "Compressible Flow: The Mach Number and the Speed of Sound - Compounded",
  "Ground Effect: Free Lift Near the Surface - Compounded",
  "Airfoil Performance: Lift Curves, Stall, and Drag Polars - Compounded",
  "Induced Drag and Aspect Ratio: The Cost of Making Lift - Compounded",
  "Normal Shock Waves: Supersonic to Subsonic in One Jump - Compounded",
  "Oblique Shocks and Expansion Fans: Turning Supersonic Flow - Compounded",
  "The Prandtl-Glauert Correction: Compressibility at Subsonic Speeds - Compounded",
  "Sweep and the Transonic Problem: Delaying the Shock - Compounded",
  "Stall and High-Lift Devices: Flaps, Slats, and the Critical Angle - Compounded",
  "Wind Shear and Wake Turbulence: Hazards in the Air - Compounded"
 ],
 "Advanced": [
  "Supersonic Airfoil Theory: Thin Wings and Wave Drag - Advanced",
  "The Area Rule: Sculpting Wave Drag Away - Advanced",
  "Hypersonic Flow: Thin Shocks, Hot Gas, Real Chemistry - Advanced",
  "Aircraft Stability: The Weathervane and the Neutral Point - Advanced",
  "Control Surfaces: Pitch, Roll, and Yaw Authority - Advanced",
  "Boundary-Layer Control: Suction, Blowing, and Laminar Wings - Advanced",
  "Helicopter Rotor Aerodynamics: Hover and Forward Flight - Advanced",
  "Wind Tunnel Testing: Similitude, Blockage, and Corrections - Advanced",
  "CFD: Solving the Navier-Stokes Equations on a Grid - Advanced",
  "Aeroelasticity: Flutter, Divergence, and Control Reversal - Advanced",
  "Propulsion Integration: Inlets, Nozzles, and Afterbodies - Advanced",
  "Sonic Boom: The N-Wave and Its Reach - Advanced",
  "Design Integration: The Lift-to-Drag Balance of the Whole Airplane - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Aerodynamics Study — "+safe+"\n"
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
    name:topic+' — aerodynamics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A aerodynamics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"aerodynamics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-aerodynamics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('aerodynamics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
