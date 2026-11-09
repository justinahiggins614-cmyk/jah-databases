/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000024 · Icarus — What the myth explains
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Icarus flew too close to the sun on wax wings made by his father Daedalus. His fall warns against hubris.\n\nMyths answer questions science had not yet asked: why the seasons turn, why suffering exists, why kings rule. Icarus encodes its culture's answers in narrative form — explanations you can remember because they move you. Viewed through a contemporary-relevance lens, Icarus is brought into the present, where its patterns still appear in new clothes.\n\nTo ask what Icarus explains is to recover the curiosity that made it. A second sub-question concerns the historical kernel: what real events or places might stand behind Icarus. Related entries in this archive: The Furies and Shiva.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Icarus — What the myth explains ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: icarus, made, what, flew, close, wings, father, daedalus");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
