(function(){'use strict';
/* JAH The Self-Replicating Industrial Machine Systems Database generator — jahdb-tech-827-self-replicating-industrial-machine-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET827-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Self-Replicating Industrial Machine Systems Is","The Current State of Self-Replicating Industrial Machine Systems","Core Principles of Self-Replicating Industrial Machine Systems","Key Vocabulary of Self-Replicating Industrial Machine Systems","Why Self-Replicating Industrial Machine Systems Matters"],"Compounded":["Piece 1 of Self-Replicating Industrial Machine Systems: Process Tooling","Piece 2 of Self-Replicating Industrial Machine Systems: Material Feedstock","Piece 3 of Self-Replicating Industrial Machine Systems: Metrology","Piece 4 of Self-Replicating Industrial Machine Systems: Control Software","Piece 5 of Self-Replicating Industrial Machine Systems: Robotics and Handling","Piece 6 of Self-Replicating Industrial Machine Systems: Quality System","Piece 7 of Self-Replicating Industrial Machine Systems: Facility Infrastructure","Piece 8 of Self-Replicating Industrial Machine Systems: Digital Twin","How the Pieces of Self-Replicating Industrial Machine Systems Fit Together","Build Plan: Making Self-Replicating Industrial Machine Systems Step by Step"],"Advanced":["The Working Self-Replicating Industrial Machine System: What a Real Build Looks Like","Simulation Program: Modeling Self-Replicating Industrial Machine Systems in Code","Testing and Verifying Self-Replicating Industrial Machine Systems","Safety, Limits, and Responsible Use of Self-Replicating Industrial Machine Systems","Scaling Self-Replicating Industrial Machine Systems to Production","The Full Teaching Ladder for Self-Replicating Industrial Machine Systems","Open Problems and Next Steps in Self-Replicating Industrial Machine Systems"]};;
var DEMOKIND="self-replicating industrial machine system record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# self-replicating industrial machine system record planner — "+safe+"\n"
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
    name:topic+' — self-replicating industrial machine system record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A self-replicating industrial machine system record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-827-self-replicating-industrial-machine-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-827-self-replicating-industrial-machine-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
