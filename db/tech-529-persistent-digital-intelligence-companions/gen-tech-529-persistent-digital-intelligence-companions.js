(function(){'use strict';
/* JAH The Persistent Digital Intelligence Companions Database generator — jahdb-tech-529-persistent-digital-intelligence-companions-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET529-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Persistent Digital Intelligence Companions Is","The Current State of Persistent Digital Intelligence Companions","Core Principles of Persistent Digital Intelligence Companions","Key Vocabulary of Persistent Digital Intelligence Companions","Why Persistent Digital Intelligence Companions Matters"],"Compounded":["Piece 1 of Persistent Digital Intelligence Companions: Knowledge Ingestion Layer","Piece 2 of Persistent Digital Intelligence Companions: World Model Core","Piece 3 of Persistent Digital Intelligence Companions: Reasoning Engine","Piece 4 of Persistent Digital Intelligence Companions: Learning Subsystem","Piece 5 of Persistent Digital Intelligence Companions: Verification Layer","Piece 6 of Persistent Digital Intelligence Companions: Action and Tool Interface","Piece 7 of Persistent Digital Intelligence Companions: Memory Architecture","Piece 8 of Persistent Digital Intelligence Companions: Oversight Console","How the Pieces of Persistent Digital Intelligence Companions Fit Together","Build Plan: Making Persistent Digital Intelligence Companions Step by Step"],"Advanced":["The Working Persistent Digital Intelligence Companion: What a Real Build Looks Like","Simulation Program: Modeling Persistent Digital Intelligence Companions in Code","Testing and Verifying Persistent Digital Intelligence Companions","Safety, Limits, and Responsible Use of Persistent Digital Intelligence Companions","Scaling Persistent Digital Intelligence Companions to Production","The Full Teaching Ladder for Persistent Digital Intelligence Companions","Open Problems and Next Steps in Persistent Digital Intelligence Companions"]};;
var DEMOKIND="persistent digital intelligence companion record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# persistent digital intelligence companion record planner — "+safe+"\n"
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
    name:topic+' — persistent digital intelligence companion record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A persistent digital intelligence companion record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-529-persistent-digital-intelligence-companions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-529-persistent-digital-intelligence-companions',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
