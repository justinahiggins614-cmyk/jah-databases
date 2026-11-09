/* JAH interactive demo program — jahdb-demo-1.0
 * Database: insurance · Record: JAH-INS-0000009 · Universal life insurance
 * Text analysis + guided reading of this record's main text field ("record_text").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="Key points.\nUniversal life insurance. Flexible permanent insurance: adjustable premiums and death benefit around a cash-value account.\n\nIn depth.\nUniversal life separates the insurance cost from the savings element, letting policyholders adjust payments within limits. Interest credited to the cash value varies with market rates, so performance — and the risk of lapse — depends on funding discipline. Educational content only — not financial advice. Consult a licensed insurance professional for your situation.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== Universal life insurance ===");
console.log("field: record_text · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: insurance, universal, life, points, flexible, permanent, adjustable, premiums");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
