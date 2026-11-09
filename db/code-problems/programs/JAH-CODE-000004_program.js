/* JAH interactive demo program — jahdb-demo-1.0
 * Database: code-problems · Record: JAH-CODE-000004 · Write a C function that sums an integer array.
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CODE-000004","task_id":"JAH-CODE-000004","title":"Write a C function that sums an integer array.","prompt":"Write a C function that sums an integer array.","language":"c","solution_code":"int array_sum(const int *a, int n) {\n    int total = 0;\n    for (int i = 0; i < n; i++)\n        total += a[i];\n    return total;\n}","explanation":"A tight loop accumulates the sum; the caller passes the length. It handles edge cases cleanly.","tests_passed":5,"difficulty":"medium"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Write a C function that sums an integer array. ===");
console.log("Record JAH-CODE-000004 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
