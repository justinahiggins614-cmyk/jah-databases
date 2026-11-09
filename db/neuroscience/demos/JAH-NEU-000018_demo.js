/* JAH interactive demo program — jahdb-demo-1.0
 * Database: neuroscience · Record: JAH-NEU-000018 · The case of Phineas Gage — research survey CS-8542/R-10018
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-8542/R-10018, compiled 2023) reviews 2,143 documented observations of The case of Phineas Gage in a research survey setting. The established facts remain: an 1848 railroad accident drove an iron rod through his frontal lobe, changing his personality and revealing the lobe’s role Observers in this illustrative study focused on frontal lobe and personality, reporting patterns consistent with the published literature. As a Signature-generated study record, the scenario is illustrative; the core facts about The case of Phineas Gage come from published neuroscience.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The case of Phineas Gage — research survey CS-8542/R-10018 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, this, case, phineas, gage, facts, frontal, lobe");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
