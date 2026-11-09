/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000011 · Hermes — Variants across tellings
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Hermes is the messenger god, patron of travelers, thieves, and merchants. He guides souls to the underworld as psychopomp.\n\nNo myth has one true version. Hermes survives in competing tellings — poets, priests, and painters each shaping it to their purpose. The variants disagree, and the disagreements are themselves revealing. Viewed through a cultural lens, Hermes is examined as a people's self-portrait — the values and fears it encodes.\n\nThe 'real' Hermes is the whole cloud of versions, not any single text. A fourth sub-question examines the moral the myth was meant to teach its first hearers. Related entries in this archive: Banshee and Popol Vuh.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Hermes — Variants across tellings ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: hermes, myth, messenger, patron, travelers, thieves, merchants, guides");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
