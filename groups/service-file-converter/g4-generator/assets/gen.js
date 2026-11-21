
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function seededShuffle(arr,rnd){var a=arr.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}

/* Conversion plan generator: seeded, deterministic. Same seed -> same plans.
   Plans come from the 10 documented format conversions. */
function makePlans(formats, seed, count){
  var rnd=mulberry32(seed);
  var picked=seededShuffle(formats,rnd).slice(0,Math.min(count,formats.length));
  var plans=picked.map(function(f,i){
    return {n:i+1, from:f.from, to:f.to, rule:f.rule,
      check:'Fidelity check: convert the result back (or compare it with the original) and confirm nothing needed was lost.'};
  });
  return {seed:seed, count:plans.length, plans:plans};
}
if(typeof module!=='undefined'){module.exports={makePlans:makePlans,mulberry32:mulberry32,seededShuffle:seededShuffle};}
