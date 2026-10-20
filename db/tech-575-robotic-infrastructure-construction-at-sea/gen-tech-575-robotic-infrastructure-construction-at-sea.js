(function(){'use strict';
/* JAH The Robotic Infrastructure Construction at Sea Database generator — jahdb-tech-575-robotic-infrastructure-construction-at-sea-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET575-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Robotic Infrastructure Construction at Sea Is","The Current State of Robotic Infrastructure Construction at Sea","Core Principles of Robotic Infrastructure Construction at Sea","Key Vocabulary of Robotic Infrastructure Construction at Sea","Why Robotic Infrastructure Construction at Sea Matters"],"Compounded":["Piece 1 of Robotic Infrastructure Construction at Sea: Mobility Platform","Piece 2 of Robotic Infrastructure Construction at Sea: Power and Energy System","Piece 3 of Robotic Infrastructure Construction at Sea: Perception Suite","Piece 4 of Robotic Infrastructure Construction at Sea: Onboard Compute","Piece 5 of Robotic Infrastructure Construction at Sea: Manipulation Hardware","Piece 6 of Robotic Infrastructure Construction at Sea: Communication Link","Piece 7 of Robotic Infrastructure Construction at Sea: Control Software Stack","Piece 8 of Robotic Infrastructure Construction at Sea: Safety and Recovery Systems","How the Pieces of Robotic Infrastructure Construction at Sea Fit Together","Build Plan: Making Robotic Infrastructure Construction at Sea Step by Step"],"Advanced":["The Working Robotic Infrastructure Construction at Sea: What a Real Build Looks Like","Simulation Program: Modeling Robotic Infrastructure Construction at Sea in Code","Testing and Verifying Robotic Infrastructure Construction at Sea","Safety, Limits, and Responsible Use of Robotic Infrastructure Construction at Sea","Scaling Robotic Infrastructure Construction at Sea to Production","The Full Teaching Ladder for Robotic Infrastructure Construction at Sea","Open Problems and Next Steps in Robotic Infrastructure Construction at Sea"]};;
var DEMOKIND="robotic infrastructure construction at sea record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# robotic infrastructure construction at sea record planner — "+safe+"\n"
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
    name:topic+' — robotic infrastructure construction at sea record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A robotic infrastructure construction at sea record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-575-robotic-infrastructure-construction-at-sea-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-575-robotic-infrastructure-construction-at-sea',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
