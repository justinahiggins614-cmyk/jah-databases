/* JAH interactive demo program — jahdb-demo-1.0
 * Database: religion · Record: JAH-REL-000017 · Judaism: Overview — Tradition Overview (Edition 1)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-REL-000017","title":"Judaism: Overview — Tradition Overview (Edition 1)","description":"Judaism is the ancient monotheistic faith of the Jewish people, centered on covenant with one God. The Pew Research Center estimated about 14 million Jews worldwide, about two-tenths of one percent of…","category":"judaism","src":"online","spec":{"(object keys)":["tradition","category","lens","edition","overview","sacred_texts","core_beliefs","practices"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Judaism: Overview — Tradition Overview (Edition 1) ===");
console.log("Record JAH-REL-000017 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
