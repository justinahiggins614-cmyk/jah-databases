/* JAH interactive demo program — jahdb-demo-1.0
 * Database: neuroscience · Record: JAH-NEU-000006 · Neuroplasticity — educational module CS-3514/R-10006
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-3514/R-10006, compiled 2016) reviews 311 documented observations of Neuroplasticity in a educational module setting. The established facts remain: the brain’s ability to rewire itself by strengthening or pruning synapses Observers in this illustrative study focused on learning and memory, reporting patterns consistent with the published literature. As a Signature-generated study record, the scenario is illustrative; the core facts about Neuroplasticity come from published neuroscience.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Neuroplasticity — educational module CS-3514/R-10006 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, this, neuroplasticity, facts, illustrative, published, 2016, generated");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
