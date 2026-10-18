(function(){'use strict';
/* JAH Signature Turtles and Tortoises Database generator — jahdb-turtles-tortoises-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TURTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Green Sea Turtle (Chelonia mydas)", "Signature Study: Loggerhead Sea Turtle (Caretta caretta)", "Signature Study: Leatherback Sea Turtle (Dermochelys coriacea)", "Signature Study: Hawksbill Sea Turtle (Eretmochelys imbricata)", "Signature Study: Kemp's Ridley Sea Turtle (Lepidochelys kempii)", "Signature Study: Olive Ridley Sea Turtle (Lepidochelys olivacea)", "Signature Study: Galápagos Tortoise (Chelonoidis niger)", "Signature Study: Aldabra Giant Tortoise (Aldabrachelys gigantea)", "Signature Study: African Spurred Tortoise (Centrochelys sulcata)", "Signature Study: Radiated Tortoise (Astrochelys radiata)", "Signature Study: Indian Star Tortoise (Geochelone elegans)"], "Compounded": ["Signature Study: Hermann's Tortoise (Testudo hermanni)", "Signature Study: Greek Tortoise (Testudo graeca)", "Signature Study: Russian Tortoise (Testudo horsfieldii)", "Signature Study: Desert Tortoise (Gopherus agassizii)", "Signature Study: Gopher Tortoise (Gopherus polyphemus)", "Signature Study: Red-footed Tortoise (Chelonoidis carbonarius)", "Signature Study: Yellow-footed Tortoise (Chelonoidis denticulatus)", "Signature Study: Leopard Tortoise (Stigmochelys pardalis)", "Signature Study: Pancake Tortoise (Malacochersus tornieri)", "Signature Study: Painted Turtle (Chrysemys picta)", "Signature Study: Red-eared Slider (Trachemys scripta elegans)", "Signature Study: Eastern Box Turtle (Terrapene carolina)"], "Advanced": ["Signature Study: Ornate Box Turtle (Terrapene ornata)", "Signature Study: Wood Turtle (Glyptemys insculpta)", "Signature Study: Bog Turtle (Glyptemys muhlenbergii)", "Signature Study: Spotted Turtle (Clemmys guttata)", "Signature Study: Diamondback Terrapin (Malaclemys terrapin)", "Signature Study: Common Snapping Turtle (Chelydra serpentina)", "Signature Study: Alligator Snapping Turtle (Macrochelys temminckii)", "Signature Study: Mata Mata (Chelus fimbriatus)", "Signature Study: Pig-nosed Turtle (Carettochelys insculpta)", "Signature Study: Chinese Softshell Turtle (Pelodiscus sinensis)", "Signature Study: Spiny Softshell Turtle (Apalone spinifera)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature turtle and tortoise species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-turtles-tortoises-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("turtles-tortoises-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
