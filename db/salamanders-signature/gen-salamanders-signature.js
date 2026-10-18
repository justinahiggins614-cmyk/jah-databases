(function(){'use strict';
/* JAH Signature Salamanders Database generator — jahdb-salamanders-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SALMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Axolotl (Ambystoma mexicanum)", "Signature Study: Tiger Salamander (Ambystoma tigrinum)", "Signature Study: Spotted Salamander (Ambystoma maculatum)", "Signature Study: Hellbender (Cryptobranchus alleganiensis)", "Signature Study: Chinese Giant Salamander (Andrias davidianus)", "Signature Study: Japanese Giant Salamander (Andrias japonicus)", "Signature Study: Mudpuppy (Necturus maculosus)", "Signature Study: Northern Red Salamander (Pseudotriton ruber)", "Signature Study: Eastern Newt (Notophthalmus viridescens)", "Signature Study: Smooth Newt (Lissotriton vulgaris)", "Signature Study: Alpine Newt (Ichthyosaura alpestris)"], "Compounded": ["Signature Study: Great Crested Newt (Triturus cristatus)", "Signature Study: Marbled Newt (Triturus marmoratus)", "Signature Study: Fire Salamander (Salamandra salamandra)", "Signature Study: Olm (Proteus anguinus)", "Signature Study: California Giant Salamander (Dicamptodon ensatus)", "Signature Study: Ensatina (Ensatina eschscholtzii)", "Signature Study: Eastern Red-backed Salamander (Plethodon cinereus)", "Signature Study: Northern Slimy Salamander (Plethodon glutinosus)", "Signature Study: Cave Salamander (Eurycea lucifuga)", "Signature Study: Long-tailed Salamander (Eurycea longicauda)", "Signature Study: Spring Salamander (Gyrinophilus porphyriticus)", "Signature Study: Two-lined Salamander (Eurycea bislineata)"], "Advanced": ["Signature Study: Northern Dusky Salamander (Desmognathus fuscus)", "Signature Study: Seal Salamander (Desmognathus monticola)", "Signature Study: Greater Siren (Siren lacertina)", "Signature Study: Lesser Siren (Siren intermedia)", "Signature Study: Two-toed Amphiuma (Amphiuma means)", "Signature Study: Iberian Ribbed Newt (Pleurodeles waltl)", "Signature Study: Mandarin Salamander (Tylototriton shanjing)", "Signature Study: Himalayan Crocodile Newt (Tylototriton verrucosus)", "Signature Study: Anderson's Salamander (Ambystoma andersoni)", "Signature Study: Santa Cruz Long-toed Salamander (Ambystoma macrodactylum croceum)", "Signature Study: Texas Blind Salamander (Eurycea rathbuni)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature salamander species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-salamanders-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("salamanders-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
