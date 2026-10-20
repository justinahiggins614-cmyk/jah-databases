(function(){'use strict';
/* JAH The Programmable Living Materials Database generator — jahdb-tech-651-programmable-living-materials-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET651-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Programmable Living Materials Is","The Current State of Programmable Living Materials","Core Principles of Programmable Living Materials","Key Vocabulary of Programmable Living Materials","Why Programmable Living Materials Matters"],"Compounded":["Piece 1 of Programmable Living Materials: Genetic Design Tools","Piece 2 of Programmable Living Materials: Cell Chassis","Piece 3 of Programmable Living Materials: Bioreactor Hardware","Piece 4 of Programmable Living Materials: Sensing and Control","Piece 5 of Programmable Living Materials: Downstream Processing","Piece 6 of Programmable Living Materials: Containment Systems","Piece 7 of Programmable Living Materials: Scale-Up Engineering","Piece 8 of Programmable Living Materials: Quality Analytics","How the Pieces of Programmable Living Materials Fit Together","Build Plan: Making Programmable Living Materials Step by Step"],"Advanced":["The Working Programmable Living Material: What a Real Build Looks Like","Simulation Program: Modeling Programmable Living Materials in Code","Testing and Verifying Programmable Living Materials","Safety, Limits, and Responsible Use of Programmable Living Materials","Scaling Programmable Living Materials to Production","The Full Teaching Ladder for Programmable Living Materials","Open Problems and Next Steps in Programmable Living Materials"]};;
var DEMOKIND="programmable living material record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# programmable living material record planner — "+safe+"\n"
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
    name:topic+' — programmable living material record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A programmable living material record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-651-programmable-living-materials-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-651-programmable-living-materials',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
