/* JAH interactive demo program — jahdb-demo-1.0
 * Database: neuroscience · Record: JAH-NEU-000019 · Basal ganglia — therapeutic program CS-7461/R-10019
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-7461/R-10019, compiled 2023) reviews 1,310 documented observations of Basal ganglia in a therapeutic program setting. The established facts remain: clusters including the caudate nucleus, putamen, globus pallidus, and substantia nigra; initiate movements Observers in this illustrative study focused on movement initiation and habit formation, reporting patterns consistent with the published literature. As a Signature-generated study record, the scenario is illustrative; the core facts about Basal ganglia come from published neuroscience.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Basal ganglia — therapeutic program CS-7461/R-10019 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, this, basal, ganglia, facts, illustrative, published, 1310");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
