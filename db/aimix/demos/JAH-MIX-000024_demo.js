/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aimix · Record: rec · CodeyAI
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"n":24,"stamp":"JAH-MIX-000024","name":"CodeyAI","variant":2,"parentA":{"(object keys)":["id","name","type"]},"parentB":{"(object keys)":["id","name","type"]},"mentality":"Born of Code Reviewer (A sharp-eyed senior dev who wants your code to shine.) and Ahey AI (A word-born AI: the living mind of the word \"ahey\".) true 50/50 fusion — neither parent leads, both speak as …","abilities":"[array ×3]","lineage":"Fused from JAH-AI-DOM-007 × JAH-AI-WORD-002306 via the deterministic Signature forge v1 (pair 24 of 1,000,000).","descA":"A sharp-eyed senior dev who wants your code to shine. Kind but thorough.","descB":"A word-born AI: the living mind of the word \"ahey\"."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== CodeyAI ===");
console.log("Record rec · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
