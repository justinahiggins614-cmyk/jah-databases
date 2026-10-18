(function(){'use strict';
/* JAH The Turtles and Tortoises Database generator — jahdb-turtles-tortoises-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TURT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Green Sea Turtle (Chelonia mydas)", "Loggerhead Sea Turtle (Caretta caretta)", "Leatherback Sea Turtle (Dermochelys coriacea)", "Hawksbill Sea Turtle (Eretmochelys imbricata)", "Kemp's Ridley Sea Turtle (Lepidochelys kempii)", "Olive Ridley Sea Turtle (Lepidochelys olivacea)", "Galápagos Tortoise (Chelonoidis niger)", "Aldabra Giant Tortoise (Aldabrachelys gigantea)", "African Spurred Tortoise (Centrochelys sulcata)", "Radiated Tortoise (Astrochelys radiata)", "Indian Star Tortoise (Geochelone elegans)"], "Compounded": ["Hermann's Tortoise (Testudo hermanni)", "Greek Tortoise (Testudo graeca)", "Russian Tortoise (Testudo horsfieldii)", "Desert Tortoise (Gopherus agassizii)", "Gopher Tortoise (Gopherus polyphemus)", "Red-footed Tortoise (Chelonoidis carbonarius)", "Yellow-footed Tortoise (Chelonoidis denticulatus)", "Leopard Tortoise (Stigmochelys pardalis)", "Pancake Tortoise (Malacochersus tornieri)", "Painted Turtle (Chrysemys picta)", "Red-eared Slider (Trachemys scripta elegans)", "Eastern Box Turtle (Terrapene carolina)"], "Advanced": ["Ornate Box Turtle (Terrapene ornata)", "Wood Turtle (Glyptemys insculpta)", "Bog Turtle (Glyptemys muhlenbergii)", "Spotted Turtle (Clemmys guttata)", "Diamondback Terrapin (Malaclemys terrapin)", "Common Snapping Turtle (Chelydra serpentina)", "Alligator Snapping Turtle (Macrochelys temminckii)", "Mata Mata (Chelus fimbriatus)", "Pig-nosed Turtle (Carettochelys insculpta)", "Chinese Softshell Turtle (Pelodiscus sinensis)", "Spiny Softshell Turtle (Apalone spinifera)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A turtle and tortoise species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-turtles-tortoises-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("turtles-tortoises",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
