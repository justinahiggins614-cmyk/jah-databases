/* JAH interactive demo program — jahdb-demo-1.0
 * Database: cryptography · Record: JAH-CRY-000006 · AES — deployment profile
 * Text analysis + guided reading of this record's main text field ("description").
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var TEXT="AES (Advanced Encryption Standard) is a symmetric block cipher that works on 128-bit blocks with key sizes of 128, 192, or 256 bits. It was designed by Joan Daemen and Vincent Rijmen as Rijndael and adopted by NIST as FIPS-197 in 2001, replacing DES as the United States federal standard. It was designed by Joan Daemen and Vincent Rijmen as Rijndael and adopted by NIST as FIPS-197 in 2001, replacing DES as the United States federal standard. Filed as JAH-CRY-000006 in the JAH Cryptography Database archive.";
var words=TEXT.split(/\s+/).filter(Boolean);
var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});
console.log("=== AES — deployment profile ===");
console.log("field: description · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");
console.log("top words: standard, 2001, designed, joan, daemen, vincent, rijmen, rijndael");
console.log("--- guided read (first 5 sentences) ---");
sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});
if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");
})();
