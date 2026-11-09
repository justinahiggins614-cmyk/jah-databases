/* JAH interactive demo program — jahdb-demo-1.0
 * Database: business-directory · Record: JAH-BIZ-000014 · Summit Trading Ltd.
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-BIZ-000014","company_id":"JAH-BIZ-000014","legal_name":"Summit Trading Ltd.","title":"Summit Trading Ltd.","description":"Summit Trading Ltd. is a 51-200-employee retail company based in Chicago, USA, founded in 2001.","industry":"retail","city":"Chicago","country":"USA","employee_band":"51-200","website":"https://example-14.com","founded_year":2001};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Summit Trading Ltd. ===");
console.log("Record JAH-BIZ-000014 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
