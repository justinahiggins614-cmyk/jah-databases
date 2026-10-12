(function(){'use strict';
/* Engineering Technologists and Technicians, Except Drafters, All Other Database generator — jahdb-engineering-technologists-and-technicians-except-drafters-al-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-ETA-';
var TITLE='Engineering Technologists and Technicians, Except Drafters, All Other';
var DESC='All engineering technologists and technicians, except drafters, not listed separately.';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Engineering Technologists and Technicians, Except Drafters, All Other.", "careers"], ["Skills", "Key skills and requirements for Engineering Technologists and Technicians, Except Drafters, All Other.", "skills"], ["Education", "Educational pathways for Engineering Technologists and Technicians, Except Drafters, All Other.", "education"], ["Outlook", "Future trends and outlook for Engineering Technologists and Technicians, Except Drafters, All Other.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'engineering-technologists-and-technicians-except-drafters-al',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_engineering_technologists_and_technicians_except_drafters_al']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('engineering-technologists-and-technicians-except-drafters-al',api);
})();
