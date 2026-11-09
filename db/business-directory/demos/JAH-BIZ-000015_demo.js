/* JAH interactive demo program — jahdb-demo-1.0
 * Database: business-directory · Record: JAH-BIZ-000015 · Summit Holdings Co.
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-BIZ-000015","company_id":"JAH-BIZ-000015","legal_name":"Summit Holdings Co.","title":"Summit Holdings Co.","description":"Summit Holdings Co. is a 201-1000-employee healthcare company based in Boston, USA, founded in 2022.","industry":"healthcare","city":"Boston","country":"USA","employee_band":"201-1000","website":"https://example-15.com","founded_year":2022};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Summit Holdings Co. ===");
console.log("Record JAH-BIZ-000015 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
