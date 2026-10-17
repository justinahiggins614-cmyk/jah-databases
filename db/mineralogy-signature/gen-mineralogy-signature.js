(function(){'use strict';
/* JAH The Mineralogy Signature Database generator — jahdb-mineralogy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Mineralogy: The Science of Earth's Crystalline Materials (Signature Edition) \u2014 Foundations",
  "The Five Tests: What Counts as a Mineral (Signature Edition) \u2014 Foundations",
  "Crystal Systems: The Seven Symmetry Systems of Mineralogy (Signature Edition) \u2014 Foundations",
  "Mineral Habit: The Shapes Crystals Take (Signature Edition) \u2014 Foundations",
  "The Mohs Hardness Scale: Scratch Testing (Signature Edition) \u2014 Foundations",
  "Cleavage, Fracture, and Parting: How Minerals Break (Signature Edition) \u2014 Foundations",
  "Luster and Streak: How Minerals Handle Light (Signature Edition) \u2014 Foundations",
  "Color in Minerals: Causes and Traps (Signature Edition) \u2014 Foundations",
  "Specific Gravity: Weighing Minerals in Water (Signature Edition) \u2014 Foundations",
  "The Dana Classification: Eight Chemical Classes (Signature Edition) \u2014 Foundations",
  "The Nickel-Strunz Classification: Structure-First Classes (Signature Edition) \u2014 Foundations",
  "Reading Mineral Formulas: From Symbols to Composition (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Symmetry Elements and the 32 Point Groups (Signature Edition) \u2014 Compounded",
  "Crystal Lattices: The 14 Bravais Lattices (Signature Edition) \u2014 Compounded",
  "Silicate Structures: The Six Tetrahedral Families (Signature Edition) \u2014 Compounded",
  "Rock-Forming Minerals: The Minerals That Build Continents (Signature Edition) \u2014 Compounded",
  "Ore Minerals: Where Metals Come From (Signature Edition) \u2014 Compounded",
  "Igneous Crystallization: Bowen's Reaction Series (Signature Edition) \u2014 Compounded",
  "Sedimentary and Metamorphic Mineral Formation (Signature Edition) \u2014 Compounded",
  "Hydrothermal Veins and Pegmatites (Signature Edition) \u2014 Compounded",
  "Optical Mineralogy: The Polarizing Microscope (Signature Edition) \u2014 Compounded",
  "Refractive Index and Birefringence (Signature Edition) \u2014 Compounded",
  "Pleochroism and Interference Colors (Signature Edition) \u2014 Compounded",
  "Gemstones: Properties, Cutting, and Value (Signature Edition) \u2014 Compounded",
  "Hand-Sample Identification: The Field Workflow (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "X-Ray Diffraction: Bragg's Law and the Unit Cell (Signature Edition) \u2014 Advanced",
  "Crystal Structure Determination (Signature Edition) \u2014 Advanced",
  "Solid Solution and Polymorphism (Signature Edition) \u2014 Advanced",
  "Thermodynamics of Mineral Stability (Signature Edition) \u2014 Advanced",
  "Phase Diagrams: Reading Mineral Stability Fields (Signature Edition) \u2014 Advanced",
  "Ionic Substitution: Goldschmidt's Rules (Signature Edition) \u2014 Advanced",
  "Gemstone Treatments and Synthetics Detection (Signature Edition) \u2014 Advanced",
  "The IMA and the Master List of Minerals (Signature Edition) \u2014 Advanced",
  "Describing a New Mineral: From Discovery to Approval (Signature Edition) \u2014 Advanced",
  "Environmental Mineralogy: Acid Drainage and Remediation (Signature Edition) \u2014 Advanced",
  "Building a Systematic Mineral Collection (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mineralogy Study — "+safe+"\n"
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
    name:topic+' — mineralogy record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mineralogy record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"mineralogy-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-mineralogy-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mineralogy-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
