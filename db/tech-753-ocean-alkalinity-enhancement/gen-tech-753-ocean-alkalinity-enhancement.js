(function(){'use strict';
/* JAH The Ocean Alkalinity Enhancement Database generator — jahdb-tech-753-ocean-alkalinity-enhancement-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET753-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Ocean Alkalinity Enhancement Is","The Current State of Ocean Alkalinity Enhancement","Core Principles of Ocean Alkalinity Enhancement","Key Vocabulary of Ocean Alkalinity Enhancement","Why Ocean Alkalinity Enhancement Matters"],"Compounded":["Piece 1 of Ocean Alkalinity Enhancement: Sensing Network","Piece 2 of Ocean Alkalinity Enhancement: Intervention Hardware","Piece 3 of Ocean Alkalinity Enhancement: Clean Energy Supply","Piece 4 of Ocean Alkalinity Enhancement: Transport and Logistics","Piece 5 of Ocean Alkalinity Enhancement: Monitoring and Verification","Piece 6 of Ocean Alkalinity Enhancement: Ecological Integration","Piece 7 of Ocean Alkalinity Enhancement: Data Platform","Piece 8 of Ocean Alkalinity Enhancement: Governance Interface","How the Pieces of Ocean Alkalinity Enhancement Fit Together","Build Plan: Making Ocean Alkalinity Enhancement Step by Step"],"Advanced":["The Working Ocean Alkalinity Enhancement: What a Real Build Looks Like","Simulation Program: Modeling Ocean Alkalinity Enhancement in Code","Testing and Verifying Ocean Alkalinity Enhancement","Safety, Limits, and Responsible Use of Ocean Alkalinity Enhancement","Scaling Ocean Alkalinity Enhancement to Production","The Full Teaching Ladder for Ocean Alkalinity Enhancement","Open Problems and Next Steps in Ocean Alkalinity Enhancement"]};;
var DEMOKIND="ocean alkalinity enhancement record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# ocean alkalinity enhancement record planner — "+safe+"\n"
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
    name:topic+' — ocean alkalinity enhancement record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An ocean alkalinity enhancement record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-753-ocean-alkalinity-enhancement-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-753-ocean-alkalinity-enhancement',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
