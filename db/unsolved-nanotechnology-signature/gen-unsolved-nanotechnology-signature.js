(function(){'use strict';
/* JAH The Unsolved Nanotechnology Signature Database generator — jahdb-unsolved-nanotechnology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USNAS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Nanomanufacturing: Building at Scale (Signature Edition) - Fabrication",
  "Nanotoxicology: Are Nanomaterials Safe? (Signature Edition) - Safety",
  "Molecular Assemblers: Drexler's Dream (Signature Edition) - Fabrication",
  "Nanorobotics: Machines at the Nanoscale (Signature Edition) - Devices",
  "Nanoelectronics: Beyond Silicon (Signature Edition) - Devices",
  "Nanomedicine: The Promise and the Delivery (Signature Edition) - Devices",
  "Quantum Dots: The Tunable Nanocrystals (Signature Edition) - Devices",
  "Nanocomposites: The Promise of the Filler (Signature Edition) - Materials",
  "Nanosensors: The Ultimate Detectors (Signature Edition) - Devices",
  "DNA Origami: Programming Matter (Signature Edition) - Fabrication",
  "Plasmonics: Light at the Nanoscale (Signature Edition) - Devices"
 ],
 "Compounded": [
  "Nanophotonics: Controlling Light (Signature Edition) - Devices",
  "Nanofluidics: Fluids at the Nanoscale (Signature Edition) - Devices",
  "Nanocatalysis: Catalysts at the Nanoscale (Signature Edition) - Materials",
  "Nanodiamonds: The Quantum Sensors (Signature Edition) - Devices",
  "Carbon Nanotubes: The Unfulfilled Promise (Signature Edition) - Materials",
  "Graphene Applications: The Wonder Material's Wait (Signature Edition) - Materials",
  "Nano-Energy: Harvesting at the Nanoscale (Signature Edition) - Devices",
  "Heat at the Nanoscale (Signature Edition) - Theory",
  "Molecular Electronics: The Single-Molecule Circuit (Signature Edition) - Devices",
  "Nanoporous Materials: The Designed Void (Signature Edition) - Materials",
  "Directed Nanoscale Assembly (Signature Edition) - Fabrication",
  "The Nano-Bio Interface (Signature Edition) - Safety"
 ],
 "Advanced": [
  "Nanolubrication: Friction at the Nanoscale (Signature Edition) - Theory",
  "Nanometrology: Measuring the Nanoworld (Signature Edition) - Theory",
  "Nano-Architected Materials (Signature Edition) - Materials",
  "Nanomaterials in the Environment (Signature Edition) - Safety",
  "Nanoscale Quantum Devices (Signature Edition) - Devices",
  "A Theory of the Nanoscale (Signature Edition) - Theory",
  "The Future of Nanotechnology: A Century Ahead (Signature Edition) - Theory",
  "The Grey-Goo Question (Signature Edition) - Safety",
  "Nanotechnology and Mind (Signature Edition) - Theory",
  "Governing Nanotechnology (Signature Edition) - Safety",
  "The Nanotech Singularity (Signature Edition) - Theory"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Nanotechnology Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-nanotechnology-solution-explorer",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-nanotechnology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-nanotechnology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
