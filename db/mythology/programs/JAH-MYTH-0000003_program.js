/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000003 · Poseidon — Echoes in later ages
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Poseidon rules the sea with his trident and shakes the earth as god of earthquakes. He contested Athena for patronage of Athens and lost.\n\nLong after its gods lost worshippers, Poseidon kept working — in Renaissance painting, in Romantic poetry, in modern film. Each age found its own anxieties reflected in the old story. Viewed through a narrative lens, Poseidon is examined as story — its plot, its pacing, and the moments that make it unforgettable.\n\nMyths survive by being reusable. Poseidon proved endlessly reusable. A third sub-question asks how Poseidon was visualized — in vase painting, sculpture, or temple relief. Related entries in this archive: Dionysus and Bhagavad Gita.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Poseidon — Echoes in later ages ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: poseidon, lost, painting, story, reusable, rules, with, trident");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
