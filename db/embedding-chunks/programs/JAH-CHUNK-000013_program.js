/* JAH interactive demo program — jahdb-demo-1.0
 * Database: embedding-chunks · Record: JAH-CHUNK-000013 · States of Matter · JAH Science Compendium Vol. 1
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CHUNK-000013","chunk_id":"JAH-CHUNK-000013","text":"Matter commonly exists as solid, liquid, gas, or plasma. In solids, particles are locked in fixed positions and vibrate in place. Liquids flow because particles slide past one another while staying cl…","token_count":78,"source_doc":"JAH Science Compendium Vol. 1","section":"States of Matter","keywords":"[array ×3]","embedding_model":"jah-embed-1.0","domain":"science","title":"States of Matter · JAH Science Compendium Vol. 1"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== States of Matter · JAH Science Compendium Vol. 1 ===");
console.log("Record JAH-CHUNK-000013 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
