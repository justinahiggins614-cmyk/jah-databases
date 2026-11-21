
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var tools=[], used={};
    while(tools.length<3){
      var t=pick(r, data.tools);
      if(!used[t.id]){ used[t.id]=1; tools.push(t); }
    }
    var term=pick(r, data.terms);
    var id='JAH-PACKGEN-'+num6(r);
    out.push({id:id, tools:tools.map(function(t){ return t.name; }), term:term.t,
      text:'Generated tool pack '+id+' (simulated): '+tools.map(function(t){ return t.name+' ('+t.cat+')'; }).join(', ')+' — plus the term "'+term.t+'" ('+term.c+'). A pack for one small job: run the three tools on the term, in order.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
