/* JAH interactive demo program — jahdb-demo-1.0
 * Database: neuroscience · Record: JAH-NEU-000020 · Electroencephalography (EEG) — imaging study CS-6380/R-10020
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-6380/R-10020, compiled 2024) reviews 791 documented observations of Electroencephalography (EEG) in a imaging study setting. The established facts remain: records the brain’s electrical activity through electrodes on the scalp Observers in this illustrative study focused on brain waves and epilepsy diagnosis, reporting patterns consistent with the published literature. As a Signature-generated study record, the scenario is illustrative; the core facts about Electroencephalography (EEG) come from published neuroscience.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Electroencephalography (EEG) — imaging study CS-6380/R-10020 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, this, electroencephalography, facts, illustrative, published, 2024, generated");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
