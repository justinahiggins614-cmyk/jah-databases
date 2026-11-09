/* JAH interactive demo program — jahdb-demo-1.0
 * Database: storytelling · Record: JAH-STRY-0000023 · Save the Cat Beat Sheet: Debate
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"plots","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Save the Cat Beat Sheet: Debate","topic":"story beat","structure":{"(object keys)":["framework","beat","order","of","note"]},"source_ref":"https://nofilmschool.com/save-the-cat-beat-sheet","description":"The undefined is stage 5 of 15 in the Save the Cat Beat Sheet framework. Pages 12-25: the hero wrestles with acting. Writers use this structure to shape rising tension and earned payoffs.","id":"JAH-STRY-0000023"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Save the Cat Beat Sheet: Debate ===");
console.log("Record JAH-STRY-0000023 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
