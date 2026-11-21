
/* Sammy's lucky numbers — a fun game, labeled fun, never a fact. */
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function makeFun(records, seed){
  var rnd=mulberry32(seed);
  var nums=[1+Math.floor(rnd()*30),1+Math.floor(rnd()*30),1+Math.floor(rnd()*30)];
  var pool=records.filter(function(r){return r.title.indexOf('Field Guide Index')<0;});
  var rule=pool[Math.floor(rnd()*pool.length)];
  return {seed:seed, kind:'fun',
    text:'Sammy says: your lucky numbers today are '+nums.join(', ')+'. Add them up — the total is '+(nums[0]+nums[1]+nums[2])+' — and the rule of the day is "'+rule.title+'".'};
}
if(typeof module!=='undefined'){module.exports={makeFun:makeFun,mulberry32:mulberry32};}
