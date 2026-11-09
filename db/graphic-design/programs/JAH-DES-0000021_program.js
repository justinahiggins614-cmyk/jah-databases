/* JAH interactive demo program — jahdb-demo-1.0
 * Database: graphic-design · Record: JAH-DES-0000021 · Signature palette: Ember works
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"color","source":"signature","creation_mode":"SIGNATURE-GENERATED","title":"Signature palette: Ember works","topic":"signature palette","palette":"[array ×4]","spec":{"(object keys)":["name","swatches","swatch_count"]},"description":"A Signature-generated palette named Ember works with 4 swatches: #c0358f, #ad8638, #49982a, #4572c4. It was composed by the JAH generator as an original color study, marked as a Signature creation rat…","id":"JAH-DES-0000021"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature palette: Ember works ===");
console.log("Record JAH-DES-0000021 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
