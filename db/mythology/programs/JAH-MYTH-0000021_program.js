/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000021 · Pandora's box — Ritual and worship
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Pandora, the first woman, opened a jar releasing all evils into the world, leaving only hope inside. Hesiod tells the tale in Works and Days.\n\nMyths were not entertainment; they were scripts for ritual. Pandora's box was enacted in festivals, sacrifices, and mysteries that bound communities together and aligned human time with cosmic time. Viewed through a symbolic lens, Pandora's box is read for its images — what each figure and object stands for beneath the plot.\n\nWhere the myth was performed, it was believed with the body, not just the mind. A second sub-question concerns the historical kernel: what real events or places might stand behind Pandora's box. Related entries in this archive: Enuma Elish and Tuatha De Danann.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Pandora's box — Ritual and worship ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: pandora's, were, time, with, what, pandora, first, woman");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
