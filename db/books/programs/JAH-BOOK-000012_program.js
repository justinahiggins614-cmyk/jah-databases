/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000012 · A Song for Puddle the duckling
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Puddle the duckling woke up wiggly on a breezy morning. \"Good morning!\" called Nixie the newt. \"Puddle the duckling, you came!\" And guess what? It was fun! The sun peeked, and the bees danced. \"I believe in you,\" said Nixie the newt, and Puddle the duckling took a deep breath. Puddle the duckling felt sad for a moment. Today was the day Puddle the duckling would visit the giggling brook.\n\nNixie the newt was already there, giggling. They shared the load. That evening, Puddle the duckling learned that patience brings sweet berries. \"Good morning!\" called Nixie the newt. \"Puddle the duckling, you came!\" Puddle the duckling smiled and dreamed of the giggling brook. \"I believe in you,\" said Nixie the newt, and Puddle the duckling took a deep breath. Puddle the duckling found a feather and showed Nixie the newt.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== A Song for Puddle the duckling ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: puddle, duckling, nixie, newt, morning, giggling, good, called");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
