(function(){'use strict';
/* JAH The Greatest Discoveries Timeline Database generator — jahdb-db-greatest-discoveries-timeline-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GDT-";
var FIELDS=["Ancient Discoveries","Scientific Revolution","Modern Breakthroughs"];
var TOPICS={
 "Ancient Discoveries": [
  "Fire vs Agriculture: First Revolutions - Ancient Discoveries",
  "Wheel vs Writing: Movers - Ancient Discoveries",
  "Zero vs Compass: Abstractions - Ancient Discoveries",
  "Iron vs Bronze: Metals - Ancient Discoveries",
  "Sail vs Plow: Wind and Soil - Ancient Discoveries",
  "Glass vs Concrete: Materials - Ancient Discoveries",
  "Democracy vs Coinage: Athens Gifts - Ancient Discoveries",
  "Pythagoras vs Euclid: Math Founders - Ancient Discoveries",
  "Archimedes vs Aristotle: Thinkers - Ancient Discoveries",
  "Paper vs Printing: Spread - Ancient Discoveries",
  "Gunpowder vs Compass: Chinese Gifts - Ancient Discoveries",
  "Saddle vs Stirrup: Riding - Ancient Discoveries"
 ],
 "Scientific Revolution": [
  "Heliocentrism vs Telescope: Cosmos - Scientific Revolution",
  "Gravity vs Calculus: Newton - Scientific Revolution",
  "Microscope vs Germ Theory: Small - Scientific Revolution",
  "Steam vs Electricity: Power Ages - Scientific Revolution",
  "Evolution vs Genetics: Life Science - Scientific Revolution",
  "Periodic Table vs Atom: Matter - Scientific Revolution",
  "Anesthesia vs X-Ray: Medicine - Scientific Revolution",
  "Telegraph vs Photography: 1800s - Scientific Revolution",
  "Dynamite vs Barbed Wire: 1800s Tools - Scientific Revolution"
 ],
 "Modern Breakthroughs": [
  "Penicillin vs Insulin: 1920s Medicine - Modern Breakthroughs",
  "DNA vs Transistor: 1947-53 - Modern Breakthroughs",
  "Moon Landing vs Internet: 1969 - Modern Breakthroughs",
  "PCR vs World Wide Web: 1989-90 - Modern Breakthroughs",
  "Human Genome vs iPhone: 2000s - Modern Breakthroughs",
  "CRISPR vs mRNA Vaccines: 2010s-20s - Modern Breakthroughs",
  "JWST vs AlphaFold: 2020s Peaks - Modern Breakthroughs",
  "Fusion Ignition vs Quantum Advantage: Recent - Modern Breakthroughs",
  "Exoplanets vs Gravitational Waves: Cosmos Now - Modern Breakthroughs",
  "AI Milestones: 2012 vs 2022 - Modern Breakthroughs",
  "Renewables Tipping vs EV Tipping: Energy Now - Modern Breakthroughs",
  "COVID Vaccines vs Smallpox Eradication: Public Health - Modern Breakthroughs",
  "Reusable Rockets vs ISS: Space Now - Modern Breakthroughs"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Discoveries Timeline Study — "+safe+"\n"
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
    name:topic+' — discovery comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A discovery comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"discoveries-timeline-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-greatest-discoveries-timeline-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-greatest-discoveries-timeline',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
