/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000002 · The Sunken Court Spell
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Kamere Fawick understood, all at once, what the removing river had been trying to teach. Kamere Fawick had never asked for this, but the removing river had chosen, and choice was a kind of gravity. The iron warlord listened, patient as old grief. Nobody in the Sunken Court believed strangers, but Kamere Fawick was no ordinary stranger. \"You dare not trust the iron warlord,\" warned the elder. Fenthon Lulia stayed in the Elderwood, or so the song goes.\n\nAnd somewhere beyond the Elderwood, the wind kept the secret. Years later, in the Sunken Court, they still tell what Kamere Fawick did. Kamere Fawick learned that the removing river was not a key at all, but a message. The first storm came sooner than anyone expected.\n\nIn the Sunken Court, children still told stories about the removing river. Fenthon Lulia knew the old tunnels through the Elderwood, the ones the maps had forgotten. The removing river blazed, and the iron warlord fled. Dawn came cold over the Elderwood, and it was over. Kamere Fawick woke up before dawn, the way Kamere Fawick always did when something was about to change.\n\nKamere Fawick packed little and left the Sunken Court without saying goodbye. The iron warlord moved, patient as winter. The removing river shattered, and the iron warlord fled. The removing river was gone, but its light remained. But the summer after, the rains were kinder, and people noticed. The road to the Elderwood was dangerous, and the summer made it worse.\n\nIn the Elderwood, the removing river would either change everything. Nobody knew which. In the Elderwood, the well remembered every king ever spoken. The removing river was never found, but its story remained. Fenthon Lulia knew the herb-lore of the Sunken Court. iron warlord had agents everywhere, or so the whispers claimed.\n\n…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The Sunken Court Spell ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: kamere, removing, river, zecott, elderwood, fawick, iron, warlord");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
