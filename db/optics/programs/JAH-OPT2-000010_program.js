/* JAH interactive demo program — jahdb-demo-1.0
 * Database: optics · Record: JAH-OPT2-000010 · Signature Study — Echelle spectrometer concept (600 l/mm gra…
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-OPT2-000010","title":"Signature Study — Echelle spectrometer concept (600 l/mm grating)","description":"This is a Signature-authored optical design study for a echelle spectrometer at 600 l/mm grating. Design goals address the real aberration profile: Coma: off-axis rays in the collimator smear the spec…","category":"spectrometers","src":"signature","spec":{"(object keys)":["instrument_type","grating_lines_per_mm","focal_length_mm","detector","aberration_notes","correction_note","application"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature Study — Echelle spectrometer concept (600 l/mm grating) ===");
console.log("Record JAH-OPT2-000010 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
