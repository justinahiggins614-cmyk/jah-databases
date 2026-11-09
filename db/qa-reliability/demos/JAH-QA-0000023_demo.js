/* JAH interactive demo program — jahdb-demo-1.0
 * Database: qa-reliability · Record: JAH-QA-0000023 · Defect Density — Overview
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"record_type":"framework-overview","title":"Defect Density — Overview","summary":"Defects per thousand lines of code (or function point) — the standard quality-density measure.","body":"Defects per thousand lines of code (or function point) — the standard quality-density measure. Standard software quality metric.\n\nApproaches commonly used alongside it include Code Quality, DPMO, Stat…","id":"JAH-QA-0000023","slug":"qa-reliability","record_kind":"quality record","category":"defects","source":"online","source_ref":"ASQ","fact_key":"defdensity","creation_mode":"CURATED"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Defect Density — Overview ===");
console.log("Record JAH-QA-0000023 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
