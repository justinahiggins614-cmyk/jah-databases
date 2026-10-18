(function(){'use strict';
/* JAH The Engineering Challenge Classroom generator — jahdb-db-engineering-challenge-classroom-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EGCCS-";
var FIELDS=["Design Process","Structures","Systems"];
var TOPICS={
 "Design Process": [
  "Think Like an Engineer (Signature Edition) - Design Process",
  "Constraints Are the Design (Signature Edition) - Design Process",
  "Brainstorming That Works (Signature Edition) - Design Process",
  "Prototyping: Fail Fast, Learn Faster (Signature Edition) - Design Process",
  "Testing: Break It on Purpose (Signature Edition) - Design Process",
  "Iteration: Version N+1 (Signature Edition) - Design Process",
  "Trade-offs: No Free Lunch (Signature Edition) - Design Process",
  "Safety Factors: Engineered Humility (Signature Edition) - Design Process",
  "Sketching for Engineers (Signature Edition) - Design Process",
  "Measurement: Trust, Then Verify (Signature Edition) - Design Process",
  "Challenge: Paper Bridge (Signature Edition) - Design Process",
  "Challenge: Egg Drop (Signature Edition) - Design Process"
 ],
 "Structures": [
  "Bridges: Spanning the Gap (Signature Edition) - Structures",
  "Towers: Standing Tall (Signature Edition) - Structures",
  "Domes and Arches (Signature Edition) - Structures",
  "Challenge: Spaghetti Tower (Signature Edition) - Structures",
  "Trusses: Triangles at Work (Signature Edition) - Structures",
  "Foundations: What Holds Everything (Signature Edition) - Structures",
  "Materials: Choose Wisely (Signature Edition) - Structures",
  "Load Paths: Follow the Force (Signature Edition) - Structures",
  "Challenge: Cardboard Chair (Signature Edition) - Structures",
  "Mechanisms: Levers and Linkages (Signature Edition) - Structures",
  "Challenge: Straw Bridge (Signature Edition) - Structures",
  "Cantilevers: Defying Gravity (Signature Edition) - Structures"
 ],
 "Systems": [
  "Challenge: Marble Run (Signature Edition) - Systems",
  "Water Filters: Clean by Design (Signature Edition) - Systems",
  "Challenge: Solar Oven (Signature Edition) - Systems",
  "Wind Power: Catching Air (Signature Edition) - Systems",
  "Challenge: Catapult (Signature Edition) - Systems",
  "Simple Machines, Real Systems (Signature Edition) - Systems",
  "Feedback: Systems That Steer (Signature Edition) - Systems",
  "Challenge: Rube Goldberg (Signature Edition) - Systems",
  "Capstone: Design for Someone Real (Signature Edition) - Systems",
  "Challenge: Water Clock (Signature Edition) - Systems"
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
var gen={version:'jahdb-db-engineering-challenge-classroom-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-engineering-challenge-classroom-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
