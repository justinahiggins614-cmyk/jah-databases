/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000016 · Theseus — Echoes in later ages
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Theseus slew the Minotaur in the Labyrinth of Crete with Ariadne's thread. He became the legendary king and unifier of Athens.\n\nLong after its gods lost worshippers, Theseus kept working — in Renaissance painting, in Romantic poetry, in modern film. Each age found its own anxieties reflected in the old story. Viewed through a narrative lens, Theseus is examined as story — its plot, its pacing, and the moments that make it unforgettable.\n\nMyths survive by being reusable. Theseus proved endlessly reusable. A fifth sub-question considers how children first meet Theseus, and what the simplified versions leave out. Related entries in this archive: Maat and Horus.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Theseus — Echoes in later ages ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: theseus, story, reusable, slew, minotaur, labyrinth, crete, with");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
