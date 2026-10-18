(function(){'use strict';
/* JAH The Culinary Herbs Signature Database generator — jahdb-culinary-herbs-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HRBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Culinary Herbs 101 (Signature Edition) \u2014 Foundations",
  "Basil (Ocimum basilicum) (Signature Edition) \u2014 Foundations",
  "Parsley (Petroselinum crispum) (Signature Edition) \u2014 Foundations",
  "Cilantro and Coriander (Coriandrum sativum) (Signature Edition) \u2014 Foundations",
  "Mint (Mentha) (Signature Edition) \u2014 Foundations",
  "Rosemary (Salvia rosmarinus) (Signature Edition) \u2014 Foundations",
  "Thyme (Thymus vulgaris) (Signature Edition) \u2014 Foundations",
  "Oregano (Origanum vulgare) (Signature Edition) \u2014 Foundations",
  "Dill (Anethum graveolens) (Signature Edition) \u2014 Foundations",
  "Chives (Allium schoenoprasum) (Signature Edition) \u2014 Foundations",
  "Bay Laurel (Laurus nobilis) (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Sage (Salvia officinalis) (Signature Edition) \u2014 Compounded",
  "Tarragon (Artemisia dracunculus) (Signature Edition) \u2014 Compounded",
  "Marjoram (Origanum majorana) (Signature Edition) \u2014 Compounded",
  "Lemongrass (Cymbopogon citratus) (Signature Edition) \u2014 Compounded",
  "Kaffir Lime Leaf (Citrus hystrix) (Signature Edition) \u2014 Compounded",
  "Curry Leaf (Murraya koenigii) (Signature Edition) \u2014 Compounded",
  "Shiso and Perilla (Perilla frutescens) (Signature Edition) \u2014 Compounded",
  "Epazote (Dysphania ambrosioides) (Signature Edition) \u2014 Compounded",
  "Herbes de Provence (Signature Edition) \u2014 Compounded",
  "Bouquet Garni (Signature Edition) \u2014 Compounded",
  "Drying Herbs (Signature Edition) \u2014 Compounded",
  "Freezing Herbs (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Growing Herbs Indoors (Signature Edition) \u2014 Advanced",
  "Herb Garden Design (Signature Edition) \u2014 Advanced",
  "Pesto Science (Signature Edition) \u2014 Advanced",
  "Chimichurri (Signature Edition) \u2014 Advanced",
  "Herb Butters and Oils (Signature Edition) \u2014 Advanced",
  "Infused Vinegars (Signature Edition) \u2014 Advanced",
  "Herbal Teas from the Garden (Signature Edition) \u2014 Advanced",
  "Cooking with Edible Flowers (Signature Edition) \u2014 Advanced",
  "Herb Pairing Guide (Signature Edition) \u2014 Advanced",
  "Herb Salts (Signature Edition) \u2014 Advanced",
  "The Herb Master's Pantry (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Culinary Herb Study — "+safe+"\n"
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
    name:topic+' — culinary herb record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A culinary herb record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"culinary-herb-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-culinary-herbs-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('culinary-herbs-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
