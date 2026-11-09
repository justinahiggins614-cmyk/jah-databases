/* JAH interactive demo program — jahdb-demo-1.0
 * Database: error-fix-pairs · Record: JAH-ERR-000001 · Traceback (most recent call last):
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ERR-000001","error_id":"JAH-ERR-000001","error_text":"Traceback (most recent call last):\n  File \"utils.py\", line 3, in <module>\n    result = recurse()\nRecursionError: maximum recursion depth exceeded","context":"server.py dies in a recursive call at line 721.","root_cause":"The recursion has no working base case, so it calls itself forever.","fix":"Add a terminating base case, or rewrite iteratively; as a stopgap, `sys.setrecursionlimit` only delays the crash.","language_or_tool":"python","severity":"high","title":"Traceback (most recent call last):"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Traceback (most recent call last): ===");
console.log("Record JAH-ERR-000001 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
