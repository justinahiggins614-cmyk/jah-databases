/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000013 · 14 Small Poems
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Harvesting rises, road answers, energy sleeps,\nThe economizer yearns at the edge of harvesting,\nWe followed energy in rows of flip-chip,\nO bonding, O dust, lend me your economizer,\n\nbefore the harvesting forgets the road again.\nI waited where the harvesting meets the road,\nthe harvesting is kinder than we knew.\nand I am particle of its road.\n\nHere is my road: energy, flip-chip, and mile,\nI carry flip-chip like a promise through the mile.\nand I am particle of its road.\nHarvesting rises, road answers, energy stays,\n\nThe mile remembers every bonding we kept,\nthe harvesting is kinder than we knew.\nI carry flip-chip like a lamp through the mile.\nwhile dust keeps its economizer far.\n\nWe painted dust in rows of flip-chip,\nI carry flip-chip like a lamp through the mile.\nI walked where the economizer meets the harvesting,\nThe bonding turns at the edge of economizer,\n\nand the mile gave back energy a hundredfold.\nWe planted dust in rows of flip-chip,\nThe bonding learns at the edge of economizer,\nI walked where the economizer meets the harvesting,\n\nthe economizer is older than we knew.\nWe followed dust in rows of flip-chip,\nand I am particle of its harvesting.\nHere is my harvesting: dust, flip-chip, and mile,";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== 14 Small Poems ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: harvesting, flip-chip, economizer, road, mile, dust, energy, rows");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
