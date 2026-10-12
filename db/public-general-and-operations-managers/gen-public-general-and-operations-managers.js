(function(){'use strict';
/* Public General and Operations Managers Database generator — jahdb-public-general-and-operations-managers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 1: Public information database. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-GAO-';
var TITLE='General and Operations Managers';
var DESC='Plan, direct, or coordinate the operations of public or private sector organizations, overseeing multiple departments or locations. Duties and responsibilities include formulating policies, managing d';
var ASPECTS=[["Overview", "Plan, direct, or coordinate the operations of public or private sector organizations, overseeing multiple departments or locations. Duties and responsibilities include formulating policies, managing d", "general"], ["Career Path", "Career paths and progression in General and Operations Managers.", "careers"], ["Skills", "Key skills and requirements for General and Operations Managers.", "skills"], ["Education", "Educational pathways for General and Operations Managers.", "education"], ["Outlook", "Future trends and outlook for General and Operations Managers.", "outlook"]];
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
    src:'public-harvest',
    seed:seed
  };
}
function validate(rec){
  return rec&&rec.id&&rec.title&&rec.id.indexOf(PREFIX)===0;
}
var api={generate:generate,validate:validate,slug:'public-general-and-operations-managers',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_public_general_and_operations_managers']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-general-and-operations-managers',api);
})();
