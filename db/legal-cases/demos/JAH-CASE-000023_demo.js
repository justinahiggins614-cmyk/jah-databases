/* JAH interactive demo program — jahdb-demo-1.0
 * Database: legal-cases · Record: JAH-CASE-000023 · Marlowe v. Thackeray
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CASE-000023","case_id":"JAH-CASE-000023","case_name":"Marlowe v. Thackeray","title":"Marlowe v. Thackeray","description":"The court found the liquidated-damages clause enforceable as a reasonable forecast of loss, and entered judgment for Thackeray.","court":"U.S. Court of Appeals","jurisdiction":"Florida","decision_date":"2017-07-27","case_type":"contract","holding_summary":"The court found the liquidated-damages clause enforceable as a reasonable forecast of loss, and entered judgment for Thackeray.","citations":"[array ×1]","judges":"[array ×2]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Marlowe v. Thackeray ===");
console.log("Record JAH-CASE-000023 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
