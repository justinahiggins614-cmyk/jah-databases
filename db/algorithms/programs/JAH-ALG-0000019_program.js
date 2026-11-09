/* JAH interactive demo program — jahdb-demo-1.0
 * Database: algorithms · Record: JAH-ALG-0000019 · Edit Distance
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ALG-0000019","category":"dynamic-programming","title":"Edit Distance","kind":"algorithm","algorithm_name":"Edit Distance","method":"edit-distance","problem":"Reference entry: Edit Distance, a canonical dynamic-programming algorithm.","description":"Minimum insertions, deletions, substitutions to turn one string into another (Levenshtein DP).","pseudocode":"[array ×1]","complexity_time":"O(n * m)","complexity_space":"O(n * m)","source":"online","source_ref":"CLRS — dynamic programming"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Edit Distance ===");
console.log("Record JAH-ALG-0000019 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
