/* JAH interactive demo program — jahdb-demo-1.0
 * Database: acoustics · Record: JAH-ACO-000017 · Measurement Principle — A 1 dB change is imperceptible; 3 dB…
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ACO-000017","title":"Measurement Principle — A 1 dB change is imperceptible; 3 dB is barely p","description":"A 1 dB change is imperceptible; 3 dB is barely perceptible; 10 dB sounds about twice as loud. Field readings use a sound level meter with A-weighting, which mimics human hearing. Used when field surve…","category":"measurement","src":"online","spec":{"(object keys)":["principle","statement","tool","application"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Measurement Principle — A 1 dB change is imperceptible; 3 dB is barely… ===");
console.log("Record JAH-ACO-000017 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
