(function(){'use strict';
/* JAH The Precision Irrigation by Individual Plant Database generator — jahdb-tech-781-precision-irrigation-by-individual-plant-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET781-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Precision Irrigation by Individual Plant Is","The Current State of Precision Irrigation by Individual Plant","Core Principles of Precision Irrigation by Individual Plant","Key Vocabulary of Precision Irrigation by Individual Plant","Why Precision Irrigation by Individual Plant Matters"],"Compounded":["Piece 1 of Precision Irrigation by Individual Plant: Source Capture","Piece 2 of Precision Irrigation by Individual Plant: Purification and Production Core","Piece 3 of Precision Irrigation by Individual Plant: Quality Sensing","Piece 4 of Precision Irrigation by Individual Plant: Distribution Network","Piece 5 of Precision Irrigation by Individual Plant: Storage Buffer","Piece 6 of Precision Irrigation by Individual Plant: Energy Integration","Piece 7 of Precision Irrigation by Individual Plant: Waste Recovery","Piece 8 of Precision Irrigation by Individual Plant: Community Interface","How the Pieces of Precision Irrigation by Individual Plant Fit Together","Build Plan: Making Precision Irrigation by Individual Plant Step by Step"],"Advanced":["The Working Precision Irrigation by Individual Plant: What a Real Build Looks Like","Simulation Program: Modeling Precision Irrigation by Individual Plant in Code","Testing and Verifying Precision Irrigation by Individual Plant","Safety, Limits, and Responsible Use of Precision Irrigation by Individual Plant","Scaling Precision Irrigation by Individual Plant to Production","The Full Teaching Ladder for Precision Irrigation by Individual Plant","Open Problems and Next Steps in Precision Irrigation by Individual Plant"]};;
var DEMOKIND="precision irrigation by individual plant record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# precision irrigation by individual plant record planner — "+safe+"\n"
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
    name:topic+' — precision irrigation by individual plant record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A precision irrigation by individual plant record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-781-precision-irrigation-by-individual-plant-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-781-precision-irrigation-by-individual-plant',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
