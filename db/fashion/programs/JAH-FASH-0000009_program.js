/* JAH interactive demo program — jahdb-demo-1.0
 * Database: fashion · Record: JAH-FASH-0000009 · Signature garment concept: Crimson house
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"garments","source":"signature","creation_mode":"SIGNATURE-GENERATED","title":"Signature garment concept: Crimson house","topic":"garment concept","garment":{"(object keys)":["concept","silhouette","fabric"]},"description":"A Signature-generated garment concept named Crimson house with a draped silhouette in muslin. An original design sketch by the JAH generator. Filed as a complete searchable record in the JAH Data Base…","id":"JAH-FASH-0000009"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature garment concept: Crimson house ===");
console.log("Record JAH-FASH-0000009 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
