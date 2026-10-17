(function(){'use strict';
/* JAH The Nanofluidics Signature Database generator — jahdb-nanofluidics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NFS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Nanofluidics: Fluids in 1-to-100 Nanometre Channels (Signature Edition) - Foundations",
  "The Nanoscale Advantage: Why Small Channels Behave Differently (Signature Edition) - Foundations",
  "Surface Charge and the Electrical Double Layer (Signature Edition) - Foundations",
  "The Debye Length: The Ruler of Nanofluidic Regimes (Signature Edition) - Foundations",
  "Slip Flow: When the No-Slip Rule Breaks (Signature Edition) - Foundations",
  "Making Nanochannels: How Nanometre Plumbing Is Built (Signature Edition) - Foundations",
  "Electro-osmosis: Pumping Liquid with Voltage (Signature Edition) - Foundations",
  "Electrophoresis: Sorting Charged Particles by Speed (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Overlapping Double Layers: How Nanochannels Choose Ions (Signature Edition) - Compounded",
  "Streaming Potential: Making Electricity from Pressure (Signature Edition) - Compounded",
  "Surface Conductance: The Extra Current Along the Walls (Signature Edition) - Compounded",
  "Ion Concentration Polarization: Depletion Zones on Demand (Signature Edition) - Compounded",
  "Nanofluidic Diodes: One-Way Streets for Ions (Signature Edition) - Compounded",
  "Osmotic Power: Electricity from Salt Gradients (Signature Edition) - Compounded",
  "Electrokinetic Energy Conversion: Efficiency and Limits (Signature Edition) - Compounded",
  "Nanopore Sensing: Reading Single Molecules by Resistance (Signature Edition) - Compounded",
  "DNA Through a Nanopore: Reading the Code of Life (Signature Edition) - Compounded",
  "The Nanofluidic Transistor: Gating Ions with Voltage (Signature Edition) - Compounded",
  "Nanofluidic Memristors: Memory Made of Ions (Signature Edition) - Compounded",
  "Desalination and Nanofluidic Membranes: Fresh Water from Salt (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Molecular Dynamics of Confined Water: What Simulations Reveal (Signature Edition) - Advanced",
  "Carbon Nanotube Membranes: Ultrafast Water Highways (Signature Edition) - Advanced",
  "Entrance and Access Resistance: The Forgotten Half of Nanopores (Signature Edition) - Advanced",
  "Pressure-Driven Flow: Hydraulic Resistance at the Nanoscale (Signature Edition) - Advanced",
  "Diffusio-osmosis: Flow from Salt Gradients (Signature Edition) - Advanced",
  "Steric Exclusion and Molecular Sieving: Sorting by Size (Signature Edition) - Advanced",
  "Nanofluidic Circuits: Resistors, Capacitors, and Ionic Logic (Signature Edition) - Advanced",
  "Angstrom Slits and 2D Nanofluidics: Plumbing One Atom High (Signature Edition) - Advanced",
  "Lab-on-a-Chip: The Nanofluidic Diagnostic Bench (Signature Edition) - Advanced",
  "Nanofluidic Biosensors: Counting Molecules Toward the Limit (Signature Edition) - Advanced",
  "Fouling and Longevity: Keeping Nanochannels Open (Signature Edition) - Advanced",
  "Design Rules: Building a Nanofluidic Device That Works (Signature Edition) - Advanced",
  "Safety and Standards in Nanofluidics: Handling the Very Small (Signature Edition) - Advanced",
  "The Future of Nanofluidics: Where the Field Is Going (Signature Edition) - Advanced"
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
var gen={version:'jahdb-nanofluidics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nanofluidics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
