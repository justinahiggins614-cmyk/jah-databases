/* JAH interactive demo program — jahdb-demo-1.0
 * Database: optics · Record: JAH-OPT2-000005 · Signature Study — Mach-Zehnder interferometer concept (1064 …
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-OPT2-000005","title":"Signature Study — Mach-Zehnder interferometer concept (1064 nm laser)","description":"This is a Signature-authored optical design study for a Mach-Zehnder interferometer at 1064 nm laser. Design goals address the real aberration profile: Astigmatism: uneven curvature that splits the in…","category":"interferometers","src":"signature","spec":{"(object keys)":["instrument_type","laser_wavelength_nm","arm_length_m","beamsplitter","aberration_notes","correction_note","application"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature Study — Mach-Zehnder interferometer concept (1064 nm laser) ===");
console.log("Record JAH-OPT2-000005 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
