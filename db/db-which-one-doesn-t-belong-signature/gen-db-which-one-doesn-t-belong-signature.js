(function(){'use strict';
/* JAH The Which One Doesn't Belong Database Signature Database generator — jahdb-db-which-one-doesn-t-belong-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WHIONEDOES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Odd one out: Apple, Banana, Carrot, Grape",
  "Odd one out: Dog, Cat, Fish, Table",
  "Odd one out: Red, Blue, Green, Happy",
  "Odd one out: 2, 4, 6, 7",
  "Odd one out: Circle, Square, Triangle, Cube",
  "Odd one out: Monday, Tuesday, Wednesday, January",
  "Odd one out: Piano, Guitar, Violin, Drum",
  "Odd one out: Cat, Dog, Bird, Car",
  "Odd one out: Hot, Cold, Warm, Blue",
  "Odd one out: 1, 3, 5, 8",
  "Odd one out: Rose, Tulip, Daisy, Oak"
 ],
 "Compounded": [
  "Odd one out: Mercury, Venus, Earth, Pluto",
  "Odd one out: Shakespeare, Dickens, Austen, Einstein",
  "Odd one out: Eagle, Sparrow, Albatross, Penguin",
  "Odd one out: Paris, London, Tokyo, Nile",
  "Odd one out: Gold, Silver, Bronze, Wood",
  "Odd one out: Bat, Whale, Dolphin, Shark",
  "Odd one out: Addition, Subtraction, Multiplication, Photosynthesis",
  "Odd one out: Violin, Viola, Cello, Flute",
  "Odd one out: Iron, Oxygen, Gold, Water",
  "Odd one out: Novel, Poem, Play, Recipe",
  "Odd one out: Tiger, Lion, Leopard, Wolf",
  "Odd one out: Democracy, Monarchy, Dictatorship, Breakfast"
 ],
 "Advanced": [
  "Odd one out: Eagle, Sparrow, Ostrich, Albatross",
  "Odd one out: Knife, Fork, Spoon, Spork",
  "Odd one out: 12, 18, 24, 21",
  "Odd one out: Meter, Kilogram, Second, Mile",
  "Odd one out: Python, Cobra, Viper, Earthworm",
  "Odd one out: Hamlet, Macbeth, Othello, Waiting for Godot",
  "Odd one out: Pine, Spruce, Fir, Maple",
  "Odd one out: Hydrogen, Helium, Lithium, Carbon",
  "Odd one out: Sonnet, Haiku, Limerick, Epitaph",
  "Odd one out: C, O, S, E",
  "Odd one out: Piano, Organ, Accordion, Trumpet"
 ]
};
var DEMOKIND="intruder-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Odd-One-Out Study — "+safe+"\n"
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
    name:topic+' — odd-one-out record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A odd-one-out record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'jahdb-db-which-one-doesn-t-belong-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-which-one-doesn-t-belong-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
