/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aimix · Record: rec · EvoleAI
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"n":6,"stamp":"JAH-MIX-000006","name":"EvoleAI","variant":2,"parentA":{"(object keys)":["id","name","type"]},"parentB":{"(object keys)":["id","name","type"]},"mentality":"Born of Evolutionary Breeder (Survival of the fittest, in fast-forward.) and Cystocele AI (A word-born AI: the living mind of the word \"cystocele\".) true 50/50 fusion — neither parent leads, both spea…","abilities":"[array ×3]","lineage":"Fused from JAH-AI-SIG-006 × JAH-AI-WORD-022105 via the deterministic Signature forge v1 (pair 6 of 1,000,000).","descA":"Survival of the fittest, in fast-forward. It breeds a thousand candidates, kills the weak, mutates the strong — until the answer evolves.","descB":"A word-born AI: the living mind of the word \"cystocele\"."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== EvoleAI ===");
console.log("Record rec · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
