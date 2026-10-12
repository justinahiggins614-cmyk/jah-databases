(function(){'use strict';
/* Public Biofuels/Biodiesel Technology and Product Development Managers Database generator — jahdb-public-biofuels-biodiesel-technology-and-product-development-manage-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 1: Public information database. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-BTA-';
var TITLE='Biofuels/Biodiesel Technology and Product Development Managers';
var DESC='Define, plan, or execute biofuels/biodiesel research programs that evaluate alternative feedstock and process technologies with near-term commercial potential.';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Biofuels/Biodiesel Technology and Product Development Managers.", "careers"], ["Skills", "Key skills and requirements for Biofuels/Biodiesel Technology and Product Development Managers.", "skills"], ["Education", "Educational pathways for Biofuels/Biodiesel Technology and Product Development Managers.", "education"], ["Outlook", "Future trends and outlook for Biofuels/Biodiesel Technology and Product Development Managers.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'public-biofuels-biodiesel-technology-and-product-development-manage',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_public_biofuels_biodiesel_technology_and_product_development_manage']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-biofuels-biodiesel-technology-and-product-development-manage',api);
})();
