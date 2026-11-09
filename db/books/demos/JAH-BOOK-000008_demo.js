/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000008 · The World of Reactions & Equations
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Key vocabulary: **product** (a substance formed by a reaction).\n\nKey vocabulary: **reactant** (a starting substance in a reaction).\n\nKey vocabulary: **catalyst** (a substance that speeds a reaction without being consumed).\n\nThe big idea: patterns matter more than memorized facts.\n\nWhat matters most here is product connects directly to catalyst.\n\nWorked example: Mixing 6 g of salt into 7 g of water makes a solution of about 46.2% concentration.\n\nWorked example: Vinegar (pH ~3) is 10000 times more acidic than pure water (pH 7).\n\nPractice: explain product in your own words\n\nYour turn: draw and label a diagram of product\n\nLink forward: everything in this chapter prepares you for Reactions & Equations: Going Deeper, where the same ideas get sharper.\n\nIn chemistry, **reactant** means a starting substance in a reaction.\n\nKey vocabulary: **product** (a substance formed by a reaction).\n\nKey vocabulary: **catalyst** (a substance that speeds a reaction without being consumed).\n\nIf you remember one thing, remember this: each new idea builds on the last one.\n\nWhat matters most here is the vocabulary is the doorway; walk through it slowly.\n\nWorked example: Vinegar (pH ~3) is 10000 times more acidic than pure water (pH 7).\n\nWorked example: Vinegar (pH ~3) is 10000 times more acidic than pure water (pH 7).\n\nPractice: draw and label a diagram of reactant\n\nPractice: write one question about reactions & equations you still have\n\nWatch out: confusing similar-sounding terms — compare them side by side\n\nChapter summary: Next, Reactions & Equations meets the real world in the chapters ahead. The practice tasks lock in the ideas. Review the worked example before moving on.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The World of Reactions & Equations ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: vocabulary, substance, reaction, product, worked, example, more, than");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
