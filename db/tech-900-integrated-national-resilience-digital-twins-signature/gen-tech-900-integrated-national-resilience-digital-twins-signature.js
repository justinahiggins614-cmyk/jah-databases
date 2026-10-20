(function(){'use strict';
/* JAH The Signature Integrated National Resilience Digital Twins Database generator — jahdb-tech-900-integrated-national-resilience-digital-twins-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET900S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Integrated National Resilience Digital Twins Is","The Current State of Integrated National Resilience Digital Twins","Core Principles of Integrated National Resilience Digital Twins","Key Vocabulary of Integrated National Resilience Digital Twins","Why Integrated National Resilience Digital Twins Matters"],"Compounded":["Piece 1 of Integrated National Resilience Digital Twins: Sensor and Data Layer","Piece 2 of Integrated National Resilience Digital Twins: Detection Engine","Piece 3 of Integrated National Resilience Digital Twins: Identity and Access","Piece 4 of Integrated National Resilience Digital Twins: Response Coordination","Piece 5 of Integrated National Resilience Digital Twins: Communications Backbone","Piece 6 of Integrated National Resilience Digital Twins: Recovery Systems","Piece 7 of Integrated National Resilience Digital Twins: Audit and Evidence","Piece 8 of Integrated National Resilience Digital Twins: Human Oversight","How the Pieces of Integrated National Resilience Digital Twins Fit Together","Build Plan: Making Integrated National Resilience Digital Twins Step by Step"],"Advanced":["The Working Integrated National Resilience Digital Twin: What a Real Build Looks Like","Simulation Program: Modeling Integrated National Resilience Digital Twins in Code","Testing and Verifying Integrated National Resilience Digital Twins","Safety, Limits, and Responsible Use of Integrated National Resilience Digital Twins","Scaling Integrated National Resilience Digital Twins to Production","The Full Teaching Ladder for Integrated National Resilience Digital Twins","Open Problems and Next Steps in Integrated National Resilience Digital Twins"]};;
var DEMOKIND="signature integrated national resilience digital twin record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature integrated national resilience digital twin record planner — "+safe+"\n"
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
    name:topic+' — signature integrated national resilience digital twin record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature integrated national resilience digital twin record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-900-integrated-national-resilience-digital-twins-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-900-integrated-national-resilience-digital-twins-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
