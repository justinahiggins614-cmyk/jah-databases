/* JAH interactive demo program — jahdb-demo-1.0
 * Database: systems-invention · Record: JAH-SYS-0000013 · Sharkskin — drag-reducing textures
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"title":"Sharkskin — drag-reducing textures","category":"cross-domain","domains":"[array ×3]","domain_count":3,"problem_statement":"Drag limits swim and flow speeds. The problem is documented and scoped before any solution work begins.","concept":"Shark skin's denticle texture reduces drag; swimsuit makers (e.g. Speedo's Fastskin line) and ship-coating researchers copy the micro-riblets. Crossover note: the power here is the domain transfer — s…","novelty_assessment":"Surface texture as a speed technology.","constraints":"[array ×2]","validation_plan":"[array ×2]","feasibility":"feasible","source":"online","source_ref":"https://en.wikipedia.org/wiki/Biomimicry","creation_mode":"ONLINE-VERIFIED","id":"JAH-SYS-0000013"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Sharkskin — drag-reducing textures ===");
console.log("Record JAH-SYS-0000013 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
