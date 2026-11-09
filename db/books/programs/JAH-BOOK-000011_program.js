/* JAH interactive demo program — jahdb-demo-1.0
 * Database: books · Record: JAH-BOOK-000011 · Cybersecurity Basics: A Signature Course
 * Text analysis + guided reading of this record's main text field ("chapters[0..1]").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Encryption — scrambling data so only key-holders read it. This idea returns in every chapter, so keep it close.\n\nIn computer science, **firewall** means a barrier filtering network traffic.\n\nIn computer science, **phishing** means fraudulent messages stealing credentials.\n\nIf you remember one thing, remember this: small examples reveal the general rule.\n\nThe big idea: experts in cybersecurity basics return to phishing again and again.\n\nCode sketch — Add two numbers:\na = 11\nb = 10\nprint(a + b)  # prints 110\n\nCode sketch — Count to N:\nfor i in range(1, 8+1):\n    print(i)\n\nRun each sketch mentally, line by line, before moving on.\n\nTry it: find two everyday examples of firewall\n\nYour turn: teach encryption to a friend in one minute\n\nLink forward: everything in this chapter prepares you for Cybersecurity Basics: Going Deeper, where the same ideas get sharper.\n\nFirewall — a barrier filtering network traffic. This idea returns in every chapter, so keep it close.\n\nKey vocabulary: **phishing** (fraudulent messages stealing credentials).\n\nKey vocabulary: **encryption** (scrambling data so only key-holders read it).\n\nThe big idea: firewall connects directly to firewall.\n\nWhat matters most here is patterns matter more than memorized facts.\n\nCode sketch — Find the biggest:\nnums = [7, 3, 6]\nprint(max(nums))  # prints 7\n\nCode sketch — Find the biggest:\nnums = [2, 2, 6]\nprint(max(nums))  # prints 6\n\nRun each sketch mentally, line by line, before moving on.\n\nTry it: compare firewall and firewall in two sentences\n\nYour turn: draw and label a diagram of firewall\n\nStudy tip: memorizing steps without understanding the why\n\nChapter summary: The practice tasks lock in the ideas. Next, Cybersecurity Basics meets the real world in the chapters ahead. Review the worked example before moving on.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Cybersecurity Basics: A Signature Course ===");
console.log("field: chapters[0..1] · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: firewall, sketch, this, idea, chapter, code, line, encryption");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
