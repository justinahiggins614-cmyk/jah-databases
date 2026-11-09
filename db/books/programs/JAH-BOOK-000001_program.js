/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000001 · Echoes Of The Nebula
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="The plan was fragile: reach the Kepler Belt before the void-born did. Every map agreed on one thing: the variant beacon belonged in the Kepler Belt. By midday the wind had changed, and Owick Rogwen knew they were being watched. The variant beacon had been lost for years, and everyone in the Helios Array knew the stories.\n\nThe void-born communicated in static, and Owick Rogwen was learning to read it. void-born sent a threat that Dovane Corwick could not ignore. \"I did not choose this,\" Dovane Corwick said. \"Yet here we are.\" The variant beacon pulsed faintly, as if it recognized Dovane Corwick. The skeptics of the Helios Array would ask, and Dovane Corwick would tell it true. Dovane Corwick looked at what remained of the variant beacon and bowed. That evening, Dovane Corwick and Owick Rogwen argued under unfamiliar stars.\n\nBy midday the sky had changed, and Owick Rogwen knew they were being watched. Shipboard time behaved strangely near the variant beacon. Dovane Corwick sealed the hatch and trusted the math. Owick Rogwen stayed in the Kepler Belt, or so the song goes.\n\nDawn came soft over the Kepler Belt, and it was over. Dovane Corwick earned peace. Nights on the road were for watching the sky, and Owick Rogwen had the best stories. Nobody in the Helios Array believed strangers, but Dovane Corwick was no ordinary stranger. Owick Rogwen knew the old songs through the Kepler Belt, the ones the maps had forgotten. The battle lasted all night.\n\nRicott Corwick learned that the variant beacon was not a tool at all, but a mirror. Nights on the road were for stories, and Owick Rogwen had the best stories. Ricott Corwick packed little and left the Helios Array without saying goodbye. The variant beacon went quiet, and the void-born fled. Ricott Corwick sealed the bulkhead and …";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Echoes Of The Nebula ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: corwick, variant, beacon, owick, rogwen, ricott, dovane, kepler");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
