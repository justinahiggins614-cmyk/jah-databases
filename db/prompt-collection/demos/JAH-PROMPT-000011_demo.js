/* JAH interactive demo program — jahdb-demo-1.0
 * Database: prompt-collection · Record: JAH-PROMPT-000011 · List the pros and cons of meal planning, then tell me which …
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-PROMPT-000011","prompt_id":"JAH-PROMPT-000011","title":"List the pros and cons of meal planning, then tell me which side is stronger and","prompt_text":"List the pros and cons of meal planning, then tell me which side is stronger and why.","task_type":"analysis","role":"user","rating":4.8,"use_count":2695,"tags":"[array ×2]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== List the pros and cons of meal planning, then tell me which side is st… ===");
console.log("Record JAH-PROMPT-000011 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
