/* JAH interactive demo program — jahdb-demo-1.0
 * Database: photography · Record: JAH-PHO-000018 · Pentax K-3 Mark III — overview
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-PHO-000018","title":"Pentax K-3 Mark III — overview","category":"camera","record_kind":"photography entry","summary":"Pentax K-3 Mark III (Pentax, 2021): An optical-viewfinder flagship. Keep practicing deliberately; the craft rewards steady work.","details":{"(object keys)":["model","maker","year","type","mount","note","aspect","angle"]},"provenance":"sourced","source":"JAH Photography curated dataset v1 — real cameras, lenses, techniques, and film stocks from public photographic knowledge."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Pentax K-3 Mark III — overview ===");
console.log("Record JAH-PHO-000018 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
