/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000009 · Plants & Photosynthesis: A Signature Course
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Stoma — a leaf pore controlling gas exchange. This idea returns in every chapter, so keep it close.\n\nChlorophyll — the green pigment capturing light. This idea returns in every chapter, so keep it close.\n\nPhotosynthesis — plants converting light to sugar. This idea returns in every chapter, so keep it close.\n\nIf you remember one thing, remember this: each new idea builds on the last one.\n\nThe big idea: small examples reveal the general rule.\n\nWorked example: The human heart beats about 9 times per day: 9 x 60 x 24 / 1000 = 12 thousand beats.\n\nWorked example: A forest of 7 hectares can hold roughly 7 x 400 = 2800 trees.\n\nTry it: find two everyday examples of stoma\n\nYour turn: teach stoma to a friend in one minute\n\nLink forward: everything in this chapter prepares you for Plants & Photosynthesis: Going Deeper, where the same ideas get sharper.\n\nKey vocabulary: **chlorophyll** (the green pigment capturing light).\n\nIn biology, **photosynthesis** means plants converting light to sugar.\n\nIn biology, **stoma** means a leaf pore controlling gas exchange.\n\nWhat matters most here is each new idea builds on the last one.\n\nWhat matters most here is patterns matter more than memorized facts.\n\nWorked example: A human body has about 9 trillion cells working together as one organism.\n\nWorked example: The human heart beats about 10 times per day: 10 x 60 x 24 / 1000 = 14 thousand beats.\n\nYour turn: write one question about plants & photosynthesis you still have\n\nPractice: find two everyday examples of stoma\n\nCommon mistake: rushing past the vocabulary — learn the words first\n\nChapter summary: Next, Plants & Photosynthesis meets the real world in the chapters ahead. Review the worked example before moving on. The key terms this chapter were chlorophyll and stoma.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Plants & Photosynthesis: A Signature Course ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: stoma, this, idea, chapter, photosynthesis, plants, worked, example");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
