/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aimix · Record: rec · Hybr
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"n":11,"stamp":"JAH-MIX-000011","name":"Hybr","variant":1,"parentA":{"(object keys)":["id","name","type"]},"parentB":{"(object keys)":["id","name","type"]},"mentality":"Born of Hybrid Fusion Core (All ten minds, one verdict.) and WordAI44455 (A word AI arriving with the dictionary drip — its file is still being written.) WordAI44455's soul leads; Hybrid Fusion Core's…","abilities":"[array ×3]","lineage":"Fused from JAH-AI-SIG-011 × JAH-AI-WORD-044455 via the deterministic Signature forge v1 (pair 11 of 1,000,000).","descA":"All ten minds, one verdict. It asks the rule-keeper, the gambler, and the sage — then fuses their answers into something none could say alone.","descB":"A word AI arriving with the dictionary drip — its file is still being written."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Hybr ===");
console.log("Record rec · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
