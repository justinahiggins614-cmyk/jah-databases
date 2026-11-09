/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000024 · The World of Solutions & Mixtures
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Concentration — the amount of solute per unit of solution. This idea returns in every chapter, so keep it close.\n\nSolubility — how much solute dissolves in a solvent. This idea returns in every chapter, so keep it close.\n\nIn chemistry, **solution** means a uniform mixture of solute and solvent.\n\nThe big idea: the vocabulary is the doorway; walk through it slowly.\n\nWhat matters most here is concentration connects directly to concentration.\n\nWorked example: Vinegar (pH ~3) is 10000 times more acidic than pure water (pH 7).\n\nWorked example: Mixing 11 g of salt into 11 g of water makes a solution of about 50.0% concentration.\n\nYour turn: compare concentration and concentration in two sentences\n\nTry it: write one question about solutions & mixtures you still have\n\nLink forward: everything in this chapter prepares you for Solutions & Mixtures: Going Deeper, where the same ideas get sharper.\n\nIn chemistry, **concentration** means the amount of solute per unit of solution.\n\nSolution — a uniform mixture of solute and solvent. This idea returns in every chapter, so keep it close.\n\nSolubility — how much solute dissolves in a solvent. This idea returns in every chapter, so keep it close.\n\nThe big idea: patterns matter more than memorized facts.\n\nThe big idea: patterns matter more than memorized facts.\n\nWorked example: Water forms when 12 hydrogen atoms join 7 oxygen atom: 12H + 7O -> H12O7, balanced as 2H2 + O2 -> 2H2O.\n\nWorked example: Vinegar (pH ~3) is 10000 times more acidic than pure water (pH 7).\n\nYour turn: write one question about solutions & mixtures you still have\n\nTry it: find two everyday examples of concentration\n\nWatch out: confusing similar-sounding terms — compare them side by side\n\nChapter summary: Solutions & Mixtures builds on Solutions & Mixtures. Review the wor…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The World of Solutions & Mixtures ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: concentration, idea, chapter, solute, this, solution, worked, example");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
