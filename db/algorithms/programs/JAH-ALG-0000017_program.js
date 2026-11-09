/* JAH interactive demo program — jahdb-demo-1.0
 * Database: algorithms · Record: JAH-ALG-0000017 · 0/1 Knapsack
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ALG-0000017","category":"dynamic-programming","title":"0/1 Knapsack","kind":"algorithm","algorithm_name":"0/1 Knapsack","method":"knapsack01","problem":"Reference entry: 0/1 Knapsack, a canonical dynamic-programming algorithm.","description":"Each item is taken or skipped. DP over capacity: dp[c] = best value achievable with capacity c.","pseudocode":"[array ×4]","complexity_time":"O(n * W)","complexity_space":"O(W)","source":"online","source_ref":"CLRS — dynamic programming"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== 0/1 Knapsack ===");
console.log("Record JAH-ALG-0000017 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
