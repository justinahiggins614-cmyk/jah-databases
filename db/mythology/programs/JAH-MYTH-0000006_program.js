/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000006 · Apollo — Variants across tellings
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Apollo is god of the sun, music, prophecy, and healing. His oracle at Delphi was consulted by kings and city-states.\n\nNo myth has one true version. Apollo survives in competing tellings — poets, priests, and painters each shaping it to their purpose. The variants disagree, and the disagreements are themselves revealing. Viewed through a narrative lens, Apollo is examined as story — its plot, its pacing, and the moments that make it unforgettable.\n\nThe 'real' Apollo is the whole cloud of versions, not any single text. A fourth sub-question examines the moral the myth was meant to teach its first hearers. Related entries in this archive: Minotaur and Ziggurats.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Apollo — Variants across tellings ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: apollo, myth, music, prophecy, healing, oracle, delphi, consulted");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
