(function(){'use strict';
/* JAH The Air Quality Interpretation Database generator — jahdb-air-quality-interpretation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AQI-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Air Quality Interpretation: Reading Your Land — foundations",
  "Air Quality Interpretation: Soil Testing Basics — foundations",
  "Air Quality Interpretation: Understanding Soil Life — foundations",
  "Air Quality Interpretation: Water: Capture and Use — foundations",
  "Air Quality Interpretation: Composting That Works — foundations",
  "Air Quality Interpretation: Planting by the Season — foundations",
  "Air Quality Interpretation: Pest Identification — foundations",
  "Air Quality Interpretation: Disease Diagnosis — foundations",
  "Air Quality Interpretation: Weed Strategy — foundations",
  "Air Quality Interpretation: Fertilizing Wisely — foundations",
  "Air Quality Interpretation: Pollinators and Beneficials — foundations",
  "Air Quality Interpretation: Saving Seeds — foundations"
 ],
 "compounded": [
  "Air Quality Interpretation: Season Extension — compounded",
  "Air Quality Interpretation: Small Livestock Basics — compounded",
  "Air Quality Interpretation: Reading the Weather — compounded",
  "Air Quality Interpretation: Air Quality Awareness — compounded",
  "Air Quality Interpretation: Invasive Species Watch — compounded",
  "Air Quality Interpretation: Native Plants Power — compounded",
  "Air Quality Interpretation: Trees: Planting and Care — compounded",
  "Air Quality Interpretation: Home Solar Assessment — compounded",
  "Air Quality Interpretation: Energy Saving at Home — compounded",
  "Air Quality Interpretation: Local Environmental Action — compounded",
  "Air Quality Interpretation: Advanced: Soil Regeneration — compounded",
  "Air Quality Interpretation: Advanced: Integrated Pest Management — compounded"
 ],
 "advanced": [
  "Air Quality Interpretation: Advanced: Water Systems Design — advanced",
  "Air Quality Interpretation: Advanced: Agroforestry Basics — advanced",
  "Air Quality Interpretation: Advanced: Seed Saving Mastery — advanced",
  "Air Quality Interpretation: Advanced: Farm Business Basics — advanced",
  "Air Quality Interpretation: Advanced: Climate Adaptation — advanced",
  "Air Quality Interpretation: Advanced: Restoration Ecology — advanced",
  "Air Quality Interpretation: Advanced: Community Food Systems — advanced",
  "Air Quality Interpretation: Advanced: Teaching Land Skills — advanced",
  "Air Quality Interpretation: Advanced: The 50-Year Land Plan — advanced",
  "Air Quality Interpretation: Advanced: Monitoring Ecosystems — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Air Quality Interpretation Database — structural study\n"
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
var gen={version:'jahdb-air-quality-interpretation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('air-quality-interpretation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
