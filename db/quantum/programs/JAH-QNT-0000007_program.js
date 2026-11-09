/* JAH interactive demo program — jahdb-demo-1.0
 * Database: quantum · Record: JAH-QNT-0000007 · Gate: Controlled-NOT
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-QNT-0000007","category":"gates","title":"Gate: Controlled-NOT","kind":"quantum-record","gate_name":"Controlled-NOT","gate_symbol":"CNOT","qubits":2,"concept":"Flips the target iff the control is |1>. Creates entanglement; with single-qubit gates it is universal.","matrix":"[array ×4]","unitary":true,"source":"online","source_ref":"Nielsen & Chuang; Wikipedia — List of quantum logic gates"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Gate: Controlled-NOT ===");
console.log("Record JAH-QNT-0000007 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
