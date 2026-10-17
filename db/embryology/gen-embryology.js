(function(){'use strict';
/* JAH The Embryology Database generator — jahdb-embryology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EBR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Embryology: The Science of Prenatal Development - Foundations",
  "Gametogenesis: Making the Reproductive Cells - Foundations",
  "Spermatogenesis: Building Sperm, Step by Step - Foundations",
  "Oogenesis: Building Eggs, From Fetus to Ovulation - Foundations",
  "Fertilization: The Moment of Conception - Foundations",
  "Cleavage: The First Divisions of the Zygote - Foundations",
  "Blastulation: Forming the Blastocyst - Foundations",
  "Implantation: Burrowing Into the Uterus - Foundations",
  "The Bilaminar Disc: Two Layers, One Future Body - Foundations",
  "The Trilaminar Disc: Three Germ Layers - Foundations",
  "Extraembryonic Membranes: The Support System - Foundations"
 ],
 "Compounded": [
  "Gastrulation: The Primitive Streak and the Body Plan - Compounded",
  "Neurulation: Building the Neural Tube - Compounded",
  "Body Axes: Head, Tail, Back, and Belly - Compounded",
  "Somitogenesis: Segmenting the Body - Compounded",
  "Folding of the Embryo: From Disc to Tube - Compounded",
  "The Placenta: The Organ That Feeds Two - Compounded",
  "The Heart: The First Working Organ - Compounded",
  "Vascular Development: Growing the Blood Vessels - Compounded",
  "Skeletal Development: Cartilage First, Bone Later - Compounded",
  "Muscle Development: From Myoblasts to Muscle - Compounded",
  "Skin Development: Building the Barrier - Compounded",
  "Lung Development: Branching Into Breathing - Compounded"
 ],
 "Advanced": [
  "Digestive System Development: The Rotating Gut - Advanced",
  "Urinary System Development: Three Kidneys in a Row - Advanced",
  "Genital Development: The Path to Male or Female - Advanced",
  "Nervous System Development: Wiring the Brain - Advanced",
  "Eye and Ear Development: The Senses Take Shape - Advanced",
  "Endocrine Development: Glands of Growth and Control - Advanced",
  "Developmental Genetics: Hox Genes and the Body Plan Code - Advanced",
  "Teratology: When Development Goes Wrong - Advanced",
  "Twinning: One Embryo Becomes Two - Advanced",
  "The Fetal Period: Growth, Week by Week - Advanced",
  "Assisted Reproduction: Science at Conception - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Embryology Study — "+safe+"\n"
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
    name:topic+' — embryology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A embryology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"embryology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-embryology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('embryology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
