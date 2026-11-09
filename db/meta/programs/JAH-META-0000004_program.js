/* JAH interactive demo program — jahdb-demo-1.0
 * Database: meta · Record: JAH-META-0000004 · Glade Immersive Visor Plus 2
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-META-0000004","title":"Glade Immersive Visor Plus 2","signature_name":"Glade Immersive Visor Plus 2","alludes_to":"Meta Quest 2 — standalone VR headset","class":1,"category":"vr-headsets","specs":{"(object keys)":["soc","ram_gb","storage_gb"]},"description":"The Glade Immersive Visor Plus 2 is a Signature-original immersive visor in the vr headsets family. It tracks the working profile of Meta Quest 2 — standalone VR headset: the headset that brought stan…","year":2020};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Glade Immersive Visor Plus 2 ===");
console.log("Record JAH-META-0000004 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
