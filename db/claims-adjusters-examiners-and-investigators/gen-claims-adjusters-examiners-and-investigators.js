(function(){'use strict';
/* Claims Adjusters, Examiners, and Investigators Database generator — jahdb-claims-adjusters-examiners-and-investigators-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-CAE-';
var TITLE='Claims Adjusters, Examiners, and Investigators';
var DESC='Review settled claims to determine that payments and settlements are made in accordance with company practices and procedures. Confer with legal counsel on claims requiring litigation. May also settle';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Claims Adjusters, Examiners, and Investigators.", "careers"], ["Skills", "Key skills and requirements for Claims Adjusters, Examiners, and Investigators.", "skills"], ["Education", "Educational pathways for Claims Adjusters, Examiners, and Investigators.", "education"], ["Outlook", "Future trends and outlook for Claims Adjusters, Examiners, and Investigators.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'claims-adjusters-examiners-and-investigators',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_claims_adjusters_examiners_and_investigators']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('claims-adjusters-examiners-and-investigators',api);
})();
