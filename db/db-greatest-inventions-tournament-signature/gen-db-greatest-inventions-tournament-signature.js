(function(){'use strict';
/* JAH The Greatest Inventions Tournament Signature Database generator — jahdb-db-greatest-inventions-tournament-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GITS-";
var FIELDS=["Ancient Bracket","Industrial Bracket","Modern Bracket"];
var TOPICS={
 "Ancient Bracket": [
  "Wheel vs Fire: The Final? (Signature Edition) - Ancient Bracket",
  "Agriculture vs Writing: Civilization Seeds (Signature Edition) - Ancient Bracket",
  "Bronze vs Iron: Metal Ages (Signature Edition) - Ancient Bracket",
  "Compass vs Map: Navigation (Signature Edition) - Ancient Bracket",
  "Paper vs Papyrus: Writing Surfaces (Signature Edition) - Ancient Bracket",
  "Zero vs Alphabet: Ideas (Signature Edition) - Ancient Bracket",
  "Plow vs Irrigation: Farming (Signature Edition) - Ancient Bracket",
  "Sail vs Oar: Propulsion (Signature Edition) - Ancient Bracket",
  "Arch vs Post-and-Lintel: Building (Signature Edition) - Ancient Bracket",
  "Coinage vs Barter: Money (Signature Edition) - Ancient Bracket",
  "Calendar vs Clock: Time (Signature Edition) - Ancient Bracket",
  "Democracy vs Writing: Governance vs Record (Signature Edition) - Ancient Bracket"
 ],
 "Industrial Bracket": [
  "Printing Press vs Steam Engine: Industrial Seeds (Signature Edition) - Industrial Bracket",
  "Telegraph vs Telephone: Distance Talk (Signature Edition) - Industrial Bracket",
  "Light Bulb vs Electric Grid: Power (Signature Edition) - Industrial Bracket",
  "Automobile vs Airplane: Transport (Signature Edition) - Industrial Bracket",
  "Penicillin vs Vaccine: Medicine (Signature Edition) - Industrial Bracket",
  "Anesthesia vs Antiseptic: Surgery (Signature Edition) - Industrial Bracket",
  "Refrigeration vs Canning: Food (Signature Edition) - Industrial Bracket",
  "Sewing Machine vs Spinning Jenny: Cloth (Signature Edition) - Industrial Bracket",
  "Bessemer vs Assembly Line: Making (Signature Edition) - Industrial Bracket",
  "Camera vs Phonograph: Recording (Signature Edition) - Industrial Bracket"
 ],
 "Modern Bracket": [
  "Internet vs Computer: Digital (Signature Edition) - Modern Bracket",
  "Smartphone vs PC: Personal (Signature Edition) - Modern Bracket",
  "GPS vs Map App: Navigation (Signature Edition) - Modern Bracket",
  "CRISPR vs PCR: Biotech (Signature Edition) - Modern Bracket",
  "Solar Panel vs Battery: Clean (Signature Edition) - Modern Bracket",
  "3D Printer vs CNC: Making New (Signature Edition) - Modern Bracket",
  "mRNA Vaccine vs Antibiotics: Modern Medicine (Signature Edition) - Modern Bracket",
  "AI vs Internet: Next Platform (Signature Edition) - Modern Bracket",
  "Blockchain vs Database: Trust (Signature Edition) - Modern Bracket",
  "Drone vs Satellite: Eyes (Signature Edition) - Modern Bracket",
  "E-book vs Print: Reading (Signature Edition) - Modern Bracket",
  "Streaming vs Cinema: Watching (Signature Edition) - Modern Bracket"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Inventions Tournament Study — "+safe+"\n"
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
    name:topic+' — invention tournament record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A invention tournament record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"inventions-tournament-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-greatest-inventions-tournament-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-greatest-inventions-tournament-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
