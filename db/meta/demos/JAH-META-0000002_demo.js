/* JAH interactive demo program — jahdb-demo-1.0
 * Database: meta · Record: JAH-META-0000002 · Umber Immersive Visor Plus 6
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-META-0000002","title":"Umber Immersive Visor Plus 6","signature_name":"Umber Immersive Visor Plus 6","alludes_to":"Meta Quest 3S — entry mixed-reality headset","class":1,"category":"vr-headsets","specs":{"(object keys)":["storage_gb","price_usd","display","tracking"]},"description":"Meta Quest 3S — entry mixed-reality headset is the nominative anchor for this record. The Umber Immersive Visor Plus 6 carries the same working details — the affordable on-ramp to the Quest mixed-real…","year":2024};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Umber Immersive Visor Plus 6 ===");
console.log("Record JAH-META-0000002 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
