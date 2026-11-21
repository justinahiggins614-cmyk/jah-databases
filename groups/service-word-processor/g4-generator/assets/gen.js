
/* Document-plan generator core. Deterministic: same seed -> same plan.
   Sections are real record titles from the pair; prompts are the first
   sentences of those records' descriptions. Nothing is invented. */
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function makePlan(records, seed, count){
  var rnd=mulberry32(seed);
  var pool=records.filter(function(r){return r.title.indexOf('Field Guide Index')<0;});
  var order=pool.slice();
  for(var i=order.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1));var t=order[i];order[i]=order[j];order[j]=t;}
  var n=Math.min(count||5, order.length);
  var sections=[];
  for(var k=0;k<n;k++){
    var r=order[k];
    var prompt=(r.description||'').split(/(?<=[.!?])\s/)[0]||r.description||'';
    sections.push({n:k+1, heading:r.title, id:r.id, prompt:prompt});
  }
  return {seed:seed, kind:'document plan', wordTarget:100+Math.floor(rnd()*400), sections:sections};
}
if(typeof module!=='undefined'){module.exports={makePlan:makePlan,mulberry32:mulberry32};}
