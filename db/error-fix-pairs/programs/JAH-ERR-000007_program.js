/* JAH interactive demo program — jahdb-demo-1.0
 * Database: error-fix-pairs · Record: JAH-ERR-000007 · Traceback (most recent call last):
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ERR-000007","error_id":"JAH-ERR-000007","error_text":"Traceback (most recent call last):\n  File \"config.py\", line 62, in <module>\n    resp = unknown_func()\nNameError: name 'unknown_func' is not defined","context":"A script crashes the moment it reaches a function call in utils.py.","root_cause":"The name was never defined or the defining import was removed, so Python cannot resolve it at call time.","fix":"Define the function before use, or add the missing import (e.g. `from helpers import unknown_func`) at the top of main.py, then rerun.","language_or_tool":"python","severity":"medium","title":"Traceback (most recent call last):"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Traceback (most recent call last): ===");
console.log("Record JAH-ERR-000007 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
