
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var t=pick(r, data.titles);
    var rel=[]; while(rel.length<2){ var x=pick(r, data.titles); if(x[0]!==t[0] && rel.indexOf(x)===-1) rel.push(x); }
    var id='JAH-SPECGEN-'+num6(r);
    out.push({id:id, title:t[1], category:t[2], related:[rel[0][1], rel[1][1]],
      text:'Generated spec outline '+id+' (simulated): Spec: '+t[1]+'. Category: '+t[2]+'. Sections: 1. What it is. 2. How it is made. 3. Related specs: '+rel[0][1]+'; '+rel[1][1]+'. An outline only, not a spec record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
