/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aviation · Record: JAH-AVI-000018 · Flight levels — historical survey CS-8542/R-10018
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-8542/R-10018, compiled 2023) examines 1,074 documented records concerning Flight levels in a historical survey setting. The established facts remain: cruise altitudes expressed in hundreds of feet: FL350 means 35,000 feet on standard pressure The study focuses on altimetry and cruise, reporting patterns consistent with published aviation references. As a Signature-generated study record, the scenario is illustrative; the core facts about Flight levels come from published aviation sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Flight levels — historical survey CS-8542/R-10018 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, flight, levels, facts, cruise, feet, published, aviation");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
