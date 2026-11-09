/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aviation · Record: JAH-AVI-000004 · Wright Flyer: overview (R-10004)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-AVI-000004","title":"Wright Flyer: overview (R-10004)","description":"Wright Flyer is a aircraft, first recorded in 1903. the first powered, controlled airplane, flown at Kitty Hawk in 1903. Key specifications: first flight: 1903; place: Kitty Hawk. Related topics: Wrig…","category":"aviation-history","spec":{"(object keys)":["subject","subject_type","category","key_spec","specs","related","year","aspect"]},"src":"online"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Wright Flyer: overview (R-10004) ===");
console.log("Record JAH-AVI-000004 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
