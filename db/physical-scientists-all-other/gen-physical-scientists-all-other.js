(function(){'use strict';
/* Physical Scientists, All Other Database generator — jahdb-physical-scientists-all-other-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-PSA-';
var TITLE='Physical Scientists, All Other';
var DESC='All physical scientists not listed separately.';
var ASPECTS=[["Overview", DESC, "general"], ["Role definition", "What this occupation is, in the occupation's own archived terms: "+DESC+" (Derived directly from the archived occupational description; no additional claims are made here.)", "definition"], ["Preparation guidance", "General guidance for researching preparation for "+TITLE+": consult current official labor-market references and the occupation's professional associations for education, credential, and entry-path facts. This guidance is general occupational-research advice, not "+TITLE+"-specific data, and is labeled as such.", "guidance"], ["Outlook research", "No outlook projection is stored in this record. To assess outlook for "+TITLE+", consult current official labor-market data. This record does not fabricate projections.", "guidance"], ["Record provenance", "Occupational description text derives from public occupational reference data; aspect framing is Signature-authored and clearly labeled. See the src and src_detail fields.", "provenance"]];
function generate(seed,opts){
  opts=opts||{};
  var s=prng(seed);
  var a=ASPECTS[(seed-1)%ASPECTS.length];
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    title:TITLE+' - '+a[0],
    description:DESC,
    aspect:a[0],
    detail:a[1],
    focus:a[2],
    src:'signature',
    src_detail:'Occupational description derives from public occupational reference data; record assembly is Signature-authored and labeled.',
    seed:seed
  };
}
function validate(rec){
  var errs=[];
  if(!rec||typeof rec!=='object')errs.push('not an object');
  if(!rec.id||rec.id.indexOf(PREFIX)!==0)errs.push('id');
  if(!rec.title||rec.title.indexOf(TITLE)!==0)errs.push('title must start with occupation title');
  if(!rec.detail||rec.detail.length<40)errs.push('detail too short to be meaningful');
  if(/Determine and formulate policies/.test(rec.detail||''))errs.push('contaminated overview text (chief-executives leakage)');
  if(/Career paths and progression in|Key skills and requirements for|Educational pathways for|Future trends and outlook for/.test(rec.detail||''))errs.push('filler aspect shell');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===rec.title&&r.aspect===rec.aspect;});
  return dups.length?{ok:false,errors:['duplicate title+aspect already in archive']}:{ok:true,errors:[]};
}

var api={generate:generate,validate:validate,slug:'physical-scientists-all-other',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_physical_scientists_all_other']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('physical-scientists-all-other',api);
})();
