/* JAH interactive demo program — jahdb-demo-1.0
 * Database: game-design · Record: JAH-GAME-0000017 · Player type: Socializerss
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"rules","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Player type: Socializerss","topic":"player type","mechanic":{"(object keys)":["type","motivation"]},"source_ref":"https://en.wikipedia.org/wiki/Bartle_taxonomy_of_player_types","description":"Bartle’s socializerss: Play to interact with other people. Designing for a healthy mix of the four types keeps a multiplayer world alive. Filed as a complete searchable record in the JAH Data Bases ar…","id":"JAH-GAME-0000017"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Player type: Socializerss ===");
console.log("Record JAH-GAME-0000017 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
