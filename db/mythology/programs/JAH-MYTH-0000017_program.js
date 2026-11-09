/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000017 · Perseus — Echoes in later ages
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Perseus beheaded the Gorgon Medusa using a mirrored shield and winged sandals. He later rescued Andromeda from a sea monster.\n\nLong after its gods lost worshippers, Perseus kept working — in Renaissance painting, in Romantic poetry, in modern film. Each age found its own anxieties reflected in the old story. Viewed through a narrative lens, Perseus is examined as story — its plot, its pacing, and the moments that make it unforgettable.\n\nMyths survive by being reusable. Perseus proved endlessly reusable. A fourth sub-question examines the moral the myth was meant to teach its first hearers. Related entries in this archive: Odin and Cerberus.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Perseus — Echoes in later ages ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: perseus, story, reusable, beheaded, gorgon, medusa, using, mirrored");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
