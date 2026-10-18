(function(){'use strict';
/* JAH The Fruit Trees Database generator — jahdb-fruit-trees-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FRUT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Fruit Trees 101 \u2014 Foundations",
  "Chill Hours Explained \u2014 Foundations",
  "Rootstocks: The Hidden Half \u2014 Foundations",
  "Planting Fruit Trees \u2014 Foundations",
  "Pruning Fruit Trees \u2014 Foundations",
  "The Apple (Malus domestica) \u2014 Foundations",
  "The Pear (Pyrus communis) \u2014 Foundations",
  "The Peach (Prunus persica) \u2014 Foundations",
  "The Plum (Prunus domestica) \u2014 Foundations",
  "The Sweet Cherry (Prunus avium) \u2014 Foundations",
  "The Apricot (Prunus armeniaca) \u2014 Foundations"
 ],
 "Compounded": [
  "The Orange (Citrus sinensis) \u2014 Compounded",
  "The Lemon (Citrus limon) \u2014 Compounded",
  "The Grapefruit (Citrus paradisi) \u2014 Compounded",
  "The Fig (Ficus carica) \u2014 Compounded",
  "The Pomegranate (Punica granatum) \u2014 Compounded",
  "The Persimmon (Diospyros kaki) \u2014 Compounded",
  "The Quince (Cydonia oblonga) \u2014 Compounded",
  "The Mulberry (Morus spp.) \u2014 Compounded",
  "The Pawpaw (Asimina triloba) \u2014 Compounded",
  "The Loquat (Eriobotrya japonica) \u2014 Compounded",
  "The Medlar (Mespilus germanica) \u2014 Compounded",
  "The Jujube (Ziziphus jujuba) \u2014 Compounded"
 ],
 "Advanced": [
  "Pollination Partners \u2014 Advanced",
  "Espalier: Flat Trees \u2014 Advanced",
  "Grafting Fruit Trees \u2014 Advanced",
  "Fruit Tree Pests \u2014 Advanced",
  "Fruit Tree Diseases \u2014 Advanced",
  "Thinning Fruit \u2014 Advanced",
  "Harvest Timing \u2014 Advanced",
  "Storing the Harvest \u2014 Advanced",
  "The Avocado (Persea americana) \u2014 Advanced",
  "The Mango (Mangifera indica) \u2014 Advanced",
  "The Banana: The Herb That Acts Like a Tree \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fruit Tree Study — "+safe+"\n"
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
    name:topic+' — fruit tree record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fruit tree record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"fruit-tree-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-fruit-trees-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fruit-trees',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
