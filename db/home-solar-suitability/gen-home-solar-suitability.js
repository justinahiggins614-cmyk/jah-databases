(function(){'use strict';
/* JAH The Home Solar Suitability Database generator — jahdb-home-solar-suitability-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HSS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Home Solar Suitability: Reading Your Land — foundations",
  "Home Solar Suitability: Soil Testing Basics — foundations",
  "Home Solar Suitability: Understanding Soil Life — foundations",
  "Home Solar Suitability: Water: Capture and Use — foundations",
  "Home Solar Suitability: Composting That Works — foundations",
  "Home Solar Suitability: Planting by the Season — foundations",
  "Home Solar Suitability: Pest Identification — foundations",
  "Home Solar Suitability: Disease Diagnosis — foundations",
  "Home Solar Suitability: Weed Strategy — foundations",
  "Home Solar Suitability: Fertilizing Wisely — foundations",
  "Home Solar Suitability: Pollinators and Beneficials — foundations",
  "Home Solar Suitability: Saving Seeds — foundations"
 ],
 "compounded": [
  "Home Solar Suitability: Season Extension — compounded",
  "Home Solar Suitability: Small Livestock Basics — compounded",
  "Home Solar Suitability: Reading the Weather — compounded",
  "Home Solar Suitability: Air Quality Awareness — compounded",
  "Home Solar Suitability: Invasive Species Watch — compounded",
  "Home Solar Suitability: Native Plants Power — compounded",
  "Home Solar Suitability: Trees: Planting and Care — compounded",
  "Home Solar Suitability: Home Solar Assessment — compounded",
  "Home Solar Suitability: Energy Saving at Home — compounded",
  "Home Solar Suitability: Local Environmental Action — compounded",
  "Home Solar Suitability: Advanced: Soil Regeneration — compounded",
  "Home Solar Suitability: Advanced: Integrated Pest Management — compounded"
 ],
 "advanced": [
  "Home Solar Suitability: Advanced: Water Systems Design — advanced",
  "Home Solar Suitability: Advanced: Agroforestry Basics — advanced",
  "Home Solar Suitability: Advanced: Seed Saving Mastery — advanced",
  "Home Solar Suitability: Advanced: Farm Business Basics — advanced",
  "Home Solar Suitability: Advanced: Climate Adaptation — advanced",
  "Home Solar Suitability: Advanced: Restoration Ecology — advanced",
  "Home Solar Suitability: Advanced: Community Food Systems — advanced",
  "Home Solar Suitability: Advanced: Teaching Land Skills — advanced",
  "Home Solar Suitability: Advanced: The 50-Year Land Plan — advanced",
  "Home Solar Suitability: Advanced: Monitoring Ecosystems — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Home Solar Suitability Database — structural study\n"
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
var gen={version:'jahdb-home-solar-suitability-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('home-solar-suitability',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
