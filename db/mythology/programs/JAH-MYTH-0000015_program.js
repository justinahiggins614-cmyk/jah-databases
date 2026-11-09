/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000015 · Heracles — Gods, heroes, and monsters
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Heracles performed the Twelve Labors — slaying the Nemean lion, the Hydra, and others — to atone for a madness-induced crime. He was the greatest hero of Greek myth, later worshipped as a god.\n\nMyths are carried by persons — gods who are larger than human, heroes who are almost, monsters who embody what must be faced. In Heracles, each figure plays a role that reveals what the culture feared, honored, and desired. Viewed through a symbolic lens, Heracles is read for its images — what each figure and object stands for beneath the plot.\n\nThe figures of Heracles outlive their religion: they become metaphors the whole world now uses. A third sub-question asks how Heracles was visualized — in vase painting, sculpture, or temple relief. Related entries in this archive: Marduk and Hel.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Heracles — Gods, heroes, and monsters ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: heracles, what, each, figure, performed, twelve, labors, slaying");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
