(function(){'use strict';
/* JAH The Autonomous Renewable Microgrids Database generator — jahdb-tech-624-autonomous-renewable-microgrids-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET624-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Autonomous Renewable Microgrids Is","The Current State of Autonomous Renewable Microgrids","Core Principles of Autonomous Renewable Microgrids","Key Vocabulary of Autonomous Renewable Microgrids","Why Autonomous Renewable Microgrids Matters"],"Compounded":["Piece 1 of Autonomous Renewable Microgrids: Primary Conversion Unit","Piece 2 of Autonomous Renewable Microgrids: Fuel and Resource Supply","Piece 3 of Autonomous Renewable Microgrids: Thermal Management","Piece 4 of Autonomous Renewable Microgrids: Power Conditioning","Piece 5 of Autonomous Renewable Microgrids: Storage Buffer","Piece 6 of Autonomous Renewable Microgrids: Control and Dispatch Software","Piece 7 of Autonomous Renewable Microgrids: Safety and Containment","Piece 8 of Autonomous Renewable Microgrids: Grid Interconnection","How the Pieces of Autonomous Renewable Microgrids Fit Together","Build Plan: Making Autonomous Renewable Microgrids Step by Step"],"Advanced":["The Working Autonomous Renewable Microgrid: What a Real Build Looks Like","Simulation Program: Modeling Autonomous Renewable Microgrids in Code","Testing and Verifying Autonomous Renewable Microgrids","Safety, Limits, and Responsible Use of Autonomous Renewable Microgrids","Scaling Autonomous Renewable Microgrids to Production","The Full Teaching Ladder for Autonomous Renewable Microgrids","Open Problems and Next Steps in Autonomous Renewable Microgrids"]};;
var DEMOKIND="autonomous renewable microgrid record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# autonomous renewable microgrid record planner — "+safe+"\n"
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
    name:topic+' — autonomous renewable microgrid record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An autonomous renewable microgrid record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-624-autonomous-renewable-microgrids-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-624-autonomous-renewable-microgrids',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
