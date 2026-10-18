(function(){'use strict';
/* JAH The Record Breaker Tracker Database generator — jahdb-db-record-breaker-tracker-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RBT-";
var FIELDS=["Speed Records","Size Records","Endurance Records"];
var TOPICS={
 "Speed Records": [
  "Bolt vs Next: 100m - Speed Records",
  "Phelps vs Ledecky: Pool GOATs - Speed Records",
  "Land vs Air Speed: Absolute - Speed Records",
  "Fastest Animal vs Machine: Cheetah - Speed Records",
  "Marathon: Kipchoge vs Next - Speed Records",
  "Swim vs Run: Speed - Speed Records",
  "Fastest Pitch vs Serve: Throw - Speed Records",
  "Ski vs Skate: Downhill - Speed Records",
  "Typing: Stenotype vs Keyboard - Speed Records",
  "Calculation: Human vs Machine - Speed Records"
 ],
 "Size Records": [
  "Tallest Building vs Next: Height - Size Records",
  "Biggest Animal vs Dinosaur: Size - Size Records",
  "Largest Tree vs Building: Tall Life - Size Records",
  "Biggest Ship vs Plane: Vessels - Size Records",
  "Longest Bridge vs Tunnel: Span - Size Records",
  "Biggest Diamond vs Pearl: Gems - Size Records",
  "Largest Desert vs Forest: Land - Size Records",
  "Deepest Dive vs Space: Extremes - Size Records",
  "Longest River vs Road: Lines - Size Records",
  "Heaviest vs Tallest: Human - Size Records"
 ],
 "Endurance Records": [
  "Longest Flight vs Drive: Distance - Endurance Records",
  "Longest Spaceflight vs Submarine: Isolated - Endurance Records",
  "Plank vs Wall Sit: Static - Endurance Records",
  "Free Dive vs Scuba: Depth Breath - Endurance Records",
  "Hot Dog vs Wings: Eating - Endurance Records",
  "Juggling vs Yo-Yo: Skill - Endurance Records",
  "Chess vs Go: Mind - Endurance Records",
  "Hula Hoop vs Jump Rope: Spin - Endurance Records",
  "Sleep Deprivation vs Awake: Rest - Endurance Records",
  "Cold vs Heat: Temperature - Endurance Records",
  "High Altitude vs Depth: Pressure - Endurance Records",
  "Longest Book vs Film: Epics - Endurance Records",
  "Marathon Gaming vs Speedrun: Play - Endurance Records",
  "Beard vs Hair: Growth - Endurance Records"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Record Breaker Study — "+safe+"\n"
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
    name:topic+' — record showdown record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A record showdown record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"record-breaker-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-record-breaker-tracker-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-record-breaker-tracker',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
