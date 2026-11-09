/* JAH interactive demo program — jahdb-demo-1.0
 * Database: code-database · Record: JAH-CODE-0000012 · Debounce — trailing edge (Javascript)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"title":"Debounce — trailing edge (Javascript)","category":"javascript","language":"javascript","description":"Debounce waits until calls stop for `wait` ms, then runs once. The standard fix for search-as-you-type hammering a backend. Worked example: run 3 rapid calls mentally — inputs bind as written, each st…","code":"function debounce(fn, wait) {\n  let t;\n  return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), wait); };\n}\nlet calls = 0;\nconst f = debounce(() => calls++, 40);\nf(); f(); f();\nsetTimeout(…","how_it_works":"Each call clears the pending timer and starts a new one; only the last call in a burst survives the quiet period.","complexity":"O(1)","test_cases":"[array ×2]","pitfalls":"Leading-edge variants need a different shape; pick one and document it.","use_cases":"Search inputs, resize handlers, autosave.","source":"online","source_ref":"https://en.wikipedia.org/wiki/Debounce","creation_mode":"ONLINE-VERIFIED","id":"JAH-CODE-0000012"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Debounce — trailing edge (Javascript) ===");
console.log("Record JAH-CODE-0000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
