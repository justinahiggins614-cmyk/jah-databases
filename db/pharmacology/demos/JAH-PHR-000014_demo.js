/* JAH interactive demo program — jahdb-demo-1.0
 * Database: pharmacology · Record: JAH-PHR-000014 · Sulfonylureas — clinical education module CS-3866/R-10014
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-3866/R-10014, compiled 2023) surveys 650 published references on Sulfonylureas for a clinical education module. The established facts remain: stimulate the pancreas to release more insulin Example drugs covered include glipizide and glyburide; therapeutic uses surveyed include type 2 diabetes. As a Signature-generated study record, the survey scenario is illustrative; the class facts come from published pharmacology. Educational reference only; not medical advice. No dosage information is stored in this database.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Sulfonylureas — clinical education module CS-3866/R-10014 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: this, study, published, facts, include, 2023, generated, cs-3866r-10014");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
