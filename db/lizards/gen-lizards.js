(function(){'use strict';
/* JAH The Lizards Database generator — jahdb-lizards-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LIZ-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Komodo Dragon (Varanus komodoensis)", "Gila Monster (Heloderma suspectum)", "Mexican Beaded Lizard (Heloderma horridum)", "Green Iguana (Iguana iguana)", "Marine Iguana (Amblyrhynchus cristatus)", "Blue Iguana (Cyclura lewisi)", "Rhinoceros Iguana (Cyclura cornuta)", "Common Chuckwalla (Sauromalus ater)", "Veiled Chameleon (Chamaeleo calyptratus)", "Panther Chameleon (Furcifer pardalis)", "Jackson's Chameleon (Trioceros jacksonii)"], "Compounded": ["Tokay Gecko (Gekko gecko)", "Leopard Gecko (Eublepharis macularius)", "Crested Gecko (Correlophus ciliatus)", "Madagascar Giant Day Gecko (Phelsuma madagascariensis)", "Gargoyle Gecko (Rhacodactylus auriculatus)", "Bearded Dragon (Pogona vitticeps)", "Frilled Lizard (Chlamydosaurus kingii)", "Thorny Devil (Moloch horridus)", "Eastern Collared Lizard (Crotaphytus collaris)", "Plumed Basilisk (Basiliscus basiliscus)", "Green Basilisk (Basiliscus plumifrons)", "Asian Water Monitor (Varanus salvator)"], "Advanced": ["Nile Monitor (Varanus niloticus)", "Savannah Monitor (Varanus exanthematicus)", "Argus Monitor (Varanus panoptes)", "Perentie (Varanus giganteus)", "Eastern Blue-tongued Skink (Tiliqua scincoides)", "Shingleback (Tiliqua rugosa)", "Solomon Islands Skink (Corucia zebrata)", "Sandfish (Scincus scincus)", "European Glass Lizard (Pseudopus apodus)", "Slow Worm (Anguis fragilis)", "Texas Horned Lizard (Phrynosoma cornutum)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Species demo\n# Topic: \""+safe+"\" | Field: "+field+"\n"
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A lizard species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-lizards-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("lizards",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
