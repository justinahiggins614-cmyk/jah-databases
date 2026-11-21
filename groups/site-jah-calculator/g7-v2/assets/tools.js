/* Group 7 tools for Signature Universal Paradox Immune Calculator. Browser + Node. */
(function(g){
'use strict';
function hashStr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){var a=hashStr(String(seed));return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function makeQuiz(seed){
  var r=rng(seed);var a=2+Math.floor(r()*8);var x=1+Math.floor(r()*9);var b=-(a*x);
  var options=[x];
  while(options.length<4){var o=1+Math.floor(r()*12);if(options.indexOf(o)===-1)options.push(o);}
  for(var i=options.length-1;i>0;i--){var j=Math.floor(r()*(i+1));var tmp=options[i];options[i]=options[j];options[j]=tmp;}
  return {kind:'fun',equation:a+'x + '+b+' = 0',question:'Solve '+a+'x + '+b+' = 0. What is x?',options:options,answer:x};
}

var API={makeQuiz:makeQuiz};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigTools=API;}
if(typeof globalThis!=='undefined'){globalThis.SigTools=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
