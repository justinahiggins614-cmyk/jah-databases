(function(){'use strict';
/* JAH The Nanomechanics Signature Database generator — jahdb-nanomechanics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Nanomechanics: The Science of Forces at the Nanoscale (Signature Edition) - Foundations",
  "Smaller Is Different: Size Effects in Mechanical Behavior (Signature Edition) - Foundations",
  "Stress, Strain, and Modulus at the Nanoscale: The Universal Language (Signature Edition) - Foundations",
  "Where Continuum Mechanics Breaks Down: The Ten-Nanometre Boundary (Signature Edition) - Foundations",
  "Surface Energy and Surface Stress: Why Small Surfaces Rule (Signature Edition) - Foundations",
  "Van der Waals, Capillary, and Electrostatic Forces at the Nanoscale (Signature Edition) - Foundations",
  "Bending a Nanobeam: Euler-Bernoulli Shrunk a Million Times (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Nanoindentation: Reading Hardness from a Force Curve (Signature Edition) - Compounded",
  "The Oliver-Pharr Method: Unloading Curves to Modulus (Signature Edition) - Compounded",
  "AFM Force Spectroscopy: Pulling Single Molecules Apart (Signature Edition) - Compounded",
  "Nanowires in Tension: Stronger Than Steel, Tested One at a Time (Signature Edition) - Compounded",
  "Hall-Petch and Its Breakdown: Grain Size vs Strength (Signature Edition) - Compounded",
  "Carbon Nanotube Mechanics: The One-Terapascal Spring (Signature Edition) - Compounded",
  "Graphene Mechanics: One Atom Thick, Strongest Material Known (Signature Edition) - Compounded",
  "Nanotribology: Friction, Wear, and Stick-Slip at Atomic Scale (Signature Edition) - Compounded",
  "Contact Mechanics at the Nanoscale: Hertz, JKR, DMT (Signature Edition) - Compounded",
  "Adhesion and Stiction: When Surfaces Won't Let Go (Signature Edition) - Compounded",
  "NEMS Resonators: Weighing Single Molecules with Vibrating Beams (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Nanotube and Nanowire Resonators: Gigahertz Mechanics (Signature Edition) - Advanced",
  "Fatigue of Nanostructures: A Billion Cycles of Tiny Bending (Signature Edition) - Advanced",
  "Fracture at the Nanoscale: Flaws, Toughness, and Ideal Strength (Signature Edition) - Advanced",
  "Molecular Dynamics for Mechanics: Atoms as Springs (Signature Edition) - Advanced",
  "In-Situ TEM Nanomechanical Testing: Watching Deformation Live (Signature Edition) - Advanced",
  "Dislocation Starvation and Source Truncation: Plasticity Without Dislocations (Signature Edition) - Advanced",
  "Shape Memory and Superelasticity at the Nanoscale (Signature Edition) - Advanced",
  "Nanotrusses and Mechanical Metamaterials: Strength Without Weight (Signature Edition) - Advanced",
  "Viscoelasticity at the Nanoscale: Polymers, Creep, and Time (Signature Edition) - Advanced",
  "Buckling, Wrinkling, and Instability of Nanostructures (Signature Edition) - Advanced",
  "Thermoelastic Damping and Heat at the Nanoscale: The Hot Small World (Signature Edition) - Advanced",
  "Electromechanical Coupling: Piezoelectric Nanowires and Flexoelectricity (Signature Edition) - Advanced",
  "Nanomechanics in Fluids: Damping, Squeeze Films, and the Quality Factor (Signature Edition) - Advanced",
  "Quantum Limits of Nanomechanical Motion: Toward the Ground State (Signature Edition) - Advanced",
  "Design Rules for Nanomechanical Devices: From Concept to Chip (Signature Edition) - Advanced",
  "Nanobiomechanics: Cells, Proteins, and DNA as Mechanical Structures (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nanomechanics Study — "+safe+"\n"
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
    name:topic+' — nanomechanics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A nanomechanics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"nanomechanics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-nanomechanics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nanomechanics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
