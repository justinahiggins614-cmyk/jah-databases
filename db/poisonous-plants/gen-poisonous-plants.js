(function(){'use strict';
/* JAH The Poisonous Plants Database generator — jahdb-poisonous-plants-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PXP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Poisonous Plants 101 \u2014 Foundations",
  "How Plant Toxins Work \u2014 Foundations",
  "Deadly Nightshade (Atropa belladonna) \u2014 Foundations",
  "Poison Hemlock (Conium maculatum) \u2014 Foundations",
  "Oleander (Nerium oleander) \u2014 Foundations",
  "Foxglove: The Toxicology View \u2014 Foundations",
  "Castor Bean (Ricinus communis) \u2014 Foundations",
  "White Snakeroot (Ageratina altissima) \u2014 Foundations",
  "Poison Ivy and Oak (Toxicodendron) \u2014 Foundations",
  "The Manchineel (Hippomane mancinella) \u2014 Foundations",
  "Water Hemlock (Cicuta maculata) \u2014 Foundations"
 ],
 "Compounded": [
  "Monkshood (Aconitum napellus) \u2014 Compounded",
  "Yew (Taxus baccata) \u2014 Compounded",
  "Lily of the Valley (Convallaria majalis) \u2014 Compounded",
  "Jimsonweed (Datura stramonium) \u2014 Compounded",
  "Pokeweed (Phytolacca americana) \u2014 Compounded",
  "Rosary Pea (Abrus precatorius) \u2014 Compounded",
  "The Suicide Tree (Cerbera odollam) \u2014 Compounded",
  "Rhododendron (Grayanotoxins and Mad Honey) \u2014 Compounded",
  "Giant Hogweed (Heracleum mantegazzianum) \u2014 Compounded",
  "Tobacco (Nicotiana tabacum) \u2014 Compounded",
  "Moonseed (Menispermum canadense) \u2014 Compounded",
  "Daffodil (Narcissus) \u2014 Compounded"
 ],
 "Advanced": [
  "Dose Makes the Poison \u2014 Advanced",
  "Poisonous Garden Bulbs \u2014 Advanced",
  "Livestock Poisoning Plants \u2014 Advanced",
  "Historical Poisonings \u2014 Advanced",
  "Antidotes and Emergency Response \u2014 Advanced",
  "When to Call Poison Control \u2014 Advanced",
  "Foraging Dangers \u2014 Advanced",
  "Lookalikes That Kill: The Rogues' Gallery \u2014 Advanced",
  "The Poison Garden (Alnwick) \u2014 Advanced",
  "Poisoning Signs in Pets \u2014 Advanced",
  "Living Safely with Toxic Plants \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Poisonous Plant Study — "+safe+"\n"
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
    name:topic+' — poisonous plant record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A poisonous plant record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"poisonous-plant-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-poisonous-plants-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('poisonous-plants',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
