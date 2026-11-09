/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000010 · Hephaestus — Variants across tellings
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Hephaestus, the lame smith god, forges divine weapons in his volcanic workshop. He crafted Achilles's armor and Pandora's form.\n\nNo myth has one true version. Hephaestus survives in competing tellings — poets, priests, and painters each shaping it to their purpose. The variants disagree, and the disagreements are themselves revealing. Viewed through a contemporary-relevance lens, Hephaestus is brought into the present, where its patterns still appear in new clothes.\n\nThe 'real' Hephaestus is the whole cloud of versions, not any single text. A fifth sub-question considers how children first meet Hephaestus, and what the simplified versions leave out. Related entries in this archive: Oni and Gilgamesh.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Hephaestus — Variants across tellings ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: hephaestus, versions, lame, smith, forges, divine, weapons, volcanic");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
