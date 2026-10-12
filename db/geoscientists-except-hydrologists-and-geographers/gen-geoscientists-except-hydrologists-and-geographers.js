(function(){'use strict';
/* Geoscientists, Except Hydrologists and Geographers Database generator — jahdb-geoscientists-except-hydrologists-and-geographers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-GEH-';
var TITLE='Geoscientists, Except Hydrologists and Geographers';
var DESC='Study the composition, structure, and other physical aspects of the Earth. May use geological, physics, and mathematics knowledge in exploration for oil, gas, minerals, or underground water; or in was';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Geoscientists, Except Hydrologists and Geographers.", "careers"], ["Skills", "Key skills and requirements for Geoscientists, Except Hydrologists and Geographers.", "skills"], ["Education", "Educational pathways for Geoscientists, Except Hydrologists and Geographers.", "education"], ["Outlook", "Future trends and outlook for Geoscientists, Except Hydrologists and Geographers.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'geoscientists-except-hydrologists-and-geographers',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_geoscientists_except_hydrologists_and_geographers']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('geoscientists-except-hydrologists-and-geographers',api);
})();
