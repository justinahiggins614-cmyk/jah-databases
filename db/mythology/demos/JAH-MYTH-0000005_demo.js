/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000005 · Athena — Echoes in later ages
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Athena, goddess of wisdom and warfare, sprang fully armed from Zeus's head. She gave Athens the olive tree and became the city's patron.\n\nLong after its gods lost worshippers, Athena kept working — in Renaissance painting, in Romantic poetry, in modern film. Each age found its own anxieties reflected in the old story. Viewed through a contemporary-relevance lens, Athena is brought into the present, where its patterns still appear in new clothes.\n\nMyths survive by being reusable. Athena proved endlessly reusable. A second sub-question concerns the historical kernel: what real events or places might stand behind Athena. Related entries in this archive: Tir na nOg and Odysseus.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Athena — Echoes in later ages ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: athena, reusable, goddess, wisdom, warfare, sprang, fully, armed");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
