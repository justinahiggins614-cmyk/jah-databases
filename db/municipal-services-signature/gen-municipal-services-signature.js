(function(){'use strict';
/* JAH The Municipal Services Signature Database generator — jahdb-municipal-services-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MUNISVC-SIG-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Building Permits (Signature Edition)", "Occupancy Permits (Signature Edition)", "Electrical Permits (Signature Edition)", "Plumbing Permits (Signature Edition)", "Mechanical and HVAC Permits (Signature Edition)", "Demolition Permits (Signature Edition)", "Zoning Permits (Signature Edition)", "Sign Permits (Signature Edition)", "Special Event Permits (Signature Edition)", "Home Occupation Permits (Signature Edition)", "Right-of-Way Permits (Signature Edition)", "Grading Permits (Signature Edition)"], "Compounded": ["Curbside Waste Collection (Signature Edition)", "Recycling Programs (Signature Edition)", "Yard Waste and Composting (Signature Edition)", "Bulk Waste Pickup (Signature Edition)", "Household Hazardous Waste (Signature Edition)", "Water Service (Signature Edition)", "Sewer Service (Signature Edition)", "Stormwater Utility Service (Signature Edition)", "Snow Removal (Signature Edition)", "Street Sweeping (Signature Edition)", "Pothole Repair (Signature Edition)", "Urban Forestry and Tree Trimming (Signature Edition)"], "Advanced": ["311 Service Request Systems (Signature Edition)", "Zoning Variances (Signature Edition)", "Conditional Use Permits (Signature Edition)", "Subdivision Review (Signature Edition)", "Site Plan Review (Signature Edition)", "Code Enforcement (Signature Edition)", "Animal Control (Signature Edition)", "Parking Enforcement (Signature Edition)", "Public Health Inspections (Signature Edition)", "Fire Inspections (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Municipal Service Study — "+safe+"\n"
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
    name:topic+' — municipal service record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A municipal service record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"service-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-municipal-services-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("municipal-services-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
