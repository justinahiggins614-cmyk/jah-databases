/* JAH interactive demo program — jahdb-demo-1.0
 * Database: graphic-design · Record: JAH-DES-0000006 · Analogous palette on Blue — poster design
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"color","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Analogous palette on Blue — poster design","topic":"color harmony","palette":"[array ×3]","spec":{"(object keys)":["base_hue_deg","base_hue_name","harmony","offsets","saturation","lightness","geometry","mood"]},"source_ref":"https://inventivehq.com/blog/color-harmonies-guide-web-design","description":"A analogous palette built on Blue (230 degrees) for poster design. Neighboring hues that feel calm and cohesive. The swatches are #2c4add, #2ca2dd, #672cdd. Serene and unified; pick one hue to lead.","id":"JAH-DES-0000006"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Analogous palette on Blue — poster design ===");
console.log("Record JAH-DES-0000006 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
