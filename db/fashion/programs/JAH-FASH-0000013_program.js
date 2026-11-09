/* JAH interactive demo program — jahdb-demo-1.0
 * Database: fashion · Record: JAH-FASH-0000013 · Signature fit block: Moonlit atelier
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"sizing","source":"signature","creation_mode":"SIGNATURE-GENERATED","title":"Signature fit block: Moonlit atelier","topic":"fit block","garment":{"(object keys)":["block","chest_in","waist_in"]},"description":"A Signature-generated fit block named Moonlit atelier with a 32in chest and 26in waist. An original sizing study by the JAH generator. Filed as a complete searchable record in the JAH Data Bases archi…","id":"JAH-FASH-0000013"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Signature fit block: Moonlit atelier ===");
console.log("Record JAH-FASH-0000013 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
