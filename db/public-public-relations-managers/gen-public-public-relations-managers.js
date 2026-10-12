(function(){'use strict';
/* Public Public Relations Managers Database generator — jahdb-public-public-relations-managers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 1: Public information database. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-PRM-';
var TITLE='Public Relations Managers';
var DESC='Plan, direct, or coordinate activities designed to create or maintain a favorable public image or raise issue awareness for their organization or client.';
var ASPECTS=[["Overview", "Plan, direct, or coordinate activities designed to create or maintain a favorable public image or raise issue awareness for their organization or client.", "general"], ["Career Path", "Career paths and progression in Public Relations Managers.", "careers"], ["Skills", "Key skills and requirements for Public Relations Managers.", "skills"], ["Education", "Educational pathways for Public Relations Managers.", "education"], ["Outlook", "Future trends and outlook for Public Relations Managers.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'public-public-relations-managers',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_public_public_relations_managers']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-public-relations-managers',api);
})();
