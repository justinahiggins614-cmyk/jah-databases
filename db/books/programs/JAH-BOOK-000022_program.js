/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000022 · Signature Probability Basics
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="In mathematics, **outcome** means a possible result of an experiment.\n\nProbability — a number from 0 to 1 measuring how likely an event is. This idea returns in every chapter, so keep it close.\n\nIn mathematics, **sample space** means the set of all possible outcomes.\n\nThe big idea: patterns matter more than memorized facts.\n\nWhat matters most here is each new idea builds on the last one.\n\nWorked example: A recipe calls for 11 cups of flour. Tripling it needs 11 x 3 = 33 cups.\n\nWorked example: A recipe calls for 2 cups of flour. Tripling it needs 2 x 3 = 6 cups.\n\nTry it: explain outcome in your own words\n\nPractice: draw and label a diagram of outcome\n\nLink forward: everything in this chapter prepares you for Probability Basics: Going Deeper, where the same ideas get sharper.\n\nKey vocabulary: **outcome** (a possible result of an experiment).\n\nIn mathematics, **probability** means a number from 0 to 1 measuring how likely an event is.\n\nSample space — the set of all possible outcomes. This idea returns in every chapter, so keep it close.\n\nIf you remember one thing, remember this: small examples reveal the general rule.\n\nWhat matters most here is patterns matter more than memorized facts.\n\nWorked example: A recipe calls for 7 cups of flour. Tripling it needs 7 x 3 = 21 cups.\n\nWorked example: A rectangle is 6 cm wide and 6 cm tall. Its area is 6 x 6 = 36 square centimeters.\n\nPractice: find two everyday examples of sample space\n\nPractice: write one question about probability basics you still have\n\nStudy tip: memorizing steps without understanding the why\n\nChapter summary: Review the worked example before moving on. Next, Probability Basics meets the real world in the chapters ahead. The key terms this chapter were outcome and sample space.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Signature Probability Basics ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: cups, outcome, probability, this, chapter, worked, example, possible");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
