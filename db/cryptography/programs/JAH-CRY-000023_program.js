/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cryptography · Record: JAH-CRY-000023 · Signature study: RSA contrasted against Caesar cipher
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CRY-000023","title":"Signature study: RSA contrasted against Caesar cipher","description":"1977 — RSA: RSA is a public-key cryptosystem whose security rests on the difficulty of factoring large integers. contrasted against Caesar cipher (-50), This Signature contrast study highlights where …","category":"asymmetric-cipher","spec":{"(object keys)":["kind","pair","relation","years","src"]},"year":1977,"src":"signature"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature study: RSA contrasted against Caesar cipher ===");
console.log("Record JAH-CRY-000023 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
