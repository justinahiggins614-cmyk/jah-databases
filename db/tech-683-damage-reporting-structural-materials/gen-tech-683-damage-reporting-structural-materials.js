(function(){'use strict';
/* JAH The Damage-Reporting Structural Materials Database generator — jahdb-tech-683-damage-reporting-structural-materials-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET683-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Damage-Reporting Structural Materials Is","The Current State of Damage-Reporting Structural Materials","Core Principles of Damage-Reporting Structural Materials","Key Vocabulary of Damage-Reporting Structural Materials","Why Damage-Reporting Structural Materials Matters"],"Compounded":["Piece 1 of Damage-Reporting Structural Materials: Precursor Chemistry","Piece 2 of Damage-Reporting Structural Materials: Synthesis Reactor","Piece 3 of Damage-Reporting Structural Materials: Structure Control","Piece 4 of Damage-Reporting Structural Materials: Characterization Suite","Piece 5 of Damage-Reporting Structural Materials: Property Testing","Piece 6 of Damage-Reporting Structural Materials: Scale Manufacturing","Piece 7 of Damage-Reporting Structural Materials: Integration Engineering","Piece 8 of Damage-Reporting Structural Materials: Lifecycle and Safety","How the Pieces of Damage-Reporting Structural Materials Fit Together","Build Plan: Making Damage-Reporting Structural Materials Step by Step"],"Advanced":["The Working Damage-Reporting Structural Material: What a Real Build Looks Like","Simulation Program: Modeling Damage-Reporting Structural Materials in Code","Testing and Verifying Damage-Reporting Structural Materials","Safety, Limits, and Responsible Use of Damage-Reporting Structural Materials","Scaling Damage-Reporting Structural Materials to Production","The Full Teaching Ladder for Damage-Reporting Structural Materials","Open Problems and Next Steps in Damage-Reporting Structural Materials"]};;
var DEMOKIND="damage-reporting structural material record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# damage-reporting structural material record planner — "+safe+"\n"
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
    name:topic+' — damage-reporting structural material record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A damage-reporting structural material record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-683-damage-reporting-structural-materials-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-683-damage-reporting-structural-materials',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
