(function(){'use strict';
/* JAH Signature World Epics Database generator — "jahdb-literature-world-epics-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LEPS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Epic of Gilgamesh (Signature Edition)", "The Iliad — Homer (Signature Edition)", "The Odyssey — Homer (Signature Edition)", "The Aeneid — Virgil (Signature Edition)", "Beowulf (Signature Edition)", "The Mahabharata (Signature Edition)", "The Ramayana — Valmiki (Signature Edition)", "The Divine Comedy — Dante (Signature Edition)", "Paradise Lost — John Milton (Signature Edition)", "The Shahnameh — Ferdowsi (Signature Edition)", "The Nibelungenlied (Signature Edition)", "The Song of Roland (Signature Edition)"], "Compounded": ["The Kalevala — Elias Lönnrot (Signature Edition)", "The Popol Vuh (Signature Edition)", "The Epic of Sundiata (Signature Edition)", "The Enuma Elish (Signature Edition)", "The Theogony — Hesiod (Signature Edition)", "The Argonautica — Apollonius (Signature Edition)", "Orlando Furioso — Ludovico Ariosto (Signature Edition)", "The Lusiads — Luís de Camões (Signature Edition)", "Cantar de Mio Cid (Signature Edition)", "Jerusalem Delivered — Torquato Tasso (Signature Edition)", "Táin Bó Cúailnge (Signature Edition)", "The Epic of King Gesar (Signature Edition)"], "Advanced": ["The Tale of the Heike (Signature Edition)", "Water Margin (Signature Edition)", "Journey to the West (Signature Edition)", "Romance of the Three Kingdoms (Signature Edition)", "The Epic of Manas (Signature Edition)", "The Book of Dede Korkut (Signature Edition)", "Kalevipoeg — Friedrich Kreutzwald (Signature Edition)", "The Song of Hiawatha — Longfellow (Signature Edition)", "The Epic of Askia (Signature Edition)", "Omeros — Derek Walcott (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — literature-world-epics-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original literary record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original literary record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-literature-world-epics-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("literature-world-epics-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
