(function(){'use strict';
/* JAH The Closed-Loop Geothermal Energy Systems Database generator — jahdb-tech-608-closed-loop-geothermal-energy-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET608-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Closed-Loop Geothermal Energy Systems Is","The Current State of Closed-Loop Geothermal Energy Systems","Core Principles of Closed-Loop Geothermal Energy Systems","Key Vocabulary of Closed-Loop Geothermal Energy Systems","Why Closed-Loop Geothermal Energy Systems Matters"],"Compounded":["Piece 1 of Closed-Loop Geothermal Energy Systems: Primary Conversion Unit","Piece 2 of Closed-Loop Geothermal Energy Systems: Fuel and Resource Supply","Piece 3 of Closed-Loop Geothermal Energy Systems: Thermal Management","Piece 4 of Closed-Loop Geothermal Energy Systems: Power Conditioning","Piece 5 of Closed-Loop Geothermal Energy Systems: Storage Buffer","Piece 6 of Closed-Loop Geothermal Energy Systems: Control and Dispatch Software","Piece 7 of Closed-Loop Geothermal Energy Systems: Safety and Containment","Piece 8 of Closed-Loop Geothermal Energy Systems: Grid Interconnection","How the Pieces of Closed-Loop Geothermal Energy Systems Fit Together","Build Plan: Making Closed-Loop Geothermal Energy Systems Step by Step"],"Advanced":["The Working Closed-Loop Geothermal Energy System: What a Real Build Looks Like","Simulation Program: Modeling Closed-Loop Geothermal Energy Systems in Code","Testing and Verifying Closed-Loop Geothermal Energy Systems","Safety, Limits, and Responsible Use of Closed-Loop Geothermal Energy Systems","Scaling Closed-Loop Geothermal Energy Systems to Production","The Full Teaching Ladder for Closed-Loop Geothermal Energy Systems","Open Problems and Next Steps in Closed-Loop Geothermal Energy Systems"]};;
var DEMOKIND="closed-loop geothermal energy system record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# closed-loop geothermal energy system record planner — "+safe+"\n"
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
    name:topic+' — closed-loop geothermal energy system record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A closed-loop geothermal energy system record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-608-closed-loop-geothermal-energy-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-608-closed-loop-geothermal-energy-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
