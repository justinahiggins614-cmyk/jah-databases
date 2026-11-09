/* JAH interactive demo program — jahdb-demo-1.0
 * Database: music · Record: JAH-SONG-0000020 · Copper Tide
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-SONG-0000020","kind":"song","n":20,"title":"Copper Tide","genre":"trap","mood":"epic","tempo":110,"key":"E major","lyrics":"[Verse 1]\nThe city hums a tune I almost know\nOld guitar leaning by the door\n\n[Chorus]\nWhisper secrets to the open sky\nThe rhythm of the wheels keeps time\n\n[Verse 2]\nOld guitar leaning by the door\nThe …","chords":"E - G# - A - G","structure":"Intro (4 bars) / Verse (16) / Chorus (16) / Verse (16) / Chorus (16) / Bridge (8) / Chorus (16) / Outro (4)","desc":"A epic trap song at 110 BPM in E major, written by the Signature song engine."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Copper Tide ===");
console.log("Record JAH-SONG-0000020 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
