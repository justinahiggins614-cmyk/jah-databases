(function(){'use strict';
/* JAH Ancient Egypt Database generator — "jahdb-history-ancient-egypt-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HEG-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Nile: Egypt's Lifeline", "Unification of Upper and Lower Egypt", "The Pharaoh: God-King", "The Pyramids of Giza", "Hieroglyphs and the Scribes", "Mummification and the Afterlife", "The Gods of Egypt", "The Old Kingdom: Age of the Pyramid Builders", "The Middle Kingdom: The Classical Age", "The New Kingdom: Empire", "Tutankhamun: The Boy King", "The Rosetta Stone"], "Compounded": ["Hatshepsut: The Woman Who Was King", "Akhenaten and the Amarna Revolution", "Ramesses II: The Great Ancestor", "The Battle of Kadesh", "The Workers of Deir el-Medina", "Egyptian Medicine", "The Ptolemaic Kingdom and Cleopatra", "Nubia: Egypt's Southern Rival and Partner", "The Sea Peoples and the Bronze Age Collapse", "Egyptian Mathematics and Astronomy", "The Book of the Dead", "Trade and the Punt Expedition"], "Advanced": ["The Amarna Letters", "Decipherment: Champollion's Breakthrough", "The Pyramid Texts and Coffin Texts", "Deir el-Bahari: Hatshepsut's Temple", "The Hyksos Interlude", "Late Period and Persian Rule", "Egyptian Law and Justice", "The Fate of the Mummies: Modern Egyptology", "Abu Simbel: Rescue of the Colossi", "The Edfu Temple: Egypt's Best-Preserved Shrine"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-ancient-egypt demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — history record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A history record study. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest-sample",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-history-ancient-egypt-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-ancient-egypt",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
