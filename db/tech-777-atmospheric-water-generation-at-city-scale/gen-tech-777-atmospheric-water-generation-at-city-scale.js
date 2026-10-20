(function(){'use strict';
/* JAH The Atmospheric Water Generation at City Scale Database generator — jahdb-tech-777-atmospheric-water-generation-at-city-scale-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET777-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Atmospheric Water Generation at City Scale Is","The Current State of Atmospheric Water Generation at City Scale","Core Principles of Atmospheric Water Generation at City Scale","Key Vocabulary of Atmospheric Water Generation at City Scale","Why Atmospheric Water Generation at City Scale Matters"],"Compounded":["Piece 1 of Atmospheric Water Generation at City Scale: Source Capture","Piece 2 of Atmospheric Water Generation at City Scale: Purification and Production Core","Piece 3 of Atmospheric Water Generation at City Scale: Quality Sensing","Piece 4 of Atmospheric Water Generation at City Scale: Distribution Network","Piece 5 of Atmospheric Water Generation at City Scale: Storage Buffer","Piece 6 of Atmospheric Water Generation at City Scale: Energy Integration","Piece 7 of Atmospheric Water Generation at City Scale: Waste Recovery","Piece 8 of Atmospheric Water Generation at City Scale: Community Interface","How the Pieces of Atmospheric Water Generation at City Scale Fit Together","Build Plan: Making Atmospheric Water Generation at City Scale Step by Step"],"Advanced":["The Working Atmospheric Water Generation at City Scale: What a Real Build Looks Like","Simulation Program: Modeling Atmospheric Water Generation at City Scale in Code","Testing and Verifying Atmospheric Water Generation at City Scale","Safety, Limits, and Responsible Use of Atmospheric Water Generation at City Scale","Scaling Atmospheric Water Generation at City Scale to Production","The Full Teaching Ladder for Atmospheric Water Generation at City Scale","Open Problems and Next Steps in Atmospheric Water Generation at City Scale"]};;
var DEMOKIND="atmospheric water generation at city scale record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# atmospheric water generation at city scale record planner — "+safe+"\n"
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
    name:topic+' — atmospheric water generation at city scale record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An atmospheric water generation at city scale record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-777-atmospheric-water-generation-at-city-scale-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-777-atmospheric-water-generation-at-city-scale',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
