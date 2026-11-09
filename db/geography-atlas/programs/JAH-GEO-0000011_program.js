/* JAH interactive demo program — jahdb-demo-1.0
 * Database: geography-atlas · Record: JAH-GEO-0000011 · Fact card: Germany (country)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-GEO-0000011","record_id":"JAH-GEO-0000011","title":"Fact card: Germany (country)","category":"political","place":"Germany","place_type":"country","region":"Europe","description":"The essential facts. Germany — country in Europe. Capital: Berlin.","key_facts":"[array ×2]","source":"online","source_ref":"https://en.wikipedia.org/wiki/List_of_river_systems_by_length","is_real":true};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Fact card: Germany (country) ===");
console.log("Record JAH-GEO-0000011 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
