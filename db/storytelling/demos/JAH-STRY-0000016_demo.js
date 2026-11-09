/* JAH interactive demo program — jahdb-demo-1.0
 * Database: storytelling · Record: JAH-STRY-0000016 · Character arc: Negative Change
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"arcs","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Character arc: Negative Change","topic":"character arc","structure":{"(object keys)":["arc","note"]},"source_ref":"Story craft standards (verified 2026-10-09)","description":"A negative change character arc: The hero falls into a worse self. Arcs track inner change against outer events. Filed as a complete searchable record in the JAH Data Bases archive, with its full spec…","id":"JAH-STRY-0000016"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Character arc: Negative Change ===");
console.log("Record JAH-STRY-0000016 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
