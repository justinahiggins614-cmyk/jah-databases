/* JAH interactive demo program — jahdb-demo-1.0
 * Database: world-history · Record: JAH-HIST-0000011 · Event summary: Newton’s Principia (1687)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-HIST-0000011","record_id":"JAH-HIST-0000011","title":"Event summary: Newton’s Principia (1687)","category":"modern","era":"Modern (1800–1945)","kind":"real-event","event":"Newton’s Principia","date_label":"1687","year_int":1687,"description":"The event in brief. Newton’s Principia, 1687, Europe: Published the laws of motion and gravity.","key_figures":"[array ×1]","region":"Europe","significance":"Published the laws of motion and gravity.","source":"online"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Event summary: Newton’s Principia (1687) ===");
console.log("Record JAH-HIST-0000011 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
