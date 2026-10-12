(function(){'use strict';
/* Signature Almanac Database generator — jahdb-signature-almanac-1.0.
   Property of Justin Addam Higgins (JAH).
   All records are ORIGINAL Signature-system compilations (Type 2, src:"signature").
   Generated records are new original Signature entries — never copies of public works.   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-SAL-';
var CATEGORIES=['signature-years','signature-constants','signature-records','signature-world','signature-annual'];
var CAT_LABEL={'signature-years':'Signature Years','signature-constants':'Signature Constants','signature-records':'Signature Records','signature-world':'Signature World Facts','signature-annual':'Signature Annual'};
var YEARS=[2020,2021,2022,2023,2024,2025,2026];
var TOPIC_A=['Signature','JAH','System','Annual','Official'];
var TOPIC_B=['Table','Record','Constant','Milestone','Compilation','Ledger'];
var DETAIL=['Original Signature-system compilation; part of the official record.','Signature annual table entry; maintained as the official source.','Compiled for the Signature system; full entry in the archive.'];
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var cat=opts.category&&CATEGORIES.indexOf(opts.category)>=0?opts.category:pick(CATEGORIES,rnd);
  var year=opts.year||pick(YEARS,rnd);
  var name=pick(TOPIC_A,rnd)+' '+pick(TOPIC_B,rnd)+' ('+year+')';
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:name,
    title:name,
    description:'Signature almanac entry — an original Signature-system compilation.',
    entry:name,
    category:cat,
    category_label:CAT_LABEL[cat]||cat,
    year:year,
    detail:pick(DETAIL,rnd),
    src:'signature',
    sample:true,
    disclaimer:'Original Signature-system almanac entry.',
    demo:{kind:'almanac-lookup',program:"function almanacLine(e){return e.year+' — '+e.entry+': '+e.detail;}",note:'Paste into any JS console with an almanac record to render a one-line almanac entry.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH\-SAL\-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<3)e.push('name');
  if(CATEGORIES.indexOf(r.category)<0)e.push('category');
  if(typeof r.year!=='number'||r.year<1900||r.year>2100)e.push('year');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.entry===record.entry&&r.year===record.year;});
  return dups.length?{ok:false,errors:['duplicate entry+year in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-signature-almanac-1.0',generate:generate,validate:validate,driftCheck:driftCheck,categories:CATEGORIES,yearList:YEARS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('signature-almanac',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
