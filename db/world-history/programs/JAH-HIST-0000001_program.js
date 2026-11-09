/* JAH interactive demo program — jahdb-demo-1.0
 * Database: world-history · Record: JAH-HIST-0000001 · Event summary: Fall of the Western Roman Empire (476 CE)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-HIST-0000001","record_id":"JAH-HIST-0000001","title":"Event summary: Fall of the Western Roman Empire (476 CE)","category":"ancient","era":"Ancient (before 500 CE)","kind":"real-event","event":"Fall of the Western Roman Empire","date_label":"476 CE","year_int":476,"description":"The event in brief. Fall of the Western Roman Empire, 476 CE, Europe: Ended ancient Rome in the west; opened the Middle Ages.","key_figures":"[array ×1]","region":"Europe","significance":"Ended ancient Rome in the west; opened the Middle Ages.","source":"online"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Event summary: Fall of the Western Roman Empire (476 CE) ===");
console.log("Record JAH-HIST-0000001 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
