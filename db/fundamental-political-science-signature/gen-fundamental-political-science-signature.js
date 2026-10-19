(function(){'use strict';
/* JAH Signature Political Science Fundamentals Database generator — "jahdb-fundamental-political-science-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FPSS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Power (Signature Edition)", "The State (Signature Edition)", "Democracy (Signature Edition)", "Authoritarianism (Signature Edition)", "Constitutions (Signature Edition)", "Elections (Signature Edition)", "Political Parties (Signature Edition)", "Ideologies (Signature Edition)", "Federalism (Signature Edition)", "Rights (Signature Edition)", "The Social Contract (Signature Edition)", "Political Culture (Signature Edition)"], "Compounded": ["Legislatures (Signature Edition)", "Executives (Signature Edition)", "Courts (Signature Edition)", "Public Policy (Signature Edition)", "Voting Behavior (Signature Edition)", "Interest Groups (Signature Edition)", "Media and Politics (Signature Edition)", "Local Government (Signature Edition)", "Diplomacy (Signature Edition)", "Political Economy (Signature Edition)", "Civil Society (Signature Edition)", "Campaigns (Signature Edition)"], "Advanced": ["International Relations Theory (Signature Edition)", "The Comparative Method (Signature Edition)", "The Democratic Peace (Signature Edition)", "The Resource Curse (Signature Edition)", "The Security Dilemma (Signature Edition)", "The Political Spectrum Deep Dive (Signature Edition)", "Teaching Politics (Signature Edition)", "The Analyst's Toolkit (Signature Edition)", "The Future of Governance (Signature Edition)", "The Political Science Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — fundamental-political-science-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — Signature-original fundamental record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original fundamental record study. Signature original samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-fundamental-political-science-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-political-science-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
