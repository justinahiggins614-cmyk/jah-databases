(function(){'use strict';
/* JAH The Signature Early Earthquake Warning Networks Database generator — jahdb-tech-885-early-earthquake-warning-networks-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET885S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Early Earthquake Warning Networks Is","The Current State of Early Earthquake Warning Networks","Core Principles of Early Earthquake Warning Networks","Key Vocabulary of Early Earthquake Warning Networks","Why Early Earthquake Warning Networks Matters"],"Compounded":["Piece 1 of Early Earthquake Warning Networks: Sensor and Data Layer","Piece 2 of Early Earthquake Warning Networks: Detection Engine","Piece 3 of Early Earthquake Warning Networks: Identity and Access","Piece 4 of Early Earthquake Warning Networks: Response Coordination","Piece 5 of Early Earthquake Warning Networks: Communications Backbone","Piece 6 of Early Earthquake Warning Networks: Recovery Systems","Piece 7 of Early Earthquake Warning Networks: Audit and Evidence","Piece 8 of Early Earthquake Warning Networks: Human Oversight","How the Pieces of Early Earthquake Warning Networks Fit Together","Build Plan: Making Early Earthquake Warning Networks Step by Step"],"Advanced":["The Working Early Earthquake Warning Network: What a Real Build Looks Like","Simulation Program: Modeling Early Earthquake Warning Networks in Code","Testing and Verifying Early Earthquake Warning Networks","Safety, Limits, and Responsible Use of Early Earthquake Warning Networks","Scaling Early Earthquake Warning Networks to Production","The Full Teaching Ladder for Early Earthquake Warning Networks","Open Problems and Next Steps in Early Earthquake Warning Networks"]};;
var DEMOKIND="signature early earthquake warning network record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature early earthquake warning network record planner — "+safe+"\n"
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
    name:topic+' — signature early earthquake warning network record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature early earthquake warning network record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-885-early-earthquake-warning-networks-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-885-early-earthquake-warning-networks-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
