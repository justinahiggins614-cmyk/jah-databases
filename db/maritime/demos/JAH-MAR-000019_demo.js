/* JAH interactive demo program — jahdb-demo-1.0
 * Database: maritime · Record: JAH-MAR-000019 · Bulk carrier — port planning study CS-7461/R-10019
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-7461/R-10019, compiled 2023) examines 658 documented records concerning Bulk carrier in a port planning study setting. The established facts remain: carry unpackaged dry cargo in classes: Capesize above 80,000 DWT, Panamax 60,000-80,000 DWT, Handymax 40,000-60,000 DWT The study focuses on coal and grain, reporting patterns consistent with published maritime references. As a Signature-generated study record, the scenario is illustrative; the core facts about Bulk carrier come from published maritime sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Bulk carrier — port planning study CS-7461/R-10019 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, bulk, carrier, facts, published, maritime, 2023, 80000");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
