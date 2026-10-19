(function(){'use strict';
/* JAH Signature Home Maintenance Database generator — "jahdb-everyday-home-maintenance-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EHMS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Changing the HVAC Filter (Signature Edition)", "Smoke and CO Detectors (Signature Edition)", "Cleaning Gutters (Signature Edition)", "Caulking: Tubs and Windows (Signature Edition)", "Fixing a Running Toilet (Signature Edition)", "Garbage Disposal Reset (Signature Edition)", "Resetting a Breaker (Signature Edition)", "Water Heater Maintenance (Signature Edition)", "Cleaning the Dryer Vent (Signature Edition)", "Lawn Care Basics (Signature Edition)", "Exterior Paint Touch-Up (Signature Edition)", "Knowing Your Shutoffs (Signature Edition)"], "Compounded": ["Fall Furnace Service (Signature Edition)", "Spring AC Service (Signature Edition)", "Roof Inspection (Signature Edition)", "Sump Pump Test (Signature Edition)", "Deck Staining (Signature Edition)", "Septic Pumping (Signature Edition)", "Chimney Sweeping (Signature Edition)", "Garage Door Maintenance (Signature Edition)", "Attic Insulation (Signature Edition)", "Foundation Monitoring (Signature Edition)", "Plumbing Lifespan (Signature Edition)", "Electrical Panel Basics (Signature Edition)"], "Advanced": ["Roof Replacement Planning (Signature Edition)", "HVAC Replacement (Signature Edition)", "Kitchen Remodel Planning (Signature Edition)", "Bathroom Renovation (Signature Edition)", "Window Replacement (Signature Edition)", "Siding Maintenance (Signature Edition)", "Long-Term Stewardship (Signature Edition)", "Home Energy Audit (Signature Edition)", "Aging in Place (Signature Edition)", "The Home's Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — everyday-home-maintenance-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original everyday record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original everyday record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-everyday-home-maintenance-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("everyday-home-maintenance-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
