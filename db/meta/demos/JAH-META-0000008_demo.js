/* JAH interactive demo program — jahdb-demo-1.0
 * Database: meta · Record: JAH-META-0000008 · Halo Vision Frames S 7
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-META-0000008","title":"Halo Vision Frames S 7","signature_name":"Halo Vision Frames S 7","alludes_to":"Orion — AR glasses prototype","class":1,"category":"smart-glasses","specs":{"(object keys)":["type","display","form","status"]},"description":"Built as the Signature version of Orion — AR glasses prototype, the Halo Vision Frames S 7 reproduces its operational facts in original expression — the first true AR glasses prototype with holographi…","year":2024};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Halo Vision Frames S 7 ===");
console.log("Record JAH-META-0000008 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
