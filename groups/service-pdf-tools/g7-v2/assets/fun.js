
/* Pip's identical twins — a fun game, labeled fun, never a fact. */
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function makeFun(records, seed){
  var rnd=mulberry32(seed);
  var pool=records.filter(function(r){return r.title.indexOf('Field Guide Index')<0;});
  var a=pool[Math.floor(rnd()*pool.length)], b=pool[Math.floor(rnd()*pool.length)];
  return {seed:seed, kind:'fun',
    text:'Pip says: open "'+a.title+'" on two different computers and compare the pages side by side — then do the same with "'+b.title+'". If every word matches, the twins are identical, as a PDF should be.'};
}
if(typeof module!=='undefined'){module.exports={makeFun:makeFun,mulberry32:mulberry32};}
