/* JAH interactive demo program — jahdb-demo-1.0
 * Database: transportation · Record: JAH-TRN-0000001 · Fact card: Trans-Siberian Railway (rail)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-TRN-0000001","record_id":"JAH-TRN-0000001","title":"Fact card: Trans-Siberian Railway (rail)","category":"rail","subject_name":"Trans-Siberian Railway","description":"The essential facts. Trans-Siberian Railway — rail: 9,289 km from Moscow to Vladivostok Begun 1891, completed 1916; crosses 8 time zones.","key_specs":"[array ×2]","source":"online","source_ref":"https://en.wikipedia.org/wiki/Trans-Siberian_Railway","is_real":true};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Fact card: Trans-Siberian Railway (rail) ===");
console.log("Record JAH-TRN-0000001 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
