(function(){'use strict';
/* JAH The Artificial Ecosystem Engineering Database generator — jahdb-tech-1014-artificial-ecosystem-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET1014-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Artificial Ecosystem Engineering Is","The Current State of Artificial Ecosystem Engineering","Core Principles of Artificial Ecosystem Engineering","Key Vocabulary of Artificial Ecosystem Engineering","Why Artificial Ecosystem Engineering Matters"],"Compounded":["Piece 1 of Artificial Ecosystem Engineering: Foundational Science","Piece 2 of Artificial Ecosystem Engineering: Exploratory Instruments","Piece 3 of Artificial Ecosystem Engineering: Theoretical Frameworks","Piece 4 of Artificial Ecosystem Engineering: Prototype Platforms","Piece 5 of Artificial Ecosystem Engineering: Safety and Ethics Review","Piece 6 of Artificial Ecosystem Engineering: Long-Horizon Roadmapping","Piece 7 of Artificial Ecosystem Engineering: Cross-Disciplinary Teams","Piece 8 of Artificial Ecosystem Engineering: Knowledge Preservation","How the Pieces of Artificial Ecosystem Engineering Fit Together","Build Plan: Making Artificial Ecosystem Engineering Step by Step"],"Advanced":["The Working Artificial Ecosystem Engineering: What a Real Build Looks Like","Simulation Program: Modeling Artificial Ecosystem Engineering in Code","Testing and Verifying Artificial Ecosystem Engineering","Safety, Limits, and Responsible Use of Artificial Ecosystem Engineering","Scaling Artificial Ecosystem Engineering to Production","The Full Teaching Ladder for Artificial Ecosystem Engineering","Open Problems and Next Steps in Artificial Ecosystem Engineering"]};;
var DEMOKIND="artificial ecosystem engineering record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# artificial ecosystem engineering record planner — "+safe+"\n"
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
    name:topic+' — artificial ecosystem engineering record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An artificial ecosystem engineering record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-1014-artificial-ecosystem-engineering-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-1014-artificial-ecosystem-engineering',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
