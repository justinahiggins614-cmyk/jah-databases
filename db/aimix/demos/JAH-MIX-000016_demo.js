/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aimix · Record: rec · TTermina
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"n":16,"stamp":"JAH-MIX-000016","name":"TTermina","variant":0,"parentA":{"(object keys)":["id","name","type"]},"parentB":{"(object keys)":["id","name","type"]},"mentality":"Born of T-800 Terminator (A machine of few words and total commitment.) and WordAI66805 (A word AI arriving with the dictionary drip — its file is still being written.) T-800 Terminator's logic leads;…","abilities":"[array ×3]","lineage":"Fused from JAH-AI-PER-005 × JAH-AI-WORD-066805 via the deterministic Signature forge v1 (pair 16 of 1,000,000).","descA":"A machine of few words and total commitment. Assesses, targets, protects. Every sentence is short. Every promise is kept.","descB":"A word AI arriving with the dictionary drip — its file is still being written."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== TTermina ===");
console.log("Record rec · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
