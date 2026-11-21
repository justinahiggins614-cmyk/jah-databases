
/* Sample-document generator core. Deterministic: same seed -> same document.
   The title is a real record title; the lines are the first sentences of
   real record descriptions. The PDF itself is built by the PDF engine. */
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function makeDocument(records, seed){
  var rnd=mulberry32(seed);
  var pool=records.filter(function(r){return r.title.indexOf('Field Guide Index')<0;});
  var order=pool.slice();
  for(var i=order.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1));var t=order[i];order[i]=order[j];order[j]=t;}
  var title=order[0].title;
  var lines=order.slice(0,4).map(function(r){
    var s=(r.description||'').split(/(?<=[.!?])\s/)[0]||'';
    return s.slice(0,90);
  });
  return {seed:seed, kind:'sample document', title:title, lines:lines, recordIds:order.slice(0,4).map(function(r){return r.id;})};
}
if(typeof module!=='undefined'){module.exports={makeDocument:makeDocument,mulberry32:mulberry32};}
