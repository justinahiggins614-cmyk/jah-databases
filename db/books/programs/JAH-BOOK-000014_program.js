/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000014 · The Garden Sensor (SG-303) Owner's Manual
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Read every step before you plug in the Garden Sensor (SG-303).\n\nKeep the unit dry, away from open flame, and out of reach of small children.\n\nUnplug before cleaning. Never open the sealed case — there are no user-serviceable parts inside.\n\nIf the case is cracked or smells unusual, stop using the unit and contact support.\n\nDo not drop the unit or stack heavy objects on it; internal alignment matters.\n\nIn a thunderstorm, unplug the unit until the storm passes.\n\n1 x Garden Sensor (SG-303)\n\n1 x quick-start card, 1 x power cable, 2 x mounting screws, 1 x warranty leaflet.\n\nCheck that all parts are present. Missing parts are replaced free within 30 days.\n\nKeep the box for at least the warranty period — it is the safest way to transport the unit.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The Garden Sensor (SG-303) Owner's Manual ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: unit, parts, before, garden, sensor, sg-303, keep, open");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
