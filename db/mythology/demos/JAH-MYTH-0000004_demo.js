/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000004 · Signature exploration: Hades — A new telling
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="This is a Signature-original exploration, written by the JAH Mythology Creator as a hypothetical study — not a historical claim. It takes Hades (greek) as its launch point and asks what a brand-new, never-before-named variation could look like if it were invented today under the Signature method.\n\nSuppose the spirit of Hades were retold today, with new characters but the old pattern intact. What would a brand-new telling look like — same mythic engine, new story? The sketch below offers one possible answer. Viewed through a symbolic lens, Hades is read for its images — what each figure and object stands for beneath the plot.\n\nThe sketch is offered as invention, not scholarship: a way to dream with Hades rather than merely study it. A second sub-question concerns the historical kernel: what real events or places might stand behind Hades. Because this entry is Signature-generated, every claim about the new variation is presented as invention, clearly separated from the sourced facts about Hades.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Signature exploration: Hades — A new telling ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: hades, what, this, study, historical, claim, brand-new, variation");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
