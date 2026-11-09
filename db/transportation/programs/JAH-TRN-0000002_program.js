/* JAH interactive demo program — jahdb-demo-1.0
 * Database: transportation · Record: JAH-TRN-0000002 · Fact card: Danyang–Kunshan Grand Bridge (rail)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-TRN-0000002","record_id":"JAH-TRN-0000002","title":"Fact card: Danyang–Kunshan Grand Bridge (rail)","category":"rail","subject_name":"Danyang–Kunshan Grand Bridge","description":"The essential facts. Danyang–Kunshan Grand Bridge — rail: 164.8 km; the world’s longest bridge Opened June 30, 2011, on the Beijing–Shanghai high-speed line.","key_specs":"[array ×2]","source":"online","source_ref":"https://en.wikipedia.org/wiki/Trans-Siberian_Railway","is_real":true};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Fact card: Danyang–Kunshan Grand Bridge (rail) ===");
console.log("Record JAH-TRN-0000002 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
