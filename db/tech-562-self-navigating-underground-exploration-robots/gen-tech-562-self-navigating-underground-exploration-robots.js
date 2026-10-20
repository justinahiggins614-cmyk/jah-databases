(function(){'use strict';
/* JAH The Self-Navigating Underground Exploration Robots Database generator — jahdb-tech-562-self-navigating-underground-exploration-robots-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET562-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Self-Navigating Underground Exploration Robots Is","The Current State of Self-Navigating Underground Exploration Robots","Core Principles of Self-Navigating Underground Exploration Robots","Key Vocabulary of Self-Navigating Underground Exploration Robots","Why Self-Navigating Underground Exploration Robots Matters"],"Compounded":["Piece 1 of Self-Navigating Underground Exploration Robots: Mobility Platform","Piece 2 of Self-Navigating Underground Exploration Robots: Power and Energy System","Piece 3 of Self-Navigating Underground Exploration Robots: Perception Suite","Piece 4 of Self-Navigating Underground Exploration Robots: Onboard Compute","Piece 5 of Self-Navigating Underground Exploration Robots: Manipulation Hardware","Piece 6 of Self-Navigating Underground Exploration Robots: Communication Link","Piece 7 of Self-Navigating Underground Exploration Robots: Control Software Stack","Piece 8 of Self-Navigating Underground Exploration Robots: Safety and Recovery Systems","How the Pieces of Self-Navigating Underground Exploration Robots Fit Together","Build Plan: Making Self-Navigating Underground Exploration Robots Step by Step"],"Advanced":["The Working Self-Navigating Underground Exploration Robot: What a Real Build Looks Like","Simulation Program: Modeling Self-Navigating Underground Exploration Robots in Code","Testing and Verifying Self-Navigating Underground Exploration Robots","Safety, Limits, and Responsible Use of Self-Navigating Underground Exploration Robots","Scaling Self-Navigating Underground Exploration Robots to Production","The Full Teaching Ladder for Self-Navigating Underground Exploration Robots","Open Problems and Next Steps in Self-Navigating Underground Exploration Robots"]};;
var DEMOKIND="self-navigating underground exploration robot record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# self-navigating underground exploration robot record planner — "+safe+"\n"
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
    name:topic+' — self-navigating underground exploration robot record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A self-navigating underground exploration robot record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-562-self-navigating-underground-exploration-robots-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-562-self-navigating-underground-exploration-robots',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
