/* JAH interactive demo program — jahdb-demo-1.0
 * Database: fashion · Record: JAH-FASH-0000003 · Pattern piece: Bodice Front
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"patterns","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Pattern piece: Bodice Front","topic":"pattern piece","garment":{"(object keys)":["piece","use"]},"source_ref":"Fashion reference (verified 2026-10-09)","description":"The bodice front pattern piece: The front of a fitted top. Accurate pieces with seam allowance are the foundation of fit. Filed as a complete searchable record in the JAH Data Bases archive, with its …","id":"JAH-FASH-0000003"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Pattern piece: Bodice Front ===");
console.log("Record JAH-FASH-0000003 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
