/* JAH interactive demo program — jahdb-demo-1.0
 * Database: error-fix-pairs · Record: JAH-ERR-000014 · TypeError: data.map is not a function
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ERR-000014","error_id":"JAH-ERR-000014","error_text":"TypeError: data.map is not a function\n    at list (server.js:426:270)","context":"Rendering a list in client.js throws on .map().","root_cause":"config is not an array here — it is an object, null, or a single item.","fix":"Normalize before mapping: `Array.isArray(items) ? items : [items]`, and fix the producer to always send an array.","language_or_tool":"javascript","severity":"medium","title":"TypeError: data.map is not a function"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== TypeError: data.map is not a function ===");
console.log("Record JAH-ERR-000014 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
