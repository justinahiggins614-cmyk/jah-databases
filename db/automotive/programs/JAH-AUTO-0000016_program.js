/* JAH interactive demo program — jahdb-demo-1.0
 * Database: automotive · Record: JAH-AUTO-0000016 · VW Beetle Type 1 — Dimensions & Specs
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"auto_id":"JAH-AUTO-0000016","category":"engines","vehicle_or_system":"VW Beetle Type 1","specifications":{"(object keys)":["years","built","engine"]},"source":"online","source_ref":{"(object keys)":["authority","url"]},"title":"VW Beetle Type 1 — Dimensions & Specs","record_type":"dimensions","description":"Specification for VW Beetle Type 1: flat-4. Per history. 1938-2003; 21.5 million built; air-cooled rear engine. Standards: history.","standards":"[array ×1]","id":"JAH-AUTO-0000016"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== VW Beetle Type 1 — Dimensions & Specs ===");
console.log("Record JAH-AUTO-0000016 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
