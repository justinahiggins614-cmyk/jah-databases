(function(){'use strict';
/* JAH Signature Mystery and Detective Database generator — "jahdb-literature-mystery-detective-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMYS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Murders in the Rue Morgue — Edgar Allan Poe (Signature Edition)", "The Hound of the Baskervilles — Arthur Conan Doyle (Signature Edition)", "The Maltese Falcon — Dashiell Hammett (Signature Edition)", "And Then There Were None — Agatha Christie (Signature Edition)", "The Big Sleep — Raymond Chandler (Signature Edition)", "The Murder of Roger Ackroyd — Agatha Christie (Signature Edition)", "The Long Goodbye — Raymond Chandler (Signature Edition)", "The Girl with the Dragon Tattoo — Stieg Larsson (Signature Edition)", "Gone Girl — Gillian Flynn (Signature Edition)", "The Da Vinci Code — Dan Brown (Signature Edition)", "The No. 1 Ladies' Detective Agency — Alexander McCall Smith (Signature Edition)", "The Curious Incident — Mark Haddon (Signature Edition)"], "Compounded": ["The Moonstone — Wilkie Collins (Signature Edition)", "The Woman in White — Wilkie Collins (Signature Edition)", "The Thin Man — Dashiell Hammett (Signature Edition)", "The Postman Always Rings Twice — James M. Cain (Signature Edition)", "Double Indemnity — James M. Cain (Signature Edition)", "The Talented Mr. Ripley — Patricia Highsmith (Signature Edition)", "In Cold Blood — Truman Capote (Signature Edition)", "The Name of the Rose — Umberto Eco (Signature Edition)", "The Alienist — Caleb Carr (Signature Edition)", "Tinker Tailor Soldier Spy — John le Carré (Signature Edition)", "The Day of the Jackal — Frederick Forsyth (Signature Edition)", "Farewell, My Lovely — Raymond Chandler (Signature Edition)"], "Advanced": ["The Secret History — Donna Tartt (Signature Edition)", "The Yiddish Policemen's Union — Michael Chabon (Signature Edition)", "Motherless Brooklyn — Jonathan Lethem (Signature Edition)", "The City & the City — China Miéville (Signature Edition)", "The Devotion of Suspect X — Keigo Higashino (Signature Edition)", "The Tokyo Zodiac Murders — Soji Shimada (Signature Edition)", "Out — Natsuo Kirino (Signature Edition)", "The Intuitionist — Colson Whitehead (Signature Edition)", "In the Woods — Tana French (Signature Edition)", "The Crying of Lot 49 — Thomas Pynchon (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — literature-mystery-detective-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-literature-mystery-detective-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("literature-mystery-detective-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
