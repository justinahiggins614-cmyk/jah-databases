(function(){'use strict';
/* Radio Frequency Identification Device Specialists Database generator — jahdb-radio-frequency-identification-device-specialists-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Type 2: Signature-developed original content. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-RFI-';
var TITLE='Radio Frequency Identification Device Specialists';
var DESC='Design and implement radio frequency identification device (RFID) systems used to track shipments or goods.';
var ASPECTS=[["Overview", "Determine and formulate policies and provide overall direction of companies or private and public sector organizations within guidelines set up by a board of directors or similar governing body. Plan,", "general"], ["Career Path", "Career paths and progression in Radio Frequency Identification Device Specialists.", "careers"], ["Skills", "Key skills and requirements for Radio Frequency Identification Device Specialists.", "skills"], ["Education", "Educational pathways for Radio Frequency Identification Device Specialists.", "education"], ["Outlook", "Future trends and outlook for Radio Frequency Identification Device Specialists.", "outlook"]];
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
var api={generate:generate,validate:validate,slug:'radio-frequency-identification-device-specialists',version:'1.0'};
if(typeof module!=='undefined'&&module.exports)module.exports=api;
window['jahdb_radio_frequency_identification_device_specialists']=api;
if(window.JAHDB&&JAHDB.registerGenerator)JAHDB.registerGenerator('radio-frequency-identification-device-specialists',api);
})();
