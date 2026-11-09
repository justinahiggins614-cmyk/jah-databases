/* JAH interactive demo program — jahdb-demo-1.0
 * Database: optics · Record: JAH-OPT2-000018 · Portrait lens — 200 mm f/1.8
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-OPT2-000018","title":"Portrait lens — 200 mm f/1.8","description":"The portrait lens is a camera lens specified here at 200 mm f/1.8. Distortion: straight lines render curved — barrel or pincushion. Coma: point highlights smear into teardrop shapes at wide apertures.…","category":"camera-lenses","src":"online","spec":{"(object keys)":["instrument_type","focal_length_mm","max_aperture","mount","aberration_notes","correction_note","application"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Portrait lens — 200 mm f/1.8 ===");
console.log("Record JAH-OPT2-000018 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
