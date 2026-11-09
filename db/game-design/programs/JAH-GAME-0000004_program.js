/* JAH interactive demo program — jahdb-demo-1.0
 * Database: game-design · Record: JAH-GAME-0000004 · Signature balance pass: Velvet quest
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"balance","source":"signature","creation_mode":"SIGNATURE-GENERATED","title":"Signature balance pass: Velvet quest","topic":"balance pass","mechanic":{"(object keys)":["pass","target","adjustment"]},"description":"A Signature-generated balance pass named Velvet quest targeting early game with -15% costs. An original tuning sketch by the JAH generator. Filed as a complete searchable record in the JAH Data Bases …","id":"JAH-GAME-0000004"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature balance pass: Velvet quest ===");
console.log("Record JAH-GAME-0000004 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
