(function(){'use strict';
/* JAH The Costed Build Recipes Signature Database generator — jahdb-costed-build-recipes-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Basic Workbench Build (Signature Edition) - Workshop Builds",
  "Mobile Tool Cart Build (Signature Edition) - Workshop Builds",
  "Pegboard Tool Wall Build (Signature Edition) - Workshop Builds",
  "Sawhorse Pair Build (Signature Edition) - Workshop Builds",
  "Shop Stool Build (Signature Edition) - Workshop Builds",
  "LED Strip Work Light Build (Signature Edition) - Electronics Builds",
  "USB Charging Station Build (Signature Edition) - Electronics Builds",
  "Simple Sensor Monitor Build (Signature Edition) - Electronics Builds",
  "Storage Shelf Unit Build (Signature Edition) - Facility Builds",
  "Rolling Material Rack Build (Signature Edition) - Workshop Builds"
 ],
 "Compounded": [
  "Dust Collection Cart Build (Signature Edition) - Workshop Builds",
  "Welding Table Build (Signature Edition) - Workshop Builds",
  "Electronics Test Bench Build (Signature Edition) - Electronics Builds",
  "Weather Station Build (Signature Edition) - Electronics Builds",
  "Access Control Keypad Build (Signature Edition) - Electronics Builds",
  "Insulated Pipe Chase Build (Signature Edition) - Facility Builds",
  "Server Rack Ventilation Build (Signature Edition) - Facility Builds",
  "Emergency Eyewash Station Retrofit Build (Signature Edition) - Facility Builds",
  "Acoustic Panel Build (Signature Edition) - Facility Builds",
  "3D Printer Enclosure Build (Signature Edition) - Prototype Builds",
  "Prototype Housing Build (Signature Edition) - Prototype Builds",
  "Test Rig Frame Build (Signature Edition) - Prototype Builds"
 ],
 "Advanced": [
  "CNC Router Build (Signature Edition) - Workshop Builds",
  "Solar Battery Bank Build (Signature Edition) - Electronics Builds",
  "Compressed Air Distribution Build (Signature Edition) - Facility Builds",
  "Fume Extraction Build (Signature Edition) - Facility Builds",
  "Automated Parts Feeder Prototype (Signature Edition) - Prototype Builds",
  "Environmental Test Chamber Build (Signature Edition) - Prototype Builds",
  "Hydraulic Press Build (Signature Edition) - Workshop Builds",
  "Powder Coating Booth Build (Signature Edition) - Facility Builds",
  "Motor Test Dynamometer Build (Signature Edition) - Prototype Builds",
  "Whole-Shop Lighting Retrofit Build (Signature Edition) - Facility Builds",
  "Rainwater Harvesting Build (Signature Edition) - Facility Builds",
  "Build Recipe Costing Method (Signature Edition) - Prototype Builds"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Costed Build Recipes Signature — "+safe+"\n"
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
    name:topic+' — costed build recipe record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A costed build recipe record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-costed-build-recipes-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('costed-build-recipes-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
