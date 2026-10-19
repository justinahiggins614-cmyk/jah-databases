(function(){'use strict';
/* JAH The Local Environmental Action Finder Signature Database generator — jahdb-local-environmental-action-finder-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LEAFS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Local Environmental Action Finder (Signature): Reading Your Land — foundations",
  "Local Environmental Action Finder (Signature): Soil Testing Basics — foundations",
  "Local Environmental Action Finder (Signature): Understanding Soil Life — foundations",
  "Local Environmental Action Finder (Signature): Water: Capture and Use — foundations",
  "Local Environmental Action Finder (Signature): Composting That Works — foundations",
  "Local Environmental Action Finder (Signature): Planting by the Season — foundations",
  "Local Environmental Action Finder (Signature): Pest Identification — foundations",
  "Local Environmental Action Finder (Signature): Disease Diagnosis — foundations",
  "Local Environmental Action Finder (Signature): Weed Strategy — foundations",
  "Local Environmental Action Finder (Signature): Fertilizing Wisely — foundations",
  "Local Environmental Action Finder (Signature): Pollinators and Beneficials — foundations",
  "Local Environmental Action Finder (Signature): Saving Seeds — foundations"
 ],
 "compounded": [
  "Local Environmental Action Finder (Signature): Season Extension — compounded",
  "Local Environmental Action Finder (Signature): Small Livestock Basics — compounded",
  "Local Environmental Action Finder (Signature): Reading the Weather — compounded",
  "Local Environmental Action Finder (Signature): Air Quality Awareness — compounded",
  "Local Environmental Action Finder (Signature): Invasive Species Watch — compounded",
  "Local Environmental Action Finder (Signature): Native Plants Power — compounded",
  "Local Environmental Action Finder (Signature): Trees: Planting and Care — compounded",
  "Local Environmental Action Finder (Signature): Home Solar Assessment — compounded",
  "Local Environmental Action Finder (Signature): Energy Saving at Home — compounded",
  "Local Environmental Action Finder (Signature): Local Environmental Action — compounded",
  "Local Environmental Action Finder (Signature): Advanced: Soil Regeneration — compounded",
  "Local Environmental Action Finder (Signature): Advanced: Integrated Pest Management — compounded"
 ],
 "advanced": [
  "Local Environmental Action Finder (Signature): Advanced: Water Systems Design — advanced",
  "Local Environmental Action Finder (Signature): Advanced: Agroforestry Basics — advanced",
  "Local Environmental Action Finder (Signature): Advanced: Seed Saving Mastery — advanced",
  "Local Environmental Action Finder (Signature): Advanced: Farm Business Basics — advanced",
  "Local Environmental Action Finder (Signature): Advanced: Climate Adaptation — advanced",
  "Local Environmental Action Finder (Signature): Advanced: Restoration Ecology — advanced",
  "Local Environmental Action Finder (Signature): Advanced: Community Food Systems — advanced",
  "Local Environmental Action Finder (Signature): Advanced: Teaching Land Skills — advanced",
  "Local Environmental Action Finder (Signature): Advanced: The 50-Year Land Plan — advanced",
  "Local Environmental Action Finder (Signature): Advanced: Monitoring Ecosystems — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Local Environmental Action Finder Signature Database — structural study\n"
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
var gen={version:'jahdb-local-environmental-action-finder-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('local-environmental-action-finder-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
