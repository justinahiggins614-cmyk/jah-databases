(function(){'use strict';
/* JAH Ancient Greece Database generator — "jahdb-history-ancient-greece-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HGR-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Land and the Polis", "Minoans and Mycenaeans", "The Archaic Rebirth", "Classical Athens and Democracy", "Sparta: The Military Polis", "The Persian Wars", "Socrates, Plato, Aristotle", "Alexander the Great", "The Hellenistic World", "Tragedy and Comedy", "The Olympic Games", "The Peloponnesian War and Thucydides"], "Compounded": ["Philip II and the Rise of Macedon", "Gods, Oracles, and Mysteries", "Homer and the Epic Tradition", "Herodotus and the Invention of History", "Stoics and Epicureans", "Greek Science and Mathematics", "The Orders of Architecture", "Triremes and the Phalanx", "Greece Under Rome", "Sappho and Lyric Poetry", "The Sacred Band of Thebes", "Greek Colonization"], "Advanced": ["Vase Painting: Pictures of Greek Life", "The Presocratics: First Physics", "Women in Ancient Greece", "Slavery and the Greek Economy", "Hippocrates and Greek Medicine", "The Delian League: Alliance to Empire", "The Spaces of the Polis", "The Successor Kingdoms and Rome's Rise", "Inscriptions: The Paperwork of Greece", "The Afterlife of Greek Thought"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-ancient-greece demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-history-ancient-greece-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-ancient-greece",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
