/* JAH interactive demo program — jahdb-demo-1.0
 * Database: equations · Record: JAH-EQ-00000011 · Integrate ∫(5x^2 − 9x + 9) dx
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"type":"integral","title":"Integrate ∫(5x^2 − 9x + 9) dx","equation":"∫(5x^2 − 9x + 9) dx = ?","steps":"[array ×6]","solution":"5/3x^3 − 9/2x^2 + 9x + C","check":"Differentiating the answer returns the integrand ✓","id":"JAH-EQ-00000011","n":11,"stamp":"Official JAH Equation Archive — solved once, published officially, retrieved thereafter."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Integrate ∫(5x^2 − 9x + 9) dx ===");
console.log("Record JAH-EQ-00000011 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
