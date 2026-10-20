(function(){'use strict';
/* JAH The Autonomous Interplanetary Navigation Systems Database generator — jahdb-tech-720-autonomous-interplanetary-navigation-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET720-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Autonomous Interplanetary Navigation Systems Is","The Current State of Autonomous Interplanetary Navigation Systems","Core Principles of Autonomous Interplanetary Navigation Systems","Key Vocabulary of Autonomous Interplanetary Navigation Systems","Why Autonomous Interplanetary Navigation Systems Matters"],"Compounded":["Piece 1 of Autonomous Interplanetary Navigation Systems: Launch and Transit","Piece 2 of Autonomous Interplanetary Navigation Systems: Power System","Piece 3 of Autonomous Interplanetary Navigation Systems: Thermal Control","Piece 4 of Autonomous Interplanetary Navigation Systems: Communications","Piece 5 of Autonomous Interplanetary Navigation Systems: Guidance and Navigation","Piece 6 of Autonomous Interplanetary Navigation Systems: Platform Structure","Piece 7 of Autonomous Interplanetary Navigation Systems: Mission Core Systems","Piece 8 of Autonomous Interplanetary Navigation Systems: Ground Operations","How the Pieces of Autonomous Interplanetary Navigation Systems Fit Together","Build Plan: Making Autonomous Interplanetary Navigation Systems Step by Step"],"Advanced":["The Working Autonomous Interplanetary Navigation System: What a Real Build Looks Like","Simulation Program: Modeling Autonomous Interplanetary Navigation Systems in Code","Testing and Verifying Autonomous Interplanetary Navigation Systems","Safety, Limits, and Responsible Use of Autonomous Interplanetary Navigation Systems","Scaling Autonomous Interplanetary Navigation Systems to Production","The Full Teaching Ladder for Autonomous Interplanetary Navigation Systems","Open Problems and Next Steps in Autonomous Interplanetary Navigation Systems"]};;
var DEMOKIND="autonomous interplanetary navigation system record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# autonomous interplanetary navigation system record planner — "+safe+"\n"
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
    name:topic+' — autonomous interplanetary navigation system record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An autonomous interplanetary navigation system record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-720-autonomous-interplanetary-navigation-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-720-autonomous-interplanetary-navigation-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
