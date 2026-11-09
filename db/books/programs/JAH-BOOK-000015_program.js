/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000015 · On Justice: A Short Philosophy
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Everyone uses the word 'justice', but few stop to ask what it means.\n\nThis book is a slow walk around justice: looking at it from several sides, testing each view, and leaving you with better questions than you started with.\n\nWe begin with the ordinary sense of 'justice' — how the word works in daily life — because philosophy that cannot touch ordinary life is only decoration. We will test our ideas against a real case along the way: Based on JAH-SPEC-395086.\n\nThe Mystic'S View holds that justice is best understood through what it does for us.\n\nIts strongest argument: it makes sense of our feelings about justice.\n\nIts hardest objection: it proves too much — or too little.\n\nHold both the argument and the objection in mind. justice deserves that much patience.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== On Justice: A Short Philosophy ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: justice, with, that, word, 'justice', what, view, ordinary");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
