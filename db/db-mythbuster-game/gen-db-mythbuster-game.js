(function(){'use strict';
/* JAH The Mythbuster Game Database Database generator — jahdb-db-mythbuster-game-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MYTBUSGAM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Myth: A dropped toast always lands butter-side down...",
  "Myth: Cell phones cause gas station fires...",
  "Myth: You can dodge a bullet after it's fired...",
  "Myth: Hair grows back thicker after shaving...",
  "Myth: Cracking knuckles causes arthritis...",
  "Myth: Lightning never strikes twice...",
  "Myth: Goldfish have 3-second memories...",
  "Myth: Bulls hate the color red...",
  "Myth: Eating carrots gives night vision...",
  "Myth: A penny from a skyscraper can kill...",
  "Myth: Humans use only 10% of their brains..."
 ],
 "Compounded": [
  "Myth: A duck's quack doesn't echo...",
  "Myth: You can pull a tablecloth without moving dishes...",
  "Myth: Talking to plants helps them grow...",
  "Myth: A watched pot never boils...",
  "Myth: Sugar makes kids hyper...",
  "Myth: Lightning rods attract lightning...",
  "Myth: You can start a fire with ice...",
  "Myth: Deoxygenated blood is blue...",
  "Myth: The five-second rule is safe...",
  "Myth: Microwaves destroy nutrients...",
  "Myth: Ostriches bury their heads...",
  "Myth: Yawns spread only by sight..."
 ],
 "Advanced": [
  "Myth: The Mpemba effect: hot water freezes faster...",
  "Myth: Glass flows over centuries...",
  "Myth: You can sneeze with your eyes open...",
  "Myth: Alcohol kills brain cells...",
  "Myth: Sharks must swim to breathe...",
  "Myth: The Coriolis effect spins drains...",
  "Myth: Vitamin C prevents colds...",
  "Myth: Full moons raise crime...",
  "Myth: Bananas are radioactive enough to matter...",
  "Myth: You can hear the ocean in a shell...",
  "Myth: Lightning heats air hotter than the Sun's surface..."
 ]
};
var DEMOKIND="myth-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mythbuster Study — "+safe+"\n"
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
    name:topic+' — myth test record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A myth test record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-mythbuster-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mythbuster-game',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
