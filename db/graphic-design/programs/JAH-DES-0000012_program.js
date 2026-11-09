/* JAH interactive demo program — jahdb-demo-1.0
 * Database: graphic-design · Record: JAH-DES-0000012 · Typography anatomy: Ligature
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"typography","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Typography anatomy: Ligature","topic":"type anatomy","spec":{"(object keys)":["term","definition","example"]},"source_ref":"https://github.com/igbuend/grimbard/blob/HEAD/skills/typography/typography-research.md","description":"The term Ligature means: Two or more letters joined into a single glyph. Common pairs: fi, fl and ff. Knowing type anatomy helps designers judge sizing, pairing and spacing instead of guessing.","id":"JAH-DES-0000012"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Typography anatomy: Ligature ===");
console.log("Record JAH-DES-0000012 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
