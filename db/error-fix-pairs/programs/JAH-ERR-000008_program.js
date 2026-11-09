/* JAH interactive demo program — jahdb-demo-1.0
 * Database: error-fix-pairs · Record: JAH-ERR-000008 · ReferenceError: resp is not defined
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ERR-000008","error_id":"JAH-ERR-000008","error_text":"ReferenceError: resp is not defined\n    at init (api.js:625:328)","context":"app.js throws the moment init() runs.","root_cause":"count was never declared (typo, missing import, or a script tag that failed to load).","fix":"Declare/import name before use; check the network tab to confirm the defining script actually loaded.","language_or_tool":"javascript","severity":"high","title":"ReferenceError: resp is not defined"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== ReferenceError: resp is not defined ===");
console.log("Record JAH-ERR-000008 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
