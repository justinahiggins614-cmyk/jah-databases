/* JAH interactive demo program — jahdb-demo-1.0
 * Database: systems-invention · Record: JAH-SYS-0000019 · Post-it note — 3M (Silver/Fry)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"title":"Post-it note — 3M (Silver/Fry)","category":"cross-domain","domains":"[array ×3]","domain_count":3,"problem_statement":"A \"failed\" weak adhesive had no use; bookmarks kept falling out of hymnals. The problem is documented and scoped before any solution work begins.","concept":"Spencer Silver's weak adhesive (1968) met Art Fry's bookmark problem (1974) at 3M: repositionable notes. A solution waited years for its problem. Validation emphasis: the listed validation plan is the…","novelty_assessment":"Failure-tolerant R&D: the lab kept the \"failure\" until the use appeared.","constraints":"[array ×2]","validation_plan":"[array ×2]","feasibility":"feasible","source":"online","source_ref":"https://en.wikipedia.org/wiki/Post-it_note","creation_mode":"ONLINE-VERIFIED","id":"JAH-SYS-0000019"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Post-it note — 3M (Silver/Fry) ===");
console.log("Record JAH-SYS-0000019 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
