(function(){'use strict';
/* JAH The PCB Design Database generator — jahdb-pcb-design-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCB-";
var FIELDS=["pcb"];
var TOPICS={
 "pcb": [
  "Schematic Capture \u2014 pcb",
  "PCB Layout \u2014 pcb",
  "Autorouters \u2014 pcb",
  "Interactive Routers \u2014 pcb",
  "Design Rule Checkers \u2014 pcb",
  "Electrical Rule Checkers \u2014 pcb",
  "Gerber Viewers \u2014 pcb",
  "Gerber Generators \u2014 pcb",
  "NC Drill Generators \u2014 pcb",
  "Pick-and-Place Generators \u2014 pcb",
  "BOM Generators \u2014 pcb",
  "SPICE Simulators \u2014 pcb",
  "Signal Integrity Simulators \u2014 pcb",
  "Power Integrity Simulators \u2014 pcb",
  "EM Simulators \u2014 pcb",
  "Thermal Simulators \u2014 pcb",
  "Footprint Libraries \u2014 pcb",
  "Symbol Libraries \u2014 pcb",
  "3D Model Libraries \u2014 pcb",
  "Stackup Designers \u2014 pcb",
  "Impedance Calculators \u2014 pcb",
  "Via Designers \u2014 pcb",
  "Differential Pair Tools \u2014 pcb",
  "Length Tuners \u2014 pcb",
  "Copper Pour Tools \u2014 pcb",
  "Plane Splitters \u2014 pcb",
  "Teardropping Tools \u2014 pcb",
  "Filleting Tools \u2014 pcb",
  "Panelizers \u2014 pcb",
  "Fiducial Generators \u2014 pcb",
  "Solder Mask Tools \u2014 pcb",
  "Silkscreen Tools \u2014 pcb",
  "Assembly Drawings \u2014 pcb",
  "Fabrication Notes \u2014 pcb",
  "Impedance Tables \u2014 pcb",
  "Test Point Tools \u2014 pcb",
  "Boundary Scan Tools \u2014 pcb",
  "Flying Probe Adapters \u2014 pcb",
  "In-Circuit Testers \u2014 pcb",
  "Design for Manufacturing \u2014 pcb",
  "Design for Assembly \u2014 pcb",
  "Design for Test \u2014 pcb",
  "Variant Managers \u2014 pcb",
  "Revision Managers \u2014 pcb",
  "Library Managers \u2014 pcb",
  "Parts Searchers \u2014 pcb",
  "Pricing Tools \u2014 pcb",
  "Availability Checkers \u2014 pcb",
  "Lifecycle Trackers \u2014 pcb",
  "Compliance Checkers \u2014 pcb",
  "Export Control Checkers \u2014 pcb",
  "Version Control Adapters \u2014 pcb",
  "Collaboration Tools \u2014 pcb",
  "Web Viewers \u2014 pcb",
  "Manufacturing Portals \u2014 pcb",
  "Assembly Portals \u2014 pcb",
  "Stencils Generators \u2014 pcb"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Pcb Design — "+safe+"\n"
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
    name:topic+' — PCB tool record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A PCB tool record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-pcb-design-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pcb-design',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
