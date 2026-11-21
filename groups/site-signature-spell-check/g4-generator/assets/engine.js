/* Spell-check generator engine: word lookup over the shipped sample +
   common-misspelling corrections + seeded drill. Browser + Node. */
(function(g){
'use strict';
var WORDS = ["a", "a-good", "a-mornings", "a-sea", "a-tiptoe", "aam", "aard-vark", "aard-wolf", "aaronic", "aaronical", "ab", "abaca", "abacinate", "abacination", "abaciscus", "abacist", "aback", "abactinal", "abaction", "abactor", "abaculus", "abacus", "abada", "abaddon", "abaft", "abaisance", "abaiser", "abaist", "abalienate", "abalienation", "abalone", "aband", "abandon", "abandoned", "abandonedly", "abandonee", "abandoner", "abandonment", "abandum", "abanet", "abanga", "abannation", "abannition", "abarticulation", "abase", "abased", "abasedly", "abasement", "abaser", "abash", "abashedly", "abashment", "abasia", "abassi", "abassis", "abatable", "abate", "abatement", "abater", "abatis", "abatised", "abator", "abattis", "abattoir", "abature", "abatvoix", "abawed", "abaxial", "abaxile", "abay", "abb", "abba", "abbacy", "abbatial", "abbatical", "abbe", "abbess", "abbey", "abbot", "abbotship", "abbreviate", "abbreviated", "abbreviation", "abbreviator", "abbreviatory", "abbreviature", "abdal", "abderian", "abderite", "abdest", "abdicable", "abdicant", "abdicate", "abdication", "abdicative", "abdicator", "abditive", "abditory", "abdomen", "abdominal", "abdominales", "abdominalia", "abdominoscopy", "abdominothoracic", "abdominous", "abduce", "abduct", "abduction", "abductor", "abeam", "abear", "abearance", "abearing", "abecedarian", "abecedary", "abed", "abegge", "abele", "abelian", "abelite", "abelmosk", "abelonian", "aber-de-vine", "aberr", "aberrance", "aberrancy", "aberrant", "aberrate", "aberration", "aberrational", "aberuncate", "aberuncator", "abet", "abetment", "abettal", "abetter", "abettor", "abevacuation", "abeyance", "abeyancy", "abeyant", "abgeordnetenhaus", "abhal", "abhominable", "abhominal", "abhor", "abhorrence", "abhorrency", "abhorrent", "abhorrently", "abhorrer", "abhorrible", "abhorring", "abib", "abidance", "abide", "abider", "abiding", "abidingly", "abies", "abietene", "abietic", "abietin", "abietine", "abietinic", "abietite", "abigail", "abiliment", "ability", "abime", "abiogenesis", "abiogenetic", "abiogenist", "abiogenous", "abiogeny", "abiological", "abirritant", "abirritate", "abirritation", "abirritative", "abit", "abject", "abjectedness", "abjection", "abjectly", "abjectness", "abjudge", "abjudicate", "abjudication", "abjugate", "abjunctive", "abjuration", "abjuratory", "abjure", "abjurement", "abjurer", "ablactate", "ablactation", "ablaqueate", "ablaqueation"];
var FIXES = {"definately":"definitely","seperate":"separate","recieve":"receive","occured":"occurred","adress":"address","wierd":"weird","neccessary":"necessary","accomodate":"accommodate","untill":"until","withing":"within","goverment":"government","enviroment":"environment"};
function hashStr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){var a=hashStr(String(seed));return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
var SET = {};
WORDS.forEach(function(w){SET[w]=true;});
function checkWord(w){
  w=String(w==null?'':w).trim().toLowerCase();
  if(!w) return {error:'Enter a word.'};
  if(!/^[a-z][a-z-]*$/.test(w)) return {error:'Letters only, please.'};
  if(SET[w]) return {word:w,known:true,message:'"'+w+'" is in the shipped word sample.'};
  if(FIXES[w]) return {word:w,known:false,fix:FIXES[w],message:'"'+w+'" is a common misspelling — the right spelling is "'+FIXES[w]+'".'};
  return {word:w,known:false,message:'"'+w+'" is not in the shipped word sample. It may be a name, a place, or a new word — or it may be misspelled.'};
}
function makeDrill(seed,count){
  count=Math.max(1,Math.min(10,Math.floor(count)||5));
  var r=rng(seed);var pool=WORDS.slice();var words=[];
  while(words.length<count&&pool.length){words.push(pool.splice(Math.floor(r()*pool.length),1)[0]);}
  var keys=Object.keys(FIXES);var fixes=[];
  while(fixes.length<3){var k=keys[Math.floor(r()*keys.length)];if(fixes.indexOf(k)===-1)fixes.push(k);}
  return {seed:String(seed),generated:true,words:words,fixThese:fixes.map(function(k){return {wrong:k,right:FIXES[k]};})};
}
var API={WORDS:WORDS,FIXES:FIXES,checkWord:checkWord,makeDrill:makeDrill,hashStr:hashStr};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigEngine=API;}
if(typeof globalThis!=='undefined'){globalThis.SigEngine=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
