/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aviation · Record: JAH-AVI-000007 · Boeing 747 — safety case CS-2433/R-10007
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-2433/R-10007, compiled 2021) examines 823 documented records concerning Boeing 747 in a safety case setting. The established facts remain: the original jumbo jet: four turbofan engines, first flight 1969, nicknamed the Queen of the Skies The study focuses on widebody and long-haul, reporting patterns consistent with published aviation references. As a Signature-generated study record, the scenario is illustrative; the core facts about Boeing 747 come from published aviation sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Boeing 747 — safety case CS-2433/R-10007 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, boeing, facts, published, aviation, 1969, 2021, this");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
