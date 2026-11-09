/* JAH interactive demo program — jahdb-demo-1.0
 * Database: music · Record: JAH-SONG-0000004 · Crimson Horizon
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-SONG-0000004","kind":"song","n":4,"title":"Crimson Horizon","genre":"house","mood":"dreamy","tempo":93,"key":"D# major","lyrics":"[Verse 1]\nThe city hums a tune I almost know\nI found a melody in the rain\n\n[Chorus]\nDance until the morning breaks\nEvery heartbeat finds its rhyme\n\n[Verse 2]\nI found a melody in the rain\nThe city hums…","chords":"D# - G - G# - F#","structure":"Intro (4 bars) / Verse (16) / Chorus (16) / Verse (16) / Chorus (16) / Bridge (8) / Chorus (16) / Outro (4)","desc":"A dreamy house song at 93 BPM in D# major, written by the Signature song engine."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Crimson Horizon ===");
console.log("Record JAH-SONG-0000004 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
