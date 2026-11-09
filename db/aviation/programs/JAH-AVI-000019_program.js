/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aviation · Record: JAH-AVI-000019 · Airbus A380 — fleet planning study CS-7461/R-10019
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-7461/R-10019, compiled 2023) examines 658 documented records concerning Airbus A380 in a fleet planning study setting. The established facts remain: the world’s largest passenger airliner: full double deck, four turbofan engines, first flight 2005 The study focuses on superjumbo and double-deck, reporting patterns consistent with published aviation references. As a Signature-generated study record, the scenario is illustrative; the core facts about Airbus A380 come from published aviation sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Airbus A380 — fleet planning study CS-7461/R-10019 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, airbus, a380, facts, published, aviation, 2005, 2023");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
