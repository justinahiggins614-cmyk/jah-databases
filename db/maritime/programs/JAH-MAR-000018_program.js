/* JAH interactive demo program — jahdb-demo-1.0
 * Database: maritime · Record: JAH-MAR-000018 · Draft, beam, and freeboard — historical survey CS-8542/R-100…
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This generated study (CS-8542/R-10018, compiled 2023) examines 1,074 documented records concerning Draft, beam, and freeboard in a historical survey setting. The established facts remain: draft is the depth below the waterline, beam is the vessel’s width, and freeboard is the height above water The study focuses on dimensions and stability, reporting patterns consistent with published maritime references. As a Signature-generated study record, the scenario is illustrative; the core facts about Draft, beam, and freeboard come from published maritime sources.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Draft, beam, and freeboard — historical survey CS-8542/R-10018 ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: study, draft, beam, freeboard, facts, published, maritime, 1074");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
