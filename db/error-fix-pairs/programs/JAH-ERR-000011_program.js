/* JAH interactive demo program — jahdb-demo-1.0
 * Database: error-fix-pairs · Record: JAH-ERR-000011 · Error response from daemon: network mynet not found
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ERR-000011","error_id":"JAH-ERR-000011","error_text":"Error response from daemon: network mynet not found","context":"docker run --network mynet fails.","root_cause":"The network `mynet` does not exist (typo or never created).","fix":"Create it (`docker network create mynet`) or fix the network name in the command/compose file.","language_or_tool":"docker","severity":"medium","title":"Error response from daemon: network mynet not found"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Error response from daemon: network mynet not found ===");
console.log("Record JAH-ERR-000011 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
