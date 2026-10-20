(function(){'use strict';
/* JAH The Entirely 3D-Printed Buildings Database generator — jahdb-tech-852-entirely-3d-printed-buildings-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET852-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations":["What Entirely 3D-Printed Buildings Is","The Current State of Entirely 3D-Printed Buildings","Core Principles of Entirely 3D-Printed Buildings","Key Vocabulary of Entirely 3D-Printed Buildings","Why Entirely 3D-Printed Buildings Matters"],"Compounded":["Piece 1 of Entirely 3D-Printed Buildings: Structural System","Piece 2 of Entirely 3D-Printed Buildings: Robotic Construction Equipment","Piece 3 of Entirely 3D-Printed Buildings: Materials Supply","Piece 4 of Entirely 3D-Printed Buildings: Building Intelligence","Piece 5 of Entirely 3D-Printed Buildings: Energy System","Piece 6 of Entirely 3D-Printed Buildings: Water and Waste","Piece 7 of Entirely 3D-Printed Buildings: Mobility Integration","Piece 8 of Entirely 3D-Printed Buildings: Resilience Engineering","How the Pieces of Entirely 3D-Printed Buildings Fit Together","Build Plan: Making Entirely 3D-Printed Buildings Step by Step"],"Advanced":["The Working Entirely 3D-Printed Building: What a Real Build Looks Like","Simulation Program: Modeling Entirely 3D-Printed Buildings in Code","Testing and Verifying Entirely 3D-Printed Buildings","Safety, Limits, and Responsible Use of Entirely 3D-Printed Buildings","Scaling Entirely 3D-Printed Buildings to Production","The Full Teaching Ladder for Entirely 3D-Printed Buildings","Open Problems and Next Steps in Entirely 3D-Printed Buildings"]};;
var DEMOKIND="entirely 3d-printed building record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# entirely 3d-printed building record planner — "+safe+"\n"
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
    name:topic+' — entirely 3d-printed building record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). An entirely 3d-printed building record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-852-entirely-3d-printed-buildings-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-852-entirely-3d-printed-buildings',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
