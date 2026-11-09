/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000020 · Trojan War — Comparative mythology
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="The Trojan War was fought over Helen, lasting ten years and ending with the wooden horse. Homer's Iliad covers only a few weeks of its final year.\n\nFloods, tricksters, dying gods, world trees — the same patterns recur across continents. Setting Trojan War beside its parallels tests whether the pattern is human nature, cultural diffusion, or coincidence. Viewed through a symbolic lens, Trojan War is read for its images — what each figure and object stands for beneath the plot.\n\nComparison honors Trojan War by taking it seriously as one answer among many. A fourth sub-question examines the moral the myth was meant to teach its first hearers. Related entries in this archive: Bifrost and Ziggurats.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Trojan War — Comparative mythology ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: trojan, fought, over, helen, lasting, years, ending, with");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
