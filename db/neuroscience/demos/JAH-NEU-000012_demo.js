/* JAH interactive demo program — jahdb-demo-1.0
 * Database: neuroscience · Record: JAH-NEU-000012 · The neuron — clinical case review CS-6028/R-10012
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-6028/R-10012, compiled 2023) reviews 84 documented observations of The neuron in a clinical case review setting. The established facts remain: the brain’s signaling cell: dendrites receive inputs, the axon transmits output; about 86 billion neurons fill the human brain Observers in this illustrative study focused on dendrites and axon, reporting patterns consistent with the published literature. As a Signature-generated study record, the scenario is illustrative; the core facts about The neuron come from published neuroscience.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The neuron — clinical case review CS-6028/R-10012 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, this, neuron, facts, dendrites, axon, about, illustrative");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
