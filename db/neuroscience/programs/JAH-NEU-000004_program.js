/* JAH interactive demo program — jahdb-demo-1.0
 * Database: neuroscience · Record: JAH-NEU-000004 · Glial cells: overview (R-10004)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-NEU-000004","title":"Glial cells: overview (R-10004)","description":"Glial cells is a neural cell type of the nervous system. Its role: the support cells of the nervous system: astrocytes, oligodendrocytes, and microglia nourish, insulate, and defend neurons. Key fact:…","category":"glial-biology","spec":{"(object keys)":["subject","subject_type","category","function","key_fact","associated","year","aspect"]},"src":"online"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Glial cells: overview (R-10004) ===");
console.log("Record JAH-NEU-000004 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
