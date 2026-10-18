(function(){'use strict';
/* JAH The Nature Detective Classroom generator — jahdb-db-nature-detective-classroom-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NDCS-";
var FIELDS=["Observation","Identification","Ecosystems"];
var TOPICS={
 "Observation": [
  "The Detective's Kit (Signature Edition) - Observation",
  "Sit Spots: Watching Wild (Signature Edition) - Observation",
  "Keeping a Field Journal (Signature Edition) - Observation",
  "Tracking: Reading Footprints (Signature Edition) - Observation",
  "Bird Language (Signature Edition) - Observation",
  "Noticing Plants (Signature Edition) - Observation",
  "Weather Reading Outdoors (Signature Edition) - Observation",
  "Night Investigation (Signature Edition) - Observation",
  "Sound Mapping (Signature Edition) - Observation",
  "Photo Documentation (Signature Edition) - Observation",
  "Questioning Nature (Signature Edition) - Observation",
  "Leave No Trace Detecting (Signature Edition) - Observation"
 ],
 "Identification": [
  "Identifying Birds (Signature Edition) - Identification",
  "Identifying Trees (Signature Edition) - Identification",
  "Identifying Insects (Signature Edition) - Identification",
  "Identifying Mammals (Signature Edition) - Identification",
  "Wildflowers and Plants (Signature Edition) - Identification",
  "Fungi: The Hidden Kingdom (Signature Edition) - Identification",
  "Rocks and Minerals (Signature Edition) - Identification",
  "Clouds and Sky (Signature Edition) - Identification",
  "Using Field Guides (Signature Edition) - Identification",
  "Citizen Science: Your Data Matters (Signature Edition) - Identification",
  "Identifying Animal Signs (Signature Edition) - Identification"
 ],
 "Ecosystems": [
  "Food Webs: Who Eats Whom (Signature Edition) - Ecosystems",
  "Habitats: Where Life Lives (Signature Edition) - Ecosystems",
  "Succession: Nature's Slow Change (Signature Edition) - Ecosystems",
  "Water Ecosystems (Signature Edition) - Ecosystems",
  "Forests: Vertical Cities (Signature Edition) - Ecosystems",
  "Grasslands and Meadows (Signature Edition) - Ecosystems",
  "Urban Nature (Signature Edition) - Ecosystems",
  "Invasive Species (Signature Edition) - Ecosystems",
  "Conservation: The Detective's Duty (Signature Edition) - Ecosystems",
  "Seasons: The Great Cycle (Signature Edition) - Ecosystems",
  "The Ecosystem Detective Agency (Signature Edition) - Ecosystems"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nature Detective Study — "+safe+"\n"
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
    name:topic+' — nature lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A nature lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"nature-detective-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-nature-detective-classroom-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-nature-detective-classroom-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
