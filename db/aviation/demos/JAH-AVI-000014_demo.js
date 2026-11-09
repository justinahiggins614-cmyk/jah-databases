/* JAH interactive demo program — jahdb-demo-1.0
 * Database: aviation · Record: JAH-AVI-000014 · Messerschmitt Me 262 — engineering review CS-3866/R-10014
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-3866/R-10014, compiled 2023) examines 862 documented records concerning Messerschmitt Me 262 in a engineering review setting. The established facts remain: the first operational jet fighter, entering Luftwaffe service in 1943 The study focuses on jet fighter and WWII, reporting patterns consistent with published aviation references. As a Signature-generated study record, the scenario is illustrative; the core facts about Messerschmitt Me 262 come from published aviation sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Messerschmitt Me 262 — engineering review CS-3866/R-10014 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, messerschmitt, facts, fighter, published, aviation, 1943, 2023");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
