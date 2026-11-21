
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var d=pick(r, data.designs);
    var m=pick(r, data.materials);
    var id='JAH-PRINTGEN-'+num6(r);
    out.push({id:id, design:d[1], group:d[2], material:m,
      text:'Generated print brief '+id+' (simulated): Print "'+d[1]+'" in the manner of the '+d[2]+' group, in '+m+'. Steps: 1. Slice at 0.2 mm layers. 2. Print with 15% infill. 3. Check the first layer, then let it finish. A brief only, not a print record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
