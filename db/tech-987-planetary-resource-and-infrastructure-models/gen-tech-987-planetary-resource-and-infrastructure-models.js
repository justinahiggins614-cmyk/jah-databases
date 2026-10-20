(function(){'use strict';
/* JAH The Planetary Resource and Infrastructure Models Database generator — jahdb-tech-987-planetary-resource-and-infrastructure-models-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET987-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Planetary Resource and Infrastructure Models Is","The Current State of Planetary Resource and Infrastructure Models","Core Principles of Planetary Resource and Infrastructure Models","Key Vocabulary of Planetary Resource and Infrastructure Models","Why Planetary Resource and Infrastructure Models Matters"],"Compounded":["Piece 1 of Planetary Resource and Infrastructure Models: Knowledge Base","Piece 2 of Planetary Resource and Infrastructure Models: Discovery Engine","Piece 3 of Planetary Resource and Infrastructure Models: Design Engine","Piece 4 of Planetary Resource and Infrastructure Models: Simulation Fabric","Piece 5 of Planetary Resource and Infrastructure Models: Manufacturing Network","Piece 6 of Planetary Resource and Infrastructure Models: Verification Grid","Piece 7 of Planetary Resource and Infrastructure Models: Coordination Layer","Piece 8 of Planetary Resource and Infrastructure Models: Long-Term Archive","How the Pieces of Planetary Resource and Infrastructure Models Fit Together","Build Plan: Making Planetary Resource and Infrastructure Models Step by Step"],"Advanced":["The Working Planetary Resource and Infrastructure Model: What a Real Build Looks Like","Simulation Program: Modeling Planetary Resource and Infrastructure Models in Code","Testing and Verifying Planetary Resource and Infrastructure Models","Safety, Limits, and Responsible Use of Planetary Resource and Infrastructure Models","Scaling Planetary Resource and Infrastructure Models to Production","The Full Teaching Ladder for Planetary Resource and Infrastructure Models","Open Problems and Next Steps in Planetary Resource and Infrastructure Models"]};;
var DEMOKIND="planetary resource and infrastructure model record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# planetary resource and infrastructure model record planner — "+safe+"\n"
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
    name:topic+' — planetary resource and infrastructure model record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A planetary resource and infrastructure model record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-987-planetary-resource-and-infrastructure-models-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-987-planetary-resource-and-infrastructure-models',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
