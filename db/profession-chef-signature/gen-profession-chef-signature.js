(function(){'use strict';
/* JAH Signature Chef Profession Database generator — "jahdb-profession-chef-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCHS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["What Chefs Do (Signature Edition)", "History of the Culinary Profession (Signature Edition)", "Core Culinary Skills (Signature Edition)", "Training Paths (Signature Edition)", "Certification (Signature Edition)", "Tools of the Trade (Signature Edition)", "A Day in the Life (Signature Edition)", "Kitchens and Settings (Signature Edition)", "Culinary Ethics (Signature Edition)", "Pay and Career Outlook (Signature Edition)", "Giants of the Kitchen (Signature Edition)", "Getting Started (Signature Edition)"], "Compounded": ["The Brigade System (Signature Edition)", "Running the Pass (Signature Edition)", "Menu Design and Engineering (Signature Edition)", "Food Cost Control (Signature Edition)", "The Sous Chef (Signature Edition)", "Pastry and Baking (Signature Edition)", "Butchery and Fish (Signature Edition)", "Wine and Beverage Program (Signature Edition)", "The Private Chef (Signature Edition)", "Catering and Events (Signature Edition)", "Food Safety: HACCP (Signature Edition)", "Opening a Restaurant (Signature Edition)"], "Advanced": ["The Executive Chef (Signature Edition)", "Michelin and the Awards (Signature Edition)", "The Chef's Media and Brand (Signature Edition)", "The Chef's Philosophy (Signature Edition)", "Kitchen Culture Reformed (Signature Edition)", "Teaching the Craft (Signature Edition)", "The Chef's Legacy (Signature Edition)", "The Restaurant Group (Signature Edition)", "The Profession's Impact (Signature Edition)", "The Master's Table (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — profession-chef-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original profession record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original profession record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-profession-chef-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("profession-chef-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
