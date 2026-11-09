/* JAH interactive demo program — jahdb-demo-1.0
 * Database: banking · Record: JAH-BNK-000022 · Auto Loans — Core Overview (Edition 1)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-BNK-000022","title":"Auto Loans — Core Overview (Edition 1)","description":"Auto loans are secured by the vehicle, with terms commonly from 36 to 72 months. The lender can repossess the car on default. This overview edition presents Auto Loans as a core lending concept in mod…","category":"lending","src":"online","spec":{"(object keys)":["instrument","category","lens","edition","how_it_works","key_terms","real_world_use","risk_notes"]}};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Auto Loans — Core Overview (Edition 1) ===");
console.log("Record JAH-BNK-000022 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
