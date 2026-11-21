
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var scales=[0.8, 1.0, 1.25];
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var m=pick(r, data.maps);
    var f=pick(r, scales);
    var rooms=m.rooms.map(function(rm){
      var w=Math.round(rm.w*f*10)/10, h=Math.round(rm.h*f*10)/10;
      return rm.label+' '+w+' by '+h+' feet ('+Math.round(w*h*10)/10+' sq ft)';
    });
    var id='JAH-MAPGEN-'+num6(r);
    out.push({id:id, base:m.id, name:m.name, scale:f,
      text:'Generated room-map variation '+id+' (simulated): "'+m.name+'" at scale '+f+' — rooms: '+rooms.join('; ')+'. Varied from archive map '+m.id+'; a variation only, not an archive record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
