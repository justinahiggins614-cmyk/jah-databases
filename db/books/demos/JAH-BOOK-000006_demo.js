/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000006 · Ratios & Proportions: A Signature Course
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="In mathematics, **proportion** means an equation stating two ratios are equal.\n\nKey vocabulary: **ratio** (a comparison of two quantities).\n\nKey vocabulary: **unit rate** (a ratio comparing a quantity to one unit of another).\n\nThe big idea: proportion connects directly to unit rate.\n\nThe big idea: patterns matter more than memorized facts.\n\nWorked example: A car drives 5 km in 3 hours, a speed of 5/3 = 1.67 km/h.\n\nWorked example: Maya has 4 apples and gives away 3. She has 4 - 3 = 1 apples left.\n\nTry it: compare proportion and unit rate in two sentences\n\nPractice: teach proportion to a friend in one minute\n\nLink forward: everything in this chapter prepares you for Ratios & Proportions: Going Deeper, where the same ideas get sharper.\n\nKey vocabulary: **proportion** (an equation stating two ratios are equal).\n\nRatio — a comparison of two quantities. This idea returns in every chapter, so keep it close.\n\nUnit rate — a ratio comparing a quantity to one unit of another. This idea returns in every chapter, so keep it close.\n\nIf you remember one thing, remember this: the vocabulary is the doorway; walk through it slowly.\n\nThe big idea: the vocabulary is the doorway; walk through it slowly.\n\nWorked example: Maya has 10 apples and gives away 2. She has 10 - 2 = 8 apples left.\n\nWorked example: A car drives 3 km in 2 hours, a speed of 3/2 = 1.5 km/h.\n\nPractice: explain proportion in your own words\n\nYour turn: explain proportion in your own words\n\nCommon mistake: skipping the worked examples\n\nChapter summary: Ratios & Proportions builds on Ratios & Proportions. Review the worked example before moving on. The practice tasks lock in the ideas.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Ratios & Proportions: A Signature Course ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: proportion, unit, worked, ratios, vocabulary, idea, example, ratio");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
