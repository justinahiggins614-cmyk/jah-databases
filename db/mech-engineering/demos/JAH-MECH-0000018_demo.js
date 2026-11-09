/* JAH interactive demo program — jahdb-demo-1.0
 * Database: mech-engineering · Record: JAH-MECH-0000018 · Property Class 5.6 Hex Bolt — Tolerances
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"mech_id":"JAH-MECH-0000018","category":"components","component":"Property Class 5.6 Hex Bolt","material":"low/medium-carbon steel","properties":{"(object keys)":["UTS","yield","material","marking"]},"source":"online","source_ref":{"(object keys)":["authority","url"]},"title":"Property Class 5.6 Hex Bolt — Tolerances","record_type":"tolerance-class","description":"Tolerance practice for Property Class 5.6 Hex Bolt: External threads 6g, nuts 6H; grip length at least one diameter.","tolerances":{"(object keys)":["note"]},"standards":"[array ×1]","id":"JAH-MECH-0000018"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Property Class 5.6 Hex Bolt — Tolerances ===");
console.log("Record JAH-MECH-0000018 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
