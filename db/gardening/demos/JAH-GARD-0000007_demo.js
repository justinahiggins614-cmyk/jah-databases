/* JAH interactive demo program — jahdb-demo-1.0
 * Database: gardening · Record: JAH-GARD-0000007 · Broccoli — Plant profile
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"id":"JAH-GARD-0000007","title":"Broccoli — Plant profile","subject":"Broccoli","category":"vegetables","record_type":"profile","source":"online","source_ref":"https://aggie-horticulture.tamu.edu/wp-content/uploads/sites/12/2011/03/E-502_home_vegetable_guide.pdf","creation_mode":"ONLINE-CURATED","summary":"Broccoli is a vegetable for cool season planting, originating in Italy. Needs: Cool; fertile loam; even water. Cool-season heads maturing in 50–85 days. Field: brassica.","facts":{"(object keys)":["j","y","k","a","cite"]},"key_points":"[array ×4]","guidance":"General information only, not professional horticultural advice. Adjust for your USDA hardiness zone."};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Broccoli — Plant profile ===");
console.log("Record JAH-GARD-0000007 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
