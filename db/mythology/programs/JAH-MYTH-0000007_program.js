/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000007 · Artemis — The tale itself
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Artemis, twin of Apollo, is goddess of the hunt, wild animals, and the moon. Her band of virgin huntresses admitted no men.\n\nEvery myth deserves to be heard as story first. Artemis unfolds with its own logic — characters acting from motives the myth takes for granted, events following one another with dreamlike necessity. To know Artemis is to be able to tell it. Viewed through a narrative lens, Artemis is examined as story — its plot, its pacing, and the moments that make it unforgettable.\n\nThe story is the data. All interpretation comes after, and must answer to the tale as told. A sixth sub-question asks what modern retellings get wrong about Artemis. Related entries in this archive: Kali and Tiamat.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Artemis — The tale itself ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: artemis, story, myth, with, twin, apollo, goddess, hunt");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
