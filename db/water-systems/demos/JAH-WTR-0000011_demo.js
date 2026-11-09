/* JAH interactive demo program — jahdb-demo-1.0
 * Database: water-systems · Record: JAH-WTR-0000011 · Aqueducts
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-WTR-0000011","title":"Aqueducts","category":"infrastructure","record_kind":"water entry","origin":"sourced","summary":"Channels carrying water across distance by gravity.","details":{"(object keys)":["key_points"]},"sections":"[array ×2]","record_text":"Key points.\nAqueducts. Channels carrying water across distance by gravity.\n\nIn depth.\nRoman aqueducts used precise gradients to move water for miles; modern aqueducts like California’s State Water Pro…","source_note":"Sourced: standard hydrology and water-engineering knowledge.","related":"[array ×0]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Aqueducts ===");
console.log("Record JAH-WTR-0000011 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
