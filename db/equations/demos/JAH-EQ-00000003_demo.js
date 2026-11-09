/* JAH interactive demo program — jahdb-demo-1.0
 * Database: equations · Record: JAH-EQ-00000003 · Solve the system: 1x + 1y = -4; 4x + 6y = -16
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"type":"system2","title":"Solve the system: 1x + 1y = -4; 4x + 6y = -16","equation":"1x + 1y = -4 and 4x + 6y = -16","steps":"[array ×5]","solution":"x = −4, y = 0","check":"1(−4) + 1(0) = -4 ✓","id":"JAH-EQ-00000003","n":3,"stamp":"Official JAH Equation Archive — solved once, published officially, retrieved thereafter."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Solve the system: 1x + 1y = -4; 4x + 6y = -16 ===");
console.log("Record JAH-EQ-00000003 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
