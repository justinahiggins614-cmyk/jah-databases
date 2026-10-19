(function(){'use strict';
/* JAH The Food Recall Verification Database generator — jahdb-food-recall-verification-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FRV-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Food Recall Verification: Reading Your Land — foundations",
  "Food Recall Verification: Soil Testing Basics — foundations",
  "Food Recall Verification: Understanding Soil Life — foundations",
  "Food Recall Verification: Water: Capture and Use — foundations",
  "Food Recall Verification: Composting That Works — foundations",
  "Food Recall Verification: Planting by the Season — foundations",
  "Food Recall Verification: Pest Identification — foundations",
  "Food Recall Verification: Disease Diagnosis — foundations",
  "Food Recall Verification: Weed Strategy — foundations",
  "Food Recall Verification: Fertilizing Wisely — foundations",
  "Food Recall Verification: Pollinators and Beneficials — foundations",
  "Food Recall Verification: Saving Seeds — foundations"
 ],
 "compounded": [
  "Food Recall Verification: Season Extension — compounded",
  "Food Recall Verification: Small Livestock Basics — compounded",
  "Food Recall Verification: Reading the Weather — compounded",
  "Food Recall Verification: Air Quality Awareness — compounded",
  "Food Recall Verification: Invasive Species Watch — compounded",
  "Food Recall Verification: Native Plants Power — compounded",
  "Food Recall Verification: Trees: Planting and Care — compounded",
  "Food Recall Verification: Home Solar Assessment — compounded",
  "Food Recall Verification: Energy Saving at Home — compounded",
  "Food Recall Verification: Local Environmental Action — compounded",
  "Food Recall Verification: Advanced: Soil Regeneration — compounded",
  "Food Recall Verification: Advanced: Integrated Pest Management — compounded"
 ],
 "advanced": [
  "Food Recall Verification: Advanced: Water Systems Design — advanced",
  "Food Recall Verification: Advanced: Agroforestry Basics — advanced",
  "Food Recall Verification: Advanced: Seed Saving Mastery — advanced",
  "Food Recall Verification: Advanced: Farm Business Basics — advanced",
  "Food Recall Verification: Advanced: Climate Adaptation — advanced",
  "Food Recall Verification: Advanced: Restoration Ecology — advanced",
  "Food Recall Verification: Advanced: Community Food Systems — advanced",
  "Food Recall Verification: Advanced: Teaching Land Skills — advanced",
  "Food Recall Verification: Advanced: The 50-Year Land Plan — advanced",
  "Food Recall Verification: Advanced: Monitoring Ecosystems — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Food Recall Verification Database — structural study\n"
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
    name:topic+' — practical guidance record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A practical guidance record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
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
var gen={version:'jahdb-food-recall-verification-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('food-recall-verification',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
