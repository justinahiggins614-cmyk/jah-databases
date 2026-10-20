(function(){'use strict';
/* JAH The Artificial Pancreas Closed-Loop Systems Database generator — jahdb-tech-630-artificial-pancreas-closed-loop-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET630-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Artificial Pancreas Closed-Loop Systems Is","The Current State of Artificial Pancreas Closed-Loop Systems","Core Principles of Artificial Pancreas Closed-Loop Systems","Key Vocabulary of Artificial Pancreas Closed-Loop Systems","Why Artificial Pancreas Closed-Loop Systems Matters"],"Compounded":["Piece 1 of Artificial Pancreas Closed-Loop Systems: Diagnostic Sensing","Piece 2 of Artificial Pancreas Closed-Loop Systems: Therapeutic Mechanism","Piece 3 of Artificial Pancreas Closed-Loop Systems: Delivery System","Piece 4 of Artificial Pancreas Closed-Loop Systems: Patient Monitoring","Piece 5 of Artificial Pancreas Closed-Loop Systems: Data and Decision Platform","Piece 6 of Artificial Pancreas Closed-Loop Systems: Manufacturing Line","Piece 7 of Artificial Pancreas Closed-Loop Systems: Safety and Trial Evidence","Piece 8 of Artificial Pancreas Closed-Loop Systems: Care Integration","How the Pieces of Artificial Pancreas Closed-Loop Systems Fit Together","Build Plan: Making Artificial Pancreas Closed-Loop Systems Step by Step"],"Advanced":["The Working Artificial Pancreas Closed-Loop System: What a Real Build Looks Like","Simulation Program: Modeling Artificial Pancreas Closed-Loop Systems in Code","Testing and Verifying Artificial Pancreas Closed-Loop Systems","Safety, Limits, and Responsible Use of Artificial Pancreas Closed-Loop Systems","Scaling Artificial Pancreas Closed-Loop Systems to Production","The Full Teaching Ladder for Artificial Pancreas Closed-Loop Systems","Open Problems and Next Steps in Artificial Pancreas Closed-Loop Systems"]};;
var DEMOKIND="artificial pancreas closed-loop system record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# artificial pancreas closed-loop system record planner — "+safe+"\n"
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
    name:topic+' — artificial pancreas closed-loop system record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An artificial pancreas closed-loop system record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-630-artificial-pancreas-closed-loop-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-630-artificial-pancreas-closed-loop-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
