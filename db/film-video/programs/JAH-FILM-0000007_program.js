/* JAH interactive demo program — jahdb-demo-1.0
 * Database: film-video · Record: JAH-FILM-0000007 · Bird’s-Eye View from a Shoulder Level angle
 * Interactive record inspector: tours every field, with a searchable field index.
 * RUN ON PC: save as demo.js, then run:  node demo.js
 * RUN IN BROWSER: press F12, paste this program into the console, press Enter.
 * RUN IN-PAGE: open this record and press "Run interactive demo". */
(function(){
var FIELDS={"category":"shots","source":"online","creation_mode":"ONLINE-VERIFIED","title":"Bird’s-Eye View from a Shoulder Level angle","topic":"shot setup","shot":{"(object keys)":["shot","angle","framing","effect"]},"source_ref":"https://www.adobe.com/vn_en/creativecloud/video/production/cinematography/camera-shots-and-angles.html","description":"A bird’s-eye view played from a shoulder level angle. Conversational realism at standing height. Combined with godlike detachment. A standard, verifiable camera setup.","id":"JAH-FILM-0000007"};
var keys=Object.keys(FIELDS);
function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}
function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \""+word+"\": "+(hits.join(", ")||"(none)"));return hits;}
console.log("=== Bird’s-Eye View from a Shoulder Level angle ===");
console.log("Record JAH-FILM-0000007 · "+keys.length+" fields:");
keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});
console.log("--- field tour ---");
keys.forEach(function(k,i){show(i);});
try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}
console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\"word\")");
})();
