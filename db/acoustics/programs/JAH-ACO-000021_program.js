/* JAH interactive demo program — jahdb-demo-1.0
 * Database: acoustics · Record: JAH-ACO-000021 · Clarinet — 85–114 dB
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-ACO-000021","title":"Clarinet — 85–114 dB","description":"Measured performance levels for clarinet run 85–114 dB, spanning from about 147 Hz into the altissimo register. High frequencies of 2,000–4,000 Hz are the most damaging, and aging steals the highs fir…","category":"musical-instruments","src":"online","spec":{"(object keys)":["instrument","db_level","frequency_range","application"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Clarinet — 85–114 dB ===");
console.log("Record JAH-ACO-000021 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
