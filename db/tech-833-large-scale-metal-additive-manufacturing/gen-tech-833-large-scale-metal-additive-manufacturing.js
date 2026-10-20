(function(){'use strict';
/* JAH The Large-Scale Metal Additive Manufacturing Database generator — jahdb-tech-833-large-scale-metal-additive-manufacturing-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET833-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Large-Scale Metal Additive Manufacturing Is","The Current State of Large-Scale Metal Additive Manufacturing","Core Principles of Large-Scale Metal Additive Manufacturing","Key Vocabulary of Large-Scale Metal Additive Manufacturing","Why Large-Scale Metal Additive Manufacturing Matters"],"Compounded":["Piece 1 of Large-Scale Metal Additive Manufacturing: Process Tooling","Piece 2 of Large-Scale Metal Additive Manufacturing: Material Feedstock","Piece 3 of Large-Scale Metal Additive Manufacturing: Metrology","Piece 4 of Large-Scale Metal Additive Manufacturing: Control Software","Piece 5 of Large-Scale Metal Additive Manufacturing: Robotics and Handling","Piece 6 of Large-Scale Metal Additive Manufacturing: Quality System","Piece 7 of Large-Scale Metal Additive Manufacturing: Facility Infrastructure","Piece 8 of Large-Scale Metal Additive Manufacturing: Digital Twin","How the Pieces of Large-Scale Metal Additive Manufacturing Fit Together","Build Plan: Making Large-Scale Metal Additive Manufacturing Step by Step"],"Advanced":["The Working Large-Scale Metal Additive Manufacturing: What a Real Build Looks Like","Simulation Program: Modeling Large-Scale Metal Additive Manufacturing in Code","Testing and Verifying Large-Scale Metal Additive Manufacturing","Safety, Limits, and Responsible Use of Large-Scale Metal Additive Manufacturing","Scaling Large-Scale Metal Additive Manufacturing to Production","The Full Teaching Ladder for Large-Scale Metal Additive Manufacturing","Open Problems and Next Steps in Large-Scale Metal Additive Manufacturing"]};;
var DEMOKIND="large-scale metal additive manufacturing record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# large-scale metal additive manufacturing record planner — "+safe+"\n"
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
    name:topic+' — large-scale metal additive manufacturing record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A large-scale metal additive manufacturing record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-833-large-scale-metal-additive-manufacturing-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-833-large-scale-metal-additive-manufacturing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
