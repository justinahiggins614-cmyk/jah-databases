
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var t=pick(r, data.titles), c=pick(r, data.cpcs), asg=pick(r, data.assignees);
    var first=t.split(/\s+/)[0];
    var yr=1988+Math.floor(r()*38);
    var id='JAH-PATGEN-'+num6(r);
    out.push({id:id, title:first+' device for '+c[1], cpc:c[0], assignee:asg, year:yr,
      text:'Generated invention sketch '+id+' (simulated): "'+first+' device for '+c[1]+'" — class '+c[0]+' ('+c[1]+'), in the manner of work held by '+asg+', dated '+yr+'. A sketch only, not a patent record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
