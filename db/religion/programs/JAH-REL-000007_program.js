/* JAH interactive demo program — jahdb-demo-1.0
 * Database: religion · Record: JAH-REL-000007 · Catholic, Protestant, and Orthodox Branches — Tradition Over…
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-REL-000007","title":"Catholic, Protestant, and Orthodox Branches — Tradition Overview (Edition 1)","description":"Christianity's three great branches, Catholic, Protestant, and Eastern Orthodox, differ on authority, tradition, and sacraments. The Catholic Church is the largest single denomination, with more than …","category":"christianity","src":"online","spec":{"(object keys)":["tradition","category","lens","edition","overview","sacred_texts","core_beliefs","practices"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Catholic, Protestant, and Orthodox Branches — Tradition Overview (Edit… ===");
console.log("Record JAH-REL-000007 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
