/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000018 · Odysseus — Ritual and worship
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Odysseus, hero of the Odyssey, took ten years to return home from Troy. His cunning — the Trojan Horse, the blinding of Polyphemus — defines him.\n\nMyths were not entertainment; they were scripts for ritual. Odysseus was enacted in festivals, sacrifices, and mysteries that bound communities together and aligned human time with cosmic time. Viewed through a cultural lens, Odysseus is examined as a people's self-portrait — the values and fears it encodes.\n\nWhere the myth was performed, it was believed with the body, not just the mind. A fourth sub-question examines the moral the myth was meant to teach its first hearers. Related entries in this archive: Heimdall and Coyote the trickster.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Odysseus — Ritual and worship ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: odysseus, were, time, with, myth, hero, odyssey, took");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
