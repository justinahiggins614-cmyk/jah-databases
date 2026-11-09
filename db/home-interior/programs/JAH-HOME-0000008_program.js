/* JAH interactive demo program — jahdb-demo-1.0
 * Database: home-interior · Record: JAH-HOME-0000008 · Ottoman — Piece profile
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-HOME-0000008","title":"Ottoman — Piece profile","subject":"Ottoman","category":"furniture","record_type":"profile","source":"online","source_ref":"https://www.coohom.com/article/standard-dimensions-for-furniture-design","creation_mode":"ONLINE-CURATED","summary":"Ottoman is a furniture for living, standard: 16–18 in high. Origin: Worldwide, era modern. Footrest matching seat height. Archived in the JAH Home and Interior Database for designers.","facts":{"(object keys)":["j","y","k","a","cite"]},"key_points":"[array ×4]","guidance":"General information only, not professional design advice. Measure your own space before buying."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Ottoman — Piece profile ===");
console.log("Record JAH-HOME-0000008 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
