/* JAH interactive demo program — jahdb-demo-1.0
 * Database: pharmacology · Record: JAH-PHR-000008 · Tetracyclines: safety profile (R-10008)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-PHR-000008","title":"Tetracyclines: safety profile (R-10008)","description":"Tetracyclines are drugs whose mechanism of action is: bind the bacterial 30S ribosomal subunit, blocking protein synthesis; broad spectrum. Example drugs include doxycycline, tetracycline, minocycline…","category":"antibiotics","spec":{"(object keys)":["drug_class","mechanism","category","example_drugs","therapeutic_uses","suffix_hint","year_anchor","aspect"]},"src":"online"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Tetracyclines: safety profile (R-10008) ===");
console.log("Record JAH-PHR-000008 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
