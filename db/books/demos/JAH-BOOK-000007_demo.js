/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000007 · Understanding Electricity Basics
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Key vocabulary: **current** (the flow of electric charge).\n\nIn physics, **voltage** means the push that drives current.\n\nResistance — opposition to current flow. This idea returns in every chapter, so keep it close.\n\nIf you remember one thing, remember this: the vocabulary is the doorway; walk through it slowly.\n\nWhat matters most here is small examples reveal the general rule.\n\nWorked example: A runner covers 11 meters in 9 seconds: speed = 11/9 = 1.22 m/s.\n\nWorked example: A wave with frequency 7 Hz and wavelength 5 m travels at 7 x 5 = 35 m/s.\n\nYour turn: teach current to a friend in one minute\n\nTry it: explain current in your own words\n\nLink forward: everything in this chapter prepares you for Electricity Basics: Going Deeper, where the same ideas get sharper.\n\nCurrent — the flow of electric charge. This idea returns in every chapter, so keep it close.\n\nVoltage — the push that drives current. This idea returns in every chapter, so keep it close.\n\nResistance — opposition to current flow. This idea returns in every chapter, so keep it close.\n\nThe big idea: current connects directly to resistance.\n\nThe big idea: each new idea builds on the last one.\n\nWorked example: A wave with frequency 3 Hz and wavelength 7 m travels at 3 x 7 = 21 m/s.\n\nWorked example: A circuit with 11 V across 3 ohms carries 11/3 = 3.67 amps (Ohm's law).\n\nYour turn: find two everyday examples of resistance\n\nTry it: explain current in your own words\n\nStudy tip: rushing past the vocabulary — learn the words first\n\nChapter summary: Review the worked example before moving on. The key terms this chapter were current and resistance. The practice tasks lock in the ideas.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Understanding Electricity Basics ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: current, this, idea, chapter, resistance, worked, example, flow");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
