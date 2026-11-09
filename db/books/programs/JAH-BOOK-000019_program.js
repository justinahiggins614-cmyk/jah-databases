/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000019 · Inheritance At Ferry Terminal Nine
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="The road to Grimshaw Lane was forgotten, and the summer made it worse. Migwen Fenwick held the line when it mattered most. Everyone at Ferry Terminal Nine had a secret. \"Remember,\" Nawick Nagwen said, \"then run.\" Nawick Nagwen counted steps and kept walking anyway.\n\nThe bargain lasted minutes. At the gate of Grimshaw Lane, they were recognized. In Blackwood Manor, children still sang about the chief telegram. The silence broke, and suddenly there was no more time for doubt. The chief telegram was hidden again, but its lesson remained. Nawick Nagwen counted stars and kept walking anyway.\n\nThat evening, Nawick Nagwen and Migwen Fenwick talked late under unfamiliar stars. Nawick Nagwen stepped forward, and in that pause the whole plan changed. Years later, in Blackwood Manor, they still argue about what Nawick Nagwen did. They crossed the river at dawn, singing. By midday the light had changed, and Migwen Fenwick knew they were being followed. blackmailer sent a threat that Nawick Nagwen could not ignore.\n\nIn Grimshaw Lane, the chief telegram would either change everything. Nobody knew which. What Migwen Fenwick had not told Nawick Nagwen was the secret of the chief telegram. The plan was fragile: reach Grimshaw Lane before the blackmailer did.\n\nNobody in Blackwood Manor believed strangers, but Nawick Nagwen was no ordinary stranger. What the chief telegram had hidden could never quite be measured. Nawick Nagwen packed a small bag and left Blackwood Manor without saying goodbye. Nawick Nagwen rose before dawn, the way Nawick Nagwen always did when something was about to change. Nawick Nagwen noticed what was too clean about the desk. The dark broke, and suddenly there was no more time for doubt.\n\nAt the gate of Grimshaw Lane, they were welcomed. What the chief telegram had…";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Inheritance At Ferry Terminal Nine ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: nagwen, nawick, grimshaw, lane, migwen, hallith, chief, telegram");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
