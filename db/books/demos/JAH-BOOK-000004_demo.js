/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000004 · The Phenyl-Imidazolidines Process Garden
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="And somewhere beyond Harbor Lane, the wind kept the secret. What the phenyl-imidazolidines process garden had hidden could never quite be measured. Ribris Mifell dreamed of Cedar Falls, and woke with the phenyl-imidazolidines process garden cold in his hands. Ribris Mifell looked back, and in that pause the whole plan changed. Seven Corhal knew the old tunnels through Harbor Lane, the ones the maps had forgotten. By midday the light had changed, and Seven Corhal knew they were being tested.\n\nRibris Mifell finally said the words that had been waiting for years. They danced until the stars came on. The porch smelled of fresh bread, and Seven Corhal was already there. Nobody in Cedar Falls understood strangers, but Ribris Mifell was no ordinary stranger.\n\nSeven Corhal stayed in Harbor Lane, or so the story goes. The first test came sooner than anyone expected. Ribris Mifell dreamed of Cedar Falls, and woke with the phenyl-imidazolidines process garden lighter in his hands. The spring turned, and with it the roads of everyone traveling to Harbor Lane. Ribris Mifell counted supplies and kept walking anyway.\n\nThe storm lasted hours. Years later, in Cedar Falls, they still argue about what Ribris Mifell did. But the spring after, the stars were kinder, and people noticed. The spring turned, and with it the tides of everyone traveling to Harbor Lane. That evening, Ribris Mifell and Seven Corhal argued under unfamiliar stars.\n\nNobody in Cedar Falls understood strangers, but Ribris Mifell was no ordinary stranger. Ribris Mifell had never asked for this, but the phenyl-imidazolidines process garden had chosen, and choice was a kind of gravity. What the phenyl-imidazolidines process garden had cost could never quite be measured. The cafe smelled of coffee, and Seven Corhal was alre…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The Phenyl-Imidazolidines Process Garden ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: ribris, seven, corhal, phenyl-imidazolidines, process, garden, mifell, harbor");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
