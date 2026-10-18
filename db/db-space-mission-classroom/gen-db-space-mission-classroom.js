(function(){'use strict';
/* JAH The Space Mission Classroom generator — jahdb-db-space-mission-classroom-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPMC-";
var FIELDS=["Solar System","Spacecraft","Missions"];
var TOPICS={
 "Solar System": [
  "Mission Brief: Scale of Space - Solar System",
  "The Sun: Our Star - Solar System",
  "Mercury: The Scorched World - Solar System",
  "Venus: The Runaway Greenhouse - Solar System",
  "Earth: The Goldilocks Planet - Solar System",
  "The Moon: Our Neighbor - Solar System",
  "Mars: The Next Frontier - Solar System",
  "Jupiter: The Giant Shield - Solar System",
  "Saturn: Lord of the Rings - Solar System",
  "Ice Giants: Uranus and Neptune - Solar System",
  "Asteroids, Comets, Meteors - Solar System",
  "The Sun's Family Portrait - Solar System"
 ],
 "Spacecraft": [
  "Rockets: Controlled Explosions - Spacecraft",
  "Orbits: Falling and Missing - Spacecraft",
  "Life Support: Air, Water, Everything - Spacecraft",
  "Spacesuits: Personal Spacecraft - Spacecraft",
  "Satellites: Eyes in the Sky - Spacecraft",
  "Probes: Robots Go First - Spacecraft",
  "Space Stations: Homes in Orbit - Spacecraft",
  "Landers and Rovers - Spacecraft",
  "Telescopes: Time Machines - Spacecraft",
  "Propulsion Futures - Spacecraft",
  "Docking: Meeting in Orbit - Spacecraft",
  "Reentry: Coming Home Hot - Spacecraft"
 ],
 "Missions": [
  "Apollo: The Moon Shot - Missions",
  "Artemis: Back to Stay - Missions",
  "Mars Rovers: Geologists on Wheels - Missions",
  "Voyager: The Grand Tour - Missions",
  "ISS: The Orbital Lab - Missions",
  "JWST: First Light - Missions",
  "DART: Moving an Asteroid - Missions",
  "Commercial Space: The New Players - Missions",
  "Your Mission: What's Next - Missions",
  "Cassini: Saturn's Grand Tour - Missions"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Space Mission Study — "+safe+"\n"
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
    name:topic+' — space lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A space lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"space-mission-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-space-mission-classroom-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-space-mission-classroom',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
