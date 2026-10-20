(function(){'use strict';
/* JAH The In-Vivo Gene Editing Therapies Database generator — jahdb-tech-628-in-vivo-gene-editing-therapies-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET628-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What In-Vivo Gene Editing Therapies Is","The Current State of In-Vivo Gene Editing Therapies","Core Principles of In-Vivo Gene Editing Therapies","Key Vocabulary of In-Vivo Gene Editing Therapies","Why In-Vivo Gene Editing Therapies Matters"],"Compounded":["Piece 1 of In-Vivo Gene Editing Therapies: Diagnostic Sensing","Piece 2 of In-Vivo Gene Editing Therapies: Therapeutic Mechanism","Piece 3 of In-Vivo Gene Editing Therapies: Delivery System","Piece 4 of In-Vivo Gene Editing Therapies: Patient Monitoring","Piece 5 of In-Vivo Gene Editing Therapies: Data and Decision Platform","Piece 6 of In-Vivo Gene Editing Therapies: Manufacturing Line","Piece 7 of In-Vivo Gene Editing Therapies: Safety and Trial Evidence","Piece 8 of In-Vivo Gene Editing Therapies: Care Integration","How the Pieces of In-Vivo Gene Editing Therapies Fit Together","Build Plan: Making In-Vivo Gene Editing Therapies Step by Step"],"Advanced":["The Working In-Vivo Gene Editing Therapy: What a Real Build Looks Like","Simulation Program: Modeling In-Vivo Gene Editing Therapies in Code","Testing and Verifying In-Vivo Gene Editing Therapies","Safety, Limits, and Responsible Use of In-Vivo Gene Editing Therapies","Scaling In-Vivo Gene Editing Therapies to Production","The Full Teaching Ladder for In-Vivo Gene Editing Therapies","Open Problems and Next Steps in In-Vivo Gene Editing Therapies"]};;
var DEMOKIND="in-vivo gene editing therapy record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# in-vivo gene editing therapy record planner — "+safe+"\n"
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
    name:topic+' — in-vivo gene editing therapy record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An in-vivo gene editing therapy record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-628-in-vivo-gene-editing-therapies-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-628-in-vivo-gene-editing-therapies',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
