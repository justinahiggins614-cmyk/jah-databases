/* JAH interactive demo program — jahdb-demo-1.0
 * Database: pharmacology · Record: JAH-PHR-000017 · Beta-2 agonists — formulary review CS-9623/R-10017
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-9623/R-10017, compiled 2019) surveys 1,146 published references on Beta-2 agonists for a formulary review. The established facts remain: stimulate beta-2 receptors in the airways, relaxing bronchial smooth muscle Example drugs covered include albuterol and salmeterol; therapeutic uses surveyed include asthma attacks and COPD. As a Signature-generated study record, the survey scenario is illustrative; the class facts come from published pharmacology. Educational reference only; not medical advice. No dosage information is stored in this database.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Beta-2 agonists — formulary review CS-9623/R-10017 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: this, study, published, beta-2, facts, include, 1146, 2019");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
