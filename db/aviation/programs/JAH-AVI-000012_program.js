/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aviation · Record: JAH-AVI-000012 · Instrument Landing System (ILS) — operations study CS-6028/R…
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-6028/R-10012, compiled 2023) examines 47 documented records concerning Instrument Landing System (ILS) in a operations study setting. The established facts remain: radio beams — localizer and glideslope — guiding aircraft to the runway in low visibility The study focuses on precision approach and low visibility, reporting patterns consistent with published aviation references. As a Signature-generated study record, the scenario is illustrative; the core facts about Instrument Landing System (ILS) come from published aviation sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Instrument Landing System (ILS) — operations study CS-6028/R-10012 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, instrument, landing, system, facts, visibility, published, aviation");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
