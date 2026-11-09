/* JAH interactive demo program — jahdb-demo-1.0
 * Database: meta · Record: JAH-META-0000006 · Ion Vision Frames Prime
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-META-0000006","title":"Ion Vision Frames Prime","signature_name":"Ion Vision Frames Prime","alludes_to":"Ray-Ban Meta smart glasses (Gen 2) — camera glasses","class":1,"category":"smart-glasses","specs":{"(object keys)":["camera_mp","price_usd","audio","assistant"]},"description":"The Ion Vision Frames Prime is a Signature-original vision frames in the smart glasses family. It tracks the working profile of Ray-Ban Meta smart glasses (Gen 2) — camera glasses: second generation w…","year":2025};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Ion Vision Frames Prime ===");
console.log("Record JAH-META-0000006 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
