(function(){'use strict';
/* JAH The Oldest Things Signature Database generator — jahdb-db-oldest-things-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OTS-";
var FIELDS=["Age Foundations","Ancient Life","Ancient Works"];
var TOPICS={
 "Age Foundations": [
  "Bristlecone Pine vs Giant Tortoise: Old Souls (Signature Edition) - Age Foundations",
  "Shark vs Tortoise: Long-Lived Animals (Signature Edition) - Age Foundations",
  "Pyramid vs Stonehenge: Ancient Stones (Signature Edition) - Age Foundations",
  "Oak vs Sequoia: Tree Elders (Signature Edition) - Age Foundations",
  "Crocodile vs Coelacanth: Living Fossils (Signature Edition) - Age Foundations",
  "Language vs Writing: Old Communication (Signature Edition) - Age Foundations",
  "Fire Use vs Tool Use: Human Firsts (Signature Edition) - Age Foundations",
  "Wheel vs Agriculture: Civilization Roots (Signature Edition) - Age Foundations",
  "Ocean vs Atmosphere: Old Earth Systems (Signature Edition) - Age Foundations",
  "Universe vs Earth: Cosmic Age (Signature Edition) - Age Foundations",
  "Bible (Manuscript) vs Diamond Sutra: Old Books (Signature Edition) - Age Foundations",
  "Tortoise vs Parrot: Pet Longevity (Signature Edition) - Age Foundations"
 ],
 "Ancient Life": [
  "Clam vs Jellyfish: Immortal-ish? (Signature Edition) - Ancient Life",
  "Redwood vs Bristlecone: Tree Kings (Signature Edition) - Ancient Life",
  "Bowhead Whale vs Elephant: Mammal Elders (Signature Edition) - Ancient Life",
  "Koi vs Goldfish: Pond Elders (Signature Edition) - Ancient Life",
  "Sponge vs Coral: Ancient Colonies (Signature Edition) - Ancient Life",
  "Tuatara vs Turtle: Reptile Relics (Signature Edition) - Ancient Life",
  "Ant Colony vs Tree: Oldest Organism? (Signature Edition) - Ancient Life",
  "Lobster vs Crab: Ageless? (Signature Edition) - Ancient Life",
  "Bacteria vs Virus: Oldest Life (Signature Edition) - Ancient Life",
  "Human vs Neanderthal: Cousin Ages (Signature Edition) - Ancient Life"
 ],
 "Ancient Works": [
  "Cave Painting vs Pottery: Old Art (Signature Edition) - Ancient Works",
  "Pyramid vs Ziggurat: Old Monuments (Signature Edition) - Ancient Works",
  "Roman Road vs Silk Road: Old Routes (Signature Edition) - Ancient Works",
  "Axe vs Knife: Old Tools (Signature Edition) - Ancient Works",
  "Boat vs Cart: Old Transport (Signature Edition) - Ancient Works",
  "Bread vs Beer: Old Foods (Signature Edition) - Ancient Works",
  "Calendar vs Alphabet: Old Systems (Signature Edition) - Ancient Works",
  "City vs Village: Old Settlements (Signature Edition) - Ancient Works",
  "Temple vs House: Old Buildings (Signature Edition) - Ancient Works",
  "Song vs Story: Old Arts (Signature Edition) - Ancient Works",
  "Gold vs Copper: Old Metals (Signature Edition) - Ancient Works",
  "Dog vs Cat: Old Companions (Signature Edition) - Ancient Works"
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
var gen={version:'jahdb-db-oldest-things-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-oldest-things-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
