/* JAH interactive demo program — jahdb-demo-1.0
 * Database: maritime · Record: JAH-MAR-000010 · Suez Canal — training module CS-8190/R-10010
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-MAR-000010","title":"Suez Canal — training module CS-8190/R-10010","description":"This generated study (CS-8190/R-10010, compiled 2018) examines 908 documented records concerning Suez Canal in a training module setting. The established facts remain: links the Mediterranean and Red …","category":"ports-harbors","spec":{"(object keys)":["subject","subject_type","category","key_fact","measures","related_terms","year","aspect"]},"src":"signature"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Suez Canal — training module CS-8190/R-10010 ===");
console.log("Record JAH-MAR-000010 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
