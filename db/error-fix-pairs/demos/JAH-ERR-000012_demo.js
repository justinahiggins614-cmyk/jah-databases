/* JAH interactive demo program — jahdb-demo-1.0
 * Database: error-fix-pairs · Record: JAH-ERR-000012 · 404 Not Found — {"error":"no_such_resource"}
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ERR-000012","error_id":"JAH-ERR-000012","error_text":"404 Not Found — {\"error\":\"no_such_resource\"}","context":"A GET to /v1/items/640 returns 404.","root_cause":"The ID does not exist, or the path version/prefix is wrong.","fix":"Verify the ID exists (list endpoint) and the base URL/version; handle 404 as \"not found\", not a crash.","language_or_tool":"api","severity":"medium","title":"404 Not Found — {\"error\":\"no_such_resource\"}"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== 404 Not Found — {\"error\":\"no_such_resource\"} ===");
console.log("Record JAH-ERR-000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
