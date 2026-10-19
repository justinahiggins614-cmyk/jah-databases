(function(){'use strict';
/* JAH The House Blueprint Database generator — jahdb-blueprint-houses-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BHP-";
var FIELDS=["Multi-Level","Multi-Unit","Single-Story","Small / Cabin","Two-Story"];
var TOPICS={
 "Multi-Level": [
  "Split-Level - Compact Architectural Blueprint - Multi-Level",
  "Split-Level - Standard Architectural Blueprint - Multi-Level",
  "Split-Level - Grand Architectural Blueprint - Multi-Level"
 ],
 "Multi-Unit": [
  "Townhouse - Compact Architectural Blueprint - Multi-Unit",
  "Duplex - Compact Architectural Blueprint - Multi-Unit",
  "Townhouse - Standard Architectural Blueprint - Multi-Unit",
  "Duplex - Standard Architectural Blueprint - Multi-Unit",
  "Townhouse - Grand Architectural Blueprint - Multi-Unit"
 ],
 "Single-Story": [
  "Ranch House - Compact Architectural Blueprint - Single-Story",
  "Cape Cod Cottage - Compact Architectural Blueprint - Single-Story",
  "Craftsman Bungalow - Compact Architectural Blueprint - Single-Story",
  "Farmhouse - Compact Architectural Blueprint - Single-Story",
  "Ranch House - Standard Architectural Blueprint - Single-Story",
  "Cape Cod Cottage - Standard Architectural Blueprint - Single-Story",
  "Craftsman Bungalow - Standard Architectural Blueprint - Single-Story",
  "Farmhouse - Standard Architectural Blueprint - Single-Story",
  "Ranch House - Grand Architectural Blueprint - Single-Story",
  "Cape Cod Cottage - Grand Architectural Blueprint - Single-Story",
  "Craftsman Bungalow - Grand Architectural Blueprint - Single-Story",
  "Farmhouse - Grand Architectural Blueprint - Single-Story"
 ],
 "Small / Cabin": [
  "Log Cabin - Compact Architectural Blueprint - Small / Cabin",
  "Accessory Dwelling Unit - Compact Architectural Blueprint - Small / Cabin",
  "Storybook Cottage - Compact Architectural Blueprint - Small / Cabin",
  "Log Cabin - Standard Architectural Blueprint - Small / Cabin",
  "Accessory Dwelling Unit - Standard Architectural Blueprint - Small / Cabin",
  "Storybook Cottage - Standard Architectural Blueprint - Small / Cabin",
  "Log Cabin - Grand Architectural Blueprint - Small / Cabin",
  "Accessory Dwelling Unit - Grand Architectural Blueprint - Small / Cabin"
 ],
 "Two-Story": [
  "Colonial Two-Story - Compact Architectural Blueprint - Two-Story",
  "Modern Flat-Roof House - Compact Architectural Blueprint - Two-Story",
  "Colonial Two-Story - Standard Architectural Blueprint - Two-Story",
  "Modern Flat-Roof House - Standard Architectural Blueprint - Two-Story",
  "Colonial Two-Story - Grand Architectural Blueprint - Two-Story",
  "Modern Flat-Roof House - Grand Architectural Blueprint - Two-Story"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Houses Blueprint Study — "+safe+"\n"
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
    name:topic+' — house blueprint record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A house blueprint record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"blueprint-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-blueprint-houses-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-houses',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
