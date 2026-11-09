/* JAH interactive demo program — jahdb-demo-1.0
 * Database: maritime · Record: JAH-MAR-000003 · SOLAS — historical survey CS-6757/R-10003
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-6757/R-10003, compiled 2021) examines 973 documented records concerning SOLAS in a historical survey setting. The established facts remain: the Safety of Life at Sea convention setting global standards for ship construction and safety The study focuses on lifeboats and drills, reporting patterns consistent with published maritime references. As a Signature-generated study record, the scenario is illustrative; the core facts about SOLAS come from published maritime sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== SOLAS — historical survey CS-6757/R-10003 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, solas, setting, facts, safety, published, maritime, 2021");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
