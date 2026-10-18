(function(){'use strict';
/* JAH Signature Lizards Database generator — jahdb-lizards-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LIZS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Komodo Dragon (Varanus komodoensis)", "Signature Study: Gila Monster (Heloderma suspectum)", "Signature Study: Mexican Beaded Lizard (Heloderma horridum)", "Signature Study: Green Iguana (Iguana iguana)", "Signature Study: Marine Iguana (Amblyrhynchus cristatus)", "Signature Study: Blue Iguana (Cyclura lewisi)", "Signature Study: Rhinoceros Iguana (Cyclura cornuta)", "Signature Study: Common Chuckwalla (Sauromalus ater)", "Signature Study: Veiled Chameleon (Chamaeleo calyptratus)", "Signature Study: Panther Chameleon (Furcifer pardalis)", "Signature Study: Jackson's Chameleon (Trioceros jacksonii)"], "Compounded": ["Signature Study: Tokay Gecko (Gekko gecko)", "Signature Study: Leopard Gecko (Eublepharis macularius)", "Signature Study: Crested Gecko (Correlophus ciliatus)", "Signature Study: Madagascar Giant Day Gecko (Phelsuma madagascariensis)", "Signature Study: Gargoyle Gecko (Rhacodactylus auriculatus)", "Signature Study: Bearded Dragon (Pogona vitticeps)", "Signature Study: Frilled Lizard (Chlamydosaurus kingii)", "Signature Study: Thorny Devil (Moloch horridus)", "Signature Study: Eastern Collared Lizard (Crotaphytus collaris)", "Signature Study: Plumed Basilisk (Basiliscus basiliscus)", "Signature Study: Green Basilisk (Basiliscus plumifrons)", "Signature Study: Asian Water Monitor (Varanus salvator)"], "Advanced": ["Signature Study: Nile Monitor (Varanus niloticus)", "Signature Study: Savannah Monitor (Varanus exanthematicus)", "Signature Study: Argus Monitor (Varanus panoptes)", "Signature Study: Perentie (Varanus giganteus)", "Signature Study: Eastern Blue-tongued Skink (Tiliqua scincoides)", "Signature Study: Shingleback (Tiliqua rugosa)", "Signature Study: Solomon Islands Skink (Corucia zebrata)", "Signature Study: Sandfish (Scincus scincus)", "Signature Study: European Glass Lizard (Pseudopus apodus)", "Signature Study: Slow Worm (Anguis fragilis)", "Signature Study: Texas Horned Lizard (Phrynosoma cornutum)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature species demo\n# Topic: \""+safe+"\" | Field: "+field+"\n"
   + "record = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('Sample record — structural sample, not an archive entry.')\n"
   + "print(record['topic'] + ' [' + record['field'] + ']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic,
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature lizard species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-generated",
    sample:true,
    disclaimer:"Generated Signature sample record \u2014 not an archive record. Seeded Signature records are the authoritative entries.",
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-lizards-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("lizards-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
