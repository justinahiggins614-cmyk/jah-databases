/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aviation · Record: JAH-AVI-000009 · Ramjet engine: safety relevance (R-10009)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-AVI-000009","title":"Ramjet engine: safety relevance (R-10009)","description":"Ramjet engine is a engine type. a duct with no moving parts that compresses air by forward motion; needs about Mach 0.5 to start and is efficient beyond Mach 3. Key specifications: moving parts: 0; ef…","category":"propulsion","spec":{"(object keys)":["subject","subject_type","category","key_spec","specs","related","year","aspect"]},"src":"online"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Ramjet engine: safety relevance (R-10009) ===");
console.log("Record JAH-AVI-000009 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
