(function(){'use strict';
/* JAH The 3D Stacked Integrated Circuits Database generator — jahdb-tech-43-3d-stacked-integrated-circuits-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET43-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What 3D Stacked Integrated Circuits Is","Current Research State of 3D Stacked Integrated Circuits","Key Technical Specifications of 3D Stacked Integrated Circuits","Key Public Developments in 3D Stacked Integrated Circuits","Challenges and Open Problems in 3D Stacked Integrated Circuits"],"Compounded": ["Hybrid Bonding Process","TSV Formation Module","HBM Memory Stack","Thermal Interface Stack","Known-Good-Die Test","3D-Aware EDA Flow","Chiplet Interface Standard"],"Advanced": ["Backside Power Network","Monolithic 3D Process","Stacked Image Sensor","Power-Thermal Co-Designer","Failure Analysis for 3D","Cost Model for Stacking","Heterogeneous Stack Demo","Recycling for Stacks"]};
var DEMOKIND="3d stacked integrated circuit record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 3d stacked integrated circuit record planner — "+safe+"\n"
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
    name:topic+' — 3d stacked integrated circuit record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 3d stacked integrated circuit record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-43-3d-stacked-integrated-circuits-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-43-3d-stacked-integrated-circuits',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
