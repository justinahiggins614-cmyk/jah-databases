(function(){'use strict';
/* Signature Dog Breeds Database generator — jahdb-signature-dog-breeds-1.0.
   Property of Justin Addam Higgins (JAH).
   Generates clearly-labeled structural samples only — never presented as real records.
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SDGB-';
var FIELDS=["Herding", "Hound", "Non-Sporting", "Sporting", "Terrier", "Toy", "Working"];

function genBody(id,field,rnd,seed){
  var title='Sample breed concept: '+field+' (seed '+seed+')';
  return {
    id:id, name:title, title:title,
    description:'SAMPLE RECORD (generated — structural sample). A deterministic breed concept sample for '+field+', seed '+seed+'. Generated samples are clearly labeled and never presented as real records.',
    src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not a real record. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample',program:"function sample(){return 'signature-dog-breeds-sample';}",note:'Structural sample demo.'},
    _seed:seed
  };
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return genBody(id,field,rnd,seed);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<3)e.push('name');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-signature-dog-breeds-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('signature-dog-breeds',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
