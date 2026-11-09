/* JAH interactive demo program — jahdb-demo-1.0
 * Database: pharmacology · Record: JAH-PHR-000006 · Proton pump inhibitors (PPIs) — therapeutic class study CS-3…
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-3514/R-10006, compiled 2016) surveys 124 published references on Proton pump inhibitors (PPIs) for a therapeutic class study. The established facts remain: irreversibly block the stomach’s proton pumps (H+/K+ ATPase), strongly reducing acid secretion Example drugs covered include omeprazole and esomeprazole; therapeutic uses surveyed include GERD and ulcers. As a Signature-generated study record, the survey scenario is illustrative; the class facts come from published pharmacology. Educational reference only; not medical advice. No dosage information is stored in this database.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Proton pump inhibitors (PPIs) — therapeutic class study CS-3514/R-1000… ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, this, published, proton, therapeutic, class, facts, include");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
