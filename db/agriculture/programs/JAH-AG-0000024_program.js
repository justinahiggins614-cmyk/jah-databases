/* JAH interactive demo program — jahdb-demo-1.0
 * Database: agriculture · Record: JAH-AG-0000024 · Cocoa — Crop profile
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-AG-0000024","title":"Cocoa — Crop profile","subject":"Cocoa","category":"crops","record_type":"profile","source":"online","source_ref":"https://www.flyriver.com/g/crop-specific-requirements","creation_mode":"ONLINE-CURATED","summary":"Cocoa is a crop of Tropics, grown in year-round. Key requirements: Hot, humid; shade; rich soil. Understory tree yielding chocolate. Field: beverage.","facts":{"(object keys)":["j","y","k","a","cite"]},"key_points":"[array ×4]","guidance":"General information only, not professional agronomic advice. Conditions vary by locale; verify with local extension data."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Cocoa — Crop profile ===");
console.log("Record JAH-AG-0000024 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
