(function(){'use strict';
/* JAH Signature Renaissance Database generator — "jahdb-history-renaissance-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HRES-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Renaissance: An Overview (Signature Edition)", "Florence and the Medici (Signature Edition)", "Humanism: The New Learning (Signature Edition)", "Brunelleschi: Dome and Perspective (Signature Edition)", "Donatello (Signature Edition)", "Leonardo da Vinci (Signature Edition)", "Michelangelo (Signature Edition)", "Raphael (Signature Edition)", "Gutenberg and the Printing Press (Signature Edition)", "The Northern Renaissance (Signature Edition)", "The Renaissance Papacy (Signature Edition)", "Venice: The Serenissima (Signature Edition)"], "Compounded": ["Erasmus (Signature Edition)", "Thomas More and Utopia (Signature Edition)", "Machiavelli and The Prince (Signature Edition)", "The Borgias (Signature Edition)", "Savonarola: The Bonfire of the Vanities (Signature Edition)", "The Sistine Chapel (Signature Edition)", "Titian and Venetian Color (Signature Edition)", "Copernicus and the New Cosmos (Signature Edition)", "The Greek Scholars' Exodus (Signature Edition)", "Durer: The Print Revolution (Signature Edition)", "The Reformation's Renaissance Roots (Signature Edition)", "The Sack of Rome (1527) (Signature Edition)"], "Advanced": ["Renaissance Women (Signature Edition)", "Patronage and the Art Market (Signature Edition)", "Renaissance Science (Signature Edition)", "Castiglione and the Courtier (Signature Edition)", "The Renaissance State (Signature Edition)", "Music of the Renaissance (Signature Edition)", "Leonardo's Notebooks (Signature Edition)", "The Legacy of the Renaissance (Signature Edition)", "The Press and Its Consequences (Signature Edition)", "Renaissance Warfare (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-renaissance-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-history-renaissance-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-renaissance-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
