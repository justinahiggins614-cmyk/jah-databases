(function(){'use strict';
/* JAH The Autonomous Precision Assembly Factories Database generator — jahdb-tech-574-autonomous-precision-assembly-factories-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET574-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Autonomous Precision Assembly Factories Is","The Current State of Autonomous Precision Assembly Factories","Core Principles of Autonomous Precision Assembly Factories","Key Vocabulary of Autonomous Precision Assembly Factories","Why Autonomous Precision Assembly Factories Matters"],"Compounded":["Piece 1 of Autonomous Precision Assembly Factories: Mobility Platform","Piece 2 of Autonomous Precision Assembly Factories: Power and Energy System","Piece 3 of Autonomous Precision Assembly Factories: Perception Suite","Piece 4 of Autonomous Precision Assembly Factories: Onboard Compute","Piece 5 of Autonomous Precision Assembly Factories: Manipulation Hardware","Piece 6 of Autonomous Precision Assembly Factories: Communication Link","Piece 7 of Autonomous Precision Assembly Factories: Control Software Stack","Piece 8 of Autonomous Precision Assembly Factories: Safety and Recovery Systems","How the Pieces of Autonomous Precision Assembly Factories Fit Together","Build Plan: Making Autonomous Precision Assembly Factories Step by Step"],"Advanced":["The Working Autonomous Precision Assembly Factory: What a Real Build Looks Like","Simulation Program: Modeling Autonomous Precision Assembly Factories in Code","Testing and Verifying Autonomous Precision Assembly Factories","Safety, Limits, and Responsible Use of Autonomous Precision Assembly Factories","Scaling Autonomous Precision Assembly Factories to Production","The Full Teaching Ladder for Autonomous Precision Assembly Factories","Open Problems and Next Steps in Autonomous Precision Assembly Factories"]};;
var DEMOKIND="autonomous precision assembly factory record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# autonomous precision assembly factory record planner — "+safe+"\n"
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
    name:topic+' — autonomous precision assembly factory record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An autonomous precision assembly factory record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-574-autonomous-precision-assembly-factories-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-574-autonomous-precision-assembly-factories',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
