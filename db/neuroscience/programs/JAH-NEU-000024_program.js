/* JAH interactive demo program — jahdb-demo-1.0
 * Database: neuroscience · Record: JAH-NEU-000024 · The case of Phineas Gage: overview (R-10024)
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-NEU-000024","title":"The case of Phineas Gage: overview (R-10024)","description":"The case of Phineas Gage is a historical case of the nervous system. First described in 1848. Its role: an 1848 railroad accident drove an iron rod through his frontal lobe, changing his personality a…","category":"brain-development","spec":{"(object keys)":["subject","subject_type","category","function","key_fact","associated","year","aspect"]},"src":"online"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== The case of Phineas Gage: overview (R-10024) ===");
console.log("Record JAH-NEU-000024 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
