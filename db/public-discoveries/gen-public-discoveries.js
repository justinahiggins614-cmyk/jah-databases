(function(){'use strict';
/* JAH Public Discoveries Database generator — jahdb-public-discoveries-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-DISC-';
var FIELDS=["physics", "biology", "medicine", "chemistry", "astronomy", "geology", "geography", "technology"];
var TOPICS={
 "astronomy":["Heliocentrism","Laws of Planetary Motion","Neptune (Mathematical Prediction)","Cosmic Microwave Background","Exoplanets (51 Pegasi b)","Expanding Universe","Black Holes (Cygnus X-1)","Dark Matter (Galaxy Rotation)","Dark Energy (Accelerating Universe)","Stellar Nucleosynthesis","Cosmic Structures","Stellar Phenomena","Planetary Systems"],
 "biology":["DNA Double Helix Structure","Evolution by Natural Selection","DNA as Genetic Material","Neurons and the Nervous System","Photosynthesis Mechanism","CRISPR Gene Editing","REM Sleep","Mendelian Inheritance","Genetic Mechanisms","Ecological Patterns","Cellular Processes"],
 "chemistry":["Oxygen and Combustion","Periodic Table of Elements","Reaction Pathways","Compound Syntheses","Analytical Techniques"],
 "geography":["The New World (1492 Voyage)","Pacific Ocean Crossing","Antarctica Sighted","Source of the Nile","Expedition Routes","Cartographic Methods","Terrain Surveys"],
 "geology":["Plate Tectonics","Deep Time (Geologic Time Scale)","Tectonic Processes","Mineral Formations","Stratigraphic Records"],
 "medicine":["Penicillin","Vaccination (Smallpox)","Germ Theory of Disease","Insulin","Blood Circulation","Anesthesia (Ether)","Antiseptic Surgery","Vitamins","Blood Groups (ABO)","Hormones (Secretin)","Anesthesia (Chloroform Obstetric)","Treatment Protocols","Diagnostic Methods","Preventive Measures"],
 "physics":["Gravity and Universal Gravitation","Theory of Relativity","Electromagnetic Induction","Radioactivity","X-Rays","Higgs Boson","Gravitational Waves","Quantum Mechanics (Matrix/Wave)","Nuclear Fission","Superconductivity","The Electron","The Nucleus (Rutherford Atom)","Antimatter (Positron)","Neutron","Quantum Field Extensions","Relativity Applications","Particle Discoveries"],
 "technology":["Printing Press (Movable Type)","Steam Engine (Practical)","Telephone","Light Bulb (Practical Incandescent)","Airplane (Powered Flight)","Transistor","Integrated Circuit","World Wide Web","Continental Shelf Oil (Offshore Drilling)","Invention Lineages","Engineering Breakthroughs","System Designs"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Discovery Lab — "+safe+"\n"
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
    name:topic+' — discovery study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A discovery study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'discovery-explorer',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-public-discoveries-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-discoveries',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
