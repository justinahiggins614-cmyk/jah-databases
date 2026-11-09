/* JAH interactive demo program — jahdb-demo-1.0
 * Database: eval-benchmarks · Record: JAH-BENCH-000012 · Call calculate with the expression "12*8+5" and report the r…
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-BENCH-000012","bench_id":"JAH-BENCH-000012","title":"Call calculate with the expression \"12*8+5\" and report the result.","task":"Call calculate with the expression \"12*8+5\" and report the result.","expected":"101","rubric":{"(object keys)":["criteria","max_score"]},"metric":"human-rating","category":"tool-use","weight":0.7};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Call calculate with the expression \"12*8+5\" and report the result. ===");
console.log("Record JAH-BENCH-000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
