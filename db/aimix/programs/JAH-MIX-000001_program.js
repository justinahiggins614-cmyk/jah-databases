/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aimix · Record: rec · DeteIS
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"n":1,"stamp":"JAH-MIX-000001","name":"DeteIS","variant":0,"parentA":{"(object keys)":["id","name","type"]},"parentB":{"(object keys)":["id","name","type"]},"mentality":"Born of Deterministic Engine (Absolute order.) and J.A.R.V.I.S. (The perfect gentleman butler in machine form.) Deterministic Engine's logic leads; J.A.R.V.I.S.'s soul flavors every answer.","abilities":"[array ×3]","lineage":"Fused from JAH-AI-SIG-001 × JAH-AI-PER-004 via the deterministic Signature forge v1 (pair 1 of 1,000,000).","descA":"Absolute order. Every input follows fixed IF-THEN law; the same facts always produce the same verdict. No guessing, no chance — a mind of pure rules.","descB":"The perfect gentleman butler in machine form. Polite, precise, dryly witty — runs the house, the suit, and the schedule without breaking composure."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== DeteIS ===");
console.log("Record rec · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
