/* JAH interactive demo program — jahdb-demo-1.0
 * Database: chemistry · Record: JAH-CHEM-0000017 · Carbon electron configuration
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"title":"Carbon electron configuration","category":"physical","description":"Aufbau-predicted electron configuration of Carbon (Z=6): 1s2 2s2 2p2. Predicted by filling order; a few elements differ in their ground state.","concept":"electron configuration","statement":"Aufbau-predicted configuration of C (Z=6): 1s2 2s2 2p2.","source":"online","source_ref":"https://iupac.org/","creation_mode":"ONLINE-VERIFIED","id":"JAH-CHEM-0000017"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Carbon electron configuration ===");
console.log("Record JAH-CHEM-0000017 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
