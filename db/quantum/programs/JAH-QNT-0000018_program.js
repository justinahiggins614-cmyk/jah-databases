/* JAH interactive demo program — jahdb-demo-1.0
 * Database: quantum · Record: JAH-QNT-0000018 · Clifford gate HSS
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-QNT-0000018","category":"gates","title":"Clifford gate HSS","kind":"quantum-record","gate_name":"Single-qubit Clifford HSS","gate_symbol":"CL7","qubits":1,"concept":"Element of the 24-element single-qubit Clifford group, expressed as the word HSS in H and S generators (phase-canonical).","matrix":"[array ×2]","unitary":true,"clifford":true,"source":"online","source_ref":"Computed — single-qubit Clifford group"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Clifford gate HSS ===");
console.log("Record JAH-QNT-0000018 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
