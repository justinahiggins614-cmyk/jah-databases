(function(){'use strict';
/* JAH Signature Ancient Egypt Database generator — "jahdb-history-ancient-egypt-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HEGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Nile: Egypt's Lifeline (Signature Edition)", "Unification of Upper and Lower Egypt (Signature Edition)", "The Pharaoh: God-King (Signature Edition)", "The Pyramids of Giza (Signature Edition)", "Hieroglyphs and the Scribes (Signature Edition)", "Mummification and the Afterlife (Signature Edition)", "The Gods of Egypt (Signature Edition)", "The Old Kingdom: Age of the Pyramid Builders (Signature Edition)", "The Middle Kingdom: The Classical Age (Signature Edition)", "The New Kingdom: Empire (Signature Edition)", "Tutankhamun: The Boy King (Signature Edition)", "The Rosetta Stone (Signature Edition)"], "Compounded": ["Hatshepsut: The Woman Who Was King (Signature Edition)", "Akhenaten and the Amarna Revolution (Signature Edition)", "Ramesses II: The Great Ancestor (Signature Edition)", "The Battle of Kadesh (Signature Edition)", "The Workers of Deir el-Medina (Signature Edition)", "Egyptian Medicine (Signature Edition)", "The Ptolemaic Kingdom and Cleopatra (Signature Edition)", "Nubia: Egypt's Southern Rival and Partner (Signature Edition)", "The Sea Peoples and the Bronze Age Collapse (Signature Edition)", "Egyptian Mathematics and Astronomy (Signature Edition)", "The Book of the Dead (Signature Edition)", "Trade and the Punt Expedition (Signature Edition)"], "Advanced": ["The Amarna Letters (Signature Edition)", "Decipherment: Champollion's Breakthrough (Signature Edition)", "The Pyramid Texts and Coffin Texts (Signature Edition)", "Deir el-Bahari: Hatshepsut's Temple (Signature Edition)", "The Hyksos Interlude (Signature Edition)", "Late Period and Persian Rule (Signature Edition)", "Egyptian Law and Justice (Signature Edition)", "The Fate of the Mummies: Modern Egyptology (Signature Edition)", "Abu Simbel: Rescue of the Colossi (Signature Edition)", "The Edfu Temple: Egypt's Best-Preserved Shrine (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-ancient-egypt-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original history record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original history record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-history-ancient-egypt-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-ancient-egypt-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
