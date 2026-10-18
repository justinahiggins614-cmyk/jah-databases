(function(){'use strict';
/* JAH The Imaginary Music Genre Database generator — jahdb-imaginary-music-genre-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMGN-";
var FIELDS=["Genre Seeds", "Imagined Worlds", "Genre Mastery"];
var TOPICS={
 "Genre Seeds": [
  "Anatomy of a Genre",
  "Naming the Unheard",
  "The Signature Sound",
  "Tempo as Identity",
  "Lore and Mythology",
  "Fashion of the Unheard",
  "The First Track",
  "Genre Family Trees",
  "The Scene Starter Kit",
  "Describing the Indescribable",
  "The Anti-Genre",
  "Microgenres and Hyperpop Logic"
 ],
 "Imagined Worlds": [
  "Glacierwave",
  "Clockwork Soul",
  "Mycelium Drone",
  "Neon Tango",
  "Desert Circuit",
  "Paper Orchestra",
  "Gravwave",
  "Lullaby Rave",
  "Thunderchoir",
  "Jellyfish Jazz",
  "Copperbeat",
  "Cathedral Organ Trap",
  "Subway Symphony",
  "Bioluminescent Ballads",
  "Tornado Polka",
  "Aurora Choir"
 ],
 "Genre Mastery": [
  "The Genre Census",
  "Making an Imaginary Genre Real",
  "Your Imaginary Genre",
  "The Genre Cookbook",
  "The Imaginary Festival",
  "Archiving the Unheard"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# genre — "+safe+"\n"
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
    name:topic+' — imaginary music genre record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A imaginary music genre record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"genre-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-imaginary-music-genre-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('imaginary-music-genre',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
