/* JAH interactive demo program — jahdb-demo-1.0
 * Database: maritime · Record: JAH-MAR-000011 · Panama Canal — port planning study CS-7109/R-10011
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-7109/R-10011, compiled 2016) examines 1,085 documented records concerning Panama Canal in a port planning study setting. The established facts remain: links the Atlantic and Pacific oceans; Panamax vessels fit its original locks at 32.2 m beam The study focuses on locks and Panamax, reporting patterns consistent with published maritime references. As a Signature-generated study record, the scenario is illustrative; the core facts about Panama Canal come from published maritime sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Panama Canal — port planning study CS-7109/R-10011 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, panama, canal, facts, panamax, locks, published, maritime");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
