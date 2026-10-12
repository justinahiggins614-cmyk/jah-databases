(function(){'use strict';
/* Public Almanac Database generator — jahdb-public-almanac-1.0.
   Property of Justin Addam Higgins (JAH).
   Seeded records are REAL almanac facts (Type 1 public info). Generated records are
   CLEARLY labeled samples (src:"signature-generated-sample") — never presented as real facts.   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-ALM-';
var CATEGORIES=['world-records','population','science','countries','history-events','annual'];
var CAT_LABEL={'world-records':'World Records','population':'Population','science':'Science & Measurement','countries':'Countries & Peoples','history-events':'Historic Events','annual':'Year in Review'};
var YEARS=[2020,2021,2022,2023,2024,2025,2026];
var TOPIC_A=['World','Annual','Global','Historic','Record','Statistical'];
var TOPIC_B=['Fact File','Data Table','Milestone','Benchmark','Compendium','Register'];
var DETAIL=['Compiled from public statistical sources; verify against the cited year.','Standard reference entry; cross-check with annual publications.','Widely cited public figure; see annual review for context.'];
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
    description:'SAMPLE ALMANAC ENTRY (generated — not a real fact). A structural almanac sample. Generated samples must never be treated as real records.',
    entry:name,
    category:cat,
    category_label:CAT_LABEL[cat]||cat,
    year:year,
    detail:pick(DETAIL,rnd),
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample entry — not a real almanac fact. Seeded archive records are real facts; this generated record is structural only.',
    demo:{kind:'almanac-lookup',program:"function almanacLine(e){return e.year+' — '+e.entry+': '+e.detail;}",note:'Paste into any JS console with an almanac record to render a one-line almanac entry.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH\-ALM\-\d{6}$/.test(r.id||''))e.push('id');
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
var gen={version:'jahdb-public-almanac-1.0',generate:generate,validate:validate,driftCheck:driftCheck,categories:CATEGORIES,yearList:YEARS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-almanac',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
