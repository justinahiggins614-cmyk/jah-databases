/* JAH interactive demo program — jahdb-demo-1.0
 * Database: fashion · Record: JAH-FASH-0000007 · Garment: Bra
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"garments","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Garment: Bra","topic":"garment","garment":{"(object keys)":["garment","class","note"]},"source_ref":"Fashion reference (verified 2026-10-09)","description":"The bra is a intimates garment: A supportive undergarment. A wardrobe staple with established construction conventions. Filed as a complete searchable record in the JAH Data Bases archive, with its fu…","id":"JAH-FASH-0000007"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Garment: Bra ===");
console.log("Record JAH-FASH-0000007 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
