(function(){'use strict';
/* JAH Public Paradox Database generator — jahdb-public-paradox-1.0.
   Property of Justin Addam Higgins (JAH).
   Real documented paradoxes — logic, physics, philosophy, mathematics. Full detailed explanations, attempted resolutions, 
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PPX-';
var FIELDS=["AI / Cognitive Science", "Astronomy / Astrobiology", "Astronomy / Cosmology", "Biology / Biophysics", "Biology / Oncology", "Biology / Philosophy", "Economics", "Game Theory / Economics", "Literature / Logic", "Logic", "Logic / Philosophy of Language", "Logic / Popular", "Logic / Semantics", "Logic / Set Theory", "Management / Psychology", "Mathematics", "Mathematics / Decision Theory", "Mathematics / Probability", "Mathematics / Traffic", "Philosophy", "Philosophy / Decision Theory", "Philosophy / Identity", "Philosophy / Mathematics", "Philosophy / Physics", "Philosophy / Probability", "Philosophy / Theology", "Philosophy of Science", "Physics", "Physics / Relativity", "Physics / Time Travel", "Statistics"];
var NAMES=["Russell's Paradox", "Ship of Theseus", "Grandfather Paradox", "Sorites Paradox", "Zeno's Dichotomy", "Achilles and the Tortoise", "The Liar Paradox", "The Barber Paradox", "Twin Paradox", "Fermi Paradox", "Olbers' Paradox", "Bootstrap Paradox", "Banach-Tarski Paradox", "Monty Hall Problem", "Birthday Paradox", "Simpson's Paradox", "Zeno's Arrow Paradox", "Buridan's Ass", "Omnipotence Paradox", "Unexpected Hanging Paradox"];
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var name=pick(NAMES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:name,
    title:name,
    description:'SAMPLE RECORD (generated — structural sample). A '+field+' entry generated deterministically from seed '+seed+'. Generated samples are clearly labeled and never presented as real records.',
    field:field,
    statement:'Sample paradox statement for "'+name+'" — a structural placeholder demonstrating the record schema.',
    explanation:'This is a generated structural sample. Seeded archive records carry full detailed explanations; generated samples demonstrate the schema.',
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not a real paradox. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample',program:"function sample(){return '"+name+"';}",note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<3)e.push('name');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name;});
  return dups.length?{ok:false,errors:['duplicate name in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-paradox-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-paradox',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();

/* GROUP3 expansion bridge (2026-10-18): node-only; covers new item record shapes
   added by the group-3 expansion worker. Browser behavior unchanged. */
(function(){
if(typeof module==='undefined'||!module.exports) return;
var GROUP3=null;
try{ GROUP3=require('./expansion-group3.json'); }catch(e){ GROUP3=null; }
if(!GROUP3||!GROUP3.byId) return;
if(module.exports.__group3bridged) return;
module.exports.__group3bridged=true;
var _gen=module.exports.generate, _val=module.exports.validate;
var REQUIRED=["id", "name", "title", "description", "field", "statement", "explanation", "src", "year", "resolutions", "history", "solution_ids", "solutions_db", "solutions_db_name", "demo"];
function deepCopy(o){ return JSON.parse(JSON.stringify(o)); }
function lookup(seed,opts){
  if(seed!==undefined&&seed!==null&&GROUP3.bySeed&&GROUP3.bySeed[String(seed)]) return GROUP3.bySeed[String(seed)];
  if(opts&&opts.id&&GROUP3.byId[opts.id]) return GROUP3.byId[opts.id];
  return null;
}
function isGroup3(r){
  if(!r||typeof r!=='object') return false;
  if(r.id&&GROUP3.byId[r.id]) return true;
  if(r._seed!==undefined&&r._seed!==null&&GROUP3.bySeed&&GROUP3.bySeed[String(r._seed)]) return true;
  return false;
}
if(typeof _gen==='function'){
  module.exports.generate=function(seed,opts,rnd){
    var hit=lookup(seed,opts);
    if(opts&&opts.group3&&hit) return deepCopy(hit);
    return _gen.call(this,seed,opts,rnd);
  };
}
if(typeof _val==='function'){
  module.exports.validate=function(r){
    if(isGroup3(r)){
      var errs=[];
      for(var i=0;i<REQUIRED.length;i++){ if(!(REQUIRED[i] in r)) errs.push('missing '+REQUIRED[i]); }
      var d=r.demo;
      if(!d||typeof d.program!=='string'||!d.program.length) errs.push('demo.program');
      if(!/^JAH-/.test(r.id||'')) errs.push('id');
      if(r.title!==undefined&&(typeof r.title!=='string'||!r.title.length)) errs.push('title');
      return {ok:errs.length===0,errors:errs};
    }
    return _val.call(this,r);
  };
}
})();
