(function(){'use strict';
/* JAH Signature Saltwater Fish Database generator — jahdb-saltwater-fish-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SWFS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Atlantic Bluefin Tuna (Thunnus thynnus)", "Signature Study: Yellowfin Tuna (Thunnus albacares)", "Signature Study: Skipjack Tuna (Katsuwonus pelamis)", "Signature Study: Atlantic Cod (Gadus morhua)", "Signature Study: Pacific Halibut (Hippoglossus stenolepis)", "Signature Study: Atlantic Halibut (Hippoglossus hippoglossus)", "Signature Study: Swordfish (Xiphias gladius)", "Signature Study: Blue Marlin (Makaira nigricans)", "Signature Study: Indo-Pacific Sailfish (Istiophorus platypterus)", "Signature Study: Mahi-mahi (Coryphaena hippurus)", "Signature Study: Wahoo (Acanthocybium solandri)"], "Compounded": ["Signature Study: Great Barracuda (Sphyraena barracuda)", "Signature Study: Goliath Grouper (Epinephelus itajara)", "Signature Study: Nassau Grouper (Epinephelus striatus)", "Signature Study: Northern Red Snapper (Lutjanus campechanus)", "Signature Study: Tarpon (Megalops atlanticus)", "Signature Study: Bonefish (Albula vulpes)", "Signature Study: Permit (Trachinotus falcatus)", "Signature Study: Common Snook (Centropomus undecimalis)", "Signature Study: Striped Bass (Morone saxatilis)", "Signature Study: Red Drum (Sciaenops ocellatus)", "Signature Study: California Yellowtail (Seriola lalandi)", "Signature Study: Greater Amberjack (Seriola dumerili)"], "Advanced": ["Signature Study: Cobia (Rachycentron canadum)", "Signature Study: Ocean Sunfish (Mola mola)", "Signature Study: Lined Seahorse (Hippocampus erectus)", "Signature Study: Ocellaris Clownfish (Amphiprion ocellaris)", "Signature Study: Palette Surgeonfish (Paracanthurus hepatus)", "Signature Study: Yellow Tang (Zebrasoma flavescens)", "Signature Study: Stoplight Parrotfish (Sparisoma viride)", "Signature Study: Green Moray (Gymnothorax funebris)", "Signature Study: Red Lionfish (Pterois volitans)", "Signature Study: Reef Stonefish (Synanceia verrucosa)", "Signature Study: Atlantic Flying Fish (Exocoetus volitans)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature saltwater fish species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-saltwater-fish-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("saltwater-fish-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
