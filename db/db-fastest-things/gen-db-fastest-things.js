(function(){'use strict';
/* JAH The Fastest Things Database generator — jahdb-db-fastest-things-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FTT-";
var FIELDS=["Speed Foundations","Record Speeds","Extreme Velocity"];
var TOPICS={
 "Speed Foundations": [
  "Cheetah vs Greyhound: Sprinters - Speed Foundations",
  "Peregrine Falcon vs Common Swift: Sky Speed - Speed Foundations",
  "Sailfish vs Black Marlin: Ocean Sprinters - Speed Foundations",
  "Pronghorn vs Cheetah: Endurance vs Sprint - Speed Foundations",
  "Human Sprint vs Human Swim: Our Limits - Speed Foundations",
  "Horse vs Greyhound: Classic Racers - Speed Foundations",
  "Eagle vs Falcon: Raptor Styles - Speed Foundations",
  "Tuna vs Shark: Pelagic Cruisers - Speed Foundations",
  "Roadrunner vs Coyote: Cartoon Physics Check - Speed Foundations",
  "Kangaroo vs Ostrich: Hoppers vs Runners - Speed Foundations",
  "Dragonfly vs Housefly: Insect Aviators - Speed Foundations",
  "Hummingbird vs Swift: Small Wonders - Speed Foundations"
 ],
 "Record Speeds": [
  "Formula 1 vs Top Fuel Dragster: Acceleration Kings - Record Speeds",
  "Concorde vs Boeing 747: Airliner Eras - Record Speeds",
  "Bullet Train vs Maglev: Rail Futures - Record Speeds",
  "SR-71 vs MiG-25: Spy Plane Duel - Record Speeds",
  "Speed of Sound vs Speed of Light: Physics Limits - Record Speeds",
  "Rocket vs Jet: Getting Off Earth - Record Speeds",
  "F1 Pit Stop vs NASCAR Pit Stop: Speed of Service - Record Speeds",
  "Motorcycle vs Car: Two Wheels vs Four - Record Speeds",
  "Elevator vs Stairs: Vertical Commute - Record Speeds",
  "Submarine vs Speedboat: Water Speed - Record Speeds"
 ],
 "Extreme Velocity": [
  "Tornado vs Hurricane: Wind Extremes - Extreme Velocity",
  "Lightning vs Electricity in Wire: Spark Speed - Extreme Velocity",
  "Particle Accelerator vs Cosmic Ray: Tiny Speedsters - Extreme Velocity",
  "Thought vs Reflex: Neural Speed - Extreme Velocity",
  "Glacier vs Lava Flow: Slow vs Fast Geology - Extreme Velocity",
  "Growing Bamboo vs Growing Oak: Plant Speed - Extreme Velocity",
  "Internet Signal vs Courier Pigeon: Message Speed - Extreme Velocity",
  "Whip Crack vs Bullet: Supersonic Everyday - Extreme Velocity",
  "Falling Raindrop vs Hailstone: Sky Fallers - Extreme Velocity",
  "Evolution vs Selective Breeding: Change Speed - Extreme Velocity",
  "Heartbeat vs Hummingbird Wings: Living Rhythms - Extreme Velocity",
  "Continental Drift vs Fingernail Growth: Slow Motion - Extreme Velocity"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fastest Things Study — "+safe+"\n"
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
    name:topic+' — speed comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A speed comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"fastest-things-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-fastest-things-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-fastest-things',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
