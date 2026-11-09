/* JAH interactive demo program — jahdb-demo-1.0
 * Database: code-problems · Record: JAH-CODE-000012 · Write a JavaScript function that filters even numbers from a…
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CODE-000012","task_id":"JAH-CODE-000012","title":"Write a JavaScript function that filters even numbers from an array.","prompt":"Write a JavaScript function that filters even numbers from an array.","language":"javascript","solution_code":"function evens(arr) {\n  return arr.filter(function(x) {\n    return x % 2 === 0;\n  });\n}\n\nconsole.log(evens([hello]));","explanation":"The filter method keeps only elements passing the even test. Clean and idiomatic. It runs in linear time.","tests_passed":4,"difficulty":"easy"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Write a JavaScript function that filters even numbers from an array. ===");
console.log("Record JAH-CODE-000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
