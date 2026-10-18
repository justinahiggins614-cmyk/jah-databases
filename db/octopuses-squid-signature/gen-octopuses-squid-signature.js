(function(){'use strict';
/* JAH Signature Octopuses and Squid Database generator — jahdb-octopuses-squid-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OCTS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Common Octopus (Octopus vulgaris)", "Signature Study: Giant Pacific Octopus (Enteroctopus dofleini)", "Signature Study: Blue-ringed Octopus (Hapalochlaena lunulata)", "Signature Study: Mimic Octopus (Thaumoctopus mimicus)", "Signature Study: Coconut Octopus (Amphioctopus marginatus)", "Signature Study: Caribbean Reef Octopus (Octopus briareus)", "Signature Study: Day Octopus (Octopus cyanea)", "Signature Study: East Pacific Red Octopus (Octopus rubescens)", "Signature Study: California Two-spot Octopus (Octopus bimaculoides)", "Signature Study: Atlantic Pygmy Octopus (Octopus joubini)", "Signature Study: Star-sucker Pygmy Octopus (Octopus wolfi)"], "Compounded": ["Signature Study: Seven-arm Octopus (Haliphron atlanticus)", "Signature Study: Blanket Octopus (Tremoctopus violaceus)", "Signature Study: Argonaut (Argonauta argo)", "Signature Study: Chambered Nautilus (Nautilus pompilius)", "Signature Study: Common Cuttlefish (Sepia officinalis)", "Signature Study: Flamboyant Cuttlefish (Metasepia pfefferi)", "Signature Study: Broadclub Cuttlefish (Sepia latimanus)", "Signature Study: Giant Cuttlefish (Sepia apama)", "Signature Study: Hawaiian Bobtail Squid (Euprymna scolopes)", "Signature Study: Caribbean Reef Squid (Sepioteuthis sepioidea)", "Signature Study: Bigfin Reef Squid (Sepioteuthis lessoniana)", "Signature Study: Humboldt Squid (Dosidicus gigas)"], "Advanced": ["Signature Study: Japanese Flying Squid (Todarodes pacificus)", "Signature Study: European Squid (Loligo vulgaris)", "Signature Study: California Market Squid (Doryteuthis opalescens)", "Signature Study: Firefly Squid (Watasenia scintillans)", "Signature Study: Giant Squid (Architeuthis dux)", "Signature Study: Vampire Squid (Vampyroteuthis infernalis)", "Signature Study: Striped Pyjama Squid (Sepioloidea lineolata)", "Signature Study: Wonderpus (Wunderpus photogenicus)", "Signature Study: Maori Octopus (Macroctopus maorum)", "Signature Study: Sydney Octopus (Octopus tetricus)", "Signature Study: Mudflat Octopus (Octopus huttoni)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature octopus and squid species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-octopuses-squid-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("octopuses-squid-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
