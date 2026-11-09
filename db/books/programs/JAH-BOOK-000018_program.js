/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000018 · Stabilizing Ashes
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="In the Sunken Court, children still asked questions about the stabilizing harmful crown. What the stabilizing harmful crown had proven could never quite be measured. In Thistledown Vale, the stabilizing harmful crown would either save everything. Nobody knew which. The Thorn Witch planned, patient as winter. The travelers of the Sunken Court would ask, and Delthon Fasha would tell it true. But the spring after, the rains were kinder, and people noticed.\n\nYears later, in the Sunken Court, they still remember what Delthon Fasha did. Delthon Fasha accepted another road. Shabris Shavane arrived with a warning, breathless and wide-eyed.\n\nThe first test came sooner than anyone expected. Delthon Fasha sacrificed the one thing she could not afford to lose. Delthon Fasha had never imagined this, but the stabilizing harmful crown had chosen, and choice was a kind of gravity. Thorn Witch stood revealed at last, and he was not what the legends had promised.\n\nThe plan was simple: reach Thistledown Vale before the Thorn Witch did. Shabris Shavane knew the sword-forms of the Sunken Court. Delthon Fasha spoke the name and the air listened. The Thorn Lufell scouts darkened the road to Thistledown Vale. Thorn Witch sent an offer that Delthon Fasha could not ignore.\n\nMagic had a sound, and Delthon Vekem was learning it. Delthon Vekem spoke the name and the water listened. In the Sunken Court, children still sang about the stabilizing harmful crown.\n\nDelthon Vekem packed only the essentials and left the Sunken Court without saying goodbye. \"We go at dawn,\" Shabris Tasoul said. \"The Thorn Witch waits for no one.\" The storm lasted all night. And somewhere beyond Thistledown Vale, the wind kept the secret.\n\nIn Thistledown Vale, the stabilizing harmful crown would either doom everything. Nobod…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Stabilizing Ashes ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: delthon, stabilizing, harmful, crown, thorn, witch, sunken, court");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
