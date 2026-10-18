(function(){'use strict';
/* JAH The Mini Robot Challenge Database generator — jahdb-db-mini-robot-challenge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MRCH-";
var FIELDS=["Mini Robot Foundations", "The Challenges", "Mini Robot Mastery"];
var TOPICS={"Mini Robot Foundations": ["Why Small Robots", "How Robots Work", "The Microcontroller Brain", "Sensors at Small Scale", "Tiny Actuators", "Power for Minis", "Programming Basics", "Building Your First Bot", "The Builder's Toolkit", "The Maker Community", "Safety with Small Bots"], "The Challenges": ["The Line Follower", "Maze Solvers", "Sumo Bots", "Mini Drag Racers", "Obstacle Courses", "The Egg Race", "Swarm Challenges", "Art Bots", "Rescue Scenarios", "The Innovation Challenge", "Speed Builds", "The Grand Challenge"], "Mini Robot Mastery": ["Advanced Control", "Custom PCB Design", "3D Printing for Bots", "Competition Strategy", "Teaching Robotics", "Open Source Bots", "Research Frontiers", "The Business of Bots", "Ethics of Small Robots", "The Tiny Philosophy", "The Bot Legacy"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# minibot — "+safe+"\n"
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
    name:topic+' — mini robot challenge record',
    title:topic,
    description:"SAMPLE RECORD (generated — structural sample). A mini robot challenge record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"topic-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-db-mini-robot-challenge-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("db-mini-robot-challenge",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
