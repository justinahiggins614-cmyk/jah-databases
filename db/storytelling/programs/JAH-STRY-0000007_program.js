/* JAH interactive demo program — jahdb-demo-1.0
 * Database: storytelling · Record: JAH-STRY-0000007 · Kishōtenketsu: Ten
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"plots","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Kishōtenketsu: Ten","topic":"story structure","structure":{"(object keys)":["framework","stage","order","of","note"]},"source_ref":"Story craft standards (verified 2026-10-09)","description":"The Ten is stage 3 of 4 in the Kishōtenketsu framework. Twist: an unexpected turn reframes everything. Writers use this structure to shape rising tension and earned payoffs.","id":"JAH-STRY-0000007"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Kishōtenketsu: Ten ===");
console.log("Record JAH-STRY-0000007 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
