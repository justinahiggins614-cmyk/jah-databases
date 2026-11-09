/* JAH interactive demo program — jahdb-demo-1.0
 * Database: travel · Record: JAH-TRV-0000012 · Sydney Opera House — Destination profile
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-TRV-0000012","title":"Sydney Opera House — Destination profile","subject":"Sydney Opera House","category":"destinations","record_type":"profile","source":"online","source_ref":"https://www.greatrail.com/the-journey-blog/2025/january/top-unesco-world-heritage-sites-around-the-world/","creation_mode":"ONLINE-CURATED","summary":"Sydney Opera House (UNESCO World Heritage Site) is a destination in Australia, typically best in autumn. Known for: Sail-shaped icon opened in 1973. Field: architecture. Archived in the JAH Travel Dat…","facts":{"(object keys)":["j","y","k","a","cite"]},"key_points":"[array ×4]","guidance":"Verify entry rules, schedules and conditions before traveling. Conditions change; check official sources."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Sydney Opera House — Destination profile ===");
console.log("Record JAH-TRV-0000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
