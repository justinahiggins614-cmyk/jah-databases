(function(){'use strict';
/* JAH The Unsolved Chemistry Signature Database generator — jahdb-unsolved-chemistry-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USCHS-";
var FIELDS=["Approachable","Deep","Frontier"];
var TOPICS={
 "Approachable": [
  "Why Does Hot Water Sometimes Freeze Faster Than Cold? (Signature Edition) - Approachable",
  "Why Does Water Behave So Strangely? (Signature Edition) - Approachable",
  "What Is a Molecule Smell Made Of? (Signature Edition) - Approachable",
  "How Do Proteins Fold Into Their Shapes? (Signature Edition) - Approachable",
  "Why Are Enzymes Such Spectacular Catalysts? (Signature Edition) - Approachable",
  "What Is the Hydrophobic Effect Really? (Signature Edition) - Approachable",
  "Why Is All of Life Chemistry One-Handed? (Signature Edition) - Approachable",
  "Where Did the Chemistry of Life Come From? (Signature Edition) - Approachable",
  "How Do Plants Split Water With Sunlight? (Signature Edition) - Approachable",
  "What Is a Glass: Liquid or Solid? (Signature Edition) - Approachable",
  "How Do Protons Hop Through Water? (Signature Edition) - Approachable",
  "What Happens at the Surface of Water? (Signature Edition) - Approachable"
 ],
 "Deep": [
  "How Do Crystals Begin? (Signature Edition) - Deep",
  "Can We Predict Which Crystals a Molecule Will Form? (Signature Edition) - Deep",
  "What Is Happening Inside a Battery as It Charges? (Signature Edition) - Deep",
  "How Does Rust Really Eat Metal? (Signature Edition) - Deep",
  "How Do We Destroy Forever Chemicals? (Signature Edition) - Deep",
  "How Do We Pull Nitrogen From the Air at Room Temperature? (Signature Edition) - Deep",
  "How Do We Turn Carbon Dioxide Back Into Fuel? (Signature Edition) - Deep",
  "How Do We Store Hydrogen Safely and Densely? (Signature Edition) - Deep",
  "How Do Catalysts Really Work on Surfaces? (Signature Edition) - Deep",
  "How Do We Design a Catalyst From Scratch? (Signature Edition) - Deep",
  "How Do We Separate Isotopes Cheaply? (Signature Edition) - Deep"
 ],
 "Frontier": [
  "How Do Molecular Machines Move on Purpose? (Signature Edition) - Frontier",
  "How Does Charge Move Through Plastic Electronics? (Signature Edition) - Frontier",
  "Can We Compute With Molecules? (Signature Edition) - Frontier",
  "How Many Stable Molecules Are Possible? (Signature Edition) - Frontier",
  "How Do We Model Molecules With Unpaired Electrons? (Signature Edition) - Frontier",
  "What Is the Chemistry of Interstellar Space? (Signature Edition) - Frontier",
  "What Is Metallic Hydrogen, and Can It Survive at Room Temperature? (Signature Edition) - Frontier",
  "What Makes High-Temperature Superconductors Superconduct? (Signature Edition) - Frontier",
  "How Do We Design Materials Backwards From Properties? (Signature Edition) - Frontier",
  "Why Do Heavy Elements Break the Periodic Table Patterns? (Signature Edition) - Frontier",
  "Can We Create Artificial Enzymes as Good as Natures? (Signature Edition) - Frontier"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Chemistry Study — "+safe+"\n"
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
    demo:{kind:"unsolved-chemistry-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-chemistry-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-chemistry-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
