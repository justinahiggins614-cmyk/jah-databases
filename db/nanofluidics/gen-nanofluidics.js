(function(){'use strict';
/* JAH The Nanofluidics Database generator — jahdb-nanofluidics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NFD-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Nanofluidics: Fluids in 1-to-100 Nanometre Channels - Foundations",
  "The Nanoscale Advantage: Why Small Channels Behave Differently - Foundations",
  "Surface Charge and the Electrical Double Layer - Foundations",
  "The Debye Length: The Ruler of Nanofluidic Regimes - Foundations",
  "Slip Flow: When the No-Slip Rule Breaks - Foundations",
  "Making Nanochannels: How Nanometre Plumbing Is Built - Foundations",
  "Electro-osmosis: Pumping Liquid with Voltage - Foundations",
  "Electrophoresis: Sorting Charged Particles by Speed - Foundations"
 ],
 "Compounded": [
  "Overlapping Double Layers: How Nanochannels Choose Ions - Compounded",
  "Streaming Potential: Making Electricity from Pressure - Compounded",
  "Surface Conductance: The Extra Current Along the Walls - Compounded",
  "Ion Concentration Polarization: Depletion Zones on Demand - Compounded",
  "Nanofluidic Diodes: One-Way Streets for Ions - Compounded",
  "Osmotic Power: Electricity from Salt Gradients - Compounded",
  "Electrokinetic Energy Conversion: Efficiency and Limits - Compounded",
  "Nanopore Sensing: Reading Single Molecules by Resistance - Compounded",
  "DNA Through a Nanopore: Reading the Code of Life - Compounded",
  "The Nanofluidic Transistor: Gating Ions with Voltage - Compounded",
  "Nanofluidic Memristors: Memory Made of Ions - Compounded",
  "Desalination and Nanofluidic Membranes: Fresh Water from Salt - Compounded"
 ],
 "Advanced": [
  "Molecular Dynamics of Confined Water: What Simulations Reveal - Advanced",
  "Carbon Nanotube Membranes: Ultrafast Water Highways - Advanced",
  "Entrance and Access Resistance: The Forgotten Half of Nanopores - Advanced",
  "Pressure-Driven Flow: Hydraulic Resistance at the Nanoscale - Advanced",
  "Diffusio-osmosis: Flow from Salt Gradients - Advanced",
  "Steric Exclusion and Molecular Sieving: Sorting by Size - Advanced",
  "Nanofluidic Circuits: Resistors, Capacitors, and Ionic Logic - Advanced",
  "Angstrom Slits and 2D Nanofluidics: Plumbing One Atom High - Advanced",
  "Lab-on-a-Chip: The Nanofluidic Diagnostic Bench - Advanced",
  "Nanofluidic Biosensors: Counting Molecules Toward the Limit - Advanced",
  "Fouling and Longevity: Keeping Nanochannels Open - Advanced",
  "Design Rules: Building a Nanofluidic Device That Works - Advanced",
  "Safety and Standards in Nanofluidics: Handling the Very Small - Advanced",
  "The Future of Nanofluidics: Where the Field Is Going - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nanofluidics Study — "+safe+"\n"
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
    name:topic+' — nanofluidics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A nanofluidics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"nanofluidics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-nanofluidics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nanofluidics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
