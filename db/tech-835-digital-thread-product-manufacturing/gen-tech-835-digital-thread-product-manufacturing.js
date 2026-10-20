(function(){'use strict';
/* JAH The Digital Thread Product Manufacturing Database generator — jahdb-tech-835-digital-thread-product-manufacturing-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET835-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Digital Thread Product Manufacturing Is","The Current State of Digital Thread Product Manufacturing","Core Principles of Digital Thread Product Manufacturing","Key Vocabulary of Digital Thread Product Manufacturing","Why Digital Thread Product Manufacturing Matters"],"Compounded":["Piece 1 of Digital Thread Product Manufacturing: Process Tooling","Piece 2 of Digital Thread Product Manufacturing: Material Feedstock","Piece 3 of Digital Thread Product Manufacturing: Metrology","Piece 4 of Digital Thread Product Manufacturing: Control Software","Piece 5 of Digital Thread Product Manufacturing: Robotics and Handling","Piece 6 of Digital Thread Product Manufacturing: Quality System","Piece 7 of Digital Thread Product Manufacturing: Facility Infrastructure","Piece 8 of Digital Thread Product Manufacturing: Digital Twin","How the Pieces of Digital Thread Product Manufacturing Fit Together","Build Plan: Making Digital Thread Product Manufacturing Step by Step"],"Advanced":["The Working Digital Thread Product Manufacturing: What a Real Build Looks Like","Simulation Program: Modeling Digital Thread Product Manufacturing in Code","Testing and Verifying Digital Thread Product Manufacturing","Safety, Limits, and Responsible Use of Digital Thread Product Manufacturing","Scaling Digital Thread Product Manufacturing to Production","The Full Teaching Ladder for Digital Thread Product Manufacturing","Open Problems and Next Steps in Digital Thread Product Manufacturing"]};;
var DEMOKIND="digital thread product manufacturing record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# digital thread product manufacturing record planner — "+safe+"\n"
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
    name:topic+' — digital thread product manufacturing record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A digital thread product manufacturing record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-835-digital-thread-product-manufacturing-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-835-digital-thread-product-manufacturing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
