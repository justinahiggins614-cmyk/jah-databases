(function(){'use strict';
/* JAH The Fertilizer Planning Database generator — jahdb-fertilizer-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FP-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Fertilizer Planning: Reading Your Land — foundations",
  "Fertilizer Planning: Soil Testing Basics — foundations",
  "Fertilizer Planning: Understanding Soil Life — foundations",
  "Fertilizer Planning: Water: Capture and Use — foundations",
  "Fertilizer Planning: Composting That Works — foundations",
  "Fertilizer Planning: Planting by the Season — foundations",
  "Fertilizer Planning: Pest Identification — foundations",
  "Fertilizer Planning: Disease Diagnosis — foundations",
  "Fertilizer Planning: Weed Strategy — foundations",
  "Fertilizer Planning: Fertilizing Wisely — foundations",
  "Fertilizer Planning: Pollinators and Beneficials — foundations",
  "Fertilizer Planning: Saving Seeds — foundations"
 ],
 "compounded": [
  "Fertilizer Planning: Season Extension — compounded",
  "Fertilizer Planning: Small Livestock Basics — compounded",
  "Fertilizer Planning: Reading the Weather — compounded",
  "Fertilizer Planning: Air Quality Awareness — compounded",
  "Fertilizer Planning: Invasive Species Watch — compounded",
  "Fertilizer Planning: Native Plants Power — compounded",
  "Fertilizer Planning: Trees: Planting and Care — compounded",
  "Fertilizer Planning: Home Solar Assessment — compounded",
  "Fertilizer Planning: Energy Saving at Home — compounded",
  "Fertilizer Planning: Local Environmental Action — compounded",
  "Fertilizer Planning: Advanced: Soil Regeneration — compounded",
  "Fertilizer Planning: Advanced: Integrated Pest Management — compounded"
 ],
 "advanced": [
  "Fertilizer Planning: Advanced: Water Systems Design — advanced",
  "Fertilizer Planning: Advanced: Agroforestry Basics — advanced",
  "Fertilizer Planning: Advanced: Seed Saving Mastery — advanced",
  "Fertilizer Planning: Advanced: Farm Business Basics — advanced",
  "Fertilizer Planning: Advanced: Climate Adaptation — advanced",
  "Fertilizer Planning: Advanced: Restoration Ecology — advanced",
  "Fertilizer Planning: Advanced: Community Food Systems — advanced",
  "Fertilizer Planning: Advanced: Teaching Land Skills — advanced",
  "Fertilizer Planning: Advanced: The 50-Year Land Plan — advanced",
  "Fertilizer Planning: Advanced: Monitoring Ecosystems — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Fertilizer Planning Database — structural study\n"
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
var gen={version:'jahdb-fertilizer-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fertilizer-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
