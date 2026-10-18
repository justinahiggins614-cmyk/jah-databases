(function(){'use strict';
/* JAH The Carnivorous Plants Signature Database generator — jahdb-carnivorous-plants-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CVPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Carnivorous Plants 101 (Signature Edition) \u2014 Foundations",
  "Why Plants Eat Meat (Signature Edition) \u2014 Foundations",
  "The Venus Flytrap (Dionaea muscipula) (Signature Edition) \u2014 Foundations",
  "Pitcher Plants (Sarracenia) (Signature Edition) \u2014 Foundations",
  "Tropical Pitcher Plants (Nepenthes) (Signature Edition) \u2014 Foundations",
  "Sundews (Drosera) (Signature Edition) \u2014 Foundations",
  "Butterworts (Pinguicula) (Signature Edition) \u2014 Foundations",
  "Bladderworts (Utricularia) (Signature Edition) \u2014 Foundations",
  "Cobra Lily (Darlingtonia californica) (Signature Edition) \u2014 Foundations",
  "Albany Pitcher (Cephalotus follicularis) (Signature Edition) \u2014 Foundations",
  "How Traps Work: The Five Designs (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Snap Traps: The Mechanics (Signature Edition) \u2014 Compounded",
  "Pitfall Traps: The Mechanics (Signature Edition) \u2014 Compounded",
  "Flypaper Traps: The Mechanics (Signature Edition) \u2014 Compounded",
  "Suction Traps: The Mechanics (Signature Edition) \u2014 Compounded",
  "Lobster-Pot Traps (Signature Edition) \u2014 Compounded",
  "Digestion: Enzymes and Partners (Signature Edition) \u2014 Compounded",
  "What Prey They Catch (Signature Edition) \u2014 Compounded",
  "Bog Habitats (Signature Edition) \u2014 Compounded",
  "Growing Venus Flytraps (Signature Edition) \u2014 Compounded",
  "Growing Tropical Pitchers (Signature Edition) \u2014 Compounded",
  "Growing Sundews (Signature Edition) \u2014 Compounded",
  "Feeding Pet Carnivorous Plants (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "The Cost of Carnivory (Signature Edition) \u2014 Advanced",
  "Evolution of Traps (Signature Edition) \u2014 Advanced",
  "Darwin and Insectivorous Plants (Signature Edition) \u2014 Advanced",
  "Conservation: Vanishing Bogs (Signature Edition) \u2014 Advanced",
  "The Poaching Crisis (Signature Edition) \u2014 Advanced",
  "Tissue Culture and Cultivars (Signature Edition) \u2014 Advanced",
  "Hybrid Pitcher Plants (Signature Edition) \u2014 Advanced",
  "Carnivorous Plant Societies (Signature Edition) \u2014 Advanced",
  "Photographing Carnivorous Plants (Signature Edition) \u2014 Advanced",
  "Building a Bog Garden (Signature Edition) \u2014 Advanced",
  "The Hungry Garden: A Capstone (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Carnivorous Plant Study — "+safe+"\n"
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
    name:topic+' — carnivorous plant record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A carnivorous plant record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"carnivorous-plant-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-carnivorous-plants-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('carnivorous-plants-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
