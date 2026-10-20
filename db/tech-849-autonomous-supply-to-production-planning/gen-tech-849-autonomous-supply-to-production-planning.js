(function(){'use strict';
/* JAH The Autonomous Supply-to-Production Planning Database generator — jahdb-tech-849-autonomous-supply-to-production-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET849-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Autonomous Supply-to-Production Planning Is","The Current State of Autonomous Supply-to-Production Planning","Core Principles of Autonomous Supply-to-Production Planning","Key Vocabulary of Autonomous Supply-to-Production Planning","Why Autonomous Supply-to-Production Planning Matters"],"Compounded":["Piece 1 of Autonomous Supply-to-Production Planning: Process Tooling","Piece 2 of Autonomous Supply-to-Production Planning: Material Feedstock","Piece 3 of Autonomous Supply-to-Production Planning: Metrology","Piece 4 of Autonomous Supply-to-Production Planning: Control Software","Piece 5 of Autonomous Supply-to-Production Planning: Robotics and Handling","Piece 6 of Autonomous Supply-to-Production Planning: Quality System","Piece 7 of Autonomous Supply-to-Production Planning: Facility Infrastructure","Piece 8 of Autonomous Supply-to-Production Planning: Digital Twin","How the Pieces of Autonomous Supply-to-Production Planning Fit Together","Build Plan: Making Autonomous Supply-to-Production Planning Step by Step"],"Advanced":["The Working Autonomous Supply-to-Production Planning: What a Real Build Looks Like","Simulation Program: Modeling Autonomous Supply-to-Production Planning in Code","Testing and Verifying Autonomous Supply-to-Production Planning","Safety, Limits, and Responsible Use of Autonomous Supply-to-Production Planning","Scaling Autonomous Supply-to-Production Planning to Production","The Full Teaching Ladder for Autonomous Supply-to-Production Planning","Open Problems and Next Steps in Autonomous Supply-to-Production Planning"]};;
var DEMOKIND="autonomous supply-to-production planning record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# autonomous supply-to-production planning record planner — "+safe+"\n"
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
    name:topic+' — autonomous supply-to-production planning record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An autonomous supply-to-production planning record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-849-autonomous-supply-to-production-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-849-autonomous-supply-to-production-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
