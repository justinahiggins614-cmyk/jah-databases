(function(){'use strict';
/* JAH The Rapidly Deployable Smart Cities Database generator — jahdb-tech-875-rapidly-deployable-smart-cities-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET875-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Rapidly Deployable Smart Cities Is","The Current State of Rapidly Deployable Smart Cities","Core Principles of Rapidly Deployable Smart Cities","Key Vocabulary of Rapidly Deployable Smart Cities","Why Rapidly Deployable Smart Cities Matters"],"Compounded":["Piece 1 of Rapidly Deployable Smart Cities: Structural System","Piece 2 of Rapidly Deployable Smart Cities: Robotic Construction Equipment","Piece 3 of Rapidly Deployable Smart Cities: Materials Supply","Piece 4 of Rapidly Deployable Smart Cities: Building Intelligence","Piece 5 of Rapidly Deployable Smart Cities: Energy System","Piece 6 of Rapidly Deployable Smart Cities: Water and Waste","Piece 7 of Rapidly Deployable Smart Cities: Mobility Integration","Piece 8 of Rapidly Deployable Smart Cities: Resilience Engineering","How the Pieces of Rapidly Deployable Smart Cities Fit Together","Build Plan: Making Rapidly Deployable Smart Cities Step by Step"],"Advanced":["The Working Rapidly Deployable Smart City: What a Real Build Looks Like","Simulation Program: Modeling Rapidly Deployable Smart Cities in Code","Testing and Verifying Rapidly Deployable Smart Cities","Safety, Limits, and Responsible Use of Rapidly Deployable Smart Cities","Scaling Rapidly Deployable Smart Cities to Production","The Full Teaching Ladder for Rapidly Deployable Smart Cities","Open Problems and Next Steps in Rapidly Deployable Smart Cities"]};;
var DEMOKIND="rapidly deployable smart city record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# rapidly deployable smart city record planner — "+safe+"\n"
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
    name:topic+' — rapidly deployable smart city record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A rapidly deployable smart city record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-875-rapidly-deployable-smart-cities-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-875-rapidly-deployable-smart-cities',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
