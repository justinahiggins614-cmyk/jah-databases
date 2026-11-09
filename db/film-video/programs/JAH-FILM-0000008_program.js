/* JAH interactive demo program — jahdb-demo-1.0
 * Database: film-video · Record: JAH-FILM-0000008 · Signature shot plan: Ember take
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"shots","source":"signature","creation_mode":"SIGNATURE-GENERATED","title":"Signature shot plan: Ember take","topic":"shot plan","shot":{"(object keys)":["plan","base_shot","takes"]},"description":"A Signature-generated shot plan named Ember take built around a point of view with 4 planned takes. An original shooting study by the JAH generator. Filed as a complete searchable record in the JAH Da…","id":"JAH-FILM-0000008"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature shot plan: Ember take ===");
console.log("Record JAH-FILM-0000008 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
