/* JAH interactive demo program — jahdb-demo-1.0
 * Database: materials · Record: JAH-MAT-0000010 · AISI 1018 Steel — Safety
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"mat_id":"JAH-MAT-0000010","category":"metals","material":"AISI 1018 Steel","composition":"0.18% C","properties":{"(object keys)":["composition","density_kg_m3","UTS_MPa","yield_MPa","hardness_HB"]},"processing":"[array ×0]","applications":"[array ×0]","data_quality":"measured-published","source":"online","source_ref":{"(object keys)":["authority","url"]},"title":"AISI 1018 Steel — Safety","record_type":"safety","description":"Safety with AISI 1018 Steel: Sharp edges; grinding PPE. Low-carbon steel; weldable, machinable, 440 MPa tensile.","standards":"[array ×1]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== AISI 1018 Steel — Safety ===");
console.log("Record JAH-MAT-0000010 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
