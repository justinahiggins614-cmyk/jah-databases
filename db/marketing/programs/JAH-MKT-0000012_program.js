/* JAH interactive demo program — jahdb-demo-1.0
 * Database: marketing · Record: JAH-MKT-0000012 · Niche Marketing — Overview
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"record_type":"framework-overview","title":"Niche Marketing — Overview","summary":"Concentrating all effort on a narrow, well-defined market slice.","body":"Concentrating all effort on a narrow, well-defined market slice. Classic small-business strategy.\n\nApproaches commonly used alongside it include Targeting Strategies, Differentiation, Long Tail.","id":"JAH-MKT-0000012","slug":"marketing","record_kind":"marketing record","category":"segments","source":"online","source_ref":"American Marketing Association","fact_key":"niche","creation_mode":"CURATED"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Niche Marketing — Overview ===");
console.log("Record JAH-MKT-0000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
