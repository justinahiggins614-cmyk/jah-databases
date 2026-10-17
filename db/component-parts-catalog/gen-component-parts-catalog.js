(function(){'use strict';
/* JAH The Component and Parts Catalog Database generator — jahdb-component-parts-catalog-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPTC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Component or Part - Foundations",
  "Reading a Component Datasheet - Foundations",
  "Units, Tolerances, and Ratings - Foundations",
  "Passive Components: Resistors, Capacitors, Inductors - Foundations",
  "Mechanical Parts: Fasteners, Bearings, Gears - Foundations",
  "Wire, Cable, and Connector Basics - Foundations",
  "Component Markings and Identification Codes - Foundations",
  "Materials Stock: Sheet, Bar, Rod, and Filament - Foundations",
  "Series and Parallel Component Rules - Foundations",
  "What Compatibility Means for Parts - Foundations",
  "Selection Criteria: How Engineers Choose a Part - Foundations",
  "Standards Bodies and Part Numbering - Foundations"
 ],
 "Compounded": [
  "Resistors in Depth - Compounded",
  "Capacitors in Depth - Compounded",
  "Inductors and Transformers - Compounded",
  "Diodes and Rectifiers - Compounded",
  "Transistors: BJT and MOSFET - Compounded",
  "Integrated Circuits and Logic Families - Compounded",
  "Sensors: Turning the World into Signals - Compounded",
  "Optoelectronics: LEDs, Displays, and Photodetectors - Compounded",
  "Fasteners and Thread Standards - Compounded",
  "Bearings and Bushings - Compounded",
  "Gears, Belts, and Power Transmission - Compounded",
  "Relays, Contactors, and Switches - Compounded"
 ],
 "Advanced": [
  "Derating and Design Margins - Advanced",
  "Tolerance Stack-Up Analysis - Advanced",
  "Thermal Management and Heat Sinks - Advanced",
  "EMI and EMC Compatibility - Advanced",
  "Reliability, MTBF, and Failure Rates - Advanced",
  "Counterfeit Component Detection - Advanced",
  "Obsolescence Management and Last-Time Buys - Advanced",
  "Sourcing, the BOM, and the Supply Chain - Advanced",
  "Cross-References and Substitution - Advanced",
  "Modules and Subassemblies: Build vs Buy - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Component Parts Study — "+safe+"\n"
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
    name:topic+' — component parts catalog record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A component parts catalog record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"component-parts-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-component-parts-catalog-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('component-parts-catalog',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
