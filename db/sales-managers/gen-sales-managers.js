(function(){'use strict';
/* Sales Managers Database generator — jahdb-sales-managers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-SM-';
var TITLE='Sales Managers';
var DESC='Plan, direct, or coordinate the actual distribution or movement of a product or service to the customer. Coordinate sales distribution by establishing sales territories, quotas, and goals and establis';
var ASPECTS=[["Overview", "Plan, direct, or coordinate the actual distribution or movement of a product or service to the customer. Coordinate sales distribution by establishing sales territories, quotas, and goals and establis", "general"], ["Career Path", "Career paths and progression in Sales Managers.", "careers"], ["Skills", "Key skills and requirements for Sales Managers.", "skills"], ["Education", "Educational pathways for Sales Managers.", "education"], ["Outlook", "Future trends and outlook for Sales Managers.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'sales-managers',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_sales_managers']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('sales-managers',api);
})();
