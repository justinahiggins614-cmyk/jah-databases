/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000022 · Prometheus — Variants across tellings
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Prometheus stole fire for humanity and was chained to a rock where an eagle ate his liver daily. He embodies the suffering benefactor of mankind.\n\nNo myth has one true version. Prometheus survives in competing tellings — poets, priests, and painters each shaping it to their purpose. The variants disagree, and the disagreements are themselves revealing. Viewed through a narrative lens, Prometheus is examined as story — its plot, its pacing, and the moments that make it unforgettable.\n\nThe 'real' Prometheus is the whole cloud of versions, not any single text. A second sub-question concerns the historical kernel: what real events or places might stand behind Prometheus. Related entries in this archive: Valhalla and Enuma Elish.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Prometheus — Variants across tellings ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: prometheus, stole, fire, humanity, chained, rock, where, eagle");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
