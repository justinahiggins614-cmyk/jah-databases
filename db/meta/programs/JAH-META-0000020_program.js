/* JAH interactive demo program — jahdb-demo-1.0
 * Database: meta · Record: JAH-META-0000020 · Vale Vision Frames Plus
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-META-0000020","title":"Vale Vision Frames Plus","signature_name":"Vale Vision Frames Plus","alludes_to":"Ray-Ban Meta smart glasses (Gen 2) — camera glasses","class":1,"category":"smart-glasses","specs":{"(object keys)":["camera_mp","price_usd","audio","assistant"]},"description":"The Vale Vision Frames Plus is a Signature-original vision frames in the smart glasses family. It tracks the working profile of Ray-Ban Meta smart glasses (Gen 2) — camera glasses: second generation w…","year":2025};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Vale Vision Frames Plus ===");
console.log("Record JAH-META-0000020 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
