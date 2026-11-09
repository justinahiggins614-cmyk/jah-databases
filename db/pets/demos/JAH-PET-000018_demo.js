/* JAH interactive demo program — jahdb-demo-1.0
 * Database: pets · Record: JAH-PET-000018 · Chihuahua — overview
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-PET-000018","title":"Chihuahua — overview","category":"dog-breed","record_kind":"pet care entry","summary":"Chihuahua (Mexico, tiny, short or long coat): The smallest dog breed in the world.","details":{"(object keys)":["breed","origin","aspect","size","coat","temperament","note"]},"provenance":"sourced","source":"JAH Pet Care curated dataset v1 — real breeds and species; origin, size, coat, and temperament from public breed knowledge; spot-checked 2026-10-09."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Chihuahua — overview ===");
console.log("Record JAH-PET-000018 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
