
function freeFallTime(height){
  var h=Number(height);
  if(!isFinite(h)) return {error:'Enter a number for the height in metres.'};
  if(h<=0) return {error:'Height must be more than zero.'};
  return {height:h, seconds:Math.round(Math.sqrt(2*h/9.8)*100)/100};
}
function pendulumPeriod(length){
  var l=Number(length);
  if(!isFinite(l)) return {error:'Enter a number for the length in metres.'};
  if(l<=0) return {error:'Length must be more than zero.'};
  return {length:l, seconds:Math.round(2*Math.PI*Math.sqrt(l/9.8)*100)/100};
}
var TITLES = ["Free-Fall Gravity Drop \u2014 steel ball at 10 m", "Pendulum Period vs Length \u2014 brass bob at 1 m", "Projectile Launch Angle \u2014 foam dart at 20 m/s"];
function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var t=TITLES[Math.floor(r()*TITLES.length)];
  return 'Fun: Ernie bubbled happily through "'+t+'" — and the pendulum kept the beat.';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { freeFallTime: freeFallTime, pendulumPeriod: pendulumPeriod, makeFun: makeFun };
