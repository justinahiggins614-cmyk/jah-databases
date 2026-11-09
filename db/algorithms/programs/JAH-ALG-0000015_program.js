/* JAH interactive demo program — jahdb-demo-1.0
 * Database: algorithms · Record: JAH-ALG-0000015 · Topological Sort
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ALG-0000015","category":"graphs","title":"Topological Sort","kind":"algorithm","algorithm_name":"Topological Sort","method":"topsort","problem":"Reference entry: Topological Sort, a canonical graphs algorithm.","description":"Orders directed-acyclic-graph nodes so every edge points forward (Kahn’s algorithm). Fails if a cycle exists.","pseudocode":"[array ×1]","complexity_time":"O(V + E)","complexity_space":"O(V)","source":"online","source_ref":"CLRS — graph algorithms"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Topological Sort ===");
console.log("Record JAH-ALG-0000015 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
