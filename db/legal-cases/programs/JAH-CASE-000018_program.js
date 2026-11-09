/* JAH interactive demo program — jahdb-demo-1.0
 * Database: legal-cases · Record: JAH-CASE-000018 · Sutton v. Osgood
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CASE-000018","case_id":"JAH-CASE-000018","case_name":"Sutton v. Osgood","title":"Sutton v. Osgood","description":"The court affirmed the conviction, holding that the evidence viewed in the light most favorable to the state proved every element beyond a reasonable doubt.","court":"U.S. Supreme Court","jurisdiction":"Colorado","decision_date":"2021-09-06","case_type":"criminal","holding_summary":"The court affirmed the conviction, holding that the evidence viewed in the light most favorable to the state proved every element beyond a reasonable doubt.","citations":"[array ×2]","judges":"[array ×2]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Sutton v. Osgood ===");
console.log("Record JAH-CASE-000018 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
