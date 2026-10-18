(function(){'use strict';
/* JAH The Rank These Things Database Database generator — jahdb-db-rank-these-things-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RANTHETHI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Rank: Ant, Cat, Elephant, Mouse",
  "Rank: Bicycle, Car, Airplane, Walking",
  "Rank: Day, Week, Month, Year",
  "Rank: Pea, Apple, Watermelon, Grape",
  "Rank: Candle, Lamp, Sun, Flashlight",
  "Rank: Egg, Chicken, Dinosaur, Whale",
  "Rank: Second, Minute, Hour, Day",
  "Rank: Turtle, Human, Cheetah, Snail",
  "Rank: Puddle, Pond, Lake, Ocean",
  "Rank: Whisper, Talk, Shout, Jet engine",
  "Rank: Seed, Sprout, Tree, Forest"
 ],
 "Compounded": [
  "Rank: Mercury, Earth, Jupiter, Mars",
  "Rank: Cheetah, Pronghorn, Lion, Greyhound",
  "Rank: Eiffel Tower, Empire State, Burj Khalifa, Shanghai Tower",
  "Rank: Amazon, Nile, Mississippi, Thames",
  "Rank: Blue whale, Elephant, Giraffe, Hippo",
  "Rank: Everest, K2, Kangchenjunga, Fuji",
  "Rank: Falcon, Eagle, Sparrow, Ostrich",
  "Rank: Diamond, Gold, Silver, Copper",
  "Rank: Sahara, Gobi, Mojave, Antarctic",
  "Rank: Pacific, Atlantic, Indian, Arctic",
  "Rank: Giraffe, Elephant, Blue whale, Ostrich",
  "Rank: Lightning, Sound, Car, Bullet"
 ],
 "Advanced": [
  "Rank: Jupiter, Saturn, Neptune, Earth",
  "Rank: Sperm whale, Colossal squid, Giant squid, Blue whale",
  "Rank: Oak, Redwood, Baobab, Bristlecone pine",
  "Rank: Venus, Mars, Mercury, Jupiter",
  "Rank: Antarctica, Australia, Europe, Africa",
  "Rank: Cheetah, Sailfish, Peregrine falcon, Pronghorn",
  "Rank: Iron, Lead, Gold, Aluminum",
  "Rank: Shakespeare, Dickens, Twain, Austen",
  "Rank: Grain of sand, Basketball, Moon, Sun",
  "Rank: Nile, Amazon, Yangtze, Mississippi",
  "Rank: Everest, Dead Sea shore, Mariana Trench, Denver"
 ]
};
var DEMOKIND="ranking-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Ranking Study — "+safe+"\n"
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
    name:topic+' — ranking challenge record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A ranking challenge record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-rank-these-things-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-rank-these-things',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
