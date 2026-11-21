/* Group 7 tools for Signature Math. Browser + Node. */
(function(g){
'use strict';
function hashStr(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}return h>>>0;}
function rng(seed){var a=hashStr(String(seed));return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
var RECORDS=[{"name": "ASCII Text", "cat": "Text encodings"}, {"name": "Audio Waveform (PCM)", "cat": "Audio"}, {"name": "Barcode (Linear)", "cat": "Visual codes"}, {"name": "Base64", "cat": "Base systems"}, {"name": "BCD (Binary-Coded Decimal)", "cat": "Base systems"}, {"name": "Binary (Base-2)", "cat": "Base systems"}, {"name": "Color Hex (#RRGGBB)", "cat": "Visual codes"}, {"name": "DNA-Style Quaternary", "cat": "Base systems"}, {"name": "Decimal (Base-10)", "cat": "Base systems"}, {"name": "Floating-Point (IEEE 754)", "cat": "Numeric formats"}, {"name": "Geometric Coordinate Sets", "cat": "Geometry"}, {"name": "Gray Code", "cat": "Base systems"}, {"name": "Hash Digest (SHA-256)", "cat": "Cryptography"}, {"name": "Hexadecimal (Base-16)", "cat": "Base systems"}, {"name": "IPv4 Address Form", "cat": "Numeric formats"}, {"name": "IPv6 Address Form", "cat": "Numeric formats"}, {"name": "MIDI Note Map", "cat": "Audio"}, {"name": "Morse Code", "cat": "Text encodings"}, {"name": "Octal (Base-8)", "cat": "Base systems"}, {"name": "Pixel Grid (Raster)", "cat": "Visual codes"}, {"name": "QR-Style Matrix Pattern", "cat": "Visual codes"}, {"name": "Run-Length Encoding (RLE)", "cat": "Compression"}, {"name": "Ternary (Base-3)", "cat": "Base systems"}, {"name": "Unicode (UTF-8)", "cat": "Text encodings"}, {"name": "ASCII-Morse-Binary Chain", "cat": "Mixes"}, {"name": "Binary-Hex Bridge", "cat": "Mixes"}, {"name": "Coordinate-to-Pixel Raster", "cat": "Mixes"}, {"name": "DNA-to-Base64 Capsule", "cat": "Mixes"}, {"name": "Gray-to-Binary Round-Trip", "cat": "Mixes"}, {"name": "Morse-to-Barcode Chain", "cat": "Mixes"}, {"name": "Pixel-to-Color-Hex Mosaic", "cat": "Mixes"}, {"name": "Ternary-to-Octal Packing", "cat": "Mixes"}];
function makeQuiz(seed){
  var r=rng(seed);var x=RECORDS[Math.floor(r()*RECORDS.length)];
  var cats=['Text encodings','Audio','Visual codes','Base systems'];
  var options=[x.cat];
  while(options.length<4){var c=cats[Math.floor(r()*cats.length)];if(options.indexOf(c)===-1)options.push(c);}
  for(var i=options.length-1;i>0;i--){var j=Math.floor(r()*(i+1));var tmp=options[i];options[i]=options[j];options[j]=tmp;}
  return {kind:'fun',name:x.name,question:'Which group does the conversion record "'+x.name+'" belong to?',options:options,answer:x.cat};
}

var API={makeQuiz:makeQuiz};
if(typeof module!=='undefined'){module.exports=API;}
if(typeof window!=='undefined'){window.SigTools=API;}
if(typeof globalThis!=='undefined'){globalThis.SigTools=API;}
})(typeof globalThis!=='undefined'?globalThis:this);
