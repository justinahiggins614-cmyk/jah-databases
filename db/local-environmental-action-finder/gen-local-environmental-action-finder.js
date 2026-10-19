(function(){'use strict';
/* JAH The Local Environmental Action Finder Database generator — jahdb-local-environmental-action-finder-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LEAF-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Local Environmental Action Finder: Reading Your Land — foundations",
  "Local Environmental Action Finder: Soil Testing Basics — foundations",
  "Local Environmental Action Finder: Understanding Soil Life — foundations",
  "Local Environmental Action Finder: Water: Capture and Use — foundations",
  "Local Environmental Action Finder: Composting That Works — foundations",
  "Local Environmental Action Finder: Planting by the Season — foundations",
  "Local Environmental Action Finder: Pest Identification — foundations",
  "Local Environmental Action Finder: Disease Diagnosis — foundations",
  "Local Environmental Action Finder: Weed Strategy — foundations",
  "Local Environmental Action Finder: Fertilizing Wisely — foundations",
  "Local Environmental Action Finder: Pollinators and Beneficials — foundations",
  "Local Environmental Action Finder: Saving Seeds — foundations"
 ],
 "compounded": [
  "Local Environmental Action Finder: Season Extension — compounded",
  "Local Environmental Action Finder: Small Livestock Basics — compounded",
  "Local Environmental Action Finder: Reading the Weather — compounded",
  "Local Environmental Action Finder: Air Quality Awareness — compounded",
  "Local Environmental Action Finder: Invasive Species Watch — compounded",
  "Local Environmental Action Finder: Native Plants Power — compounded",
  "Local Environmental Action Finder: Trees: Planting and Care — compounded",
  "Local Environmental Action Finder: Home Solar Assessment — compounded",
  "Local Environmental Action Finder: Energy Saving at Home — compounded",
  "Local Environmental Action Finder: Local Environmental Action — compounded",
  "Local Environmental Action Finder: Advanced: Soil Regeneration — compounded",
  "Local Environmental Action Finder: Advanced: Integrated Pest Management — compounded"
 ],
 "advanced": [
  "Local Environmental Action Finder: Advanced: Water Systems Design — advanced",
  "Local Environmental Action Finder: Advanced: Agroforestry Basics — advanced",
  "Local Environmental Action Finder: Advanced: Seed Saving Mastery — advanced",
  "Local Environmental Action Finder: Advanced: Farm Business Basics — advanced",
  "Local Environmental Action Finder: Advanced: Climate Adaptation — advanced",
  "Local Environmental Action Finder: Advanced: Restoration Ecology — advanced",
  "Local Environmental Action Finder: Advanced: Community Food Systems — advanced",
  "Local Environmental Action Finder: Advanced: Teaching Land Skills — advanced",
  "Local Environmental Action Finder: Advanced: The 50-Year Land Plan — advanced",
  "Local Environmental Action Finder: Advanced: Monitoring Ecosystems — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Local Environmental Action Finder Database — structural study\n"
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
var gen={version:'jahdb-local-environmental-action-finder-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('local-environmental-action-finder',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
