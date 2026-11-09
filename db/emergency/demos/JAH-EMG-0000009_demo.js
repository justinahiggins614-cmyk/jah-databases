/* JAH interactive demo program — jahdb-demo-1.0
 * Database: emergency · Record: JAH-EMG-0000009 · Family emergency communication plan
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-EMG-0000009","title":"Family emergency communication plan","category":"preparedness","record_kind":"emergency protocol","origin":"sourced","summary":"An out-of-area contact everyone calls; a meeting place; practiced by all.","details":{"(object keys)":["key_points"]},"sections":"[array ×2]","record_text":"Key points.\nFamily emergency communication plan. An out-of-area contact everyone calls; a meeting place; practiced by all.\n\nProcedure.\nChoose: pick an out-of-area contact every family member calls. Me…","source_note":"Sourced: standard public-safety guidance; get certified hands-on training for medical procedures.","related":"[array ×0]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Family emergency communication plan ===");
console.log("Record JAH-EMG-0000009 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
