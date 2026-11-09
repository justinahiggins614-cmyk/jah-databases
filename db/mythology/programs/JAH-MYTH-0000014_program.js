/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000014 · Persephone — Ritual and worship
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Persephone, queen of the underworld, divides her year between Hades and her mother Demeter. Her story explains the cycle of the seasons.\n\nMyths were not entertainment; they were scripts for ritual. Persephone was enacted in festivals, sacrifices, and mysteries that bound communities together and aligned human time with cosmic time. Viewed through a symbolic lens, Persephone is read for its images — what each figure and object stands for beneath the plot.\n\nWhere the myth was performed, it was believed with the body, not just the mind. A fourth sub-question examines the moral the myth was meant to teach its first hearers. Related entries in this archive: Osiris and Loki.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Persephone — Ritual and worship ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: persephone, were, time, with, myth, queen, underworld, divides");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
