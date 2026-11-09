/* JAH interactive demo program — jahdb-demo-1.0
 * Database: embedding-chunks · Record: JAH-CHUNK-000006 · Time Zones · JAH General Reference
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-CHUNK-000006","chunk_id":"JAH-CHUNK-000006","text":"Time zones divide Earth into regions sharing a standard time. They exist because the planet rotates: noon arrives at different moments around the globe. Most zones differ by whole hours from UTC, thou…","token_count":79,"source_doc":"JAH General Reference","section":"Time Zones","keywords":"[array ×3]","embedding_model":"jah-embed-1.0","domain":"general","title":"Time Zones · JAH General Reference"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Time Zones · JAH General Reference ===");
console.log("Record JAH-CHUNK-000006 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
