(function(){'use strict';
/* Architectural and Civil Drafters Database generator — jahdb-architectural-and-civil-drafters-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-AAC-';
var TITLE='Architectural and Civil Drafters';
var DESC='Prepare detailed drawings of architectural and structural features of buildings or drawings and topographical relief maps used in civil engineering projects, such as highways, bridges, and public work';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Architectural and Civil Drafters.", "careers"], ["Skills", "Key skills and requirements for Architectural and Civil Drafters.", "skills"], ["Education", "Educational pathways for Architectural and Civil Drafters.", "education"], ["Outlook", "Future trends and outlook for Architectural and Civil Drafters.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'architectural-and-civil-drafters',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_architectural_and_civil_drafters']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('architectural-and-civil-drafters',api);
})();
