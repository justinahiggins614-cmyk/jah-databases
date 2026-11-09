/* JAH interactive demo program — jahdb-demo-1.0
 * Database: optics · Record: JAH-OPT2-000012 · Confocal microscope — 600x 60x
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-OPT2-000012","title":"Confocal microscope — 600x 60x","description":"The confocal microscope is a microscope specified here at 600x 60x. Axial chromatic aberration: colors focus at different depths in the specimen. Field curvature: the focal surface curves instead of l…","category":"microscopes","src":"online","spec":{"(object keys)":["instrument_type","objective","eyepiece","total_magnification","illumination","aberration_notes","correction_note","application"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Confocal microscope — 600x 60x ===");
console.log("Record JAH-OPT2-000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
