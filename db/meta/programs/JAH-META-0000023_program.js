/* JAH interactive demo program — jahdb-demo-1.0
 * Database: meta · Record: JAH-META-0000023 · Forge Cognitive Engine Prime
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-META-0000023","title":"Forge Cognitive Engine Prime","signature_name":"Forge Cognitive Engine Prime","alludes_to":"Llama 3.1 405B — open-weight language model","class":1,"category":"ai-models","specs":{"(object keys)":["params_b","license","context_k"]},"description":"The Forge Cognitive Engine Prime is a Signature-original cognitive engine in the ai models family. It tracks the working profile of Llama 3.1 405B — open-weight language model: 405 billion parameters …","year":2024};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Forge Cognitive Engine Prime ===");
console.log("Record JAH-META-0000023 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
