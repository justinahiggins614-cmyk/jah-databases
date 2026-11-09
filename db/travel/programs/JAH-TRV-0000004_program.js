/* JAH interactive demo program — jahdb-demo-1.0
 * Database: travel · Record: JAH-TRV-0000004 · Acropolis of Athens — Destination profile
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-TRV-0000004","title":"Acropolis of Athens — Destination profile","subject":"Acropolis of Athens","category":"destinations","record_type":"profile","source":"online","source_ref":"https://www.greatrail.com/the-journey-blog/2025/january/top-unesco-world-heritage-sites-around-the-world/","creation_mode":"ONLINE-CURATED","summary":"Acropolis of Athens (UNESCO World Heritage Site) is a destination in Greece, typically best in spring. Known for: Citadel crowned by the Parthenon. Field: historic. Archived in the JAH Travel Database…","facts":{"(object keys)":["j","y","k","a","cite"]},"key_points":"[array ×4]","guidance":"Verify entry rules, schedules and conditions before traveling. Conditions change; check official sources."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Acropolis of Athens — Destination profile ===");
console.log("Record JAH-TRV-0000004 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
