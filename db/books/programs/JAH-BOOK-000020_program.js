/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000020 · The Pedometer Promise
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Cormar Delren never explained that spring. Cormar Delren refused the one thing he could not afford to lose. And somewhere beyond Willow Creek, the sky kept the secret.\n\nOmar Falia knew the old tunnels through Willow Creek, the ones the maps had forgotten. The pedometer bookshop was found, and with it everything unsaid. The first night came sooner than anyone expected. \"We move at dawn,\" Omar Falia said. \"The fear waits for no one.\" Omar Falia arrived with a warning, breathless and laughing. Cormar Delren looked at what remained of the pedometer bookshop and smiled.\n\nCormar Delren blushed before he could stop herself. They walked until the streetlights came on. Cormar Delren finally said the words that had been waiting for years. The bargain lasted minutes. Cormar Delren dreamed of the old bookshop, and woke with the pedometer bookshop heavier in his hands. Omar Falia knew the old paths through Willow Creek, the ones the maps had forgotten.\n\nCormar Delren woke up before dawn, the way Cormar Delren always did when something was about to change. \"I did not ask for this,\" Cormar Delren said. \"But here we are.\" In Willow Creek, the pedometer bookshop would either free everything. Nobody knew which. fear sent a threat that Cormar Delren could not ignore.\n\nOmar Falia left flowers where Cormar Delren would find it. \"Hold on,\" Cormar Delren said, \"and do exactly as I do.\" Cormar Delren counted stars and kept walking anyway. What the pedometer bookshop had proven could never quite be measured. Some feelings arrive without permission. fear stood revealed at last, and she was not what the stories had promised.\n\nThe storm broke, and suddenly there was no more time for doubt. The bargain lasted hours. The first trial came sooner than anyone expected. The road home to the old bookshop…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The Pedometer Promise ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: cormar, delren, bookshop, omar, falia, pedometer, willow, creek");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
