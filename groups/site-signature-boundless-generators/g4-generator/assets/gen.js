
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var fam=pick(r, data.families);
    var pool=data.records.filter(function(x){ return x.facet===fam; });
    var src=pick(r, pool.length?pool:data.records);
    var id='JAH-GENGEN-'+num6(r);
    out.push({id:id, family:fam, pattern:src.id, title:src.title,
      text:'Generated generator record '+id+' (simulated): "'+src.title+'" again, in the '+fam+' family — in the manner of '+src.id+'. Description: '+src.desc+' A generated record only, not an archive record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
