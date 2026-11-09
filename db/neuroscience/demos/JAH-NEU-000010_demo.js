/* JAH interactive demo program — jahdb-demo-1.0
 * Database: neuroscience · Record: JAH-NEU-000010 · Long-term potentiation — imaging study CS-8190/R-10010
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-8190/R-10010, compiled 2018) reviews 1,810 documented observations of Long-term potentiation in a imaging study setting. The established facts remain: lasting strengthening of synapses after repeated stimulation; a cellular basis of memory Observers in this illustrative study focused on memory and hippocampus, reporting patterns consistent with the published literature. As a Signature-generated study record, the scenario is illustrative; the core facts about Long-term potentiation come from published neuroscience.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Long-term potentiation — imaging study CS-8190/R-10010 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, this, long-term, potentiation, facts, memory, illustrative, published");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
