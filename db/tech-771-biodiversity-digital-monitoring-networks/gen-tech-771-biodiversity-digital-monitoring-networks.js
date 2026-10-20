(function(){'use strict';
/* JAH The Biodiversity Digital Monitoring Networks Database generator — jahdb-tech-771-biodiversity-digital-monitoring-networks-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET771-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Biodiversity Digital Monitoring Networks Is","The Current State of Biodiversity Digital Monitoring Networks","Core Principles of Biodiversity Digital Monitoring Networks","Key Vocabulary of Biodiversity Digital Monitoring Networks","Why Biodiversity Digital Monitoring Networks Matters"],"Compounded":["Piece 1 of Biodiversity Digital Monitoring Networks: Sensing Network","Piece 2 of Biodiversity Digital Monitoring Networks: Intervention Hardware","Piece 3 of Biodiversity Digital Monitoring Networks: Clean Energy Supply","Piece 4 of Biodiversity Digital Monitoring Networks: Transport and Logistics","Piece 5 of Biodiversity Digital Monitoring Networks: Monitoring and Verification","Piece 6 of Biodiversity Digital Monitoring Networks: Ecological Integration","Piece 7 of Biodiversity Digital Monitoring Networks: Data Platform","Piece 8 of Biodiversity Digital Monitoring Networks: Governance Interface","How the Pieces of Biodiversity Digital Monitoring Networks Fit Together","Build Plan: Making Biodiversity Digital Monitoring Networks Step by Step"],"Advanced":["The Working Biodiversity Digital Monitoring Network: What a Real Build Looks Like","Simulation Program: Modeling Biodiversity Digital Monitoring Networks in Code","Testing and Verifying Biodiversity Digital Monitoring Networks","Safety, Limits, and Responsible Use of Biodiversity Digital Monitoring Networks","Scaling Biodiversity Digital Monitoring Networks to Production","The Full Teaching Ladder for Biodiversity Digital Monitoring Networks","Open Problems and Next Steps in Biodiversity Digital Monitoring Networks"]};;
var DEMOKIND="biodiversity digital monitoring network record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# biodiversity digital monitoring network record planner — "+safe+"\n"
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
    name:topic+' — biodiversity digital monitoring network record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A biodiversity digital monitoring network record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-771-biodiversity-digital-monitoring-networks-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-771-biodiversity-digital-monitoring-networks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
