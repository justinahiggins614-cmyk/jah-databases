/* JAH interactive demo program — jahdb-demo-1.0
 * Database: neuroscience · Record: JAH-NEU-000023 · Hippocampus — laboratory study CS-3137/R-10023
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-3137/R-10023, compiled 2021) reviews 880 documented observations of Hippocampus in a laboratory study setting. The established facts remain: forms new memories and supports spatial navigation; neuron death here is a hallmark of Alzheimer’s disease Observers in this illustrative study focused on memory formation and spatial navigation, reporting patterns consistent with the published literature. As a Signature-generated study record, the scenario is illustrative; the core facts about Hippocampus come from published neuroscience.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Hippocampus — laboratory study CS-3137/R-10023 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, this, hippocampus, facts, spatial, navigation, illustrative, published");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
