/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000012 · Demeter — What the myth explains
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Demeter, goddess of grain and harvest, is central to the Eleusinian Mysteries. Her grief over Persephone's abduction brings winter.\n\nMyths answer questions science had not yet asked: why the seasons turn, why suffering exists, why kings rule. Demeter encodes its culture's answers in narrative form — explanations you can remember because they move you. Viewed through a narrative lens, Demeter is examined as story — its plot, its pacing, and the moments that make it unforgettable.\n\nTo ask what Demeter explains is to recover the curiosity that made it. A fourth sub-question examines the moral the myth was meant to teach its first hearers. Related entries in this archive: Hades and Pegasus.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Demeter — What the myth explains ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: demeter, narrative, that, goddess, grain, harvest, central, eleusinian");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
