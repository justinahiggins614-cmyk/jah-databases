/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aviation · Record: JAH-AVI-000016 · Helicopter rotor system — training module CS-1704/R-10016
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-1704/R-10016, compiled 2026) examines 58 documented records concerning Helicopter rotor system in a training module setting. The established facts remain: a powered main rotor provides lift and thrust while the tail rotor counters torque The study focuses on rotor and collective, reporting patterns consistent with published aviation references. As a Signature-generated study record, the scenario is illustrative; the core facts about Helicopter rotor system come from published aviation sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Helicopter rotor system — training module CS-1704/R-10016 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: rotor, study, helicopter, system, facts, published, aviation, 2026");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
