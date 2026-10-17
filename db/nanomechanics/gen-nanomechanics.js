(function(){'use strict';
/* JAH The Nanomechanics Database generator — jahdb-nanomechanics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NMH-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Nanomechanics: The Science of Forces at the Nanoscale - Foundations",
  "Smaller Is Different: Size Effects in Mechanical Behavior - Foundations",
  "Stress, Strain, and Modulus at the Nanoscale: The Universal Language - Foundations",
  "Where Continuum Mechanics Breaks Down: The Ten-Nanometre Boundary - Foundations",
  "Surface Energy and Surface Stress: Why Small Surfaces Rule - Foundations",
  "Van der Waals, Capillary, and Electrostatic Forces at the Nanoscale - Foundations",
  "Bending a Nanobeam: Euler-Bernoulli Shrunk a Million Times - Foundations"
 ],
 "Compounded": [
  "Nanoindentation: Reading Hardness from a Force Curve - Compounded",
  "The Oliver-Pharr Method: Unloading Curves to Modulus - Compounded",
  "AFM Force Spectroscopy: Pulling Single Molecules Apart - Compounded",
  "Nanowires in Tension: Stronger Than Steel, Tested One at a Time - Compounded",
  "Hall-Petch and Its Breakdown: Grain Size vs Strength - Compounded",
  "Carbon Nanotube Mechanics: The One-Terapascal Spring - Compounded",
  "Graphene Mechanics: One Atom Thick, Strongest Material Known - Compounded",
  "Nanotribology: Friction, Wear, and Stick-Slip at Atomic Scale - Compounded",
  "Contact Mechanics at the Nanoscale: Hertz, JKR, DMT - Compounded",
  "Adhesion and Stiction: When Surfaces Won't Let Go - Compounded",
  "NEMS Resonators: Weighing Single Molecules with Vibrating Beams - Compounded"
 ],
 "Advanced": [
  "Nanotube and Nanowire Resonators: Gigahertz Mechanics - Advanced",
  "Fatigue of Nanostructures: A Billion Cycles of Tiny Bending - Advanced",
  "Fracture at the Nanoscale: Flaws, Toughness, and Ideal Strength - Advanced",
  "Molecular Dynamics for Mechanics: Atoms as Springs - Advanced",
  "In-Situ TEM Nanomechanical Testing: Watching Deformation Live - Advanced",
  "Dislocation Starvation and Source Truncation: Plasticity Without Dislocations - Advanced",
  "Shape Memory and Superelasticity at the Nanoscale - Advanced",
  "Nanotrusses and Mechanical Metamaterials: Strength Without Weight - Advanced",
  "Viscoelasticity at the Nanoscale: Polymers, Creep, and Time - Advanced",
  "Buckling, Wrinkling, and Instability of Nanostructures - Advanced",
  "Thermoelastic Damping and Heat at the Nanoscale: The Hot Small World - Advanced",
  "Electromechanical Coupling: Piezoelectric Nanowires and Flexoelectricity - Advanced",
  "Nanomechanics in Fluids: Damping, Squeeze Films, and the Quality Factor - Advanced",
  "Quantum Limits of Nanomechanical Motion: Toward the Ground State - Advanced",
  "Design Rules for Nanomechanical Devices: From Concept to Chip - Advanced",
  "Nanobiomechanics: Cells, Proteins, and DNA as Mechanical Structures - Advanced"
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
var gen={version:'jahdb-nanomechanics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nanomechanics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
