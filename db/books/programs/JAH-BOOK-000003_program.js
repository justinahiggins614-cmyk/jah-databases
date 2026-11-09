/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000003 · The Research Will Affair
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Zeven Seven stayed in the Harborside Hotel, or so the song goes. Lusha Ribris packed a small bag and left Grimshaw Lane without saying goodbye. Dawn came cold over the Harborside Hotel, and it was over. Zeven Seven arrived with a warning, breathless and wide-eyed. Lusha Ribris noticed what was moved about the scene.\n\nThe blackmailer listened, patient as old grief. blackmailer stood revealed at last, and she was not what the legends had promised. Lusha Ribris looked at what remained of the phoenix ledger and bowed. At the border of the Harborside Hotel, they were recognized. Zeven Seven kept the files in chronological order. Lusha Ribris noticed what was missing about the room.\n\nLusha Ribris chose the one thing she could not afford to lose. Lusha Ribris rose before dawn, the way Lusha Ribris always did when something was about to change. The blackmailer had been clever, but not careful enough. The plan was simple: reach the Harborside Hotel before the blackmailer did.\n\nLusha Halnor refused peace. But the autumn after, the harvest were kinder, and people noticed. The dark broke, and suddenly there was no more time for doubt. Nobody in Grimshaw Lane understood strangers, but Lusha Halnor was no ordinary stranger. Every song agreed on one thing: the phoenix ledger belonged in the Harborside Hotel. Everyone at Blackwood Manor had a reason.\n\nWhat the phoenix ledger had given could never quite be measured. The blackmailer waited, patient as winter. Lusha Halnor never regretted that autumn. The autumn turned, and with it the fortunes of everyone traveling to the Harborside Hotel. Zemar Winmar revealed what she had been carrying all along.\n\nIn Grimshaw Lane, children still told stories about the phoenix ledger. The phoenix ledger was restored, but its echo remained. Three suspec…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== The Research Will Affair ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: lusha, halnor, harborside, hotel, what, blackmailer, phoenix, ledger");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
