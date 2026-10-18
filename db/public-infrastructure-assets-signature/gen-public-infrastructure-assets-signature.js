(function(){'use strict';
/* JAH The Public Infrastructure Assets Signature Database generator — jahdb-public-infrastructure-assets-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INFRA-SIG-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Road Networks: Arterials, Collectors, and Local Streets (Signature Edition)", "Highway Bridges (Signature Edition)", "Water Treatment Plants (Signature Edition)", "Wastewater Collection and Treatment (Signature Edition)", "Stormwater Drainage Systems (Signature Edition)", "Public Buildings (Signature Edition)", "Parks and Recreation Facilities (Signature Edition)", "Street Lighting (Signature Edition)", "Traffic Signals (Signature Edition)", "Sidewalks and Curb Ramps (Signature Edition)", "Public Parking Facilities (Signature Edition)", "Solid Waste and Landfill Facilities (Signature Edition)"], "Compounded": ["Public Dams (Signature Edition)", "Levees and Flood Control Structures (Signature Edition)", "Public Airports (Signature Edition)", "Seaports and Harbors (Signature Edition)", "Public Transit: Bus Systems (Signature Edition)", "Public Transit: Rail Systems (Signature Edition)", "Municipal Electric Distribution (Signature Edition)", "Natural Gas Distribution Systems (Signature Edition)", "Broadband and Fiber Networks (Signature Edition)", "Fire Stations (Signature Edition)", "Police Stations (Signature Edition)", "Public Hospitals (Signature Edition)"], "Advanced": ["Public Schools as Infrastructure (Signature Edition)", "Public Libraries (Signature Edition)", "Courthouses and Civic Buildings (Signature Edition)", "ISO 55000 Asset Management (Signature Edition)", "Pavement Condition Rating (PASER) (Signature Edition)", "National Bridge Inspection Standards (NBIS) (Signature Edition)", "Lifecycle Cost Analysis (Signature Edition)", "Capital Improvement Planning (Signature Edition)", "GIS Asset Inventories (Signature Edition)", "Infrastructure Resilience and Climate Adaptation (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Infrastructure Asset Study — "+safe+"\n"
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
    name:topic+' — infrastructure asset record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A infrastructure asset record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"asset-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-public-infrastructure-assets-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("public-infrastructure-assets-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
