/* JAH interactive demo program — jahdb-demo-1.0
 * Database: systems-invention · Record: JAH-SYS-0000016 · Shinkansen nose — kingfisher beak
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"title":"Shinkansen nose — kingfisher beak","category":"cross-domain","domains":"[array ×2]","domain_count":2,"problem_statement":"Bullet trains exiting tunnels at speed produced a sonic-boom-like tunnel boom that broke noise regulations.","concept":"Engineer and birdwatcher Eiji Nakatsu redesigned the Shinkansen nose after the kingfisher's beak — a shape that moves between air and water without a splash. The boom vanished, speed rose, and energy …","novelty_assessment":"Cross-domain transfer by a hobbyist's eye: fluid dynamics shared between beaks and trains.","constraints":"[array ×2]","validation_plan":"[array ×2]","feasibility":"feasible","source":"online","source_ref":"https://en.wikipedia.org/wiki/Shinkansen","creation_mode":"ONLINE-VERIFIED","id":"JAH-SYS-0000016"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Shinkansen nose — kingfisher beak ===");
console.log("Record JAH-SYS-0000016 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
