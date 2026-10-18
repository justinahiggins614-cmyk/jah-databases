(function(){'use strict';
/* JAH Signature Crocodilians Database generator — jahdb-crocodilians-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CROCS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Saltwater Crocodile (Crocodylus porosus)", "Signature Study: Nile Crocodile (Crocodylus niloticus)", "Signature Study: American Crocodile (Crocodylus acutus)", "Signature Study: Orinoco Crocodile (Crocodylus intermedius)", "Signature Study: Cuban Crocodile (Crocodylus rhombifer)", "Signature Study: Siamese Crocodile (Crocodylus siamensis)", "Signature Study: Philippine Crocodile (Crocodylus mindorensis)", "Signature Study: Mugger Crocodile (Crocodylus palustris)", "Signature Study: Freshwater Crocodile (Crocodylus johnstoni)", "Signature Study: Morelet's Crocodile (Crocodylus moreletii)", "Signature Study: Slender-snouted Crocodile (Mecistops cataphractus)"], "Compounded": ["Signature Study: Dwarf Crocodile (Osteolaemus tetraspis)", "Signature Study: American Alligator (Alligator mississippiensis)", "Signature Study: Chinese Alligator (Alligator sinensis)", "Signature Study: Black Caiman (Melanosuchus niger)", "Signature Study: Spectacled Caiman (Caiman crocodilus)", "Signature Study: Yacare Caiman (Caiman yacare)", "Signature Study: Broad-snouted Caiman (Caiman latirostris)", "Signature Study: Cuvier's Dwarf Caiman (Paleosuchus palpebrosus)", "Signature Study: Schneider's Dwarf Caiman (Paleosuchus trigonatus)", "Signature Study: Gharial (Gavialis gangeticus)", "Signature Study: False Gharial (Tomistoma schlegelii)", "Signature Study: Deinosuchus (Deinosuchus riograndensis)"], "Advanced": ["Signature Study: Sarcosuchus (Sarcosuchus imperator)", "Signature Study: Purussaurus (Purussaurus brasiliensis)", "Signature Study: Mourasuchus (Mourasuchus amazonensis)", "Signature Study: Stomatosuchus (Stomatosuchus inermis)", "Signature Study: Rhamphosuchus (Rhamphosuchus crassidens)", "Signature Study: Gryposuchus (Gryposuchus neogaeus)", "Signature Study: Quinkana (Quinkana fortirostrum)", "Signature Study: Mekosuchus (Mekosuchus inexpectatus)", "Signature Study: Voay (Voay robustus)", "Signature Study: Euthecodon (Euthecodon brumpti)", "Signature Study: Crocodylus thorbjarnarsoni (Crocodylus thorbjarnarsoni)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature crocodilian species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-crocodilians-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("crocodilians-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
