(function(){'use strict';
/* Cartographers and Photogrammetrists Database generator — jahdb-cartographers-and-photogrammetrists-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-CAP-';
var TITLE='Cartographers and Photogrammetrists';
var DESC='Research, study, and prepare maps and other spatial data in digital or graphic form for one or more purposes, such as legal, social, political, educational, and design purposes. May work with Geograph';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Cartographers and Photogrammetrists.", "careers"], ["Skills", "Key skills and requirements for Cartographers and Photogrammetrists.", "skills"], ["Education", "Educational pathways for Cartographers and Photogrammetrists.", "education"], ["Outlook", "Future trends and outlook for Cartographers and Photogrammetrists.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'cartographers-and-photogrammetrists',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_cartographers_and_photogrammetrists']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('cartographers-and-photogrammetrists',api);
})();
