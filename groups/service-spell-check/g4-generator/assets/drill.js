
/* Spelling-drill generator core. Deterministic: same seed -> same drill.
   Words come from the archive headword sample (assets/sample-words.json).
   Corruptions are rule-based misspellings, each one edit away from the answer. */
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function corrupt(w,rnd){
  var ops=[];
  ops.push(function(x){var i=1+Math.floor(rnd()*(x.length-1));return x.slice(0,i)+x.slice(i+1);}); /* drop a letter */
  ops.push(function(x){var i=1+Math.floor(rnd()*(x.length-2));return x.slice(0,i)+x[i+1]+x[i]+x.slice(i+2);}); /* swap neighbours */
  if(/([a-z])\1/.test(w)) ops.push(function(x){return x.replace(/([a-z])\1/, '$1');}); /* undouble */
  else ops.push(function(x){var i=1+Math.floor(rnd()*(x.length-1));return x.slice(0,i)+x[i]+x.slice(i);}); /* double a letter */
  if(w.indexOf('ie')>=0) ops.push(function(x){return x.replace('ie','ei');});
  else if(w.indexOf('ei')>=0) ops.push(function(x){return x.replace('ei','ie');});
  else ops.push(function(x){var i=1+Math.floor(rnd()*(x.length-1));return x.slice(0,i)+x.slice(i+1);});
  var out=ops[Math.floor(rnd()*ops.length)](w);
  return out===w?w.slice(0,1)+w.slice(2):out;
}
function makeDrill(words, seed, count, misspellRate, headwords){
  /* headwords (optional Set of all archive headwords): a corrupted form that
     is itself a real headword (e.g. pacificable -> pacifiable, need -> nee)
     would be a correctly-spelled word, not a mistake — retry until the
     corruption is not a headword; if none is found, leave the word right. */
  var rnd=mulberry32(seed);
  var pool=words.slice();
  for(var i=pool.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1));var t=pool[i];pool[i]=pool[j];pool[j]=t;}
  var items=[], n=Math.min(count, pool.length);
  for(var k=0;k<n;k++){
    var ans=pool[k], miss=rnd()<misspellRate, given=ans;
    if(miss){
      var ok=false;
      for(var a=0;a<10&&!ok;a++){
        var g=corrupt(ans,rnd);
        if(g!==ans && (!headwords || !headwords.has(g))){ given=g; ok=true; }
      }
      if(!ok){ miss=false; given=ans; }
    }
    items.push({n:k+1, given:given, answer:ans, misspelled:miss});
  }
  return {seed:seed, count:n, items:items};
}
if(typeof module!=='undefined'){module.exports={makeDrill:makeDrill,corrupt:corrupt,mulberry32:mulberry32};}
