/* JAH interactive demo program — jahdb-demo-1.0
 * Database: maritime · Record: JAH-MAR-000023 · Container ship — fleet review CS-3137/R-10023
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-3137/R-10023, compiled 2021) examines 444 documented records concerning Container ship in a fleet review setting. The established facts remain: boxships carry standardized containers measured in TEU; the largest carry well over 20,000 TEU The study focuses on TEU and intermodal, reporting patterns consistent with published maritime references. As a Signature-generated study record, the scenario is illustrative; the core facts about Container ship come from published maritime sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Container ship — fleet review CS-3137/R-10023 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, container, ship, facts, carry, published, maritime, 2021");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
