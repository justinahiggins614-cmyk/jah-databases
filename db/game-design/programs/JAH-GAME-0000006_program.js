/* JAH interactive demo program — jahdb-demo-1.0
 * Database: game-design · Record: JAH-GAME-0000006 · Quest type: Timed
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"quests","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Quest type: Timed","topic":"quest type","mechanic":{"(object keys)":["type","objective","structure"]},"source_ref":"Game design standards (verified 2026-10-09)","description":"The timed quest: Complete an objective before the clock ends. Built here with a linear structure. Clear objectives and fair feedback keep quests satisfying. Filed as a complete searchable record in th…","id":"JAH-GAME-0000006"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Quest type: Timed ===");
console.log("Record JAH-GAME-0000006 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
