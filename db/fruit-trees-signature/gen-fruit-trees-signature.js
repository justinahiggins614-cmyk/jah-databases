(function(){'use strict';
/* JAH The Fruit Trees Signature Database generator — jahdb-fruit-trees-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FRUTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Fruit Trees 101 (Signature Edition) \u2014 Foundations",
  "Chill Hours Explained (Signature Edition) \u2014 Foundations",
  "Rootstocks: The Hidden Half (Signature Edition) \u2014 Foundations",
  "Planting Fruit Trees (Signature Edition) \u2014 Foundations",
  "Pruning Fruit Trees (Signature Edition) \u2014 Foundations",
  "The Apple (Malus domestica) (Signature Edition) \u2014 Foundations",
  "The Pear (Pyrus communis) (Signature Edition) \u2014 Foundations",
  "The Peach (Prunus persica) (Signature Edition) \u2014 Foundations",
  "The Plum (Prunus domestica) (Signature Edition) \u2014 Foundations",
  "The Sweet Cherry (Prunus avium) (Signature Edition) \u2014 Foundations",
  "The Apricot (Prunus armeniaca) (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "The Orange (Citrus sinensis) (Signature Edition) \u2014 Compounded",
  "The Lemon (Citrus limon) (Signature Edition) \u2014 Compounded",
  "The Grapefruit (Citrus paradisi) (Signature Edition) \u2014 Compounded",
  "The Fig (Ficus carica) (Signature Edition) \u2014 Compounded",
  "The Pomegranate (Punica granatum) (Signature Edition) \u2014 Compounded",
  "The Persimmon (Diospyros kaki) (Signature Edition) \u2014 Compounded",
  "The Quince (Cydonia oblonga) (Signature Edition) \u2014 Compounded",
  "The Mulberry (Morus spp.) (Signature Edition) \u2014 Compounded",
  "The Pawpaw (Asimina triloba) (Signature Edition) \u2014 Compounded",
  "The Loquat (Eriobotrya japonica) (Signature Edition) \u2014 Compounded",
  "The Medlar (Mespilus germanica) (Signature Edition) \u2014 Compounded",
  "The Jujube (Ziziphus jujuba) (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Pollination Partners (Signature Edition) \u2014 Advanced",
  "Espalier: Flat Trees (Signature Edition) \u2014 Advanced",
  "Grafting Fruit Trees (Signature Edition) \u2014 Advanced",
  "Fruit Tree Pests (Signature Edition) \u2014 Advanced",
  "Fruit Tree Diseases (Signature Edition) \u2014 Advanced",
  "Thinning Fruit (Signature Edition) \u2014 Advanced",
  "Harvest Timing (Signature Edition) \u2014 Advanced",
  "Storing the Harvest (Signature Edition) \u2014 Advanced",
  "The Avocado (Persea americana) (Signature Edition) \u2014 Advanced",
  "The Mango (Mangifera indica) (Signature Edition) \u2014 Advanced",
  "The Banana: The Herb That Acts Like a Tree (Signature Edition) \u2014 Advanced"
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
var gen={version:'jahdb-fruit-trees-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fruit-trees-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
