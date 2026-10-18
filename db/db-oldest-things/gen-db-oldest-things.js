(function(){'use strict';
/* JAH The Oldest Things Database generator — jahdb-db-oldest-things-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OT-";
var FIELDS=["Age Foundations","Ancient Life","Ancient Works"];
var TOPICS={
 "Age Foundations": [
  "Bristlecone Pine vs Giant Tortoise: Old Souls - Age Foundations",
  "Shark vs Tortoise: Long-Lived Animals - Age Foundations",
  "Pyramid vs Stonehenge: Ancient Stones - Age Foundations",
  "Oak vs Sequoia: Tree Elders - Age Foundations",
  "Crocodile vs Coelacanth: Living Fossils - Age Foundations",
  "Language vs Writing: Old Communication - Age Foundations",
  "Fire Use vs Tool Use: Human Firsts - Age Foundations",
  "Wheel vs Agriculture: Civilization Roots - Age Foundations",
  "Ocean vs Atmosphere: Old Earth Systems - Age Foundations",
  "Universe vs Earth: Cosmic Age - Age Foundations",
  "Bible (Manuscript) vs Diamond Sutra: Old Books - Age Foundations",
  "Tortoise vs Parrot: Pet Longevity - Age Foundations"
 ],
 "Ancient Life": [
  "Clam vs Jellyfish: Immortal-ish? - Ancient Life",
  "Redwood vs Bristlecone: Tree Kings - Ancient Life",
  "Bowhead Whale vs Elephant: Mammal Elders - Ancient Life",
  "Koi vs Goldfish: Pond Elders - Ancient Life",
  "Sponge vs Coral: Ancient Colonies - Ancient Life",
  "Tuatara vs Turtle: Reptile Relics - Ancient Life",
  "Ant Colony vs Tree: Oldest Organism? - Ancient Life",
  "Lobster vs Crab: Ageless? - Ancient Life",
  "Bacteria vs Virus: Oldest Life - Ancient Life",
  "Human vs Neanderthal: Cousin Ages - Ancient Life"
 ],
 "Ancient Works": [
  "Cave Painting vs Pottery: Old Art - Ancient Works",
  "Pyramid vs Ziggurat: Old Monuments - Ancient Works",
  "Roman Road vs Silk Road: Old Routes - Ancient Works",
  "Axe vs Knife: Old Tools - Ancient Works",
  "Boat vs Cart: Old Transport - Ancient Works",
  "Bread vs Beer: Old Foods - Ancient Works",
  "Calendar vs Alphabet: Old Systems - Ancient Works",
  "City vs Village: Old Settlements - Ancient Works",
  "Temple vs House: Old Buildings - Ancient Works",
  "Song vs Story: Old Arts - Ancient Works",
  "Gold vs Copper: Old Metals - Ancient Works",
  "Dog vs Cat: Old Companions - Ancient Works"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Oldest Things Study — "+safe+"\n"
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
    name:topic+' — age comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A age comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"oldest-things-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-oldest-things-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-oldest-things',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
