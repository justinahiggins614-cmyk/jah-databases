(function(){'use strict';
/* Administrative Law Judges, Adjudicators, and Hearing Officers Database generator — jahdb-administrative-law-judges-adjudicators-and-hearing-officers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-ALJ-';
var TITLE='Administrative Law Judges, Adjudicators, and Hearing Officers';
var DESC='Conduct hearings to recommend or make decisions on claims concerning government programs or other government-related matters. Determine liability, sanctions, or penalties, or recommend the acceptance ';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Administrative Law Judges, Adjudicators, and Hearing Officers.", "careers"], ["Skills", "Key skills and requirements for Administrative Law Judges, Adjudicators, and Hearing Officers.", "skills"], ["Education", "Educational pathways for Administrative Law Judges, Adjudicators, and Hearing Officers.", "education"], ["Outlook", "Future trends and outlook for Administrative Law Judges, Adjudicators, and Hearing Officers.", "outlook"]];
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
    seed:seed
  };
}
function validate(rec){
  return rec&&rec.id&&rec.title&&rec.id.indexOf(PREFIX)===0;
}
var api={generate:generate,validate:validate,slug:'administrative-law-judges-adjudicators-and-hearing-officers',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_administrative_law_judges_adjudicators_and_hearing_officers']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('administrative-law-judges-adjudicators-and-hearing-officers',api);
})();
