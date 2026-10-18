(function(){'use strict';
/* JAH The Edible Wild Plants Signature Database generator — jahdb-edible-wild-plants-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EWPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Foraging Safety 101 (Signature Edition) \u2014 Foundations",
  "The Universal Edibility Test: Truth and Limits (Signature Edition) \u2014 Foundations",
  "Dandelion (Taraxacum officinale) (Signature Edition) \u2014 Foundations",
  "Chickweed (Stellaria media) (Signature Edition) \u2014 Foundations",
  "Purslane (Portulaca oleracea) (Signature Edition) \u2014 Foundations",
  "Plantain (Plantago major) (Signature Edition) \u2014 Foundations",
  "Wood Sorrel (Oxalis) (Signature Edition) \u2014 Foundations",
  "Wild Garlic and Ramps (Allium) (Signature Edition) \u2014 Foundations",
  "Stinging Nettle (Urtica dioica) (Signature Edition) \u2014 Foundations",
  "Cattail (Typha) (Signature Edition) \u2014 Foundations",
  "Acorns: The Forgotten Staple (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Blackberry and Raspberry (Rubus) (Signature Edition) \u2014 Compounded",
  "Elderberry (Sambucus): Cooked Only (Signature Edition) \u2014 Compounded",
  "Wild Strawberry (Fragaria) (Signature Edition) \u2014 Compounded",
  "Lambsquarters (Chenopodium album) (Signature Edition) \u2014 Compounded",
  "Wild Amaranth (Amaranthus) (Signature Edition) \u2014 Compounded",
  "Pine Needle Tea (Safe Pines Only) (Signature Edition) \u2014 Compounded",
  "Spruce Tips (Signature Edition) \u2014 Compounded",
  "Burdock (Arctium) (Signature Edition) \u2014 Compounded",
  "Chicory (Cichorium intybus) (Signature Edition) \u2014 Compounded",
  "Common Milkweed (Asclepias syriaca) (Signature Edition) \u2014 Compounded",
  "Ostrich Fern Fiddleheads (Signature Edition) \u2014 Compounded",
  "Sheep Sorrel (Rumex acetosella) (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Hickory and Black Walnut (Signature Edition) \u2014 Advanced",
  "The Foraging Calendar (Signature Edition) \u2014 Advanced",
  "Legal Foraging: Know the Rules (Signature Edition) \u2014 Advanced",
  "The Pollution Rule (Signature Edition) \u2014 Advanced",
  "Preserving the Harvest (Signature Edition) \u2014 Advanced",
  "Feeding Family Safely (Signature Edition) \u2014 Advanced",
  "Evening Primrose (Oenothera) (Signature Edition) \u2014 Advanced",
  "When NOT to Forage (Signature Edition) \u2014 Advanced",
  "Teaching Kids to Forage (Signature Edition) \u2014 Advanced",
  "Building a Forager's Library (Signature Edition) \u2014 Advanced",
  "The Forager's Year: A Capstone (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Wild Food Study — "+safe+"\n"
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
    name:topic+' — edible wild plant record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A edible wild plant record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"wild-food-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-edible-wild-plants-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('edible-wild-plants-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
