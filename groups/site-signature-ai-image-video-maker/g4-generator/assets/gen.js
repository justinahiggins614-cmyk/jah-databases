
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var g=pick(r, data.goods), c1=pick(r, data.palette), c2=pick(r, data.palette);
    var id='JAH-PIXGEN-'+num6(r);
    out.push({id:id, title:g[1], kind:g[2], c1:c1, c2:c2,
      text:'Generated product design '+id+' (simulated): A '+g[2]+' in the manner of "'+g[1]+'". Colours: '+c1+' and '+c2+'. Print: two-colour print on the '+g[2]+', colours as named. A design only, not a catalog record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
