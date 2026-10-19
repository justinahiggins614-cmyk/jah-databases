(function(){'use strict';
/* JAH Signature Industrial Revolution Database generator — "jahdb-history-industrial-revolution-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HIRS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Industrial Revolution: An Overview (Signature Edition)", "Textiles: The Leading Industry (Signature Edition)", "Watt's Steam Engine (Signature Edition)", "Coal and Iron (Signature Edition)", "The Railways (Signature Edition)", "The Factory System (Signature Edition)", "The Industrial Cities (Signature Edition)", "Workers and Unions (Signature Edition)", "The Inventors (Signature Edition)", "Steamships and the Telegraph (Signature Edition)", "The Spread of Industrialism (Signature Edition)", "The Second Industrial Revolution (Signature Edition)"], "Compounded": ["The Engine's Lineage: Newcomen to Trevithick (Signature Edition)", "Arkwright and the Factory (Signature Edition)", "The Luddites (Signature Edition)", "Peterloo (1819) (Signature Edition)", "Chartism (Signature Edition)", "The Railway Navvies (Signature Edition)", "The Great Exhibition (1851) (Signature Edition)", "The Cotton Famine (Signature Edition)", "Bessemer and the Age of Steel (Signature Edition)", "Electricity: The Wired World (Signature Edition)", "Chemicals: Dyes and Dynamite (Signature Edition)", "The Internal Combustion Engine (Signature Edition)"], "Advanced": ["Ford and the Assembly Line (Signature Edition)", "The Slums and Public Health (Signature Edition)", "Women and Children in the Mills (Signature Edition)", "The Industrial Novel (Signature Edition)", "Empire and Industry (Signature Edition)", "The Industrial Environment (Signature Edition)", "Industrial Time (Signature Edition)", "The Legacy: The World the Revolution Made (Signature Edition)", "Debating the Revolution (Signature Edition)", "The Global Shadow (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — history-industrial-revolution-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-history-industrial-revolution-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("history-industrial-revolution-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
