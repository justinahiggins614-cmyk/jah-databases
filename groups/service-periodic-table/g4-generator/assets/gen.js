
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function seededShuffle(arr,rnd){var a=arr.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}

/* Element quiz generator: seeded, deterministic. Same seed -> same quiz.
   Questions come from all 118 elements in the table data. */
function makeQuiz(elements, seed, count){
  var rnd=mulberry32(seed);
  var picked=seededShuffle(elements,rnd).slice(0,Math.min(count,elements.length));
  var items=picked.map(function(el,i){
    var kind=i%4, q, correct, pool;
    if(kind===0){q='What is the symbol of '+el.name+'?';correct=el.symbol;
      pool=seededShuffle(elements.filter(function(e){return e.symbol!==el.symbol;}),rnd).map(function(e){return e.symbol;});}
    else if(kind===1){q='Which element has the symbol '+el.symbol+'?';correct=el.name;
      pool=seededShuffle(elements.filter(function(e){return e.name!==el.name;}),rnd).map(function(e){return e.name;});}
    else if(kind===2){q='What is the atomic number of '+el.name+'?';correct=String(el.z);
      pool=seededShuffle(elements.filter(function(e){return e.z!==el.z;}),rnd).map(function(e){return String(e.z);});}
    else{q='Which element has atomic number '+el.z+'?';correct=el.name;
      pool=seededShuffle(elements.filter(function(e){return e.name!==el.name;}),rnd).map(function(e){return e.name;});}
    var choices=seededShuffle([correct].concat(pool.filter(function(v,ix,arr){return v!==correct&&arr.indexOf(v)===ix;}).slice(0,3)),rnd);
    return {n:i+1, question:q, choices:choices, answer:correct};
  });
  return {seed:seed, count:items.length, items:items};
}
if(typeof module!=='undefined'){module.exports={makeQuiz:makeQuiz,mulberry32:mulberry32,seededShuffle:seededShuffle};}
