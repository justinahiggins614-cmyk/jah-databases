(function(){'use strict';
/* JAH Thesaurus Database generator — jahdb-thesaurus-1.0.
   Property of Justin Addam Higgins (JAH).
   A full thesaurus of real English words: synonyms, antonyms, related terms, definitions, and example sentences for every 
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-THES';
var FIELDS=["adjective", "adverb", "noun", "verb"];
var NAMES=["happy", "sad", "angry", "calm", "brave", "kind", "cruel", "honest", "generous", "proud", "humble", "patient", "careful", "big", "small", "fast", "slow", "tall", "short", "long"];
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var name=pick(NAMES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id, name:name, title:name,
    description:'SAMPLE RECORD (generated — structural sample). A '+field+' thesaurus entries generated deterministically from seed '+seed+'. Generated samples are clearly labeled and never presented as real records.',
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not a real entry. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample',program:"function sample(){return '"+name+"';}",note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<2)e.push('name');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name;});
  return dups.length?{ok:false,errors:['duplicate name in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-thesaurus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('thesaurus',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
