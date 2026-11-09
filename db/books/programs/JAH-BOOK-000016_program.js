/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000016 · The A plant-sitting network Playbook
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Every business starts as a sentence. Yours: a plant-sitting network.\n\nWrite the sentence down. Say it to ten people. Watch their faces — confusion means the idea needs sharpening, not abandoning.\n\nThe Signature test: can a twelve-year-old repeat your idea back correctly? If yes, it is clear enough to build.\n\nIdeas are cheap; clarity is the actual product at this stage.\n\nYour customer is not 'everyone'. Name one real person with the problem you solve.\n\nAsk that person what they tried before, what it cost, and what frustrated them.\n\nTen honest conversations beat a hundred guesses. Take notes; patterns will appear by conversation six.\n\nFor a plant-sitting network, the customer is probably closer than you think — start with your own street.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The A plant-sitting network Playbook ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: your, what, sentence, plant-sitting, network, idea, customer, person");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
