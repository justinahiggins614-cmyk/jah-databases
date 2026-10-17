(function(){'use strict';
/* JAH The Entomology Signature Database generator — jahdb-entomology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ESG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is an Insect: The Six-Legged Kingdom (Signature Edition) \u2014 Foundations",
  "Insect Anatomy I: Head, Thorax, Abdomen (Signature Edition) \u2014 Foundations",
  "The Exoskeleton and Molting (Signature Edition) \u2014 Foundations",
  "Insect Legs: Walking, Jumping, Swimming (Signature Edition) \u2014 Foundations",
  "Insect Mouthparts: Chewing, Piercing, Sponging (Signature Edition) \u2014 Foundations",
  "Insect Eyes and Vision (Signature Edition) \u2014 Foundations",
  "Antennae and Smell (Signature Edition) \u2014 Foundations",
  "Insect Wings and Flight (Signature Edition) \u2014 Foundations",
  "Insect Blood and Breathing: Hemolymph and Tracheae (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Metamorphosis I: Hemimetaboly (Incomplete) (Signature Edition) \u2014 Compounded",
  "Metamorphosis II: Holometaboly (Complete) (Signature Edition) \u2014 Compounded",
  "The Insect Orders: Coleoptera, the Beetles (Signature Edition) \u2014 Compounded",
  "The Insect Orders: Diptera and Hymenoptera (Signature Edition) \u2014 Compounded",
  "The Insect Orders: Lepidoptera, Orthoptera, Hemiptera (Signature Edition) \u2014 Compounded",
  "Insect Taxonomy and Classification (Signature Edition) \u2014 Compounded",
  "Insect Behavior: Communication (Signature Edition) \u2014 Compounded",
  "Social Insects: Ants and Termites (Signature Edition) \u2014 Compounded",
  "Social Insects: Bees and Wasps (Signature Edition) \u2014 Compounded",
  "Pollination Ecology (Signature Edition) \u2014 Compounded",
  "Insect-Plant Interactions: Herbivory (Signature Edition) \u2014 Compounded",
  "Beneficial Insects: Predators and Parasitoids (Signature Edition) \u2014 Compounded",
  "Insect Physiology: The Nervous System (Signature Edition) \u2014 Compounded",
  "Insect Reproduction and Eggs (Signature Edition) \u2014 Compounded",
  "Insect Migration (Signature Edition) \u2014 Compounded",
  "Collection and Identification Methods (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Integrated Pest Management (Signature Edition) \u2014 Advanced",
  "Agricultural Entomology: Crop Pests (Signature Edition) \u2014 Advanced",
  "Medical and Veterinary Entomology: Vectors (Signature Edition) \u2014 Advanced",
  "Stored-Product Entomology (Signature Edition) \u2014 Advanced",
  "Insecticide Modes of Action and Resistance (Signature Edition) \u2014 Advanced",
  "Forensic Entomology (Signature Edition) \u2014 Advanced",
  "Insect Physiology: Diapause and Cold Hardiness (Signature Edition) \u2014 Advanced",
  "Insect Genetics and Genomics (Signature Edition) \u2014 Advanced",
  "Insect Diversity: Why Insects Rule (Signature Edition) \u2014 Advanced",
  "Urban Entomology: Bed Bugs, Cockroaches, Termites (Signature Edition) \u2014 Advanced",
  "Conservation of Insects: Pollinator Declines (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Entomology Study — "+safe+"\n"
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
    name:topic+' — entomology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A entomology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"entomology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-entomology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('entomology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
