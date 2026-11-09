/* JAH interactive demo program — jahdb-demo-1.0
 * Database: anatomy · Record: JAH-ANA-0000012 · frontal bone - clinical notes
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"title":"frontal bone - clinical notes","category":"skeletal","description":"Clinical correlation record for the frontal bone. Fractures are classified by pattern and location; healing proceeds through inflammation, repair, and remodeling phases.","source":"online","source_ref":"https://openstax.org/details/books/anatomy-and-physiology-2e","creation_mode":"ONLINE-VERIFIED","region":"skull","structure_type":"flat bone","latin_name":"","functions":"[array ×1]","related_structures":"[array ×1]","clinical_notes":"Assess neurovascular status with any suspected fracture.","id":"JAH-ANA-0000012"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== frontal bone - clinical notes ===");
console.log("Record JAH-ANA-0000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
