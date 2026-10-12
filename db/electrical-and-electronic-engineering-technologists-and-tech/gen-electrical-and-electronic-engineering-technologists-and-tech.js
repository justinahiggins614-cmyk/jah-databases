(function(){'use strict';
/* Electrical and Electronic Engineering Technologists and Technicians Database generator — jahdb-electrical-and-electronic-engineering-technologists-and-tech-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-EAE-';
var TITLE='Electrical and Electronic Engineering Technologists and Technicians';
var DESC='Apply electrical and electronic theory and related knowledge, usually under the direction of engineering staff, to design, build, repair, adjust, and modify electrical components, circuitry, controls,';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Electrical and Electronic Engineering Technologists and Technicians.", "careers"], ["Skills", "Key skills and requirements for Electrical and Electronic Engineering Technologists and Technicians.", "skills"], ["Education", "Educational pathways for Electrical and Electronic Engineering Technologists and Technicians.", "education"], ["Outlook", "Future trends and outlook for Electrical and Electronic Engineering Technologists and Technicians.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'electrical-and-electronic-engineering-technologists-and-tech',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_electrical_and_electronic_engineering_technologists_and_tech']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('electrical-and-electronic-engineering-technologists-and-tech',api);
})();
