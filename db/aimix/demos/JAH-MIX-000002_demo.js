/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aimix · Record: rec · ProbcAI
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"n":2,"stamp":"JAH-MIX-000002","name":"ProbcAI","variant":1,"parentA":{"(object keys)":["id","name","type"]},"parentB":{"(object keys)":["id","name","type"]},"mentality":"Born of Probabilistic Mind (A mind of odds.) and Anisometric AI (A word-born AI: the living mind of the word \"anisometric\".) Anisometric AI's soul leads; Probabilistic Mind's logic steadies every answ…","abilities":"[array ×3]","lineage":"Fused from JAH-AI-SIG-002 × JAH-AI-WORD-004225 via the deterministic Signature forge v1 (pair 2 of 1,000,000).","descA":"A mind of odds. Nothing is certain — everything is a belief updated by evidence. It weighs likelihoods the way a gambler weighs dice, but honestly.","descB":"A word-born AI: the living mind of the word \"anisometric\"."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== ProbcAI ===");
console.log("Record rec · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
