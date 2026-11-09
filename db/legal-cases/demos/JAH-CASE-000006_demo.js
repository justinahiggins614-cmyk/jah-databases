/* JAH interactive demo program — jahdb-demo-1.0
 * Database: legal-cases · Record: JAH-CASE-000006 · Holloway v. Upton
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CASE-000006","case_id":"JAH-CASE-000006","case_name":"Holloway v. Upton","title":"Holloway v. Upton","description":"The court partitioned the parcel between Holloway and Upton, ordering sale and an equal division of proceeds.","court":"U.S. Court of Appeals","jurisdiction":"Georgia","decision_date":"2015-01-26","case_type":"property","holding_summary":"The court partitioned the parcel between Holloway and Upton, ordering sale and an equal division of proceeds.","citations":"[array ×1]","judges":"[array ×1]"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Holloway v. Upton ===");
console.log("Record JAH-CASE-000006 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
