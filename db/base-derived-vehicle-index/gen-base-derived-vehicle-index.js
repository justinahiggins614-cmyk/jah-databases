(function(){'use strict';
/* JAH Vehicle Master Index Database generator — "jahdb-base-derived-vehicle-index-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BVI-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Vehicle Master Index", "How to Use This Index", "Member: Vehicle Checklists", "Member: Vehicle History Interpretation", "Member: Vehicle Maintenance Schedules", "Member: Vehicle Repair Cost Estimation", "Member: Aircraft Records", "Member: Vehicle Blueprints", "Public vs Signature Editions in the Index", "The 7-DB Map: Which DB Answers Which Question", "How the Index Stays Current", "Quick-Start: Three Questions, Three DBs"], "Compounded": ["The Used-Car Buying Workflow", "Reading a Vehicle History Report", "The Maintenance Calendar Build", "Estimating a Repair Before the Shop", "Aircraft Ownership: The Records Path", "Checklists for Road Trips", "Seasonal Maintenance Swaps", "The 100k-Mile Service Plan", "Repair vs Replace: The Math", "Blueprint Reading for Owners", "The Pre-Purchase Inspection", "Keeping the Service Binder"], "Advanced": ["Total Cost of Ownership Model", "Fleet Maintenance Synthesis", "The Lemon-Law Paper Trail", "Restoration Project Planning", "Aircraft Annual Inspection Prep", "The Index as Research Method", "Cross-DB Verification Technique", "Building Your Own Vehicle Dossier", "The 200k-Mile Club: Longevity Synthesis", "The Vehicle Index Legacy"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — base-derived-vehicle-index demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — master index record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A master index record study. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest-sample",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-base-derived-vehicle-index-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("base-derived-vehicle-index",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
