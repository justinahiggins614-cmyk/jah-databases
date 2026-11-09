/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000008 · Ares — Gods, heroes, and monsters
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Ares is the brutal god of war, loathed by the other Olympians. The Romans remade him as Mars, a far more honored figure.\n\nMyths are carried by persons — gods who are larger than human, heroes who are almost, monsters who embody what must be faced. In Ares, each figure plays a role that reveals what the culture feared, honored, and desired. Viewed through a cultural lens, Ares is examined as a people's self-portrait — the values and fears it encodes.\n\nThe figures of Ares outlive their religion: they become metaphors the whole world now uses. A second sub-question concerns the historical kernel: what real events or places might stand behind Ares. Related entries in this archive: Ganesha and Tuatha De Danann.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Ares — Gods, heroes, and monsters ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: ares, what, honored, figure, brutal, loathed, other, olympians");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
