
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function seededShuffle(arr,rnd){var a=arr.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}

/* Conversion worksheet generator: seeded, deterministic. Same seed -> same
   worksheet. Values and units are drawn from the real unit ratios. */
function makeWorksheet(units, seed, count){
  var rnd=mulberry32(seed);
  var cats=Object.keys(units).sort();
  var items=[];
  for(var k=0;k<count;k++){
    var cat=cats[Math.floor(rnd()*cats.length)];
    var names=Object.keys(units[cat].units);
    var from=names[Math.floor(rnd()*names.length)];
    var to=names[Math.floor(rnd()*names.length)];
    if(to===from) to=names[(names.indexOf(from)+1)%names.length];
    var value=Math.round((1+rnd()*999)*100)/100;
    var answer=Math.round(value*units[cat].units[from]/units[cat].units[to]*1000000)/1000000;
    items.push({n:k+1, category:cat, value:value, from:from, to:to, answer:answer});
  }
  return {seed:seed, count:items.length, items:items};
}
if(typeof module!=='undefined'){module.exports={makeWorksheet:makeWorksheet,mulberry32:mulberry32,seededShuffle:seededShuffle};}
