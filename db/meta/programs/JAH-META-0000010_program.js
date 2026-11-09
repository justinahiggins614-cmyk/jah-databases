/* JAH interactive demo program — jahdb-demo-1.0
 * Database: meta · Record: JAH-META-0000010 · Harbor Cognitive Engine One
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-META-0000010","title":"Harbor Cognitive Engine One","signature_name":"Harbor Cognitive Engine One","alludes_to":"Llama 3.2 — multimodal language model family","class":1,"category":"ai-models","specs":{"(object keys)":["sizes","multimodal","license","context_k"]},"description":"Llama 3.2 — multimodal language model family is the nominative anchor for this record. The Harbor Cognitive Engine One carries the same working details — adds vision understanding to the open model fa…","year":2024};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Harbor Cognitive Engine One ===");
console.log("Record JAH-META-0000010 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
