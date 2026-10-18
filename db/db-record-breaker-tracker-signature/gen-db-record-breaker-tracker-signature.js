(function(){'use strict';
/* JAH The Record Breaker Tracker Signature Database generator — jahdb-db-record-breaker-tracker-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RBTS-";
var FIELDS=["Speed Records","Size Records","Endurance Records"];
var TOPICS={
 "Speed Records": [
  "Bolt vs Next: 100m (Signature Edition) - Speed Records",
  "Phelps vs Ledecky: Pool GOATs (Signature Edition) - Speed Records",
  "Land vs Air Speed: Absolute (Signature Edition) - Speed Records",
  "Fastest Animal vs Machine: Cheetah (Signature Edition) - Speed Records",
  "Marathon: Kipchoge vs Next (Signature Edition) - Speed Records",
  "Swim vs Run: Speed (Signature Edition) - Speed Records",
  "Fastest Pitch vs Serve: Throw (Signature Edition) - Speed Records",
  "Ski vs Skate: Downhill (Signature Edition) - Speed Records",
  "Typing: Stenotype vs Keyboard (Signature Edition) - Speed Records",
  "Calculation: Human vs Machine (Signature Edition) - Speed Records"
 ],
 "Size Records": [
  "Tallest Building vs Next: Height (Signature Edition) - Size Records",
  "Biggest Animal vs Dinosaur: Size (Signature Edition) - Size Records",
  "Largest Tree vs Building: Tall Life (Signature Edition) - Size Records",
  "Biggest Ship vs Plane: Vessels (Signature Edition) - Size Records",
  "Longest Bridge vs Tunnel: Span (Signature Edition) - Size Records",
  "Biggest Diamond vs Pearl: Gems (Signature Edition) - Size Records",
  "Largest Desert vs Forest: Land (Signature Edition) - Size Records",
  "Deepest Dive vs Space: Extremes (Signature Edition) - Size Records",
  "Longest River vs Road: Lines (Signature Edition) - Size Records",
  "Heaviest vs Tallest: Human (Signature Edition) - Size Records"
 ],
 "Endurance Records": [
  "Longest Flight vs Drive: Distance (Signature Edition) - Endurance Records",
  "Longest Spaceflight vs Submarine: Isolated (Signature Edition) - Endurance Records",
  "Plank vs Wall Sit: Static (Signature Edition) - Endurance Records",
  "Free Dive vs Scuba: Depth Breath (Signature Edition) - Endurance Records",
  "Hot Dog vs Wings: Eating (Signature Edition) - Endurance Records",
  "Juggling vs Yo-Yo: Skill (Signature Edition) - Endurance Records",
  "Chess vs Go: Mind (Signature Edition) - Endurance Records",
  "Hula Hoop vs Jump Rope: Spin (Signature Edition) - Endurance Records",
  "Sleep Deprivation vs Awake: Rest (Signature Edition) - Endurance Records",
  "Cold vs Heat: Temperature (Signature Edition) - Endurance Records",
  "High Altitude vs Depth: Pressure (Signature Edition) - Endurance Records",
  "Longest Book vs Film: Epics (Signature Edition) - Endurance Records",
  "Marathon Gaming vs Speedrun: Play (Signature Edition) - Endurance Records",
  "Beard vs Hair: Growth (Signature Edition) - Endurance Records"
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
var gen={version:'jahdb-db-record-breaker-tracker-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-record-breaker-tracker-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
