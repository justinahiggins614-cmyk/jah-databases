(function(){'use strict';
/* JAH The Thorium-Based Nuclear Energy Systems Database generator — jahdb-tech-604-thorium-based-nuclear-energy-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET604-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Thorium-Based Nuclear Energy Systems Is","The Current State of Thorium-Based Nuclear Energy Systems","Core Principles of Thorium-Based Nuclear Energy Systems","Key Vocabulary of Thorium-Based Nuclear Energy Systems","Why Thorium-Based Nuclear Energy Systems Matters"],"Compounded":["Piece 1 of Thorium-Based Nuclear Energy Systems: Primary Conversion Unit","Piece 2 of Thorium-Based Nuclear Energy Systems: Fuel and Resource Supply","Piece 3 of Thorium-Based Nuclear Energy Systems: Thermal Management","Piece 4 of Thorium-Based Nuclear Energy Systems: Power Conditioning","Piece 5 of Thorium-Based Nuclear Energy Systems: Storage Buffer","Piece 6 of Thorium-Based Nuclear Energy Systems: Control and Dispatch Software","Piece 7 of Thorium-Based Nuclear Energy Systems: Safety and Containment","Piece 8 of Thorium-Based Nuclear Energy Systems: Grid Interconnection","How the Pieces of Thorium-Based Nuclear Energy Systems Fit Together","Build Plan: Making Thorium-Based Nuclear Energy Systems Step by Step"],"Advanced":["The Working Thorium-Based Nuclear Energy System: What a Real Build Looks Like","Simulation Program: Modeling Thorium-Based Nuclear Energy Systems in Code","Testing and Verifying Thorium-Based Nuclear Energy Systems","Safety, Limits, and Responsible Use of Thorium-Based Nuclear Energy Systems","Scaling Thorium-Based Nuclear Energy Systems to Production","The Full Teaching Ladder for Thorium-Based Nuclear Energy Systems","Open Problems and Next Steps in Thorium-Based Nuclear Energy Systems"]};;
var DEMOKIND="thorium-based nuclear energy system record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# thorium-based nuclear energy system record planner — "+safe+"\n"
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
    name:topic+' — thorium-based nuclear energy system record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A thorium-based nuclear energy system record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-604-thorium-based-nuclear-energy-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-604-thorium-based-nuclear-energy-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
