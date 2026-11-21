
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function buildName(r, pools){
  function catWord(cat){ return cat.split(' ')[0].replace('&', '').trim(); }
  var ci=Math.floor(r()*pools.cats.length), si=Math.floor(r()*pools.styles.length);
  var ai=Math.floor(r()*pools.adj.length), ni=Math.floor(r()*pools.noun.length), pi=Math.floor(r()*pools.palettes.length);
  return {name: pools.adj[ai]+' '+catWord(pools.cats[ci])+' '+pools.noun[ni], cat: pools.cats[ci], style: pools.styles[si], palette: pools.palettes[pi]};
}
function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var b=buildName(r, data.pools);
    var id='JAH-WEBGEN-'+num6(r);
    out.push({id:id, name:b.name, cat:b.cat, style:b.style, palette:b.palette,
      text:'Generated build concept '+id+' (simulated): "'+b.name+'" — a '+b.style.toLowerCase()+' '+b.cat.toLowerCase()+' website build. Palette: '+b.palette.join(', ')+'. Hero, intro, tab bar, archive and contact page included. A concept only, not a filed record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
