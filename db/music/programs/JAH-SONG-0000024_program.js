/* JAH interactive demo program — jahdb-demo-1.0
 * Database: music · Record: JAH-SONG-0000024 · Patient River
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-SONG-0000024","kind":"song","n":24,"title":"Patient River","genre":"rock","mood":"dark","tempo":133,"key":"A# minor","lyrics":"[Verse 1]\nWoke up with the sunrise in my pocket\nYour laughter lingers in the hallway\n\n[Chorus]\nHold the night, don't let it go\nWe are golden in the afterglow\n\n[Verse 2]\nYour laughter lingers in the ha…","chords":"A# - D - D# - C#","structure":"Intro (4 bars) / Verse (16) / Chorus (16) / Verse (16) / Chorus (16) / Bridge (8) / Chorus (16) / Outro (4)","desc":"A dark rock song at 133 BPM in A# minor, written by the Signature song engine."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Patient River ===");
console.log("Record JAH-SONG-0000024 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
