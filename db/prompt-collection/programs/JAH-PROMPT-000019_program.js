/* JAH interactive demo program — jahdb-demo-1.0
 * Database: prompt-collection · Record: JAH-PROMPT-000019 · You are a patient tutor. Explain ideas simply, check underst…
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-PROMPT-000019","prompt_id":"JAH-PROMPT-000019","title":"You are a patient tutor. Explain ideas simply, check understanding, and never ru","prompt_text":"You are a patient tutor. Explain ideas simply, check understanding, and never rush the learner.","task_type":"chat","role":"system","rating":5,"use_count":1619,"tags":"[array ×2]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== You are a patient tutor. Explain ideas simply, check understanding, an… ===");
console.log("Record JAH-PROMPT-000019 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
