(function(){'use strict';
/* JAH The Fabrication Tools Database generator — jahdb-fabrication-tools-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FBT-";
var FIELDS=["fab"];
var TOPICS={
 "fab": [
  "Parametric CAD \u2014 fab",
  "Direct CAD \u2014 fab",
  "Mesh Editors \u2014 fab",
  "Surface Modelers \u2014 fab",
  "CAM Processors \u2014 fab",
  "Toolpath Generators \u2014 fab",
  "Post-Processors \u2014 fab",
  "G-Code Simulators \u2014 fab",
  "G-Code Editors \u2014 fab",
  "Feed Calculators \u2014 fab",
  "Speed Calculators \u2014 fab",
  "Cutting Optimizers \u2014 fab",
  "Nesting Tools \u2014 fab",
  "Kerf Compensators \u2014 fab",
  "Tab Generators \u2014 fab",
  "Lead-In Tools \u2014 fab",
  "Pierce Controllers \u2014 fab",
  "Height Controllers \u2014 fab",
  "Breakaway Tools \u2014 fab",
  "Dust Collectors \u2014 fab",
  "Coolant Systems \u2014 fab",
  "Workholding Designers \u2014 fab",
  "Fixture Plates \u2014 fab",
  "Soft Jaw Generators \u2014 fab",
  "Probe Cycles \u2014 fab",
  "Tool Setters \u2014 fab",
  "Tool Libraries \u2014 fab",
  "Wear Compensators \u2014 fab",
  "Chatter Analyzers \u2014 fab",
  "Surface Finish Estimators \u2014 fab",
  "Cycle Time Estimators \u2014 fab",
  "Cost Estimators \u2014 fab",
  "Quoting Tools \u2014 fab",
  "Job Trackers \u2014 fab",
  "Inventory Managers \u2014 fab",
  "Maintenance Schedulers \u2014 fab",
  "Calibration Tools \u2014 fab",
  "Laser Aligners \u2014 fab",
  "Beam Profilers \u2014 fab",
  "Power Meters \u2014 fab",
  "Fume Extractors \u2014 fab",
  "Air Assist Controllers \u2014 fab",
  "Gas Mixers \u2014 fab",
  "Etching Tanks \u2014 fab",
  "Plating Controllers \u2014 fab",
  "Anodizing Controllers \u2014 fab",
  "Powder Coating Guns \u2014 fab",
  "Sandblasters \u2014 fab",
  "Vibratory Finishers \u2014 fab",
  "Ultrasonic Cleaners \u2014 fab",
  "Parts Washers \u2014 fab",
  "Rust Preventatives \u2014 fab",
  "CMM Software \u2014 fab",
  "Vision Systems \u2014 fab",
  "Roughness Testers \u2014 fab",
  "Hardness Testers \u2014 fab",
  "Tensile Testers \u2014 fab"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fabrication Tools — "+safe+"\n"
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
    name:topic+' — fabrication tool record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fabrication tool record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-fabrication-tools-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fabrication-tools',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
