/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000010 · Primary Sources & Evidence: People and Events
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Bias — a slant shaping how evidence is presented. This idea returns in every chapter, so keep it close.\n\nPrimary source — firsthand evidence from the time. This idea returns in every chapter, so keep it close.\n\nIn history, **corroboration** means checking claims against multiple sources.\n\nThe big idea: the vocabulary is the doorway; walk through it slowly.\n\nIf you remember one thing, remember this: the vocabulary is the doorway; walk through it slowly.\n\nTimeline note: The steam engine's improvements by James Watt (1776) powered the Industrial Revolution.\n\nTimeline note: The Roman Empire at its height (c. 117 CE) ringed the Mediterranean Sea.\n\nPractice: compare bias and corroboration in two sentences\n\nTry it: write one question about primary sources & evidence you still have\n\nLink forward: everything in this chapter prepares you for Primary Sources & Evidence: Going Deeper, where the same ideas get sharper.\n\nIn history, **bias** means a slant shaping how evidence is presented.\n\nIn history, **primary source** means firsthand evidence from the time.\n\nIn history, **corroboration** means checking claims against multiple sources.\n\nWhat matters most here is small examples reveal the general rule.\n\nWhat matters most here is the vocabulary is the doorway; walk through it slowly.\n\nTimeline note: The Silk Road linked China to the Mediterranean for over a thousand years.\n\nTimeline note: In 1492, Columbus reached the Americas, beginning sustained European contact.\n\nTry it: explain bias in your own words\n\nYour turn: teach bias to a friend in one minute\n\nStudy tip: skipping the worked examples\n\nChapter summary: The key terms this chapter were bias and corroboration. Review the worked example before moving on. Primary Sources & Evidence builds on Primary Sources & Evidence.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Primary Sources & Evidence: People and Events ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: evidence, bias, primary, sources, this, chapter, history, corroboration");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
