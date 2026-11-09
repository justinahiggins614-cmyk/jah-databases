/* JAH interactive demo program — jahdb-demo-1.0
 * Database: storytelling · Record: JAH-STRY-0000020 · Signature arc study: Harbor saga
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"arcs","source":"signature","creation_mode":"SIGNATURE-GENERATED","title":"Signature arc study: Harbor saga","topic":"arc study","structure":{"(object keys)":["study","shape","direction"]},"description":"A Signature-generated arc study named Harbor saga following a from bad to worse pattern with a rising line. An original structure experiment by the JAH generator. Filed as a complete searchable record…","id":"JAH-STRY-0000020"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature arc study: Harbor saga ===");
console.log("Record JAH-STRY-0000020 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
