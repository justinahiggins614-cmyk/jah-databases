(function(){'use strict';
/* JAH The Autonomous Building Energy Management Database generator — jahdb-tech-857-autonomous-building-energy-management-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET857-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Autonomous Building Energy Management Is","The Current State of Autonomous Building Energy Management","Core Principles of Autonomous Building Energy Management","Key Vocabulary of Autonomous Building Energy Management","Why Autonomous Building Energy Management Matters"],"Compounded":["Piece 1 of Autonomous Building Energy Management: Structural System","Piece 2 of Autonomous Building Energy Management: Robotic Construction Equipment","Piece 3 of Autonomous Building Energy Management: Materials Supply","Piece 4 of Autonomous Building Energy Management: Building Intelligence","Piece 5 of Autonomous Building Energy Management: Energy System","Piece 6 of Autonomous Building Energy Management: Water and Waste","Piece 7 of Autonomous Building Energy Management: Mobility Integration","Piece 8 of Autonomous Building Energy Management: Resilience Engineering","How the Pieces of Autonomous Building Energy Management Fit Together","Build Plan: Making Autonomous Building Energy Management Step by Step"],"Advanced":["The Working Autonomous Building Energy Management: What a Real Build Looks Like","Simulation Program: Modeling Autonomous Building Energy Management in Code","Testing and Verifying Autonomous Building Energy Management","Safety, Limits, and Responsible Use of Autonomous Building Energy Management","Scaling Autonomous Building Energy Management to Production","The Full Teaching Ladder for Autonomous Building Energy Management","Open Problems and Next Steps in Autonomous Building Energy Management"]};;
var DEMOKIND="autonomous building energy management record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# autonomous building energy management record planner — "+safe+"\n"
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
    name:topic+' — autonomous building energy management record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An autonomous building energy management record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-857-autonomous-building-energy-management-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-857-autonomous-building-energy-management',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
