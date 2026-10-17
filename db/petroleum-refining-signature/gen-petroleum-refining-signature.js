(function(){'use strict';
/* JAH The Petroleum Refining Signature Database generator — jahdb-petroleum-refining-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Petroleum Refining Is: From Black Crude to Clear Products (Signature Edition) - Foundations",
  "Crude Oil Composition: The Hydrocarbon Family (Signature Edition) - Foundations",
  "Reading a Crude Assay: An Oil's DNA (Signature Edition) - Foundations",
  "API Gravity, Density, and Viscosity: The First Measurements (Signature Edition) - Foundations",
  "The Modern Refinery: Units, Flow, and Block Diagrams (Signature Edition) - Foundations",
  "Crude Desalting: The First Line of Defense (Signature Edition) - Foundations",
  "Atmospheric Distillation: The Crude Distillation Unit (Signature Edition) - Foundations",
  "Vacuum Distillation: The Second Cut (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Light Ends Recovery: LPG, Fuel Gas, and the Gas Plant (Signature Edition) - Compounded",
  "Thermal Cracking and Visbreaking: Heat as a Hammer (Signature Edition) - Compounded",
  "Fluid Catalytic Cracking: The Beating Heart of the Refinery (Signature Edition) - Compounded",
  "Hydrocracking: Premium Barrels from Heavy Feed (Signature Edition) - Compounded",
  "Catalytic Reforming: Octane and Hydrogen from Naphtha (Signature Edition) - Compounded",
  "Alkylation: The Finest Gasoline Molecule (Signature Edition) - Compounded",
  "Isomerization: Upgrading Light Straight-Run Naphtha (Signature Edition) - Compounded",
  "Delayed Coking: Cooking the Bottom of the Barrel (Signature Edition) - Compounded",
  "Hydrotreating: Desulfurizing the Streams (Signature Edition) - Compounded",
  "The Refinery Hydrogen Network: Balancing Producers and Consumers (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Amine Treating and Sulfur Recovery: Taming Hydrogen Sulfide (Signature Edition) - Advanced",
  "Gasoline Blending: The Octane Recipe (Signature Edition) - Advanced",
  "Diesel and Jet Fuel: Specifications That Matter (Signature Edition) - Advanced",
  "Lubricants and Base Oils: The Quiet Products (Signature Edition) - Advanced",
  "Asphalt, Coke, and Heavy Products: Nothing Wasted (Signature Edition) - Advanced",
  "Petrochemical Integration: Where Refinery Meets Chemical Plant (Signature Edition) - Advanced",
  "Refinery Safety: HAZOP, Relief, and Process Safety Management (Signature Edition) - Advanced",
  "Emissions and Environmental Controls: The Clean Refinery (Signature Edition) - Advanced",
  "Refinery Economics: Margins, Complexity, and Linear Programming (Signature Edition) - Advanced",
  "Product Quality Testing: Proving the Barrel (Signature Edition) - Advanced",
  "Corrosion and Materials: The Refinery's Slow Enemy (Signature Edition) - Advanced",
  "Energy Integration: Furnaces, Exchangers, and Pinch (Signature Edition) - Advanced",
  "Wastewater Treatment: Cleaning the Refinery's Water (Signature Edition) - Advanced",
  "Catalysts: The Refinery's Invisible Workforce (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Petroleum Refining Study — "+safe+"\n"
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
    name:topic+' — petroleum refining record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A petroleum refining record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"petroleum-refining-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-petroleum-refining-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('petroleum-refining-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
