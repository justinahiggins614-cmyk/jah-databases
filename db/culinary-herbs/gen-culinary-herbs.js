(function(){'use strict';
/* JAH The Culinary Herbs Database generator — jahdb-culinary-herbs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HRB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Culinary Herbs 101 \u2014 Foundations",
  "Basil (Ocimum basilicum) \u2014 Foundations",
  "Parsley (Petroselinum crispum) \u2014 Foundations",
  "Cilantro and Coriander (Coriandrum sativum) \u2014 Foundations",
  "Mint (Mentha) \u2014 Foundations",
  "Rosemary (Salvia rosmarinus) \u2014 Foundations",
  "Thyme (Thymus vulgaris) \u2014 Foundations",
  "Oregano (Origanum vulgare) \u2014 Foundations",
  "Dill (Anethum graveolens) \u2014 Foundations",
  "Chives (Allium schoenoprasum) \u2014 Foundations",
  "Bay Laurel (Laurus nobilis) \u2014 Foundations"
 ],
 "Compounded": [
  "Sage (Salvia officinalis) \u2014 Compounded",
  "Tarragon (Artemisia dracunculus) \u2014 Compounded",
  "Marjoram (Origanum majorana) \u2014 Compounded",
  "Lemongrass (Cymbopogon citratus) \u2014 Compounded",
  "Kaffir Lime Leaf (Citrus hystrix) \u2014 Compounded",
  "Curry Leaf (Murraya koenigii) \u2014 Compounded",
  "Shiso and Perilla (Perilla frutescens) \u2014 Compounded",
  "Epazote (Dysphania ambrosioides) \u2014 Compounded",
  "Herbes de Provence \u2014 Compounded",
  "Bouquet Garni \u2014 Compounded",
  "Drying Herbs \u2014 Compounded",
  "Freezing Herbs \u2014 Compounded"
 ],
 "Advanced": [
  "Growing Herbs Indoors \u2014 Advanced",
  "Herb Garden Design \u2014 Advanced",
  "Pesto Science \u2014 Advanced",
  "Chimichurri \u2014 Advanced",
  "Herb Butters and Oils \u2014 Advanced",
  "Infused Vinegars \u2014 Advanced",
  "Herbal Teas from the Garden \u2014 Advanced",
  "Cooking with Edible Flowers \u2014 Advanced",
  "Herb Pairing Guide \u2014 Advanced",
  "Herb Salts \u2014 Advanced",
  "The Herb Master's Pantry \u2014 Advanced"
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
var gen={version:'jahdb-culinary-herbs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('culinary-herbs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
