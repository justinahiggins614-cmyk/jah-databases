(function(){'use strict';
/* JAH The Poisonous Plants Signature Database generator — jahdb-poisonous-plants-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PXPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Poisonous Plants 101 (Signature Edition) \u2014 Foundations",
  "How Plant Toxins Work (Signature Edition) \u2014 Foundations",
  "Deadly Nightshade (Atropa belladonna) (Signature Edition) \u2014 Foundations",
  "Poison Hemlock (Conium maculatum) (Signature Edition) \u2014 Foundations",
  "Oleander (Nerium oleander) (Signature Edition) \u2014 Foundations",
  "Foxglove: The Toxicology View (Signature Edition) \u2014 Foundations",
  "Castor Bean (Ricinus communis) (Signature Edition) \u2014 Foundations",
  "White Snakeroot (Ageratina altissima) (Signature Edition) \u2014 Foundations",
  "Poison Ivy and Oak (Toxicodendron) (Signature Edition) \u2014 Foundations",
  "The Manchineel (Hippomane mancinella) (Signature Edition) \u2014 Foundations",
  "Water Hemlock (Cicuta maculata) (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Monkshood (Aconitum napellus) (Signature Edition) \u2014 Compounded",
  "Yew (Taxus baccata) (Signature Edition) \u2014 Compounded",
  "Lily of the Valley (Convallaria majalis) (Signature Edition) \u2014 Compounded",
  "Jimsonweed (Datura stramonium) (Signature Edition) \u2014 Compounded",
  "Pokeweed (Phytolacca americana) (Signature Edition) \u2014 Compounded",
  "Rosary Pea (Abrus precatorius) (Signature Edition) \u2014 Compounded",
  "The Suicide Tree (Cerbera odollam) (Signature Edition) \u2014 Compounded",
  "Rhododendron (Grayanotoxins and Mad Honey) (Signature Edition) \u2014 Compounded",
  "Giant Hogweed (Heracleum mantegazzianum) (Signature Edition) \u2014 Compounded",
  "Tobacco (Nicotiana tabacum) (Signature Edition) \u2014 Compounded",
  "Moonseed (Menispermum canadense) (Signature Edition) \u2014 Compounded",
  "Daffodil (Narcissus) (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Dose Makes the Poison (Signature Edition) \u2014 Advanced",
  "Poisonous Garden Bulbs (Signature Edition) \u2014 Advanced",
  "Livestock Poisoning Plants (Signature Edition) \u2014 Advanced",
  "Historical Poisonings (Signature Edition) \u2014 Advanced",
  "Antidotes and Emergency Response (Signature Edition) \u2014 Advanced",
  "When to Call Poison Control (Signature Edition) \u2014 Advanced",
  "Foraging Dangers (Signature Edition) \u2014 Advanced",
  "Lookalikes That Kill: The Rogues' Gallery (Signature Edition) \u2014 Advanced",
  "The Poison Garden (Alnwick) (Signature Edition) \u2014 Advanced",
  "Poisoning Signs in Pets (Signature Edition) \u2014 Advanced",
  "Living Safely with Toxic Plants (Signature Edition) \u2014 Advanced"
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
var gen={version:'jahdb-poisonous-plants-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('poisonous-plants-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
