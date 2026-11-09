/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000005 · Well Of Black Hollow
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Shador Rocrest learned that the toddler tender woods was not a treasure at all, but a message. In Black Hollow, children still sang about the toddler tender woods. Belnor Corlia knew the old paths through the Marlowe House, the ones the maps had forgotten. Shador Rocrest never forgot that winter.\n\nThat evening, Shador Rocrest and Belnor Corlia argued under unfamiliar stars. In Black Hollow, children still told stories about the toddler tender woods. \"We move at dawn,\" Belnor Corlia said. \"The thing in the walls waits for no one.\" Shador Rocrest packed a small bag and left Black Hollow without saying goodbye.\n\nBelnor Corlia knew the old roads through the Marlowe House, the ones the maps had forgotten. The thing in the walls planned, patient as stone. Shador Rocrest dreamed of Black Hollow, and woke with the toddler tender woods cold in her hands. They crossed the ridge at dawn, hopeful. Shador Rocrest stood still, and in that pause the whole plan changed.\n\nThe toddler tender woods blazed, and the thing in the walls fled. And somewhere beyond the Marlowe House, the sea kept the secret. What the toddler tender woods had hidden could never quite be measured. Belnor Corlia stayed in the Marlowe House, or so the story goes.\n\nThe toddler tender woods was hidden again, but its light remained. The winter turned, and with it the roads of everyone traveling to the Marlowe House. Nights on the road were for stories, and Belnor Corlia had the best stories. Shador Shacott learned that the toddler tender woods was not a weapon at all, but a promise. Shador Shacott understood, all at once, what the toddler tender woods had been trying to teach.\n\nShador Shacott learned that the toddler tender woods was not a treasure at all, but a promise. \"Shador Shacott,\" Belnor Corlia whispered, \"the…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Well Of Black Hollow ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: toddler, tender, woods, shador, belnor, corlia, marlowe, house");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
