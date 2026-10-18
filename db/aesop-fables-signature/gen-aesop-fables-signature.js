(function(){'use strict';
/* JAH The Aesop Fables Signature Database generator — jahdb-aesop-fables-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AESF-S-";
var FIELDS=["Fables of Cunning", "Fables of Character", "Fables of Wisdom"];
var TOPICS={
 "Fables of Cunning": [
  "The Lion and the Mouse (Signature Edition) \u2014 Fables of Cunning",
  "The Signature Method for The Fox and the Crow \u2014 Fables of Cunning",
  "The Fox and the Stork (Signature Edition) \u2014 Fables of Cunning",
  "The Bat, the Birds, and the Beasts (Signature Edition) \u2014 Fables of Cunning",
  "The Signature Method for The Lion's Share \u2014 Fables of Cunning",
  "The Signature Method for The Cat and the Mice — The Hanged Cat \u2014 Fables of Cunning"
 ],
 "Fables of Character": [
  "The Signature Method for The Fox and the Grapes \u2014 Fables of Character",
  "The Boy Who Cried Wolf (Signature Edition) \u2014 Fables of Character",
  "The Signature Method for The Wolf in Sheep's Clothing \u2014 Fables of Character",
  "The Dog and the Bone (Signature Edition) \u2014 Fables of Character",
  "The Ass in the Lion's Skin (Signature Edition) \u2014 Fables of Character",
  "The Signature Method for The Miser and His Gold \u2014 Fables of Character",
  "The Signature Method for The Wolf and the Lamb \u2014 Fables of Character",
  "The Signature Method for The Donkey and the Lapdog \u2014 Fables of Character",
  "The Signature Method for The Goose That Laid Golden Eggs \u2014 Fables of Character",
  "The Peacock and the Crane (Signature Edition) \u2014 Fables of Character",
  "The Man and the Satyr (Signature Edition) \u2014 Fables of Character",
  "The Signature Method for The Quack Frog \u2014 Fables of Character"
 ],
 "Fables of Wisdom": [
  "The Tortoise and the Hare (Signature Edition) \u2014 Fables of Wisdom",
  "The Signature Method for The Ant and the Grasshopper \u2014 Fables of Wisdom",
  "The Hare and the Tortoise's Lesson (Signature Edition) \u2014 Fables of Wisdom",
  "The Signature Method for The Town Mouse and the Country Mouse \u2014 Fables of Wisdom",
  "The Belly and the Members (Signature Edition) \u2014 Fables of Wisdom",
  "The Signature Method for The Frogs Who Desired a King \u2014 Fables of Wisdom",
  "The Old Man and Death (Signature Edition) \u2014 Fables of Wisdom",
  "The Signature Method for The Oak and the Reed \u2014 Fables of Wisdom",
  "The Wind and the Sun (Signature Edition) \u2014 Fables of Wisdom",
  "The Milkmaid and Her Pail (Signature Edition) \u2014 Fables of Wisdom",
  "The Signature Method for The Two Pots \u2014 Fables of Wisdom",
  "The Crab and Its Mother (Signature Edition) \u2014 Fables of Wisdom",
  "The Signature Method for The Horse and the Ass \u2014 Fables of Wisdom",
  "The Nurse and the Wolf (Signature Edition) \u2014 Fables of Wisdom",
  "The Signature Method for The Bald Man and the Fly \u2014 Fables of Wisdom",
  "The Shipwrecked Man and the Sea (Signature Edition) \u2014 Fables of Wisdom"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Aesop Fables Signature — "+safe+"\n"
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
    name:topic+' — fable record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fable record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-aesop-fables-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('aesop-fables-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
