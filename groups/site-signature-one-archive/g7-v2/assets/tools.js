function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }

function specIdCheck(id){
  if(id==null) return {error:'Enter a spec ID, for example JAH-SPEC-000001.'};
  var s=String(id).trim().toUpperCase();
  if(!s) return {error:'Enter a spec ID, for example JAH-SPEC-000001.'};
  var m=/^JAH-SPEC-(\d{6})$/.exec(s);
  if(!m) return {error:'That is not a spec ID. A spec ID looks like JAH-SPEC-000001.'};
  var n=parseInt(m[1], 10);
  if(n<1||n>908995) return {error:'Spec number '+n+' is outside the archive (1 to 908995).'};
  return {id:s, number:n};
}
function specAge(year){
  var y=Number(year);
  if(!isFinite(y)||Math.floor(y)!==y) return {error:'Enter a whole year, for example 1990.'};
  if(y<1800||y>2026) return {error:'Enter a year between 1800 and 2026.'};
  return {year:y, age:2026-y};
}
var TITLES = ["API gateway for batch ETL using WebAssembly sandboxing", "ECG patch for frequency hopping using conformal coating", "Floodlight for LiDAR scanning using micro-bump arrays", "Stream joiner for batch ETL using attention-gated memory", "Solar charge controller for EMI shielding using eutectic die attach", "Paraphrase detector for demand prediction using Merkle-chained logging", "Smart thermostat for short-circuit protection using system-in-package layout", "Face matcher for document summarization using bit-sliced indexing", "Memory management unit for short-circuit protection using dynamic voltage scaling", "Offline-first sync engine for speech transcription using federated gradient compression", "Offline inference runtime for query optimization using Merkle-chained logging", "Defect inspector for data deduplication using delta encoding", "ADAS camera for shock absorption using flip-chip bonding", "OBD dongle for gesture recognition using body biasing", "Op-amp for sensor fusion using capacitive sensing", "Spot instance bidder for log analysis using columnar encoding", "Multipath scheduler for clinical triage using columnar encoding", "Action cam housing for ultrasonic ranging using embedded passives", "Feature store indexer for capacity planning using leaky bucket pacing", "Auto-leveling probe for on-device learning using body biasing", "Check valve for edge inference using underfill encapsulation", "Lint rule engine for data deduplication using event sourcing", "Environmental beacon for surge suppression using spread-spectrum clocking", "Dosing pump for overload protection using underfill encapsulation"];
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var t=TITLES[Math.floor(r()*TITLES.length)];
  return 'Fun: Sammy drafted a spec for "'+t+'" — it was approved, filed, and then used to draft the next spec.';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { specIdCheck: specIdCheck, specAge: specAge, makeFun: makeFun };
