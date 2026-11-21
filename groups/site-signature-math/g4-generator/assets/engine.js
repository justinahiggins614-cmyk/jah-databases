/* Math generator engine: base conversion + triangle area + seeded
   conversion drill from the site's own 32 conversion records. Browser + Node. */
(function(g){
'use strict';
var RECORDS = [{"name": "ASCII Text", "cat": "Text encodings"}, {"name": "Audio Waveform (PCM)", "cat": "Audio"}, {"name": "Barcode (Linear)", "cat": "Visual codes"}, {"name": "Base64", "cat": "Base systems"}, {"name": "BCD (Binary-Coded Decimal)", "cat": "Base systems"}, {"name": "Binary (Base-2)", "cat": "Base systems"}, {"name": "Color Hex (#RRGGBB)", "cat": "Visual codes"}, {"name": "DNA-Style Quaternary", "cat": "Base systems"}, {"name": "Decimal (Base-10)", "cat": "Base systems"}, {"name": "Floating-Point (IEEE 754)", "cat": "Numeric formats"}, {"name": "Geometric Coordinate Sets", "cat": "Geometry"}, {"name": "Gray Code", "cat": "Base systems"}, {"name": "Hash Digest (SHA-256)", "cat": "Cryptography"}, {"name": "Hexadecimal (Base-16)", "cat": "Base systems"}, {"name": "IPv4 Address Form", "cat": "Numeric formats"}, {"name": "IPv6 Address Form", "cat": "Numeric formats"}, {"name": "MIDI Note Map", "cat": "Audio"}, {"name": "Morse Code", "cat": "Text encodings"}, {"name": "Octal (Base-8)", "cat": "Base systems"}, {"name": "Pixel Grid (Raster)", "cat": "Visual codes"}, {"name": "QR-Style Matrix Pattern", "cat": "Visual codes"}, {"name": "Run-Length Encoding (RLE)", "cat": "Compression"}, {"name": "Ternary (Base-3)", "cat": "Base systems"}, {"name": "Unicode (UTF-8)", "cat": "Text encodings"}, {"name": "ASCII-Morse-Binary Chain", "cat": "Mixes"}, {"name": "Binary-Hex Bridge", "cat": "Mixes"}, {"name": "Coordinate-to-Pixel Raster", "cat": "Mixes"}, {"name": "DNA-to-Base64 Capsule", "cat": "Mixes"}, {"name": "Gray-to-Binary Round-Trip", "cat": "Mixes"}, {"name": "Morse-to-Barcode Chain", "cat": "Mixes"}, {"name": "Pixel-to-Color-Hex Mosaic", "cat": "Mixes"}, {"name": "Ternary-to-Octal Packing", "cat": "Mixes"}];
function hashStr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){var a=hashStr(String(seed));return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function toBase(n,base){
  if(typeof n!=='number'||!isFinite(n)||Math.floor(n)!==n) return {error:'Enter a whole number.'};
  if(n<0) return {error:'Enter 0 or more.'};
  if(base!==2&&base!==8&&base!==16) return {error:'Base must be 2, 8 or 16.'};
  return {value:n.toString(base).toUpperCase()};
}
function triangleArea(b,h){
  if(typeof b!=='number'||typeof h!=='number'||!isFinite(b)||!isFinite(h)) return {error:'Enter numbers.'};
  if(b<=0||h<=0) return {error:'Base and height must be more than 0.'};
  return {value:(b*h)/2};
}
function gcd(a,b){
  a=Math.abs(Math.floor(a));b=Math.abs(Math.floor(b));
  if(!isFinite(a)||!isFinite(b)) return {error:'Enter whole numbers.'};
  while(b){var t=b;b=a%b;a=t;}
  return {value:a};
}
function makeDrill(seed){
  var r=rng(seed);var pool=RECORDS.slice();var out=[];
  while(out.length<3&&pool.length){out.push(pool.splice(Math.floor(r()*pool.length),1)[0]);}
  var n=2+Math.floor(r()*90);
  return {seed:String(seed),generated:true,number:n,records:out.map(function(x){return {name:x.name,cat:x.cat};})};
}
var API={RECORDS:RECORDS,toBase:toBase,triangleArea:triangleArea,gcd:gcd,makeDrill:makeDrill,hashStr:hashStr};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigEngine=API;}
if(typeof globalThis!=='undefined'){globalThis.SigEngine=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
