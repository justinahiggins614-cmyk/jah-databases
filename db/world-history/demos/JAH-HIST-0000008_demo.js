/* JAH interactive demo program — jahdb-demo-1.0
 * Database: world-history · Record: JAH-HIST-0000008 · Event summary: Berlin Wall falls (November 9, 1989)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-HIST-0000008","record_id":"JAH-HIST-0000008","title":"Event summary: Berlin Wall falls (November 9, 1989)","category":"contemporary","era":"Contemporary (1945–present)","kind":"real-event","event":"Berlin Wall falls","date_label":"November 9, 1989","year_int":1989,"description":"The event in brief. Berlin Wall falls, November 9, 1989, Europe: Symbolized the Cold War’s end.","key_figures":"[array ×1]","region":"Europe","significance":"Symbolized the Cold War’s end.","source":"online"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Event summary: Berlin Wall falls (November 9, 1989) ===");
console.log("Record JAH-HIST-0000008 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
