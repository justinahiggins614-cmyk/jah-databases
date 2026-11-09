/* JAH interactive demo program — jahdb-demo-1.0
 * Database: meta · Record: JAH-META-0000001 · Opal Immersive Visor Prime
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-META-0000001","title":"Opal Immersive Visor Prime","signature_name":"Opal Immersive Visor Prime","alludes_to":"Meta Quest 3 — mixed-reality headset","class":1,"category":"vr-headsets","specs":{"(object keys)":["soc","ram_gb","storage_gb","display","price_usd"]},"description":"Meta Quest 3 — mixed-reality headset is the nominative anchor for this record. The Opal Immersive Visor Prime carries the same working details — Snapdragon XR2 Gen 2 with 8 GB of RAM, starting at $499…","year":2023};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Opal Immersive Visor Prime ===");
console.log("Record JAH-META-0000001 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
