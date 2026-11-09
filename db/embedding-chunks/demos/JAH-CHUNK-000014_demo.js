/* JAH interactive demo program — jahdb-demo-1.0
 * Database: embedding-chunks · Record: JAH-CHUNK-000014 · The Industrial Revolution · JAH History Atlas
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CHUNK-000014","chunk_id":"JAH-CHUNK-000014","text":"The Industrial Revolution began in Britain in the late 1700s. Steam power mechanized spinning, weaving, and transport. Factories drew workers from farms into fast-growing cities. Railways shrank dista…","token_count":68,"source_doc":"JAH History Atlas","section":"The Industrial Revolution","keywords":"[array ×3]","embedding_model":"jah-embed-1.0","domain":"history","title":"The Industrial Revolution · JAH History Atlas"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== The Industrial Revolution · JAH History Atlas ===");
console.log("Record JAH-CHUNK-000014 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
