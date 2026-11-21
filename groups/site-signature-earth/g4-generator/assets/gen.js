
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var stops=[], used={};
    while(stops.length<3){
      var p=pick(r, data.places);
      if(!used[p[0]]){ used[p[0]]=1; stops.push(p); }
    }
    var id='JAH-TOURGEN-'+num6(r);
    var legs=stops.map(function(p,i){ return (i+1)+'. '+p[1]+', '+p[4]+' ('+p[2]+', '+p[3]+')'; }).join(' | ');
    out.push({id:id, stops:stops.map(function(p){ return p[0]; }),
      text:'Generated place tour '+id+' (simulated): '+legs+'. Three real archive addresses, in tour order.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
