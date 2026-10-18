(function(){'use strict';
/* JAH The Trees of the World Database generator — jahdb-trees-of-the-world-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TWO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Tree? \u2014 Foundations",
  "Roots: The Hidden Half \u2014 Foundations",
  "Trunk and Bark \u2014 Foundations",
  "Branches and the Crown \u2014 Foundations",
  "Leaves: The Solar Panels \u2014 Foundations",
  "How a Tree Grows: Rings and Wood \u2014 Foundations",
  "The Oak (Quercus robur) \u2014 Foundations",
  "The Sugar Maple (Acer saccharum) \u2014 Foundations",
  "The Silver Birch (Betula pendula) \u2014 Foundations",
  "The Weeping Willow (Salix babylonica) \u2014 Foundations",
  "The Date Palm (Phoenix dactylifera) \u2014 Foundations"
 ],
 "Compounded": [
  "The Baobab (Adansonia digitata) \u2014 Compounded",
  "The Coast Redwood (Sequoia sempervirens) \u2014 Compounded",
  "The Giant Sequoia (Sequoiadendron giganteum) \u2014 Compounded",
  "The Bristlecone Pine (Pinus longaeva) \u2014 Compounded",
  "The Banyan (Ficus benghalensis) \u2014 Compounded",
  "The Rainbow Eucalyptus (Eucalyptus deglupta) \u2014 Compounded",
  "The Olive Tree (Olea europaea) \u2014 Compounded",
  "The Cherry Blossom (Prunus serrulata) \u2014 Compounded",
  "The Ginkgo (Ginkgo biloba) \u2014 Compounded",
  "The Monkey Puzzle (Araucaria araucana) \u2014 Compounded",
  "The Quaking Aspen (Populus tremuloides) \u2014 Compounded",
  "The Mangrove (Rhizophora mangle) \u2014 Compounded"
 ],
 "Advanced": [
  "Tree Rings: A Tree's Autobiography \u2014 Advanced",
  "The Wood Wide Web: Mycorrhizal Networks \u2014 Advanced",
  "Forest Succession Stages \u2014 Advanced",
  "Urban Forestry \u2014 Advanced",
  "Heritage Tree Preservation \u2014 Advanced",
  "Trees and the Carbon Cycle \u2014 Advanced",
  "Sacred Groves of the World \u2014 Advanced",
  "Agroforestry Systems \u2014 Advanced",
  "The Kauri (Agathis australis) \u2014 Advanced",
  "Tree Conservation and the IUCN Red List \u2014 Advanced",
  "The Future Forest: Assisted Migration \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tree Study — "+safe+"\n"
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
    name:topic+' — tree record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tree record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"tree-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-trees-of-the-world-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('trees-of-the-world',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
