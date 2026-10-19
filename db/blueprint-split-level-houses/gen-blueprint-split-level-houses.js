(function(){'use strict';
/* JAH The Split-Level Houses Blueprint Database generator — jahdb-blueprint-split-level-houses-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BP-SLH-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Reading Split-Level Houses Blueprints",
  "Blueprint Symbols and Line Weights",
  "Split-Level House Safety Basics",
  "Measuring and Layout",
  "Foundations and Footings",
  "Materials Primer for Split-Level Houses",
  "Permits and Codes Overview",
  "Cost Estimating Basics",
  "Site Selection for Split-Level Houses",
  "Plan Sheet Organization"
 ],
 "Compounded": [
  "Structural Systems for Split-Level Houses",
  "Split-Level House Detailing",
  "Code Compliance",
  "Drainage and Grading",
  "Electrical Rough-In Planning",
  "Plumbing Rough-In Planning",
  "HVAC Planning for Split-Level Houses",
  "Accessibility in Split-Level Houses Design",
  "Classic 3-Level Design Details",
  "Small 1400 sq ft Design Details",
  "Construction Sequencing",
  "Inspection Checkpoints"
 ],
 "Advanced": [
  "Split-Level House Engineering Calculations",
  "Load Paths and Lateral Design",
  "Value Engineering Split-Level Houses",
  "Sustainable Split-Level House Design",
  "Historic Split-Level House Restoration",
  "Advanced Split-Level House Materials",
  "Large 2600 sq ft Master Details",
  "1960s Original Master Details",
  "Failure Modes and Prevention",
  "Professional Practice and Liability"
 ]
};
var DEMOKIND="blueprint planning";
var SAMPLEDESC="Public-record sample, clearly labeled as a sample.";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Blueprint material estimate — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "# Property of Justin Addam Higgins (JAH).\n"
   + "design = \""+safe+"\"\n"
   + "materials = \"representative materials\"\n"
   + "def estimate(design, materials):\n"
   + "    return {'design': design, 'materials': materials,\n"
   + "            'note': 'Representative estimate — verify with a licensed professional before building.'}\n"
   + "print(estimate(design, materials))\n"
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
    name:topic+' — split-level house blueprint record sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A split-level house blueprint record sample of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-blueprint-split-level-houses-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-split-level-houses',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
