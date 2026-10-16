(function(){'use strict';
/* JAH The Hardware and Fabrication Taxonomy Database generator — "jahdb-hardware-fabrication-taxonomy-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. generateChecked: every generated
   record passes validate() and driftCheck() before it may be filed. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function escQ(s){return String(s).split("\\").join("\\\\").split("'").join("\\'");}
var PREFIX="JAH-HFT-";
var FIELDS=["HARDWARE, FABRICATION & PHYSICAL SYSTEM "];
var TOPICS={"HARDWARE, FABRICATION & PHYSICAL SYSTEM ": ["Microcontrollers (MCUs)", "Single-Board Computers (SBCs)", "System-on-Chips (SoCs)", "System-on-Modules (SoMs)", "Field-Programmable Gate Arrays (FPGAs)", "Complex Programmable Logic Devices (CPLDs)", "Application-Specific Integrated Circuits (ASICs)", "Processors", "Central Processing Units (CPUs)", "Graphics Processing Units (GPUs)", "Tensor Processing Units (TPUs)", "Neural Processing Units (NPUs)"]};
function demoProgram(topic,field){
  return '# taxonomy term record study demo\n'
   + "print('Study: ' + '" + escQ(topic) + "')\n"
   + "print('Field: ' + '" + escQ(field) + "')\n"
   + "print('Full entries: description, how it works, key points, requirements, citations, demo.')\n"
   + "print('Sample record - structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' - taxonomy term record study',
    title:topic,
    description:'SAMPLE RECORD (generated - structural sample). A taxonomy term record study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'study-explorer',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
function generateChecked(seed,opts,sample){
  var r=generate(seed,opts||{});
  var v=validate(r);
  if(!v.ok)return {ok:false,errors:v.errors};
  var d=driftCheck(r,sample||[]);
  if(!d.ok)return {ok:false,errors:d.errors};
  return {ok:true,record:r};
}
var gen={version:"jahdb-hardware-fabrication-taxonomy-1.0",generate:generate,validate:validate,driftCheck:driftCheck,generateChecked:generateChecked,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("hardware-fabrication-taxonomy",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
