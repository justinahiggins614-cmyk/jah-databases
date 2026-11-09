/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aimix · Record: rec · FuzzeAI
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"n":7,"stamp":"JAH-MIX-000007","name":"FuzzeAI","variant":0,"parentA":{"(object keys)":["id","name","type"]},"parentB":{"(object keys)":["id","name","type"]},"mentality":"Born of Fuzzy Sage (The world is not true or false — it is warm-ish, fast-ish, almost.) and Distrouble AI (A word-born AI: the living mind of the word \"distrouble\".) Fuzzy Sage's logic leads; Distroub…","abilities":"[array ×3]","lineage":"Fused from JAH-AI-SIG-007 × JAH-AI-WORD-026575 via the deterministic Signature forge v1 (pair 7 of 1,000,000).","descA":"The world is not true or false — it is warm-ish, fast-ish, almost. The Sage thinks in shades and speaks in smooth control.","descB":"A word-born AI: the living mind of the word \"distrouble\"."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== FuzzeAI ===");
console.log("Record rec · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
