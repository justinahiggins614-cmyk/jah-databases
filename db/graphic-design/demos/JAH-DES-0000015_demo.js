/* JAH interactive demo program — jahdb-demo-1.0
 * Database: graphic-design · Record: JAH-DES-0000015 · Signature type pairing: Garamond + Roboto
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"typography","source":"signature","creation_mode":"SIGNATURE-GENERATED","title":"Signature type pairing: Garamond + Roboto","topic":"type pairing","spec":{"(object keys)":["pairing","headline_size","body_size","line_height"]},"description":"A Signature-generated type pairing, Garamond + Roboto, set with 62px headlines and 15px body copy at 1.5 line height. An original pairing study by the JAH generator.","id":"JAH-DES-0000015"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature type pairing: Garamond + Roboto ===");
console.log("Record JAH-DES-0000015 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
