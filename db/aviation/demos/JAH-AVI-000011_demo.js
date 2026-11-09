/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aviation · Record: JAH-AVI-000011 · Piston aircraft engine — fleet planning study CS-7109/R-1001…
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-7109/R-10011, compiled 2016) examines 1,085 documented records concerning Piston aircraft engine in a fleet planning study setting. The established facts remain: reciprocating engines driving propellers on light aircraft, in inline, V-type, radial, or opposed layouts The study focuses on propeller and light aircraft, reporting patterns consistent with published aviation references. As a Signature-generated study record, the scenario is illustrative; the core facts about Piston aircraft engine come from published aviation sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Piston aircraft engine — fleet planning study CS-7109/R-10011 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, aircraft, piston, engine, facts, light, published, aviation");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
