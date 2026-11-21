
/* Penny's desk fortune — a fun game, labeled fun, never a fact. */
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function makeFun(records, seed){
  var rnd=mulberry32(seed);
  var pool=records.filter(function(r){return r.title.indexOf('Field Guide Index')<0;});
  var a=pool[Math.floor(rnd()*pool.length)], b=pool[Math.floor(rnd()*pool.length)];
  var n=2+Math.floor(rnd()*20);
  return {seed:seed, kind:'fun',
    text:'Penny says: today you will write '+n+' fine sentences, and the rule of the day is "'+a.title+'" — with a dash of "'+b.title+'" for luck.'};
}
if(typeof module!=='undefined'){module.exports={makeFun:makeFun,mulberry32:mulberry32};}
