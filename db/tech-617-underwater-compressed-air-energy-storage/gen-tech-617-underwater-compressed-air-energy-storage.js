(function(){'use strict';
/* JAH The Underwater Compressed-Air Energy Storage Database generator — jahdb-tech-617-underwater-compressed-air-energy-storage-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET617-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Underwater Compressed-Air Energy Storage Is","The Current State of Underwater Compressed-Air Energy Storage","Core Principles of Underwater Compressed-Air Energy Storage","Key Vocabulary of Underwater Compressed-Air Energy Storage","Why Underwater Compressed-Air Energy Storage Matters"],"Compounded":["Piece 1 of Underwater Compressed-Air Energy Storage: Primary Conversion Unit","Piece 2 of Underwater Compressed-Air Energy Storage: Fuel and Resource Supply","Piece 3 of Underwater Compressed-Air Energy Storage: Thermal Management","Piece 4 of Underwater Compressed-Air Energy Storage: Power Conditioning","Piece 5 of Underwater Compressed-Air Energy Storage: Storage Buffer","Piece 6 of Underwater Compressed-Air Energy Storage: Control and Dispatch Software","Piece 7 of Underwater Compressed-Air Energy Storage: Safety and Containment","Piece 8 of Underwater Compressed-Air Energy Storage: Grid Interconnection","How the Pieces of Underwater Compressed-Air Energy Storage Fit Together","Build Plan: Making Underwater Compressed-Air Energy Storage Step by Step"],"Advanced":["The Working Underwater Compressed-Air Energy Storage: What a Real Build Looks Like","Simulation Program: Modeling Underwater Compressed-Air Energy Storage in Code","Testing and Verifying Underwater Compressed-Air Energy Storage","Safety, Limits, and Responsible Use of Underwater Compressed-Air Energy Storage","Scaling Underwater Compressed-Air Energy Storage to Production","The Full Teaching Ladder for Underwater Compressed-Air Energy Storage","Open Problems and Next Steps in Underwater Compressed-Air Energy Storage"]};;
var DEMOKIND="underwater compressed-air energy storage record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# underwater compressed-air energy storage record planner — "+safe+"\n"
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
    name:topic+' — underwater compressed-air energy storage record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An underwater compressed-air energy storage record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-617-underwater-compressed-air-energy-storage-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-617-underwater-compressed-air-energy-storage',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
