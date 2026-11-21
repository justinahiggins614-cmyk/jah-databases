
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var keys=['C major','G major','D major','A major','E major','F major','A minor','E minor','D minor','C minor'];
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var s=pick(r, data.songs);
    var tempo=Math.max(40, Math.min(220, Number(s.tempo)+Math.floor(r()*21)-10));
    var key=pick(r, keys);
    var id='JAH-SONGGEN-'+num6(r);
    out.push({id:id, base:s.id, title:s.title, genre:s.genre, mood:s.mood, tempo:tempo, key:key, chords:s.chords,
      text:'Generated song sketch '+id+' (simulated): "'+s.title+' (variation)" — a '+s.mood+' '+s.genre+' song at '+tempo+' BPM in '+key+', chords '+s.chords+'. Sketched from archive song '+s.id+'; a sketch only, not an archive record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
