/* JAH interactive demo program — jahdb-demo-1.0
 * Database: maritime · Record: JAH-MAR-000020 · Lifeboats and muster drills — training module CS-6380/R-1002…
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-6380/R-10020, compiled 2024) examines 399 documented records concerning Lifeboats and muster drills in a training module setting. The established facts remain: passenger ships must carry survival craft for all aboard and drill passengers in emergencies The study focuses on survival craft and EPIRB, reporting patterns consistent with published maritime references. As a Signature-generated study record, the scenario is illustrative; the core facts about Lifeboats and muster drills come from published maritime sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Lifeboats and muster drills — training module CS-6380/R-10020 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, lifeboats, muster, drills, facts, survival, craft, published");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
