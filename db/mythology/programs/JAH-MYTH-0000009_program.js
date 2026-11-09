/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000009 · Aphrodite — Gods, heroes, and monsters
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Aphrodite, goddess of love and beauty, was born from sea foam according to Hesiod. Her judgment of Paris sparked the Trojan War.\n\nMyths are carried by persons — gods who are larger than human, heroes who are almost, monsters who embody what must be faced. In Aphrodite, each figure plays a role that reveals what the culture feared, honored, and desired. Viewed through a contemporary-relevance lens, Aphrodite is brought into the present, where its patterns still appear in new clothes.\n\nThe figures of Aphrodite outlive their religion: they become metaphors the whole world now uses. One fruitful sub-question is which telling of Aphrodite is oldest, and how the tale changed in transmission. Related entries in this archive: Tanabata and Hanuman.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Aphrodite — Gods, heroes, and monsters ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: aphrodite, what, goddess, love, beauty, born, from, foam");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
