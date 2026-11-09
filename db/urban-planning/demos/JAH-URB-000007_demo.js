/* JAH interactive demo program — jahdb-demo-1.0
 * Database: urban-planning · Record: JAH-URB-000007 · Urban Growth Boundary — Core Overview (Edition 1)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-URB-000007","title":"Urban Growth Boundary — Core Overview (Edition 1)","description":"An urban growth boundary draws a legal line around a metro area, concentrating development inside and preserving farmland and open space outside. Oregon's 1973 statewide planning law required every ci…","category":"land-use","src":"online","spec":{"(object keys)":["concept","category","lens","edition","principles","mechanisms","real_examples","key_metrics"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Urban Growth Boundary — Core Overview (Edition 1) ===");
console.log("Record JAH-URB-000007 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
