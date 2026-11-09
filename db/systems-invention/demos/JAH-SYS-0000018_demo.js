/* JAH interactive demo program — jahdb-demo-1.0
 * Database: systems-invention · Record: JAH-SYS-0000018 · Six Thinking Hats — de Bono
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"title":"Six Thinking Hats — de Bono","category":"concepts","domains":"[array ×2]","domain_count":2,"problem_statement":"Group thinking tangles facts, feelings, and criticism into one argument. The problem is documented and scoped before any solution work begins.","concept":"Edward de Bono's Six Thinking Hats (1985): separate thinking modes — white (facts), red (feelings), black (caution), yellow (benefits), green (creativity), blue (process) — worn one at a time.","novelty_assessment":"Parallel thinking: everyone thinks the same way at the same time. Novelty check: search prior art for each claimed transfer before investing.","constraints":"[array ×2]","validation_plan":"[array ×2]","feasibility":"feasible","source":"online","source_ref":"https://en.wikipedia.org/wiki/Six_Thinking_Hats","creation_mode":"ONLINE-VERIFIED","id":"JAH-SYS-0000018"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Six Thinking Hats — de Bono ===");
console.log("Record JAH-SYS-0000018 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
