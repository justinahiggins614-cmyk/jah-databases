/* JAH interactive demo program — jahdb-demo-1.0
 * Database: quantum · Record: JAH-QNT-0000002 · Gate: Pauli-Y
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-QNT-0000002","category":"gates","title":"Gate: Pauli-Y","kind":"quantum-record","gate_name":"Pauli-Y","gate_symbol":"Y","qubits":1,"concept":"Bit+phase flip: maps |0> to i|1>. Hermitian, unitary, traceless like all Paulis.","matrix":"[array ×2]","unitary":true,"source":"online","source_ref":"Nielsen & Chuang; Wikipedia — List of quantum logic gates"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Gate: Pauli-Y ===");
console.log("Record JAH-QNT-0000002 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
