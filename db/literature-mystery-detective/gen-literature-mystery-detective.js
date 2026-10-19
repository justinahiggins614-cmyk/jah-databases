(function(){'use strict';
/* JAH Mystery and Detective Database generator — "jahdb-literature-mystery-detective-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LMY-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Murders in the Rue Morgue — Edgar Allan Poe", "The Hound of the Baskervilles — Arthur Conan Doyle", "The Maltese Falcon — Dashiell Hammett", "And Then There Were None — Agatha Christie", "The Big Sleep — Raymond Chandler", "The Murder of Roger Ackroyd — Agatha Christie", "The Long Goodbye — Raymond Chandler", "The Girl with the Dragon Tattoo — Stieg Larsson", "Gone Girl — Gillian Flynn", "The Da Vinci Code — Dan Brown", "The No. 1 Ladies' Detective Agency — Alexander McCall Smith", "The Curious Incident — Mark Haddon"], "Compounded": ["The Moonstone — Wilkie Collins", "The Woman in White — Wilkie Collins", "The Thin Man — Dashiell Hammett", "The Postman Always Rings Twice — James M. Cain", "Double Indemnity — James M. Cain", "The Talented Mr. Ripley — Patricia Highsmith", "In Cold Blood — Truman Capote", "The Name of the Rose — Umberto Eco", "The Alienist — Caleb Carr", "Tinker Tailor Soldier Spy — John le Carré", "The Day of the Jackal — Frederick Forsyth", "Farewell, My Lovely — Raymond Chandler"], "Advanced": ["The Secret History — Donna Tartt", "The Yiddish Policemen's Union — Michael Chabon", "Motherless Brooklyn — Jonathan Lethem", "The City & the City — China Miéville", "The Devotion of Suspect X — Keigo Higashino", "The Tokyo Zodiac Murders — Soji Shimada", "Out — Natsuo Kirino", "The Intuitionist — Colson Whitehead", "In the Woods — Tana French", "The Crying of Lot 49 — Thomas Pynchon"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — literature-mystery-detective demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — literary record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A literary record study. Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-literature-mystery-detective-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("literature-mystery-detective",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
