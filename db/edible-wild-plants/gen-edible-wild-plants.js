(function(){'use strict';
/* JAH The Edible Wild Plants Database generator — jahdb-edible-wild-plants-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EWP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Foraging Safety 101 \u2014 Foundations",
  "The Universal Edibility Test: Truth and Limits \u2014 Foundations",
  "Dandelion (Taraxacum officinale) \u2014 Foundations",
  "Chickweed (Stellaria media) \u2014 Foundations",
  "Purslane (Portulaca oleracea) \u2014 Foundations",
  "Plantain (Plantago major) \u2014 Foundations",
  "Wood Sorrel (Oxalis) \u2014 Foundations",
  "Wild Garlic and Ramps (Allium) \u2014 Foundations",
  "Stinging Nettle (Urtica dioica) \u2014 Foundations",
  "Cattail (Typha) \u2014 Foundations",
  "Acorns: The Forgotten Staple \u2014 Foundations"
 ],
 "Compounded": [
  "Blackberry and Raspberry (Rubus) \u2014 Compounded",
  "Elderberry (Sambucus): Cooked Only \u2014 Compounded",
  "Wild Strawberry (Fragaria) \u2014 Compounded",
  "Lambsquarters (Chenopodium album) \u2014 Compounded",
  "Wild Amaranth (Amaranthus) \u2014 Compounded",
  "Pine Needle Tea (Safe Pines Only) \u2014 Compounded",
  "Spruce Tips \u2014 Compounded",
  "Burdock (Arctium) \u2014 Compounded",
  "Chicory (Cichorium intybus) \u2014 Compounded",
  "Common Milkweed (Asclepias syriaca) \u2014 Compounded",
  "Ostrich Fern Fiddleheads \u2014 Compounded",
  "Sheep Sorrel (Rumex acetosella) \u2014 Compounded"
 ],
 "Advanced": [
  "Hickory and Black Walnut \u2014 Advanced",
  "The Foraging Calendar \u2014 Advanced",
  "Legal Foraging: Know the Rules \u2014 Advanced",
  "The Pollution Rule \u2014 Advanced",
  "Preserving the Harvest \u2014 Advanced",
  "Feeding Family Safely \u2014 Advanced",
  "Evening Primrose (Oenothera) \u2014 Advanced",
  "When NOT to Forage \u2014 Advanced",
  "Teaching Kids to Forage \u2014 Advanced",
  "Building a Forager's Library \u2014 Advanced",
  "The Forager's Year: A Capstone \u2014 Advanced"
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
var gen={version:'jahdb-edible-wild-plants-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('edible-wild-plants',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
