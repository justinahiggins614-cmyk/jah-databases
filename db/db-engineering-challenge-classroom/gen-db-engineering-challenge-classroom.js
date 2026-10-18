(function(){'use strict';
/* JAH The Engineering Challenge Classroom generator — jahdb-db-engineering-challenge-classroom-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EGCC-";
var FIELDS=["Design Process","Structures","Systems"];
var TOPICS={
 "Design Process": [
  "Think Like an Engineer - Design Process",
  "Constraints Are the Design - Design Process",
  "Brainstorming That Works - Design Process",
  "Prototyping: Fail Fast, Learn Faster - Design Process",
  "Testing: Break It on Purpose - Design Process",
  "Iteration: Version N+1 - Design Process",
  "Trade-offs: No Free Lunch - Design Process",
  "Safety Factors: Engineered Humility - Design Process",
  "Sketching for Engineers - Design Process",
  "Measurement: Trust, Then Verify - Design Process",
  "Challenge: Paper Bridge - Design Process",
  "Challenge: Egg Drop - Design Process"
 ],
 "Structures": [
  "Bridges: Spanning the Gap - Structures",
  "Towers: Standing Tall - Structures",
  "Domes and Arches - Structures",
  "Challenge: Spaghetti Tower - Structures",
  "Trusses: Triangles at Work - Structures",
  "Foundations: What Holds Everything - Structures",
  "Materials: Choose Wisely - Structures",
  "Load Paths: Follow the Force - Structures",
  "Challenge: Cardboard Chair - Structures",
  "Mechanisms: Levers and Linkages - Structures",
  "Challenge: Straw Bridge - Structures",
  "Cantilevers: Defying Gravity - Structures"
 ],
 "Systems": [
  "Challenge: Marble Run - Systems",
  "Water Filters: Clean by Design - Systems",
  "Challenge: Solar Oven - Systems",
  "Wind Power: Catching Air - Systems",
  "Challenge: Catapult - Systems",
  "Simple Machines, Real Systems - Systems",
  "Feedback: Systems That Steer - Systems",
  "Challenge: Rube Goldberg - Systems",
  "Capstone: Design for Someone Real - Systems",
  "Challenge: Water Clock - Systems"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Engineering Challenge Study — "+safe+"\n"
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
    name:topic+' — engineering lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A engineering lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"engineering-challenge-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-engineering-challenge-classroom-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-engineering-challenge-classroom',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
