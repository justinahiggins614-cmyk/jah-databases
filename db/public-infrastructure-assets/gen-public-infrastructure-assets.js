(function(){'use strict';
/* JAH The Public Infrastructure Assets Database generator — jahdb-public-infrastructure-assets-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INFRA-PUB-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Road Networks: Arterials, Collectors, and Local Streets", "Highway Bridges", "Water Treatment Plants", "Wastewater Collection and Treatment", "Stormwater Drainage Systems", "Public Buildings", "Parks and Recreation Facilities", "Street Lighting", "Traffic Signals", "Sidewalks and Curb Ramps", "Public Parking Facilities", "Solid Waste and Landfill Facilities"], "Compounded": ["Public Dams", "Levees and Flood Control Structures", "Public Airports", "Seaports and Harbors", "Public Transit: Bus Systems", "Public Transit: Rail Systems", "Municipal Electric Distribution", "Natural Gas Distribution Systems", "Broadband and Fiber Networks", "Fire Stations", "Police Stations", "Public Hospitals"], "Advanced": ["Public Schools as Infrastructure", "Public Libraries", "Courthouses and Civic Buildings", "ISO 55000 Asset Management", "Pavement Condition Rating (PASER)", "National Bridge Inspection Standards (NBIS)", "Lifecycle Cost Analysis", "Capital Improvement Planning", "GIS Asset Inventories", "Infrastructure Resilience and Climate Adaptation"]};
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
var gen={version:"jahdb-public-infrastructure-assets-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("public-infrastructure-assets",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
