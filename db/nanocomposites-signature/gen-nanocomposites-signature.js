(function(){'use strict';
/* JAH The Nanocomposites Signature Database generator — jahdb-nanocomposites-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NCS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Nanocomposites: Plastics and Metals Reinforced at the Nanoscale (Signature Edition) - Foundations",
  "The Nanoscale Advantage: Why a Nanometre of Filler Changes Everything (Signature Edition) - Foundations",
  "Zero, One, Two Dimensions: The Filler Zoo (Particles, Tubes, Platelets) (Signature Edition) - Foundations",
  "The Host Matters: Polymer, Metal, and Ceramic Matrices (Signature Edition) - Foundations",
  "The Rule of Mixtures: Your First Property Estimate (Signature Edition) - Foundations",
  "Weight vs Volume: Filler Fractions and Density Bookkeeping (Signature Edition) - Foundations",
  "Dispersion: The Difference Between a Composite and a Clump (Signature Edition) - Foundations",
  "The Interface: Where the Composite Is Really Made (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Halpin-Tsai: Stiffness Math for Real Composites (Signature Edition) - Compounded",
  "Aspect Ratio: Why Long and Thin Wins (Signature Edition) - Compounded",
  "Percolation: When Conductivity Switches On (Signature Edition) - Compounded",
  "Carbon Nanotubes in Polymers: Strength from a Straw (Signature Edition) - Compounded",
  "Graphene Fillers: A Single Atomic Sheet as Reinforcement (Signature Edition) - Compounded",
  "Clay Nanocomposites: The First Commercial Nanocomposite (Signature Edition) - Compounded",
  "Nanocellulose Composites: Strength from Wood at the Nanoscale (Signature Edition) - Compounded",
  "Metal-Matrix Nanocomposites: Strength Without the Weight Penalty (Signature Edition) - Compounded",
  "Ceramic-Matrix Nanocomposites: Toughness for Brittle Hosts (Signature Edition) - Compounded",
  "Making Them: Melt Mixing, Solution Blending, In-Situ Polymerization (Signature Edition) - Compounded",
  "Seeing the Invisible: TEM, XRD, and Rheology Fingerprints (Signature Edition) - Compounded",
  "Nanocomposite Coatings: Hard, Slick, and Corrosion-Proof Surfaces (Signature Edition) - Compounded",
  "Electrospun Nanofiber Composites: Mats That Behave Like Materials (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Fracture Toughness: How Nanofillers Stop Cracks (Signature Edition) - Advanced",
  "EMI Shielding: Conductive Networks That Swallow Interference (Signature Edition) - Advanced",
  "Thermal Conductivity: Moving Heat Through a Maze (Signature Edition) - Advanced",
  "Barrier Properties: The Tortuous Path That Blocks Gas (Signature Edition) - Advanced",
  "Flame Retardancy: Char Layers Built by Nanofillers (Signature Edition) - Advanced",
  "3D Printing Nanocomposites: Printing Strength Into Shape (Signature Edition) - Advanced",
  "Biomedical Nanocomposites: Bone Scaffolds and Dental Fillings (Signature Edition) - Advanced",
  "Self-Healing Nanocomposites: Materials That Repair Themselves (Signature Edition) - Advanced",
  "Magnetic Nanocomposites: From Hard Drives to Hyperthermia (Signature Edition) - Advanced",
  "Modeling Across Scales: From Atoms to Finite Elements (Signature Edition) - Advanced",
  "End of Life: Recycling and Sustainability of Nanocomposites (Signature Edition) - Advanced",
  "Working Safe: Nanoparticle Handling and Standards (Signature Edition) - Advanced",
  "Design Rules: The Engineer's Nanocomposite Checklist (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nanocomposites Study — "+safe+"\n"
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
    name:topic+' — nanocomposites record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A nanocomposites record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"nanocomposites-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-nanocomposites-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nanocomposites-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
