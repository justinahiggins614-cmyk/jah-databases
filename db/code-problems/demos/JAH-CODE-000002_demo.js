/* JAH interactive demo program — jahdb-demo-1.0
 * Database: code-problems · Record: JAH-CODE-000002 · Write a Java method that finds the smallest integer in an ar…
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CODE-000002","task_id":"JAH-CODE-000002","title":"Write a Java method that finds the smallest integer in an array.","prompt":"Write a Java method that finds the smallest integer in an array.","language":"java","solution_code":"public static int findMin(int[] a) {\n    int best = a[0];\n    for (int i = 1; i < a.length; i++) {\n        if (a[i] < best) best = a[i];\n    }\n    return best;\n}","explanation":"One pass keeps the smallest value seen; the loop starts at index 1. The approach is easy to test.","tests_passed":8,"difficulty":"hard"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Write a Java method that finds the smallest integer in an array. ===");
console.log("Record JAH-CODE-000002 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
