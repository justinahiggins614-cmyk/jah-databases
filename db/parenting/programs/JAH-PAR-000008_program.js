/* JAH interactive demo program — jahdb-demo-1.0
 * Database: parenting · Record: JAH-PAR-000008 · Preschooler — overview
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-PAR-000008","title":"Preschooler — overview","category":"development-stage","record_kind":"parenting guide","summary":"Developmental stage Preschooler (3-4 years). Preschooler (3-4 years): Pedals a tricycle; speaks clearly in sentences; plays cooperatively with others. Every child develops at their own pace; milestone…","details":{"(object keys)":["stage","ages","milestones","aspect"]},"provenance":"sourced","source":"JAH Parenting curated dataset v1 — standard developmental milestones, established methods, and widely shared family guidance. General information only."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Preschooler — overview ===");
console.log("Record JAH-PAR-000008 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
