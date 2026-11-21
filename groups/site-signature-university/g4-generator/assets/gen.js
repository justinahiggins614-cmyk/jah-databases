
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var c=pick(r, data.courses);
    var col=pick(r, data.colleges);
    var id='JAH-COURSEGEN-'+num6(r);
    out.push({id:id, course:c[1], title:c[2], college:c[3], level:c[4], extra:col,
      text:'Generated course plan '+id+' (simulated): Course: '+c[1]+' — '+c[2]+' ('+c[3]+', level '+c[4]+'). Plan: 1. Read the course title aloud. 2. Study one real course from the same college. 3. Cross-read: '+col+'. A plan only, not a course record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
