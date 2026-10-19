(function(){'use strict';
/* JAH The Fertilizer Planning Signature Database generator — jahdb-fertilizer-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FPS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Fertilizer Planning (Signature): Reading Your Land — foundations",
  "Fertilizer Planning (Signature): Soil Testing Basics — foundations",
  "Fertilizer Planning (Signature): Understanding Soil Life — foundations",
  "Fertilizer Planning (Signature): Water: Capture and Use — foundations",
  "Fertilizer Planning (Signature): Composting That Works — foundations",
  "Fertilizer Planning (Signature): Planting by the Season — foundations",
  "Fertilizer Planning (Signature): Pest Identification — foundations",
  "Fertilizer Planning (Signature): Disease Diagnosis — foundations",
  "Fertilizer Planning (Signature): Weed Strategy — foundations",
  "Fertilizer Planning (Signature): Fertilizing Wisely — foundations",
  "Fertilizer Planning (Signature): Pollinators and Beneficials — foundations",
  "Fertilizer Planning (Signature): Saving Seeds — foundations"
 ],
 "compounded": [
  "Fertilizer Planning (Signature): Season Extension — compounded",
  "Fertilizer Planning (Signature): Small Livestock Basics — compounded",
  "Fertilizer Planning (Signature): Reading the Weather — compounded",
  "Fertilizer Planning (Signature): Air Quality Awareness — compounded",
  "Fertilizer Planning (Signature): Invasive Species Watch — compounded",
  "Fertilizer Planning (Signature): Native Plants Power — compounded",
  "Fertilizer Planning (Signature): Trees: Planting and Care — compounded",
  "Fertilizer Planning (Signature): Home Solar Assessment — compounded",
  "Fertilizer Planning (Signature): Energy Saving at Home — compounded",
  "Fertilizer Planning (Signature): Local Environmental Action — compounded",
  "Fertilizer Planning (Signature): Advanced: Soil Regeneration — compounded",
  "Fertilizer Planning (Signature): Advanced: Integrated Pest Management — compounded"
 ],
 "advanced": [
  "Fertilizer Planning (Signature): Advanced: Water Systems Design — advanced",
  "Fertilizer Planning (Signature): Advanced: Agroforestry Basics — advanced",
  "Fertilizer Planning (Signature): Advanced: Seed Saving Mastery — advanced",
  "Fertilizer Planning (Signature): Advanced: Farm Business Basics — advanced",
  "Fertilizer Planning (Signature): Advanced: Climate Adaptation — advanced",
  "Fertilizer Planning (Signature): Advanced: Restoration Ecology — advanced",
  "Fertilizer Planning (Signature): Advanced: Community Food Systems — advanced",
  "Fertilizer Planning (Signature): Advanced: Teaching Land Skills — advanced",
  "Fertilizer Planning (Signature): Advanced: The 50-Year Land Plan — advanced",
  "Fertilizer Planning (Signature): Advanced: Monitoring Ecosystems — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Fertilizer Planning Signature Database — structural study\n"
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
    name:topic+' — signature-original record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature-original record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-fertilizer-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fertilizer-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
