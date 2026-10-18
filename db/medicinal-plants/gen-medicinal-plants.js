(function(){'use strict';
/* JAH The Medicinal Plants Database generator — jahdb-medicinal-plants-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MPL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Medicinal Plants 101 \u2014 Foundations",
  "How Plant Medicines Work \u2014 Foundations",
  "The Evidence Ladder \u2014 Foundations",
  "Safety First: Reading the Risks \u2014 Foundations",
  "Echinacea (Echinacea purpurea) \u2014 Foundations",
  "Ginger (Zingiber officinale) \u2014 Foundations",
  "Garlic (Allium sativum) \u2014 Foundations",
  "Turmeric (Curcuma longa) \u2014 Foundations",
  "Chamomile (Matricaria chamomilla) \u2014 Foundations",
  "Peppermint (Mentha piperita) \u2014 Foundations",
  "Valerian (Valeriana officinalis) \u2014 Foundations"
 ],
 "Compounded": [
  "St. John's Wort (Hypericum perforatum) \u2014 Compounded",
  "Milk Thistle (Silybum marianum) \u2014 Compounded",
  "Saw Palmetto (Serenoa repens) \u2014 Compounded",
  "Black Cohosh (Actaea racemosa) \u2014 Compounded",
  "Ginseng (Panax ginseng) \u2014 Compounded",
  "Ashwagandha (Withania somnifera) \u2014 Compounded",
  "Calendula (Calendula officinalis) \u2014 Compounded",
  "Elderberry (Sambucus nigra) \u2014 Compounded",
  "Cranberry (Vaccinium macrocarpon) \u2014 Compounded",
  "Green Tea (Camellia sinensis) \u2014 Compounded",
  "Willow Bark (Salix alba) \u2014 Compounded",
  "Foxglove (Digitalis purpurea) \u2014 Compounded"
 ],
 "Advanced": [
  "The Opium Poppy (Papaver somniferum) \u2014 Advanced",
  "Cinchona: The Fever Tree \u2014 Advanced",
  "Sweet Annie (Artemisia annua) \u2014 Advanced",
  "The Pacific Yew (Taxus brevifolia) \u2014 Advanced",
  "Madagascar Periwinkle (Catharanthus roseus) \u2014 Advanced",
  "Drug Interactions: The Hidden Danger \u2014 Advanced",
  "Standardization and Quality \u2014 Advanced",
  "Traditional Chinese Medicine: Key Herbs \u2014 Advanced",
  "Ayurveda: Key Herbs \u2014 Advanced",
  "Growing Medicinal Herbs \u2014 Advanced",
  "The Future: Plant-Derived Drugs \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Medicinal Plant Study — "+safe+"\n"
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
    name:topic+' — medicinal plant record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A medicinal plant record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"medicinal-plant-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-medicinal-plants-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('medicinal-plants',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
