/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000023 · Sisyphus — The tale itself
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Sisyphus was condemned to roll a boulder uphill forever, watching it roll back down. Camus made him the emblem of the absurd.\n\nEvery myth deserves to be heard as story first. Sisyphus unfolds with its own logic — characters acting from motives the myth takes for granted, events following one another with dreamlike necessity. To know Sisyphus is to be able to tell it. Viewed through a narrative lens, Sisyphus is examined as story — its plot, its pacing, and the moments that make it unforgettable.\n\nThe story is the data. All interpretation comes after, and must answer to the tale as told. A fourth sub-question examines the moral the myth was meant to teach its first hearers. Related entries in this archive: Set and Maat.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Sisyphus — The tale itself ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: sisyphus, myth, story, roll, first, with, condemned, boulder");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
