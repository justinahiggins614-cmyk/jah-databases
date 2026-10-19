(function(){'use strict';
/* JAH Signature Ancient Greece Database generator — "jahdb-history-ancient-greece-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HGRS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Land and the Polis (Signature Edition)", "Minoans and Mycenaeans (Signature Edition)", "The Archaic Rebirth (Signature Edition)", "Classical Athens and Democracy (Signature Edition)", "Sparta: The Military Polis (Signature Edition)", "The Persian Wars (Signature Edition)", "Socrates, Plato, Aristotle (Signature Edition)", "Alexander the Great (Signature Edition)", "The Hellenistic World (Signature Edition)", "Tragedy and Comedy (Signature Edition)", "The Olympic Games (Signature Edition)", "The Peloponnesian War and Thucydides (Signature Edition)"], "Compounded": ["Philip II and the Rise of Macedon (Signature Edition)", "Gods, Oracles, and Mysteries (Signature Edition)", "Homer and the Epic Tradition (Signature Edition)", "Herodotus and the Invention of History (Signature Edition)", "Stoics and Epicureans (Signature Edition)", "Greek Science and Mathematics (Signature Edition)", "The Orders of Architecture (Signature Edition)", "Triremes and the Phalanx (Signature Edition)", "Greece Under Rome (Signature Edition)", "Sappho and Lyric Poetry (Signature Edition)", "The Sacred Band of Thebes (Signature Edition)", "Greek Colonization (Signature Edition)"], "Advanced": ["Vase Painting: Pictures of Greek Life (Signature Edition)", "The Presocratics: First Physics (Signature Edition)", "Women in Ancient Greece (Signature Edition)", "Slavery and the Greek Economy (Signature Edition)", "Hippocrates and Greek Medicine (Signature Edition)", "The Delian League: Alliance to Empire (Signature Edition)", "The Spaces of the Polis (Signature Edition)", "The Successor Kingdoms and Rome's Rise (Signature Edition)", "Inscriptions: The Paperwork of Greece (Signature Edition)", "The Afterlife of Greek Thought (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-ancient-greece-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-history-ancient-greece-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-ancient-greece-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
