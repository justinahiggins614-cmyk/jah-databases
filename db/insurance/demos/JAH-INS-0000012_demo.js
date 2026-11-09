/* JAH interactive demo program — jahdb-demo-1.0
 * Database: insurance · Record: JAH-INS-0000012 · Filing a health insurance claim
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-INS-0000012","title":"Filing a health insurance claim","category":"claims-process","record_kind":"insurance entry","origin":"sourced","summary":"Most claims file automatically; appeals have deadlines — calendar them.","details":{"(object keys)":["key_points"]},"sections":"[array ×2]","record_text":"Key points.\nFiling a health insurance claim. Most claims file automatically; appeals have deadlines — calendar them.\n\nIn depth.\nProviders usually bill insurers directly. Review every Explanation of Be…","source_note":"Sourced: standard insurance knowledge; educational only, not financial advice.","related":"[array ×0]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Filing a health insurance claim ===");
console.log("Record JAH-INS-0000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
