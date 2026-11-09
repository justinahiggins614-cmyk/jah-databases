/* JAH interactive demo program — jahdb-demo-1.0
 * Database: world-history · Record: JAH-HIST-0000004 · Event summary: World War I (1914–1918)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-HIST-0000004","record_id":"JAH-HIST-0000004","title":"Event summary: World War I (1914–1918)","category":"contemporary","era":"Contemporary (1945–present)","kind":"real-event","event":"World War I","date_label":"1914–1918","year_int":1914,"description":"The event in brief. World War I, 1914–1918, Global: Global conflict that redrew the world map.","key_figures":"[array ×1]","region":"Global","significance":"Global conflict that redrew the world map.","source":"online"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Event summary: World War I (1914–1918) ===");
console.log("Record JAH-HIST-0000004 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
