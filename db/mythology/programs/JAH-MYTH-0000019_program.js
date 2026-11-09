/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mythology · Record: JAH-MYTH-0000019 · Achilles — The tale itself
 * Text analysis + guided reading of this record's main text field ("body").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Achilles, the Iliad's greatest warrior, chose a short glorious life over long obscurity. His heel was his only vulnerability, giving us the 'Achilles heel.'\n\nEvery myth deserves to be heard as story first. Achilles unfolds with its own logic — characters acting from motives the myth takes for granted, events following one another with dreamlike necessity. To know Achilles is to be able to tell it. Viewed through a symbolic lens, Achilles is read for its images — what each figure and object stands for beneath the plot.\n\nThe story is the data. All interpretation comes after, and must answer to the tale as told. A third sub-question asks how Achilles was visualized — in vase painting, sculpture, or temple relief. Related entries in this archive: Raijin and Fujin and Perseus.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Achilles — The tale itself ===");
console.log("field: body · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: achilles, myth, story, with, iliad's, greatest, warrior, chose");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
