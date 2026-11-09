/* JAH interactive demo program — jahdb-demo-1.0
 * Database: prompt-collection · Record: JAH-PROMPT-000013 · You are a skeptic. Stress-test each claim and flag what the …
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-PROMPT-000013","prompt_id":"JAH-PROMPT-000013","title":"You are a skeptic. Stress-test each claim and flag what the data cannot prove.","prompt_text":"You are a skeptic. Stress-test each claim and flag what the data cannot prove.","task_type":"analysis","role":"system","rating":3.6,"use_count":43,"tags":"[array ×2]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== You are a skeptic. Stress-test each claim and flag what the data canno… ===");
console.log("Record JAH-PROMPT-000013 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
