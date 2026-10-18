(function(){'use strict';
/* JAH The Can You Solve It Database Database generator — jahdb-db-can-you-solve-it-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CANYOUSOL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Can you solve it? What has keys but no locks, space but no room, and y...",
  "Can you solve it? I am always hungry and must always be fed; the finge...",
  "Can you solve it? What gets wetter the more it dries...",
  "Can you solve it? What has a head and a tail but no body...",
  "Can you solve it? The more you take, the more you leave behind. What a...",
  "Can you solve it? What comes once in a minute, twice in a moment, but...",
  "Can you solve it? What has many needles but never sews...",
  "Can you solve it? What runs but never walks, has a mouth but never tal...",
  "Can you solve it? I have cities but no houses, forests but no trees, r...",
  "Can you solve it? What belongs to you but others use it more than you...",
  "Can you solve it? Forward I am heavy, backward I am not. What am I..."
 ],
 "Compounded": [
  "Can you solve it? A man pushes his car up to a hotel and shouts 'I'm b...",
  "Can you solve it? What can you catch but never throw...",
  "Can you solve it? I turn once, what is out will not get in; I turn aga...",
  "Can you solve it? The person who makes it sells it; the buyer never us...",
  "Can you solve it? What has 13 hearts but no other organs...",
  "Can you solve it? I am not alive but I grow; I don't have lungs but I...",
  "Can you solve it? What goes up but never comes down...",
  "Can you solve it? A box without hinges, key, or lid, yet golden treasu...",
  "Can you solve it? What is so fragile that saying its name breaks it...",
  "Can you solve it? I have no voice yet I speak to you; I tell of all th...",
  "Can you solve it? What invention lets you look right through a wall...",
  "Can you solve it? What has a thumb and four fingers but is not alive..."
 ],
 "Advanced": [
  "Can you solve it? I am the beginning of the end, and the end of time a...",
  "Can you solve it? What English word has three consecutive double lette...",
  "Can you solve it? Which word in the dictionary is spelled incorrectly...",
  "Can you solve it? What 5-letter word becomes shorter when you add two...",
  "Can you solve it? What occurs twice in a week, once in a year, but nev...",
  "Can you solve it? I am always coming but never arrive. What am I...",
  "Can you solve it? What has roots nobody sees, taller than trees, up ye...",
  "Can you solve it? The more there is, the less you see. What is it...",
  "Can you solve it? What can fill a room but takes up no space...",
  "Can you solve it? I have a neck but no head, two arms but no hands. Wh...",
  "Can you solve it? What word is pronounced the same if you take away fo..."
 ]
};
var DEMOKIND="solution-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Solve-It Study — "+safe+"\n"
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
    name:topic+' — solve-it challenge record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A solve-it challenge record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-can-you-solve-it-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-can-you-solve-it',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
