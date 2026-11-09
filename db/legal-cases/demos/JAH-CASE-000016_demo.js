/* JAH interactive demo program — jahdb-demo-1.0
 * Database: legal-cases · Record: JAH-CASE-000016 · Bennett v. Zimmerman
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CASE-000016","case_id":"JAH-CASE-000016","case_name":"Bennett v. Zimmerman","title":"Bennett v. Zimmerman","description":"The court quieted title in favor of Zimmerman, finding the chain of deeds unbroken and Bennett’s adverse-possession claim unsupported by continuous use.","court":"U.S. Court of Appeals","jurisdiction":"Illinois","decision_date":"2015-12-15","case_type":"property","holding_summary":"The court quieted title in favor of Zimmerman, finding the chain of deeds unbroken and Bennett’s adverse-possession claim unsupported by continuous use.","citations":"[array ×2]","judges":"[array ×1]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Bennett v. Zimmerman ===");
console.log("Record JAH-CASE-000016 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
