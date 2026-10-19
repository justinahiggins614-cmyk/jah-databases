(function(){'use strict';
/* JAH The Invasive Species Identification Database generator — jahdb-invasive-species-identification-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ISI-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Invasive Species Identification: Reading Your Land — foundations",
  "Invasive Species Identification: Soil Testing Basics — foundations",
  "Invasive Species Identification: Understanding Soil Life — foundations",
  "Invasive Species Identification: Water: Capture and Use — foundations",
  "Invasive Species Identification: Composting That Works — foundations",
  "Invasive Species Identification: Planting by the Season — foundations",
  "Invasive Species Identification: Pest Identification — foundations",
  "Invasive Species Identification: Disease Diagnosis — foundations",
  "Invasive Species Identification: Weed Strategy — foundations",
  "Invasive Species Identification: Fertilizing Wisely — foundations",
  "Invasive Species Identification: Pollinators and Beneficials — foundations",
  "Invasive Species Identification: Saving Seeds — foundations"
 ],
 "compounded": [
  "Invasive Species Identification: Season Extension — compounded",
  "Invasive Species Identification: Small Livestock Basics — compounded",
  "Invasive Species Identification: Reading the Weather — compounded",
  "Invasive Species Identification: Air Quality Awareness — compounded",
  "Invasive Species Identification: Invasive Species Watch — compounded",
  "Invasive Species Identification: Native Plants Power — compounded",
  "Invasive Species Identification: Trees: Planting and Care — compounded",
  "Invasive Species Identification: Home Solar Assessment — compounded",
  "Invasive Species Identification: Energy Saving at Home — compounded",
  "Invasive Species Identification: Local Environmental Action — compounded",
  "Invasive Species Identification: Advanced: Soil Regeneration — compounded",
  "Invasive Species Identification: Advanced: Integrated Pest Management — compounded"
 ],
 "advanced": [
  "Invasive Species Identification: Advanced: Water Systems Design — advanced",
  "Invasive Species Identification: Advanced: Agroforestry Basics — advanced",
  "Invasive Species Identification: Advanced: Seed Saving Mastery — advanced",
  "Invasive Species Identification: Advanced: Farm Business Basics — advanced",
  "Invasive Species Identification: Advanced: Climate Adaptation — advanced",
  "Invasive Species Identification: Advanced: Restoration Ecology — advanced",
  "Invasive Species Identification: Advanced: Community Food Systems — advanced",
  "Invasive Species Identification: Advanced: Teaching Land Skills — advanced",
  "Invasive Species Identification: Advanced: The 50-Year Land Plan — advanced",
  "Invasive Species Identification: Advanced: Monitoring Ecosystems — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Invasive Species Identification Database — structural study\n"
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
var gen={version:'jahdb-invasive-species-identification-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('invasive-species-identification',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
