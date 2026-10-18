(function(){'use strict';
/* JAH The Roses Database generator — jahdb-roses-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RSE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Roses 101: The World's Favorite Flower \u2014 Foundations",
  "Rose Anatomy: Hips, Prickles, and Leaves \u2014 Foundations",
  "The Hybrid Tea \u2014 Foundations",
  "The Floribunda \u2014 Foundations",
  "The Grandiflora \u2014 Foundations",
  "Climbing Roses \u2014 Foundations",
  "Shrub Roses \u2014 Foundations",
  "Miniature Roses \u2014 Foundations",
  "Planting Roses \u2014 Foundations",
  "Watering and Feeding Roses \u2014 Foundations",
  "Pruning Roses \u2014 Foundations"
 ],
 "Compounded": [
  "The Damask Rose (Rosa damascena) \u2014 Compounded",
  "The Gallica Rose \u2014 Compounded",
  "The Centifolia (Cabbage Rose) \u2014 Compounded",
  "The Alba Rose \u2014 Compounded",
  "The Moss Rose \u2014 Compounded",
  "The China Rose (Rosa chinensis) \u2014 Compounded",
  "The Tea Rose \u2014 Compounded",
  "The Bourbon Rose \u2014 Compounded",
  "The Portland Rose \u2014 Compounded",
  "The Hybrid Perpetual \u2014 Compounded",
  "David Austin English Roses \u2014 Compounded",
  "Rose Hips: The Fruit \u2014 Compounded"
 ],
 "Advanced": [
  "Rose Fragrance Chemistry \u2014 Advanced",
  "Black Spot, Mildew, and Rust: Rose Diseases \u2014 Advanced",
  "Rose Pests: Aphids to Japanese Beetles \u2014 Advanced",
  "Grafting and Budding Roses \u2014 Advanced",
  "Hybridizing Roses \u2014 Advanced",
  "The Rose in History and Culture \u2014 Advanced",
  "Attar of Roses: The Oil \u2014 Advanced",
  "Preserving Roses: Drying and Pressing \u2014 Advanced",
  "Exhibiting Roses: The Show Bench \u2014 Advanced",
  "Old Garden Roses vs Modern Roses \u2014 Advanced",
  "The Rose Garden: Design \u2014 Advanced"
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
var gen={version:'jahdb-roses-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('roses',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
