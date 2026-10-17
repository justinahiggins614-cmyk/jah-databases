(function(){'use strict';
/* JAH The Petrology Signature Database generator — jahdb-petrology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PSG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Petrology: The Science of Rocks (Signature Edition) \u2014 Foundations",
  "The Rock Cycle: How Rocks Transform Into Each Other (Signature Edition) \u2014 Foundations",
  "Igneous Rocks: Born from Molten Magma (Signature Edition) \u2014 Foundations",
  "Sedimentary Rocks: Layers of Earth's History (Signature Edition) \u2014 Foundations",
  "Metamorphic Rocks: Transformed by Heat and Pressure (Signature Edition) \u2014 Foundations",
  "Magma and Lava: The Molten Source (Signature Edition) \u2014 Foundations",
  "The Rock-Forming Minerals: Petrology's Building Blocks (Signature Edition) \u2014 Foundations",
  "Intrusive vs. Extrusive: Where Magma Cools Decides Everything (Signature Edition) \u2014 Foundations",
  "Reading Igneous Textures: What Grain Patterns Reveal (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Bowen's Reaction Series: The Order of Crystallization (Signature Edition) \u2014 Compounded",
  "IUGS Classification: The Official Naming of Igneous Rocks (Signature Edition) \u2014 Compounded",
  "The QAP Diagram: Classifying Plutonic Rocks by Their Minerals (Signature Edition) \u2014 Compounded",
  "TAS Classification: Naming Volcanic Rocks by Chemistry (Signature Edition) \u2014 Compounded",
  "Magma Genesis: How Magmas Are Born (Signature Edition) \u2014 Compounded",
  "Partial Melting and Fractional Crystallization: The Twin Engines (Signature Edition) \u2014 Compounded",
  "Magma Differentiation: How One Magma Makes Many Rocks (Signature Edition) \u2014 Compounded",
  "Volcanic Textures: Reading Eruptions in Stone (Signature Edition) \u2014 Compounded",
  "Sedimentary Provenance: Reading the Source Rocks in Sand (Signature Edition) \u2014 Compounded",
  "Sedimentary Structures: Reading Ancient Environments (Signature Edition) \u2014 Compounded",
  "Diagenesis: From Loose Sediment to Solid Rock (Signature Edition) \u2014 Compounded",
  "Carbonate Petrology: Limestones, Dolostones, and Reefs (Signature Edition) \u2014 Compounded",
  "Metamorphic Grade and Index Minerals: Reading Temperature in Stone (Signature Edition) \u2014 Compounded",
  "Metamorphic Facies: Pressure-Temperature Fingerprints (Signature Edition) \u2014 Compounded",
  "Metamorphic Textures: Foliation, Porphyroblasts, and Deformation (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Phase Equilibria: Reading Binary Phase Diagrams (Signature Edition) \u2014 Advanced",
  "The Lever Rule: Quantifying Phase Diagrams (Signature Edition) \u2014 Advanced",
  "Ternary Phase Diagrams: Three-Component Crystallization (Signature Edition) \u2014 Advanced",
  "Geothermobarometry: Thermometers and Barometers in Minerals (Signature Edition) \u2014 Advanced",
  "Petrographic Microscopy: Reading Thin Sections (Signature Edition) \u2014 Advanced",
  "Optical Properties in Thin Section: Birefringence and Extinction (Signature Edition) \u2014 Advanced",
  "Igneous Geochemistry: Trace Elements and Isotopes (Signature Edition) \u2014 Advanced",
  "Ophiolites and Mantle Petrology: Slices of Ocean Floor on Land (Signature Edition) \u2014 Advanced",
  "Granite Petrogenesis: The Granite Problem (Signature Edition) \u2014 Advanced",
  "Metamorphic P-T-t Paths: Clockwise, Counterclockwise, and What They Mean (Signature Edition) \u2014 Advanced",
  "Experimental Petrology: Recreating Deep Earth in the Laboratory (Signature Edition) \u2014 Advanced",
  "Field Petrology: Mapping and Sampling Like a Petrologist (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Petrology Study — "+safe+"\n"
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
    name:topic+' — petrology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A petrology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"petrology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-petrology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('petrology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
