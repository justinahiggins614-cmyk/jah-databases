(function(){'use strict';
/* JAH The Botany Database generator — jahdb-botany-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BOT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Plant: The Green Kingdom \u2014 Foundations",
  "The Plant Cell: Wall, Vacuole, and Plastids \u2014 Foundations",
  "Roots: Anchorage and Absorption \u2014 Foundations",
  "Stems: Support and Transport \u2014 Foundations",
  "Leaves: The Solar Collectors \u2014 Foundations",
  "Photosynthesis I: The Light Reactions \u2014 Foundations",
  "Photosynthesis II: The Calvin Cycle \u2014 Foundations",
  "Water Transport: Transpiration and the Xylem \u2014 Foundations",
  "Plant Life Cycles: Annuals, Biennials, and Perennials \u2014 Foundations"
 ],
 "Compounded": [
  "Alternation of Generations: Two Bodies, One Life Cycle \u2014 Compounded",
  "Bryophytes: Mosses, Liverworts, and Hornworts \u2014 Compounded",
  "Ferns and Horsetails: The Seedless Vascular Plants \u2014 Compounded",
  "Gymnosperms: The Naked-Seed Plants \u2014 Compounded",
  "The Flower: Structure and Function \u2014 Compounded",
  "Angiosperms: The Flowering Revolution \u2014 Compounded",
  "Pollination: Partnerships and Strategies \u2014 Compounded",
  "Fruits and Seed Dispersal: Getting Away \u2014 Compounded",
  "Seeds and Germination: The Waiting Game \u2014 Compounded",
  "Plant Hormones: Auxin to Ethylene \u2014 Compounded",
  "Tropisms and Nastic Movements: Plants in Motion \u2014 Compounded",
  "C3, C4, and CAM: Photosynthetic Strategies \u2014 Compounded",
  "Mendel and Plant Genetics: The Pea Experiments \u2014 Compounded",
  "Mycorrhizae and Nitrogen Fixation: Root Alliances \u2014 Compounded",
  "Plant Ecology: Communities and Succession \u2014 Compounded",
  "Plant Taxonomy: The APG IV System \u2014 Compounded",
  "Carnivorous Plants: Traps and Lures \u2014 Compounded"
 ],
 "Advanced": [
  "Plant Pathology: Disease and Defense \u2014 Advanced",
  "Economic Botany: Crops that Feed the World \u2014 Advanced",
  "Secondary Metabolites: Medicine from Plants \u2014 Advanced",
  "Drought Physiology: How Plants Survive Dry \u2014 Advanced",
  "Plant Tissue Culture and Micropropagation \u2014 Advanced",
  "Grafting and Vegetative Propagation \u2014 Advanced",
  "Dendrochronology: Reading Tree Rings \u2014 Advanced",
  "Epiphytes: Life in the Canopy \u2014 Advanced",
  "Paleobotany: The Fossil Record of Plants \u2014 Advanced",
  "Plant Breeding and Crop Improvement \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Botany Study — "+safe+"\n"
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
    name:topic+' — botany record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A botany record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"botany-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-botany-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('botany',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
