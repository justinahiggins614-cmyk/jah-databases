/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000013 · Dionysus — Variants across tellings
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Dionysus is god of wine, theater, and ecstatic ritual. His worship could dissolve social order, as in Euripides's Bacchae.\n\nNo myth has one true version. Dionysus survives in competing tellings — poets, priests, and painters each shaping it to their purpose. The variants disagree, and the disagreements are themselves revealing. Viewed through a symbolic lens, Dionysus is read for its images — what each figure and object stands for beneath the plot.\n\nThe 'real' Dionysus is the whole cloud of versions, not any single text. One fruitful sub-question is which telling of Dionysus is oldest, and how the tale changed in transmission. Related entries in this archive: Achilles and Trojan War.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Dionysus — Variants across tellings ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: dionysus, each, wine, theater, ecstatic, ritual, worship, could");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
