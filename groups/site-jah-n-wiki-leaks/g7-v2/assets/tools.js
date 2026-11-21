
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function decodeClassification(cls){
  if(!cls||typeof cls!=='string') return {error:'Enter a classification line, for example TOP SECRET // JAH-N // STELLAR // NOFORN.'};
  var parts=cls.split('//').map(function(p){ return p.trim(); }).filter(Boolean);
  if(parts.length<2) return {error:'A classification line has parts joined by //.'};
  return {level:parts[0], system:parts[1]||'', code:parts[2]||'', caveat:parts[3]||'', parts:parts};
}
function makeDossierCode(seed, category){
  var cat=String(category==null?'':category);
  var letters=cat.replace(/[^A-Za-z]/g,'').slice(0,4).toUpperCase() || 'FILE';
  var r=rng(String(seed==null?'':seed)+':'+cat);
  return 'JAH-LEAKGEN-'+letters+'-'+String(1000+Math.floor(r()*9000));
}
var SUBJECTS = ["UFOs (Unidentified Flying Objects)", "Flying Saucers", "Area 51", "The Roswell Incident (1947)", "Alien Abductions", "Crop Circles", "Men in Black", "The Wow! Signal (1977)", "Dyson Spheres", "Wormholes", "Warp Drive", "Anti-Gravity", "Foo Fighters (WWII)", "Plasma Orbs", "Tic Tac UFO (2004 Nimitz)", "Bigfoot / Sasquatch", "The Loch Ness Monster", "Chupacabra", "Mothman", "The Kraken", "Yeti (Abominable Snowman)", "Jersey Devil", "Thunderbird", "Mongolian Death Worm"];
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var s=SUBJECTS[Math.floor(r()*SUBJECTS.length)];
  return 'Fun: Lenny filed "'+s+'" under "L" for lantern-light reading — and the lantern agreed.';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { decodeClassification: decodeClassification, makeDossierCode: makeDossierCode, makeFun: makeFun };
