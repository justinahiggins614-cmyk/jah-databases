(function(){'use strict';
/* JAH The Roses Signature Database generator — jahdb-roses-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RSES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Roses 101: The World's Favorite Flower (Signature Edition) \u2014 Foundations",
  "Rose Anatomy: Hips, Prickles, and Leaves (Signature Edition) \u2014 Foundations",
  "The Hybrid Tea (Signature Edition) \u2014 Foundations",
  "The Floribunda (Signature Edition) \u2014 Foundations",
  "The Grandiflora (Signature Edition) \u2014 Foundations",
  "Climbing Roses (Signature Edition) \u2014 Foundations",
  "Shrub Roses (Signature Edition) \u2014 Foundations",
  "Miniature Roses (Signature Edition) \u2014 Foundations",
  "Planting Roses (Signature Edition) \u2014 Foundations",
  "Watering and Feeding Roses (Signature Edition) \u2014 Foundations",
  "Pruning Roses (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "The Damask Rose (Rosa damascena) (Signature Edition) \u2014 Compounded",
  "The Gallica Rose (Signature Edition) \u2014 Compounded",
  "The Centifolia (Cabbage Rose) (Signature Edition) \u2014 Compounded",
  "The Alba Rose (Signature Edition) \u2014 Compounded",
  "The Moss Rose (Signature Edition) \u2014 Compounded",
  "The China Rose (Rosa chinensis) (Signature Edition) \u2014 Compounded",
  "The Tea Rose (Signature Edition) \u2014 Compounded",
  "The Bourbon Rose (Signature Edition) \u2014 Compounded",
  "The Portland Rose (Signature Edition) \u2014 Compounded",
  "The Hybrid Perpetual (Signature Edition) \u2014 Compounded",
  "David Austin English Roses (Signature Edition) \u2014 Compounded",
  "Rose Hips: The Fruit (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Rose Fragrance Chemistry (Signature Edition) \u2014 Advanced",
  "Black Spot, Mildew, and Rust: Rose Diseases (Signature Edition) \u2014 Advanced",
  "Rose Pests: Aphids to Japanese Beetles (Signature Edition) \u2014 Advanced",
  "Grafting and Budding Roses (Signature Edition) \u2014 Advanced",
  "Hybridizing Roses (Signature Edition) \u2014 Advanced",
  "The Rose in History and Culture (Signature Edition) \u2014 Advanced",
  "Attar of Roses: The Oil (Signature Edition) \u2014 Advanced",
  "Preserving Roses: Drying and Pressing (Signature Edition) \u2014 Advanced",
  "Exhibiting Roses: The Show Bench (Signature Edition) \u2014 Advanced",
  "Old Garden Roses vs Modern Roses (Signature Edition) \u2014 Advanced",
  "The Rose Garden: Design (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Rose Study — "+safe+"\n"
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
    name:topic+' — rose record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A rose record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"rose-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-roses-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('roses-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
