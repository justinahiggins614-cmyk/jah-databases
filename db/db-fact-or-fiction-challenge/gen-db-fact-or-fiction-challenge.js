(function(){'use strict';
/* JAH The Fact or Fiction Challenge Database generator — jahdb-db-fact-or-fiction-challenge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FACORFIC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Fact or fiction: Water boils at 100 degrees Celsius...",
  "Fact or fiction: Bats are blind...",
  "Fact or fiction: The Great Wall of China is visible from the Moon...",
  "Fact or fiction: Goldfish have a 3-second memory...",
  "Fact or fiction: Lightning never strikes the same place twice...",
  "Fact or fiction: Humans use only 10% of their brains...",
  "Fact or fiction: Ostriches bury their heads in the sand...",
  "Fact or fiction: A penny dropped from a skyscraper can kill...",
  "Fact or fiction: Cracking knuckles causes arthritis...",
  "Fact or fiction: The five-second rule keeps food safe...",
  "Fact or fiction: Mount Everest is the tallest mountain on Earth..."
 ],
 "Compounded": [
  "Fact or fiction: Honey never spoils...",
  "Fact or fiction: There are more possible chess games than atoms in the un...",
  "Fact or fiction: Sharks get cancer...",
  "Fact or fiction: The Eiffel Tower grows taller in summer...",
  "Fact or fiction: Bananas are radioactive...",
  "Fact or fiction: Glass is a slow-moving liquid...",
  "Fact or fiction: You can see the Great Wall from space with the naked eye...",
  "Fact or fiction: Walt Disney is frozen...",
  "Fact or fiction: Napoleon was short...",
  "Fact or fiction: Vikings wore horned helmets...",
  "Fact or fiction: A duck's quack does not echo...",
  "Fact or fiction: Humans and dinosaurs coexisted..."
 ],
 "Advanced": [
  "Fact or fiction: Cleopatra lived closer in time to the iPhone than to the...",
  "Fact or fiction: Oxford University is older than the Aztec Empire...",
  "Fact or fiction: There are more trees on Earth than stars in the Milky Wa...",
  "Fact or fiction: Woolly mammoths were still alive while the pyramids were...",
  "Fact or fiction: The first oranges were not orange...",
  "Fact or fiction: Nintendo was founded when Jack the Ripper was active...",
  "Fact or fiction: Shakespeare and Pocahontas died in the same year...",
  "Fact or fiction: The sun is a green star...",
  "Fact or fiction: Hot water can freeze faster than cold water...",
  "Fact or fiction: There is a giant water reservoir in space holding 140 tr...",
  "Fact or fiction: The dot over the letter i has a name..."
 ]
};
var DEMOKIND="verdict-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fact or Fiction Study — "+safe+"\n"
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
    name:topic+' — fact-or-fiction record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fact-or-fiction record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-fact-or-fiction-challenge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-fact-or-fiction-challenge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
