(function(){'use strict';
/* Public Human Factors Engineers and Ergonomists Database generator — jahdb-public-human-factors-engineers-and-ergonomists-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 1: Public information database. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-HFE-';
var TITLE='Human Factors Engineers and Ergonomists';
var DESC='Design objects, facilities, and environments to optimize human well-being and overall system performance, applying theory, principles, and data regarding the relationship between humans and respective';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Human Factors Engineers and Ergonomists.", "careers"], ["Skills", "Key skills and requirements for Human Factors Engineers and Ergonomists.", "skills"], ["Education", "Educational pathways for Human Factors Engineers and Ergonomists.", "education"], ["Outlook", "Future trends and outlook for Human Factors Engineers and Ergonomists.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'public-human-factors-engineers-and-ergonomists',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_public_human_factors_engineers_and_ergonomists']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-human-factors-engineers-and-ergonomists',api);
})();
