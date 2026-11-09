/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000021 · Basement Of Black Hollow
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="The nursery rhyme shattered, and the thing in the walls laughed. The nursery rhyme glowed faintly, as if it recognized Zecott Dotal. Zecott Dotal understood, all at once, what the nursery rhyme had been trying to say. Years later, in the Marlowe House, they still tell what Zecott Dotal did. Zecott Dotal had never feared this, but the nursery rhyme had chosen, and choice was a kind of gravity.\n\nZecott Dotal packed a small bag and left the Marlowe House without saying goodbye. Every legend agreed on one thing: the nursery rhyme belonged in Grimsby Pines. \"We move at dawn,\" Milia Zetal said. \"The thing in the walls is close.\" Zecott Dotal had never asked for this, but the nursery rhyme had chosen, and choice was a kind of gravity. The radio flickered, and Milia Zetal stopped laughing. Zecott Dotal sacrificed the one thing she could not afford to lose.\n\nZecott Dotal earned another road. \"Hold on,\" Zecott Dotal said, \"and do not look back.\" That evening, Zecott Dotal and Milia Zetal shared a meal under unfamiliar stars. The house was wrong in a way Zecott Dotal could not name. Zecott Dotal dreamed of the Marlowe House, and woke with the nursery rhyme warm in her hands. The summer turned, and with it the fortunes of everyone traveling to Grimsby Pines.\n\nEvery song agreed on one thing: the nursery rhyme belonged in Grimsby Pines. The dark broke, and suddenly there was no more time for doubt. Milia Zetal confessed what she had been carrying all along. They crossed the desert at dawn, tired.\n\nNights on the road were for silence, and Milia Zetal had the best stories. Zecott Dotal had never imagined this, but the nursery rhyme had chosen, and choice was a kind of gravity. And somewhere beyond Grimsby Pines, the sky kept the secret. Every legend agreed on one thing: the nursery rhy…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Basement Of Black Hollow ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: nursery, rhyme, zecott, dotal, milia, thing, grimsby, pines");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
