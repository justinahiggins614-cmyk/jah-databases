(function(){'use strict';
/* JAH The Fastest Things Signature Database generator — jahdb-db-fastest-things-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FSTS-";
var FIELDS=["Speed Foundations","Record Speeds","Extreme Velocity"];
var TOPICS={
 "Speed Foundations": [
  "Cheetah vs Greyhound: Sprinters (Signature Edition) - Speed Foundations",
  "Peregrine Falcon vs Common Swift: Sky Speed (Signature Edition) - Speed Foundations",
  "Sailfish vs Black Marlin: Ocean Sprinters (Signature Edition) - Speed Foundations",
  "Pronghorn vs Cheetah: Endurance vs Sprint (Signature Edition) - Speed Foundations",
  "Human Sprint vs Human Swim: Our Limits (Signature Edition) - Speed Foundations",
  "Horse vs Greyhound: Classic Racers (Signature Edition) - Speed Foundations",
  "Eagle vs Falcon: Raptor Styles (Signature Edition) - Speed Foundations",
  "Tuna vs Shark: Pelagic Cruisers (Signature Edition) - Speed Foundations",
  "Roadrunner vs Coyote: Cartoon Physics Check (Signature Edition) - Speed Foundations",
  "Kangaroo vs Ostrich: Hoppers vs Runners (Signature Edition) - Speed Foundations",
  "Dragonfly vs Housefly: Insect Aviators (Signature Edition) - Speed Foundations",
  "Hummingbird vs Swift: Small Wonders (Signature Edition) - Speed Foundations"
 ],
 "Record Speeds": [
  "Formula 1 vs Top Fuel Dragster: Acceleration Kings (Signature Edition) - Record Speeds",
  "Concorde vs Boeing 747: Airliner Eras (Signature Edition) - Record Speeds",
  "Bullet Train vs Maglev: Rail Futures (Signature Edition) - Record Speeds",
  "SR-71 vs MiG-25: Spy Plane Duel (Signature Edition) - Record Speeds",
  "Speed of Sound vs Speed of Light: Physics Limits (Signature Edition) - Record Speeds",
  "Rocket vs Jet: Getting Off Earth (Signature Edition) - Record Speeds",
  "F1 Pit Stop vs NASCAR Pit Stop: Speed of Service (Signature Edition) - Record Speeds",
  "Motorcycle vs Car: Two Wheels vs Four (Signature Edition) - Record Speeds",
  "Elevator vs Stairs: Vertical Commute (Signature Edition) - Record Speeds",
  "Submarine vs Speedboat: Water Speed (Signature Edition) - Record Speeds"
 ],
 "Extreme Velocity": [
  "Tornado vs Hurricane: Wind Extremes (Signature Edition) - Extreme Velocity",
  "Lightning vs Electricity in Wire: Spark Speed (Signature Edition) - Extreme Velocity",
  "Particle Accelerator vs Cosmic Ray: Tiny Speedsters (Signature Edition) - Extreme Velocity",
  "Thought vs Reflex: Neural Speed (Signature Edition) - Extreme Velocity",
  "Glacier vs Lava Flow: Slow vs Fast Geology (Signature Edition) - Extreme Velocity",
  "Growing Bamboo vs Growing Oak: Plant Speed (Signature Edition) - Extreme Velocity",
  "Internet Signal vs Courier Pigeon: Message Speed (Signature Edition) - Extreme Velocity",
  "Whip Crack vs Bullet: Supersonic Everyday (Signature Edition) - Extreme Velocity",
  "Falling Raindrop vs Hailstone: Sky Fallers (Signature Edition) - Extreme Velocity",
  "Evolution vs Selective Breeding: Change Speed (Signature Edition) - Extreme Velocity",
  "Heartbeat vs Hummingbird Wings: Living Rhythms (Signature Edition) - Extreme Velocity",
  "Continental Drift vs Fingernail Growth: Slow Motion (Signature Edition) - Extreme Velocity"
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
var gen={version:'jahdb-db-fastest-things-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-fastest-things-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
