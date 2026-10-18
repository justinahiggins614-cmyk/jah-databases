(function(){'use strict';
/* JAH The Strange Animal Database Database generator — jahdb-db-strange-animal-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Platypus Paradox",
  "Narwhal Tusks",
  "The Mantis Shrimp (Again, Stranger)",
  "Axolotl Neoteny",
  "The Star-Nosed Mole",
  "Tardigrade Toughness",
  "The Immortal Jellyfish Cycle",
  "Goblin Sharks",
  "The Saiga Antelope",
  "Naked Mole-Rats",
  "The Aye-Aye"
 ],
 "Compounded": [
  "Strangeness: A Field Guide",
  "The Barreleye Fish",
  "Vampire Squid Turnarounds",
  "The Pangolin Armor",
  "Glass Frogs",
  "The Thorny Devil",
  "Yeti Crabs",
  "The Okapi Mystery",
  "Strange Defenses",
  "Strange Reproduction",
  "The Proboscis Monkey",
  "The Blobfish Reality"
 ],
 "Advanced": [
  "Advanced: The Science of Weird",
  "Advanced: Undiscovered Strangeness",
  "Advanced: Weird and Wonderful Pets",
  "Advanced: The Strangeness Tournament",
  "Advanced: Strangeness in the Fossil Record",
  "Advanced: Protecting the Strange",
  "Advanced: Weird Symbiosis",
  "Advanced: The Mantis Shrimp Eye Lab",
  "Advanced: Strange Migrations",
  "Advanced: The Museum of Weird",
  "The Strange Animal Encyclopedia"
 ]
};
var DEMOKIND="animals-lab-demo";
var SAMPLEDESC="Sample records are complete real species entries with real measurement math.";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nature Lab Demo — "+safe+"\n"
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
    name:topic+' — strange animal record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A strange animal record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-strange-animal-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-strange-animal',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
