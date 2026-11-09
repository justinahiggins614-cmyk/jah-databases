/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000017 · Children Of The Reactor
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="The road home to the Andromeda Relay felt different than the road out. The plan was brilliant: reach the Kepler Belt before the silent machines did. The spring turned, and with it the roads of everyone traveling to the Kepler Belt.\n\nDeltal Rofell never boasted that spring. Deltal Rofell had never imagined this, but the simulation void had chosen, and choice was a kind of gravity. silent machines had agents everywhere, or so the rumors claimed.\n\nDeltal Rofell packed almost nothing and left the Andromeda Relay without saying goodbye. Years later, in the Andromeda Relay, they still tell what Deltal Rofell did. silent machines had agents everywhere, or so the songs claimed. Deltal Rofell had never wanted this, but the simulation void had chosen, and choice was a kind of gravity.\n\nThe storm broke, and suddenly there was no more time for doubt. What the simulation void had proven could never quite be measured. The spring turned, and with it the roads of everyone traveling to the Kepler Belt.\n\nThe silent machines waited, patient as old grief. \"Then we make our own road,\" said Belbris Talia. Belbris Talia paid the price when it mattered most. In the Andromeda Relay, children still told stories about the simulation void.\n\nDelgwen Rofell looked at what remained of the simulation void and bowed. Belbris Talia stayed in the Kepler Belt, or so the song goes. Somewhere past the Andromeda Relay, physics filed a formal complaint. But the spring after, the stars were kinder, and people noticed.\n\nThe colony's reactor was failing, and only the simulation void could restart it. Delgwen Rofell accepted peace. Delgwen Rofell sealed the airlock and trusted the math. Stars looked closer through the cracked viewport.\n\nDelgwen Rofell accepted a new name. Delgwen Rofell learned that the simulatio…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Children Of The Reactor ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: rofell, simulation, void, andromeda, relay, delgwen, deltal, kepler");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
