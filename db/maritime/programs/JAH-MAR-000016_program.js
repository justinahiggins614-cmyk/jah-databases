/* JAH interactive demo program — jahdb-demo-1.0
 * Database: maritime · Record: JAH-MAR-000016 · COLREGs — training module CS-1704/R-10016
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-1704/R-10016, compiled 2026) examines 58 documented records concerning COLREGs in a training module setting. The established facts remain: the International Regulations for Preventing Collisions at Sea: the rules of the road for vessels The study focuses on right of way and lights, reporting patterns consistent with published maritime references. As a Signature-generated study record, the scenario is illustrative; the core facts about COLREGs come from published maritime sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== COLREGs — training module CS-1704/R-10016 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, colregs, facts, published, maritime, 2026, this, generated");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
