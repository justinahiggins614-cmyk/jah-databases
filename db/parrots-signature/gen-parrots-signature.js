(function(){'use strict';
/* JAH Signature Parrots Database generator — jahdb-parrots-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Scarlet Macaw (Ara macao)", "Signature Study: Blue-and-yellow Macaw (Ara ararauna)", "Signature Study: Hyacinth Macaw (Anodorhynchus hyacinthinus)", "Signature Study: Green-winged Macaw (Ara chloropterus)", "Signature Study: Military Macaw (Ara militaris)", "Signature Study: Great Green Macaw (Ara ambiguus)", "Signature Study: African Grey Parrot (Psittacus erithacus)", "Signature Study: Budgerigar (Melopsittacus undulatus)", "Signature Study: Cockatiel (Nymphicus hollandicus)", "Signature Study: Sulphur-crested Cockatoo (Cacatua galerita)", "Signature Study: Moluccan Cockatoo (Cacatua moluccensis)"], "Compounded": ["Signature Study: Umbrella Cockatoo (Cacatua alba)", "Signature Study: Galah (Eolophus roseicapilla)", "Signature Study: Major Mitchell's Cockatoo (Lophochroa leadbeateri)", "Signature Study: Rainbow Lorikeet (Trichoglossus moluccanus)", "Signature Study: Eclectus Parrot (Eclectus roratus)", "Signature Study: Monk Parakeet (Myiopsitta monachus)", "Signature Study: Ring-necked Parakeet (Psittacula krameri)", "Signature Study: Alexandrine Parakeet (Psittacula eupatria)", "Signature Study: Sun Conure (Aratinga solstitialis)", "Signature Study: Green-cheeked Conure (Pyrrhura molinae)", "Signature Study: Nanday Parakeet (Aratinga nenday)", "Signature Study: Yellow-headed Amazon (Amazona oratrix)"], "Advanced": ["Signature Study: Blue-fronted Amazon (Amazona aestiva)", "Signature Study: Orange-winged Amazon (Amazona amazonica)", "Signature Study: Kea (Nestor notabilis)", "Signature Study: Kakapo (Strigops habroptilus)", "Signature Study: Kaka (Nestor meridionalis)", "Signature Study: Crimson Rosella (Platycercus elegans)", "Signature Study: Eastern Rosella (Platycercus eximius)", "Signature Study: Fischer's Lovebird (Agapornis fischeri)", "Signature Study: Peach-faced Lovebird (Agapornis roseicollis)", "Signature Study: Senegal Parrot (Poicephalus senegalus)", "Signature Study: White-bellied Caique (Pionites leucogaster)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature parrot species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-parrots-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("parrots-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
