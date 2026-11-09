/* JAH interactive demo program — jahdb-demo-1.0
 * Database: equations · Record: JAH-EQ-00000008 · Evaluate (3 − 11) × 12
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"type":"evaluate","title":"Evaluate (3 − 11) × 12","equation":"(3 − 11) × 12 = ?","steps":"[array ×3]","solution":"(3 − 11) × 12 = −96","check":"Order of operations: parentheses first ✓","id":"JAH-EQ-00000008","n":8,"stamp":"Official JAH Equation Archive — solved once, published officially, retrieved thereafter."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Evaluate (3 − 11) × 12 ===");
console.log("Record JAH-EQ-00000008 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
