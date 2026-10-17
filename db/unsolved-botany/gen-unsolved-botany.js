(function(){'use strict';
/* JAH The Unsolved Botany Database generator — jahdb-unsolved-botany-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USBO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Leaves Turn Color in Autumn - Foundations",
  "How the Venus Flytrap Counts Its Prey - Foundations",
  "How Plants Find the Light - Foundations",
  "How a Seed Knows When to Wake Up - Foundations",
  "What Tells a Plant It Is Time to Flower - Foundations",
  "Why Some Plants Eat Animals - Foundations",
  "Do Plants Warn Each Other of Attack - Foundations",
  "How Plants Remember Winter - Foundations",
  "Why Bristlecone Pines Live Five Millennia - Foundations",
  "The Wood Wide Web: Do Fungi Really Feed Trees - Foundations",
  "Do Plants Think: The Plant Cognition Debate - Foundations"
 ],
 "Compounded": [
  "How Trees Drink From a Hundred Meters Up - Compounded",
  "The Full Map of Plant Hormone Crosstalk - Compounded",
  "How Plants Fight Disease - Compounded",
  "The Root Microbiome: Who Lives Down There - Compounded",
  "What Mycorrhizal Networks Actually Do - Compounded",
  "The Complete Genetics of Drought Tolerance - Compounded",
  "Why C4 Photosynthesis Evolved More Than Sixty Times - Compounded",
  "Photorespiration: The Wasteful Flaw - Compounded",
  "Nitrogen Fixation for Cereals - Compounded",
  "How Leaves Rewire Light Capture - Compounded",
  "The Epigenetic Memory of Plants - Compounded",
  "The Electrical Language of Plants - Compounded"
 ],
 "Advanced": [
  "The Field Efficiency Gap: Why Crops Capture Barely One Percent of Sunlight - Advanced",
  "Rubisco: Engineering the World's Slowest Enzyme - Advanced",
  "Crop Yield Ceilings: How Much Can a Field Ever Give - Advanced",
  "Engineering C4 Rice: Rewiring a Staple - Advanced",
  "The Genomic Architecture of a Five-Thousand-Year Life - Advanced",
  "The Origin of Land Plants - Advanced",
  "The Chloroplast's Long Journey: Full Endosymbiosis Mechanics - Advanced",
  "Synthetic Chloroplasts Built From Scratch - Advanced",
  "The Complete Mechanics of Photosynthesis Optimization - Advanced",
  "Designing a De Novo Photosynthetic Organism - Advanced",
  "Plant Consciousness: The Hardest Question in Botany - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Botany Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-botany-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-botany-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-botany',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
