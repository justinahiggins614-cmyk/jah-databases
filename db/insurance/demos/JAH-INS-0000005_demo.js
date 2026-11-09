/* JAH interactive demo program — jahdb-demo-1.0
 * Database: insurance · Record: JAH-INS-0000005 · Whole life insurance
 * Text analysis + guided reading of this record's main text field ("record_text").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Key points.\nWhole life insurance. Permanent coverage with level premiums, a cash value that grows, and dividends possible from mutual insurers.\n\nIn depth.\nWhole life covers you for life as long as premiums are paid. Part of each premium funds the death benefit; part builds cash value that grows tax-deferred and can be borrowed against. Premiums are much higher than term for the same death benefit. Educational content only — not financial advice. Consult a licensed insurance professional for your situation.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Whole life insurance ===");
console.log("field: record_text · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: life, premiums, whole, insurance, cash, value, that, grows");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
