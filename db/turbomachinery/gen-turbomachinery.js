(function(){'use strict';
/* JAH The Turbomachinery Database generator — jahdb-turbomachinery-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Turbomachinery Is: The Machines That Move Fluids Through Spinning Blades - Foundations",
  "The Fluid Mechanics Foundation: Pressure, Velocity, and the Duct - Foundations",
  "The Conservation Laws: Mass, Momentum, and Energy Across the Machine - Foundations",
  "The Euler Turbine Equation: The One Equation That Rules Every Rotor - Foundations",
  "Velocity Triangles: The Language Every Blade Speaks - Foundations",
  "Degree of Reaction: Splitting the Pressure Change Between Rotor and Stator - Foundations",
  "The Turbomachinery Family: Turbines, Compressors, Pumps, and Fans - Foundations",
  "Axial, Radial, and Mixed Flow: Three Geometries, One Physics - Foundations",
  "Dimensionless Performance: The Flow, Head, and Power Coefficients - Foundations",
  "Specific Speed and Specific Diameter: The Machine Selector's Compass - Foundations",
  "The Affinity Laws: How Speed Changes Everything, Predictably - Foundations",
  "Losses and Efficiency: Where the Energy Goes - Foundations"
 ],
 "Compounded": [
  "Steam Turbines: Impulse, Reaction, and the Rankine Workhorse - Compounded",
  "Gas Turbines: The Brayton Cycle Made of Metal - Compounded",
  "Wind Turbines: Harvesting the Sky Within the Betz Limit - Compounded",
  "Hydraulic Turbines: Pelton, Francis, and Kaplan by Head and Flow - Compounded",
  "Axial Compressors: Building Pressure Stage by Stage - Compounded",
  "Centrifugal Compressors: The Impeller, the Slip, and the Diffuser - Compounded",
  "Centrifugal and Axial Pumps: The Rotodynamic Workhorses - Compounded",
  "Positive Displacement Pumps: When Flow Must Be Forced, Not Flung - Compounded",
  "Fans and Blowers: Moving Air at Low Pressure Rise - Compounded",
  "Performance Maps: Reading the Compressor and Pump Chart - Compounded",
  "Blade Cascades and Airfoils: The Two-Dimensional Heart of the Blade - Compounded",
  "Cavitation: When Liquid Boils Inside the Pump - Compounded",
  "Net Positive Suction Head: The Guard Against Cavitation - Compounded"
 ],
 "Advanced": [
  "Surge and Stall: The Instability Twins of Compression - Advanced",
  "Rotordynamics: Critical Speeds and the Spinning Shaft - Advanced",
  "Bearings: Rolling, Fluid-Film, and Magnetic - Advanced",
  "Seals and Leakage Control: Labyrinths, Brushes, and Dry Gas Seals - Advanced",
  "Blade Cooling and High-Temperature Materials: Surviving the Furnace - Advanced",
  "Tip Clearance and Secondary Flows: The Efficiency Thieves - Advanced",
  "Multi-Stage Matching and Off-Design Operation - Advanced",
  "Variable Geometry: Inlet Guide Vanes and Variable Stators - Advanced",
  "Combined Cycles and Cogeneration: Squeezing Every Joule - Advanced",
  "Condition Monitoring and Failure Modes: Listening to the Machine - Advanced",
  "The Design Workflow: From Duty Point to Manufactured Blade - Advanced",
  "The Frontier: Hydrogen Turbines and Supercritical Carbon Dioxide - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Turbomachinery Study — "+safe+"\n"
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
    name:topic+' — turbomachinery record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A turbomachinery record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"turbomachinery-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-turbomachinery-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('turbomachinery',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
