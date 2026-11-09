/* JAH interactive demo program — jahdb-demo-1.0
 * Database: systems-invention · Record: JAH-SYS-0000009 · Morpho butterfly — structural color
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"title":"Morpho butterfly — structural color","category":"cross-domain","domains":"[array ×2]","domain_count":2,"problem_statement":"Pigments fade and need toxic chemistry for vivid colors. The problem is documented and scoped before any solution work begins.","concept":"Morpho butterfly wings get their blue from nanoscale structures, not pigment — light interference does the coloring. Structural color never fades and needs no dye chemistry. Crossover note: the power …","novelty_assessment":"Color as geometry rather than chemistry.","constraints":"[array ×3]","validation_plan":"[array ×2]","feasibility":"plausible","source":"online","source_ref":"https://en.wikipedia.org/wiki/Biomimicry","creation_mode":"ONLINE-VERIFIED","id":"JAH-SYS-0000009"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Morpho butterfly — structural color ===");
console.log("Record JAH-SYS-0000009 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
