(function(){'use strict';
/* JAH The Science Quiz Database generator — jahdb-quiz-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-QZSC-";
var FIELDS=["Physics","Chemistry","Biology","Earth Science","Astronomy"];
var TOPICS={
 "Physics": [
  "What Is Motion? A First Physics Quiz - Physics",
  "Pushes, Pulls, and Magnets - Physics",
  "Simple Machines - Physics",
  "Light, Shadows, and Color - Physics",
  "Forces, Friction, and Newton's First Law - Physics",
  "Energy: Kinetic and Potential - Physics",
  "Electricity: Circuits and Current - Physics",
  "Waves: Sound and Light - Physics",
  "Gravity, Orbits, and Kepler's Laws - Physics",
  "Relativity: Time and Space Basics - Physics"
 ],
 "Chemistry": [
  "Matter All Around Us - Chemistry",
  "The Air We Breathe and Mixtures - Chemistry",
  "Acids and Bases Around the Home - Chemistry",
  "The Periodic Table: Reading the Chart - Chemistry",
  "Chemical Reactions: What Changes - Chemistry",
  "Atoms: Protons, Neutrons, Electrons - Chemistry",
  "Bonding: Ionic and Covalent - Chemistry",
  "Stoichiometry: Counting Atoms - Chemistry"
 ],
 "Biology": [
  "Living Things and Their Needs - Biology",
  "Plants and How They Grow - Biology",
  "The Human Body: Bones and Muscles - Biology",
  "Ecosystems and Food Chains - Biology",
  "Cells: The Building Blocks of Life - Biology",
  "Photosynthesis and Respiration - Biology",
  "DNA, Genes, and Heredity - Biology"
 ],
 "Earth Science": [
  "Day, Night, and the Seasons - Earth Science",
  "Rocks and the Rock Cycle - Earth Science",
  "Weather and the Water Cycle - Earth Science",
  "Plate Tectonics and Earthquakes - Earth Science",
  "Climate Systems and the Greenhouse Effect - Earth Science"
 ],
 "Astronomy": [
  "Our Sun and the Planets - Astronomy",
  "The Moon and Its Phases - Astronomy",
  "Stars: How Stars Are Born, Live, and Die - Astronomy",
  "Cosmology: The Big Bang and Beyond - Astronomy"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Science Quiz Study — "+safe+"\n"
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
    name:topic+' — quiz record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A quiz record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"science-quiz-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-quiz-science-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quiz-science',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
