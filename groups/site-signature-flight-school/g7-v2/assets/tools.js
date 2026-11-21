
function flightTime(distanceKm, speedKmh){
  var d=Number(distanceKm), s=Number(speedKmh);
  if(!isFinite(d)||!isFinite(s)) return {error:'Enter numbers for the distance and the speed.'};
  if(d<=0||s<=0) return {error:'Distance and speed must be more than zero.'};
  var hours=d/s;
  return {distance:d, speed:s, hours:Math.round(hours*100)/100, minutes:Math.round(hours*60)};
}
function feetToMeters(feet){
  var f=Number(feet);
  if(!isFinite(f)) return {error:'Enter a number for the feet.'};
  if(f<0) return {error:'Feet cannot be negative.'};
  return {feet:f, meters:Math.round(f*0.3048*100)/100};
}
var AIRCRAFT = ["Skyhopper T-1 Trainer", "Cloudrunner C-2", "Albatross G-1 Glider", "Whirlybird H-4", "Dart Racer R-3", "Comet Cruiser C-9", "Sunseeker A-6 Amphibian", "Thunderbolt J-7", "Sky Giant G-800", "Stormchaser S-5", "Night Owl N-2", "Starhopper X-1 Rocket"];
var PATHS = ["Al Canyon Carve", "Al River Follow", "Be River Follow", "Be Storm Edge Ride", "Cor Island Hop", "Cor River Follow", "Del Sunrise Run", "Del Valley Tour", "El Summit Loop", "El Valley Tour", "Fi Storm Edge Ride", "Fi Summit Loop", "Gar River Follow", "Gar Thunderhead Tour", "Hal Harbor Hop", "Hal Night Lights Tour", "Il Harbor Hop", "Il Valley Tour", "Jor Canyon Carve", "Jor Island Hop", "Kal Island Hop", "Kal Sunrise Run", "Lan Canyon Carve", "Lan Storm Edge Ride", "Mar Harbor Hop", "Mar River Follow", "Nor Summit Loop", "Nor Sunrise Run", "Or Glacier Glide", "Or Harbor Hop", "Pal Storm Edge Ride", "Pal Summit Loop", "Quil Canyon Carve", "Quil Harbor Hop", "Quil Sunrise Run", "Ros Night Lights Tour", "Ros Thunderhead Tour", "Sal Canyon Carve", "Sal Thunderhead Tour", "Tar Canyon Carve", "Tar Island Hop", "Ul Storm Edge Ride", "Ul Sunrise Run", "Val Harbor Hop", "Val Night Lights Tour", "Wil Sunset Cruise", "Wil Thunderhead Tour", "Xan Glacier Glide", "Xan Island Hop", "Xan Sunrise Run", "Yor Summit Loop", "Yor Thunderhead Tour", "Zal Harbor Hop", "Zal Summit Loop", "Zal Valley Tour"];
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var p=PATHS[Math.floor(r()*PATHS.length)];
  return 'Fun: Pippa flew "'+p+'" so high she waved at the sun — and the sun waved back with both rays.';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { flightTime: flightTime, feetToMeters: feetToMeters, makeFun: makeFun };
