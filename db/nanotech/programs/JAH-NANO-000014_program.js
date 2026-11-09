/* JAH interactive demo program — jahdb-demo-1.0
 * Database: nanotech · Record: JAH-NANO-000014 · Titanium dioxide nanoparticle — nanoparticles
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-NANO-000014","title":"Titanium dioxide nanoparticle — nanoparticles","description":"The titanium dioxide nanoparticle is a 0D nanomaterial with definition: 1–100 nm in at least one dimension; uv: absorbs ultraviolet light. Fabrication route: sol-gel process. The nanoscale runs 1–100 …","category":"nanoparticles","src":"online","spec":{"(object keys)":["material","dimensionality","key_properties","fabrication_method","scale_note"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Titanium dioxide nanoparticle — nanoparticles ===");
console.log("Record JAH-NANO-000014 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
