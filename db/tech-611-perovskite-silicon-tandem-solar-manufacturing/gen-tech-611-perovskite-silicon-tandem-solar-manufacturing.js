(function(){'use strict';
/* JAH The Perovskite-Silicon Tandem Solar Manufacturing Database generator — jahdb-tech-611-perovskite-silicon-tandem-solar-manufacturing-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET611-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Perovskite-Silicon Tandem Solar Manufacturing Is","The Current State of Perovskite-Silicon Tandem Solar Manufacturing","Core Principles of Perovskite-Silicon Tandem Solar Manufacturing","Key Vocabulary of Perovskite-Silicon Tandem Solar Manufacturing","Why Perovskite-Silicon Tandem Solar Manufacturing Matters"],"Compounded":["Piece 1 of Perovskite-Silicon Tandem Solar Manufacturing: Primary Conversion Unit","Piece 2 of Perovskite-Silicon Tandem Solar Manufacturing: Fuel and Resource Supply","Piece 3 of Perovskite-Silicon Tandem Solar Manufacturing: Thermal Management","Piece 4 of Perovskite-Silicon Tandem Solar Manufacturing: Power Conditioning","Piece 5 of Perovskite-Silicon Tandem Solar Manufacturing: Storage Buffer","Piece 6 of Perovskite-Silicon Tandem Solar Manufacturing: Control and Dispatch Software","Piece 7 of Perovskite-Silicon Tandem Solar Manufacturing: Safety and Containment","Piece 8 of Perovskite-Silicon Tandem Solar Manufacturing: Grid Interconnection","How the Pieces of Perovskite-Silicon Tandem Solar Manufacturing Fit Together","Build Plan: Making Perovskite-Silicon Tandem Solar Manufacturing Step by Step"],"Advanced":["The Working Perovskite-Silicon Tandem Solar Manufacturing: What a Real Build Looks Like","Simulation Program: Modeling Perovskite-Silicon Tandem Solar Manufacturing in Code","Testing and Verifying Perovskite-Silicon Tandem Solar Manufacturing","Safety, Limits, and Responsible Use of Perovskite-Silicon Tandem Solar Manufacturing","Scaling Perovskite-Silicon Tandem Solar Manufacturing to Production","The Full Teaching Ladder for Perovskite-Silicon Tandem Solar Manufacturing","Open Problems and Next Steps in Perovskite-Silicon Tandem Solar Manufacturing"]};;
var DEMOKIND="perovskite-silicon tandem solar manufacturing record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# perovskite-silicon tandem solar manufacturing record planner — "+safe+"\n"
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
    name:topic+' — perovskite-silicon tandem solar manufacturing record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A perovskite-silicon tandem solar manufacturing record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-611-perovskite-silicon-tandem-solar-manufacturing-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-611-perovskite-silicon-tandem-solar-manufacturing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
