(function(){'use strict';
/* JAH Chemistry in Daily Life Database generator — jahdb-chemistry-in-daily-life-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHEMIDLS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Cooking Chemistry (Signature Edition)", "The Maillard Reaction (Signature Edition)", "Acids and Bases (Signature Edition)", "Soap Chemistry (Signature Edition)", "Bleach Safety (Signature Edition)", "Batteries (Signature Edition)", "Rust (Signature Edition)", "Fermentation (Signature Edition)", "Baking Chemistry (Signature Edition)", "Cleaning Products (Signature Edition)", "Water Chemistry (Signature Edition)"], "Compounded": ["Polymers and Plastics (Signature Edition)", "Metals (Signature Edition)", "Glass and Ceramics (Signature Edition)", "Cosmetics Chemistry (Signature Edition)", "Food Preservation (Signature Edition)", "Fire and Combustion (Signature Edition)", "Air Chemistry (Signature Edition)", "pH in the Garden (Signature Edition)", "Medicines (Signature Edition)", "Nutrition Chemistry (Signature Edition)", "Dyes and Color (Signature Edition)", "Adhesives (Signature Edition)"], "Advanced": ["Photography Chemistry (Signature Edition)", "Corrosion Prevention (Signature Edition)", "Teaching Chemistry (Signature Edition)", "Green Chemistry (Signature Edition)", "The Annual Curiosity Review (Signature Edition)", "Distillation (Signature Edition)", "Electrolysis (Signature Edition)", "Catalysts (Signature Edition)", "Solutions (Signature Edition)", "Oxidation and Reduction (Signature Edition)", "Chemical Equilibrium (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — chemistry guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — chemistry guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A chemistry guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"chemistry-in-daily-life-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-chemistry-in-daily-life-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("chemistry-in-daily-life-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
