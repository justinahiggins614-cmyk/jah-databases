/* Group 7 tools for The Signature Spell Check. Browser + Node. */
(function(g){
'use strict';
function hashStr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){var a=hashStr(String(seed));return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
var WORDS=["a", "a-good", "a-mornings", "a-sea", "a-tiptoe", "aam", "aard-vark", "aard-wolf", "aaronic", "aaronical", "ab", "abaca", "abacinate", "abacination", "abaciscus", "abacist", "aback", "abactinal", "abaction", "abactor", "abaculus", "abacus", "abada", "abaddon", "abaft", "abaisance", "abaiser", "abaist", "abalienate", "abalienation", "abalone", "aband", "abandon", "abandoned", "abandonedly", "abandonee", "abandoner", "abandonment", "abandum", "abanet", "abanga", "abannation", "abannition", "abarticulation", "abase", "abased", "abasedly", "abasement", "abaser", "abash", "abashedly", "abashment", "abasia", "abassi", "abassis", "abatable", "abate", "abatement", "abater", "abatis", "abatised", "abator", "abattis", "abattoir", "abature", "abatvoix", "abawed", "abaxial", "abaxile", "abay", "abb", "abba", "abbacy", "abbatial", "abbatical", "abbe", "abbess", "abbey", "abbot", "abbotship", "abbreviate", "abbreviated", "abbreviation", "abbreviator", "abbreviatory", "abbreviature", "abdal", "abderian", "abderite", "abdest", "abdicable", "abdicant", "abdicate", "abdication", "abdicative", "abdicator", "abditive", "abditory", "abdomen", "abdominal", "abdominales", "abdominalia", "abdominoscopy", "abdominothoracic", "abdominous", "abduce", "abduct", "abduction", "abductor", "abeam", "abear", "abearance", "abearing", "abecedarian", "abecedary", "abed", "abegge", "abele", "abelian", "abelite", "abelmosk", "abelonian", "aber-de-vine", "aberr", "aberrance", "aberrancy", "aberrant", "aberrate", "aberration", "aberrational", "aberuncate", "aberuncator", "abet", "abetment", "abettal", "abetter", "abettor", "abevacuation", "abeyance", "abeyancy", "abeyant", "abgeordnetenhaus", "abhal", "abhominable", "abhominal", "abhor", "abhorrence", "abhorrency", "abhorrent", "abhorrently", "abhorrer", "abhorrible", "abhorring", "abib", "abidance", "abide", "abider", "abiding", "abidingly", "abies", "abietene", "abietic", "abietin", "abietine", "abietinic", "abietite", "abigail", "abiliment", "ability", "abime", "abiogenesis", "abiogenetic", "abiogenist", "abiogenous", "abiogeny", "abiological", "abirritant", "abirritate", "abirritation", "abirritative", "abit", "abject", "abjectedness", "abjection", "abjectly", "abjectness", "abjudge", "abjudicate", "abjudication", "abjugate", "abjunctive", "abjuration", "abjuratory", "abjure", "abjurement", "abjurer", "ablactate", "ablactation", "ablaqueate", "ablaqueation"];
function makeQuiz(seed){
  var r=rng(seed);var w=WORDS[Math.floor(r()*WORDS.length)];
  var pos=1+Math.floor(r()*(w.length-2));
  var shown=w.slice(0,pos)+'_'+w.slice(pos+1);
  var letters='abcdefghijklmnopqrstuvwxyz'.split('');
  var options=[w[pos]];
  while(options.length<4){var L=letters[Math.floor(r()*letters.length)];if(options.indexOf(L)===-1)options.push(L);}
  for(var i=options.length-1;i>0;i--){var j=Math.floor(r()*(i+1));var tmp=options[i];options[i]=options[j];options[j]=tmp;}
  return {kind:'fun',word:w,question:'Fill the missing letter: "'+shown+'". Which letter goes in the gap?',options:options,answer:w[pos]};
}

var API={makeQuiz:makeQuiz};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigTools=API;}
if(typeof globalThis!=='undefined'){globalThis.SigTools=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
