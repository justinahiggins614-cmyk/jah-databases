(function(){'use strict';
/* JAH The Greek Mythology Database generator — jahdb-greek-mythology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GRMY-";
var FIELDS=["The Olympians", "Heroes & Epics", "Creatures & Cosmos"];
var TOPICS={
 "The Olympians": [
  "Zeus — King of the Gods \u2014 The Olympians",
  "Hera — Queen of Heaven \u2014 The Olympians",
  "Poseidon — God of the Sea \u2014 The Olympians",
  "Athena — Goddess of Wisdom \u2014 The Olympians",
  "Apollo — God of Light and Prophecy \u2014 The Olympians",
  "Artemis — Goddess of the Hunt \u2014 The Olympians",
  "Ares — God of War \u2014 The Olympians",
  "Aphrodite — Goddess of Love \u2014 The Olympians",
  "Hephaestus — God of the Forge \u2014 The Olympians",
  "Hermes — Messenger of the Gods \u2014 The Olympians",
  "Demeter — Goddess of the Harvest \u2014 The Olympians",
  "Hades — Lord of the Underworld \u2014 The Olympians"
 ],
 "Heroes & Epics": [
  "Heracles — The Twelve Labors \u2014 Heroes & Epics",
  "Theseus — Slayer of the Minotaur \u2014 Heroes & Epics",
  "Perseus — Slayer of Medusa \u2014 Heroes & Epics",
  "Odysseus — The Long Voyage Home \u2014 Heroes & Epics",
  "Achilles — The Wrath of the Iliad \u2014 Heroes & Epics",
  "Jason — The Golden Fleece \u2014 Heroes & Epics",
  "The Trojan War — Ten Years at Troy \u2014 Heroes & Epics",
  "The Odyssey — Monsters and Temptations \u2014 Heroes & Epics",
  "Oedipus — The Riddle of the Sphinx \u2014 Heroes & Epics",
  "Orpheus — The Descent for Eurydice \u2014 Heroes & Epics",
  "Daedalus and Icarus — The Waxen Wings \u2014 Heroes & Epics",
  "The Argonauts — Crew of the Argo \u2014 Heroes & Epics"
 ],
 "Creatures & Cosmos": [
  "The Titans — The First Gods \u2014 Creatures & Cosmos",
  "The Creation — From Chaos to Cosmos \u2014 Creatures & Cosmos",
  "Prometheus — Fire-Bringer and Trickster \u2014 Creatures & Cosmos",
  "Pandora — The First Woman and the Jar \u2014 Creatures & Cosmos",
  "Medusa — The Gorgon \u2014 Creatures & Cosmos",
  "The Minotaur — The Labyrinth Beast \u2014 Creatures & Cosmos",
  "The Oracle of Delphi — Voice of Apollo \u2014 Creatures & Cosmos",
  "The Underworld — Hades' Realm \u2014 Creatures & Cosmos",
  "The Fates — Clotho, Lachesis, Atropos \u2014 Creatures & Cosmos",
  "The Muses — Nine Goddesses of the Arts \u2014 Creatures & Cosmos"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Greek Mythology — "+safe+"\n"
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
var gen={version:'jahdb-greek-mythology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('greek-mythology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
