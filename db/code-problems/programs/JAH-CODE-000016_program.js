/* JAH interactive demo program — jahdb-demo-1.0
 * Database: code-problems · Record: JAH-CODE-000016 · Write a bash one-liner pipeline counting lines in 5 files.
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CODE-000016","task_id":"JAH-CODE-000016","title":"Write a bash one-liner pipeline counting lines in 5 files.","prompt":"Write a bash one-liner pipeline counting lines in 5 files.","language":"bash","solution_code":"#!/bin/bash\ncount=0\nfor f in *.5; do\n  n=$(wc -l < \"$f\")\n  count=$((count + n))\ndone\necho \"Total lines: $count\"","explanation":"Loop over matching files, count lines with wc, and accumulate the total. The approach is easy to test.","tests_passed":6,"difficulty":"easy"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Write a bash one-liner pipeline counting lines in 5 files. ===");
console.log("Record JAH-CODE-000016 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
