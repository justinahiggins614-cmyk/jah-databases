/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cryptography · Record: JAH-CRY-000019 · Signature study: SHA-2 alongside scrypt
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CRY-000019","title":"Signature study: SHA-2 alongside scrypt","description":"2001 — SHA-2: SHA-2 is a family of hash functions with 224, 256, 384, and 512-bit digests, published by the NSA in 2001 as FIPS-180. alongside scrypt (2009), This Signature pairing study examines the …","category":"hash-function","spec":{"(object keys)":["kind","pair","relation","years","src"]},"year":2009,"src":"signature"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature study: SHA-2 alongside scrypt ===");
console.log("Record JAH-CRY-000019 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
