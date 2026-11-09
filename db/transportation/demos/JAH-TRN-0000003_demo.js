/* JAH interactive demo program — jahdb-demo-1.0
 * Database: transportation · Record: JAH-TRN-0000003 · Fact card: Shanghai Metro (urban-transit)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-TRN-0000003","record_id":"JAH-TRN-0000003","title":"Fact card: Shanghai Metro (urban-transit)","category":"urban-transit","subject_name":"Shanghai Metro","description":"The essential facts. Shanghai Metro — urban-transit: The world’s longest metro, over 800 km First line opened in 1993.","key_specs":"[array ×2]","source":"online","source_ref":"https://en.wikipedia.org/wiki/Danyang–Kunshan_Grand_Bridge","is_real":true};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Fact card: Shanghai Metro (urban-transit) ===");
console.log("Record JAH-TRN-0000003 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
