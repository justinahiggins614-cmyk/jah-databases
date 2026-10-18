(function(){'use strict';
/* JAH Signature 19th Century Database generator — jahdb-19th-century-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-19THCS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The 19th Century: An Overview (Signature Edition)", "The Napoleonic Wars (Signature Edition)", "The Congress of Vienna (Signature Edition)", "The Industrial Revolution Spreads (Signature Edition)", "The American Civil War (Signature Edition)", "Abolition in the United States (Signature Edition)", "Darwin and On the Origin of Species (Signature Edition)", "The Railway Age (Signature Edition)", "The Telegraph (Signature Edition)", "The Telephone (Signature Edition)", "The Light Bulb (Signature Edition)"], "Compounded": ["The Meiji Restoration (Signature Edition)", "The Scramble for Africa (Signature Edition)", "The Crimean War (Signature Edition)", "Italian Unification (Signature Edition)", "German Unification (Signature Edition)", "The Franco-Prussian War (Signature Edition)", "Germ Theory and Pasteur (Signature Edition)", "Mendeleev's Periodic Table (Signature Edition)", "Photography Is Born (Signature Edition)", "The Suez Canal (Signature Edition)", "The Transatlantic Cable (Signature Edition)", "Women's Suffrage Movements Begin (Signature Edition)"], "Advanced": ["Maxwell and Electromagnetism (Signature Edition)", "Thermodynamics Comes of Age (Signature Edition)", "The Gold Rushes (Signature Edition)", "Impressionism (Signature Edition)", "The Boxer Rebellion (Signature Edition)", "The Spanish-American War (Signature Edition)", "Psychoanalysis Begins (Signature Edition)", "The Typewriter and the Office (Signature Edition)", "The Steel Age (Signature Edition)", "Realism in Literature (Signature Edition)", "The Century Turns: 1900 in Review (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — 19th-century-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — century record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A century record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"19th-century-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-19th-century-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("19th-century-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
