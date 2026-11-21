function hashSeed(s){ var h=2166136261; s=String(s); for(var i=0;i<s.length;i++){ h^=s.charCodeAt(i); h=Math.imul(h,16777619); } return h>>>0; }
function rng(seed){ var a=hashSeed(seed); return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }

function printTime(heightMm, layerMm, secPerLayer){
  var h=Number(heightMm), l=Number(layerMm), s=Number(secPerLayer);
  if(!isFinite(h)||!isFinite(l)||!isFinite(s)) return {error:'Enter numbers for height, layer height, and seconds per layer.'};
  if(h<=0||l<=0||s<=0) return {error:'Height, layer height, and seconds per layer must all be more than zero.'};
  var layers=Math.ceil(h/l);
  var minutes=Math.round((layers*s/60)*10)/10;
  return {heightMm:h, layerMm:l, layers:layers, minutes:minutes};
}
function filamentWeight(lengthM){
  var m=Number(lengthM);
  if(!isFinite(m)) return {error:'Enter a length in metres.'};
  if(m<0) return {error:'Length must be zero or more.'};
  if(m===0) return {lengthM:0, grams:0};
  return {lengthM:m, grams:Math.round(m*3*10)/10};
}
var TITLES = ["3D Benchy", "20mm XYZ Calibration Cube", "Cali Cat", "Temperature Tower", "Retraction Test (Twin Towers)", "Voron 2.4 Printed Parts Set", "Prusa i3 MK3S+ Printed Parts", "StealthBurner Toolhead", "Gridfinity Baseplate System", "E-NABLE Phoenix Prosthetic Hand", "Montana Mask Frame", "Articulated Crystal Dragon", "Lithophane Photo Panel", "Cable Chain (Energy Chain)", "Filament Dry Box", "Parametric Battery Dispenser", "Tool Holder Wall Panel", "Self-Watering Planter", "Cookie Cutter Set", "Phone Stand (Adjustable)", "Headphone Stand", "Drawer Organizer Grid", "SD Card Holder", "Raspberry Pi 4 Case"];
function makeFun(seed){
  var r=rng(String(seed==null?'':seed));
  var t=TITLES[Math.floor(r()*TITLES.length)];
  return 'Fun: Pip printed "'+t+'" so small it floated in a teacup — and the teacup is still sailing.';
}
if (typeof module !== 'undefined' && module.exports) module.exports = { printTime: printTime, filamentWeight: filamentWeight, makeFun: makeFun };
