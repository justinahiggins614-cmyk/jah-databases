/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000023 · The Energy & Work Guide
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Key vocabulary: **potential energy** (stored energy due to position).\n\nIn physics, **energy** means the capacity to do work.\n\nKey vocabulary: **kinetic energy** (energy of motion).\n\nIf you remember one thing, remember this: the vocabulary is the doorway; walk through it slowly.\n\nWhat matters most here is potential energy connects directly to potential energy.\n\nWorked example: A circuit with 12 V across 10 ohms carries 12/10 = 1.2 amps (Ohm's law).\n\nWorked example: Lifting a 8 kg box 10 meters does 8 x 9.8 x 10 = 784.0 joules of work.\n\nYour turn: find two everyday examples of potential energy\n\nYour turn: draw and label a diagram of potential energy\n\nLink forward: everything in this chapter prepares you for Energy & Work: Going Deeper, where the same ideas get sharper.\n\nPotential energy — stored energy due to position. This idea returns in every chapter, so keep it close.\n\nKinetic energy — energy of motion. This idea returns in every chapter, so keep it close.\n\nEnergy — the capacity to do work. This idea returns in every chapter, so keep it close.\n\nThe big idea: potential energy connects directly to potential energy.\n\nThe big idea: patterns matter more than memorized facts.\n\nWorked example: A 6 kg cart pushed with 10 N accelerates at 10/6 = 1.67 m/s^2 (F = ma).\n\nWorked example: A 6 kg cart pushed with 3 N accelerates at 3/6 = 0.5 m/s^2 (F = ma).\n\nPractice: find two everyday examples of potential energy\n\nTry it: write one question about energy & work you still have\n\nStudy tip: skipping the worked examples\n\nChapter summary: Review the worked example before moving on. The practice tasks lock in the ideas. Energy & Work builds on Energy & Work.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The Energy & Work Guide ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: energy, potential, work, worked, this, example, chapter, idea");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
