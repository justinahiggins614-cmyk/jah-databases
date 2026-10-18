(function(){'use strict';
/* JAH The Succulents and Cacti Database generator — jahdb-succulents-cacti-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SUC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Succulents 101: Water-Storing Plants \u2014 Foundations",
  "Cacti vs Succulents \u2014 Foundations",
  "CAM Photosynthesis \u2014 Foundations",
  "Gritty Mix and Drainage \u2014 Foundations",
  "Light for Succulents \u2014 Foundations",
  "Watering Succulents \u2014 Foundations",
  "The Echeveria \u2014 Foundations",
  "The Sedum (Stonecrop) \u2014 Foundations",
  "The Haworthia \u2014 Foundations",
  "The Lithops (Living Stones) \u2014 Foundations",
  "The Barrel Cactus \u2014 Foundations"
 ],
 "Compounded": [
  "The Saguaro (Carnegiea gigantea) \u2014 Compounded",
  "The Cholla (Cylindropuntia) \u2014 Compounded",
  "The Cardon (Pachycereus pringlei) \u2014 Compounded",
  "The Prickly Pear (Opuntia ficus-indica) \u2014 Compounded",
  "The Agave (Agave americana) \u2014 Compounded",
  "The Ghost Plant (Graptopetalum paraguayense) \u2014 Compounded",
  "The String of Pearls (Senecio rowleyanus) \u2014 Compounded",
  "The Christmas Cactus (Schlumbergera) \u2014 Compounded",
  "The Crown of Thorns (Euphorbia milii) \u2014 Compounded",
  "The Panda Plant (Kalanchoe tomentosa) \u2014 Compounded",
  "The Gasteria \u2014 Compounded",
  "The Desert Rose (Adenium obesum) \u2014 Compounded"
 ],
 "Advanced": [
  "Propagating Succulents \u2014 Advanced",
  "Grafting Cacti \u2014 Advanced",
  "The Peyote (Lophophora williamsii) \u2014 Advanced",
  "Etiolation: Stretching for Light \u2014 Advanced",
  "Sunburn and Frost Damage \u2014 Advanced",
  "Succulent Pests: Mealybugs and Scale \u2014 Advanced",
  "The Living Rock (Ariocarpus) \u2014 Advanced",
  "Crested and Monstrose Forms \u2014 Advanced",
  "Succulent Arrangements and Dish Gardens \u2014 Advanced",
  "Hardy Succulents: Hens and Chicks \u2014 Advanced",
  "The Succulent Collection: Long-Term Care \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Succulent Study — "+safe+"\n"
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
    name:topic+' — succulent record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A succulent record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"succulent-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-succulents-cacti-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('succulents-cacti',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
