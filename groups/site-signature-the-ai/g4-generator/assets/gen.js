
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function pick(r, arr){ return arr[Math.floor(r()*arr.length)]; }
function num6(r){ return String(100000 + Math.floor(r()*900000)); }

var NAME_A = ['Ember', 'Signal', 'Lantern', 'Harbor', 'Cinder', 'Juniper', 'Marble', 'North', 'Peregrine', 'Quill', 'Ridgeline', 'Solace', 'Tidewater', 'Umber', 'Vesper', 'Willow'];
var NAME_B = ['Mind', 'Sage', 'Guide', 'Beacon', 'Atlas', 'Compass', 'Herald', 'Warden', 'Scribe', 'Pilot', 'Sentinel', 'Weaver', 'Oracle', 'Steward', 'Ranger', 'Clerk'];
var NAME_C = ['Mix', 'Build', 'Forge', 'Blend', 'Assembly', 'Edition', 'Compound', 'Fusion'];
var PROFILES = ['optimal', 'standard', 'maximal', 'minimal'];
function makeOutputs(seed, n, data){
  if(!(n>=1)) n=1; if(n>5) n=5;
  var out=[];
  for(var k=0;k<n;k++){
    var r=rng(seed+':'+k);
    var name=pick(r, NAME_A)+' '+pick(r, NAME_B)+' '+pick(r, NAME_C);
    var prof=pick(r, PROFILES);
    var libs=[]; while(libs.length<3){ var x=pick(r, data.libs); if(libs.indexOf(x)===-1) libs.push(x); }
    var id='JAH-LLAMAGEN-'+num6(r);
    out.push({id:id, name:name, profile:prof, libraries:libs,
      text:'Generated tool-set build '+id+' (simulated): "'+name+'", profile '+prof+'. Libraries: '+libs.join(', ')+'. A build only, not a filed record.'});
  }
  return out;
}
if (typeof module !== 'undefined' && module.exports) module.exports = { makeOutputs: makeOutputs, hashSeed: hashSeed };
