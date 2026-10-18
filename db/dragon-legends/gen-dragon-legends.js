(function(){'use strict';
/* JAH The Dragon Legends Database generator — jahdb-dragon-legends-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DRGL-";
var FIELDS=["Dragons of the East", "Dragons of the West", "Dragon Lore & Symbolism"];
var TOPICS={
 "Dragons of the East": [
  "The Chinese Long — The Rain Dragon \u2014 Dragons of the East",
  "The Japanese Ryu — The Water Kami \u2014 Dragons of the East",
  "The Korean Yong — The Sky Dragon \u2014 Dragons of the East",
  "The Vietnamese Rong — The Ancestor \u2014 Dragons of the East",
  "Quetzalcoatl — The Feathered Serpent \u2014 Dragons of the East",
  "The Naga — Serpent Kings \u2014 Dragons of the East",
  "Tiamat — The First Dragon \u2014 Dragons of the East",
  "The Lung Wang — Dragon Kings of China \u2014 Dragons of the East"
 ],
 "Dragons of the West": [
  "Fafnir — The Gold Dragon \u2014 Dragons of the West",
  "Jormungandr — The Midgard Serpent \u2014 Dragons of the West",
  "The Beowulf Dragon \u2014 Dragons of the West",
  "Ladon — The Hesperian Dragon \u2014 Dragons of the West",
  "Python — The Delphic Serpent \u2014 Dragons of the West",
  "Saint George — The Dragon Saint \u2014 Dragons of the West",
  "The Lambton Worm \u2014 Dragons of the West",
  "The Wawel Dragon \u2014 Dragons of the West",
  "The Hydra — Many-Headed \u2014 Dragons of the West",
  "The Basilisk — The King Serpent \u2014 Dragons of the West",
  "The Wyvern — The Two-Legged \u2014 Dragons of the West",
  "The Tarasque — The Tamed Dragon \u2014 Dragons of the West",
  "Nidhogg — The Corpse Gnawer \u2014 Dragons of the West",
  "The Cockatrice — The Rooster Serpent \u2014 Dragons of the West"
 ],
 "Dragon Lore & Symbolism": [
  "Dragon-Slayers — The Roll \u2014 Dragon Lore & Symbolism",
  "Dragon Hoards — The Gold \u2014 Dragon Lore & Symbolism",
  "Dragon Blood — The Power \u2014 Dragon Lore & Symbolism",
  "The Dragon's Pearl — Wisdom \u2014 Dragon Lore & Symbolism",
  "East vs West — The Great Divide \u2014 Dragon Lore & Symbolism",
  "The Serpent in Eden — The Biblical Dragon \u2014 Dragon Lore & Symbolism",
  "Dragon Festivals — The Celebration \u2014 Dragon Lore & Symbolism",
  "The Last Dragons — Survivors \u2014 Dragon Lore & Symbolism",
  "Draco — The Constellation \u2014 Dragon Lore & Symbolism",
  "The Dragon's Hoard — Psychology \u2014 Dragon Lore & Symbolism",
  "Dragon Eggs — The Promise \u2014 Dragon Lore & Symbolism",
  "The Dragon's Breath — Fire \u2014 Dragon Lore & Symbolism"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Dragon Legends — "+safe+"\n"
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
    name:topic+' — mythology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mythology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-dragon-legends-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('dragon-legends',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
