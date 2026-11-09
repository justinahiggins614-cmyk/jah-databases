/* JAH interactive demo program — jahdb-demo-1.0
 * Database: insurance · Record: JAH-INS-0000025 · Comprehensive coverage
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-INS-0000025","title":"Comprehensive coverage","category":"insurance-type","record_kind":"insurance entry","origin":"sourced","summary":"Pays for non-collision damage: theft, hail, flood, fire, falling objects, animal strikes.","details":{"(object keys)":["key_points"]},"sections":"[array ×2]","record_text":"Key points.\nComprehensive coverage. Pays for non-collision damage: theft, hail, flood, fire, falling objects, animal strikes.\n\nIn depth.\nComprehensive handles the “acts of nature and mischief” side of…","source_note":"Sourced: standard insurance knowledge; educational only, not financial advice.","related":"[array ×0]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Comprehensive coverage ===");
console.log("Record JAH-INS-0000025 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
