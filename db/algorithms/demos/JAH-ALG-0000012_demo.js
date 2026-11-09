/* JAH interactive demo program — jahdb-demo-1.0
 * Database: algorithms · Record: JAH-ALG-0000012 · Dijkstra’s Algorithm
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ALG-0000012","category":"graphs","title":"Dijkstra’s Algorithm","kind":"algorithm","algorithm_name":"Dijkstra’s Algorithm","method":"dijkstra","problem":"Reference entry: Dijkstra’s Algorithm, a canonical graphs algorithm.","description":"Expands the closest unvisited node first, settling shortest paths from the start. Requires non-negative weights.","pseudocode":"[array ×5]","complexity_time":"O((V + E) log V)","complexity_space":"O(V)","source":"online","source_ref":"CLRS — graph algorithms"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Dijkstra’s Algorithm ===");
console.log("Record JAH-ALG-0000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
