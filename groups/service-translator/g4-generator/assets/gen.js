
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function seededShuffle(arr,rnd){var a=arr.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}

/* Phrase quiz generator: seeded, deterministic. Same seed -> same quiz.
   Phrases and translations come from the checked phrasebook (80 phrases). */
function makeQuiz(phrases, seed, count, lang){
  var rnd=mulberry32(seed);
  var keys=Object.keys(phrases).sort();
  var picked=seededShuffle(keys,rnd).slice(0,Math.min(count,keys.length));
  var items=picked.map(function(eng,i){
    var correct=phrases[eng][lang];
    var others=seededShuffle(keys.filter(function(k){return k!==eng;}),rnd)
      .map(function(k){return phrases[k][lang];})
      .filter(function(v,ix,arr){return v!==correct&&arr.indexOf(v)===ix;}).slice(0,3);
    var choices=seededShuffle([correct].concat(others),rnd);
    return {n:i+1, english:eng, lang:lang, choices:choices, answer:correct};
  });
  return {seed:seed, lang:lang, count:items.length, items:items};
}
if(typeof module!=='undefined'){module.exports={makeQuiz:makeQuiz,mulberry32:mulberry32,seededShuffle:seededShuffle};}
