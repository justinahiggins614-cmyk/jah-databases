/* JAH interactive demo program — jahdb-demo-1.0
 * Database: agriculture · Record: JAH-AG-0000001 · Rice — Crop profile
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-AG-0000001","title":"Rice — Crop profile","subject":"Rice","category":"crops","record_type":"profile","source":"online","source_ref":"https://www.flyriver.com/g/crop-specific-requirements","creation_mode":"ONLINE-CURATED","summary":"Rice is a crop of Asia, grown in kharif/monsoon. Key requirements: 15–27°C; 100–150 cm rain; clayey loam. Staple grain of tropical regions needing heat and abundant water. Field: cereal.","facts":{"(object keys)":["j","y","k","a","cite"]},"key_points":"[array ×4]","guidance":"General information only, not professional agronomic advice. Conditions vary by locale; verify with local extension data."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Rice — Crop profile ===");
console.log("Record JAH-AG-0000001 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
