/* JAH interactive demo program — jahdb-demo-1.0
 * Database: pharmacology · Record: JAH-PHR-000019 · Angiotensin II receptor blockers (ARBs) — prescribing refere…
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-7461/R-10019, compiled 2023) surveys 497 published references on Angiotensin II receptor blockers (ARBs) for a prescribing reference study. The established facts remain: block angiotensin II receptors directly, without affecting bradykinin levels Example drugs covered include losartan and valsartan; therapeutic uses surveyed include hypertension and heart failure. As a Signature-generated study record, the survey scenario is illustrative; the class facts come from published pharmacology. Educational reference only; not medical advice. No dosage information is stored in this database.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Angiotensin II receptor blockers (ARBs) — prescribing reference study … ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, this, published, angiotensin, reference, facts, include, 2023");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
