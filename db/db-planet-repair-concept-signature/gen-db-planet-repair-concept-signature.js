(function(){'use strict';
/* JAH The Planet Repair Concept Signature Database generator — jahdb-db-planet-repair-concept-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPRCS-";
var FIELDS=["Land Repair","Water Repair","Sky Repair"];
var TOPICS={
 "Land Repair": [
  "The Rewilding Reserve (Signature Edition) \u2014 Land Repair",
  "The Signature Method for The Rewilding Reserve \u2014 Land Repair",
  "The Soil Regeneration (Signature Edition) \u2014 Land Repair",
  "The Signature Method for The Soil Regeneration \u2014 Land Repair",
  "The Forest Comeback (Signature Edition) \u2014 Land Repair",
  "The Signature Method for The Forest Comeback \u2014 Land Repair",
  "The Grassland Revival (Signature Edition) \u2014 Land Repair",
  "The Signature Method for The Grassland Revival \u2014 Land Repair",
  "The Urban Rewilding (Signature Edition) \u2014 Land Repair",
  "The Signature Method for The Urban Rewilding \u2014 Land Repair",
  "The Peatland Restoration (Signature Edition) \u2014 Land Repair",
  "The Signature Method for The Peatland Restoration \u2014 Land Repair",
  "The Restoration Designer's Method (Signature Edition) \u2014 Land Repair",
  "The Signature Method for The Restoration Designer's Method \u2014 Land Repair"
 ],
 "Water Repair": [
  "The Reef Restoration (Signature Edition) \u2014 Water Repair",
  "The Signature Method for The Reef Restoration \u2014 Water Repair",
  "The Wetland Return (Signature Edition) \u2014 Water Repair",
  "The Signature Method for The Wetland Return \u2014 Water Repair",
  "The River Unchaining (Signature Edition) \u2014 Water Repair",
  "The Signature Method for The River Unchaining \u2014 Water Repair",
  "The Mangrove Shield (Signature Edition) \u2014 Water Repair",
  "The Signature Method for The Mangrove Shield \u2014 Water Repair",
  "The Plastic Purge (Signature Edition) \u2014 Water Repair",
  "The Signature Method for The Plastic Purge \u2014 Water Repair",
  "The Deep Sea Protection (Signature Edition) \u2014 Water Repair",
  "The Signature Method for The Deep Sea Protection \u2014 Water Repair"
 ],
 "Sky Repair": [
  "The Air Cleaning (Signature Edition) \u2014 Sky Repair",
  "The Signature Method for The Air Cleaning \u2014 Sky Repair",
  "The Carbon Drawdown (Signature Edition) \u2014 Sky Repair",
  "The Signature Method for The Carbon Drawdown \u2014 Sky Repair",
  "The Dark Sky Restoration (Signature Edition) \u2014 Sky Repair",
  "The Signature Method for The Dark Sky Restoration \u2014 Sky Repair",
  "The Quiet Restoration (Signature Edition) \u2014 Sky Repair",
  "The Signature Method for The Quiet Restoration \u2014 Sky Repair"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Planet Repair Study — "+safe+"\n"
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
    name:topic+' — planet repair concept record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A planet repair concept record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-planet-repair-concept-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-planet-repair-concept-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
